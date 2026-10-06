"""H1 VitalDB, test of G12: checks of the analysis code on synthetic series only (pre-registration Section 9,
step 3). No VitalDB data is used. Each scenario writes a synthetic dataset in the VitalDB layout the analysis
reads, runs the count and the analysis unchanged, and compares the verdict with the one the scenario was
built to produce.

Generators:
- noise: an AR(1) process on 10-s bins around 80 mmHg. "warning": the coefficient rises from 0.5 to 0.95 over
  the 30 minutes before the fall (innovations fixed, so variance rises too). "none": constant 0.5, then a
  sudden fall (a switch). "reverse": the coefficient falls from 0.9 to 0.3 before the fall.
- engine: the TQ engine (theory/sim/tq_core.py, the TQ9 G12 set-up with a slower load ramp). Pressure
  deviation = -2 mmHg x the record deficit left by small knocks, one engine step per 10 s. "taper": reserve
  with a knee (0.5); "switch": no knee, the switch fires. Control periods: the same engine with no overload.

Every case carries artefacts the cleaning must handle: flush spikes (SBP 300), short and long gaps.

Usage: python h1_vdb_g12_synthetic.py [--work DIR]
"""
import argparse
import gzip
import json
import os
import random
import shutil
import sys
import tempfile

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "theory", "sim"))
import h1_vdb_g12 as A  # noqa: E402

OUT = os.path.join(HERE, "..", "results", "H1-VDB-synthetic")
BASE = 80.0


# ---------------------------------------------------------------- generators (10-s bins, deviation from BASE)
def ar_series(rng, n, phi, sigma=2.0, x0=0.0):
    phi = np.broadcast_to(phi, (n,))
    x = np.empty(n)
    prev = x0
    for i in range(n):
        prev = phi[i] * prev + sigma * rng.standard_normal()
        x[i] = prev
    return np.clip(x, -12, 12)


def noise_pre(rng, kind, n=240):
    """The 40 minutes before the fall."""
    if kind == "warning":
        phi = np.r_[np.full(n - 180, 0.5), np.linspace(0.5, 0.95, 180)]
    elif kind == "reverse":
        phi = np.r_[np.full(n - 180, 0.9), np.linspace(0.9, 0.3, 180)]
    else:
        phi = np.full(n, 0.5)
    return ar_series(rng, n, phi)


def engine_series(seed, knee, switch, overload, steps):
    import tq_core as core
    rng = random.Random(seed)
    kn = [rng.expovariate(1 / 1.5) if rng.random() < 0.4 else 0.0 for _ in range(steps)]
    top_d = (lambda t: 20.0 + min(8.0, 0.012 * t)) if overload else (lambda t: 20.0)
    P = [core.Part("Top", 5, 22.0, top_d, renewable=False, vital=1.0),
         core.Part("Base", 2, 50.0, 50.0, vital=0.6, rebuild=20.0)]
    R = core.Reserve(level=300.0, max=300.0, release=10.0, knee=knee)
    sw = core.Switch(at=0.15, shed=0.5, release_at=0.4) if switch else None
    rows, _ = core.run(P, R, steps, labelled=True, adapt=True, priority="computed", economise=False,
                       switch=sw, knocks=lambda t: kn[t])
    brk = next((r["t"] for r in rows if r["record"] < 0.99 or r["switch_on"]), None) if overload else None
    dev = np.array([-2.0 * r["rec_deficit"] for r in rows])
    return dev, brk


def engine_pre(seed, kind, n=240):
    dev, brk = engine_series(seed, 0.5 if kind == "taper" else 0.0, kind == "switch", True, 900)
    if brk is None or brk < n:
        raise RuntimeError(f"engine break too early or absent (seed {seed}, {kind}: {brk})")
    return np.clip(dev[brk - n:brk], -12, 12)


def engine_stable(seed, n):
    dev, _ = engine_series(seed + 10_000, 0.5, False, False, n)
    return np.clip(dev, -12, 12)


# ---------------------------------------------------------------- one synthetic case
def build_case(rng, pre, stable_fn, break_in_second_half=True):
    """10-s MAP bins for a whole surgery: stable 100 min, the 40-min approach, the fall, stable 75 min."""
    head = 600 if break_in_second_half else 30
    fall = np.r_[np.linspace(BASE + pre[-1], 55, 6), np.full(30, 55.0), np.linspace(55, BASE, 12)]
    tail = 450
    bins = np.r_[BASE + stable_fn(head), BASE + pre, fall, BASE + stable_fn(tail)]
    return bins


def write_case(rng, cid, bins, files, tracks, labs, hb_fall, infusion_change, t_open=600.0):
    n2 = len(bins) * 5
    t = t_open + np.arange(n2) * 2.0
    mbp = np.repeat(bins, 5) + 0.5 * rng.standard_normal(n2)
    sbp = mbp + 30 + rng.standard_normal(n2)
    dbp = mbp - 15 + rng.standard_normal(n2)
    hr = 70 - 0.5 * (mbp - BASE) + rng.standard_normal(n2)
    keep = np.ones(n2, bool)
    for _ in range(3):                       # flush spikes: 16 s of SBP 300 (invalid, longer than gap fill)
        i = rng.integers(0, n2 - 8)
        sbp[i:i + 8] = 300.0
    for _ in range(20):                      # single dropped rows (short gaps, filled)
        keep[rng.integers(0, n2)] = False
    i = rng.integers(0, 600)                 # one long gap early in surgery
    keep[i:i + 40] = False
    for name, v in (("Solar8000/ART_MBP", mbp), ("Solar8000/ART_SBP", sbp), ("Solar8000/ART_DBP", dbp),
                    ("Solar8000/HR", hr)):
        tid = f"{cid}_{name.replace('/', '_')}"
        tracks.append(dict(caseid=cid, tname=name, tid=tid))
        files[tid] = pd.DataFrame({"Time": t[keep], name: v[keep]})
    if infusion_change is not None:
        name = "Orchestra/PHEN_RATE"
        tid = f"{cid}_PHEN"
        tracks.append(dict(caseid=cid, tname=name, tid=tid))
        tt = np.arange(t_open, t[-1], 1.0)
        rate = np.where(tt >= infusion_change, 10.0, 5.0)
        files[tid] = pd.DataFrame({"Time": tt, name: rate})
    for k, frac in enumerate((0.2, 0.45, 0.7)):
        labs.append(dict(caseid=cid, dt=t_open + frac * len(bins) * 10, name="hb",
                         result=12.0 - (k * 1.2 if hb_fall else 0.0)))
    return t_open, t_open + len(bins) * 10 - 10


def scenario(name, work, high_kind, low_kind, n_high=25, n_low=25, gen="noise", seed=1, extras=True):
    rng = np.random.default_rng(seed)
    root = os.path.join(work, name)
    if os.path.exists(root):
        shutil.rmtree(root)
    os.makedirs(os.path.join(root, "tracks"))
    cases, tracks, labs, files = [], [], [], {}
    cid = 0

    def add(kind, share, phe=0.0, second_half=True, short=False, infusion=False):
        nonlocal cid
        cid += 1
        if gen == "noise":
            pre = noise_pre(rng, kind)
            stable_fn = lambda n: ar_series(rng, n, 0.5)
        else:
            pre = engine_pre(cid, kind)
            stable_fn = lambda n: engine_stable(int(rng.integers(0, 10**6)), n)
        bins = build_case(rng, pre, stable_fn, second_half)
        if short:
            bins = bins[:500]
        t_brk = 600.0 + (600 if second_half else 30) * 10 + 240 * 10
        opstart, opend = write_case(rng, cid, bins, files, tracks, labs, hb_fall=share > 0.1,
                                    infusion_change=(t_brk - 900) if infusion else None)
        weight = 70.0
        cases.append(dict(caseid=cid, sex="M", weight=weight, ane_type="General", opstart=opstart, opend=opend,
                          intraop_ebl=share * 70 * weight, intraop_phe=phe, intraop_eph=0.0, intraop_epi=0.0))

    for i in range(n_high):
        add(high_kind, 0.25, infusion=(i < 3))
    for _ in range(n_low):
        add(low_kind, 0.03)
    if extras:
        add(high_kind, 0.25, phe=100.0)          # bolus: excluded from the primary cohort
        add(high_kind, 0.25, short=True)         # surgery too short
        add(high_kind, 0.10)                     # loss between groups
        add(high_kind, 0.25, second_half=False)  # fall in the first half: not qualifying
        cases.append(dict(caseid=999, sex="M", weight=70.0, ane_type="General", opstart=600, opend=20000,
                          intraop_ebl=2000.0, intraop_phe=None, intraop_eph=0.0, intraop_epi=0.0))  # missing bolus field
    pd.DataFrame(cases).to_csv(os.path.join(root, "cases.csv"), index=False)
    pd.DataFrame(tracks).to_csv(os.path.join(root, "trks.csv"), index=False)
    pd.DataFrame(labs).to_csv(os.path.join(root, "labs.csv"), index=False)
    for tid, df in files.items():
        with gzip.open(os.path.join(root, "tracks", f"{tid}.csv.gz"), "wt") as f:
            df.to_csv(f, index=False)
    out = os.path.join(OUT, name)
    dec = A.cmd_count(root, out)
    summ = A.cmd_analyse(root, out)
    return dec, summ


# ---------------------------------------------------------------- unit checks
def unit_checks():
    res = {}
    x = np.array([1, np.nan, np.nan, 4, np.nan] + [np.nan] * 6 + [5.0])
    f = A.gap_fill(x, 5)
    res["gap_fill_short_run_interpolated"] = bool(np.allclose(f[:4], [1, 2, 3, 4]))
    res["gap_fill_long_run_left"] = bool(np.isnan(f[4:11]).all())
    m = A.clean_map(np.array([80, 80, 10, 80.0]), np.array([110, 300.5, 40, 85.0]),
                    np.array([65, 65, 5, 80.0]))
    res["artefact_rule"] = bool(np.isfinite(m[0]) and np.isnan(m[1:]).all())
    rng = np.random.default_rng(0)
    xs = ar_series(rng, 6000, 0.7, sigma=1.0)
    res["ar1_recovers_0.7"] = bool(abs(A.ar1(xs) - 0.7) < 0.03)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", default=None)
    a = ap.parse_args()
    work = a.work or tempfile.mkdtemp(prefix="h1vdb_synth_")
    expected = [
        ("S1_noise_warning_vs_none", "warning", "none", dict(), "Supported"),
        ("S2_noise_none_both", "none", "none", dict(), "Fails"),
        ("S3_noise_warning_both", "warning", "warning", dict(), "Narrowed"),
        ("S4_noise_reverse", "reverse", "none", dict(), "Contradicted"),
        ("S5_too_few_high", "warning", "none", dict(n_high=12), "not runnable"),
        ("S6_engine_taper_vs_switch", "taper", "switch", dict(gen="engine"), "Supported"),
        ("S7_engine_switch_both", "switch", "switch", dict(gen="engine"), "Fails"),
    ]
    report = dict(unit_checks=unit_checks(), scenarios=[])
    for name, hk, lk, kw, exp in expected:
        dec, summ = scenario(name, work, hk, lk, **kw)
        prim = summ.get("primary", {})
        report["scenarios"].append(dict(
            scenario=name, expected=exp, got=summ["verdict"], match=summ["verdict"] == exp,
            cohort=dec.get("cohort"), high_threshold=dec.get("high_threshold"),
            n_high=prim.get("n_high"), n_low=prim.get("n_low"),
            P1=prim.get("P1"), P2=prim.get("P2"), P3=prim.get("P3"),
            G1=summ.get("G1_check"), sensitivity_verdicts={k: v["verdict"] for k, v in summ.get("sensitivity", {}).items()}))
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "synthetic_report.json"), "w") as f:
        json.dump(report, f, indent=2, default=float)
    print(json.dumps(dict(unit_checks=report["unit_checks"],
                          scenarios=[(s["scenario"], s["expected"], s["got"], s["n_high"], s["n_low"])
                                     for s in report["scenarios"]]), indent=1))


if __name__ == "__main__":
    main()
