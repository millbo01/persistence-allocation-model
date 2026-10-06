"""H1 VitalDB: reconcile GPT's implementation (h1_vdb_g12_check.py, unedited) with the frozen run.

GPT's audit flagged two readings in the frozen code (missing bins in the stable approach; interpolating
missing 10-s bins inside usable windows). This diagnostic swaps the frozen code's readings into GPT's
script, one at a time and together, by replacing those two functions only, and records the counts. With
both swapped, it also runs the full analysis, to check whether the two implementations otherwise agree.
It selects nothing: the frozen run remains the primary result.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import h1_vdb_g12_check as G  # noqa: E402

ORIG_STABLE = G.approach_is_stable
ORIG_WINDOW = G.measurement_window


def stable_frozen(case, onset):
    a = G.bin_index(case, onset - G.APPROACH_S)
    b = G.bin_index(case, onset)
    v = case["map_bins"][max(0, a):b]
    v = v[np.isfinite(v)]
    return len(v) > 0 and bool(np.all(v >= G.HYPOTENSION))


def window_frozen(case, start, stop):
    v = ORIG_WINDOW(case, start, stop)
    if v is None:
        return None
    if np.isnan(v).any():
        idx = np.arange(len(v))
        ok = ~np.isnan(v)
        if ok.sum() < 3:
            return None
        v = np.interp(idx, idx[ok], v[ok])
    return v


def run(label, stable, window, full):
    G.approach_is_stable = stable
    G.measurement_window = window
    repo = G.Repository(os.path.join(HERE, "..", "..", "data", "vitaldb"))
    dec = G.count_design(repo)
    out = dict(variant=label, counts=dec["counts"], runnable=dec["runnable"], cohort=dec["cohort"],
               threshold=dec["threshold"])
    if full and dec["runnable"]:
        _, processed, high, low, scored, _ = G.analyze_variant(repo, dec["cohort"] == "fallback", dec["threshold"])
        out.update(n_high=len(high), n_low=len(low), P1=scored["P1"], P2=scored["P2"], P3=scored["P3"],
                   verdict=scored["verdict"], high_ids=sorted(high), low_ids=sorted(low),
                   high_D={int(c): scored["high_ar"][c] for c in high})
    return out


if __name__ == "__main__":
    res = [run("A: frozen stable rule only", stable_frozen, ORIG_WINDOW, False),
           run("B: frozen window interpolation only", ORIG_STABLE, window_frozen, False),
           run("C: both frozen readings", stable_frozen, window_frozen, True)]
    out = os.path.join(HERE, "..", "results", "H1-VDB-R1")
    os.makedirs(out, exist_ok=True)
    json.dump(res, open(os.path.join(out, "reconcile.json"), "w"), indent=2, default=float)
    for r in res:
        print(r["variant"], r["counts"], r.get("verdict"))
