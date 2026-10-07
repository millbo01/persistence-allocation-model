"""PT1 (fixed against dynamic priority) and G25: analysis code.

Implements the frozen pre-registration tests/PT1 Priority test - pre-registration.md (frozen 7 October 2026,
SHA-256 begins a4aab81d). Written before any spending, population or funding data was opened; tested only on
synthetic data (tests/scripts/pt1_synthetic.py).

Input: tidy CSV files in DIR, produced by a parser written after the structure-only inspection (pre-registration
Section 9, step 5); the parser is separate and its settings are logged before the run.
    spend.csv  ons_code, la_type (UA | MD | LB | other), year (financial year start, 2014..2019), form (RO2..RO6),
               line_name, nce_thousands (net current expenditure, GBP thousands, cash)
    pop.csv    ons_code, year (mid-year), group (all | 0_17 | 65plus | 18plus), population
    proj.csv   ons_code, edition (2011i | 2012 | 2014 | 2016), year, group, population
    csp.csv    ons_code, year (2015..2019), csp_thousands (Core Spending Power, cash)
    cpi.csv    year (financial year start), cpi (financial-year average index)
Classification: tests/PT1_statutory_classification.csv.

Usage: python pt1_councils.py --data DIR --out DIR
"""
import argparse
import hashlib
import json
import os
import re
import sys

import numpy as np
import pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
CLASSIFICATION = os.path.join(HERE, "..", "PT1_statutory_classification.csv")

YEARS = list(range(2014, 2020))               # financial years 2014-15 .. 2019-20
EDITION = {2014: "2011i", 2015: "2012", 2016: "2012", 2017: "2014", 2018: "2014", 2019: "2016"}
EXCLUDED_CODES = {"E09000001", "E06000053"}   # City of London, Isles of Scilly
SINGLE_TIER = {"UA", "MD", "LB"}
BETA_STAR = 0.25
ALPHA = 0.05

IMPLEMENTATION_NOTES = [
    "Line names are normalised by lower-casing and removing every character that is not a letter or digit; the "
    "leading 'line NN' label, if present in a name, is removed before normalising.",
    "Scope: classification rows in RO2, RO4, RO5, and RO3 lines 10 to 27 (children's social care), minus RO5 226 "
    "and 244. Sensitivity 1 adds RO3 60 (total adult social care); sensitivity 4 adds RO6 430, 441, 442, 460, 475.",
    "A spending line is in scope if its normalised name equals the normalised name of an in-scope classification "
    "row in the same form; lines in the data with no such match are out of scope (counted).",
    "Councils: la_type in UA, MD, LB; City of London and Isles of Scilly excluded; a council must have spending rows "
    "in all six years (same ONS code).",
    "Duplicate names: if a normalised line name occurs more than once in the same council, year and form, that "
    "council's series for the line is dropped (counted); names must identify a line uniquely.",
    "Series rules per council-line: positive nce in all six years; mean real nce over the window at least the "
    "minimum (GBP thousands, 2014-15 prices; primary 100, sensitivity 50 and 250).",
    "Real terms: nce divided by cpi(year)/cpi(2014).",
    "Client groups: RO3 children's social care 0_17; RO2 71 statutory concessionary fares 65plus; RO3 60 adult "
    "social care total 18plus; all others 'all'. RO2 71 is identified by its normalised name.",
    "Outcome winsorised at the 1st and 99th percentiles of the pooled sample of the model being estimated.",
    "Projected growth: ln(P(tau+h)/P(tau)) from the edition assigned to the budget year, tau = financial year start, "
    "h = 5 (sensitivity 5: h = 10; where an edition does not reach tau+10, the growth to its last year is scaled by "
    "10/available years).",
    "Fixed effects absorbed by alternating projections (convergence 1e-10 on the maximum change). Cluster-robust "
    "standard errors by council with the small-sample factor G/(G-1)*(N-1)/(N-K), K = estimated coefficients plus "
    "the number of line fixed effects (council-year effects are nested in clusters and not counted); t "
    "distribution with G-1 degrees of freedom.",
    "PT1-S thresholds: the nine deciles of g_proj in the estimation sample; BIC = N ln(RSS/N) + k ln(N) computed "
    "on the fixed-effect-demeaned data, k = slope parameters (+1 for the threshold).",
    "G25-C scarcity: minus the change in ln(real CSP per head of total population) from 2015-16 to 2019-20; the "
    "interaction is [A] x scarcity (scarcity's main effect is absorbed by council-year effects).",
    "SS: council-years (2015-16 on) where total in-scope real nce fell from the year before; share in which any "
    "A-class series fell while the C-class series in that council kept more than half their 2014-15 real total.",
    "Ambiguous candidates ordered A > B > C; 'lowest' takes the last (C-most) candidate, 'highest' the first.",
]


# ------------------------------------------------------------------ helpers
def norm(name):
    s = str(name).lower()
    s = re.sub(r"^\s*line\s*\d+\s*", "", s)
    return re.sub(r"[^a-z0-9]", "", s)


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def load(data_dir):
    d = {k: pd.read_csv(os.path.join(data_dir, f"{k}.csv")) for k in ("spend", "pop", "proj", "csp", "cpi")}
    d["cls"] = pd.read_csv(CLASSIFICATION)
    return d


def scope_table(cls, extra=()):
    c = cls.copy()
    c["key"] = c["line_name"].map(norm)
    keep = c["form"].isin(["RO2", "RO4", "RO5"]) | ((c["form"] == "RO3") & c["line"].between(10, 27))
    keep &= ~((c["form"] == "RO5") & c["line"].isin([226, 244]))
    for form, line in extra:
        keep |= (c["form"] == form) & (c["line"] == line)
    c = c[keep].copy()
    c["group"] = "all"
    c.loc[(c["form"] == "RO3") & c["line"].between(10, 27), "group"] = "0_17"
    c.loc[(c["form"] == "RO2") & (c["line"] == 71), "group"] = "65plus"
    c.loc[(c["form"] == "RO3") & (c["line"] == 60), "group"] = "18plus"
    return c[["form", "line", "key", "cls", "candidates", "group"]]


def build_panel(d, min_mean=100.0, extra=(), horizon=5):
    """Council-line-year panel after the frozen council, line and series rules. Returns (panel, counts)."""
    counts = {}
    sp = d["spend"].copy()
    sp["key"] = sp["line_name"].map(norm)
    sc = scope_table(d["cls"], extra)
    sp = sp.merge(sc, on=["form", "key"], how="left")
    counts["spend_rows_out_of_scope"] = int(sp["cls"].isna().sum())
    sp = sp[sp["cls"].notna()]
    # councils
    st = sp.groupby("ons_code")["la_type"].first()
    ok = st.index[st.isin(SINGLE_TIER) & ~st.index.isin(EXCLUDED_CODES)]
    yrs = sp.groupby("ons_code")["year"].apply(lambda s: set(s))
    ok = [c for c in ok if set(YEARS) <= yrs[c]]
    counts["councils_single_tier_all_years"] = len(ok)
    counts["councils_dropped"] = int(sp["ons_code"].nunique() - len(ok))
    sp = sp[sp["ons_code"].isin(ok) & sp["year"].isin(YEARS)]
    # lines present in all six years (anywhere in the data)
    ly = sp.groupby(["form", "key"])["year"].apply(lambda s: set(s))
    lines_ok = [k for k, v in ly.items() if set(YEARS) <= v]
    counts["lines_matched_all_years"] = len(lines_ok)
    counts["lines_dropped_not_all_years"] = sorted([f"{k[0]}:{k[1]}" for k, v in ly.items() if not set(YEARS) <= v])
    sp = sp.set_index(["form", "key"]).loc[lines_ok].reset_index()
    # duplicate names within council-year-form: drop that council's series
    dup = sp.duplicated(["ons_code", "year", "form", "key"], keep=False)
    bad = set(map(tuple, sp.loc[dup, ["ons_code", "form", "key"]].drop_duplicates().values))
    counts["series_dropped_duplicate_names"] = len(bad)
    if bad:
        idx = pd.MultiIndex.from_frame(sp[["ons_code", "form", "key"]])
        sp = sp[~idx.isin(list(bad))]
    # real terms
    cpi = d["cpi"].set_index("year")["cpi"]
    sp["real"] = sp["nce_thousands"] / (cpi.loc[sp["year"]].values / cpi.loc[2014])
    # series rules
    g = sp.groupby(["ons_code", "form", "key"])
    full = g["year"].transform("nunique") == len(YEARS)
    pos = g["real"].transform(lambda s: (s > 0).all())
    big = g["real"].transform("mean") >= min_mean
    counts["series_total"] = int(g.ngroups)
    counts["series_dropped_incomplete"] = int(sp[~full].groupby(["ons_code", "form", "key"]).ngroups)
    counts["series_dropped_nonpositive"] = int(sp[full & ~pos].groupby(["ons_code", "form", "key"]).ngroups)
    counts["series_dropped_below_minimum"] = int(sp[full & pos & ~big].groupby(["ons_code", "form", "key"]).ngroups)
    sp = sp[full & pos & big]
    counts["series_kept"] = int(sp.groupby(["ons_code", "form", "key"]).ngroups)
    # population
    pop = d["pop"].set_index(["ons_code", "year", "group"])["population"]
    sp["P"] = [pop.get((c, y, gr), np.nan) for c, y, gr in zip(sp["ons_code"], sp["year"], sp["group"])]
    # projected growth
    pr = d["proj"].set_index(["ons_code", "edition", "year", "group"])["population"]
    last = d["proj"].groupby("edition")["year"].max()

    def gproj(c, y, gr):
        e = EDITION[y]
        h = horizon
        end = y + h
        scale = 1.0
        if end > last[e]:
            scale = h / (last[e] - y)
            end = last[e]
        a, b = pr.get((c, e, y, gr), np.nan), pr.get((c, e, end, gr), np.nan)
        return scale * np.log(b / a)
    sp["g_proj"] = [gproj(c, y, gr) for c, y, gr in zip(sp["ons_code"], sp["year"], sp["group"])]
    sp = sp.sort_values(["ons_code", "form", "key", "year"])
    sp["lnpc"] = np.log(sp["real"] / sp["P"])
    sp["lnP"] = np.log(sp["P"])
    grp = sp.groupby(["ons_code", "form", "key"])
    sp["y"] = grp["lnpc"].diff()
    sp["g_real"] = grp["lnP"].diff()
    sp["line_id"] = sp["form"] + ":" + sp["key"]
    sp["cy"] = sp["ons_code"] + ":" + sp["year"].astype(str)
    return sp, counts


# ------------------------------------------------------------------ estimation
def demean(cols, fe_lists, tol=1e-10, maxit=10000):
    X = cols.copy()
    for _ in range(maxit):
        old = X.copy()
        for fe in fe_lists:
            X = X - X.groupby(fe).transform("mean")
        if np.max(np.abs((X - old).values)) < tol:
            break
    return X


def ols_cluster(df, ycol, xcols, fes, cluster, n_line_fe):
    d = df[list(dict.fromkeys([ycol] + xcols + fes + [cluster]))].dropna()
    Z = demean(d[[ycol] + xcols], [d[f] for f in fes])
    y, X = Z[ycol].values, Z[xcols].values
    XtX_inv = np.linalg.pinv(X.T @ X)
    b = XtX_inv @ X.T @ y
    u = y - X @ b
    N, k = X.shape
    K = k + n_line_fe
    meat = np.zeros((k, k))
    for _, idx in d.groupby(cluster).indices.items():
        s = X[idx].T @ u[idx]
        meat += np.outer(s, s)
    G = d[cluster].nunique()
    V = XtX_inv @ meat @ XtX_inv * (G / (G - 1)) * ((N - 1) / max(N - K, 1))
    se = np.sqrt(np.diag(V))
    return dict(b=b, se=se, V=V, N=N, G=G, df=G - 1, rss=float(u @ u), names=xcols, Z=Z, u=u)


def one_sided(b, se, df):
    t = b / se
    return float(stats.t.sf(t, df)), float(2 * stats.t.sf(abs(t), df))


def winsor(df, col):
    lo, hi = df[col].quantile([0.01, 0.99])
    df = df.copy()
    df[col] = df[col].clip(lo, hi)
    return df


# ------------------------------------------------------------------ tests
def pt1(panel, do_winsor=True):
    p = panel.dropna(subset=["y", "g_proj", "g_real"])
    if do_winsor:
        p = winsor(p, "y")
    n_line = p["line_id"].nunique()
    r = ols_cluster(p, "y", ["g_proj", "g_real"], ["line_id", "cy"], "ons_code", n_line)
    b, se = r["b"][0], r["se"][0]
    p1, p2 = one_sided(b, se, r["df"])
    tcrit = stats.t.ppf(0.975, r["df"])
    upper = b + tcrit * se
    if p1 < ALPHA:
        verdict = "H-fixed fails in this system; dynamic priority earned for institutions of this kind"
    elif b < 0 and p2 < ALPHA:
        verdict = "Contrary to H-dynamic"
    elif upper < BETA_STAR:
        verdict = "H-fixed supported (no meaningful anticipation)"
    else:
        verdict = "Inconclusive (insufficient precision)"
    out = dict(beta=float(b), se=float(se), p_one_sided=p1, p_two_sided=p2, ci95=[float(b - tcrit * se), float(upper)],
               gamma_realised=float(r["b"][1]), N=r["N"], councils=r["G"], lines=int(n_line), verdict=verdict)
    if p1 < ALPHA:
        out["PT1_S"] = pt1s(p, r)
    return out


def pt1s(p, r):
    Z = r["Z"]
    N = len(Z)
    bic_lin = N * np.log(r["rss"] / N) + 2 * np.log(N)
    d = p.dropna(subset=["y", "g_proj", "g_real"])
    best = None
    for q in np.arange(0.1, 1.0, 0.1):
        th = d["g_proj"].quantile(q)
        dd = d.assign(step=(d["g_proj"] > th).astype(float))
        rr = ols_cluster(dd, "y", ["step", "g_real"], ["line_id", "cy"], "ons_code", d["line_id"].nunique())
        if best is None or rr["rss"] < best[1]:
            best = (float(th), rr["rss"])
    bic_step = N * np.log(best[1] / N) + 3 * np.log(N)
    if bic_lin < bic_step - 2:
        shape = "graded"
    elif bic_step < bic_lin - 2:
        shape = "stepped"
    else:
        shape = "indeterminate"
    return dict(bic_linear=float(bic_lin), bic_step=float(bic_step), threshold=best[0], shape=shape)


def class_cols(panel, ambiguous="exclude"):
    p = panel.copy()
    c = p["cls"].copy()
    if ambiguous != "exclude":
        amb = p["cls"] == "ambiguous"
        cands = p.loc[amb, "candidates"].str.split("/")
        c.loc[amb] = cands.map(lambda L: L[-1] if ambiguous == "lowest" else L[0])
    p["cls_used"] = c
    p = p[p["cls_used"].isin(["A", "B", "C"])]
    p["A"] = (p["cls_used"] == "A").astype(float)
    p["B"] = (p["cls_used"] == "B").astype(float)
    return p


def g25(panel, ambiguous="exclude", do_winsor=True):
    p = class_cols(panel, ambiguous).dropna(subset=["y", "g_real"])
    if do_winsor:
        p = winsor(p, "y")
    r = ols_cluster(p, "y", ["A", "B", "g_real"], ["cy"], "ons_code", 0)
    dA, dB = r["b"][0], r["b"][1]
    seA, seB = r["se"][0], r["se"][1]
    seAB = np.sqrt(r["V"][0, 0] + r["V"][1, 1] - 2 * r["V"][0, 1])
    pA, pA2 = one_sided(dA, seA, r["df"])
    pB, _ = one_sided(dB, seB, r["df"])
    pAB, _ = one_sided(dA - dB, seAB, r["df"])
    if pA < ALPHA and dA >= dB >= 0:
        v = "Supported"
    elif pA < ALPHA:
        v = "Partly supported"
    elif dA < 0 and pA2 < ALPHA:
        v = "Contradicted"
    else:
        v = "Fails"
    return dict(delta_A=float(dA), delta_B=float(dB), p_A=pA, p_A_two_sided=pA2, p_B=pB, p_A_minus_B=pAB,
                N=r["N"], councils=r["G"], verdict=v, weight=0.5)


def g25c(panel, d, do_winsor=True):
    p = class_cols(panel).dropna(subset=["y", "g_real"])
    cpi = d["cpi"].set_index("year")["cpi"]
    csp = d["csp"].copy()
    csp["real"] = csp["csp_thousands"] / (cpi.loc[csp["year"]].values / cpi.loc[2014])
    pop = d["pop"][d["pop"]["group"] == "all"].set_index(["ons_code", "year"])["population"]
    csp["pc"] = [r / pop.get((c, y), np.nan) for c, y, r in zip(csp["ons_code"], csp["year"], csp["real"])]
    w = csp.pivot(index="ons_code", columns="year", values="pc")
    scar = -(np.log(w[2019]) - np.log(w[2015]))
    p["scarcity"] = p["ons_code"].map(scar)
    p["A_x_scar"] = p["A"] * p["scarcity"]
    if do_winsor:
        p = winsor(p, "y")
    r = ols_cluster(p.dropna(subset=["scarcity"]), "y", ["A", "B", "A_x_scar", "g_real"], ["cy"], "ons_code", 0)
    b, se = r["b"][2], r["se"][2]
    p1, _ = one_sided(b, se, r["df"])
    return dict(interaction=float(b), se=float(se), p_one_sided=p1,
                verdict="Supported" if p1 < ALPHA else "Not supported", weight=0.5)


def ss(panel):
    p = class_cols(panel)
    tot = p.groupby(["ons_code", "year"])["real"].sum().unstack()
    base_c = p[(p["cls_used"] == "C") & (p["year"] == 2014)].groupby("ons_code")["real"].sum()
    n = hit = 0
    for c in tot.index:
        for y in range(2015, 2020):
            if tot.loc[c, y] < tot.loc[c, y - 1]:
                n += 1
                a = p[(p["ons_code"] == c) & (p["cls_used"] == "A")].pivot(index="key", columns="year", values="real")
                cnow = p[(p["ons_code"] == c) & (p["cls_used"] == "C") & (p["year"] == y)]["real"].sum()
                a_fell = (a[y] < a[y - 1]).any() if len(a) else False
                if a_fell and base_c.get(c, 0) > 0 and cnow > 0.5 * base_c[c]:
                    hit += 1
    return dict(council_years_with_fall=n, share_A_fell_while_C_kept_over_half=(hit / n if n else None))


def long_difference(d):
    panel, _ = build_panel(d)
    first = panel[panel["year"] == 2014].set_index(["ons_code", "line_id"])
    lastp = panel[panel["year"] == 2019].set_index(["ons_code", "line_id"])
    j = first[["lnpc", "lnP", "g_proj"]].join(lastp[["lnpc", "lnP"]], rsuffix="_e").dropna().reset_index()
    j["y"] = j["lnpc_e"] - j["lnpc"]
    j["g_real"] = j["lnP_e"] - j["lnP"]
    j = winsor(j, "y")
    r = ols_cluster(j, "y", ["g_proj", "g_real"], ["line_id", "ons_code"], "ons_code", j["line_id"].nunique())
    p1, p2 = one_sided(r["b"][0], r["se"][0], r["df"])
    return dict(beta=float(r["b"][0]), se=float(r["se"][0]), p_one_sided=p1, N=r["N"])


# ------------------------------------------------------------------ main
def analyse(data_dir, out_dir):
    d = load(data_dir)
    panel, counts = build_panel(d)
    res = dict(prereg="tests/PT1 Priority test - pre-registration.md", prereg_sha256_begins="a4aab81d",
               code_sha256=sha(os.path.abspath(__file__)), classification_sha256=sha(CLASSIFICATION),
               implementation_notes=IMPLEMENTATION_NOTES, counts=counts)
    res["PT1"] = pt1(panel)
    res["G25"] = g25(panel)
    res["G25_C"] = g25c(panel, d)
    res["SS"] = ss(panel)
    sens = {}
    p1, _ = build_panel(d, extra=[("RO3", 60)])
    sens["1_adult_social_care_included"] = dict(PT1=pt1(p1))
    sens["2_long_difference"] = long_difference(d)
    sens["3_ambiguous_lowest"] = g25(panel, "lowest")
    sens["3_ambiguous_highest"] = g25(panel, "highest")
    p4, _ = build_panel(d, extra=[("RO6", 430), ("RO6", 441), ("RO6", 442), ("RO6", 460), ("RO6", 475)])
    sens["4_RO6_client_lines"] = dict(PT1=pt1(p4), G25=g25(p4))
    p5, _ = build_panel(d, horizon=10)
    sens["5_ten_year_projection"] = dict(PT1=pt1(p5))
    sens["6_no_winsorising"] = dict(PT1=pt1(panel, do_winsor=False), G25=g25(panel, do_winsor=False))
    p7 = panel[~panel["ons_code"].str.startswith("E09")]
    sens["7_london_excluded"] = dict(PT1=pt1(p7), G25=g25(p7))
    for m in (50.0, 250.0):
        pm, _ = build_panel(d, min_mean=m)
        sens[f"8_minimum_{int(m)}"] = dict(PT1=pt1(pm), G25=g25(pm))
    res["sensitivity"] = sens
    os.makedirs(out_dir, exist_ok=True)
    json.dump(res, open(os.path.join(out_dir, "summary.json"), "w"), indent=2, default=float)
    print(json.dumps(dict(PT1=res["PT1"]["verdict"], G25=res["G25"]["verdict"], G25_C=res["G25_C"]["verdict"]), indent=1))
    return res


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    analyse(a.data, a.out)
