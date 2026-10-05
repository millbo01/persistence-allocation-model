# Natural test 2: prolonged fasting. Predictions, committed before the data are opened (5 October 2026)

**Status:** theorising (phase 3).

**Model:** the tier-queue core with the two refinements adopted after natural test 1 (James, 5 October 2026):
- **A, shared upstream supply:** a part's capacity follows the supply it depends on.
- **B, an active threshold switch in control:** it sheds a commitment when the buffer can no longer cover demand.

A third element is new for this test: the reserve's release falls in proportion to its level below a knee, because a small store cannot release fast enough.

**Derivation:** theory/sim/tq6_fasting.py and outputs/2026-10-05_TQ6 (illustrative parameters). The model was run from a fat start, a lean start (60% of the fat start), and a fat start with 30% higher demand (cold).

## Starting stage

Wild fasting birds such as breeding penguins and geese begin a natural fast fattened, so they are read as optimal. Laboratory rats and humans start wherever their diet and housing left them. Each study's starting fat and condition will be noted before its results are read.

## Predictions

| No. | Prediction | Model output | Contamination |
|---|---|---|---|
| F1 | Depletion order: fat first and most; labile low-priority organs (gut, liver, spleen) next; muscle later; brain and heart least | Built into the priority order | **Known.** The Cahill-type table of tissue losses was already reported in this conversation |
| F2 | Phase III (rising protein use) begins at about the same fat level whatever the starting fat. A leaner start reaches it sooner, and the length of phase II scales with the fat above that level | Onset at fat 19.9 (fat start, day 46) against 18.8 (lean start, day 26) | Partly known: Claude knew that phase III follows a "threshold adiposity". The invariance across starting fat, and the scaling of phase II, were not known to Claude |
| F3 | The control switch (shedding the commitment: abandoning the egg; also the shift to food search) comes at the onset of phase III, within days | 2 to 3 days after onset in all three runs | **Known:** egg desertion at a critical body mass close to phase III was already reported in this conversation |
| F4 | The defended figure (supply to vital organs; in practice blood glucose) holds through phases I and II and falls only late in phase III | Record first below 99% about 11 to 16 days after phase III onset | Partly known |
| F5 | A leaner, stressed start enters phase III sooner, at the same fat level | Day 26 against day 46 | Not known as a quantitative result |
| F6 | Refeeding order: gut and intake first, then muscle, vital tissues, fat last | Gut back to 95% at day 126 (6 days after refeeding), muscle 148, vital 155, fat back to start last (205 or more, or not reached) | Gut first is **known** (stage 3 rats, stopover birds). Fat last is the model's prediction; Claude knows of a contrary human result (catch-up fat) from a source James has ruled out of this work |
| F7 | Higher energy demand (cold, activity) moves phase III to a **higher** fat level and an earlier day, because release must meet a larger demand. This contrasts with blood loss, where the break came at the same cumulative loss whatever the rate | Onset at fat 25.6 (cold) against 19.9 | Not known to Claude |

**Most informative:** F2, F5 and F7, because Claude did not know them in advance. F1, F3 and part of F6 can only be "consistent".
