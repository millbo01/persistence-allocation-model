# Tier-queue model: refinement and natural-system tests (plan, 5 October 2026)

**Status:** phase 3 (theory). James's steer, 5 October 2026: TQ2 to TQ4 jumped straight to institutions, the area with the worst data. Refine the model, and test it against known data in natural systems first.

## 1. Refinements before any test

The core is made generic. Institutional features (turnover, hiring, cover) move to a separate module that is not used in natural tests.

1. **Parts:** working parts (with intake as a kind of working part), reserves, and control parts.
2. **Reserves** deplete and refill. They are not compromised.
3. **Working parts** move through optimal, stressed (coping, then protective slowing), and compromised.
4. **Graded compromise, with overload felt against current capacity** (James's answer on TQ4). Demand stays the same while effectiveness falls, so loss compounds. The local break is a sudden exit from work (sick leave in people; in a body, perhaps a sudden shutdown).
5. **Routing.** Load passes to lower priority by the path of least resistance. Unlabelled load cannot be refused.
6. **Control parts:** routing fails when debt reaches them.
7. **Recovery.** Intake comes first, and reserves are refilled last. Recovery needs slack: it cannot begin while load is still being generated.
8. **Scars:** a lowered ceiling after compromise.
9. **Two read-outs from every run:** the record (output of the protected or regulated figure) and state signals (where strain lands).

## 2. How the natural tests work

For each system:
- **estimate its starting stage first** (optimal, stressed or compromised) from baseline state markers, because study populations need not start optimal (James, 5 October 2026; core spec and TQ5);
- map it to the model's parts **before** opening its quantitative data;
- write the model's predictions down and commit them;
- then look, and log what holds and what fails.

This is James's rule for theorising (name the place before looking), applied to the model. Contamination is declared in each case: Claude already knows parts of several of these systems, so a match is "consistent", not confirmation.

**Candidate systems,** chosen because each has a regulated figure that acts as a record, measured state signals where strain lands, a buffer, and quantitative open data:

| System | Record (defended figure) | State signals | Buffer | Break |
|---|---|---|---|---|
| Blood loss, or lower body negative pressure (LBNP) in volunteers | Blood pressure | Heart rate, stroke volume, compensatory reserve | Venous reservoir, constriction of vessels in skin, gut and kidney | Decompensation (presyncope or shock) |
| Prolonged fasting (birds, mammals) | Function of the protected organs, blood glucose | Body composition, nitrogen excretion, stress hormones, behaviour | Fat (reserve), labile protein | The stage 3 switch at a fat threshold |
| Kidney nephron loss | Serum creatinine | Hyperfiltration per nephron, protein in the urine | Spare nephrons (redundancy) | Creatinine rising steeply once GFR falls below about half |
| Honeybee colony after forager loss | Brood care, colony weight | Task reallocation, worker age at first foraging | Hive bees, stores | Colony failure (K1b already logged) |

## 3. First test: blood loss and LBNP (proposed)

**Why first.** It has the cleanest record against state signals, a well-known break, controlled human experiments with graded load (LBNP), and documented recovery.

**Mapping:**
- **Working parts:** heart (top), brain (top), kidney, gut and skin (lower priority).
- **Reserve:** the venous reservoir and other circulating-volume buffers.
- **Control parts:** the vasomotor centre and the baroreflex.
- **Record:** mean arterial pressure.
- **State signals:** heart rate, stroke volume, peripheral and splanchnic constriction.

**Model predictions (committed before opening the quantitative data):**
- **N1.** Blood pressure stays near baseline while heart rate rises and stroke volume falls from the start of the load. The state signals move first.
- **N2.** Blood flow to lower-priority parts (skin, gut, kidney) falls before flow to the brain or heart.
- **N3.** The break in blood pressure comes when the buffer is exhausted, and it is steep compared with the earlier change. Once control parts are hit (the vasomotor centre short of blood), the order breaks down.
- **N4.** If the buffer is a stock, the break comes at roughly the same cumulative loss whatever the rate of bleeding. If buffer release is rate-limited, faster loading breaks earlier in cumulative terms. This rule decides whether the buffer behaves as a stock or a flow.
- **N5.** Individuals with a larger buffer (compensatory reserve) last longer before the break, and their blood pressure stays flatter.
- **N6.** On recovery (load removed, volume restored), heart rate and blood pressure return quickly, while the lower-priority beds and reserves (kidney function, red cell mass, iron) return last.

**Contamination declared.** Claude knows the ATLS class scheme (blood pressure held until roughly 30% to 40% loss) and Convertino's compensatory reserve work in outline. N1, N2 and N3 are partly known to Claude, so a match there is "consistent". N4 and N5 are the more informative predictions.

## 4. Order of work

1. Write the refined core (a spec plus a clean script) and re-run a generic case. **Done 5 October 2026:** theory/tier_queue_core_spec.md, theory/sim/tq_core.py, TQ5 (baseline dependence).
2. Blood loss and LBNP: gather open quantitative sources, then check N1 to N6. **Done 5 October 2026:** theory/natural_test_blood_loss.md (N1, N3, N4, N5 consistent; N2, N6 partly; heat stress shows the starting-state effect; two mismatches with proposed refinements: top shares an upstream supply; the break is an active threshold switch).
3. Fasting, then kidney, then honeybees, each with predictions committed first. **Fasting done 5 October 2026:** theory/natural_test_fasting.md (F2, F5 consistent; F1, F3 consistent but known; F6 consistent for starvation, opposite under restriction; F4, F7 untested; the knee came from the source's own hypothesis, declared).
4. Stock-take against paper one.
