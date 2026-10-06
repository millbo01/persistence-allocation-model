# H1 VitalDB G12: checks of the analysis code on synthetic data (6 October 2026)

**No VitalDB data was used.** These runs test the frozen analysis (tests/scripts/h1_vdb_g12.py) against synthetic datasets built in VitalDB's documented layout by tests/scripts/h1_vdb_g12_synthetic.py. The pre-registration is tests/H1 VitalDB G12 - pre-registration.md (frozen 6 October 2026, SHA-256 begins 371caf3c), Section 9, step 3.

## What was built

**Each scenario** has 25 high-loss cases (25% of estimated blood volume) and 25 low-loss cases (3%). Every case runs through the count step, then the analysis, unchanged.

**Five distractor cases** are added to every scenario. Each should be dropped:
- a bolus case (intraop_phe = 100): excluded from the primary cohort;
- a surgery under 90 minutes;
- a loss between the two groups (10%);
- a fall in the first half of surgery;
- a case with intraop_phe missing.

**Artefacts in every case:**
- three 16-second flush spikes (systolic 300);
- 20 dropped single rows;
- one 80-second gap.

**Three high-loss cases** change a phenylephrine infusion rate during the approach. They test sensitivity 1.

## Results

| Scenario | Generator: high loss / low loss | Expected | Got | P1 median D (p) | P2 p |
|---|---|---|---|---|---|
| S1 | noise: rising AR1 / none | Supported | Supported | 0.291 (7.5e-6) | 4.5e-4 |
| S2 | noise: none / none | Fails | Fails | -0.034 (0.58) | 0.73 |
| S3 | noise: rising AR1 / rising AR1 | Narrowed | Narrowed | 0.291 (7.5e-6) | 0.60 |
| S4 | noise: falling AR1 / none | Contradicted | Contradicted | -0.331 (two-sided p < 0.05) | 1.00 |
| S5 | as S1 with only 12 high-loss cases | not runnable | not runnable | - | - |
| S6 | TQ engine: tapering store / switch | Supported | Supported | 0.856 (3.0e-8) | 7.1e-10 |
| S7 | TQ engine: switch / switch | Fails | Fails | -0.031 (0.52) | 0.22 |

**Unit checks, all passed:**
- gap filling interpolates runs of 10 s or less and leaves longer runs missing;
- the artefact rule;
- AR1 recovers a known coefficient (0.7).

**Exclusions worked in every scenario:**
- all five distractors were dropped (25 high-loss cases kept);
- sensitivity 1 dropped the three infusion-change cases (22 kept);
- in S5, the step-down to 15% and then the fallback cohort were tried, in order, before "not runnable".

**Sensitivity analyses 1 to 5** gave the same verdict as the primary in every scenario.

## What this shows, and does not

**What it shows:**
- **The code returns each verdict when the data contain that pattern,** including from the TQ engine's own tapering store against its switch.
- **No false warning in S2 and S7.** The fall's last minute stays out of the late window and is controlled for, so a sudden fall with no change before it gave no false P1. This bears on Section 11, item 8 of the pre-registration.

**What it does not show:**
- **G1 was not challenged.** Every synthetic case was built with falling haemoglobin and held pressure, so the check has not been seen to fail.
- **G18 is exploratory,** and was only run, not checked.
- **The synthetic noise is simple.** Real pressure has drift, surgical stimulation and drug effects that these series lack. The verdicts here say the code is correct, not that the test is sensitive enough on real data.

**Files:** synthetic_report.json, and counts.json and summary.json for each scenario.
