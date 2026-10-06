# Tier-queue model: changelog (5 October 2026)

The history of the canonical model (theory/TIER_QUEUE_MODEL_v*.md), moved out of the model document at v0.15 so that the document states the model as it stands. Earlier versions remain in the repository.

## Renamed (James, 6 October 2026)

The model is now called **the Persistence Allocation Model** (formerly the tier-queue model). The name changes from now on. File names, engine names (tq_*, TQ runs) and frozen documents, including the H1 VitalDB pre-registration, keep the old name.

## Changes in v0.17 (James approved, 6 October 2026)

**A simplification:** the vocabulary is frozen at this version. The central claim was reworded (Claude's rewording, approved by James). Decisions with James's wording are in theory/v0.17_pending.md. The engine work behind them is TQ10 to TQ13b (theory/sim/outputs/).

| No. | Change | Source |
|---|---|---|
| 1 | **The governor is a separate, parallel system, and it only allocates.** It holds the levels persistence depends on ("maintain X, Y, Z") by sharing out resources. It sets no work targets. It is a function, not always an organ | James; repair and allocation scan |
| 2 | **Parts have no demand.** A part works to the limit of the resources it is given, set by the scarcest one it needs (law of the minimum). "Demand" is the name for reallocating resources to hold the governor's levels | James |
| 3 | **Several resources, each with its stores** (more than one per resource allowed: a fast store and a slow one), released, refilled and spilled by the governor. Some resources cannot be spilled and are held by controlling intake | James; scan; TQ12, TQ13b |
| 4 | **A part's only state is its units:** active, switched off, or lost; some lost units scarred. Condition, dose and the consolidation floor are removed | James; TQ13 |
| 5 | **Three outcomes, kept apart.** Switched off: comes back quickly, not harm. Lost: rebuilt over the rebuild time, delayed recovery, not harm. **Scar:** damage to the template, the only real harm | James |
| 6 | **Harm comes only when supply falls faster than a part can scale down.** Otherwise units are switched off in an orderly way: consolidation, like switching servers off | James; TQ13 |
| 7 | **Template damage:** disorderly loss in an episode past a limit set for each part when mapping | James (option 1) |
| 8 | **A part keeps only its basal maintenance and its work.** Basal maintenance is paid first; work never stops for repair | James; TQ12b |
| 9 | **Repair is a network, represented like everything else** (James). The repair workforce is a set of parts whose work is renewing and rebuilding other parts' units. It has its own resources and stores, the governor allocates to it by rank, and its capacity is shared across parts. It is local where resident cells do it and mobile where it is dispatched from a central source. Under a sustained shortfall the governor ranks repair down; under an acute threat it pre-positions it. No new element: parts, resources, ranks and the shared-repair coupling route already exist | James; repair scan addendum (Kiecolt-Glaser 1995; Marucha 1998; Dhabhar; macrophage reviews) |
| 9a | **Every part's basal maintenance comes before any support work.** A part cannot die, so no allocation may starve a part's existence to fund another's work | James (TQ13b question (a)) |
| 10 | **Parts do not die; the system dies,** when load reaches the top (the exhaustion cascade) or a non-bypassable link is cut (severance) | James |
| 11 | **The intake rule.** What is upstream of X is maintained at all costs. The intake's maintenance is support at all times; its work only while it has something to take in | James; TQ11b, TQ13 |
| 12 | **Economising** is the governor's anticipation: an even cut, made early, that preserves the stores. It is not what prevents damage (the allocation order already does that) | James; TQ11 |
| 13 | **Protective slowing** is the governor's choice, not a part's | James |
| 14 | **Carried from v0.16 but not needed by any engine result so far:** computed marginal value, the horizon, signal gain, labelled refusal, peak protection, growth, reserve memory. They are kept, flagged, each with its own untested prediction (Section 9) | TQ11 parsimony check |
| 15 | **Open questions are tiered:** model-threatening, refining, niche | Perplexity check |
| 16 | **Section 1 is unchanged** (James's wording); a proposed rewording follows it | |
| 17 | **Superseded at model level:** the repair-share rule inside the part (TQ12b) and the per-part rebuild time. Renewal and rebuilding are now the repair network's work. The frozen engine still uses the in-part rule (Section 10) | James |

**Not yet updated for v0.17:** the maths, the diagram, and the frozen engine (claim order and in-part repair; see the model's Section 10).

## v0.16 engine: TQ10b, protective slowing (James chose option B, 6 October 2026)

- **Rule:** a part below condition 0.9 lowers its demand to what it can do, never below its demand floor, until it is back at 0.99. Predictions were committed first, and TQ10's outputs are unchanged with slowing off.
- **Fixes:** two implementation errors, fixed and logged: the floor was ignored at first, and slowing was released at once for a part that had lost its template.
- **Results:** the trap is gone; deterioration is graded; G10 is reproduced in the diagnostic (parts first after acute, reserve first after chronic); exhaustion and severance hold; G12, G18 and the spiral are qualitatively unchanged; overuse scars are small.
- **Question for James:** can control override protective slowing?

## v0.16 engine: TQ10 (James approved the build, 6 October 2026)

- **New module:** theory/sim/tq16.py (v0.16 rules); tq_core.py untouched, and TQ5 to TQ9 identical.
- **Process:** predictions, build notes and scenario parameters were committed before any run. One implementation bug (load ratio) was fixed after the first run and logged.
- **Results:**
  - reproduced: throughput tracking, the flat record and order of loss, rate-independence, exhaustion, severance, weak templates and fixed capital, and G12 and G18 (weaker);
  - partly reproduced: economising (timing), deterioration (large doses run away), scar (through permanent overload, not a patch), economising preventing deterioration, and the spiral;
  - not reproduced: recovery order (G10).
- **Main finding:** deterioration is all-or-nothing as built. Options to James: unmet-share deprivation, protective slowing, patch under load.
- **Model document:** status entries only.

## Changes in v0.16 (James approved, 6 October 2026)

**Clarification after approval (James, 6 October 2026):**
- Within its ceiling, a part's throughput tracks demand whenever supply, reserves included, covers it. There is no separate sustained-capacity limit and no throughput target.
- Demand is whatever the governor needs to hold its level.
- Applied in Section 2 (structural and deployed capacity) and in the maths (Section 4); the open question on reserves and throughput is closed.

From discussion of the TQ9 results, with James's decisions recorded in theory/v0.16_pending.md. Supporting checks: theory/framing_crosscheck.md (engineered and natural systems) and theory/deterioration_threshold_scan.md (deterioration against scarring). Neither carries evidential weight.

1. **Two routes to outright failure** (James).
   - **Exhaustion:** no part fails while there is somewhere for its load to go.
   - **Severance:** a non-bypassable link is cut, with receivers intact.
   - The control cliff is generalised to non-bypassable links (central control, transporters, series links). G20 added.
2. **Work is local; load is displaced** (James).
   - Load arises in two ways: throughput maxed, or supply diverted. A priority change is a condition, not a cause.
   - Routing becomes resources taken from lower-priority parts (first their slack, then beyond it as load), plus load backing up a dependency. Spare capacity and displacement merge into one step.
   - The "landing forms" proposed by Claude were dropped (James), as was any distinction between a part doing another's work and resources being redirected.
3. **What counts as one part** (James). Duplicates that share resources and balance load are one part. Series links are separate parts linked by dependency. "Part" means a working part; a reserve is not a part (Section 1 and Terms).
4. **Repair is the container refilling** (James). There is no separate repair pool: returning supply reaches parts in priority order, and each part refills once its own leak stops. The recovery formula is reread as the order of resupply.
5. **Economising is the switch's action** (Claude's recommendation, James agreed). Control lowers demand and capacity together, reversibly, down to each part's demand floor. **Deferral is withdrawn from economising:** the v0.11 shed and debt split is reversed (James), and the fitted deferred share (0.5) is withdrawn. G16 reworded.
6. **Deterioration and scars** (scan; James).
   - Deterioration comes only from load beyond capacity, and is reversible while the template survives.
   - A scar is template loss, or repair that stalls, followed by a patch that keeps integrity without function.
   - New part properties: template and demand floor.
   - "Compromised" is redefined. G7 reworded; G19 (three kinds of capacity loss) added.
7. **G8 restated:** the chronic state permits deterioration; the dose decides whether it scars.
8. **Contrast case:** road traffic, as load mechanics without a system-level objective.
9. **Central claim and "In parts" revised** on Claude's recommendation (James deferred): resources taken rather than load passed; deterioration rather than debt; the scar sentence tied to template loss; working parts distinguished from reserves.
10. **Maths and diagram updated** (theory/tier_queue_math_v0.16.md, the model's target form, with theory/tier_queue_math_v0.15.md kept as the engine's description; theory/figures/tier_queue_diagram_v016.svg and .png). "Every repayment depends on it" (the intake) became "every refill". **Not yet updated:** the engine (Section 10 lists the departures).

## v0.15 engine update: TQ9 (engine work D, James approved, 5 October 2026)

- **Engine (opt-in; TQ5 to TQ8 unchanged):** network loops, local stocks per part, record dynamics (knocks restored from remaining release) and capacity insults (theory/tier_queue_core_spec.md; theory/sim/outputs/2026-10-05_TQ9/README.md). Predictions committed first (theory/sim/tq9_predictions.md).
- **Results:**
  - G12 reproduced (mechanism check).
  - G18 reproduced for shared dependency.
  - The spiral partly reproduced: loop worse and kidney relief helps where it engaged (2 of 20 cells: large fall, little slack). The record never broke. Heart relief made it worse when the heart's signal was filtered.
  - MR reproduced by construction.
- **Model document, status only (no new elements):** G12 and G18 status, engine limitations, two open questions (relieving a part control cannot see; economised work and dependants).
- **Maths:** loops and local stocks written; G12 and G18 marked as simulation results.

## Changes in v0.15 (James approved, 5 October 2026)

- **Consolidation, no new content.** The model document now states the model as it stands. Version tags were removed from the body; this changelog holds the history; answered or withdrawn open questions moved here (below).
- **Consistency fixes:** co-movement before the break (G18) listed among the read-outs; the threshold switch and mapping step worded to match anticipatory economising (a set point in the gap between expected shortfall and reserve, of which a set depletion is the case with nothing expected); the evidence section lists natural tests 11 and 12 and the exploratory applications (bears, migratory birds, heart failure, the reverse-mode exchange) as non-diagnostic.
- **Diagram redrawn** for the current model (theory/figures/tier_queue_diagram_v015.svg and .png); the v0.1 diagram is kept.
- **Maths consolidated** into theory/tier_queue_math_v0.15.md; theory/tier_queue_math_v0.4.md is kept as history.

## Changes in v0.14 (James approved, 5 October 2026)

From a Perplexity exchange on heart failure, brain reserve, coupling and running the model in reverse (raw/2026-10-05_perplexity_heart-failure_brain-reserve_coupling.md; raw/2026-10-05_perplexity_reverse-mode_cardiometabolic.md), with James's decisions (theory/v0.14_pending.md):
1. **A network, not a tree** (Section 1). Dynamic priority sets routing without a strict hierarchy; dependencies can form loops.
2. **Coupling is shared dependency,** not shared classification (Section 3, item 3; mapping step 7).
3. **Using the model in reverse** (Section 5a), with three disciplines (hypothesis generator; correct for visibility; name a set, not a cause).
4. **G18: co-movement before the break,** with the third review's R11 (synchrony) folded in as its consequence.
5. **Price-clustered against dependency-clustered failure,** a distinction reverse mode needs and a test to design (Section 5a).
6. **Evidence rule:** not identified is not absent (Section 7a; CLAUDE.md).
7. **Standing check** against mechanism creep (Section 7a).
8. **Withdrawn before adoption:** "the cost of defence" as a new mechanism. James: defending the record is displacement, reallocation or slowing, already in the model; why it happens is irrelevant. The heart-failure spiral is displacement over a network loop.
9. **Logged, no change:** reserves are stocks; contractile or vascular "reserve" is spare capacity; the brain has almost no fuel stock and is protected through supply priority, redundancy and compensation.

## Changes in v0.13 (James approved, 5 October 2026)

- **Central claim confirmed** (James), with a plainer version for abstracts to come.
- **Anticipatory economising adopted** (James; Claude's derivation from the bear application). G16 rewritten. Predictions AE1 to AE6 committed before the build (theory/v0.13_anticipatory_economising_predictions.md).
- **Engine (computed mode; TQ5 and TQ7 unchanged).** Economising follows the gap between expected remaining shortfall and reserve; a known need can be supplied (`anticipate`), a prior on episode length can be set when mapping (`episode_prior`), and episode length is learned. With nothing expected the rule equals v0.10.
- **Results against AE1 to AE6:**
  - AE1 holds: with the winter's need known, economising starts at onset (step 20; step 57 without) (TQ8 C10);
  - AE2 holds for the reserve (964 of 1100 left at the end, against 605); muscle took no strain either way, so the strain half cannot show;
  - AE3 holds: with long breaks, economising falls burst by burst as their length is learned (0.16, 0.04, 0.02, about 0.01);
  - AE4 does not hold as realised: at the same depletion the slow route showed more economising than the fast (0.30 against 0.18), because the response lags and the slow route has time to catch up; the targets match;
  - AE5 holds: a first open-ended continuous restriction economises far earlier (full economising by 70% depletion, against 0.05 before);
  - AE6 holds: G10 (S3, S3b).
- **A consequence found in the build, adopted as G17: economising and growth compete.** In S1 the first acute pulse now triggers economising (each pulse needs about nine times the reserve), which spares the base so it never reaches the strain growth needs: no growth in S1 (G8 had been reproduced there since v0.4). Across pulse sizes, growth of the base occurs only with economising switched off (TQ8 C11), while economising holds the record (1.0 against 0.55 to 0.75 at the middle sizes). A prior on episode length did not change this: the expected shortfall genuinely exceeds the reserve. G8 gains a condition: growth needs strain without economising.

## Changes in v0.12 (James approved, 5 October 2026)

From the Perplexity review (raw/2026-10-05_perplexity_review_tier-queue.md) and its exploratory applications (bears, migratory birds), with James's decisions (theory/v0.12_pending.md):
1. **Control rule narrowed:** only a necessary, non-bypassable routing bottleneck is priced as a cliff; distributed, redundant or bypassable control is priced like any part (Section 2a; mapping step 5). Engine behaviour for parts mapped as control is unchanged.
2. **Status labels** for every generic prediction (Section 6) and a list of what is fitted (Section 7a).
3. **Engine assumptions** listed (Section 7a).
4. **Numbering:** internal G-numbers keep the gap; a public version would be renumbered with a crosswalk.
5. **Central claim restated** (Section 1): the review's formulation, with the record line and the recovery half added. **Wording for James to confirm.**
6. **Chronic is a state, not a duration** (James): acute, attrition and chronic defined as states (Terms); G8 and G10 reworded; Section 3, item 8.
7. **Structural capacity against deployed throughput:** suppression and remodelling are not compromise (Section 2; Terms).
8. **Value is task-relative,** and the horizon can be the next task's deadline (Section 2a).
9. **State signals are judged against the system's own reference state for its phase** (mapping step 9).
10. "Debt nobody knows about is never repaid" is read as a prediction about unobserved state.

**Not adopted, for James:** anticipatory economising (open questions).

## Changes in v0.11 (James approved, 5 October 2026)

- **Economised demand split into shed and debt** (Section 3, item 4). Each part carries the share of its economised demand that is deferred maintenance (illustrative 0.5 in the engine; to be fixed from sources when mapping).
- **Engine (computed mode; TQ5 and TQ7 unchanged).** Continuous restriction with none, half or all of the economising deferred: lowest reserve 42, 2 and 0 (of 200); reserve back to 95% after 4, 7 and 24 steps; debt cleared after 0, 1 and 20 steps.
- **A fault found and fixed in the build:** economising decayed towards zero without reaching it, adding slivers of debt every step, so episodes never ended and no protection was granted (S1's second pulse lost its protection). Economising now ends below a small tolerance.
- **The opaque trap does not return in S2** with the split: each part repaid its deferred debt from its own slack in the gap between pulses. A first run suggested it had partly returned (second-pulse strain 7.3); that came from the fault above and is withdrawn. The trap would return where deferred debt cannot be repaid before the next load (short gaps, or parts with no slack); open.

## Changes in v0.10 (James approved, 5 October 2026)

- **Not a new principle (James).** The model already had the acute-chronic flip and a threshold switch at a set depletion. The weight-cycling test (natural test 12) found, before this was written, that intermittent restriction gives more weight loss per unit of deficit than continuous restriction in mice; that is supporting evidence. v0.10 makes the economising response explicit as the graded form of the switch (Section 3, item 4). Predictions E1 to E5 were committed before the build (theory/v0.10_economising_predictions.md).
- **Shape (James's question):** an S-curve in depletion (threshold, rise, floor), not a line: a line would have no threshold (contradicting G3) and no floor (contradicting protection of control and fixed capital).
- **Faults found and fixed during the build,** both by principles the model already states: economising first lowered the working parts' apparent value (they looked spare) and lowered the expected shortfall (economising hid the scarcity), which reversed both halves of G10. Value and expected shortfall are now measured against normal demand.
- **Engine (computed mode; TQ5 and TQ7 unchanged).** TQ8 C9, equal total extra demand: continuous restriction economised up to 21% and shed 508 units of working demand; with breaks long enough to refill the reserve, none; with 2-step breaks, up to 14% and 250 units. Economising persisted 12 to 15 steps after the load ended, easing as the reserve refilled. At the same depletion (70%) a slower route showed slightly more economising (0.049 against 0.037) because the response lags by a few steps.
- **Against the predictions:** E3 said short breaks give no advantage; the engine gives a partial one (half the economising).
- **A result that changed: the opaque trap.** In S2 the opaque system no longer traps its base after the first pulse (second-pulse strain 0, against 18 in v0.9): economising cuts the working parts' demand below their capacity, so they recover. Its price is paid as shed commitments, which the record does not see. The v0.4 finding "opaque systems do not get the benefit of an acute challenge" holds only where the system cannot economise; this needs re-examining.
- G10 holds (S3, S3b). C3: the kidney is now strained later (step 26).

## Changes in v0.9 (James approved, 5 October 2026)

From the third review (relayed by James; raw/2026-10-05_claude-chat_review3_astro-econ.md), which tested v0.7 against economics: one severe crisis (Asia 1997) left reserves enlarged for about 15 years, against v0.5's text that a single acute episode raises the reserve "only briefly". James contested the comparison: brief relative to what?
- **The system's clock** (Section 5, step 6): every duration claim is made in units fixed in advance and native to the level being modelled. "Only briefly" now has to name its unit.
- **The reserve is peak-referenced** (Section 2a), as parts became in v0.8: depth sets the size and its persistence, frequency sets the place in the refill order. New prediction G15.
- **Already covered for parts by v0.8:** because protection fades from the peak excess, a larger peak stays protective for longer (duration grows with the log of the peak's excess), matching the muscle durations (2 weeks after low intensity, up to about 24 weeks after maximal).
- **Held (James):** R11 (sharpness of the break depends on how synchronised the buffers' depletion is) and R14 (tests of the horizon need the budget held constant).
- **Engine (computed mode; TQ5 and TQ7 unchanged).** TQ8 C8, same total extra load in three shapes: one severe pulse enlarged the reserve to twice its base, still twice 150 steps later (the size cap binds); four short pulses enlarged it to 1.72 times, 1.30 times 150 steps later; a long mild load within spare capacity left it unchanged. After the severe pulse the reserve still refilled after the working parts. G10 holds in S3 and S3b. The balance between depth and frequency depends on the size cap (twice base) and memory length, both arbitrary.

## Changes in v0.8 (5 October 2026; Claude's call, delegated by James)

James: "I provide the observation, the pattern and some predictions; you translate that into text and formula. Your call."
- **The Felicity read-out adopted** (Section 4), from the muscle check (natural test 11): protection follows the previous peak load (10 maximal contractions protected as well as 45); it is graded (lower-intensity first bouts protected partly against a maximal one); it fades (2 weeks but not 3 for low intensity; up to about 24 weeks for maximal); and a scar lowers the load at which strain appears (previous hamstring strain: two to six times the re-injury risk, higher strain next to the scar). The prediction that strain appears below the previous peak during ordinary recovery failed; the stage had been misassigned, and the scar case checked.
- **Re-tuning is now set by the episode's peak load, not its cumulative strain** (Section 3, item 8; computed mode in the engine). In v0.7 protection grew with peak exposure, which mixes in volume.
- **New prediction G14.**
- **Engine (computed mode only; TQ5 and TQ7 unchanged):** after a recovered episode a part carries demand up to its normal capacity plus the excess it met at the peak without strain; that excess fades with the re-tuning memory; a scar resets it. TQ8 C7 reproduces the muscle pattern: strain onset in a ramped second bout sits at the previous peak after a low-peak first bout, just below it after a high-peak bout 60 steps earlier (fading), at normal capacity with no first bout, and below normal capacity after a scar (ratio 0.69). High-peak first bouts of short and long duration protect about equally. In S1 the base's strain in the second identical pulse falls from 3.42 to 0.91.

## Changes in v0.7 (James approved, 5 October 2026)

From a second review by another Claude chat, relayed by James. Elements adopted from it are recorded as built from it (theory/tier_queue_provenance.md).
- **A. Units and episode length.** The spending cost is $v_i\,s_i\,\min(\tau+h_i,T)$. Building it into the engine exposed two pricing faults, both instances of B:
  - **control** was priced by its own workload and, in long episodes, spent until routing failed. Control is now always at the bottleneck. **Confirmed by James, 5 October 2026** (added during the build);
  - **saturating damage**: long episodes spread load across every part until all failed together. The capacity-at-stake term $s_i$ makes a lost part the fuse. **Confirmed by James, 5 October 2026** (added during the build).
- **B. When marginal-value spending is optimal**, and the three departures (saturation, cliffs, increasing returns). Semelparity needs a short horizon and increasing returns; the v0.6 text is corrected.
- **C. Record dynamics** as a read-out, with the conditional prediction G12. Derived in the maths; the engine cannot show it.
- **D. Two layers.** Predictions and evidence are tagged. The kidney test is layer 1 only; the order, recovery, fuse and re-tuning findings carry layer 2.
- **E. G9 tests follow individuals.** Our re-tuning evidence mostly did; the human link did not; spruce is to check.
- **F. Integral windup** recorded as a rival to the expected-shortfall rule, with a discriminating test (open questions).
- **G. Felicity ratio** held, pending a check of the muscle repeated-bout effect (open questions).
- **Withdrawn: the demand-cut sink** (v0.5, narrowed in v0.6). Under the fuse term, displaced load goes to the part already lost, so a part that cut its demand is never singled out. The v0.5 result came from mispricing parts at their floor.
- **TQ8 rerun:** growth against no growth, both halves of G10, the fasting gut flip, kidney after gut and skin, opacity and the horizon check all hold. Long opaque episodes keep the record (0.95 to 0.99) with the intake as fuse. The episode-length prediction is not reproduced (C6). TQ5 and TQ7 are unchanged.

## Changes in v0.6 (James approved all four, 5 October 2026)

From a review by another Claude chat, relayed by James:
- **Recovery wording.** Recovery needs demand below current capacity, not zero demand. Under the model's own definition of load (the excess, not the work) the old sentence meant the same thing, but the document used "load" in both senses. **Demand** and **load** are now defined in Terms and used consistently.
- **Parameters fixed before predicting.** The free parameter had moved from a fixed rank into the vital weight. Vital weight, rebuild time and restoration cost must now come from independent sources, logged, before an order is predicted (Section 5, step 5).
- **Whose persistence.** The mapping names the level the objective measures (Section 2a; Section 5, step 1). Worker bees, semelparous species and terminal investment become test cases.
- **The remaining horizon** (Section 2a). The v0.5 formula, $p_i=v_i(1+h_i)$ with $h_i$ measured against the horizon, made fixed capital *dearer* to spend as the horizon shortened. That contradicted the text, which said a short horizon values fixed capital less. The text was right: a system cannot go without a part for longer than it has left. The spending cost is now $v_i(1+\min(h_i,T))$.

**TQ8 rerun** (theory/sim/outputs/2026-10-05_TQ8/README.md). TQ5 and TQ7 are unchanged.
- **Held:** growth after coupled acute pulses and none when opaque; both halves of G10; the gut spent first in a fast and rebuilt first at refeeding; the kidney cut after gut and skin; opacity undervaluing a strained part.
- **Improved:** the gut is now spent before skin because it is rebuilt faster. That order no longer rests on the vital weight chosen for skin.
- **New (C5):** with a short horizon, the kidney that cannot be rebuilt loses its protection and is strained first.
- **Revised: the demand-cut sink.** Under the new formula, rebuild time separates renewable parts strongly. In the original S4 the intake is rebuilt fastest, so it is spent first whatever the base does, and the base's demand cut helps in both regimes. When base and intake are equally replaceable (S4b), the v0.5 result returns: under opacity the base that cut its demand becomes the lowest priority and a sink for displaced load, and the record is worse. With signals the cut is roughly neutral. The candidate prediction is narrowed accordingly.

## Changes in v0.5

- **Priority is computed from marginal value** (Section 2a; theory/priority_formula.md). It replaces the fixed priority rule. The maths was worked first, at James's request: if the priority rule could not be written as a formula, the model still had problems. It could, and the formula reproduced every order seen in the natural tests (priority_formula.md, Section 3).
- **The objective is the system's persistence first and its output second, for every system.** The draft formula proposed a declared objective for institutions (stated purpose against operating objective). **That slot is dropped (James, 5 October 2026):** the model is natural-systems first, and it should explain institutions without being reshaped for them. James's view that an institution's stated purpose is not its actual priority is held as speculative. Persistence first is not speculative: it follows from the point that a system cannot do its function if it no longer exists.
- **The reserve's value is the expected shortfall,** learned from experience. It replaces the fixed 30% enlargement after chronic episodes.
- **Opacity acts as signal gain** on the value control sees, and a sustained signal loses gain (adaptation).
- **Built into the engine** as `priority="computed"`. The fixed-priority engine stays the default, and TQ5 and TQ7 are unchanged. TQ8 checks:
  - growth after coupled acute pulses, and none when opaque: reproduced;
  - G10, both halves: reproduced. The definition of a shortfall was chosen while checking this, so it is reproduced, not predicted (TQ8 README, fix 4);
  - the gut flip in fasting and the kidney-after-gut order: emerge from value;
  - opacity: control values a strained part at 0.41 while it carries 138% of capacity.
- **A new result, not built in (TQ8, S4):** whether a part that cuts its own demand helps the system depends on signal gain. With signals it helps (the spruce pattern). Without them the part looks spare, its priority falls to the lowest, and displaced load is routed onto it. (Narrowed in v0.6: it holds among parts that are equally replaceable.)

## Changes in v0.4

- **Rule R for the record** (natural_test_record_rule.md): only a held output behaves as a flat record. This resolved the muscle mismatch, where performance had been measured with capacity tests. It sorted five paired cases without a break: submaximal force against EMG and maximal force; hearing thresholds against synapse counts; visual field against nerve-fibre thickness; glucose against insulin; T4 against TSH. All five were known in outline.
- **G11 withdrawn (James, 5 October 2026).** It adds no mechanism. A compensating part carries load passed to it, so its output rises while it copes and falls when it is compromised. That already follows from the existing rules. It is kept only as a reading note in Section 4.

## Changes in v0.3

- **Recovery order depends on the type of past load.** This was formed after the growth-restriction result, then checked on three cases it was not built from: adults after long-term undernutrition, growth-restricted lambs and piglets, and food-limited migrating sparrows. All three fitted (natural_test_recovery_order.md; surface level, one case contaminated).
- **Speed separated from order,** with the intake's double advantage.
- **A rule not yet found: the next demand.** When a system builds without prior deprivation, it builds for what is coming (ground squirrels multiply their fat before hibernation; warblers fuel for the next leg). The gut's history suggests a form for it (theorising): **a part's priority follows its value to the system's current bottleneck.** The gut is spent when there is nothing to absorb (low value) and rebuilt first when food returns (it becomes the bottleneck). Fat is built ahead of a known fast. This would unify state-dependent priority, role reassignment and the next demand. To test.
- **New generic prediction** G10.

## Changes from v0.1 to v0.2

- **Scars can cut demand as well as capacity.** From the plant check: spruce leaf area was down 60% after drought and still 30% down four years later, and the trees coped better with the next drought. The explanation was named, then checked.
- **Four recovery outcomes** (growth, re-tuning, scar, loss), with their conditions. This includes the acute-chronic flip, from James (5 October 2026): resilience exists in too many places to leave out. Muscle growing after hard work is a healthy, coupled system adding capacity. The leaf cut is short-term adaptation from experience, like a vaccine.
- **New generic predictions** G8 and G9.

## Open questions answered or withdrawn (moved from the model document at v0.15)

- ~~How does priority combine vital, irreplaceable and redundant?~~ Answered in v0.5: vital and redundancy combine in the marginal value, and irreplaceability scales it in the spending order.
- ~~Does priority follow value to the current bottleneck?~~ Adopted in v0.5. What would still distinguish it from fixed priority plus role reassignment in data: order among parts that are not bottlenecks should be set by replaceability alone.
- ~~The demand-cut sink.~~ Withdrawn in v0.7 (an artefact of mispricing parts at their floor).
- ~~Where economised demand lands.~~ Split into shed and debt in v0.11. Open: what share is deferred in each natural system (a mapping value to fix from sources).
- ~~Anticipatory economising.~~ Adopted in v0.13.
- ~~Synchrony (R11).~~ Folded into G18 (v0.14) as a consequence of shared dependency. **Horizon against budget (R14)** still held.
- ~~Felicity ratio.~~ Adopted in v0.8 as the Felicity read-out (Section 4). Repeated loading during ordinary recovery adds no damage because the load does not exceed the raised no-strain ceiling (James, 5 October 2026): the model already says this. What remains open is below the model's level: **how** a part raises its ceiling within days while its maximal force is still reduced. The same load damaged the muscle the first time, so the ceiling that governs strain is not maximal force (consistent with rule R: maximal force is a state signal). Candidate mechanisms (loss of the most susceptible fibres, a fuse inside the part; neural or connective-tissue adaptation) are not the model's to choose.
