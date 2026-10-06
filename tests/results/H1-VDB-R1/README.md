# H1 VitalDB G12: computation replication by a second model (R1, 6 October 2026)

**Inputs:**
- **GPT's audit and script, verbatim:** raw/2026-10-06_chatgpt_H1-VDB-R1.md.
- **The script, extracted unedited:** tests/scripts/h1_vdb_g12_check.py.
- **Data:** the same local VitalDB files (data/README.md). They never left this machine; GPT saw the pre-registration and the code, not the data or the results.
- **Reconciliation diagnostic:** tests/scripts/h1_vdb_r1_reconcile.py. It swaps the frozen code's readings into GPT's script, replacing two functions and nothing else.

## Results

| Run | Stable-approach rule | Missing 10-s bins inside a window | Fallback 15%: high / low qualifying | Outcome |
|---|---|---|---|---|
| Frozen code (the result of record) | A missing bin is ignored | Interpolated | 25 / 42 | **Fails** (P1 median D -0.072, p 0.48; P2 p 0.78) |
| GPT's script, as written | A missing bin fails the approach | Left missing; only adjacent pairs used | 15 / 31 | **Not runnable** (high group short) |
| GPT's script, both frozen readings swapped in | Ignored | Interpolated | 25 / 42 | **Fails**, with every number identical to the frozen run |
| GPT's script, frozen stable rule only | Ignored | Left missing | 25 / 42 | **Fails** (P1 median D -0.050, p 0.62; P2 p 0.85) |
| GPT's script, frozen window rule only | Fails the approach | Interpolated | 15 / 31 | Not runnable |

**What the runs show:**
1. **The computation is replicated.** With the same two readings, GPT's independently written script reproduces the frozen run exactly: the same counts at every step, the same 25 high-loss and 42 low-loss cases, case scores D identical (largest difference 0.0), and the same P1, P2 and P3.
2. **The whole disagreement is one reading.** It is how a missing 10-second bin is treated in the 31-minute stable approach before the fall.
   - The pre-registration says "every 10-second bin at or above 65 mmHg".
   - **The frozen code** reads that as every bin that has a value. This is implementation note 5, committed before data.
   - **GPT** reads it as every bin, so a bin with no valid value fails the approach.
   - Under GPT's reading, the test is not runnable.
3. **The window reading (GPT's second material finding) does not change the verdict.** With the frozen stable rule, the result is "Fails" either way.

**Other audit findings,** none affecting this run:
- **Edge cases that did not occur here:** an all-zero P1, a P2 that cannot be computed, and silently dropped scores. Every selected case gave a finite score.
- **Sensitivity 2** still interpolates bins.
- **Reporting gaps:** cases dropped for having no control pair, and the 15% count when the low-loss group is already short, were not reported.
- **A different G1 definition** in GPT's script: the window ends at the first sustained fall of any kind, rather than the first qualifying one.

## Open: the stable-approach reading (for James)

**The text supports both readings.**
- **Read literally,** "every bin at or above 65" can mean GPT's reading.
- **The rule's stated purpose favours the frozen reading.** The decision log, item 7, says the rule "excludes falls preceded by earlier dips", and a missing bin is not a dip. The pre-registration also expects artefacts, such as arterial blood sampling, to be removed by rule, not to disqualify a case.

**A hypothesis, not checked:** the strict reading may remove high-loss cases disproportionately (19 to 11 at 20%, against 42 to 31 low-loss). Arterial blood is sampled more often when a patient is bleeding, and each sample leaves a gap.

**Adopting GPT's reading would turn a recorded failure into "not runnable".** It would be chosen after the result was seen, and it removes evidence against the model. Under the delegation rule, that decision belongs to James.

**Claude's recommendation:**
1. Keep the frozen run as the result of record.
2. Report GPT's reading alongside it as a stated dependency: the test is runnable only under the frozen reading of missing bins.
3. Reduce the weight of the "Fails" result accordingly.
