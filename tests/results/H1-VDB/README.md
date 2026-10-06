# H1 VitalDB, test of G12: results (6 October 2026)

**Pre-registration:** tests/H1 VitalDB G12 - pre-registration.md (frozen 6 October 2026, SHA-256 begins 371caf3c).
**Code:** tests/scripts/h1_vdb_g12.py (SHA-256 9fbe80d7, unchanged since its commit before the data were opened).
**Data:** data/README.md (VitalDB, downloaded 6 October 2026 after James accepted the registration agreement).

**Status:**
- **This is the computed result, run once.**
- **It is not yet replicated or adjudicated.** Next are computation replication by a second model, then blind GPT adjudication. Claude does not adjudicate.

## Count step (counts.json)

| Cohort | High-loss threshold | Eligible | High loss qualifying | Low loss qualifying | Outcome |
|---|---|---|---|---|---|
| Primary (no boluses) | 20% of EBV | 755 | 0 | 16 | Not runnable |
| Fallback (boluses allowed) | 20% | 2,324 | 19 | 42 | High group short |
| Fallback | 15% | 2,324 | 25 | 42 | **Runnable: analysed, half weight** |

**Interpretation applied:** the step-down to 15% was also applied inside the fallback cohort. The pre-registration does not say this explicitly. It was fixed in the code before the data were opened, and the synthetic check S5 tested it.

## Primary result (fallback cohort, half weight)

| Test | n | Statistic | p (one-sided) |
|---|---|---|---|
| P1: excess rise in AR1 before falls, high loss | 25 | median D = -0.072 | 0.48 (two-sided 0.96) |
| P2: high-loss excess greater than low-loss | 25 against 42 | medians -0.072 against +0.065 | 0.78 |
| P3: excess rise in SD of pressure, high loss (secondary) | 25 | median D = +0.081 (log scale) | 0.25 |

**Computed verdict (Section 5 table): Fails.**
- P1 is not met: the median is below zero and p ≥ 0.05.
- It is not "Contradicted": the two-sided p of 0.96 is far from 0.05.

**Recovery time (high loss, median):** 44.5 s in the early window and 44.3 s in the late window.

## Sensitivity analyses (not part of the verdict)

| No. | Variant | n high / low | P1 median D (p) | Verdict |
|---|---|---|---|---|
| 1 | Exclude infusion-rate changes in the approach | 24 / 42 | -0.060 (0.43) | Fails |
| 2 | No gap filling | 22 / 39 | -0.048 (0.46) | Fails |
| 3 | Fall sustained 5 min | 1 / 9 | n/a | Not computable |
| 4 | High loss at 15% | n/a | n/a | Not run: the primary already used 15% |
| 5 | Late window ends at t0 − 3 min | 22 / 40 | -0.039 (0.40) | Fails |

## G1 check (low weight)

- **Case selection:** 75 high-loss cases had at least two haemoglobin samples before the first fall.
- **Result:** in 10.7% of them, pressure stayed within ±20% of the early-surgery baseline at every sample **and** haemoglobin fell.
- **Pre-stated rule:** "consistent" needs more than half. **Not consistent.**
- **Not decomposed.** Under the conservation-principle rule, any explanation must be logged as a prediction before anyone looks.

## G18 (exploratory, not scored)

- **Heart rate:** the correlation of pressure with heart rate rose by a median of 0.126 more before falls than across controls (25 cases).
- **Stroke volume:** median change -0.002 (12 cases).

## Deviations and run notes

- **No deviations from the pre-registration or the code.**
- **A harmless runtime warning ("All-NaN slice")** came from G18 in cases with no usable stroke-volume windows. Those cases are dropped from the G18 count, as the code intends.

## Weight, as stated in advance

The pre-registration fixed these weights and biases before the data:
- **The fallback cohort carries half weight.**
- **Untimed boluses are present,** reduced but not removed by the bolus-signature rule.
- **Bleeding is recorded only as a case total.** That dilutes the effect towards the null; the bias was accepted beforehand, and a null still counts.
- **The high-loss threshold dropped to 15%.**

Under the standing check, a "Fails" verdict, once adjudicated, is logged in the model's Section 10. The release-profile mapping for blood loss under anaesthesia is the first candidate for revision. No new mechanism is added.
