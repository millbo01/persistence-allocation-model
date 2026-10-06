# The tier-queue model, v0.17 (DRAFT for James, 6 October 2026)

**Status:** working model (phase 3).

**Draft, not yet canonical.** theory/TIER_QUEUE_MODEL_v0.16.md remains the reference until James approves this version.

**What v0.17 is.**
- **Simplification, not expansion.** v0.17 removes things: parts lose their demand and their condition, and the governor becomes a separate allocator. Every decision is recorded with James's wording in theory/v0.17_pending.md.
- **The reference implementation** is theory/sim/tq_units.py (frozen after TQ13b).
- **The v0.16 maths and engines** are kept for the results they produced.

**After approval, the vocabulary is frozen.** No new mechanism enters unless an existing mapping fails a pre-committed test (the standing check, Section 10).

## Changes from v0.16

| No. | Change | Source |
|---|---|---|
| 1 | **The governor is a separate, parallel system, and it only allocates.** It holds the levels persistence depends on ("maintain X, Y, Z") by sharing out resources. It sets no work targets. It is a function, not always an organ | James; repair and allocation scan |
| 2 | **Parts have no demand.** A part works to the limit of the resources it is given, set by the scarcest one it needs (law of the minimum). "Demand" is the name for reallocating resources to hold the governor's levels | James |
| 3 | **Several resources, each with its stores** (more than one per resource allowed: a fast store and a slow one), released, refilled and spilled by the governor. Some resources cannot be spilled and are held by controlling intake | James; scan; TQ12, TQ13b |
| 4 | **A part's only state is its units:** active, switched off, or lost; some lost units scarred. Condition, dose and the consolidation floor are removed | James; TQ13 |
| 5 | **Three outcomes, kept apart.** Switched off: comes back quickly, not harm. Lost: rebuilt over the rebuild time, delayed recovery, not harm. **Scar:** damage to the template, the only real harm | James |
| 6 | **Harm comes only when supply falls faster than a part can scale down.** Otherwise units are switched off in an orderly way: consolidation, like switching servers off | James; TQ13 |
| 7 | **Template damage:** disorderly loss in an episode past a limit set for each part when mapping | James (option 1) |
| 8 | **Inside a part,** basal maintenance is paid first. Renewal keeps a fixed share of the rest, and is cut first when supply falls below basal plus that share. Work never stops for repair | James; TQ12b |
| 9 | **Repair is local and governed by supply:** the part repairs itself from what reaches it, and the governor decides what reaches it | Scan; James |
| 10 | **Parts do not die; the system dies,** when load reaches the top (the exhaustion cascade) or a non-bypassable link is cut (severance) | James |
| 11 | **The intake rule.** What is upstream of X is maintained at all costs. The intake's maintenance is support at all times; its work only while it has something to take in | James; TQ11b, TQ13 |
| 12 | **Economising** is the governor's anticipation: an even cut, made early, that preserves the stores. It is not what prevents damage (the allocation order already does that) | James; TQ11 |
| 13 | **Protective slowing** is the governor's choice, not a part's | James |
| 14 | **Carried from v0.16 but not needed by any engine result so far:** computed marginal value, the horizon, signal gain, labelled refusal, peak protection, growth, reserve memory. They are kept, flagged, each with its own untested prediction (Section 9) | TQ11 parsimony check |
| 15 | **Open questions are tiered:** model-threatening, refining, niche | Perplexity check |
| 16 | **Section 1 is unchanged** (James's wording); a proposed rewording follows it | |

## 1. The principle

**Central claim** (v0.16, unchanged; James's wording):

> In a goal-directed system with finite-capacity parts and limited reserves, load is routed according to each part's current marginal value to the persistence of the level being protected, judged against the next task that persistence depends on. The system holds its routine output steady by drawing reserves, taking resources from lower-value or expendable parts, which absorb the load, lowering demand and capacity where it can, or exporting it. So the record sees compromise, not stress: it moves only when the buffers, sacrificial parts and routing capacity can no longer absorb the demand. Recovery runs the other way. It begins once demand falls back within current capacity and supply flows again, rebuilds the intake and the capacity the next task needs first, and refills reserves according to how scarce the system has learned its world to be. Load without enough slack to restore what the next task needs makes the system chronic: that state, not the passage of time, permits deterioration, and deterioration becomes a scar only when it destroys what rebuilds a part.

> **Proposed rewording for v0.17** (for James to choose, reword or reject):
>
> In a goal-directed system, a governor holds the levels its persistence depends on by allocating finite resources among parts that have no demand of their own: each part works to the limit of the scarcest resource it is given. When supply falls short, the governor draws its stores and then takes resources from lower-ranked parts, which switch units off. The routine output, the record, holds until nothing more can be taken: the record sees compromise, not stress. Load is relocated, never removed: it ends in switched-off or lost units, drawn stores, or across the boundary. A part scales down without harm when supply falls no faster than it can switch units off; units are lost when supply falls faster; the part is scarred only when those losses destroy what rebuilds it. Recovery runs the other way: the intake first, then parts and stores in order of value, with stores first when the system has learned its world is scarce. Parts do not die; the system dies, when load reaches the top or a non-bypassable link is cut.

## 2. The components

**The governor.**
- **What it is:** a separate, parallel system that holds the levels persistence depends on: the top level X (the record), and the levels X depends on (Y, Z: stores, supply to dependants).
- **What it does:** only allocates. It releases, stores and spills resources, and shares them among parts.
- **Where it sits:** it may be an organ (the liver's control of iron supply), several organs, or distributed among the parts (a plant's sugar signalling; a colony's foragers reading local cues). It is a function, not a place.
- **Who it serves:** it trumps any part.

**Working parts.**
- **What they are:** simple processors. A part does the work only it can do, and has no demand.
- **How much they work:** to the limit of the resources given, set by the scarcest one they need.
- **Units:** a part is made of units (cells, nephrons, servers). Units that duplicate each other, share resources and balance load are one part; units in series are separate parts.
- **Unit states:** **active**, **switched off** (coasting on minimal maintenance) or **lost**. Lost units can be rebuilt unless **scarred** (template gone).
- **Capacity** is active units, scaled by any dependency on another part's delivered output.

**Special roles.**
- **The intake** brings resources in. What is upstream of X is maintained at all costs: its maintenance is support at all times, its work only while it has something to take in.
- **Non-bypassable links** (central control, transporters, links in series) break the system when cut.

**Resources and stores.**
- **Several resources.** Work, maintenance and renewal each need their own set of resources, in fixed ratio.
- **Stores.** Each resource has one or more stores, drawn in order and refilled in order. Each has its own release rate, which can taper as it empties (the knee).
- **Spill.** The governor spills a resource it does not need once its stores are full. A resource that cannot be spilled (iron) is held by limiting intake.
- **A store is not a part:** it does no work.

## 3. What the governor does

1. **Allocation order** (each resource, each step):
   1. the top's full need;
   2. support parts' full allocation (parts the top depends on, and the intake's maintenance);
   3. every other part's basal maintenance, by rank;
   4. every other part's allocation for work and renewal, by rank;
   5. **from surplus only:** reactivating and rebuilding parts by rank, against refilling the stores at their value (the expected shortfall).

   **When supply falls short,** the governor draws its stores (each up to its release rate), then lower-ranked parts lose supply first. That is "resources taken from lower-priority parts".
2. **Rank, and the open question about priority.**
   - **v0.16's claim:** priority is computed from each part's current marginal value to persistence.
   - **What the engine shows:** everything tested so far is reproduced by ranks fixed when mapping, plus two things:
     - the intake rule;
     - one dynamic quantity, the stores' value. That value is the expected shortfall, learned from how often supply has fallen short.
   - **The challenge:** whether dynamic priority adds anything beyond fixed rank plus role reassignment is the central open question (Tier 1). The claim is kept, flagged, until a test discriminates.
3. **Economising.** When the shortfall still expected outruns the stores, the governor cuts other parts' allocations early and evenly. Their units switch off in an orderly way and the stores are preserved. With a known need (a predictable season), it starts at onset.
4. **The switch,** and governors as modes (open; Section 11): signals from outside (day length, temperature, sight, smell) may select a different governor that overrides the routine one.

## 4. What a part does with what it receives

1. **Basal maintenance first.** Basal maintenance keeps the part's units in existence: active and switched-off units both need it.
2. **Then work and renewal.** Renewal keeps a fixed share of what is left. When supply falls below basal plus that share, renewal's share is cut faster than work's: the repair buffer is cut first. Work never stops for repair.
3. **Work** = min(active capacity, the work allocation of each required resource ÷ its requirement). What it cannot use goes back to the governor.
4. **Units change only through supply:**

   | What is short | What happens | Kind |
   |---|---|---|
   | Renewal | Units that cannot be renewed are switched off, up to the part's switch-off rate. The rest fail and are lost | Switched off: orderly. Lost: disorderly |
   | Basal maintenance | Units that cannot be kept in existence are lost | Lost |
   | Work (more units active than the supported work needs) | Units are switched off: consolidation | Switched off |
   | Nothing (supply returns) | Switched-off units are reactivated quickly, at a cost; lost units are rebuilt over the rebuild time, unless scarred | Coming back |
5. **Scar.** If units lost in disorder in one episode exceed the part's template limit, the excess is scarred and never returns. Fixed capital has no rebuild, so any loss is kept.

## 5. How load moves, and how systems fail

- **Load is relocated, never removed.** When supply falls short, load ends as drawn stores, switched-off units in lower parts, lost units, or load leaving across the boundary.
- **Load backs up a dependency:** a part limited by throughput leaves work undone, and parts depending on its output lose capacity (supply edges; loops).
- **Coupling is shared dependency.** Parts sharing an input, a stressor, a store or repair machinery move together (G18).
- **The death cascade (exhaustion).** Parts switch off in ascending rank, then lose units in ascending rank. The top loses its last units last: system death.
- **Severance.** Cutting a non-bypassable link breaks the record while stores are full and other parts are funded.
- **Recovery runs the other way.**
  - The intake comes first.
  - Parts and stores then compete for surplus by value.
  - After a short episode (low expected shortfall), parts come back first. After a long one, the stores do.

## 6. Read-outs

- **The record:** the top's work ÷ X. It is flat while load is absorbed below, and moves when nothing more can be taken.
- **Record dynamics** (G12): with a store whose release tapers, recovery from small knocks slows before the break.
- **State signals:** active, switched-off and lost units per part; store levels.
- **Co-movement** (G18): parts sharing a loaded dependency move together before the break.
- **The three outcomes,** told apart by what comes back and how fast:

  | Outcome | Comes back | How |
  |---|---|---|
  | Switched off | Fully, within a few steps | Reactivation |
  | Lost | Fully, over the rebuild time | Rebuilding |
  | Scar | Never | Ceiling lowered |
- **The ledger:** supply in plus stores drawn = work done + maintenance and renewal + reactivation and rebuilding + stores refilled + spill.
- **Carried from v0.16, not re-examined:** the Felicity read-out (protection set by peak load); reading a compensating part's output.

## 7. Mapping a system

Do this before opening any outcome data.

1. **Boundary, currency and objective.** Name the system, its boundary and the level whose persistence is protected. Fix all three before outcomes are seen: they are the model's main safeguards.
2. **Resources and stores.** Which resources does work need, in what ratio? Which stores exist for each, in what order, with what release? Which can be spilled?
3. **The governor and its levels.** What is X (the record)? What levels does X depend on? Where does the governor sit: an organ, several, or distributed?
4. **Parts.** For each part:
   - its units and capacity;
   - its rank;
   - its rebuild time and template limit (fixed capital: none);
   - its requirements per unit of work, basal maintenance and renewal;
   - whether it is support for the top;
   - whether it is the intake.

   Fix these from independent sources. Anything chosen with the expected outcome in mind is declared fitted.
5. **Links.** Dependencies (supply edges), loops, and non-bypassable links (severance points).
6. **The clock.** Fix the unit in which durations are judged.
7. **Predictions.** Write the generic predictions (Section 9) for this system before looking at outcomes.

## 8. Using the model in reverse

Unchanged from v0.16, Section 7.
- Reverse mode starts from what is seen failing and points to where load entered, which parts were absorbing it unseen, and which dependency the failing parts share. It suggests where to look; it never names a cause.
- **Disciplines:** it is a hypothesis generator, not evidence; correct for visibility; name a set, not a cause.
- It must distinguish price-clustered from dependency-clustered failure.

## 9. Generic predictions

**Layers:** layer 1 holds for any finite-stock feedback loop; layer 2 needs selection or design.

**Status reflects v0.17 engine results:** TQ11 to TQ13b, theory/sim/outputs/. None is tested against held-out data yet.

| No. | Prediction | Layer | Status |
|---|---|---|---|
| G1 | The record stays near normal while lower parts and stores move | 1 | Natural observation: consistent; simulation result (TQ13) |
| G2 | Lower-ranked parts lose supply first, in ascending rank | 2 | Natural observation: consistent; simulation result (TQ13) |
| G3 | With a store carrying the gap, the break comes at the same cumulative shortfall whatever the rate | 1 | Simulation result (built in); stress-test candidate (H1) |
| G4 | A larger store gives a longer silence; a depleted start breaks sooner | 1 | Natural observation: consistent |
| G5 | Parts absorbing load lose units (switched off first, lost if supply falls too fast), so loss compounds down the ranks | 1 | Simulation result (TQ13) |
| G6 | Recovery starts with the intake; the record recovers before the state does | 2 | Natural observation: consistent (kidney); simulation result (TQ11b, TQ13) |
| G7 | Fixed capital keeps what it loses; renewable parts rebuild lost units, except where the template is scarred | 1 | Natural observation: consistent; simulation result (TQ13) |
| G8 | **Rate decides harm.** Supply falling no faster than a part can switch units off leaves no loss. Faster falls lose units (delayed recovery). Losses past the template limit scar | 1 | Simulation result (TQ13 O1, O4); compatible: scan (supply cut suddenly to heart muscle against gradual atrophy); untested |
| G9 | A system re-tuned to a past threat does better against it again, and may do worse if conditions change | 2 | Carried from v0.16 (not re-examined) |
| G10 | After a short episode, parts come back before stores; after a long one, stores come first | 2 | Natural observation: consistent; simulation result (TQ11d, TQ13) |
| G12 | With a tapering store, recovery from small knocks slows before the break; with full release until a switch, no warning | 1 | Simulation result (TQ9 to TQ11); blood-loss contamination declared; stress-test candidate (H1, VitalDB) |
| G13 | Lowest-ranked parts take the load first and longest (the fuse) | 2 | Simulation result (TQ13 cascade) |
| G14 | Peak-referenced protection (the Felicity read-out) | 2 | Carried from v0.16 (not re-examined; not in the v0.17 engine) |
| G15 | Store memory: a deeper shortfall leaves larger stores for longer | 2 | Carried from v0.16 (not in the v0.17 engine) |
| G16 | **Economising:** with an expected shortfall, the governor cuts allocations early and evenly; units switch off in an orderly way; stores are preserved | 2 | Simulation result (TQ11, TQ13 O4); compatible: hibernation, remodelling |
| G17 | Economising and growth compete | 2 | Carried from v0.16 (growth not in the v0.17 engine) |
| G18 | Parts sharing a loaded dependency co-move before the break; parts clustered only by rank do not | 1 and 2 | Simulation result (TQ9 to TQ11); untested |
| G19 | **Three outcomes** (switched off, lost, scar) are distinguishable by what comes back and how fast | 1 | Simulation result (TQ13 O4); untested |
| G20 | **Exhaustion and severance.** No part loses units while there is somewhere else to take resources from. The top goes last. Failure with willing receivers intact means a non-bypassable link was cut | 1 | Simulation result (TQ13 O2, TQ11 M4); untested |
| G21 | **The law of the minimum.** A part's work falls in proportion to its scarcest resource while other resources are ample; their unused share is returned and spilled | 1 | Simulation result (TQ12, TQ13); known (Liebig) |
| G22 | **The intake coasts.** With nothing to take in, the intake switches its units off on minimal maintenance and is back first at refeeding, whatever its rank | 2 | Simulation result (TQ13); compatible: python gut, migrating birds |

## 10. Status, evidence and working rules

- **Evidence so far:**
  - natural surface tests 1 to 12;
  - definition checks (framing crosscheck; deterioration and scar scan; repair and allocation scan);
  - simulations TQ1 to TQ13b;
  - exploratory applications.
  - **No held-out data test yet.** Weights are as stated in v0.16, Section 9.
- **The reference implementation:** theory/sim/tq_units.py (frozen).
- **Its constants are engine-level and illustrative,** not universal levels (James): switch-off and reactivation rates, failure rate, reactivation and rebuild costs, the default template limit.
- **Open engine questions from TQ13b** (Tier 2):
  - (a) should every part's basal maintenance come before support parts' work?
  - (b) should units starved of basal maintenance be lost at a rate rather than at once?
- **Status labels, the fitted list, the evidence rule** ("not identified is not absent") and **the standing check:** as v0.16.
- **The standing check is strengthened (Perplexity):** before adding any rule, attempt a complete mapping with the existing parts, resources, stores, ranks, links, boundary, objective and clock. Add a mechanism only after a confirmed qualitative failure in a pre-committed test.

## 11. Open questions, tiered

**Tier 1: could threaten the model.**
- **Fixed against dynamic priority.** Does dynamic priority do better than fixed rank plus role reassignment? Discriminating test (Perplexity): change the expected next task while holding the parts and recent losses constant.
- **Independence of inputs.** Can ranks, requirements, rebuild times and template limits be fixed independently of the outcome?
- **Out-of-sample prediction.** Does the model predict a new system's order of loss and recovery without fitting it?
- **The three outcomes in held-out data.** Are switched off, lost and scarred distinguishable there?
- **G18 in data.** Do dependency-clustered parts co-move before failure?
- **Sensitivity to framing.** Does the model fail when the boundary or objective is changed?

**Tier 2: refining a surviving model.**
- the TQ13b engine questions (a) and (b);
- what sets a store's release profile (a knee or a full release until a switch);
- what starts anticipatory economising;
- how the expected shortfall is learned;
- what sets a part's template limit;
- harmful inputs (raising the renewal a part needs, as wear does);
- governors as modes selected by signals, and whether rarity sets which wins: the same event should move from override to routine as it becomes frequent;
- the carried v0.16 mechanisms (horizon, signal gain, labelled refusal, peak protection, growth, reserve memory): which predictions need them?

**Tier 3: niche or application.**
- the boundary between labelled and unlabelled load;
- objectives at two levels (mother and fetus);
- whether a dependant's need falls with its supplier's economising;
- institutions growing or re-tuning.

**For the novelty stage:**
- "no demand, only maintained levels" (James) against cascade control and perceptual control theory;
- renewal cut before productive work, against Dynamic Energy Budget theory, which pays maintenance first. DEB theory must be read in full first.

## 12. Way forward (agreed 6 October 2026)

1. **Approve v0.17** (with or without the proposed Section 1 rewording) and freeze the vocabulary.
2. **One pre-registered held-out test:** VitalDB first (blood loss; G1, G3, G12), the anaesthetist mapped as an outside defending loop.
3. **Design the fixed-against-dynamic priority test.**
4. **The model paper, then a preprint.** Before writing, read DEB theory and the nearest work (cascade control, perceptual control theory, allostasis, resilience engineering) to state what is new.

## 13. Terms

- **Governor:** the separate system that holds the levels persistence depends on, by allocation only.
- **Part:** a working part (including intake and control), made of units; it has no demand.
- **Unit states:** active, switched off, lost, scarred.
- **Store:** a stock of one resource, drawn and refilled in order with others of its kind; it does no work.
- **Load:** what the governor cannot fund where it is needed. It ends as drawn stores, switched-off or lost units, or load leaving across the boundary.
- **Switched off:** units coasting on minimal maintenance; they come back quickly; not harm.
- **Lost:** units starved before they could be switched off; rebuilt over the rebuild time; delayed recovery, not harm.
- **Scar:** template damage, from disorderly loss past the part's limit; the only real harm.
- **Economising:** the governor's early, even cut in allocations when shortfall is expected.
- **Exhaustion and severance:** the two routes to system death.
- **Chronic (a state):** a sustained shortfall in which units cannot be kept, renewed or brought back before the next one.
