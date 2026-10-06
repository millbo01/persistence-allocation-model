# H1 VitalDB, test of G12: pre-registration (DRAFT for James, 6 October 2026)

Drafted by Claude, 6 October 2026. **Status: draft. Not frozen until James confirms. No VitalDB data has been opened, and VitalDB's terms have not been accepted.** After freezing, any change is a new, separately logged experiment.

**Sources:**
- Model: theory/TIER_QUEUE_MODEL_v0.17.md (vocabulary frozen).
- Setting map and mapping: tests/H1 VitalDB G12 - setting map and mapping (draft).md.
- Structure only, with no values: raw/2026-10-06_gemini_H1-VDB-S1.md (SHA begins 27383b4d), assessed in theory/tier_queue_heldout_datasets_DRAFT.md.
- Every field and track named below is taken from that documentation.

**James's decision (6 October 2026): release profile A.**
- Compensation for blood loss draws on a store that tapers as it empties, and may end in a switch.
- **G12 therefore predicts a warning** before falls in pressure during substantial blood loss.
- **A null result counts as a failure of G12 as mapped for this system.** It may not be explained away afterwards as "it was a switch".

## 1. Hypotheses

| Code | Role | Statement |
|---|---|---|
| **P1** | Primary (G12) | Before a fall in pressure in a high-loss case, the lag-one autocorrelation of mean arterial pressure rises more than it does across matched control windows from the same case |
| **P2** | Primary (G12, specificity) | That excess rise is larger in high-loss cases than in low-loss cases (falls with no depleted store) |
| P3 | Secondary | The same as P1, for the standard deviation of mean arterial pressure |
| G1 | Check (low weight) | In high-loss cases, pressure stays near its baseline until the first fall while the blood's haemoglobin falls |
| G18 | Exploratory (not scored) | The correlation between heart rate and mean arterial pressure changes before the fall |

**Change from the setting-map draft, made before data:**
- The draft's contrast was falls soon after anaesthesia starts.
- **That cannot be used.** The measures need 31 minutes of stable, recorded pressure before each fall. Falls soon after induction have no such history: the arterial line may not yet be in, and the early window would fall before anaesthesia.
- **The contrast is now falls in low-loss cases** in the second half of surgery, with the same window geometry. In those falls no store is being depleted by bleeding (causes include anaesthetic depth, drugs and position), so the model predicts a weaker warning or none.

## 2. Cases

**Included cases must meet all of the following:**
1. ane_type indicates general anaesthesia.
2. Solar8000/ART_MBP, ART_SBP and ART_DBP are present.
3. intraop_ebl, weight and sex are recorded.
4. **No bolus vasopressors:** intraop_phe = 0, intraop_eph = 0 and intraop_epi = 0. Every vasopressor given is then visible in time, through the Orchestra infusion tracks.
5. Surgery lasted at least 90 minutes (opend − opstart).

**Groups, by estimated blood loss as a share of estimated blood volume (EBV):**
- **EBV** = 70 mL/kg for men and 65 mL/kg for women, multiplied by weight. These are conventional textbook values.
- **High loss:** intraop_ebl ≥ 20% of EBV. 20% is the lower end of the reported onset of the second phase (Section 2, item 5, of the setting map). It also sits inside ATLS haemorrhage class II (15 to 30%).
- **Low loss:** intraop_ebl ≤ 5% of EBV.
- Cases between the two are not used.

**Minimum numbers, and one fixed step-down:**
- **Required:** at least 20 cases per group, each with a qualifying fall (Section 3) and at least one control pair (Section 4).
- **The count comes first.** A counting script runs before any measure is computed, and outputs counts only.
- **If the high-loss group has fewer than 20,** its threshold steps down once, to 15% of EBV (the lower bound of ATLS class II).
- **If it is still short,** or the low-loss group is short, **the test is declared not runnable.** That is reported as such, with no further relaxation.
- **Fallback, lower weight, only if the primary is not runnable:** the bolus exclusion is dropped, and windows containing a rise in pressure of more than 15 mmHg within 60 seconds (the signature of a bolus) are excluded. A result from this cohort is labelled "fallback" and carries half weight in the verdict.

## 3. The record and the break

**Pressure signal:**
- Solar8000/ART_MBP numerics, every 2 seconds.
- The 500 Hz waveform is not used in the primary analysis.

**Artefact rule.** A 2-second sample is invalid if any of these holds:
- mean pressure < 20 or > 200 mmHg;
- systolic > 300 mmHg;
- systolic − diastolic < 10 mmHg (a damped line, a flush, or blood sampling).

**Gaps:**
- Missing rows (numeric tracks drop disconnections) and invalid samples are treated alike.
- Gaps of 10 seconds or less are filled by linear interpolation.
- A window with more than 10% of its time invalid or missing is unusable.

**Resampling:** the signal is averaged into 10-second bins, giving 60 points per 10-minute window.

**The break: a fall in pressure.**
- **Definition:** onset t0 is the first time the 10-second series stays below 65 mmHg for at least 60 seconds (6 consecutive bins). 65 mmHg is the conventional definition of intraoperative hypotension.
- **Qualifying breaks must meet all of the following:**
  - t0 lies in the second half of surgery: after (opstart + opend) / 2, and before opend. This is chosen because bleeding accumulates, so later falls are more likely to follow loss.
  - The 31 minutes before t0 (the approach) lie after opstart, with every 10-second bin at or above 65 mmHg.
  - Both measurement windows (Section 4) are usable.
- **Only the first qualifying break per case is used.**

## 4. Measures and windows

**Windows, relative to the break onset t0:**
- **Late window L:** from t0 − 11 min to t0 − 1 min. The last minute is dropped to keep the fall itself out.
- **Early window E:** from t0 − 31 min to t0 − 21 min.

**Within each window:**
1. Remove the window's own straight-line fit (linear detrending).
2. **AR1:** the lag-one autocorrelation of the residuals.
3. **SD:** the standard deviation of the residuals.
4. Recovery time, −10 s / ln(AR1), is reported. It is a transform of AR1, so it is not a separate test.

**Change for a break:** ΔAR1 = AR1(L) − AR1(E), and ΔlnSD = ln SD(L) − ln SD(E).

**Control pairs (the same case, the same geometry):**
- **Pseudo-onsets t\*** lie on a 5-minute grid in the second half of surgery.
- **No break near t\*:** no 10-second bin below 65 mmHg from t\* − 31 min to t\* + 30 min.
- **The same validity rules apply.**
- **Per case,** the control change is the median over its control pairs.

**Case score:** D = Δ(break) − median Δ(control). Cases with no control pair are dropped, and their number is reported.

## 5. Tests and verdict

**Tests,** all one-sided with α = 0.05:
- **P1:** a Wilcoxon signed-rank test that D_AR1 > 0 in high-loss cases.
- **P2:** a Mann-Whitney test that D_AR1(high) > D_AR1(low).
- **P3:** a Wilcoxon signed-rank test that D_lnSD > 0 in high-loss cases (secondary).
- **No correction is applied.** The primary verdict rests on P1 and P2 for AR1 only, decided in advance.

**Verdict for G12 in this system:**

| Result | Verdict |
|---|---|
| P1 passes (p < 0.05, median D_AR1 > 0) **and** P2 passes | **Supported** |
| P1 passes, P2 fails | **Narrowed.** A warning is present but not specific to depletion, so the model's account of why is not supported |
| P1 fails (p ≥ 0.05 or median D_AR1 ≤ 0) | **Fails.** Logged as a failure of G12 as mapped, under the standing check |
| Median D_AR1 < 0 with two-sided p < 0.05 | **Contradicted:** the record became less sluggish before the fall |

- P3 is reported alongside the verdict but does not change it.
- **A fallback cohort** result (Section 2) is reported with its label, at half weight.

**Sensitivity analyses** (reported, not part of the verdict):
1. Breaks with any change in a vasoactive infusion rate (Orchestra PHEN, NEPI, EPI, VASO, DOPA, DOBU) between t0 − 31 min and t0 are excluded.
2. Gap filling is set to 0 seconds (no interpolation).
3. The break is sustained for 5 minutes instead of 1.
4. High-loss cases at 15% of EBV, if the primary used 20%.
5. The late window ends at t0 − 3 min instead of t0 − 1 min (guards against the start of the fall leaking into L; see Section 11, item 8).

**Known bias, stated in advance:** bleeding is recorded only as a case total.
- Some falls in high-loss cases will come **before** most of the bleeding.
- This dilutes the effect towards the null.
- It is **accepted, not corrected,** and a null still counts as a failure.

## 6. G1 check (low weight)

**What is computed,** for high-loss cases:
- **Baseline pressure:** the median valid mean pressure from opstart to opstart + 10 min.
- **Pressure at each intraoperative haemoglobin sample:** for every lab_data hb sample with dt between opstart and the first break (or opend if there is no break), the median mean pressure in the 5 minutes before that sample.

**Consistent with G1** if, in more than half of cases with at least two such samples, both hold:
- pressure stays within ±20% of baseline at every sample (a conventional intraoperative tolerance);
- the last haemoglobin is lower than the first.

**Weight:** the anaesthetist defends pressure, which makes the check close to trivial. It is reported as consistent or not, at low weight.

## 7. G18, exploratory (not scored)

**Measure:** in high-loss breaks, the Pearson correlation between detrended mean pressure and detrended Solar8000/HR (10-second bins) in L against E, compared with the control pairs.

**Also reported:** stroke volume (Vigileo/SV or EV1000/SV) where present.

**Status:** descriptive only, with no pass rule.

## 8. Contamination (declared)

1. **TQ-DS2a:** the essay described dynamics before fainting in laboratory tests in general terms.
2. **Commercial hypotension-prediction indices:** Claude knows in outline that falls in pressure during surgery can be predicted minutes ahead from the arterial waveform. That makes some warning before falls plausible on prior knowledge. **P2 (specificity to blood loss) is the part that prior knowledge does not supply.**
3. **The two-phase physiology of bleeding** (reviews PMC1918009, PMC2739247), which was used to choose profile A.

**Weight:** P1 alone is weak evidence for the model. The verdict "supported" needs P2.

## 9. Procedure and order

**Before any data is opened:**
1. **James confirms** this pre-registration.
2. It is frozen and committed, and its SHA is recorded in CONTROL.md.
3. **Claude writes the analysis code** (tests/scripts/h1_vdb_g12.py). It is tested only on synthetic series, built with the TQ engine and with plain noise models (one with rising AR1 before a fall, one without). It is committed, with its SHA, **before** data is opened.

**Opening the data:**
4. **James accepts VitalDB's registration agreement** (CC BY-NC-SA 4.0).
5. Data is downloaded through the documented VitalDB route (Python library or web download) into data/ (git-ignored). Source URL and checksums go in data/README.md.

**Running:**
6. The **counting script** runs first and outputs counts only (Section 2).
7. The full analysis runs once, unchanged. Outputs go to tests/results/H1-VDB/ (README.md and summary.json).
8. **Any deviation** (a bug, a missing field, a changed field name) is logged as a deviation with the reason, never silently fixed. A bug fix that changes the verdict is reported with both results.

**After the run:**
9. **Blind adjudication by GPT.** The adjudicator receives this pre-registration and summary.json, with the hypothesis labels intact but no commentary from Claude. It applies Section 5's verdict table, and its verdict is recorded verbatim.
10. **Computation replicated by a second model** from the same files and this pre-registration (standing rule). Any difference is logged and resolved before the verdict is reported.
11. **Replication.** The same frozen rules are applied to an independent dataset, documented in its own run (INSPIRE or the MIMIC-III matched waveforms). Field mappings may change; thresholds, windows and the verdict table may not.

## 10. What a result would mean

- **Supported:** in one held-out physiological system, the model's conditional prediction holds. A warning appears where a tapering store is being drawn down, and is weaker where it is not.
- **Narrowed or failed:** recorded in the model's Section 10 under the standing check. The release-profile mapping for blood loss under anaesthesia is then the first candidate for revision. **No new mechanism is added.**

## 11. Decision log (methodology choices, with the direction each pushes)

Logged under the delegation rule. Choices that make the model easier to pass are marked; James confirms them with the rest.

| No. | Choice | Direction |
|---|---|---|
| 1 | Release profile A; a null counts as failure (James) | Harder to pass |
| 2 | Contrast moved to low-loss falls (window geometry) | Harder: low-loss falls may include volume loss from other causes (fasting, urine), making them more like high-loss falls and P2 harder to pass |
| 3 | High loss at 20% of EBV | Neutral: purer group, fewer cases |
| 4 | One step-down to 15% if short | Harder: dilutes the group, but makes the test runnable |
| 5 | Bolus fallback cohort | **Easier to run**, at half weight |
| 6 | Falls only in the second half of surgery | **Favours the model** (falls more likely to follow loss); applied to both groups alike |
| 7 | Stable approach (no bin below 65 mmHg for 31 minutes) | Neutral: excludes falls preceded by earlier dips |
| 8 | Linear detrending within windows | **Favours P1:** a curving start of the fall left in L raises AR1. Not corrected in P1; P2 controls for it (low-loss falls carry the same artefact), which is why "supported" needs P2. Sensitivity 5 also checks it |
| 9 | One-sided tests; no multiplicity correction | **Favours the model;** limited by fixing a single primary measure (AR1) and requiring both P1 and P2 |
| 10 | Bleeding timing unknown; bias accepted | Harder to pass |
| 11 | First qualifying break per case only | Neutral: avoids dependent breaks |
