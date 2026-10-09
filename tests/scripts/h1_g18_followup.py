"""H1 G18 follow-up (exploratory, post hoc; James's v2 prompt, D5, 8 October 2026).

Not part of the H1 test and not scored. The frozen script tests/scripts/h1_vdb_g12.py is imported unchanged;
this script only reads its functions and the frozen counts.json, and re-runs the same cohort selection.

Question: the frozen G18 figure is the median, over high-loss cases, of
    [corr_L - corr_E at the break] - median over control times of [corr_L - corr_E],
where corr is the Pearson correlation of detrended MAP with detrended HR (or SV) in 10-s bins, E is the window
31 to 21 min before the break and L the window 11 to 1 min before it. A positive figure can mean the correlation
moved away from zero or towards it, depending on its sign. This script reports the raw correlations.

Usage: python tests/scripts/h1_g18_followup.py data/vitaldb tests/results/H1-VDB-G18-followup
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import h1_vdb_g12 as h1  # noqa: E402  (frozen; imported, not modified)


def corr_pair(case, t, late_end, which):
    E, L = h1.pair_windows(case, t, late_end, "map")
    Eo, Lo = h1.pair_windows(case, t, late_end, which)
    if E is None or L is None or Eo is None or Lo is None:
        return np.nan, np.nan
    return h1.xcorr(E, Eo), h1.xcorr(L, Lo)


def summarise(vals):
    v = np.array([x for x in vals if np.isfinite(x)])
    if len(v) == 0:
        return dict(n=0)
    return dict(n=int(len(v)), median=float(np.median(v)), q25=float(np.percentile(v, 25)),
                q75=float(np.percentile(v, 75)), share_negative=float(np.mean(v < 0)))


def main(data_dir, out):
    dec = json.load(open(os.path.join(os.path.dirname(HERE), "results", "H1-VDB", "counts.json")))
    data = h1.Data(data_dir)
    res, hi, lo, p = h1.analyse(data, dec)
    report = dict(note="Exploratory, post hoc, not scored. Frozen H1 code imported unchanged.",
                  frozen_code_sha256=h1.sha(h1.__file__), cohort=dec["cohort"], high_threshold=dec["high_threshold"],
                  n_high=len(hi), windows="E: 31 to 21 min before; L: 11 to 1 min before (10-s bins, detrended)")
    for which in ("hr", "sv"):
        rows = []
        for cid in hi:
            r = res[cid]
            case = r["case"]
            t0 = r["brk"][0]
            bE, bL = corr_pair(case, t0, p["late_end"], which)
            ctl = [corr_pair(case, t, p["late_end"], which) for t, _, _ in r["ctl"]]
            cE = np.nanmedian([c[0] for c in ctl]) if ctl else np.nan
            cL = np.nanmedian([c[1] for c in ctl]) if ctl else np.nan
            dctl = np.nanmedian([c[1] - c[0] for c in ctl]) if ctl else np.nan
            if not (np.isfinite(bE) and np.isfinite(bL) and np.isfinite(dctl)):
                continue
            rows.append(dict(caseid=cid, break_E=bE, break_L=bL, ctl_E=float(cE), ctl_L=float(cL),
                             excess=float((bL - bE) - dctl),
                             break_abs_change=float(abs(bL) - abs(bE))))
        excess = [x["excess"] for x in rows]
        report["map_" + which] = dict(
            n=len(rows),
            median_excess_change_in_correlation=float(np.median(excess)) if rows else None,
            break_window_E=summarise([x["break_E"] for x in rows]),
            break_window_L=summarise([x["break_L"] for x in rows]),
            control_windows_E=summarise([x["ctl_E"] for x in rows]),
            control_windows_L=summarise([x["ctl_L"] for x in rows]),
            break_abs_change=summarise([x["break_abs_change"] for x in rows]),
            share_cases_moving_away_from_zero=float(np.mean([x["break_abs_change"] > 0 for x in rows])) if rows else None,
            cases=rows)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "g18_followup.json"), "w") as f:
        json.dump(report, f, indent=2, default=float)
    for which in ("hr", "sv"):
        m = report["map_" + which]
        print(which, "n", m["n"], "excess", m["median_excess_change_in_correlation"],
              "break E", m["break_window_E"].get("median"), "break L", m["break_window_L"].get("median"),
              "ctl E", m["control_windows_E"].get("median"), "ctl L", m["control_windows_L"].get("median"),
              "away from zero", m["share_cases_moving_away_from_zero"])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
