# Written by GPT (raw/2026-10-06_chatgpt_H1-VDB-R1.md, Part B), extracted verbatim. Not edited.
import argparse
import json
import os

import numpy as np
import pandas as pd
from scipy import stats


GRID_S = 2.0
BIN_S = 10.0
POINTS_PER_BIN = 5
HYPOTENSION = 65.0

APPROACH_S = 31 * 60.0
CONTROL_AFTER_S = 30 * 60.0
WINDOW_S = 10 * 60.0
EARLY_START_S = 31 * 60.0
EARLY_END_S = 21 * 60.0

MIN_CASES = 20

PRESSURE_TRACKS = {
    "map": "Solar8000/ART_MBP",
    "sbp": "Solar8000/ART_SBP",
    "dbp": "Solar8000/ART_DBP",
}

INFUSION_DRUGS = ("PHEN", "NEPI", "EPI", "VASO", "DOPA", "DOBU")

PRIMARY_SETTINGS = {
    "gap_points": 5,
    "sustain_bins": 6,
    "late_end_s": 60.0,
    "fallback": False,
}


class Repository:
    def __init__(self, root):
        self.root = root
        self.cases = pd.read_csv(os.path.join(root, "cases.csv"))
        self.labs = pd.read_csv(os.path.join(root, "labs.csv"))
        self.tracks = pd.read_csv(os.path.join(root, "trks.csv"))

        for col in ("caseid", "dt", "result"):
            if col in self.labs.columns:
                self.labs[col] = pd.to_numeric(
                    self.labs[col], errors="coerce"
                )

        self.track_id = {}
        for row in self.tracks.itertuples(index=False):
            self.track_id[(int(row.caseid), str(row.tname))] = row.tid

    def lists_track(self, caseid, name):
        return (int(caseid), name) in self.track_id

    def load_track(self, caseid, name):
        tid = self.track_id.get((int(caseid), name))
        if tid is None:
            return None

        path = os.path.join(
            self.root, "tracks", f"{tid}.csv.gz"
        )
        if not os.path.exists(path):
            return None

        frame = pd.read_csv(
            path, compression="gzip"
        ).iloc[:, :2].copy()
        frame.columns = ["time", "value"]
        frame["time"] = pd.to_numeric(
            frame["time"], errors="coerce"
        )
        frame["value"] = pd.to_numeric(
            frame["value"], errors="coerce"
        )
        frame = frame.dropna().sort_values("time")

        return (
            frame["time"].to_numpy(float),
            frame["value"].to_numpy(float),
        )


def numeric_case_columns(frame):
    out = frame.copy()
    cols = (
        "caseid",
        "weight",
        "opstart",
        "opend",
        "intraop_ebl",
        "intraop_phe",
        "intraop_eph",
        "intraop_epi",
    )
    for col in cols:
        out[col] = pd.to_numeric(
            out[col], errors="coerce"
        )
    return out


def blood_loss_share(row):
    sex = str(row.sex).strip().upper()

    if sex == "M":
        ml_per_kg = 70.0
    elif sex == "F":
        ml_per_kg = 65.0
    else:
        return np.nan

    if (
        not np.isfinite(row.weight)
        or not np.isfinite(row.intraop_ebl)
        or row.weight <= 0
    ):
        return np.nan

    return (
        float(row.intraop_ebl)
        / (ml_per_kg * float(row.weight))
    )


def eligible_cases(repo, fallback):
    cases = numeric_case_columns(repo.cases)

    # Implementation note: case-insensitive word "general".
    general = cases["ane_type"].astype(str).str.contains(
        r"\bgeneral\b",
        case=False,
        regex=True,
        na=False,
    )

    pressure_tracks = cases.apply(
        lambda row: all(
            repo.lists_track(row.caseid, name)
            for name in PRESSURE_TRACKS.values()
        ),
        axis=1,
    )

    recorded = (
        cases["intraop_ebl"].notna()
        & cases["weight"].notna()
        & cases["sex"].notna()
    )

    duration_ok = (
        cases["opend"] - cases["opstart"]
    ) >= 90.0 * 60.0

    keep = (
        general
        & pressure_tracks
        & recorded
        & duration_ok
    )

    if not fallback:
        keep &= (
            cases["intraop_phe"].notna()
            & (cases["intraop_phe"] == 0)
            & cases["intraop_eph"].notna()
            & (cases["intraop_eph"] == 0)
            & cases["intraop_epi"].notna()
            & (cases["intraop_epi"] == 0)
        )

    cases = cases.loc[keep].copy()
    cases["ebv_share"] = cases.apply(
        blood_loss_share, axis=1
    )

    return cases.loc[
        cases["ebv_share"].notna()
    ].copy()


def snap_to_grid(times, values, start, n_points):
    out = np.full(
        n_points, np.nan, dtype=float
    )

    if times is None or len(times) == 0:
        return out

    index = np.rint(
        (times - start) / GRID_S
    ).astype(np.int64)

    near = (
        (index >= 0)
        & (index < n_points)
        & (
            np.abs(
                times
                - (start + index * GRID_S)
            )
            <= 1.0 + 1e-9
        )
    )

    if not np.any(near):
        return out

    tmp = pd.DataFrame(
        {
            "i": index[near],
            "v": values[near],
        }
    )

    means = tmp.groupby(
        "i", sort=True
    )["v"].mean()

    out[
        means.index.to_numpy(int)
    ] = means.to_numpy(float)

    return out


def fill_short_internal_gaps(values, max_points):
    y = values.copy()

    if max_points <= 0:
        return y

    missing = np.isnan(y)
    i = 0

    while i < len(y):
        if not missing[i]:
            i += 1
            continue

        j = i + 1
        while (
            j < len(y)
            and missing[j]
        ):
            j += 1

        if (
            i > 0
            and j < len(y)
            and (j - i) <= max_points
        ):
            y[i:j] = np.interp(
                np.arange(
                    i, j, dtype=float
                ),
                np.array(
                    [i - 1, j],
                    dtype=float,
                ),
                np.array(
                    [y[i - 1], y[j]],
                    dtype=float,
                ),
            )

        i = j

    return y


def ten_second_means(grid_values):
    n_bins = (
        len(grid_values)
        // POINTS_PER_BIN
    )

    if n_bins == 0:
        return np.array(
            [], dtype=float
        )

    block = grid_values[
        : n_bins * POINTS_PER_BIN
    ].reshape(
        n_bins,
        POINTS_PER_BIN,
    )

    valid_n = np.sum(
        np.isfinite(block),
        axis=1,
    )

    sums = np.nansum(
        block, axis=1
    )

    return np.where(
        valid_n > 0,
        sums / np.maximum(valid_n, 1),
        np.nan,
    )


def build_pressure_case(
    row,
    repo,
    gap_points,
):
    opstart = float(row.opstart)
    opend = float(row.opend)

    n_points = (
        int(
            np.floor(
                (opend - opstart)
                / GRID_S
            )
        )
        + 1
    )

    grids = {}

    for key, track_name in (
        PRESSURE_TRACKS.items()
    ):
        loaded = repo.load_track(
            int(row.caseid),
            track_name,
        )

        if loaded is None:
            grids[key] = np.full(
                n_points, np.nan
            )
        else:
            grids[key] = snap_to_grid(
                loaded[0],
                loaded[1],
                opstart,
                n_points,
            )

    m = grids["map"]
    s = grids["sbp"]
    d = grids["dbp"]

    valid = (
        np.isfinite(m)
        & np.isfinite(s)
        & np.isfinite(d)
        & (m >= 20.0)
        & (m <= 200.0)
        & (s <= 300.0)
        & ((s - d) >= 10.0)
    )

    raw_map = np.where(
        valid,
        m,
        np.nan,
    )

    filled_map = (
        fill_short_internal_gaps(
            raw_map,
            gap_points,
        )
    )

    return {
        "caseid": int(row.caseid),
        "opstart": opstart,
        "opend": opend,
        "mid": (
            opstart + opend
        ) / 2.0,
        "ebv_share": float(
            row.ebv_share
        ),
        "map_raw": raw_map,
        "map_filled": filled_map,
        "map_bins": ten_second_means(
            filled_map
        ),
    }


def grid_index(case, time_s):
    return int(
        np.rint(
            (
                time_s
                - case["opstart"]
            )
            / GRID_S
        )
    )


def bin_index(case, time_s):
    return int(
        np.rint(
            (
                time_s
                - case["opstart"]
            )
            / BIN_S
        )
    )


def measurement_window(
    case,
    start,
    stop,
):
    if (
        start
        < case["opstart"] - 1e-9
        or stop
        > case["opend"] + 1e-9
        or stop <= start
    ):
        return None

    ga = grid_index(
        case, start
    )
    gb = grid_index(
        case, stop
    )

    grid = case[
        "map_filled"
    ][ga:gb]

    expected_grid = int(
        round(
            (stop - start)
            / GRID_S
        )
    )

    if (
        len(grid)
        != expected_grid
        or len(grid) == 0
    ):
        return None

    if (
        np.mean(
            ~np.isfinite(grid)
        )
        > 0.10
    ):
        return None

    ba = bin_index(
        case, start
    )
    bb = bin_index(
        case, stop
    )

    values = case[
        "map_bins"
    ][ba:bb].copy()

    expected_bins = int(
        round(
            (stop - start)
            / BIN_S
        )
    )

    if len(values) != expected_bins:
        return None

    # Deliberate correction to the supplied
    # implementation note. A remaining
    # missing 10-s bin arises from a gap
    # longer than the permitted 10 s, so
    # it is NOT interpolated here.
    return values


def window_pair(
    case,
    onset,
    late_end_s,
):
    early = measurement_window(
        case,
        onset - EARLY_START_S,
        onset - EARLY_END_S,
    )

    late = measurement_window(
        case,
        onset
        - (
            WINDOW_S
            + late_end_s
        ),
        onset - late_end_s,
    )

    return early, late


def fallback_bolus_signature(
    values,
):
    for i in range(
        1, len(values)
    ):
        if not np.isfinite(
            values[i]
        ):
            continue

        prior = values[
            max(0, i - 6):i
        ]

        prior = prior[
            np.isfinite(prior)
        ]

        if (
            len(prior)
            and (
                values[i]
                - np.min(prior)
                > 15.0
            )
        ):
            return True

    return False


def sustained_fall_onsets(
    case,
    sustain_bins,
):
    below = (
        np.isfinite(
            case["map_bins"]
        )
        & (
            case["map_bins"]
            < HYPOTENSION
        )
    )

    onsets = []
    i = 0

    while i < len(below):
        if not below[i]:
            i += 1
            continue

        j = i + 1

        while (
            j < len(below)
            and below[j]
        ):
            j += 1

        if (
            j - i
            >= sustain_bins
        ):
            onsets.append(
                case["opstart"]
                + i * BIN_S
            )

        i = j

    return onsets


def approach_is_stable(
    case,
    onset,
):
    a = bin_index(
        case,
        onset - APPROACH_S,
    )
    b = bin_index(
        case,
        onset,
    )

    values = case[
        "map_bins"
    ][a:b]

    expected = int(
        APPROACH_S / BIN_S
    )

    # Frozen rule says EVERY bin is
    # at or above 65. Missing bins
    # therefore cannot be discarded.
    return (
        len(values) == expected
        and np.all(
            np.isfinite(values)
        )
        and np.all(
            values >= HYPOTENSION
        )
    )


def first_qualifying_break(
    case,
    settings,
):
    onsets = sustained_fall_onsets(
        case,
        settings[
            "sustain_bins"
        ],
    )

    for onset in onsets:
        if not (
            case["mid"]
            < onset
            < case["opend"]
        ):
            continue

        if (
            onset - APPROACH_S
            < case["opstart"]
        ):
            continue

        if not approach_is_stable(
            case, onset
        ):
            continue

        early, late = window_pair(
            case,
            onset,
            settings[
                "late_end_s"
            ],
        )

        if (
            early is None
            or late is None
        ):
            continue

        if (
            settings["fallback"]
            and (
                fallback_bolus_signature(
                    early
                )
                or fallback_bolus_signature(
                    late
                )
            )
        ):
            continue

        return {
            "onset": float(onset),
            "early": early,
            "late": late,
        }

    return None


def control_interval_clear(
    case,
    onset,
):
    a = bin_index(
        case,
        onset - APPROACH_S,
    )
    b = bin_index(
        case,
        onset
        + CONTROL_AFTER_S,
    )

    values = case[
        "map_bins"
    ][a:b]

    return not np.any(
        np.isfinite(values)
        & (
            values
            < HYPOTENSION
        )
    )


def control_windows(
    case,
    settings,
):
    controls = []
    k = 0

    while True:
        onset = (
            case["mid"]
            + 300.0 * k
        )
        k += 1

        if (
            onset
            + CONTROL_AFTER_S
            > case["opend"]
        ):
            break

        if (
            onset - APPROACH_S
            < case["opstart"]
        ):
            continue

        if not control_interval_clear(
            case, onset
        ):
            continue

        early, late = window_pair(
            case,
            onset,
            settings[
                "late_end_s"
            ],
        )

        if (
            early is None
            or late is None
        ):
            continue

        if (
            settings["fallback"]
            and (
                fallback_bolus_signature(
                    early
                )
                or fallback_bolus_signature(
                    late
                )
            )
        ):
            continue

        controls.append(
            {
                "onset": float(onset),
                "early": early,
                "late": late,
            }
        )

    return controls


def process_candidates(
    repo,
    eligible,
    settings,
):
    candidates = eligible.loc[
        (
            eligible["ebv_share"]
            >= 0.15
        )
        | (
            eligible["ebv_share"]
            <= 0.05
        )
    ]

    out = {}

    for row in candidates.itertuples(
        index=False
    ):
        case = build_pressure_case(
            row,
            repo,
            settings["gap_points"],
        )

        out[int(row.caseid)] = {
            "case": case,
            "break": (
                first_qualifying_break(
                    case,
                    settings,
                )
            ),
            "controls": (
                control_windows(
                    case,
                    settings,
                )
            ),
        }

    return out


def group_ids(
    processed,
    high_threshold,
):
    high = []
    low = []

    for cid, record in (
        processed.items()
    ):
        qualifies = (
            record["break"]
            is not None
            and len(
                record["controls"]
            )
            > 0
        )

        if not qualifies:
            continue

        share = record[
            "case"
        ]["ebv_share"]

        if share >= high_threshold:
            high.append(cid)
        elif share <= 0.05:
            low.append(cid)

    return high, low


def count_design(repo):
    rows = []

    for fallback in (
        False, True
    ):
        cohort = (
            "fallback"
            if fallback
            else "primary"
        )

        eligible = eligible_cases(
            repo,
            fallback=fallback,
        )

        settings = dict(
            PRIMARY_SETTINGS
        )
        settings[
            "fallback"
        ] = fallback

        processed = (
            process_candidates(
                repo,
                eligible,
                settings,
            )
        )

        high20, low20 = group_ids(
            processed,
            0.20,
        )

        rows.append(
            {
                "cohort": cohort,
                "threshold": 0.20,
                "eligible": int(
                    len(eligible)
                ),
                "high_qualifying": int(
                    len(high20)
                ),
                "low_qualifying": int(
                    len(low20)
                ),
            }
        )

        if (
            len(high20)
            >= MIN_CASES
            and len(low20)
            >= MIN_CASES
        ):
            return {
                "runnable": True,
                "cohort": cohort,
                "threshold": 0.20,
                "counts": rows,
            }

        # Frozen rule: when the high
        # group is short, step down once.
        # Record this count even when the
        # low group is also short.
        if (
            len(high20)
            < MIN_CASES
        ):
            high15, low15 = (
                group_ids(
                    processed,
                    0.15,
                )
            )

            rows.append(
                {
                    "cohort": cohort,
                    "threshold": 0.15,
                    "eligible": int(
                        len(eligible)
                    ),
                    "high_qualifying": int(
                        len(high15)
                    ),
                    "low_qualifying": int(
                        len(low15)
                    ),
                }
            )

            if (
                len(high15)
                >= MIN_CASES
                and len(low15)
                >= MIN_CASES
            ):
                return {
                    "runnable": True,
                    "cohort": cohort,
                    "threshold": 0.15,
                    "counts": rows,
                }

        # Only after primary is not
        # runnable may fallback be tried.
        if not fallback:
            continue

    return {
        "runnable": False,
        "cohort": None,
        "threshold": None,
        "counts": rows,
    }


def residuals_with_missing(
    values,
):
    values = np.asarray(
        values, dtype=float
    )
    x = np.arange(
        len(values),
        dtype=float,
    )

    good = np.isfinite(values)

    residual = np.full(
        len(values),
        np.nan,
    )

    if np.sum(good) < 2:
        return residual

    slope, intercept = np.polyfit(
        x[good],
        values[good],
        1,
    )

    residual[good] = (
        values[good]
        - (
            slope * x[good]
            + intercept
        )
    )

    return residual


def ar1_value(values):
    residual = (
        residuals_with_missing(
            values
        )
    )

    paired = (
        np.isfinite(
            residual[:-1]
        )
        & np.isfinite(
            residual[1:]
        )
    )

    a = residual[:-1][paired]
    b = residual[1:][paired]

    if (
        len(a) < 2
        or np.std(a) < 1e-12
        or np.std(b) < 1e-12
    ):
        return np.nan

    return float(
        np.corrcoef(a, b)[0, 1]
    )


def sd_value(values):
    residual = (
        residuals_with_missing(
            values
        )
    )

    finite = residual[
        np.isfinite(residual)
    ]

    if len(finite) < 2:
        return np.nan

    value = float(
        np.std(
            finite,
            ddof=1,
        )
    )

    if value <= 1e-12:
        return np.nan

    return value


def pair_change(
    pair,
    measure,
):
    if measure == "ar1":
        early = ar1_value(
            pair["early"]
        )
        late = ar1_value(
            pair["late"]
        )

        if (
            not np.isfinite(early)
            or not np.isfinite(late)
        ):
            return np.nan

        return float(
            late - early
        )

    early = sd_value(
        pair["early"]
    )
    late = sd_value(
        pair["late"]
    )

    if (
        not np.isfinite(early)
        or not np.isfinite(late)
        or early <= 0
        or late <= 0
    ):
        return np.nan

    return float(
        np.log(late)
        - np.log(early)
    )


def case_score(
    record,
    measure,
):
    break_change = pair_change(
        record["break"],
        measure,
    )

    control_changes = [
        pair_change(
            pair,
            measure,
        )
        for pair
        in record["controls"]
    ]

    control_changes = np.asarray(
        [
            value
            for value
            in control_changes
            if np.isfinite(value)
        ],
        dtype=float,
    )

    if (
        not np.isfinite(
            break_change
        )
        or len(
            control_changes
        )
        == 0
    ):
        return np.nan

    return float(
        break_change
        - np.median(
            control_changes
        )
    )


def wilcoxon_summary(
    values,
    include_two_sided,
):
    x = np.asarray(
        [
            value
            for value in values
            if np.isfinite(value)
        ],
        dtype=float,
    )

    median = (
        float(np.median(x))
        if len(x)
        else None
    )

    out = {
        "n": int(len(x)),
        "median": median,
        "p": None,
    }

    if include_two_sided:
        out[
            "two_sided_p"
        ] = None

    if len(x) == 0:
        return out

    if np.all(x == 0):
        # The signed-rank statistic is
        # degenerate, but median D == 0
        # is explicitly a frozen failure.
        out["p"] = 1.0

        if include_two_sided:
            out[
                "two_sided_p"
            ] = 1.0

        return out

    try:
        out["p"] = float(
            stats.wilcoxon(
                x,
                alternative="greater",
            ).pvalue
        )

        if include_two_sided:
            out[
                "two_sided_p"
            ] = float(
                stats.wilcoxon(
                    x,
                    alternative=(
                        "two-sided"
                    ),
                ).pvalue
            )
    except ValueError:
        pass

    return out


def mann_whitney_summary(
    high_values,
    low_values,
):
    high = np.asarray(
        [
            value
            for value
            in high_values
            if np.isfinite(value)
        ],
        dtype=float,
    )

    low = np.asarray(
        [
            value
            for value
            in low_values
            if np.isfinite(value)
        ],
        dtype=float,
    )

    out = {
        "n_high": int(len(high)),
        "n_low": int(len(low)),
        "median_high": (
            float(
                np.median(high)
            )
            if len(high)
            else None
        ),
        "median_low": (
            float(
                np.median(low)
            )
            if len(low)
            else None
        ),
        "p": None,
    }

    if (
        len(high)
        and len(low)
    ):
        out["p"] = float(
            stats.mannwhitneyu(
                high,
                low,
                alternative="greater",
            ).pvalue
        )

    return out


def frozen_verdict(p1, p2):
    median = p1["median"]

    if median is None:
        return "not computable"

    if (
        median < 0
        and p1.get(
            "two_sided_p"
        )
        is not None
        and p1[
            "two_sided_p"
        ]
        < 0.05
    ):
        return "Contradicted"

    if median <= 0:
        return "Fails"

    if p1["p"] is None:
        return "not computable"

    if p1["p"] >= 0.05:
        return "Fails"

    if p2["p"] is None:
        return "not computable"

    if p2["p"] < 0.05:
        return "Supported"

    return "Narrowed"


def score_groups(
    processed,
    high_ids,
    low_ids,
):
    high_ar = {
        cid: case_score(
            processed[cid],
            "ar1",
        )
        for cid in high_ids
    }

    low_ar = {
        cid: case_score(
            processed[cid],
            "ar1",
        )
        for cid in low_ids
    }

    high_sd = {
        cid: case_score(
            processed[cid],
            "lnsd",
        )
        for cid in high_ids
    }

    p1_raw = wilcoxon_summary(
        high_ar.values(),
        include_two_sided=True,
    )

    p1 = {
        "n": p1_raw["n"],
        "median": (
            p1_raw["median"]
        ),
        "one_sided_p": (
            p1_raw["p"]
        ),
        "two_sided_p": (
            p1_raw[
                "two_sided_p"
            ]
        ),
    }

    p2 = mann_whitney_summary(
        high_ar.values(),
        low_ar.values(),
    )

    p3_raw = wilcoxon_summary(
        high_sd.values(),
        include_two_sided=False,
    )

    p3 = {
        "n": p3_raw["n"],
        "median": (
            p3_raw["median"]
        ),
        "p": p3_raw["p"],
    }

    verdict_p1 = {
        "median": p1["median"],
        "p": p1[
            "one_sided_p"
        ],
        "two_sided_p": p1[
            "two_sided_p"
        ],
    }

    return {
        "high_ar": high_ar,
        "low_ar": low_ar,
        "high_sd": high_sd,
        "P1": p1,
        "P2": p2,
        "P3": p3,
        "verdict": (
            frozen_verdict(
                verdict_p1,
                p2,
            )
        ),
    }


def analyze_variant(
    repo,
    fallback,
    threshold,
    changes=None,
):
    settings = dict(
        PRIMARY_SETTINGS
    )
    settings[
        "fallback"
    ] = fallback

    if changes:
        settings.update(changes)

    eligible = eligible_cases(
        repo,
        fallback=fallback,
    )

    processed = (
        process_candidates(
            repo,
            eligible,
            settings,
        )
    )

    high, low = group_ids(
        processed,
        threshold,
    )

    scored = score_groups(
        processed,
        high,
        low,
    )

    return (
        eligible,
        processed,
        high,
        low,
        scored,
        settings,
    )


def infusion_changed(
    repo,
    caseid,
    onset,
):
    start = (
        onset - APPROACH_S
    )

    for drug in INFUSION_DRUGS:
        loaded = repo.load_track(
            caseid,
            f"Orchestra/{drug}_RATE",
        )

        if loaded is None:
            continue

        time, value = loaded

        before = np.flatnonzero(
            time < start
        )

        inside = (
            (time >= start)
            & (time <= onset)
        )

        values = list(
            value[inside]
        )

        if len(before):
            values.insert(
                0,
                value[
                    before[-1]
                ],
            )

        if (
            len(values) >= 2
            and np.any(
                np.diff(
                    np.asarray(
                        values,
                        dtype=float,
                    )
                )
                != 0
            )
        ):
            return True

    return False


def test_bundle(
    processed,
    high,
    low,
):
    scored = score_groups(
        processed,
        high,
        low,
    )

    return {
        "n_high": int(
            len(high)
        ),
        "n_low": int(
            len(low)
        ),
        "P1": scored["P1"],
        "P2": scored["P2"],
        "P3": scored["P3"],
        "verdict": (
            scored["verdict"]
        ),
    }


def sensitivity_analyses(
    repo,
    fallback,
    threshold,
    main_processed,
    main_high,
    main_low,
):
    out = {}

    high_no_change = [
        cid
        for cid in main_high
        if not infusion_changed(
            repo,
            cid,
            main_processed[
                cid
            ]["break"]["onset"],
        )
    ]

    low_no_change = [
        cid
        for cid in main_low
        if not infusion_changed(
            repo,
            cid,
            main_processed[
                cid
            ]["break"]["onset"],
        )
    ]

    out[
        "1_no_infusion_change"
    ] = test_bundle(
        main_processed,
        high_no_change,
        low_no_change,
    )

    variants = (
        (
            "2_no_gap_fill",
            {"gap_points": 0},
        ),
        (
            "3_sustained_5_min",
            {
                "sustain_bins": 30
            },
        ),
        (
            "5_late_window_ends_3_min",
            {
                "late_end_s": 180.0
            },
        ),
    )

    for label, changes in variants:
        (
            _,
            processed,
            high,
            low,
            _,
            _,
        ) = analyze_variant(
            repo,
            fallback=fallback,
            threshold=threshold,
            changes=changes,
        )

        out[label] = test_bundle(
            processed,
            high,
            low,
        )

    if threshold == 0.20:
        high15, low15 = (
            group_ids(
                main_processed,
                0.15,
            )
        )

        out[
            "4_high_at_15pct"
        ] = test_bundle(
            main_processed,
            high15,
            low15,
        )

    return out


def recovery_time(ar1):
    if (
        np.isfinite(ar1)
        and 0 < ar1 < 1
    ):
        return float(
            -BIN_S
            / np.log(ar1)
        )

    return np.nan


def recovery_summary(
    processed,
    high_ids,
):
    early = []
    late = []

    for cid in high_ids:
        pair = processed[
            cid
        ]["break"]

        early.append(
            recovery_time(
                ar1_value(
                    pair["early"]
                )
            )
        )

        late.append(
            recovery_time(
                ar1_value(
                    pair["late"]
                )
            )
        )

    early = [
        value
        for value in early
        if np.isfinite(value)
    ]

    late = [
        value
        for value in late
        if np.isfinite(value)
    ]

    return {
        "E_median_s": (
            float(
                np.median(early)
            )
            if early
            else None
        ),
        "L_median_s": (
            float(
                np.median(late)
            )
            if late
            else None
        ),
    }


def dropped_no_control(
    processed,
    threshold,
):
    high = 0
    low = 0

    for record in (
        processed.values()
    ):
        if (
            record["break"]
            is None
            or len(
                record["controls"]
            )
            != 0
        ):
            continue

        share = record[
            "case"
        ]["ebv_share"]

        if share >= threshold:
            high += 1
        elif share <= 0.05:
            low += 1

    return {
        "high": int(high),
        "low": int(low),
    }


def median_raw_map(
    case,
    start,
    stop,
):
    a = max(
        0,
        grid_index(
            case, start
        ),
    )

    b = min(
        len(case["map_raw"]),
        grid_index(
            case, stop
        ),
    )

    values = case[
        "map_raw"
    ][a:b]

    values = values[
        np.isfinite(values)
    ]

    if not len(values):
        return np.nan

    return float(
        np.median(values)
    )


def g1_check(
    repo,
    eligible,
    high_threshold,
    gap_points,
):
    high = eligible.loc[
        eligible["ebv_share"]
        >= high_threshold
    ]

    hb_all = repo.labs.loc[
        repo.labs[
            "name"
        ].astype(str).str.lower()
        == "hb"
    ].copy()

    evaluated = []
    skipped_missing_pressure = 0
    skipped_fewer_than_two = 0

    for row in high.itertuples(
        index=False
    ):
        case = build_pressure_case(
            row,
            repo,
            gap_points,
        )

        baseline = median_raw_map(
            case,
            case["opstart"],
            case["opstart"]
            + 600.0,
        )

        if not np.isfinite(
            baseline
        ):
            skipped_missing_pressure += 1
            continue

        # Section 6 says "first break".
        # Use the first sustained fall
        # under the Section 3 break
        # definition, not merely the
        # first break qualifying for P1.
        raw_breaks = (
            sustained_fall_onsets(
                case, 6
            )
        )

        end = (
            raw_breaks[0]
            if raw_breaks
            else case["opend"]
        )

        hb = hb_all.loc[
            (
                hb_all["caseid"]
                == int(row.caseid)
            )
            & (
                hb_all["dt"]
                > case["opstart"]
            )
            & (
                hb_all["dt"]
                < end
            )
            & hb_all[
                "result"
            ].notna()
        ].sort_values("dt")

        if len(hb) < 2:
            skipped_fewer_than_two += 1
            continue

        pressures = []
        haemoglobin = []
        missing_pressure = False

        for lab in hb.itertuples(
            index=False
        ):
            pressure = median_raw_map(
                case,
                max(
                    case["opstart"],
                    float(lab.dt)
                    - 300.0,
                ),
                float(lab.dt),
            )

            if not np.isfinite(
                pressure
            ):
                missing_pressure = True
                break

            pressures.append(
                pressure
            )
            haemoglobin.append(
                float(lab.result)
            )

        if missing_pressure:
            skipped_missing_pressure += 1
            continue

        within = all(
            abs(
                pressure / baseline
                - 1.0
            )
            <= 0.20
            for pressure
            in pressures
        )

        hb_fell = (
            haemoglobin[-1]
            < haemoglobin[0]
        )

        evaluated.append(
            bool(
                within
                and hb_fell
            )
        )

    share = (
        float(
            np.mean(evaluated)
        )
        if evaluated
        else None
    )

    return {
        "cases_with_two_hb_and_evaluable_pressure": int(
            len(evaluated)
        ),
        "share_consistent": share,
        "consistent": bool(
            share is not None
            and share > 0.5
        ),
        "skipped_fewer_than_two_hb": int(
            skipped_fewer_than_two
        ),
        "skipped_missing_pressure": int(
            skipped_missing_pressure
        ),
    }


def case_output(
    processed,
    ids,
    scores,
):
    out = []

    for cid in ids:
        d = scores.get(
            cid, np.nan
        )

        out.append(
            {
                "caseid": int(cid),
                "break_onset": float(
                    processed[
                        cid
                    ]["break"]["onset"]
                ),
                "D_AR1": (
                    float(d)
                    if np.isfinite(d)
                    else None
                ),
                "finite_for_test": bool(
                    np.isfinite(d)
                ),
            }
        )

    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data",
        required=True,
    )
    parser.add_argument(
        "--out",
        required=True,
    )
    args = parser.parse_args()

    repo = Repository(
        args.data
    )

    # Count/decision first. AR1, SD,
    # tests and verdict are not computed
    # until this finishes.
    decision = count_design(
        repo
    )

    result = {
        "counts": decision[
            "counts"
        ],
        "runnable": bool(
            decision["runnable"]
        ),
        "cohort": decision[
            "cohort"
        ],
        "threshold": decision[
            "threshold"
        ],
        "n_high": 0,
        "n_low": 0,
        "P1": {
            "n": 0,
            "median": None,
            "one_sided_p": None,
            "two_sided_p": None,
        },
        "P2": {
            "n_high": 0,
            "n_low": 0,
            "median_high": None,
            "median_low": None,
            "p": None,
        },
        "P3": {
            "n": 0,
            "median": None,
            "p": None,
        },
        "verdict": (
            "not runnable"
        ),
        "high_loss_cases": [],
        "low_loss_cases": [],
        "G1": None,
    }

    if decision["runnable"]:
        fallback = (
            decision["cohort"]
            == "fallback"
        )

        threshold = float(
            decision[
                "threshold"
            ]
        )

        (
            eligible,
            processed,
            high,
            low,
            scored,
            settings,
        ) = analyze_variant(
            repo,
            fallback=fallback,
            threshold=threshold,
        )

        result.update(
            {
                "cohort_weight": (
                    0.5
                    if fallback
                    else 1.0
                ),
                "n_high": int(
                    len(high)
                ),
                "n_low": int(
                    len(low)
                ),
                "P1": scored["P1"],
                "P2": scored["P2"],
                "P3": scored["P3"],
                "verdict": scored[
                    "verdict"
                ],
                "high_loss_cases": (
                    case_output(
                        processed,
                        high,
                        scored[
                            "high_ar"
                        ],
                    )
                ),
                "low_loss_cases": (
                    case_output(
                        processed,
                        low,
                        scored[
                            "low_ar"
                        ],
                    )
                ),
                "dropped_no_control": (
                    dropped_no_control(
                        processed,
                        threshold,
                    )
                ),
                "recovery_time_s_median_high_break": (
                    recovery_summary(
                        processed,
                        high,
                    )
                ),
                "sensitivity": (
                    sensitivity_analyses(
                        repo,
                        fallback,
                        threshold,
                        processed,
                        high,
                        low,
                    )
                ),
                "G1": g1_check(
                    repo,
                    eligible,
                    threshold,
                    settings[
                        "gap_points"
                    ],
                ),
            }
        )

    os.makedirs(
        args.out,
        exist_ok=True,
    )

    output_path = os.path.join(
        args.out,
        "check.json",
    )

    with open(
        output_path,
        "w",
        encoding="utf-8",
    ) as handle:
        json.dump(
            result,
            handle,
            indent=2,
            allow_nan=False,
        )

    print(
        json.dumps(
            {
                "runnable": result[
                    "runnable"
                ],
                "cohort": result[
                    "cohort"
                ],
                "threshold": result[
                    "threshold"
                ],
                "verdict": result[
                    "verdict"
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
