# PT1 and G25: results of the single run (7 October 2026)

**Status: ADJUDICATED (7 October 2026).** Computation replicated exactly by a second model (tests/results/PT1-R1/README.md). Blind adjudication by GPT (raw/2026-10-07_chatgpt_PT1-ADJ1.md), accepted as given: **PT1 Inconclusive (full weight); G25 Supported (half weight); G25-C Not supported (half weight).** No faults found; D-1 to D-5 and the missing projections do not make any verdict unsafe; none of G1 to G6 changes a verdict.

**Provenance**
- Pre-registration: tests/PT1 Priority test - pre-registration.md (frozen 7 October 2026, SHA-256 begins a4aab81d).
- Code: tests/scripts/pt1_councils.py, unchanged (SHA-256 995abfc5...). Classification SHA-256 begins faf45875.
- Data: data/pt1/tidy/ (checksums in data/pt1/tidy/MANIFEST.txt), built by tests/scripts/pt1_parse.py with deviations D-1 to D-5 (procedure log).
- Output: summary.json (full), counts.json, run.log.
- **Attempt 1 stopped with an error before any result** (duplicate code in the funding table); fixed by D-5, approved by James; this is attempt 2. Procedure log, step 7.

## Verdicts (as computed)

| Test | Weight | Estimate | Verdict (frozen table) |
|---|---|---|---|
| **PT1** (fixed against dynamic priority) | Primary | β = 0.054 (SE 0.405), one-sided p = 0.45; 95% CI −0.75 to 0.86 | **Inconclusive (insufficient precision).** β is not significant, but the upper bound (0.86) is above β* = 0.25 |
| PT1-S (graded or stepped) | Secondary | Not run | Runs only if PT1 finds an effect |
| **G25** (statutory class predicts protection) | Half | δ_A = 0.046 (one-sided p = 2×10⁻¹¹); δ_B = 0.004 (p = 0.27); A − B, p = 1×10⁻⁸ | **Supported** (δ_A > 0, and the point estimates are ordered δ_A ≥ δ_B ≥ 0) |
| G25-C (scarcity reveals the order) | Half | A × scarcity = 0.22 (SE 0.25), one-sided p = 0.18 | **Not supported** |
| SS (strict or shared) | Descriptive | 349 council-years with a fall in in-scope spending; in 96.8%, some A-class series fell while the C-class series kept more than half their 2014-15 total | Not scored |

**Sample:** 121 councils, 93 lines, 23,373 rows (PT1); 18,905 rows (G25). Realised client growth: γ = −1.44 (PT1).

**In plain terms (computed, not adjudicated):**
- **PT1.** Projected client growth published before the budget showed no detectable link with how well a line's spending per head was protected. The estimate is close to zero, but too imprecise to rule out an effect of the size set in advance as meaningful. Under the frozen table that is inconclusive, not support for fixed priority.
- **G25.** Within a council and year, lines with a statutory duty (class A) had real spending per head growing about 4.6 percentage points a year faster than discretionary lines (class C). Lines with a duty of uncertain level (class B) were not distinguishable from C.
- **G25-C.** The A over C gap was not detectably larger where funding fell more.

## Sensitivity analyses (not part of the verdict)

| No. | Variant | PT1 β (95% CI) | PT1 verdict | G25 verdict |
|---|---|---|---|---|
| 1 | Adult social care included | 0.030 (−0.75 to 0.81) | Inconclusive | (not run) |
| 2 | Long difference, 2014-15 to 2019-20 | −2.59 (SE 2.16), one-sided p = 0.88, N = 4,626 | (no verdict) | (not run) |
| 3 | Ambiguous lines at lowest class | (not run) | | Supported (δ_A 0.035, δ_B 0.009) |
| 3 | Ambiguous lines at highest class | (not run) | | Supported (δ_A 0.045, δ_B 0.014) |
| 4 | RO6 client lines added | 0.152 (−0.65 to 0.95) | Inconclusive | Supported |
| 5 | Ten-year projection horizon | 0.201 (−0.18 to 0.58) | Inconclusive | (not run) |
| 6 | No winsorising | 0.061 (−0.89 to 1.01) | Inconclusive | Supported |
| 7 | London excluded (89 councils) | 0.003 (−1.20 to 1.20) | Inconclusive | **Partly supported** (δ_B = −0.003, so the order B ≥ C fails; δ_A still positive, p = 1×10⁻⁷) |
| 8 | Minimum £50,000 | −0.029 (−0.85 to 0.80) | Inconclusive | Supported |
| 8 | Minimum £250,000 | 0.025 (−0.77 to 0.82) | Inconclusive | Supported |

**PT1 is inconclusive in every variant;** no variant's upper bound falls below 0.25. **G25's A-class protection holds in every variant;** the B-above-C step is small and fails its ordering without London.

## Notes on the run

1. **A warning during G25-C** ("divide by zero encountered in log") comes from councils with zero Core Spending Power in 2015-16 or 2019-20: the Dorset reorganisation codes (E06000058, E06000059 before 2019; E06000028, E06000029 in 2019). None is in the panel (they lack the same code in all six years), and scarcity is mapped only to panel councils, so the warning does not reach any estimate. Checked by a diagnostic run with output to a scratch folder.
2. **SS is descriptive and coarse.** "Some A-class series fell" is likely in almost any council-year with about a dozen A series, so the 96.8% says little about strict order on its own.
3. **Contamination (pre-registration Section 8):** G25 carries half weight because Claude knew the broad pattern in advance.
