# The tier-queue model, v0.1 (canonical state, 5 October 2026)

**Status:** working model (phase 3).

This is the single reference for the model as it stands. Earlier documents are its working history: theory/tier_queue_model_DRAFT.md, theory/tier_queue_core_spec.md, theory/sim/tq_core.py, and the natural test files. Changes go here as new versions, with what changed and why.

![Tier-queue model](figures/tier_queue_diagram.png)

## 1. The principle

A goal-directed system is a tree of parts. Each part does work and has a limited capacity. When demand exceeds what a part can do, the excess is not removed. It is drawn from a reserve, passed to parts of lower priority, deferred as debt, or sent out across the boundary.
- Load therefore runs downhill, from protected parts to expendable ones.
- The protected part's output, which is what the system records, stays normal while the parts below absorb the excess. It changes only when they can absorb no more. **The record sees compromise, not stress.**
- Recovery runs the other way, starting with the intake. It cannot begin while load is still being generated, and debt nobody knows about is never repaid.

## 2. The parts

| Kind | What it is | Examples |
|---|---|---|
| **Working part** | Does a job with a limited capacity | Brain, heart, nephron, nurse bee, front-line staff |
| **Intake** | A working part whose job brings resource in. Every repayment depends on it | Gut, leaves, roots, foragers, a referral or recruitment function |
| **Control part** | A working part whose job is routing. It holds the threshold switch | Vasomotor centre, hypothalamus, an institution's management |
| **Reserve** | A stock that is drawn on and refilled. It runs full, drawing or empty, and is not itself damaged | Fat, iron stores, venous blood volume, honey stores, budget reserves |

Each working part has five properties:
- a **priority** (how strongly it is protected);
- a **capacity**;
- a **renewal class**: fast (a conveyor such as the gut lining), slow (liver), or none (fixed capital: neurons, heart muscle);
- a **ceiling**, lowered by scars;
- its **spare capacity** (redundancy).

**Priority rule:** priority rises with how vital a part is, and falls with how fast it can be rebuilt and how much spare capacity it has.

**State, for working parts only:**
- **Optimal:** within capacity, reserve full.
- **Stressed but coping:** covering the excess from reserve, spare capacity or debt still within its recovery window. Protective slowing begins here, giving up some capacity to protect the part.
- **Compromised:** debt held beyond the recovery window, so capacity is eroding.

Losses compound, because overload is felt against what the part can do now, not what it could do before.

## 3. How the parts interact

1. **Routing.** A part's shortfall goes first to the reserve, then to spare capacity in lower-priority parts, then is displaced onto them (lowest first). Whatever cannot be placed becomes the part's own debt, or leaves across the boundary.
2. **Labelled and unlabelled load.** Load that arrives with its origin can be refused by a part already under strain, which keeps the strain visible higher up. Load passed on through opacity has no origin, so it cannot be refused and sinks to the lowest tier.
3. **Shared supply.** A protected part depends on upstream supply, so it is protected only partly when that supply falls. (Brain flow falls with cardiac output.)
4. **Threshold switch.** At a set depletion of the buffer, not at exhaustion, control changes mode. It sheds a commitment, changes metabolism or behaviour, and often makes the record move.
5. **Control failure.** If debt reaches the control part, routing stops following priority: protected parts are hit while buffers remain. (Division of labour breaks down in collapsing colonies.)
6. **Compounding on survivors.** Parts carrying displaced or covered load are damaged by it. Their failure adds load to the rest: hyperfiltration in the kidney, precocious foraging in bees, the vacancy cascade in teams.
7. **Recovery.**
   - Slack repays debt and refills reserves, in this order: intake, then the working parts the next job needs, then reserves.
   - Recovery requires slack: it cannot start while load is still generated.
   - Debt nobody knows about is not repaid.
   - After compromise, renewable parts return with a scar (a lower ceiling, a shorter tolerance window, more resistance). Fixed capital keeps its loss: the point of no return.
8. **Starting state.** A system need not start optimal. Its stage at the start sets how much room it has. The stage is read from state signals, because the record cannot show it.

## 4. Read-outs

- **The record:** the output the system routinely watches, which is the top's served demand. It is flat through stress and moves at compromise, or at the switch.
- **State signals:** each part's strain, debt, capacity and reserve level. They move from the start of stress. In opaque systems they are filtered, mistranslated or lost.
- **The ledger:** demand = work done + reserves drawn + debt + load leaving the boundary. Nothing leaves the ledger except through work done or the boundary.

## 5. Mapping a system: how to identify the parts and assign labels

Do this before opening any outcome data.

1. **Boundary and currency.** Name the system and its boundary, and choose a currency that obeys a balance (energy, blood volume, filtration, labour hours, cases).
2. **Load.** What demand arrives, and from where?
3. **The record.** What figure does the system, or its observer, routinely watch and defend? (Blood pressure, creatinine, stores and brood, a performance indicator.)
4. **The top.** Which part's output is that figure? Is it fixed capital?
5. **The parts.** List the parts that do work. For each, decide:
   - its **role**: working, intake or control;
   - its **priority**: how vital is it, can it be rebuilt and how fast, and how much spare capacity does it have?
   - its **renewal class**: fast, slow or none.
6. **The reserves.** Which stocks are drawn first? Does release slow as they shrink?
7. **Labelled or not.** Does load passed down arrive with its origin? Can the receiver refuse it? Do state signals reach the top?
8. **Control and the switch.** What routes load? Is there a known mode change at a set depletion?
9. **State signals.** For each part, what measure shows its strain, debt or reserve?
10. **Starting stage.** From baseline state markers, classify the system as optimal, stressed or compromised. Population "normal" ranges may describe the stressed stage.
11. **Predictions.** Write the generic predictions in Section 6 for this system before looking at outcomes.

## 6. Generic predictions (what the model always says)

| No. | Prediction |
|---|---|
| G1 | The record stays near normal while state signals and reserves move |
| G2 | Lower-priority parts are drawn down first, in reverse priority |
| G3 | The break comes at a set depletion of the buffer, not at exhaustion. If the buffer is a stock, the break comes at the same cumulative load whatever the rate |
| G4 | A larger buffer gives a longer silence and a sharper break; a stressed or compromised start breaks sooner |
| G5 | Survivors that carry extra load are damaged by it, so loss compounds |
| G6 | Recovery runs intake first and reserves last, and needs slack. Unknown debt is not repaid, so the record recovers before the state does |
| G7 | Parts that cannot be rebuilt keep their losses; renewable parts return with a scar |

## 7. Evidence so far, and its weight

- **Simulations TQ1 to TQ6:** illustrative parameters.
- **Surface checks in four natural systems:** blood loss, fasting, kidney and honeybees (theory/natural_test_*.md; theory/natural_tests_patterns.md). All were consistent in shape.
- **Limits:**
  - the sources were read through summaries;
  - several predictions were known in advance;
  - refinements A and B and the reserve knee were built from the literature;
  - the most informative predictions are untested: whether higher energy demand moves the fasting threshold, and whether a larger buffer gives flatter pressure.

## 8. Way forward (James, 5 October 2026)

1. **Test, revise, test again,** in more natural systems, at surface level first, updating this file with each version.
2. **Keep the best datasets unopened** for a final stress test once the model is consistent. That list is to be agreed before any of them is used.
3. **Run full stress tests on those held-out datasets,** with predictions committed in advance.
4. **Only then, novelty.** Hand pass 1 (theory/novelty_tier_queue_pass1.md) and the provenance log (theory/tier_queue_provenance.md) are kept for that stage and are not acted on now.

## 9. Open questions

- How does priority combine vital, irreplaceable and redundant: as a product, or by rank?
- Is the threshold switch always protective (an active choice) or sometimes simply failure?
- Does a high-reserve system decline faster after its break? (Cognitive reserve may say yes, from recall, to check.)
- Restriction against starvation: does the type of load change the recovery order?
- What sets the boundary between "labelled" and "unlabelled" in natural systems?
