## Part A: AUDIT

The frozen rules for Sections 2–7 are at Pasted text and the implementation notes/code begin at Pasted text.

### Section 2 — Cases and count step

| Rule | Implementation | Assessment |
|---|---|---|
| General anaesthesia | `eligible_cases`, line 595 | **Yes for the documented categories.** It uses case-insensitive substring matching for `"general"`. |
| ART_MBP, ART_SBP, ART_DBP present | `eligible_cases`, line 596 | **Yes, with an interpretation.** “Present” means a matching `trks.csv` entry; the track file itself need not exist at eligibility time. |
| EBL, weight, sex recorded | lines 597, 603–604 | **Yes**, except the code additionally rejects non-positive weight through `ebv_share`. |
| No bolus PHE/EPH/EPI in primary cohort | lines 599–601 | **Yes.** Missing fields are also excluded, as stated in the implementation notes. |
| Surgery ≥90 min | line 598 | **Yes.** |
| EBV 70 mL/kg M, 65 mL/kg F | lines 584–588 | **Yes.** |
| High ≥20%, low ≤5%, middle unused | lines 622–624 | **Yes.** |
| ≥20 qualifying cases/group, each with break + control | `qualifies`, lines 618–624 | **Yes.** |
| Count occurs before measures | `count`/`analyse` commands, lines 752–777 | **Substantively yes.** The count pass computes signal cleaning, breaks, windows and control availability, but not AR1/SD/test statistics. |
| Count outputs counts only | lines 752–758 | **Minor discrepancy.** `counts.json` also contains code SHA, runnable status, chosen cohort and threshold. It does not expose outcome measures. |
| Step high threshold from 20% to 15% once if high group short | lines 635–643 | **Mostly yes.** If the low group is already short at 20%, line 639 breaks before recording the 15% count even if the high group is also short. The final runnable decision is unaffected because lowering the high threshold cannot repair a short low group. |
| Still short → not runnable | lines 631–644 | **Yes.** |
| Fallback only after primary not runnable | outer loop in `decide_cohort` | **Yes.** |
| Fallback drops bolus-total exclusion and excludes bolus-signature windows | `eligible_cases(..., True)`, lines 539–540/560–561 | **Yes, under the implementation's bolus-signature interpretation.** |
| Fallback labelled and half weight | lines 785–786 | **Yes.** The weight is represented as `0.5`; the pre-registration does not define a mathematical alteration to the categorical verdict. |

### Section 3 — Record, artefacts, gaps and break

| Rule | Implementation | Assessment |
|---|---|---|
| Use Solar8000 ART_MBP numerics, not waveform | `TRACKS`, `Case` | **Yes.** |
| MAP <20 or >200 invalid | `clean_map`, lines 386–389 | **Yes.** Boundaries 20 and 200 remain valid, as written. |
| SBP >300 invalid | same | **Yes.** |
| SBP−DBP <10 invalid | same | **Yes.** |
| Missing and invalid treated alike | invalid MAP becomes NaN before gap filling | **Yes.** |
| Gaps ≤10 s linearly interpolated | `gap_fill`, lines 365–383 | **Yes at the 2-s-grid stage:** ≤5 missing grid positions, bounded by valid values. |
| >10% missing/invalid window unusable | `Case.window`, lines 437–443 | **Yes under the chosen reading** that the percentage is measured *after* allowed short-gap filling. |
| 10-s bins | `bins`, lines 396–402 | **Yes.** |
| Six consecutive bins <65 define a break | `candidate_breaks`, lines 511–525 | **Yes.** |
| Missing bin breaks a hypotensive run | line 513 | **Yes.** |
| t0 strictly after midpoint and before opend | lines 529–531 | **Yes.** |
| 31-min approach after opstart | lines 532–533 | **Yes.** |
| **Every** approach bin ≥65 | `stable`, lines 505–508 | **No. Material discrepancy.** It deletes NaN bins and tests only the remaining bins. A missing bin therefore passes rather than making the approach fail. |
| Both E and L usable | lines 536–538 | **Yes.** |
| First qualifying break only | loop returns first qualifying candidate, line 541 | **Yes.** |

The approach discrepancy is directly against the frozen wording that every approach bin must be at or above 65. Pasted text

### Section 4 — Windows, measures, controls and D

| Rule | Implementation | Assessment |
|---|---|---|
| E = [t0−31 min, t0−21 min) | `pair_windows`, line 491 | **Yes.** |
| L = [t0−11 min, t0−1 min) | lines 489–491 with `late_end=60` | **Yes.** |
| Linear detrending separately in each window | `detrend`, lines 456–459 | **Yes.** |
| AR1 of detrended residuals | `ar1`, lines 462–467 | **Yes.** Pearson correlation of adjacent residuals. |
| SD of residuals | `sd`, lines 470–472 | **Yes**, with `ddof=1`, an implementation choice not frozen in the pre-registration. |
| Recovery time −10/ln(AR1) reported | lines 499–501, 788–790 | **Partly.** It is correctly calculated for `0<AR1<1`, but the final summary reports only median E/L recovery time for high-loss break windows, not recovery time across all relevant break/control windows. |
| ΔAR1 = L−E | line 497 | **Yes.** |
| ΔlnSD = ln SD(L)−ln SD(E) | line 498 | **Yes.** |
| Pseudo-onsets on 5-min grid in second half | lines 545–562 | **Yes under the stated implementation note:** midpoint + k×300 s, including k=0. |
| No bin <65 from t*−31 to t*+30 | line 555 using `stable` | **Yes for finite bins.** Missing bins are ignored rather than treated as below 65, which is consistent with the literal “no bin below 65” but is an explicit choice. |
| Same measurement-window validity | lines 557–559 | **Yes.** |
| Control Δ is median over pairs | `case_scores`, line 651 | **Yes, but `np.nanmedian` silently omits undefined control deltas.** |
| D = break Δ − median control Δ | line 652 | **Yes.** |
| No-control cases dropped | `qualifies` | **Yes.** |
| Number dropped for no control reported | outputs | **No.** It is not explicitly reported. |

There is a second material gap-rule problem here: after the 2-s gap rule has deliberately left gaps longer than 10 seconds unfilled, `Case.window` interpolates **all** missing 10-s bins, including endpoint extrapolation with the nearest value. That can fill gaps longer than the frozen 10-second maximum. Lines 447–452 therefore conflict with the gap rule. Pasted text

### Section 5 — P1/P2/P3, verdict and sensitivities

| Rule | Implementation | Assessment |
|---|---|---|
| P1 Wilcoxon, D_AR1 >0, high-loss | lines 655–661, 685–691 | **Yes.** Correct sign and one-sided direction. |
| P2 Mann–Whitney, high > low | lines 664–670 | **Yes.** Correct statistic and direction. |
| P3 Wilcoxon D_lnSD >0, high | lines 685–691 | **Yes.** |
| α=.05, one-sided | tests/verdict | **Yes.** |
| No multiplicity correction | no correction performed | **Yes.** |
| P1+P2 determine primary verdict | `verdict`, lines 673–682 | **Generally yes**, with two edge-case bugs below. |
| Contradicted if median<0 and two-sided p<.05 | lines 676–677 | **Yes.** |
| P3 cannot alter verdict | `verdict` receives only P1/P2 | **Yes.** |
| Sensitivity 1: infusion-rate changes | lines 792–795 | **Implemented.** It drops the selected case rather than searching for a later qualifying break; that choice is ambiguous. |
| Sensitivity 2: zero gap fill | lines 796–799 | **Not fully implemented.** The 2-s interpolation is disabled, but `Case.window` still interpolates missing 10-s bins. Thus this is not actually “no interpolation.” |
| Sensitivity 3: 5-min fall | `sustain_bins=30` | **Yes.** |
| Sensitivity 4: high at 15% if main used 20% | lines 800–802 | **Yes.** |
| Sensitivity 5: L ends at t0−3 min | `late_end=180` | **Yes.** |
| Bleeding-time bias accepted, not corrected | no timing correction | **Yes.** |

Two verdict/NaN issues matter:

1. `wilcoxon_greater` returns `p=None` when all D values equal zero. `verdict` immediately returns `"not computable"`. The frozen table instead says median \(D_{AR1}\le0\) means **Fails**, so an all-zero result is a definite failure, not “not computable.” Pasted text
2. Non-finite case scores are silently filtered out by the statistical wrappers. If enough AR1/SD values become undefined, the actual test sample may be smaller than the count-step sample. If P1 still passes but P2 becomes non-computable, `verdict` treats `P2["p"] is None` as a failed P2 and emits **Narrowed**, rather than indicating that P2 could not be tested.

### Section 6 — G1

| Rule | Implementation | Assessment |
|---|---|---|
| Compute for high-loss cases | `all_hi`, lines 804–805 | **Yes.** It includes selected-cohort high-loss cases whether or not they qualify for P1/P2. |
| Baseline = median valid MAP first 10 min | lines 702–706 | **Yes.** Uses unfilled valid MAP, matching the implementation note. |
| Hb samples between opstart and first break/opend | lines 707–708 | **Ambiguous implementation.** “First break” is taken to mean first **qualifying** break; the alternative is the first sustained fall defined in Section 3, whether or not it qualifies for P1/P2. |
| Median MAP in preceding 5 min for each Hb | lines 710–714 | **Mostly yes.** For an Hb within the first five intraoperative minutes, the interval is clipped at opstart. |
| Every sample remains ±20% baseline | line 717 | **Yes for the Hb samples retained by the code.** |
| Last Hb < first | line 718 | **Yes.** |
| More than half of cases | lines 720–722 | **Yes, strict >0.5.** |
| Cases need ≥2 such samples | lines 715–719 | **Choice/ambiguity.** Samples without usable MAP or finite Hb result are silently skipped; the case qualifies only if at least two usable pressure/Hb pairs remain. |
| Low-weight label | output | **Not explicit.** The result is reported, but no `"weight": "low"` field is emitted. |

### Section 7 — G18

| Rule | Implementation | Assessment |
|---|---|---|
| High-loss qualifying breaks | `g18(res, hi, ...)` | **Yes.** |
| Detrended MAP–HR Pearson correlation in E and L | `xcorr` + `g18`, lines 725–740 | **Yes.** |
| Compare L−E with control-pair changes | same | **Yes.** It reports a case-adjusted excess change and then its median. |
| Solar8000/HR | implementation note + `TRACKS` | **Yes.** |
| Stroke volume where present | `sv1`/`sv2`, lines 424–427 and G18 call | **Yes under one reading.** If any Vigileo/SV value exists anywhere in the case, the code chooses Vigileo for the whole case; EV1000 is considered only when Vigileo has no finite values at all. |
| Descriptive only, no pass rule | output only | **Yes.** |

### IMPLEMENTATION_NOTES audit

| Note | Code implements note? | Assessment against frozen rules |
|---|---|---|
| 1. Snap samples to 2-s grid from opstart, ≤1 s; average collisions | **Yes**, `to_grid` | Pre-registration silent; acceptable. Exact 1-s ties use `np.rint`'s tie behaviour. |
| 2. Require MAP/SBP/DBP at same grid point to validate MAP | **Yes** | Reasonable conservative reading of the artefact rule. |
| 3. Fill ≤5 consecutive missing 2-s points, bounded both sides | **Yes** | Consistent with ≤10-s interpolation. |
| 4. 10% window criterion measured after filling | **Yes** | Pre-registration ambiguous; plausible reading. |
| 5. Missing 10-s bin breaks hypotensive run and is “not counted as below” in stable approach | **Yes as code behaviour, but note is partly wrong.** Missing breaking a hypotensive run is fine; ignoring a missing bin in the 31-min stable approach conflicts with “every 10-second bin at or above 65.” |
| 6. Interpolate missing 10-s bins inside usable windows, endpoints nearest | **Yes, but note is wrong.** It permits interpolation of gaps longer than 10 s and therefore overrides the frozen maximum gap length. |
| 7. Pearson AR1; SD ddof=1 | **Yes** | Pre-registration silent on estimator details; acceptable. |
| 8. Controls anchored at midpoint + k×300 with temporal bounds | **Yes** | Explicit resolution of an ambiguity. |
| 9. Missing bolus-total fields excluded primary, allowed fallback | **Yes** | Pre-registration silent; acceptable. |
| 10. `ane_type` word “general”, case-insensitive | **Not literally.** Code uses substring `.contains("general")`, not word matching. With the documented categories this produces the same answer. |
| 11. Fallback bolus signature from current bin vs minimum prior six bins | **Yes**, `bolus_signature` | A reasonable but non-unique reading of “rise >15 within 60 seconds.” |
| 12. Infusion change includes last sample before approach | **Yes** | Pre-registration silent on sampling mechanics; acceptable. |
| 13. G1 uses valid unfilled MAP | **Yes** | Consistent. |
| 14. G18 HR 20–250, SV 5–250; same correlation analysis | **Yes** | Pre-registration silent on these validity ranges. |

### a. Discrepancies

| Code/function | Frozen rule | Discrepancy | Can change P1/P2/P3/verdict? |
|---|---|---|---|
| `stable`, 505–508 | Every approach bin ≥65 | NaNs are removed, so missing bins pass the stable-approach check. | **Yes — all four.** It can admit a different break/case and therefore change D and cohort counts. |
| `Case.window`, 447–452 | Only gaps ≤10 s interpolated | Remaining missing 10-s bins are interpolated regardless of the originating gap length; endpoints are extrapolated. | **Yes — all four.** It can change eligibility, AR1/SD and control values. |
| Sensitivity 2 via `Case.window` | No interpolation | 2-s filling is disabled, but 10-s-bin interpolation remains. | **No for the primary verdict**, but **yes for reported sensitivity results**. |
| `wilcoxon_greater` + `verdict` | median D≤0 ⇒ Fails | All-zero P1 returns `"not computable"` instead of `"Fails"`. | **Yes — verdict.** |
| `case_scores`, test wrappers | Selected cases tested | Undefined break/control measures can become NaN and are silently omitted from tests. | **Yes — P1/P2/P3 and possibly verdict.** |
| `verdict`, 681–682 | P2 must pass/fail as a test | A non-computable P2 is treated like a failed P2, producing `"Narrowed"` if P1 passes. | **Yes — verdict.** |
| outputs | No-control cases dropped **and their number reported** | Number dropped specifically for lack of control pair is not reported. | **No.** Reporting discrepancy only. |
| 788–790 | Recovery time is reported | Only median recovery times for high-loss break E/L windows are emitted. | **No.** |
| `decide_cohort`, line 639 | Step down high threshold if high group short | When both low and high are short, low-short exits before recording the 15% high count. | **No for the decision/verdict.** It changes the count record. |
| `eligible_cases`, `.contains("general")` | Implementation note says the word `"general"` | Substring rather than word match. | **No under the supplied category set; unclear otherwise.** |
| `ebv_share`, weight≤0 | Inclusion requires weight recorded | Adds a positivity requirement not explicitly frozen. | **Unclear/yes if such records exist.** It could change counts and thus the analysis. |
| G1 output | G1 reported at low weight | No explicit low-weight field. | **No.** |
| count output | counting script “outputs counts only” | Also outputs decision metadata and SHA. | **No.** No outcome measure is leaked. |

### b. Bugs

1. **Stable-approach NaN bug:** `stable()` removes NaNs, violating the explicit every-bin condition.
2. **Long-gap interpolation bug:** `Case.window()` can fill missing bins produced by gaps longer than 10 seconds.
3. **No-gap-fill sensitivity bug:** sensitivity 2 still performs the preceding 10-s-bin interpolation.
4. **All-zero verdict bug:** a P1 vector consisting entirely of zeros gives `"not computable"` rather than frozen-table `"Fails"`.
5. **Silent case-loss/NaN bug:** P1/P2/P3 wrappers silently remove non-finite D values after the ≥20 count decision.
6. **Silent control-value omission:** `np.nanmedian` silently removes undefined control-pair changes. The frozen rule says median over the case's control pairs but does not define this omission.
7. **Non-computable-P2 verdict bug:** P2 `p=None` is converted into a substantive `"Narrowed"` verdict when P1 passes.
8. **Reporting bug:** cases dropped specifically for having no control pair are not counted/reported as required.

No wrong sign, reversed alternative, wrong named test, or clear E/L off-by-one error was found. P1/P3 use greater-sided Wilcoxon, P2 uses greater-sided Mann–Whitney, and both Δ definitions have the frozen L−E sign.

### c. Ambiguities and the reading chosen by the code

| Frozen ambiguity | Code's reading | Reasonable alternative |
|---|---|---|
| Phase/origin of 10-s bins | Bins begin at `opstart`. | Align bins to case-start clock/multiples of 10 s. This can move detected t0. |
| Exact 2-s sample alignment | Nearest opstart-anchored grid point within 1 s. | Require exact recorded 2-s timestamps or use another tie rule. |
| Track “present” | `trks.csv` contains a track ID. | Require the corresponding file and/or at least one sample. |
| Window >10% missing criterion | Count missing **after** permitted short-gap filling. | Count original invalid/missing time before interpolation. |
| Remaining missing bins in a ≤10%-missing window | Interpolate all of them. | Leave them missing and use finite adjacent pairs, or declare the measure undefined. The code's choice conflicts with the explicit maximum gap rule. |
| SD convention | Sample SD, `ddof=1`. | Population SD, `ddof=0`. |
| AR1 definition | Pearson correlation of residual[t] and residual[t+1]. | Regression coefficient or covariance/variance estimator. The code's Pearson choice is supported by its frozen implementation note. |
| Pseudo-onset 5-min grid origin | `midpoint + k×300`, starting at midpoint. | First 5-min boundary strictly after midpoint or a grid anchored at opstart/case start. |
| Whether “second half” includes exact midpoint for controls | Yes, k=0 is midpoint. | Require t*>midpoint, as is explicitly required for actual breaks. |
| Fallback “rise >15 within 60 s” | 10-s-bin value minus minimum of preceding up-to-six bins within E/L. | Detect on 2-s samples; require a full six-bin history; or scan every pair ≤60 s. |
| “Windows containing” bolus signature | Only E and L windows. | Exclude if signature occurs anywhere in the entire 31-min approach. |
| Undefined control Δ | Ignore it in `nanmedian`. | Make case score undefined, or require every retained control pair to yield the measure. |
| Wilcoxon zero handling | SciPy default except explicit all-zero rejection. | Pre-specify `zero_method`, exact/asymptotic method and all-zero behaviour. |
| Fallback “half weight” | Store `weight=0.5`; categorical Supported/Narrowed/Fails unchanged. | Define an explicit weighted evidence aggregation rule. None is frozen. |
| Sensitivity 1 after a contaminated first break | Drop that case. | Search for the first later qualifying break without an infusion change. |
| G1 “first break” | First **qualifying** main-analysis break. | First sustained ≥60-s fall below 65, whether or not it satisfies half-surgery/approach/window criteria. I use this latter literal Section-3 definition in Part B. |
| G1 Hb exactly at endpoints | Strictly `opstart < dt < break`. | Include either/both endpoints. |
| Hb within first five operative minutes | Clip preceding-pressure interval at opstart. | Require a complete five-minute interval. |
| Hb with no usable pressure | Skip that Hb observation. | Treat the case as unevaluable because the rule says pressure at every sample. Part B makes such a case explicitly unevaluable rather than silently deleting the sample. |
| G18 case summary | Median case-adjusted change in correlation. | Merely report break E/L correlations, or a different descriptive aggregation. |
| Both Vigileo/SV and EV1000/SV present | Prefer Vigileo whenever it has any finite sample anywhere. | Choose whichever has usable data in each relevant window, or report both separately. |

## Part B: YOUR OWN IMPLEMENTATION

The script below follows the frozen rules and the non-conflicting implementation notes. In particular, it deliberately does **not** follow the two problematic missing-data choices: a missing approach bin fails the stable-approach criterion, and missing 10-second bins left after the ≤10-second gap fill are not subsequently fabricated. For AR1 with such residual missing bins, it fits the linear trend to available bins and uses only genuinely adjacent finite 10-second pairs.

```python
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
```

A compiled copy of the same standalone script is available here: h1_vdb_g12_check.py[h1_vdb_g12_check.py](sandbox:/mnt/data/h1_vdb_g12_check.py).

## Part C: SELF-CHECK

- **No introduction written:** yes; the response starts directly with Part A as required. Pasted text
- **No guess at the VitalDB data or results:** yes. No unseen case count, statistic, p-value or verdict has been inferred.
- **Every rule in Sections 2–7 covered in Part A:** yes, including all 14 `IMPLEMENTATION_NOTES`, the five sensitivities, G1 and descriptive G18.
- **Standalone Part B:** yes. It imports only Python standard-library modules plus `numpy`, `pandas` and `scipy`; it does not import or call the supplied analysis code.
- **Execution check:** `python -m py_compile h1_vdb_g12_check.py` succeeds, and I exercised both its not-runnable path and its full runnable P1/P2/P3/sensitivity path using synthetic files only. No real VitalDB values or results were used.
