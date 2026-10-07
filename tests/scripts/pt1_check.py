#!/usr/bin/env python3
"""Independent checker for PT1 / G25.

Python 3.12; dependencies limited to numpy, pandas and scipy.

This starts from the tidy CSV files. Fixed effects are absorbed independently
of pt1_councils.py by projecting y and X on a sparse dummy-matrix for the fixed
effects with scipy.sparse.linalg.lsqr (Frisch-Waugh-Lovell), rather than by
alternating group demeaning.
"""

import argparse
import json
import os
import re

import numpy as np
import pandas as pd
from scipy import sparse, stats
from scipy.sparse.linalg import lsqr


YEARS = tuple(range(2014, 2020))
EDITION = {
    2014: "2011i",
    2015: "2012",
    2016: "2012",
    2017: "2014",
    2018: "2014",
    2019: "2016",
}
ALLOWED_TYPES = {"UA", "MD", "LB"}
EXCLUDED_CODES = {"E09000001", "E06000053"}  # City of London, Isles of Scilly
ALPHA = 0.05
BETA_STAR = 0.25


def normalise_name(value):
    s = str(value).lower()
    # Implementation note: strip a leading printed "line NN" label first.
    s = re.sub(r"^\s*line\s*\d+\s*", "", s)
    return re.sub(r"[^a-z0-9]", "", s)


def finite_mask(frame, columns):
    m = np.ones(len(frame), dtype=bool)
    for c in columns:
        v = pd.to_numeric(frame[c], errors="coerce").to_numpy(dtype=float)
        m &= np.isfinite(v)
    return m


def strict_unique(frame, keys, label):
    dup = frame.duplicated(keys, keep=False)
    if dup.any():
        ex = frame.loc[dup, keys].drop_duplicates().head(10).to_dict("records")
        raise ValueError(f"{label} is not unique on {keys}; examples: {ex}")


def read_inputs(data_dir, cls_path):
    out = {}
    for name in ("spend", "pop", "proj", "csp", "cpi"):
        out[name] = pd.read_csv(os.path.join(data_dir, f"{name}.csv"))
    out["cls"] = pd.read_csv(cls_path)

    required = {
        "spend": {
            "ons_code", "la_type", "year", "form",
            "line_name", "nce_thousands",
        },
        "pop": {"ons_code", "year", "population", "group"},
        "proj": {
            "ons_code", "edition", "year", "group", "population",
        },
        "csp": {"ons_code", "year", "csp_thousands"},
        "cpi": {"year", "cpi"},
        "cls": {"form", "line", "line_name", "cls", "candidates"},
    }
    for name, need in required.items():
        missing = need - set(out[name].columns)
        if missing:
            raise ValueError(
                f"{name} is missing required columns: {sorted(missing)}"
            )

    for name in ("spend", "pop", "proj", "csp", "cpi"):
        out[name]["year"] = pd.to_numeric(
            out[name]["year"], errors="raise"
        ).astype(int)
    out["cls"]["line"] = pd.to_numeric(
        out["cls"]["line"], errors="raise"
    ).astype(int)
    return out


def scoped_classification(cls, extras=()):
    c = cls.copy()
    c["key"] = c["line_name"].map(normalise_name)

    keep = c["form"].isin(["RO2", "RO4", "RO5"])
    keep |= (c["form"] == "RO3") & c["line"].between(10, 27)
    keep &= ~(
        (c["form"] == "RO5") & c["line"].isin([226, 244])
    )

    for form, line in extras:
        keep |= (c["form"] == form) & (c["line"] == int(line))

    c = c.loc[keep].copy()

    # A name is the matching key under the frozen rule. Refuse to silently
    # multiply spending rows if the classification itself is non-unique.
    strict_unique(c, ["form", "key"], "in-scope classification")

    c["group"] = "all"
    c.loc[
        (c["form"] == "RO3") & c["line"].between(10, 27),
        "group",
    ] = "0_17"
    c.loc[
        (c["form"] == "RO2") & (c["line"] == 71),
        "group",
    ] = "65plus"
    c.loc[
        (c["form"] == "RO3") & (c["line"] == 60),
        "group",
    ] = "18plus"

    return c[
        [
            "form", "line", "line_name", "key",
            "cls", "candidates", "group",
        ]
    ]


def cpi_lookup(cpi):
    c = cpi.loc[
        cpi["year"].isin(YEARS), ["year", "cpi"]
    ].copy()
    strict_unique(c, ["year"], "CPI")
    c["cpi"] = pd.to_numeric(c["cpi"], errors="coerce")
    s = c.set_index("year")["cpi"]

    missing = [
        y
        for y in YEARS
        if (
            y not in s.index
            or not np.isfinite(s.loc[y])
            or s.loc[y] <= 0
        )
    ]
    if missing:
        raise ValueError(
            f"missing/nonpositive CPI for financial-year starts: {missing}"
        )
    return s


def council_selection(spend):
    s = spend.loc[spend["year"].isin(YEARS)].copy()
    by = s.groupby("ons_code", sort=False)

    rows = []
    for code, g in by:
        types = {
            str(x)
            for x in g["la_type"].dropna().unique()
        }
        all_single = bool(types) and types <= ALLOWED_TYPES
        excluded = code in EXCLUDED_CODES

        years = set(
            pd.to_numeric(
                g["year"], errors="coerce"
            ).dropna().astype(int)
        )
        all_years = set(YEARS) <= years

        rows.append(
            (
                code,
                all_single,
                excluded,
                all_years,
                sorted(types),
            )
        )

    tab = pd.DataFrame(
        rows,
        columns=[
            "ons_code",
            "single_tier_all_rows",
            "excluded_code",
            "has_return_all_years",
            "types",
        ],
    )

    if len(tab) == 0:
        return set(), {
            "councils_seen": 0,
            "councils_kept": 0,
            "councils_dropped_not_single_tier": 0,
            "councils_dropped_excluded_code": 0,
            "councils_dropped_missing_year": 0,
        }

    keep = (
        tab["single_tier_all_rows"]
        & ~tab["excluded_code"]
        & tab["has_return_all_years"]
    )

    counts = {
        "councils_seen": int(len(tab)),
        "councils_kept": int(keep.sum()),
        "councils_dropped_not_single_tier": int(
            (~tab["single_tier_all_rows"]).sum()
        ),
        "councils_dropped_excluded_code": int(
            (
                tab["single_tier_all_rows"]
                & tab["excluded_code"]
            ).sum()
        ),
        "councils_dropped_missing_year": int(
            (
                tab["single_tier_all_rows"]
                & ~tab["excluded_code"]
                & ~tab["has_return_all_years"]
            ).sum()
        ),
    }

    return set(tab.loc[keep, "ons_code"]), counts


def projection_series(proj):
    p = proj.copy()
    p["population"] = pd.to_numeric(
        p["population"], errors="coerce"
    )
    strict_unique(
        p,
        ["ons_code", "edition", "year", "group"],
        "projection table",
    )
    return p.set_index(
        ["ons_code", "edition", "year", "group"]
    )["population"]


def population_series(pop):
    p = pop.copy()
    p["population"] = pd.to_numeric(
        p["population"], errors="coerce"
    )
    strict_unique(
        p,
        ["ons_code", "year", "group"],
        "population table",
    )
    return p.set_index(
        ["ons_code", "year", "group"]
    )["population"]


def build_panel(
    inputs,
    min_mean=100.0,
    extras=(),
    horizon=5,
    council_subset=None,
):
    """Build the retained council-line-year panel from the tidy inputs.

    The frozen text says a council missing a final return is excluded.
    Unlike the original code, return presence is checked on the raw tidy
    spending table before applying the in-scope-line filter; this is the
    more literal reading and avoids making council eligibility depend on
    which lines are in the analysis.
    """
    spend = inputs["spend"].copy()
    spend = spend.loc[
        spend["year"].isin(YEARS)
    ].copy()
    spend["key"] = spend["line_name"].map(
        normalise_name
    )

    council_codes, counts = council_selection(spend)

    if council_subset is not None:
        counts[
            "councils_kept_before_sensitivity_filter"
        ] = int(len(council_codes))
        council_codes &= set(council_subset)
        counts["councils_kept"] = int(
            len(council_codes)
        )

    spend = spend.loc[
        spend["ons_code"].isin(council_codes)
    ].copy()

    scope = scoped_classification(
        inputs["cls"], extras
    )

    spend = spend.merge(
        scope,
        on=["form", "key"],
        how="left",
        suffixes=("_data", "_cls"),
        validate="many_to_one",
    )

    counts["spending_rows_out_of_scope"] = int(
        spend["cls"].isna().sum()
    )
    spend = spend.loc[
        spend["cls"].notna()
    ].copy()

    # Global line-name rule: the normalised form/name must occur
    # in every year.
    line_years = spend.groupby(
        ["form", "key"], sort=False
    )["year"].agg(lambda x: set(x))

    good_lines = {
        idx
        for idx, ys in line_years.items()
        if set(YEARS) <= ys
    }
    bad_lines = [
        idx
        for idx, ys in line_years.items()
        if not set(YEARS) <= ys
    ]

    counts["lines_in_scope_seen"] = int(
        len(line_years)
    )
    counts["lines_matched_all_years"] = int(
        len(good_lines)
    )

    display = scope.set_index(
        ["form", "key"]
    )["line_name"]

    counts["lines_dropped_not_all_years"] = [
        f"{form}:{display.get((form, key), key)}"
        for form, key in sorted(bad_lines)
    ]

    if good_lines:
        idx = pd.MultiIndex.from_frame(
            spend[["form", "key"]]
        )
        spend = spend.loc[
            idx.isin(good_lines)
        ].copy()
    else:
        spend = spend.iloc[0:0].copy()

    # Duplicate-name implementation note: if a
    # council/year/form/name is not unique, drop that
    # council-line series in every year rather than pick one.
    series_keys = ["ons_code", "form", "key"]

    initial_series = spend[
        series_keys
    ].drop_duplicates()
    counts["series_total"] = int(
        len(initial_series)
    )

    dup = spend.duplicated(
        ["ons_code", "year", "form", "key"],
        keep=False,
    )

    bad_dup = spend.loc[
        dup, series_keys
    ].drop_duplicates()

    counts[
        "series_dropped_duplicate_names"
    ] = int(len(bad_dup))

    if len(bad_dup):
        bad_idx = pd.MultiIndex.from_frame(
            bad_dup
        )
        idx = pd.MultiIndex.from_frame(
            spend[series_keys]
        )
        spend = spend.loc[
            ~idx.isin(bad_idx)
        ].copy()

    # Deflate before applying the real-expenditure minimum.
    cpi = cpi_lookup(inputs["cpi"])
    spend["nce_thousands"] = pd.to_numeric(
        spend["nce_thousands"],
        errors="coerce",
    )
    spend["real"] = (
        spend["nce_thousands"]
        / (
            spend["year"].map(cpi)
            / float(cpi.loc[2014])
        )
    )

    # Apply series exclusions sequentially so counts
    # are mutually exclusive.
    by = spend.groupby(
        series_keys, sort=False
    )

    stats_series = by.agg(
        n_years=("year", "nunique"),
        n_obs=("nce_thousands", "size"),
        n_missing=(
            "nce_thousands",
            lambda x: int(x.isna().sum()),
        ),
        any_nonpositive=(
            "nce_thousands",
            lambda x: bool(
                (
                    pd.to_numeric(
                        x, errors="coerce"
                    )
                    <= 0
                )
                .fillna(False)
                .any()
            ),
        ),
        mean_real=("real", "mean"),
    ).reset_index()

    incomplete = (
        stats_series["n_years"]
        != len(YEARS)
    )
    missing = (
        ~incomplete
        & (stats_series["n_missing"] > 0)
    )
    nonpositive = (
        ~incomplete
        & ~missing
        & stats_series["any_nonpositive"]
    )
    too_small = (
        ~incomplete
        & ~missing
        & ~nonpositive
        & (
            stats_series["mean_real"]
            < float(min_mean)
        )
    )

    keep_series = ~(
        incomplete
        | missing
        | nonpositive
        | too_small
    )

    counts["series_dropped_incomplete"] = int(
        incomplete.sum()
    )

    # The implementation note says "positive nce in all six
    # years"; keeping a separate missing category avoids
    # silently labelling blanks as <= 0.
    counts["series_dropped_missing_nce"] = int(
        missing.sum()
    )
    counts["series_dropped_nonpositive"] = int(
        nonpositive.sum()
    )
    counts["series_dropped_below_minimum"] = int(
        too_small.sum()
    )
    counts["series_kept"] = int(
        keep_series.sum()
    )

    kept = stats_series.loc[
        keep_series, series_keys
    ]

    if len(kept):
        kept_idx = pd.MultiIndex.from_frame(
            kept
        )
        idx = pd.MultiIndex.from_frame(
            spend[series_keys]
        )
        spend = spend.loc[
            idx.isin(kept_idx)
        ].copy()
    else:
        spend = spend.iloc[0:0].copy()

    spend["line_id"] = (
        spend["form"].astype(str)
        + ":"
        + spend["key"].astype(str)
    )
    spend["series_id"] = (
        spend["ons_code"].astype(str)
        + "|"
        + spend["line_id"]
    )

    pop = population_series(inputs["pop"])
    spend["P"] = [
        pop.get((c, int(y), g), np.nan)
        for c, y, g in zip(
            spend["ons_code"],
            spend["year"],
            spend["group"],
        )
    ]

    # Projected growth. For the ten-year sensitivity, follow
    # the original implementation note where the frozen text
    # is silent about editions whose horizon ends before tau+10:
    # scale the available log growth to ten years.
    proj = projection_series(inputs["proj"])
    last_year = (
        inputs["proj"]
        .groupby("edition")["year"]
        .max()
        .to_dict()
    )

    def projected_growth(code, year, group):
        ed = EDITION[int(year)]
        end = int(year) + int(horizon)
        scale = 1.0
        last = int(last_year[ed])

        if end > last:
            available = last - int(year)
            if available <= 0:
                return np.nan
            end = last
            scale = (
                float(horizon)
                / float(available)
            )

        a = proj.get(
            (code, ed, int(year), group),
            np.nan,
        )
        b = proj.get(
            (code, ed, int(end), group),
            np.nan,
        )

        if not (
            np.isfinite(a)
            and np.isfinite(b)
            and a > 0
            and b > 0
        ):
            return np.nan

        return float(
            scale * np.log(b / a)
        )

    spend["g_proj"] = [
        projected_growth(c, y, g)
        for c, y, g in zip(
            spend["ons_code"],
            spend["year"],
            spend["group"],
        )
    ]

    spend["P"] = pd.to_numeric(
        spend["P"], errors="coerce"
    )

    spend["lnpc"] = np.where(
        (spend["real"] > 0)
        & (spend["P"] > 0),
        np.log(
            spend["real"] / spend["P"]
        ),
        np.nan,
    )

    spend["lnP"] = np.where(
        spend["P"] > 0,
        np.log(spend["P"]),
        np.nan,
    )

    spend = spend.sort_values(
        ["ons_code", "form", "key", "year"]
    ).copy()

    grouped = spend.groupby(
        series_keys, sort=False
    )
    spend["y"] = grouped[
        "lnpc"
    ].diff()
    spend["g_real"] = grouped[
        "lnP"
    ].diff()

    spend["cy"] = (
        spend["ons_code"].astype(str)
        + ":"
        + spend["year"].astype(str)
    )

    series_class = (
        spend
        .drop_duplicates(series_keys)["cls"]
        .value_counts(dropna=False)
    )
    counts["series_kept_by_class"] = {
        str(k): int(v)
        for k, v in series_class.items()
    }

    pt1_mask = finite_mask(
        spend,
        ["y", "g_proj", "g_real"],
    )

    g25_base = spend["cls"].isin(
        ["A", "B", "C"]
    ).to_numpy()

    g25_mask = (
        g25_base
        & finite_mask(
            spend, ["y", "g_real"]
        )
    )

    counts["rows_usable_PT1"] = int(
        pt1_mask.sum()
    )
    counts["rows_usable_G25"] = int(
        g25_mask.sum()
    )

    counts[
        "rows_with_missing_projected_growth_after_series_rules"
    ] = int(
        (
            finite_mask(
                spend, ["y", "g_real"]
            )
            & ~finite_mask(
                spend, ["g_proj"]
            )
        ).sum()
    )

    return spend, counts


def winsorise(frame, column):
    d = frame.copy()
    q = d[column].quantile(
        [0.01, 0.99]
    )
    d[column] = d[column].clip(
        float(q.iloc[0]),
        float(q.iloc[1]),
    )
    return d


def fe_residualise(
    frame,
    columns,
    fe_columns,
):
    """FWL residuals using sparse least-squares
    on the complete FE dummy space.
    """
    if not fe_columns:
        return frame[
            columns
        ].to_numpy(dtype=float)

    n = len(frame)
    rows = np.arange(n)
    blocks = []

    for f in fe_columns:
        codes, uniques = pd.factorize(
            frame[f], sort=True
        )

        if (codes < 0).any():
            raise ValueError(
                f"missing fixed-effect value in {f}"
            )

        blocks.append(
            sparse.csr_matrix(
                (
                    np.ones(
                        n, dtype=float
                    ),
                    (rows, codes),
                ),
                shape=(
                    n, len(uniques)
                ),
            )
        )

    D = sparse.hstack(
        blocks,
        format="csr",
    )

    out = np.empty(
        (n, len(columns)),
        dtype=float,
    )

    for j, col in enumerate(columns):
        v = frame[
            col
        ].to_numpy(dtype=float)

        sol = lsqr(
            D,
            v,
            atol=1e-12,
            btol=1e-12,
            iter_lim=max(
                1000,
                10 * D.shape[1],
            ),
        )

        resid = v - D @ sol[0]

        # Normal-equation orthogonality checks that FE
        # absorption actually converged.
        ortho = (
            np.max(
                np.abs(D.T @ resid)
            )
            if D.shape[1]
            else 0.0
        )
        scale = max(
            1.0,
            np.max(np.abs(v)),
        )

        if (
            not np.isfinite(ortho)
            or ortho > 1e-7 * scale
        ):
            raise RuntimeError(
                "fixed-effect projection did not converge "
                f"for {col}: orthogonality={ortho}"
            )

        out[:, j] = resid

    return out


def cluster_fit(
    frame,
    ycol,
    xcols,
    fe_columns,
    cluster_col,
    n_line_fe,
):
    cols = list(
        dict.fromkeys(
            [ycol]
            + list(xcols)
            + list(fe_columns)
            + [cluster_col]
        )
    )

    d = frame[cols].copy()

    numeric = [
        ycol
    ] + list(xcols)
    mask = finite_mask(
        d, numeric
    )

    for f in (
        list(fe_columns)
        + [cluster_col]
    ):
        mask &= d[
            f
        ].notna().to_numpy()

    d = d.loc[
        mask
    ].reset_index(drop=True)

    if len(d) == 0:
        raise ValueError(
            "empty estimation sample"
        )

    Z = fe_residualise(
        d,
        [ycol] + list(xcols),
        fe_columns,
    )

    y = Z[:, 0]
    X = Z[:, 1:]

    n, k = X.shape
    rank = int(
        np.linalg.matrix_rank(X)
    )

    if rank < k:
        raise ValueError(
            "regressor matrix is rank deficient after "
            f"fixed effects: rank {rank} < {k}"
        )

    b, _, _, _ = np.linalg.lstsq(
        X, y, rcond=None
    )

    u = y - X @ b
    XtX_inv = np.linalg.inv(
        X.T @ X
    )

    groups = pd.factorize(
        d[cluster_col],
        sort=True,
    )[0]

    G = int(
        groups.max() + 1
    )

    if G <= 1:
        raise ValueError(
            "clustered inference requires "
            "at least two councils"
        )

    meat = np.zeros(
        (k, k),
        dtype=float,
    )

    for g in range(G):
        idx = groups == g
        score = X[idx].T @ u[idx]
        meat += np.outer(
            score, score
        )

    # Follow the declared implementation note:
    # council-year (or council) FE nested in clusters
    # do not count in K; line FE do.
    K = int(
        k + n_line_fe
    )

    if n <= K:
        raise ValueError(
            "small-sample correction undefined: "
            f"N={n}, K={K}"
        )

    factor = (
        (G / (G - 1.0))
        * (
            (n - 1.0)
            / (n - K)
        )
    )

    V = (
        XtX_inv
        @ meat
        @ XtX_inv
        * factor
    )

    se = np.sqrt(
        np.maximum(
            np.diag(V), 0.0
        )
    )

    return {
        "b": b,
        "se": se,
        "V": V,
        "N": int(n),
        "G": G,
        "df": G - 1,
        "rss": float(u @ u),
        "sample": d,
    }


def pvalues(
    coef,
    se,
    df,
):
    if not (
        np.isfinite(coef)
        and np.isfinite(se)
    ):
        return np.nan, np.nan

    if se == 0:
        if coef > 0:
            return 0.0, 0.0
        if coef < 0:
            return 1.0, 0.0
        return 0.5, 1.0

    t = coef / se

    return (
        float(
            stats.t.sf(t, df)
        ),
        float(
            2.0
            * stats.t.sf(
                abs(t), df
            )
        ),
    )


def pt1_verdict(
    beta,
    p_one,
    p_two,
    upper,
):
    if p_one < ALPHA:
        return (
            "H-fixed fails in this system; dynamic priority "
            "earned for institutions of this kind"
        )

    if (
        beta < 0
        and p_two < ALPHA
    ):
        return "Contrary to H-dynamic"

    if upper < BETA_STAR:
        return (
            "H-fixed supported: "
            "no meaningful anticipation"
        )

    return "Inconclusive"


def pt1_shape(
    sample,
    linear_fit,
    fe_columns,
    cluster_col,
    n_line_fe,
):
    n = int(
        linear_fit["N"]
    )

    if n <= 0:
        raise ValueError(
            "PT1-S has no observations"
        )

    rss_lin = float(
        linear_fit["rss"]
    )

    bic_linear = (
        n
        * np.log(
            rss_lin / n
        )
        + 2.0 * np.log(n)
    )

    best = None
    thresholds = []

    for q in np.arange(
        0.1, 1.0, 0.1
    ):
        th = float(
            sample["g_proj"].quantile(
                float(q)
            )
        )

        thresholds.append(th)

        d = sample.copy()
        d["step"] = (
            d["g_proj"] > th
        ).astype(float)

        fit = cluster_fit(
            d,
            "y",
            ["step", "g_real"],
            fe_columns,
            cluster_col,
            n_line_fe,
        )

        if (
            best is None
            or fit["rss"] < best[1]
        ):
            best = (
                th,
                float(fit["rss"]),
            )

    bic_step = (
        n
        * np.log(
            best[1] / n
        )
        + 3.0 * np.log(n)
    )

    if (
        bic_linear
        < bic_step - 2.0
    ):
        shape = "graded"
    elif (
        bic_step
        < bic_linear - 2.0
    ):
        shape = "stepped"
    else:
        shape = "indeterminate"

    return {
        "bic_linear": float(
            bic_linear
        ),
        "bic_step": float(
            bic_step
        ),
        "threshold": float(
            best[0]
        ),
        "shape": shape,
        "candidate_thresholds": [
            float(x)
            for x in thresholds
        ],
    }


def run_pt1(
    panel,
    do_winsor=True,
    fe_columns=("line_id", "cy"),
    cluster_col="ons_code",
):
    d = panel.loc[
        finite_mask(
            panel,
            ["y", "g_proj", "g_real"],
        )
    ].copy()

    if do_winsor:
        d = winsorise(
            d, "y"
        )

    n_lines = int(
        d["line_id"].nunique()
    )

    fit = cluster_fit(
        d,
        "y",
        ["g_proj", "g_real"],
        list(fe_columns),
        cluster_col,
        n_lines,
    )

    beta = float(
        fit["b"][0]
    )
    se = float(
        fit["se"][0]
    )

    p_one, p_two = pvalues(
        beta,
        se,
        fit["df"],
    )

    crit = float(
        stats.t.ppf(
            0.975,
            fit["df"],
        )
    )

    lower = (
        beta - crit * se
    )
    upper = (
        beta + crit * se
    )

    out = {
        "beta": beta,
        "se": se,
        "p_one_sided": p_one,
        "p_two_sided": p_two,
        "ci95": [
            float(lower),
            float(upper),
        ],
        "N": int(fit["N"]),
        "councils": int(
            d[cluster_col].nunique()
        ),
        "lines": n_lines,
        "verdict": pt1_verdict(
            beta,
            p_one,
            p_two,
            upper,
        ),
    }

    if p_one < ALPHA:
        out["PT1_S"] = pt1_shape(
            d,
            fit,
            list(fe_columns),
            cluster_col,
            n_lines,
        )

    return out


def apply_classes(
    panel,
    ambiguous="exclude",
):
    d = panel.copy()
    used = d["cls"].astype(
        object
    ).copy()

    if ambiguous in {
        "lowest", "highest"
    }:
        amb = d[
            "cls"
        ].eq("ambiguous")

        def pick(value):
            vals = [
                x.strip()
                for x in str(
                    value
                ).split("/")
                if x.strip()
                in {"A", "B", "C"}
            ]

            if not vals:
                return np.nan

            # Fixed ordering A > B > C; supplied candidates
            # are written in that order.
            if ambiguous == "lowest":
                return vals[-1]
            return vals[0]

        used.loc[amb] = d.loc[
            amb, "candidates"
        ].map(pick)

    d["cls_used"] = used

    d = d.loc[
        d["cls_used"].isin(
            ["A", "B", "C"]
        )
    ].copy()

    d["A"] = d[
        "cls_used"
    ].eq("A").astype(float)

    d["B"] = d[
        "cls_used"
    ].eq("B").astype(float)

    return d


def run_g25(
    panel,
    ambiguous="exclude",
    do_winsor=True,
):
    d = apply_classes(
        panel, ambiguous
    )

    d = d.loc[
        finite_mask(
            d,
            ["y", "g_real"],
        )
    ].copy()

    if do_winsor:
        d = winsorise(
            d, "y"
        )

    fit = cluster_fit(
        d,
        "y",
        ["A", "B", "g_real"],
        ["cy"],
        "ons_code",
        0,
    )

    dA = float(
        fit["b"][0]
    )
    dB = float(
        fit["b"][1]
    )
    seA = float(
        fit["se"][0]
    )
    seB = float(
        fit["se"][1]
    )

    var_diff = float(
        fit["V"][0, 0]
        + fit["V"][1, 1]
        - 2.0 * fit["V"][0, 1]
    )

    se_diff = float(
        np.sqrt(
            max(var_diff, 0.0)
        )
    )

    pA, pA2 = pvalues(
        dA,
        seA,
        fit["df"],
    )
    pB, pB2 = pvalues(
        dB,
        seB,
        fit["df"],
    )
    pAB, pAB2 = pvalues(
        dA - dB,
        se_diff,
        fit["df"],
    )

    if (
        pA < ALPHA
        and dA >= dB >= 0
    ):
        verdict = "Supported"
    elif pA < ALPHA:
        verdict = "Partly supported"
    elif (
        dA < 0
        and pA2 < ALPHA
    ):
        verdict = "Contradicted"
    else:
        verdict = "Fails"

    return {
        "delta_A": dA,
        "delta_B": dB,
        "se_A": seA,
        "se_B": seB,
        "p_A": pA,
        "p_A_two_sided": pA2,
        "p_B": pB,
        "p_B_two_sided": pB2,
        "p_A_minus_B": pAB,
        "p_A_minus_B_two_sided": pAB2,
        "N": int(fit["N"]),
        "councils": int(
            fit["G"]
        ),
        "verdict": verdict,
        "weight": 0.5,
    }


def scarcity_map(inputs):
    csp = inputs["csp"].copy()

    csp = csp.loc[
        csp["year"].isin(
            [2015, 2019]
        )
    ].copy()

    strict_unique(
        csp,
        ["ons_code", "year"],
        "CSP table",
    )

    csp[
        "csp_thousands"
    ] = pd.to_numeric(
        csp["csp_thousands"],
        errors="coerce",
    )

    cpi = cpi_lookup(
        inputs["cpi"]
    )

    csp["real_csp"] = (
        csp["csp_thousands"]
        / (
            csp["year"].map(cpi)
            / float(cpi.loc[2014])
        )
    )

    pop = inputs["pop"].loc[
        (
            inputs["pop"]["group"]
            .eq("all")
        )
        & (
            inputs["pop"]["year"]
            .isin([2015, 2019])
        ),
        [
            "ons_code",
            "year",
            "population",
        ],
    ].copy()

    strict_unique(
        pop,
        ["ons_code", "year"],
        "total-population table for scarcity",
    )

    pop["population"] = pd.to_numeric(
        pop["population"],
        errors="coerce",
    )

    csp = csp.merge(
        pop,
        on=["ons_code", "year"],
        how="left",
        validate="one_to_one",
    )

    csp["pc"] = np.where(
        (
            csp["real_csp"] > 0
        )
        & (
            csp["population"] > 0
        ),
        (
            csp["real_csp"]
            / csp["population"]
        ),
        np.nan,
    )

    wide = csp.pivot(
        index="ons_code",
        columns="year",
        values="pc",
    )

    if (
        2015 not in wide
        or 2019 not in wide
    ):
        return pd.Series(
            dtype=float
        )

    # Larger scarcity = deeper fall.
    out = -(
        np.log(wide[2019])
        - np.log(wide[2015])
    )

    return out


def run_g25c(
    panel,
    inputs,
    do_winsor=True,
    ambiguous="exclude",
):
    d = apply_classes(
        panel, ambiguous
    )

    d = d.loc[
        finite_mask(
            d,
            ["y", "g_real"],
        )
    ].copy()

    scar = scarcity_map(
        inputs
    )

    d["scarcity"] = d[
        "ons_code"
    ].map(scar)

    d = d.loc[
        finite_mask(
            d, ["scarcity"]
        )
    ].copy()

    d["A_x_scar"] = (
        d["A"]
        * d["scarcity"]
    )

    # Frozen rule: winsorise the pooled sample of the model
    # actually estimated, so missing-scarcity rows are removed
    # before calculating the cut points.
    if do_winsor:
        d = winsorise(
            d, "y"
        )

    fit = cluster_fit(
        d,
        "y",
        [
            "A",
            "B",
            "A_x_scar",
            "g_real",
        ],
        ["cy"],
        "ons_code",
        0,
    )

    b = float(
        fit["b"][2]
    )
    se = float(
        fit["se"][2]
    )

    p_one, p_two = pvalues(
        b,
        se,
        fit["df"],
    )

    return {
        "interaction": b,
        "se": se,
        "p_one_sided": p_one,
        "p_two_sided": p_two,
        "N": int(fit["N"]),
        "councils": int(
            fit["G"]
        ),
        "verdict": (
            "Supported"
            if p_one < ALPHA
            else "Not supported"
        ),
        "weight": 0.5,
    }


def run_ss(panel):
    """Descriptive strict/shared statistic.

    The denominator uses all retained in-scope series, including
    ambiguous statutory lines. The original code called its G25
    class filter first, which excluded ambiguous lines from
    "total in-scope" spending.

    For "base-year spending", follow the implementation note's
    explicit reading: the fixed 2014-15 C-class real total.
    """
    p = panel.copy()

    totals = (
        p.groupby(
            ["ons_code", "year"]
        )["real"]
        .sum(min_count=1)
        .unstack()
    )

    c_base = (
        p.loc[
            p["cls"].eq("C")
            & p["year"].eq(2014)
        ]
        .groupby(
            "ons_code"
        )["real"]
        .sum(min_count=1)
    )

    hits = 0
    eligible = 0

    for code in totals.index:
        for year in range(
            2015, 2020
        ):
            if (
                year not in totals.columns
                or year - 1
                not in totals.columns
            ):
                continue

            now = totals.loc[
                code, year
            ]
            prev = totals.loc[
                code, year - 1
            ]

            if not (
                np.isfinite(now)
                and np.isfinite(prev)
                and now < prev
            ):
                continue

            eligible += 1

            a = p.loc[
                p["ons_code"].eq(code)
                & p["cls"].eq("A"),
                [
                    "line_id",
                    "year",
                    "real",
                ],
            ]

            if len(a):
                aw = a.pivot(
                    index="line_id",
                    columns="year",
                    values="real",
                )

                if (
                    year in aw.columns
                    and year - 1
                    in aw.columns
                ):
                    a_fell = bool(
                        (
                            aw[year]
                            < aw[year - 1]
                        )
                        .fillna(False)
                        .any()
                    )
                else:
                    a_fell = False
            else:
                a_fell = False

            c_now = p.loc[
                p["ons_code"].eq(code)
                & p["cls"].eq("C")
                & p["year"].eq(year),
                "real",
            ].sum(min_count=1)

            base = c_base.get(
                code, np.nan
            )

            if (
                a_fell
                and np.isfinite(base)
                and base > 0
                and np.isfinite(c_now)
                and c_now
                > 0.5 * base
            ):
                hits += 1

    return {
        "council_years_with_in_scope_real_spending_fall":
            int(eligible),
        "hits": int(hits),
        "share_A_fell_while_C_kept_over_half":
            (
                float(
                    hits / eligible
                )
                if eligible
                else None
            ),
        "base_year_for_C": 2014,
        "verdict": None,
    }


def suite(
    panel,
    inputs,
    do_winsor=True,
    include_ss=True,
):
    out = {
        "PT1": run_pt1(
            panel,
            do_winsor=do_winsor,
        ),
        "G25": run_g25(
            panel,
            do_winsor=do_winsor,
        ),
        "G25_C": run_g25c(
            panel,
            inputs,
            do_winsor=do_winsor,
        ),
    }

    if include_ss:
        out["SS"] = run_ss(
            panel
        )

    return out


def make_long_difference(panel):
    base = panel.loc[
        panel["year"].eq(2014)
    ].set_index(
        ["ons_code", "line_id"]
    )

    end = panel.loc[
        panel["year"].eq(2019)
    ].set_index(
        ["ons_code", "line_id"]
    )

    j = (
        base[
            ["lnpc", "lnP", "g_proj"]
        ]
        .join(
            end[
                ["lnpc", "lnP"]
            ],
            how="inner",
            rsuffix="_2019",
        )
        .reset_index()
    )

    j["y"] = (
        j["lnpc_2019"]
        - j["lnpc"]
    )

    j["g_real"] = (
        j["lnP_2019"]
        - j["lnP"]
    )

    # Not used in this specification; council itself is the
    # long-difference fixed effect.
    j["cy"] = j["ons_code"]

    return j


def run_long_difference(panel):
    j = make_long_difference(
        panel
    )

    # One observation per council-line. The natural
    # long-difference analogue of line + council-year FE
    # is line + council FE.
    return run_pt1(
        j,
        do_winsor=True,
        fe_columns=(
            "line_id",
            "ons_code",
        ),
        cluster_col="ons_code",
    )


def sensitivity_results(
    inputs,
    primary_panel,
    primary_counts,
):
    out = {}

    # 1. Adult social care included.
    p1, c1 = build_panel(
        inputs,
        extras=(
            ("RO3", 60),
        ),
    )

    out[
        "1_adult_social_care_included"
    ] = {
        "counts": c1,
        **suite(
            p1, inputs
        ),
    }

    # 2. Long difference.
    out[
        "2_long_difference"
    ] = {
        "counts": primary_counts,
        "PT1": run_long_difference(
            primary_panel
        ),
    }

    # 3. Ambiguous lines in G25 at their lowest/highest
    # candidate statutory class.
    out[
        "3_ambiguous_lowest"
    ] = {
        "counts": primary_counts,
        "G25": run_g25(
            primary_panel,
            ambiguous="lowest",
        ),
    }

    out[
        "3_ambiguous_highest"
    ] = {
        "counts": primary_counts,
        "G25": run_g25(
            primary_panel,
            ambiguous="highest",
        ),
    }

    # 4. RO6 client-facing lines.
    p4, c4 = build_panel(
        inputs,
        extras=(
            ("RO6", 430),
            ("RO6", 441),
            ("RO6", 442),
            ("RO6", 460),
            ("RO6", 475),
        ),
    )

    out[
        "4_RO6_client_facing_lines_included"
    ] = {
        "counts": c4,
        **suite(
            p4, inputs
        ),
    }

    # 5. Ten-year projected growth.
    p5, c5 = build_panel(
        inputs,
        horizon=10,
    )

    out[
        "5_ten_year_projected_growth"
    ] = {
        "counts": c5,
        "PT1": run_pt1(p5),
    }

    # 6. No winsorisation.
    out[
        "6_no_winsorising"
    ] = {
        "counts": primary_counts,
        "PT1": run_pt1(
            primary_panel,
            do_winsor=False,
        ),
        "G25": run_g25(
            primary_panel,
            do_winsor=False,
        ),
        "G25_C": run_g25c(
            primary_panel,
            inputs,
            do_winsor=False,
        ),
        # SS never uses winsorisation; included for a complete
        # sensitivity record.
        "SS": run_ss(
            primary_panel
        ),
    }

    # 7. London boroughs excluded. Use the explicit la_type
    # field rather than inferring borough status from code prefix.
    london_codes = set(
        primary_panel.loc[
            primary_panel[
                "la_type"
            ].eq("LB"),
            "ons_code",
        ].unique()
    )

    non_london = (
        set(
            primary_panel[
                "ons_code"
            ].unique()
        )
        - london_codes
    )

    p7, c7 = build_panel(
        inputs,
        council_subset=non_london,
    )

    out[
        "7_london_boroughs_excluded"
    ] = {
        "counts": c7,
        **suite(
            p7, inputs
        ),
    }

    # 8. Alternative minimum real-NCE thresholds.
    for minimum in (
        50.0, 250.0
    ):
        p8, c8 = build_panel(
            inputs,
            min_mean=minimum,
        )

        out[
            f"8_minimum_{int(minimum)}_thousand"
        ] = {
            "counts": c8,
            **suite(
                p8, inputs
            ),
        }

    return out


def json_clean(value):
    if isinstance(
        value, dict
    ):
        return {
            str(k): json_clean(v)
            for k, v in value.items()
        }

    if isinstance(
        value, (list, tuple)
    ):
        return [
            json_clean(v)
            for v in value
        ]

    if isinstance(
        value, np.integer
    ):
        return int(value)

    if isinstance(
        value, (np.floating, float)
    ):
        x = float(value)
        return (
            x
            if np.isfinite(x)
            else None
        )

    if isinstance(
        value, np.bool_
    ):
        return bool(value)

    return value


def main():
    ap = argparse.ArgumentParser()

    ap.add_argument(
        "--data",
        required=True,
        help=(
            "directory containing spend.csv, pop.csv, "
            "proj.csv, csp.csv, cpi.csv"
        ),
    )

    ap.add_argument(
        "--cls",
        required=True,
        help="statutory classification CSV",
    )

    ap.add_argument(
        "--out",
        required=True,
        help="output directory",
    )

    args = ap.parse_args()

    inputs = read_inputs(
        args.data,
        args.cls,
    )

    panel, counts = build_panel(
        inputs
    )

    result = {
        "counts": counts,
        **suite(
            panel, inputs
        ),
        "sensitivity":
            sensitivity_results(
                inputs,
                panel,
                counts,
            ),
        "implementation": {
            "fixed_effect_absorption": (
                "Frisch-Waugh-Lovell projection on sparse FE "
                "dummy matrix using scipy.sparse.linalg.lsqr"
            ),
            "cluster": "council",
            "cluster_df": "G-1",
            "cluster_small_sample_factor": (
                "G/(G-1) * (N-1)/(N-K), with nested "
                "council-year/council FE excluded from K "
                "and line FE counted"
            ),
            "ss_total_spending_fix": (
                "ambiguous statutory lines remain in total "
                "in-scope spending; only A/C labels are used "
                "for the hit condition"
            ),
        },
    }

    result = json_clean(
        result
    )

    os.makedirs(
        args.out,
        exist_ok=True,
    )

    path = os.path.join(
        args.out,
        "check.json",
    )

    with open(
        path,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            result,
            f,
            indent=2,
            ensure_ascii=False,
            allow_nan=False,
        )

    print(path)


if __name__ == "__main__":
    main()
