# PT1: checks of the analysis code on synthetic data (7 October 2026)

**No real data was used.** This tests tests/scripts/pt1_councils.py against synthetic tidy data built by tests/scripts/pt1_synthetic.py, in the layout the code reads. Pre-registration: tests/PT1 Priority test - pre-registration.md (frozen 7 October 2026, SHA-256 begins a4aab81d), Section 9, step 3.

**How the data was built:**
- **Councils:** 80 or 120 single-tier councils (20 in S3), plus three that must be dropped:
  - a district council (wrong type);
  - the City of London code;
  - a council missing a year.
- **Lines:** the real in-scope line names from the frozen classification, so that name matching is exercised.
- **Planted effects:**
  - projected growth (by council and client group);
  - realised growth tracking the projection with noise;
  - council-year shocks;
  - line trends;
  - noise.
- **Distractors:**
  - the real "On-street parking" line made negative (positivity rule);
  - "Tourism" made tiny (minimum rule);
  - "Allotments" missing in 2016-17 (all-years rule);
  - a duplicated "Library services" row in one council (duplicate-name rule).

## Results

| Scenario | Planted | PT1 expected / got | β (95% CI) | PT1-S | G25 expected / got | Match |
|---|---|---|---|---|---|---|
| S1 | β = 0.6, classes A > B > C | H-fixed fails / **H-fixed fails** | 0.609 | graded | Supported / **Supported** | yes |
| S2 | β = 0, precise | H-fixed supported / **H-fixed supported** | 0.014 | - | Supported / **Supported** | yes |
| S3 | β = 0, very noisy, 20 councils | Inconclusive / **Inconclusive** | 0.38 | - | (not checked) / Partly supported | yes |
| S4 | β = -0.6 | Contrary / **Contrary** | -0.519 | - | Supported / **Supported** | yes |
| S5 | a step at projected growth 0.04 | H-fixed fails / **H-fixed fails** | 0.505 | **stepped** | Supported / **Supported** | yes |
| S6 | β = 0, classes reversed (C > A) | H-fixed supported / **H-fixed supported** | 0.014 | - | Contradicted / **Contradicted** | yes |
| S7 | β = 0, no class effect | H-fixed supported / **H-fixed supported** | 0.014 | - | Fails / **Partly supported** (seed 1) | **no** |

**S7 is a chance false positive, not a bug.**
- With seed 1, G25 found $\delta_A$ = 0.0006 per year (one-sided p = 0.007). That is a 1-in-100 event at the frozen α.
- **Re-run with seeds 2, 3 and 4,** S7 gave **Fails** each time ($\delta_A$ between -0.00015 and 0.00025, p from 0.16 to 0.71).
- **It shows a property of the frozen G25 test:** it has no smallest meaningful effect. With very large samples and very low noise, a trivially small difference can reach significance.
- **Recorded as a limitation,** to be reported with the real result. The real effect sizes and noise will be shown alongside the verdict.

**The full pipeline** (`analyse()`, with all eight sensitivity analyses, G25-C and SS) ran on S1 without error.
- **Outputs:** S1_full/summary.json and synthetic_report.json.

**Bugs found and fixed during these checks (before any data):**
1. **A duplicated column** when the council is both a fixed effect and the cluster (the long-difference analysis).
2. **No duplicate-name rule.** The generator's first distractors reused real line names, which merged two series. A rule was added and logged as an implementation note: a council's series is dropped if its line name occurs twice in the same year and form.
