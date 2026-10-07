# PT1 and G25: computation replicated by a second model (R1, 7 October 2026)

**Inputs**
- **GPT's audit and script, verbatim:** raw/2026-10-07_chatgpt_PT1-R1.md (prompt tests/prompts/PT1-R1.txt).
- **The script, extracted unedited:** tests/scripts/pt1_check.py. It absorbs fixed effects by sparse least squares (Frisch-Waugh-Lovell), not by the frozen code's alternating projections, and checks convergence and rank.
- **Data:** the same local tidy files (data/pt1/tidy, MANIFEST.txt). GPT saw the pre-registration, the code and the parser, not the data or the results.
- **Output:** check.json, run.log (exit 0, no warnings).

## Result: replicated exactly

| Quantity | Frozen run | GPT's script |
|---|---|---|
| Councils, lines matched, series total, kept | 121, 95, 11,495, 4,707 | Same |
| Series dropped: non-positive, below minimum | 6,345, 443 | Same (GPT counts blanks separately: 0) |
| Series kept by class (A, B, C, ambiguous) | 1,334, 1,214, 1,233, 926 | Same |
| Rows usable, PT1 and G25 | 23,373 and 18,905 | Same |
| **PT1** β (SE), one-sided p; verdict | 0.0537 (0.4053), 0.447; Inconclusive | Same to 8 digits; Inconclusive |
| **G25** δ_A, δ_B, p_A; verdict | 0.0464, 0.0041, 2.3×10⁻¹¹; Supported | Same; Supported |
| **G25-C** interaction (SE), p; verdict | 0.2247 (0.2481), 0.183; Not supported | Same; Not supported |
| Every shared sensitivity (1 to 8: PT1 and G25) | As in tests/results/PT1/README.md | Same to 8 digits, same verdicts |

**One difference, descriptive only: SS.** GPT keeps ambiguous lines in the "total in-scope spending" that defines a falling council-year (the frozen code dropped them first). Council-years with a fall: 320 (GPT) against 349 (frozen); share in which some A series fell while C kept more than half its 2014-15 total: 96.9% against 96.8%. SS is not scored.

**Extra sensitivities run by GPT's script** (G25-C and SS were not rerun in the frozen code; reported, not part of any verdict): G25-C is "not supported" in every variant (interaction 0.12 to 0.30, one-sided p 0.12 to 0.37); SS is 96.3% to 97.2%.

## GPT's audit findings, checked against the data

| Finding | Check | Effect on this run |
|---|---|---|
| Council type taken from the first row; return presence checked after line scoping | GPT's script checks every row's type and presence before scoping | **None:** the same 121 councils |
| Blank spending counted as non-positive | GPT counts blanks separately | **None:** 0 blank series |
| G25-C winsorised before rows with missing scarcity are dropped | All 121 councils have scarcity | **None:** identical estimate |
| Alternating projections never assert convergence; `pinv` accepts rank deficiency; no guard against infinities | GPT's script asserts convergence and full rank and drops non-finite values | **None:** identical estimates, so the frozen absorption converged and every coefficient is identified |
| Parser: missing single-age cells would be skipped silently in group sums | Checked the sources: no missing cells; every code has all 91 ages (both sexes for the mid-year estimates); no zero populations in the tidy files | **None** |
| 2012-based edition's publication date not in the materials supplied | Procedure log, step 2: published 29 May 2014, before the 1 February 2015 cut-off | **None:** the assignment stands |
| Lines dropped reported as normalised keys | Readable names are in the procedure log (bus lane enforcement, allotments) | Reporting only |
| SS denominator excludes ambiguous lines | See above | Descriptive only |

**Conclusion:** the computation is replicated. No audit finding changes a scored estimate or verdict in this run.
