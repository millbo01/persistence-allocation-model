# Natural test 11: the Felicity ratio in muscle (results, 5 October 2026)

**Status:** theorising (phase 3); surface level. Predictions FM1 to FM5 were committed before any source was opened (theory/natural_test_felicity_muscle_predictions.md, commit a06cc46).

**Sources** were found by web search and read through search summaries or abstract pages, not in full:
- S1. Howatson, van Someren and Hortobágyi 2007 (Int J Sports Med; summary at coachsci.sdsu.edu): 10 against 45 maximal eccentric contractions as the first bout; 45 as the second bout, 14 days later.
- S2. Chen, Nosaka and colleagues (Edith Cowan University repository; Eur J Appl Physiol): first bouts at 10% and 20% of maximal strength, or maximal isometric contractions, against a maximal eccentric second bout; and "protection by low-intensity eccentric contractions remains for 2 weeks but not 3 weeks".
- S3. Nosaka and Newton 2002 (J Strength Cond Res): repeat bouts at 50% of maximal force 2 and 4 days after the first.
- S4. Search summaries of studies with a maximal second bout 2 days after the first, and of a study grading second-bout intensity during incomplete recovery (ultrasound).
- S5. Lavender and Nosaka (summarised in a PMC review of eccentric exercise in older adults, PMC10492690): repeated bout effect in older and young adults at 7-day and 4-week gaps.
- S6. Hamstring strain studies (PMC2923440; Br J Sports Med 46:81): re-injury risk after a previous strain; scar persistence; strain distribution next to scar tissue.
- S7. Connolly, Reed and McHugh 2002 (J Sports Sci Med): no protection of the opposite limb.

## Results

| Prediction | Finding | Verdict |
|---|---|---|
| FM1. A recovered first bout protects at the same load | The repeated bout effect: damage markers reduced in the second bout (S1; protection lasting up to about 24 weeks, from the re-tuning test) | **Consistent** (known in advance) |
| FM2. Protection is referenced to the previous peak load; a milder first bout protects only partly | With the same peak intensity (maximal), a first bout of 10 contractions gave the **same** protection as 45 (S1). First bouts at 10% or 20% of maximal strength protected against a maximal second bout, but less than a maximal first bout (S2) | **Partly consistent.** Protection follows the previous **peak load**, not cumulative work: the Kaiser idea. But the threshold is graded, not sharp: a lower peak still protects somewhat above itself |
| FM3. A second bout before recovery is complete gives strain at or below the previous peak | Repeat bouts at the same moderate load 2 and 4 days later did not add damage or slow recovery (S3). A **maximal** repeat bout 2 days later caused further acute impairment, and more damaged area than lower-intensity repeats (S4) | **Inconsistent as written** (see below) |
| FM4. Protection fades | Low-intensity protection lasted 2 weeks but not 3 (S2); maximal protection up to about 24 weeks | **Consistent.** Duration also depends on the dose of the first bout |
| FM5. A compromised start shows less protection | Older adults: similar protection at a 7-day gap, smaller at a 4-week gap (S5) | **Partly consistent:** protection fades faster rather than being smaller from the start |

**Also found, not predicted:** a first bout on one limb gave no protection to the other limb (S7). Protection sits in the part itself (local re-tuning), not in control.

## FM3: explanation named before checking, then checked

**Named place (before looking, per James's rule):** the prediction assigned the wrong stage. Incomplete recovery after a short, coupled bout is the coping stage, not a scar. In the model, a scar follows compromise. The proper test is a muscle carrying a real scar from an earlier injury: it should show strain below its previous peak load (ratio below 1).

**Checked (S6):** a previous hamstring strain is the strongest risk factor for re-injury (two to six times the risk). Scar tissue is visible from about 6 weeks after injury and persists in animal models. Under the same running load, previously injured muscles show greater peak strain in the tissue next to the scar. That is strain appearing at loads the muscle once carried without it: **ratio below 1 in scarred muscle. The named explanation holds**, at surface level (epidemiology plus imaging; no direct Felicity measurement).

**Why repeat loading during ordinary recovery adds no damage (James, 5 October 2026):** the repeat load does not exceed the no-strain ceiling, which the first bout raised to that load. The model already says this; no extra explanation is needed. What is open is how the ceiling rises within days while maximal force is still reduced (the same load damaged the muscle the first time, so the governing ceiling is not maximal force). Candidate mechanisms (loss of the most susceptible fibres, neural or connective-tissue adaptation) sit below the model's level and are logged, not tested.

## Outcome against the committed verdict rule

The rule: if FM2 and FM3 hold, the Felicity ratio enters the model as a read-out of starting stage derived from G7 and G8; if FM2 fails, it is not adopted.
- FM2 holds in its essential part (peak-referenced), with a graded rather than sharp threshold.
- FM3 holds once the stage is assigned correctly (scar), and fails as written for ordinary incomplete recovery.

**Recommendation (for James):** adopt the Felicity ratio as a read-out derived from G7 and G8, with three refinements:
1. the reference is the previous **peak** load, not cumulative load;
2. the threshold is graded: protection extends somewhat above the previous peak and is greater the higher that peak was;
3. a ratio below 1 marks a **scar** (compromise), not ordinary recovery: during recovery from a coupled acute episode, protection arrives before capacity fully returns. This makes the ratio more useful, because it separates "recovering" from "scarred", which the record cannot.

**Decision (5 October 2026):** adopted in v0.8 as the Felicity read-out, on Claude's recommendation; James delegated the call ("your call"). Re-tuning in the model and engine is now set by the episode's peak load. TQ8 C7 reproduces the pattern in the engine.

**Weight:** surface level; summaries only; FM1 and FM4 known in advance; FM3's rescue is a reassignment made after the result and checked once.
