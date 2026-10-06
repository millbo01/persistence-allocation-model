"""H1 VitalDB, test of G12: analysis code.

Implements the frozen pre-registration: tests/H1 VitalDB G12 - pre-registration.md (frozen 6 October 2026,
SHA-256 begins 371caf3c). Written before any VitalDB data was opened; tested only on synthetic series
(tests/scripts/h1_vdb_g12_synthetic.py).

Usage (in order; the count must run before the analysis):
    python h1_vdb_g12.py count   [--data DIR] [--out DIR]
    python h1_vdb_g12.py analyse [--data DIR] [--out DIR]

Data layout (written by h1_vdb_download.py, or by the synthetic builder):
    DIR/cases.csv     one row per case; the documented clinical fields (caseid, sex, weight, ane_type,
                      opstart, opend, intraop_ebl, intraop_phe, intraop_eph, intraop_epi)
    DIR/labs.csv      caseid, dt, name, result
    DIR/trks.csv      caseid, tname, tid
    DIR/tracks/<tid>.csv.gz   two columns: time (s from casestart), value

Implementation details not fixed by the pre-registration, fixed here before data (each logged in
summary.json under implementation_notes):
"""
import argparse
import gzip
import hashlib
import json
import os
import sys

import numpy as np
import pandas as pd
from scipy import stats

IMPLEMENTATION_NOTES = [
    "Each 2-second numeric sample is placed on a 2-s grid from opstart (nearest grid point within 1 s; "
    "several samples at one point are averaged).",
    "A mean-pressure sample is valid only if systolic and diastolic are present at the same grid point and "
    "the artefact rule passes (MAP 20 to 200, SBP <= 300, SBP - DBP >= 10). Conservative: a MAP without "
    "SBP and DBP cannot be checked and is invalid.",
    "Gap filling: runs of up to 5 consecutive missing grid points (10 s) with valid points on both sides "
    "are linearly interpolated.",
    "Window usability (more than 10% invalid or missing) is measured on the 2-s grid after gap filling.",
    "10-second bins are the mean of the valid grid points in the bin; a bin with none is missing. A "
    "missing bin breaks a run below 65 mmHg, and is not counted as below 65 in the stable-approach rule.",
    "Inside a usable window, missing 10-s bins are linearly interpolated (ends: nearest value) before "
    "detrending.",
    "AR1 is the Pearson correlation of the detrended residuals with themselves lagged by one bin; SD uses "
    "ddof = 1.",
    "Control pseudo-onsets: t* = midpoint of surgery + k x 300 s, with t* - 31 min >= opstart and "
    "t* + 30 min <= opend.",
    "Missing intraop_phe, intraop_eph or intraop_epi is not taken as zero: the case is excluded from the "
    "primary cohort (it may enter the fallback cohort).",
    "ane_type is matched case-insensitively on the word 'general'.",
    "Fallback bolus signature: within either measurement window, any 10-s bin more than 15 mmHg above the "
    "minimum of the six bins before it (within the window).",
    "Infusion sensitivity: a change is any difference between successive recorded rates of PHEN, NEPI, "
    "EPI, VASO, DOPA or DOBU from the last sample before t0 - 31 min to t0.",
    "G1 baseline: median of valid (unfilled) mean pressure from opstart to opstart + 10 min. Pressure at "
    "an hb sample: median of valid mean pressure in the 5 min before it.",
    "G18: Pearson correlation of detrended MAP and detrended HR (Solar8000/HR valid 20 to 250) in each "
    "window; the same with stroke volume (Vigileo/SV or EV1000/SV, valid 5 to 250) where present.",
]

GRID = 2.0
BIN = 10.0
PTS_PER_BIN = int(BIN / GRID)
HYPO = 65.0
APPROACH = 31 * 60
CONTROL_AFTER = 30 * 60
WIN = 10 * 60
EARLY_START, EARLY_END = 31 * 60, 21 * 60
MIN_CASES = 20
EBV_ML_PER_KG = {"M": 70.0, "F": 65.0}
INFUSION_DRUGS = ("PHEN", "NEPI", "EPI", "VASO", "DOPA", "DOBU")
TRACKS = dict(mbp="Solar8000/ART_MBP", sbp="Solar8000/ART_SBP", dbp="Solar8000/ART_DBP",
              hr="Solar8000/HR", sv1="Vigileo/SV", sv2="EV1000/SV")

PRIMARY = dict(gapfill_pts=5, sustain_bins=6, late_end=60, fallback=False)


# ---------------------------------------------------------------- loading
class Data:
    def __init__(self, root):
        self.root = root
        self.cases = pd.read_csv(os.path.join(root, "cases.csv"))
        self.labs = pd.read_csv(os.path.join(root, "labs.csv"))
        for f in ("caseid", "dt", "result"):
            self.labs[f] = pd.to_numeric(self.labs[f], errors="coerce")
        self.trks = pd.read_csv(os.path.join(root, "trks.csv"))
        self._tid = {(int(r.caseid), r.tname): r.tid for r in self.trks.itertuples()}

    def has(self, caseid, tname):
        return (int(caseid), tname) in self._tid

    def track(self, caseid, tname):
        tid = self._tid.get((int(caseid), tname))
        if tid is None:
            return None
        path = os.path.join(self.root, "tracks", f"{tid}.csv.gz")
        if not os.path.exists(path):
            return None
        df = pd.read_csv(path, compression="gzip")
        df = df.iloc[:, :2]
        df.columns = ["t", "v"]
        df = df.dropna()
        return df["t"].to_numpy(float), df["v"].to_numpy(float)


# ---------------------------------------------------------------- signal handling
def to_grid(t, v, t_start, n):
    """Place samples on the 2-s grid; NaN where none."""
    out = np.full(n, np.nan)
    if t is None or len(t) == 0:
        return out
    idx = np.rint((t - t_start) / GRID).astype(np.int64)
    ok = (idx >= 0) & (idx < n) & (np.abs(t - (t_start + idx * GRID)) <= GRID / 2 + 1e-9)
    if not ok.any():
        return out
    s = pd.Series(v[ok]).groupby(idx[ok]).mean()
    out[s.index.to_numpy()] = s.to_numpy()
    return out


def gap_fill(x, max_pts):
    """Linearly interpolate runs of NaN of length <= max_pts that have valid values on both sides."""
    x = x.copy()
    if max_pts <= 0:
        return x
    isn = np.isnan(x)
    n = len(x)
    i = 0
    while i < n:
        if isn[i]:
            j = i
            while j < n and isn[j]:
                j += 1
            if i > 0 and j < n and (j - i) <= max_pts:
                x[i:j] = np.interp(np.arange(i, j), [i - 1, j], [x[i - 1], x[j]])
            i = j
        else:
            i += 1
    return x


def clean_map(mbp, sbp, dbp):
    ok = (~np.isnan(mbp) & ~np.isnan(sbp) & ~np.isnan(dbp)
          & (mbp >= 20) & (mbp <= 200) & (sbp <= 300) & ((sbp - dbp) >= 10))
    return np.where(ok, mbp, np.nan)


def clean_range(x, lo, hi):
    return np.where(~np.isnan(x) & (x >= lo) & (x <= hi), x, np.nan)


def bins(x):
    nb = len(x) // PTS_PER_BIN
    b = x[:nb * PTS_PER_BIN].reshape(nb, PTS_PER_BIN)
    with np.errstate(all="ignore"):
        cnt = (~np.isnan(b)).sum(1)
        m = np.where(cnt > 0, np.nansum(b, 1) / np.maximum(cnt, 1), np.nan)
    return m


class Case:
    """One case's signals on a common clock from opstart."""

    def __init__(self, row, data, gapfill_pts):
        self.id = int(row.caseid)
        self.opstart = float(row.opstart)
        self.opend = float(row.opend)
        self.mid = (self.opstart + self.opend) / 2
        n = int((self.opend - self.opstart) // GRID) + 1
        self.n = n
        g = {k: to_grid(*(data.track(self.id, tn) or (None, None)), self.opstart, n)
             for k, tn in TRACKS.items()}
        raw = clean_map(g["mbp"], g["sbp"], g["dbp"])
        self.map_raw = raw
        self.map = gap_fill(raw, gapfill_pts)
        self.map_bins = bins(self.map)
        hr = gap_fill(clean_range(g["hr"], 20, 250), gapfill_pts)
        self.hr = hr
        self.hr_bins = bins(hr)
        sv = g["sv1"] if np.isfinite(g["sv1"]).any() else g["sv2"]
        sv = gap_fill(clean_range(sv, 5, 250), gapfill_pts)
        self.sv = sv
        self.sv_bins = bins(sv)
        self.data = data

    # times in seconds from casestart
    def bin_index(self, t):
        return int(round((t - self.opstart) / BIN))

    def grid_slice(self, a, b):
        return slice(int(round((a - self.opstart) / GRID)), int(round((b - self.opstart) / GRID)))

    def window(self, a, b, which="map"):
        """10-s bins for [a, b), or None if unusable (more than 10% of the 2-s grid missing)."""
        if a < self.opstart or b > self.opend:
            return None
        grid = getattr(self, which)[self.grid_slice(a, b)]
        if len(grid) == 0 or np.isnan(grid).mean() > 0.10:
            return None
        bb = getattr(self, which + "_bins")[self.bin_index(a):self.bin_index(b)]
        if len(bb) != int(round((b - a) / BIN)):
            return None
        if np.isnan(bb).any():
            idx = np.arange(len(bb))
            ok = ~np.isnan(bb)
            if ok.sum() < 3:
                return None
            bb = np.interp(idx, idx[ok], bb[ok])
        return bb


def detrend(x):
    i = np.arange(len(x))
    p = np.polyfit(i, x, 1)
    return x - np.polyval(p, i)


def ar1(x):
    r = detrend(x)
    a, b = r[:-1], r[1:]
    if a.std() < 1e-12 or b.std() < 1e-12:
        return np.nan
    return float(np.corrcoef(a, b)[0, 1])


def sd(x):
    s = float(np.std(detrend(x), ddof=1))
    return s if s > 1e-12 else np.nan


def xcorr(x, y):
    a, b = detrend(x), detrend(y)
    if a.std() < 1e-12 or b.std() < 1e-12:
        return np.nan
    return float(np.corrcoef(a, b)[0, 1])


def bolus_signature(x):
    for i in range(1, len(x)):
        if x[i] - x[max(0, i - 6):i].min() > 15.0:
            return True
    return False


def pair_windows(case, t, late_end, which="map"):
    L = case.window(t - (WIN + late_end), t - late_end, which)
    E = case.window(t - EARLY_START, t - EARLY_END, which)
    return E, L


def pair_measures(E, L):
    m = dict(ar1_E=ar1(E), ar1_L=ar1(L), sd_E=sd(E), sd_L=sd(L))
    m["d_ar1"] = m["ar1_L"] - m["ar1_E"]
    m["d_lnsd"] = (np.log(m["sd_L"]) - np.log(m["sd_E"])) if (m["sd_E"] > 0 and m["sd_L"] > 0) else np.nan
    for k in ("E", "L"):
        a = m["ar1_" + k]
        m["rec_" + k] = float(-BIN / np.log(a)) if (a is not None and 0 < a < 1) else np.nan
    return m


def stable(case, a, b):
    bb = case.map_bins[max(0, case.bin_index(a)):case.bin_index(b)]
    bb = bb[~np.isnan(bb)]
    return len(bb) > 0 and bool((bb >= HYPO).all())


def candidate_breaks(case, sustain_bins):
    """Onsets (s from casestart) of runs of >= sustain_bins consecutive bins below 65 mmHg."""
    below = ~np.isnan(case.map_bins) & (case.map_bins < HYPO)
    out, i, n = [], 0, len(below)
    while i < n:
        if below[i]:
            j = i
            while j < n and below[j]:
                j += 1
            if j - i >= sustain_bins:
                out.append(case.opstart + i * BIN)
            i = j
        else:
            i += 1
    return out


def first_qualifying_break(case, p):
    for t0 in candidate_breaks(case, p["sustain_bins"]):
        if not (case.mid < t0 < case.opend):
            continue
        if t0 - APPROACH < case.opstart:
            continue
        if not stable(case, t0 - APPROACH, t0):
            continue
        E, L = pair_windows(case, t0, p["late_end"])
        if E is None or L is None:
            continue
        if p["fallback"] and (bolus_signature(E) or bolus_signature(L)):
            continue
        return t0, E, L
    return None


def control_pairs(case, p):
    out = []
    k = 0
    while True:
        ts = case.mid + k * 300.0
        k += 1
        if ts + CONTROL_AFTER > case.opend:
            break
        if ts - APPROACH < case.opstart:
            continue
        if not stable(case, ts - APPROACH, ts + CONTROL_AFTER):
            continue
        E, L = pair_windows(case, ts, p["late_end"])
        if E is None or L is None:
            continue
        if p["fallback"] and (bolus_signature(E) or bolus_signature(L)):
            continue
        out.append((ts, E, L))
    return out


def infusion_changed(data, caseid, t0):
    for d in INFUSION_DRUGS:
        tr = data.track(caseid, f"Orchestra/{d}_RATE")
        if tr is None:
            continue
        t, v = tr
        a = t0 - APPROACH
        before = np.where(t < a)[0]
        sel = (t >= a) & (t <= t0)
        vals = list(v[sel])
        if len(before):
            vals = [v[before[-1]]] + vals
        if len(vals) >= 2 and np.any(np.diff(np.array(vals)) != 0):
            return True
    return False


# ---------------------------------------------------------------- cohort
def ebv_share(row):
    k = EBV_ML_PER_KG.get(str(row.sex).strip().upper()[:1])
    if k is None or not np.isfinite(row.weight) or row.weight <= 0 or not np.isfinite(row.intraop_ebl):
        return np.nan
    return row.intraop_ebl / (k * row.weight)


def eligible_cases(data, fallback):
    c = data.cases.copy()
    for f in ("weight", "intraop_ebl", "opstart", "opend", "intraop_phe", "intraop_eph", "intraop_epi"):
        c[f] = pd.to_numeric(c[f], errors="coerce")
    keep = c["ane_type"].astype(str).str.lower().str.contains("general")
    keep &= c.apply(lambda r: all(data.has(r.caseid, TRACKS[k]) for k in ("mbp", "sbp", "dbp")), axis=1)
    keep &= c["intraop_ebl"].notna() & c["weight"].notna() & c["sex"].notna()
    keep &= (c["opend"] - c["opstart"]) >= 90 * 60
    if not fallback:
        for f in ("intraop_phe", "intraop_eph", "intraop_epi"):
            keep &= c[f].notna() & (c[f] == 0)
    c = c[keep].copy()
    c["ebv_share"] = c.apply(ebv_share, axis=1)
    return c[c["ebv_share"].notna()]


def process(data, cases, p):
    """Per case: first qualifying break and control pairs. Returns dict caseid -> result (or None)."""
    out = {}
    for row in cases.itertuples():
        case = Case(row, data, p["gapfill_pts"])
        br = first_qualifying_break(case, p)
        ctl = control_pairs(case, p)
        out[int(row.caseid)] = dict(case=case, ebv_share=float(row.ebv_share), brk=br, ctl=ctl)
    return out


def qualifies(r):
    return r["brk"] is not None and len(r["ctl"]) > 0


def group_ids(res, hi_thr):
    hi = [cid for cid, r in res.items() if r["ebv_share"] >= hi_thr and qualifies(r)]
    lo = [cid for cid, r in res.items() if r["ebv_share"] <= 0.05 and qualifies(r)]
    return hi, lo


def decide_cohort(data):
    """The count step: decide threshold and cohort from counts only (Section 2)."""
    log = []
    for fallback in (False, True):
        cases = eligible_cases(data, fallback)
        p = dict(PRIMARY, fallback=fallback)
        res = process(data, cases[(cases.ebv_share >= 0.15) | (cases.ebv_share <= 0.05)], p)
        for thr in (0.20, 0.15):
            hi, lo = group_ids(res, thr)
            log.append(dict(cohort="fallback" if fallback else "primary", high_threshold=thr,
                            eligible_cases=int(len(cases)), high_qualifying=len(hi), low_qualifying=len(lo)))
            if len(lo) < MIN_CASES:
                break
            if len(hi) >= MIN_CASES:
                return dict(runnable=True, cohort="fallback" if fallback else "primary",
                            high_threshold=thr, counts=log)
    return dict(runnable=False, counts=log)


# ---------------------------------------------------------------- scores and tests
def case_scores(r, measure="d_ar1"):
    _, E, L = r["brk"]
    b = pair_measures(E, L)[measure]
    c = np.nanmedian([pair_measures(E2, L2)[measure] for _, E2, L2 in r["ctl"]])
    return float(b - c), float(b), float(c)


def wilcoxon_greater(x):
    x = np.asarray([v for v in x if np.isfinite(v)])
    if len(x) < 2 or np.all(x == 0):
        return dict(n=int(len(x)), median=float(np.median(x)) if len(x) else None, p=None)
    return dict(n=int(len(x)), median=float(np.median(x)),
                p=float(stats.wilcoxon(x, alternative="greater").pvalue),
                p_two_sided=float(stats.wilcoxon(x).pvalue))


def mwu_greater(a, b):
    a = [v for v in a if np.isfinite(v)]
    b = [v for v in b if np.isfinite(v)]
    if len(a) < 2 or len(b) < 2:
        return dict(n_high=len(a), n_low=len(b), p=None)
    return dict(n_high=len(a), n_low=len(b), median_high=float(np.median(a)), median_low=float(np.median(b)),
                p=float(stats.mannwhitneyu(a, b, alternative="greater").pvalue))


def verdict(P1, P2):
    if P1.get("p") is None:
        return "not computable"
    if P1["median"] < 0 and P1.get("p_two_sided") is not None and P1["p_two_sided"] < 0.05:
        return "Contradicted"
    p1 = P1["p"] < 0.05 and P1["median"] > 0
    if not p1:
        return "Fails"
    p2 = P2.get("p") is not None and P2["p"] < 0.05
    return "Supported" if p2 else "Narrowed"


def run_tests(res, hi, lo):
    dh = [case_scores(res[c])[0] for c in hi]
    dl = [case_scores(res[c])[0] for c in lo]
    sh = [case_scores(res[c], "d_lnsd")[0] for c in hi]
    P1 = wilcoxon_greater(dh)
    P2 = mwu_greater(dh, dl)
    P3 = wilcoxon_greater(sh)
    return dict(P1=P1, P2=P2, P3=P3, verdict=verdict(P1, P2))


def g1_check(data, res, ids):
    labs = data.labs
    labs = labs[labs["name"].astype(str).str.lower() == "hb"]
    rows = []
    for cid in ids:
        r = res[cid]
        case = r["case"]
        base = case.map_raw[case.grid_slice(case.opstart, case.opstart + 600)]
        base = base[~np.isnan(base)]
        if len(base) == 0:
            continue
        b = float(np.median(base))
        tend = r["brk"][0] if r["brk"] else case.opend
        hb = labs[(labs.caseid == cid) & (labs.dt > case.opstart) & (labs.dt < tend)].sort_values("dt")
        pts = []
        for h in hb.itertuples():
            m = case.map_raw[case.grid_slice(max(case.opstart, h.dt - 300), h.dt)]
            m = m[~np.isnan(m)]
            if len(m) and np.isfinite(h.result):
                pts.append((float(np.median(m)), float(h.result)))
        if len(pts) < 2:
            continue
        within = all(abs(m / b - 1) <= 0.20 for m, _ in pts)
        fell = pts[-1][1] < pts[0][1]
        rows.append(within and fell)
    frac = float(np.mean(rows)) if rows else None
    return dict(cases_with_two_hb=len(rows), share_consistent=frac,
                consistent=(frac is not None and frac > 0.5))


def g18(res, ids, late_end, which):
    d = []
    for cid in ids:
        r = res[cid]
        case = r["case"]

        def dc(t, E, L):
            Eo, Lo = pair_windows(case, t, late_end, which)
            if Eo is None or Lo is None:
                return np.nan
            return xcorr(L, Lo) - xcorr(E, Eo)
        t0, E, L = r["brk"]
        b = dc(t0, E, L)
        c = np.nanmedian([dc(t, E2, L2) for t, E2, L2 in r["ctl"]] or [np.nan])
        if np.isfinite(b) and np.isfinite(c):
            d.append(b - c)
    return dict(n=len(d), median_excess_change_in_correlation=float(np.median(d)) if d else None)


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


# ---------------------------------------------------------------- commands
def cmd_count(data_dir, out):
    data = Data(data_dir)
    dec = decide_cohort(data)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "counts.json"), "w") as f:
        json.dump(dict(code_sha256=sha(__file__), **dec), f, indent=2)
    print(json.dumps(dec, indent=2))
    return dec


def analyse(data, dec, extra=None):
    fb = dec["cohort"] == "fallback"
    thr = dec["high_threshold"]
    p = dict(PRIMARY, fallback=fb, **(extra or {}))
    cases = eligible_cases(data, fb)
    res = process(data, cases[(cases.ebv_share >= min(thr, 0.15)) | (cases.ebv_share <= 0.05)], p)
    hi, lo = group_ids(res, thr)
    return res, hi, lo, p


def cmd_analyse(data_dir, out):
    cpath = os.path.join(out, "counts.json")
    if not os.path.exists(cpath):
        sys.exit("counts.json not found: run the count step first (pre-registration Section 2).")
    dec = json.load(open(cpath))
    data = Data(data_dir)
    summary = dict(prereg="tests/H1 VitalDB G12 - pre-registration.md", prereg_sha256_begins="371caf3c",
                   code_sha256=sha(__file__), implementation_notes=IMPLEMENTATION_NOTES, counts=dec)
    if not dec["runnable"]:
        summary["verdict"] = "not runnable"
    else:
        res, hi, lo, p = analyse(data, dec)
        main = run_tests(res, hi, lo)
        summary["primary"] = dict(cohort=dec["cohort"], weight=0.5 if dec["cohort"] == "fallback" else 1.0,
                                  high_threshold=dec["high_threshold"], n_high=len(hi), n_low=len(lo), **main)
        summary["verdict"] = main["verdict"]
        summary["recovery_time_s_median"] = dict(
            E=float(np.nanmedian([pair_measures(res[c]["brk"][1], res[c]["brk"][2])["rec_E"] for c in hi])),
            L=float(np.nanmedian([pair_measures(res[c]["brk"][1], res[c]["brk"][2])["rec_L"] for c in hi])))
        sens = {}
        # 1: exclude breaks with an infusion-rate change in the approach
        hi1 = [c for c in hi if not infusion_changed(data, c, res[c]["brk"][0])]
        lo1 = [c for c in lo if not infusion_changed(data, c, res[c]["brk"][0])]
        sens["1_no_infusion_change"] = dict(n_high=len(hi1), n_low=len(lo1), **run_tests(res, hi1, lo1))
        for key, extra in (("2_no_gap_fill", dict(gapfill_pts=0)), ("3_sustained_5_min", dict(sustain_bins=30)),
                           ("5_late_window_ends_3_min", dict(late_end=180))):
            r2, h2, l2, _ = analyse(data, dec, extra)
            sens[key] = dict(n_high=len(h2), n_low=len(l2), **run_tests(r2, h2, l2))
        if dec["high_threshold"] == 0.20:
            h4, l4 = group_ids(res, 0.15)
            sens["4_high_at_15pct"] = dict(n_high=len(h4), n_low=len(l4), **run_tests(res, h4, l4))
        summary["sensitivity"] = sens
        all_hi = [c for c, r in res.items() if r["ebv_share"] >= dec["high_threshold"]]
        summary["G1_check"] = g1_check(data, res, all_hi)
        summary["G18_exploratory"] = dict(map_hr=g18(res, hi, p["late_end"], "hr"),
                                          map_sv=g18(res, hi, p["late_end"], "sv"))
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2, default=float)
    print(json.dumps({k: summary[k] for k in ("verdict",)}, indent=2))
    return summary


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=("count", "analyse"))
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("--data", default=os.path.join(here, "..", "..", "data", "vitaldb"))
    ap.add_argument("--out", default=os.path.join(here, "..", "results", "H1-VDB"))
    a = ap.parse_args()
    (cmd_count if a.cmd == "count" else cmd_analyse)(a.data, a.out)
