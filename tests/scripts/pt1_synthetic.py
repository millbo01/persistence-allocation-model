"""PT1: checks of the analysis code on synthetic data only (pre-registration Section 9, step 3). No real data.

Each scenario writes tidy files in the layout pt1_councils.py reads, with a planted effect, and checks the verdict.
Real line names come from the frozen classification so that name matching is exercised. Distractors: a non-single-
tier council, the City of London code, a council missing a year, a line missing in one year, a parking-like line
with negative spending, and a tiny line.

Usage: python pt1_synthetic.py [--work DIR]
"""
import argparse
import json
import os
import shutil
import sys
import tempfile

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pt1_councils as A  # noqa: E402

OUT = os.path.join(HERE, "..", "results", "PT1-synthetic")
YEARS = A.YEARS


def lines_for_test():
    sc = A.scope_table(pd.read_csv(A.CLASSIFICATION),
                       extra=[("RO3", 60), ("RO6", 430), ("RO6", 441), ("RO6", 442), ("RO6", 460), ("RO6", 475)])
    cls = pd.read_csv(A.CLASSIFICATION)
    cls["key"] = cls["line_name"].map(A.norm)
    return sc.merge(cls[["form", "key", "line_name"]], on=["form", "key"])


def make(name, work, beta=0.0, class_eff=(0.03, 0.015), noise=0.03, n_councils=80, step=None, seed=1):
    rng = np.random.default_rng(seed)
    root = os.path.join(work, name)
    if os.path.exists(root):
        shutil.rmtree(root)
    os.makedirs(root)
    L = lines_for_test()
    codes = [f"E06{i:06d}" for i in range(1, n_councils + 1)]
    types = ["UA"] * (n_councils // 3) + ["MD"] * (n_councils // 3) + ["LB"] * (n_councils - 2 * (n_councils // 3))
    codes += ["E07000999", "E09000001", "E06999999"]       # district (out), City of London (out), missing a year
    types += ["other", "LB", "UA"]
    groups = ["all", "0_17", "65plus", "18plus"]
    # projected five-year growth by council and group; realised annual growth tracks it with noise
    gp = {(c, g): rng.normal(0.04, 0.03) for c in codes for g in groups}
    pop, proj = [], []
    for c in codes:
        for g in groups:
            base = rng.uniform(2e4, 3e5) if g != "all" else rng.uniform(1.5e5, 1e6)
            P = base
            for y in range(2010, 2021):
                pop.append(dict(ons_code=c, year=y, group=g, population=P))
                P *= np.exp(gp[(c, g)] / 5 + rng.normal(0, 0.004))
            for ed, by, last in (("2011i", 2011, 2021), ("2012", 2012, 2037), ("2014", 2014, 2039), ("2016", 2016, 2041)):
                Q = base * np.exp((by - 2010) * gp[(c, g)] / 5)
                for y in range(by, last + 1):
                    proj.append(dict(ons_code=c, edition=ed, year=y, group=g, population=Q))
                    Q *= np.exp(gp[(c, g)] / 5 + rng.normal(0, 0.001))
    pop = pd.DataFrame(pop)
    proj = pd.DataFrame(proj)
    popi = pop.set_index(["ons_code", "year", "group"])["population"]
    cpi = pd.DataFrame(dict(year=YEARS, cpi=[100 * 1.02 ** i for i in range(len(YEARS))]))
    cut = {c: rng.uniform(0.0, 0.08) for c in codes}       # council funding squeeze (for scarcity)
    csp = pd.DataFrame([dict(ons_code=c, year=y, csp_thousands=5e5 * np.exp(-cut[c] * (y - 2015)) * 1.02 ** (y - 2014))
                        for c in codes for y in range(2015, 2020)])
    spend = []
    clsmap = {"A": class_eff[0], "B": class_eff[1], "C": 0.0, "ambiguous": class_eff[1] / 2}
    for c, t in zip(codes, types):
        cy_shock = {y: rng.normal(-0.02, 0.01) for y in YEARS}
        for _, ln in L.iterrows():
            g = ln["group"]
            pc = rng.uniform(5, 60)                       # GBP per head, 2014-15
            lt = rng.normal(0, 0.01)
            for y in YEARS:
                if y > 2014:
                    gpj = gp[(c, g)]                      # the planted projected five-year growth
                    eff = beta * gpj if step is None else step * (gpj > 0.04)
                    pc *= np.exp(eff + clsmap[ln["cls"]] + cy_shock[y] + lt + rng.normal(0, noise))
                real = pc * popi[(c, y, g)] / 1000.0      # GBP thousands
                nominal = real * (1.02 ** (y - 2014))
                if c == "E06999999" and y == 2017:
                    continue
                if A.norm(ln["line_name"]) == A.norm("On-street parking"):
                    nominal = -500.0                      # income-generating line (positivity rule)
                if A.norm(ln["line_name"]) == A.norm("Tourism"):
                    nominal = 20.0                        # tiny line (minimum rule)
                spend.append(dict(ons_code=c, la_type=t, year=y, form=ln["form"], line_name=ln["line_name"],
                                  nce_thousands=nominal))
        if c == codes[0]:   # a duplicated name in one council (duplicate rule)
            for y in YEARS:
                spend.append(dict(ons_code=c, la_type=t, year=y, form="RO5", line_name="Library services", nce_thousands=999.0))
    spend = pd.DataFrame(spend)
    spend = spend[~((spend["line_name"] == "Allotments") & (spend["year"] == 2016))]   # a line missing one year
    for k, df in (("spend", spend), ("pop", pop), ("proj", proj), ("csp", csp), ("cpi", cpi)):
        df.to_csv(os.path.join(root, f"{k}.csv"), index=False)
    return root


SCEN = [
    ("S1_dynamic_graded", dict(beta=0.6), "H-fixed fails", "Supported"),
    ("S2_fixed_precise", dict(beta=0.0, noise=0.01, n_councils=120), "H-fixed supported", "Supported"),
    ("S3_fixed_noisy", dict(beta=0.0, noise=0.4, n_councils=20), "Inconclusive", None),
    ("S4_contrary", dict(beta=-0.6), "Contrary", "Supported"),
    ("S5_stepped", dict(step=0.04), "H-fixed fails", "Supported"),
    ("S6_class_reversed", dict(beta=0.0, noise=0.01, class_eff=(-0.03, -0.015), n_councils=120), "H-fixed supported", "Contradicted"),
    ("S7_no_class_effect", dict(beta=0.0, noise=0.01, class_eff=(0.0, 0.0), n_councils=120), "H-fixed supported", "Fails"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", default=None)
    a = ap.parse_args()
    work = a.work or tempfile.mkdtemp(prefix="pt1_synth_")
    rep = []
    for name, kw, exp_pt1, exp_g25 in SCEN:
        root = make(name, work, **kw)
        out = os.path.join(OUT, name)
        d = A.load(root)
        panel, counts = A.build_panel(d)
        r1 = A.pt1(panel)
        r2 = A.g25(panel)
        ok1 = r1["verdict"].startswith(exp_pt1)
        ok2 = exp_g25 is None or r2["verdict"] == exp_g25
        row = dict(scenario=name, expected_PT1=exp_pt1, got_PT1=r1["verdict"], beta=r1["beta"], ci=r1["ci95"],
                   shape=r1.get("PT1_S", {}).get("shape"), expected_G25=exp_g25, got_G25=r2["verdict"],
                   match=bool(ok1 and ok2), counts={k: v for k, v in counts.items() if k != "lines_dropped_not_all_years"},
                   lines_dropped=counts["lines_dropped_not_all_years"])
        rep.append(row)
        print(name, "|", r1["verdict"], "| beta", round(r1["beta"], 3), "| shape", row["shape"], "|", r2["verdict"], "| match", row["match"])
    # one full run of analyse() (all sensitivities) on S1, to exercise the whole pipeline
    full = A.analyse(os.path.join(work, "S1_dynamic_graded"), os.path.join(OUT, "S1_full"))
    os.makedirs(OUT, exist_ok=True)
    json.dump(rep, open(os.path.join(OUT, "synthetic_report.json"), "w"), indent=2, default=float)


if __name__ == "__main__":
    main()
