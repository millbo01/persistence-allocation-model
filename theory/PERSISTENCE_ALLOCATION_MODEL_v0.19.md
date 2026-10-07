# The Persistence Allocation Model, v0.19 (consolidation, 7 October 2026)

**Status:** working model (phase 3). **Consolidation draft for James's approval.** It becomes the canonical state when James approves it; until then v0.18 stands.

**What v0.19 is:** v0.18 with every dated correction and amendment of 6 and 7 October 2026 folded into the text, the two items approved for v0.19 applied, and the sections v0.18 took "as v0.17" written out in full. **Nothing new enters.** Every change from v0.18's wording is listed in the consolidation notes at the end, with its source, so it can be checked.

**The vocabulary is frozen** (as v0.18). The terms added by approved decisions (wear, throttled, steal, capture basin) are in Section 14.

**Rules carried forward:**
- The probing phase is over.
- **The standing check:** no new mechanism enters unless an existing mapping fails a pre-committed test (Section 10).

**References:**
- **History:** theory/tier_queue_changelog.md.
- **Previous canonical state:** theory/PERSISTENCE_ALLOCATION_MODEL_v0.18.md (kept as the record; v0.17 and earlier likewise).
- **The maths:** theory/PAM_math_v0.18.md (restatement with the DEB imports and the wear term restored).
- **Derived propositions:** theory/PAM_propositions_DRAFT.md (P1 to P18, checked numerically by scripts/pam_propositions_check.py). They supersede theory/PAM_results_v0.18.md for the paper.
- **Recovery and viability:** theory/PAM_recovery_value_and_viability.md.
- **The reference implementation:** theory/sim/tq_units.py (frozen; a reduced form; its departures are listed in Section 11).
- **The diagram** is not yet updated.

## Changes from v0.18 (all approved by James, 6 and 7 October 2026)

| No. | Change | Source |
|---|---|---|
| 1 | **Access-limited load and "chronic".** The central claim covers shortfall from supply, requirement **or access**. Three origins of load, with a guard: an access restriction counts only for a mode and gate documented independently. "Chronic" is restoration persistently failing to keep pace with deterioration (the backlog equation) | Correction, 7 October (PAM_proposals_7Oct_access-limited-load.md) |
| 2 | **Collapse and death by viability theory.** The system collapses when load reaches the top or a non-bypassable link is cut, and dies only when no route back remains | Amendment, 7 October |
| 3 | **Recovery by marginal value** (inventory theory). The stores' value is renamed **the expected frequency of shortfall** | Amendment and correction, 7 October |
| 4 | **Bundles under joint scarcity;** pathway capacity as **maximum flow;** the complementarity check in mapping | Correction from the literature map, 7 October |
| 5 | **Resources are drawn from a flow;** nothing is returned. **Exported load is residue,** not a resource term | Correction from the maths, 7 October |
| 6 | **Four forms from DEB:** store release proportional to content (the default); spill with a recovery fraction; unpaid upkeep paid from the part's own units (shrinking); synthesising-unit kinetics as the general law of the minimum | Maths amendment, 7 October |
| 7 | **Renewal is a baseline per active unit plus wear per unit of work** (the engine form since TQ11, restored to the maths) | Correction, 7 October (James) |
| 8 | **Economising is a magnitude;** consolidation is its default realisation; **switched off defined** | Approved for v0.19, 7 October |
| 9 | **Sequential records; mode held constant in a test of dynamic priority; repair capacity as a state** | Amendment from probes P10 to P12, 7 October |
| 10 | **Predictions given their derived forms:** G3, G12, G13, G16, G20, G23(b), G24, G26; new read-outs (two thresholds, time of crisis, cost of restoration) | Amendments from the derived results and propositions, 7 October |
| 11 | **Derived result beside the principle:** total unmet load is invariant under access settings at fixed supply, stores and outside input | Propositions P1, 7 October |
| 12 | **Rank from affinity** as a mapping rule | Propositions P17, 7 October |
| 13 | **Drain against capture** as the extension's first test | Propositions P18, 7 October |
| 14 | **Results of H1 and PT1 recorded** | 7 October |

## 1. The principle

**Central claim** (unchanged from v0.18 as corrected and amended on 7 October 2026):

> In a system that regulates its own persistence, a governor holds the levels its persistence depends on by regulating access to finite shared resources among parts that have no demand of their own; the allocation among parts is the resulting flow. Each part works to the limit of the scarcest resource that reaches it. When what reaches a part falls short of what the reference state requires, whether supply falls, requirement rises or access is restricted, the governor draws its stores, and lower-ranked parts lose access first and switch units off. The routine output, the record, holds until nothing more can be taken: the record sees compromise, not stress. Load is relocated, never removed: the resource gap is met from stores, met from outside the boundary, or left unmet at a named part, and unmet load leaves its residue in switched-off, lost or scarred units, or in work not done, which may land across the boundary. A part scales down without harm when supply falls no faster than it can switch units off; units are lost when supply falls faster; the part is scarred only when those losses destroy what rebuilds it. Repair is its own network, governed like any part: under a sustained shortfall it loses access and lost units wait. Recovery runs the other way: the intake first, then parts and stores in order of value, with stores first when the system has learned its world is scarce. A part dies only when its route back is cut; the system collapses when load reaches the top or a non-bypassable link is cut, and dies only when no route back remains.

**Derived result** (propositions P1). At fixed supply, store draw and resource from outside, **the total unmet load is the same under every access setting**: every order, every phase, every gate the governor sets. Access decides only where load lands.
- Total load falls only by raising supply, drawing the stores harder (which needs release headroom), or bringing resource in from outside.
- An intervention that restores one part's supply without adding resource moves the same amount of load onto other parts.
- This is an identity of the model, not an empirical claim; the empirical content is where the load lands.

## 2. Scope

1. **Persistence is a viability constraint.**
   - The governor keeps the system within the states compatible with its continued existence. Within that envelope, the system pursues its purposes.
   - When purpose and viability conflict, the purpose can become a recipient of load: an institution cannot pursue its purpose if it does not survive.
   - The model describes the dynamics while persistence is being governed. It does not claim a system cannot choose to dissolve.
2. **Terminal reproductive programmes are out of scope.**
   - **Examples:** semelparous salmon, males of some dasyurid marsupials (Antechinus), monocarpic plants. In these, individual persistence stops being the protected constraint.
   - **Prediction:** the model works before the reproductive switch and fails systematically after it.
   - **A counterexample** would be an ordinary, non-semelparous system, in ordinary conditions, whose own regulation destroys recoverable viability with no higher-level system being protected. That would count against the model.
3. **The model is not a theory of action selection.**
   - Behaviour that risks death (a parent shielding a child) is a different control problem.
   - Meanwhile the internal regulation goes on preserving the body.
4. **No redrawing after a counterexample.**
   - The boundary, the protected level and the classification of components are fixed at mapping (Section 8).
   - Changing them after an outcome is seen is a fitted change, declared as such.

## 3. The components

**The governor.**
- **What it is:** the function that holds the levels persistence depends on: the top level X (the record), and the levels X depends on (Y, Z: stores, supply to dependants).
- **What it does:** it **regulates access** to resources, through:
  - releasing, filling and spilling stores;
  - opening and closing intake;
  - setting the capacity of pathways and gates (vascular tone; connection; transporters);
  - mobilising repair (giving the repair network access).

  **It does not switch units directly.** Units switch off or come back when the flow that reaches them crosses their local thresholds (Section 5).

  **The realised allocation is the resulting flow,** set by the network and the state of the parts. **Explicit allocation** (a budget line, a rota) is one way of setting access; it is not excluded.
- **How it acts:** largely by broadcast. A signal reaches many parts and pathways, and each responds by rules encoded locally: its receptors, local metabolites, its own autoregulation. The same sympathetic signal constricts gut and kidney beds strongly, while the brain's autoregulation and the heart's local metabolic control hold their own flow.
- **Where it sits:** it may be an organ, several organs, or distributed (sensors, signals and gates throughout the system). **A signal produced inside a part belongs to the governor function.** It is a function, not a place. (So two regulators that can each take control, such as the brain and the immune system, are **two modes of one governor function**, not two governors.)
- **Who it serves:** it trumps any part. It sets no work targets.

**Formally:**
- **The governor:** access parameters g(t) = G(sensed state, environment).
- **Each part's allocation:** aᵢ(t) = Φᵢ(resources, network, g(t), sᵢ(t)).
- **Each part's next state:** sᵢ(t+1) = Fᵢ(sᵢ(t), aᵢ(t)).
- **Nothing more:** a part has no utility, claim or bargaining.

**Working parts.**
- **What they are:** simple processors. A part does the work only it can do. **It has no demand of its own:** it may emit signals, but signalling belongs to the governor function.
- **How much they work:** to the limit of the resources that reach them, set by the scarcest one they need.
- **Units:** a part is made of units (cells, nephrons, servers). Units that duplicate each other, share resources and balance load are one part; units in series are separate parts.
- **Unit states:**
  - **active;**
  - **switched off:** the unit keeps its route back, receives basal maintenance only, and does little or no work. Cellular quiescence is an instance;
  - **lost:** the unit is gone, but can be rebuilt by the repair network;
  - **scarred:** lost with its template, so it never returns.
- **Capacity** is active units, scaled by any dependency on another part's delivered output.
- **Part death:** a part at zero capacity whose route back is intact is not dead. **It dies when its route back is severed:** the template, the repair source or the reconnection. Fixed capital has no route back.
- **Temporary parts:** a part may appear for a period and take a rank when it does (the placenta in pregnancy).

**Special roles.**
- **The intake** brings resources in. What is upstream of X is maintained at all costs: its maintenance is support at all times, its work only while it has something to take in.
- **Non-bypassable links** (central control, transporters, links in series) break the system when their capacity falls to zero.

**The repair network.**
- **What it is:** the repair workforce, a set of working parts whose work is renewing other parts' active units and rebuilding their lost units.
- **Where it works:**
  - **resident** where local cells do the work;
  - **mobile** where it is supplied centrally and reaches damage through the network. Leukocytes circulate and are captured where local signals have changed the vessel wall; nothing dispatches them to an address.
- **What it needs:** its own resources and stores. One missing resource stops it everywhere (scurvy).
- **How it is governed:** like any part. Its capacity is shared, so the parts it serves are coupled through it, **served strictly by rank** (G23 b).
- **Under stress:**
  - **sustained shortfall:** it loses access, so healing slows even where the damaged part's own supply is ample;
  - **acute threat:** it is moved towards likely sites of damage.
- **Its capacity is itself a state:** primed by acute load that is recovered from, reduced by sustained shortfall, impaired by damage to its niche or supply, and shared across sites through common support.
- **Renewal has two parts:** a **baseline per active unit** (turnover whether or not the unit works) and **wear per unit of work done** (usage). Cutting work cuts the wear part at once; the baseline falls only as units are switched off.

**Resources, carriers and stores.**
- **Several resources.** Work, maintenance and renewal each need their own set of resources, in fixed ratio where they are complementary.
- **Resources are a flow.** Each part draws from the flow what its access allows and its work can use. What it does not draw stays in the flow for the parts after it; what no part draws goes to the stores or is spilled. **Nothing is handed out and nothing is returned.**
- **Carriers are not resources.** A carrier (blood, a power line, a supply chain) is part of the network. It is a resource only where its own stock is what is short (blood volume in haemorrhage).
- **Stores.** Each resource has one or more stores, drawn in order and refilled in order. **Release is proportional to content by default** (DEB), so a store releases less as it empties. **Full release until empty** is the alternative profile; which profile a store has may depend on the governor's mode, and is fixed at mapping. The engine uses a knee between the two.
- **Spill.** Of the flow left undrawn, a share (the recovery fraction) refills the stores and the rest is spilled, so a resource in excess cannot accumulate without bound. A resource that cannot be spilled (iron) is held by limiting intake.
- **A store is not a part:** it does no work.

**Damage.** Trauma, toxins and pathogens enter from outside as a loss of units or of pathway capacity. The model then handles the resource consequences (repair, load, access). It contains no damage mechanism.

## 4. What the governor does

1. **The order of access** (each resource, each step). In the reduced form, the network's outcome is written as an ordered draw from the flow:
   1. the top's full need;
   2. **every part's basal maintenance,** by rank. Existence comes before anyone's work;
   3. support parts' work and renewal (parts the top depends on; the intake while it has something to take in);
   4. every other part's work and renewal, by rank, **with the repair network ranked among them,** cut by economising on work;
   5. **from what is left in the flow:** reactivation, and the repair network's added draw for rebuilding when the governor raises its access in recovery, against refilling the stores, by **marginal value** (item 5).

   - **When supply falls short,** stores are drawn (each up to its release), then lower-ranked parts lose access first.
   - **Where the network is known,** it replaces the ordered draw.
2. **Rank.**
   - **Per resource:** each resource r has its own order of sacrifice, πᵣ. There is no reason the order for oxygen must match the order for protein, iron, staff time or money. **Where the orders coincide, a single "rank" is shorthand,** and the mapping says so.
   - **Under joint scarcity:** πᵣ is the order of sacrifice when resource r alone is limiting. Parts draw **bundles of activity**, never separate resources. Where several complementary resources bind together and their orders conflict, ordinal ranks do not decide the outcome (propositions P16): the explicit network is needed, and the reduced form reports the case as underdetermined.
   - **What it is:** for each resource, the order in which parts lose adequate access when it is scarce. It is a coarse-grained property of the network: topology, pathway capacity, gating, autoregulation, affinity, redundancy.
   - **What it answers:** who absorbs the shortfall first. It does not set how much each part receives in normal running, which the governor varies all the time.
   - **How it is fixed:** at mapping, from documented properties of access. **Examples:**
     - how strongly each vascular bed constricts under sympathetic drive;
     - autoregulation;
     - redundant routes;
     - **affinity, where access is by saturable uptake** (propositions P17; Section 8, step 4);
     - which budget lines are discretionary.

     **It is never read off the observed order of sacrifice** in the data being tested.
   - **Strict or shared:** where access is by saturable uptake, priority is strict only where neighbouring affinities are far apart, and shared otherwise (P17).
   - **The open question (Tier 1):** is the order fixed, or does it reverse with conditions?
     - **A valid test needs two recipients competing for the same scarce resource at the same time,** with their order reversing between conditions.
     - A part receiving more in one condition and less in another is not such a test.
     - **A change of allocation between conditions is not evidence of rank reversal if the governor mode also changes** (item 4). The test needs the mode held constant.
     - A reversal could also come from local autoregulation, so the test is designed with the network in view.
3. **Economising.**
   - **What it is:** a **magnitude**, the share by which ordinary parts' work access is cut when the shortfall still expected outruns the stores. With a known need (a predictable season), it starts at onset.
   - **How it is realised** (fixed at mapping): **consolidation** (units switched off) is the default; a mapping may declare a **throttled** share (active units working below capacity, returning at once with no reactivation cost). Loss is not a realisation of economising.
   - **What it does:** it cuts work, not renewal, so **it causes no unit loss at any speed.** Its saving arrives at once for work and its wear, and as units are switched off for their baseline renewal. Stores are preserved (G16; propositions P11).
   - **Reversible remodelling** (organs shrinking and regrowing with mode or season) is economising realised through consolidation and later reactivation, not deterioration.
4. **The switch, and governors as modes** (open; Section 12): signals may select a different setting that overrides the routine one. **A mode is a setting of the governor that opens one class of work and closes another** (for example, a build or production setting and a consolidate or maintenance setting). That is the source of access-limited load (Section 6).
5. **Recovery by marginal value.**
   - **The intake comes first** (it is support).
   - Then each unit of surplus goes to whichever is worth more:
     - **a unit of store** is worth the expected frequency of shortfall, times the chance that the next deficit is deeper than the store's level, times the cost of being short. Its value falls as the store fills;
     - **a unit of a part** is worth the probability that it will bind, times the cost of that part's output being short.
   - **After a short episode,** parts come back first. **After a long one,** the stores do (G10). The crossover is computed only when a mapping supplies the costs in common units, fixed before outcomes.
   - **A store refills only to a critical fractile** of remembered episode depths while parts are still short (G26).

## 5. What a part does with what reaches it

1. **Basal maintenance first.** Basal maintenance keeps the part's units in existence: active and switched-off units both need it.
2. **Then work.** A part does its work with what reaches it. It does not repair itself: renewal of its units, and rebuilding of its lost units, are the repair network's work. Work never stops for repair.
3. **Work** is the minimum of active capacity and, for each required resource, what reaches the part for work divided by its requirement (the law of the minimum). Near co-limitation by several resources, the synthesising-unit form gives somewhat less work, smoothly. **What the part cannot use stays in the flow.**
4. **Units change only through supply:**

   | What is short | What happens | Kind |
   |---|---|---|
   | Basal maintenance | The part pays the unmet upkeep from its own units: switched-off units are broken down first, then active ones. **It shrinks** rather than losing its whole unfunded share; the units broken down are lost | Lost (disorderly) |
   | Renewal (the repair network does not reach these units) | Units that cannot be renewed are switched off, up to the part's switch-off rate. The rest fail and are lost | Switched off: orderly. Lost: disorderly |
   | Work (more units active than the supported work needs) | Units are switched off (consolidation), or held active below capacity where the mapping declares a throttled share | Switched off, or throttled |
   | Nothing (supply returns) | Switched-off units are reactivated at a limited rate, at a cost; lost units are rebuilt by the repair network, in its order of priority and at its capacity, unless scarred | Coming back |
5. **Scar.** If units lost in disorder in one episode exceed the part's template limit, the excess is scarred and never returns. Fixed capital has no rebuild, so any loss is kept.

**Rate decides harm.** A fall in renewal no faster than the switch-off rate loses nothing at any depth. A faster fall loses units; a scar needs both speed and depth, and the threshold depth falls as speed rises. Fixed capital is scarred by any fall faster than the switch-off rate (G8; propositions P6).

**Rising requirement.** Work rises within active capacity; switched-off units are then reactivated, at a limited rate and a cost; output falls short only when the rise outpaces reactivation or exceeds total capacity (propositions P14).

## 6. How load moves, and how systems fail

**Load, defined.**
- **What it is:** resource redirection. For each resource r and part i:
  - **qᵢᵣ⁰(t)** is the **reference allocation**: what the part would receive without the shortfall, fixed at mapping as a rule (basal maintenance, work, and renewal with wear, for the reference state under current conditions);
  - **aᵢᵣ(t)** is what actually reaches it;
  - **local load** is **ℓᵢᵣ(t) = max(0, qᵢᵣ⁰(t) − aᵢᵣ(t)).**
- **Load is a vector** (one value per resource). A single number is used only where a common currency exists.
- **The reference stays fixed.** If a part switches units off and its requirement is redefined downwards, the load has not vanished: it has been absorbed.
- **Load flow and load residue.**
  - **Load flow** is the deficit moving through the system.
  - **Load residue** is the state change left by absorbing it: units switched off, lost or scarred, and stores drawn.
- **Two ledgers, kept apart.**
  - **The resource ledger** (per resource, in units of that resource). The gap between the reference requirement and supply equals store draw, plus the unmet reference allocations (the sum of the local loads), plus resource drawn in from outside the boundary. **Every unit of gap is accounted for:** carried by a store, met from outside, or left unmet at a named part.
  - **Exported load is not a resource term:** a commitment the system sheds shows as unmet load at the part whose work was shed, and the work not done, landing on another system, is residue. The reference allocation is never redefined to make an export disappear.
  - **The state ledger** (in units of state). What each unmet allocation leaves behind: units switched off, lost or scarred, and the work not done. **Residue is a consequence of load, not a further destination for it.** It is never added to the resource ledger.
  - **Load passing on:** where a part's unmet allocation reduces its output, parts depending on that output lose capacity. That is load moving through a dependency, counted at the receiving part.
- **Three origins of load** (all within ℓ = max(0, q⁰ − a), with a depending on the governor's settings):
  - **supply-limited:** the flow falls;
  - **requirement-limited:** the reference requirement rises;
  - **access-limited:** the governor's current setting restricts a part's access while resources are sufficient. For example, a growth or production setting holds a maintenance or recycling process shut, as growth signalling (mTORC1) suppresses autophagy even when nutrients are present. **An opportunity cost imposed by control architecture** (James).
  - **Guard:** an access restriction counts only if the setting (the mode) and the process it gates are **documented independently and named at mapping** (Section 8). It is never inferred from the shortfall it would explain.
- **Chronic** is a state in which a required restorative process persistently fails to keep pace with the deterioration it must clear, whatever the origin of the load. For a maintenance class M with backlog B_M: B_M(t+1) = B_M(t) + ℓ_M(t) − R_M(t), where R_M is the clearing achieved. It is chronic when the expected load exceeds the expected clearing over the period that matters, so the backlog grows.
  - **Time is therefore an allocation dimension:** with resources held equal, a backlog grows with the share of time spent in settings that gate its process shut.

**Movement and failure.**
- **Load is relocated, never removed** (Section 1 and its derived result).
- **Load backs up a dependency:** a part limited by throughput leaves work undone, and parts depending on its output lose capacity.
- **Coupling is shared dependency.** Parts sharing an input, a stressor, a store or repair machinery move together (G18).
- **Pathways and severance.**
  - **A pathway's capacity** is the maximum flow from the resource's source to the part (the sum of its routes in the simplest parallel case).
  - **Severance** is a pathway's capacity at zero: the minimum cut between source and part has capacity zero, however many cuts that took. **Constriction** is capacity above zero but below need.
  - **Rerouting.** Losing or narrowing a route moves its flow onto the rest. **Where flow divides by physics** (vessels, pipes, power lines), a surviving route can be overloaded, or the displaced flow drawn from another part's branch (steal), even with spare total capacity; in bodies the governor's gates then correct the split where they can. **Where flow is reallocated by choice** (budgets, routers), this happens only when total spare capacity is short. Overloaded routes fail in turn: a cascade along substitutes (G24).
  - **Severing a bypassable route relocates flow; severing a non-bypassable link stops it.**
- **The exhaustion cascade.** Parts switch off in ascending rank, then lose units in ascending rank. The top loses its last units last.
- **Severance or constriction of a non-bypassable link** breaks the record while stores hold and other parts are funded.
- **Collapse and death** (viability theory).
  - **The viable set** is the states in which the record and the levels it depends on hold, fixed at mapping.
  - **Collapse:** the system is outside the viable set, but a route back exists: some admissible course of access returns it (the state is inside the capture basin).
  - **Death:** no admissible route back remains.
  - **Exhaustion and severance are the two routes to collapse.** They end in death only when the route back is lost too: the template is scarred, stores and intake cannot rebuild the top before other parts' basal maintenance fails, or a severed link cannot be repaired. A sufficient condition for collapse, not death, can be checked before the outcome (propositions P15).
  - **Whether outside support is admissible** (an anaesthetist, a bail-out, a defibrillator) is fixed at mapping. The same state can be collapse with it and death without it.

## 7. Read-outs

- **The record:** the top's work divided by X. It is flat while load is absorbed below, and moves when nothing more can be taken. **It breaks at two thresholds:** at once when what is available falls below the top's own need, and one step later, through its dependence on support parts, when it falls below the top's need plus everyone's basal maintenance plus support parts' needs.
- **Record dynamics (G12).** Recovery from small knocks slows as release headroom shrinks. Under proportional release, headroom reaches zero before the break, by a lead time that shortens as the shortfall grows relative to what parts below the top can carry (propositions P5).
- **State signals:** active, switched-off, lost and scarred units per part; store levels; **the repair backlog** (lost units waiting for the repair network).
- **Co-movement (G18):** parts sharing a loaded dependency move together before the break.
- **The three outcomes,** told apart by what comes back and how fast:

  | Outcome | Comes back | How |
  |---|---|---|
  | Switched off | Fully, within a few steps | Reactivation |
  | Lost | Fully, over the rebuild time | Rebuilding by the repair network |
  | Scar | Never | Ceiling lowered |
- **The ledgers:**
  - per resource: supply in plus stores drawn = work done + maintenance and renewal + reactivation and rebuilding + stores refilled + spill;
  - against the reference allocation, the resource ledger: gap = store draw + unmet reference allocations + resource drawn in from outside;
  - separately, the state ledger: the residue each unmet allocation leaves (Section 6).
- **Time of crisis:** the time spent outside the viable set before re-entry.
- **Cost of restoration:** the resource needed to get back. Its inverse is resilience (Martin 2004).
- **Carried from v0.16, not re-examined:** the Felicity read-out (protection set by peak load); reading a compensating part's output.

## 8. Mapping a system

Do this before opening any outcome data.

1. **Boundary, currency and protected level.** Name the system, its boundary and the level whose viability is protected. Fix all three before outcomes are seen: they are the model's main safeguards.
   - **Also fix the viable set,** and **whether outside support counts as admissible** (it decides collapse against death).
   - **A record may be an intermediate stage of a longer pathway:** an early stage can hold while load appears in a later dependent stage. Mapping fixes whether viability requires the early output, the downstream completion, or both. The order of failure in the read-outs need not be the order of onset.
2. **Resources, carriers and stores.**
   - Which resources does work need, in what ratio?
   - **Are they complementary** (used in fixed proportion)? The law of the minimum applies only where they are. **Substitutable inputs are mapped as one resource,** or declared (for the brain, glucose and ketones are one resource, energy).
   - What carries them (the network)?
   - Which stores exist for each, in what order, with what release profile (proportional, or full until empty), and with what turnover?
   - Which can be spilled?
3. **The governor and its levels.**
   - What is X (the record), and what levels does X depend on?
   - What does the governor act through: stores, intake, gates, pathway capacity, explicit budgets?
4. **Parts.** For each part:
   - its units and capacity;
   - **its rank for each resource, fixed from documented properties of access** (Section 4, item 2), or one shared rank if the orders are documented to coincide;
   - **where access is by saturable uptake** (transporters, binding), the rank is the **order of affinities** (half-saturation constants), lowest affinity losing first. Priority is **strict** only where neighbouring affinities are far apart, and **shared** otherwise. Document the constants and their separation before outcomes (propositions P17);
   - its rebuild time, template limit and route back (fixed capital: none);
   - its requirements per unit of work, basal maintenance and renewal (renewal as a baseline per active unit **plus wear per unit of work**);
   - **its reference allocation** (for load);
   - whether it is support for the top;
   - whether it is the intake;
   - whether it is temporary;
   - **how economising is realised** in it: consolidation (the default) or a declared throttled share.

   Fix these from independent sources. Anything chosen with the expected outcome in mind is declared fitted.
5. **The repair network.** Its parts (resident and mobile), their capacity and source, their resources and reserves, and their rank.
6. **Links and pathways.**
   - Dependencies (supply edges) and loops.
   - Pathways and their routes (redundancy), and **whether flow among routes divides by physics or is reallocated by choice** (G24).
   - Non-bypassable links (severance points).
   - Which parts share the repair network.
7. **Nested systems** (only if the extension in Section 15 is used): list every component treated as a nested system, with the evidence for its own access loop, and its interfaces. **A component not listed here stays a part.**
8. **Modes and gates** (only if access-limited load is claimed): name each governor setting and the process it gates, with independent documentation of the gate. A gate not named here cannot be invoked to explain a shortfall later.
9. **The clock.** Fix the unit in which durations are judged.

**The bias ledger** (adopted 7 October 2026; theory/PAM_probe_register.md). Before looking anything up, score the interpretive freedom of each mapping choice from 1 (forced) to 5 (open).

## 9. Using the model in reverse

- Reverse mode starts from what is seen failing and points to where load entered, which parts were absorbing it unseen, and which dependency the failing parts share.
- **It suggests where to look; it never names a cause.**
- **Disciplines:** it is a hypothesis generator, not evidence; correct for visibility; name a set, not a cause.
- It must distinguish failure clustered by rank from failure clustered by dependency.

## 10. Generic predictions

**Layers:** layer 1 holds for any finite-stock feedback loop; layer 2 needs selection or design.

**Evidence labels** (adopted 7 October 2026): modelling choice; derived prediction; simulation result; natural-system observation; direct test; compatible but non-diagnostic; unknown; contradicted; fitted.

| No. | Prediction | Layer | Status |
|---|---|---|---|
| G1 | The record stays near normal while lower parts and stores move. **It is flat while the gap is no larger than what the stores release plus what parts below the top can give up** | 1 | Natural observation: consistent; simulation result (TQ13); derived (propositions P2). H1 check not consistent (10.7% of 75 cases), low weight |
| G2 | Lower-ranked parts lose access first, in ascending rank | 2 | Natural observation: consistent; simulation result (TQ13); derived (P3) |
| G3 | With a store carrying the gap and its release not binding, the break comes at the same cumulative shortfall whatever the rate. Where release binds (a tapering store, or a gap above the release rate), faster onset breaks earlier. **Under proportional release (the default), the store left unused at the break is (gap minus margin) divided by the store's turnover rate, so a faster shortfall leaves more of the store unused, in proportion** | 1 | Derived (results R4; propositions P4); stress-test candidate |
| G4 | A larger store gives a longer silence; a depleted start breaks sooner | 1 | Natural observation: consistent; derived (P2) |
| G5 | Parts absorbing load lose units (switched off first, lost if supply falls too fast), so loss compounds down the ranks | 1 | Simulation result (TQ13); derived (P3, P6) |
| G6 | Recovery starts with the intake; the record recovers before the state does | 2 | Natural observation: consistent (kidney); simulation result (TQ11b, TQ13) |
| G7 | Fixed capital keeps what it loses; renewable parts rebuild lost units, except where the template is scarred | 1 | Natural observation: consistent; simulation result (TQ13) |
| G8 | **Rate decides harm.** Renewal falling no faster than a part can switch units off leaves no loss. Faster falls lose units. A scar needs speed and depth together; the threshold depth falls as speed rises | 1 | Simulation result (TQ13 O1, O4); derived with bounds (P6); compatible: supply cut suddenly to heart muscle against gradual atrophy; untested |
| G9 | A system re-tuned to a past threat does better against it again, and may do worse if conditions change | 2 | Carried from v0.16 (not re-examined) |
| G10 | After a short episode, parts come back before stores; after a long one, stores come first | 2 | Natural observation: consistent; simulation result (TQ11d, TQ13); qualitative unless costs are mapped (P9) |
| G12 | Recovery from small knocks slows before the break when the break is approached through shrinking release headroom (a tapering store, or a gap rising towards the release rate). It does not when the break comes with headroom intact (a store with full release emptying, or a switch) | 1 | **Fails in its first held-out test** (H1 VitalDB, blood loss under anaesthesia, release profile committed as taper; adjudicated 7 October 2026). Weight: fallback cohort, half. Qualifications: runnable only under the pre-data reading of missing bins; step-down inside the fallback cohort not stated in the pre-registration. tests/results/H1-VDB/README.md. Lead time derived (P5) |
| G13 | Lowest-ranked parts take the load first, and longest **where their value in recovery is also lowest** (recovery is by marginal value, not rank) | 2 | Simulation result (TQ13 cascade); derived (P12) |
| G14 | Peak-referenced protection (the Felicity read-out) | 2 | Carried from v0.16 (not re-examined; not in the engine) |
| G15 | Store memory: a deeper shortfall leaves larger stores for longer | 2 | Carried from v0.16 (not in the engine) |
| G16 | **Economising:** with an expected shortfall, the governor cuts work access early and evenly. **It causes no unit loss at any speed:** work is cut, not renewal. Its saving arrives at once for work and wear, and as units are switched off for their baseline renewal; stores are preserved | 2 | Simulation result (TQ11, TQ13 O4); derived (P11); compatible: hibernation, remodelling |
| G17 | Economising and growth compete | 2 | Carried from v0.16 (growth not in the engine) |
| G18 | Parts sharing a loaded dependency co-move before the break; parts clustered only by rank do not | 1 and 2 | Simulation result (TQ9 to TQ11); untested |
| G19 | **Three outcomes** (switched off, lost, scar) are distinguishable by what comes back and how fast | 1 | Simulation result (TQ13 O4); untested |
| G20 | **Exhaustion and severance.** No part loses units while there is somewhere else to take resources from. The top goes last. Failure with willing receivers intact means a link **cut or constricted below need** (pathway capacity as maximum flow) **or damage from outside** to the top or its supports | 1 | Simulation result (TQ13 O2, TQ11 M4); derived (results R6; P8); untested |
| G21 | **The law of the minimum.** A part's work falls in proportion to its scarcest resource while other resources are ample; what it cannot use stays in the flow, and surplus is spilled | 1 | Simulation result (TQ12, TQ13); known (Liebig); general form: synthesising units (DEB) |
| G22 | **The intake coasts.** With nothing to take in, the intake switches its units off on basal maintenance and is back first at refeeding, whatever its rank | 2 | Simulation result (TQ13); derived (P9); compatible: python gut, migrating birds |
| G23 | **Repair is a shared, governed network.** (a) Under a sustained shortfall, repair slows across the system, even where the damaged part's own supply is ample. (b) **Strict rank:** when several parts are damaged at once, those ranked after another damaged part heal more slowly than alone; the highest-ranked damaged part heals as fast as alone. (c) An acute threat moves repair capacity to likely sites of damage before it occurs | 2 | Compatible: (a) stress slows wound healing (Kiecolt-Glaser 1995; Marucha 1998); (c) acute stress redistributes immune cells (Dhabhar). (b) derived (results R8; P10); untested; distinguishable in data from shared repair, in which every damaged part slows. Not in the frozen engine |
| G24 | **Cascade along substitutes.** Losing or narrowing a route moves its flow onto the rest. **Where flow divides by physics** (vessels, pipes, power lines), a surviving route can be overloaded, or the displaced flow drawn from another part's branch (**steal**), **even with spare total capacity.** **Where flow is reallocated by choice** (budgets, routers), this happens only when total spare capacity is short. Overloaded routes fail in turn, so failure spreads along the substitutes, not by rank | 1 | Derived (P13); known in power systems; steal known in physiology (subclavian, coronary); untested as a model prediction |
| G25 | **Order of sacrifice from access.** Under scarcity, the order in which parts lose adequate supply is predicted by properties of access documented beforehand (constriction under sympathetic drive, autoregulation, affinity, redundancy; discretionary budgets) | 2 | Derived; compatible: splanchnic and renal vasoconstriction protecting heart and brain in haemorrhage. **Supported in its first held-out test at half weight** (PT1, English single-tier councils 2014-15 to 2019-20, with statutory duty classified blind as the documented access property; adjudicated 7 October 2026): lines with a statutory duty were protected more than discretionary lines; lines with a duty of uncertain level were not distinguishable from discretionary ones, and that step fails without London (sensitivity only). **The scarcity version (G25-C) was not supported:** the gap did not widen detectably where funding fell more. tests/results/PT1/README.md |
| G26 | **Partial refill.** In recovery, a store refills only until its marginal value falls to that of the best competing use, so it need not refill to full while parts are still short. **The refill level is a critical fractile of remembered episode depths:** the 1 − V/(c_S ρ) quantile, where V is the best competing value, c_S the cost of the store being short and ρ the expected frequency of shortfall | 2 | Derived (marginal analysis; P9, newsvendor); untested |

**The standing check:** before adding any rule, attempt a complete mapping with the existing parts, resources, stores, ranks, links, boundary, objective and clock. Add a mechanism only after a confirmed qualitative failure in a pre-committed test.

## 11. Status, evidence and working rules

- **Evidence so far:**
  - natural surface tests 1 to 12;
  - definition checks (framing crosscheck; deterioration and scar scan; repair and allocation scan);
  - simulations TQ1 to TQ13b;
  - derived propositions P1 to P18, checked numerically;
  - two held-out tests (below);
  - the theory-building probes of 6 October 2026 (salmon, cancer, pregnancy, the power grid, skin circulation) and the probe register P1 to P12. **They are not tests:** the outcomes were known, and none counts as support.
- **First held-out test: H1 VitalDB (G12).**
  - Run, and the computation replicated by a second model.
  - **Adjudicated blind by GPT (7 October 2026): Fails, at half weight,** with two stated qualifications (raw/2026-10-07_chatgpt_H1-VDB-ADJ1.md). The computed verdict depends on the reading of missing bins in the stable approach (tests/results/H1-VDB-R1/README.md).
  - **Under the standing check:** G12 as mapped for blood loss under anaesthesia has failed once. The first candidate for revision is that mapping (the release profile: taper or switch), not a new mechanism. One failure at half weight does not remove G12. The release-profile question (Tier 2) is live.
  - **The G1 check in H1 was also not consistent** (10.7% of 75 cases, against more than half), at low weight. The anaesthetist defends pressure, and the check was not decomposed.
- **Second held-out test: PT1, English single-tier councils, 2014-15 to 2019-20** (fixed against dynamic priority, with G25).
  - Run, and the computation replicated exactly by a second model (tests/results/PT1-R1/README.md). Deviations D-1 to D-5 logged, all neutral.
  - **Adjudicated blind by GPT (7 October 2026)** (raw/2026-10-07_chatgpt_PT1-ADJ1.md):
    - **PT1: Inconclusive, full weight.** Projected client growth published before the budget showed no detectable effect on which lines were protected (β = 0.05), but the 95% interval (−0.75 to 0.86) includes the smallest effect that mattered (0.25). Neither fixed nor dynamic priority is earned for this system.
    - **G25: Supported, half weight** (contamination: the broad pattern was known).
    - **G25-C: Not supported, half weight.**
    - **SS (descriptive):** in about 97% of council-years with a fall in spending, some statutory line also fell while discretionary lines kept more than half their 2014-15 total. A coarse measure; it does not show a strict queue at line level.
- **The reference implementation:** theory/sim/tq_units.py (frozen). **Its constants are engine-level and illustrative,** not universal levels: switch-off and reactivation rates, failure rate, reactivation and rebuild costs, the default template limit.
- **Where the frozen engine departs from v0.19:**
  - **Claim order:** it funds support parts' basal maintenance and work before ordinary parts' basal maintenance; v0.19 puts every part's basal maintenance first.
  - **Repair:** it renews inside each part by a repair-share rule, with no repair network.
  - **Access:** it writes access as an order of claims with one rank for all resources; what a part cannot use goes back to the stores rather than on to later parts in the flow.
  - **Forms:** it keeps the knee, the earlier unit-loss rule (no shrinking), the minimum, and refill-then-spill; it has the wear term.
  - **Not in the engine:** the reference allocation and the load ledgers, pathway capacity and severance by capacity, damage, part death by severance of the route back, temporary parts.
  - **Consequence:** results that depend on these (the refeeding loss in TQ13b) are engine artefacts. Any new engine run states which forms it uses. If the paper needs a demonstration, a small engine check of the repair network and the claim order comes first.
- **Status labels, the fitted list, the evidence rule** ("not identified is not absent") **and the standing check:** as stated in CLAUDE.md and v0.16 Section 9.

## 12. Open questions, tiered

**Tier 1: could threaten the model.**
- **Fixed against dynamic priority.** Does the order of sacrifice reverse with conditions? Tested by Section 4, item 2: two recipients, one scarce resource, the same time, mode held constant. **First test (PT1, councils): inconclusive,** for lack of precision. Still open.
- **Independence of inputs.** Can ranks (from access), requirements, reference allocations, rebuild times and template limits be fixed independently of the outcome?
- **Out-of-sample prediction.** Does the model predict a new system's order of loss and recovery without fitting it (G25)? **First held-out support at half weight (PT1, councils),** for order of loss only; recovery untested.
- **The three outcomes in held-out data.**
- **G18 in data.**
- **Sensitivity to framing.**

**Tier 2: refining a surviving model.**
- **The release profile** (proportional, a knee, or full release until a switch). **Live after H1.**
- **The repair network:** resident and mobile kept apart, or one workforce?
- **What starts anticipatory economising;** how the expected frequency of shortfall is learned; what sets a template limit.
- **Harmful inputs:** entered for now as exogenous loss of units or pathway capacity (Section 3, Damage). A mechanism is added only if a pre-committed test fails without one.
- **Governors as modes,** and which wins when two are signalled at once. Straub's cases (chronic inflammation silencing the brain-led setting; chronic stress suppressing the immune setting) are evidence for this question, not a second governor.
- **The cascade rule** (G24): how an overloaded route fails. Left open until a mapping needs it.
- **The carried v0.16 mechanisms:** which predictions need them?
- **Closed (7 October 2026):** collapse or death of the whole system, by viability theory (Section 6).

**Tier 3: niche or application.**
- the boundary between labelled and unlabelled load;
- whether a dependant's need falls with its supplier's economising;
- institutions growing or re-tuning.

**For the paper:**
- the claims to test are the general architecture, not the physiology (broadcast signals with selective receivers are textbook);
- prior theories are convergence (theory/PAM_unification_table.md); the contribution is unification and generality, with three components no prior theory carries: **rank fixed beforehand from documented access, the conserved load ledger, and application outside bodies;**
- GPT's six conditions for a significant contribution: formal load; the governor and parts written formally; propositions derived analytically (P1 to P18); what the model predicts that DEB, allostasis and control theory do not; held-out tests; scope and stated failures.

## 13. Way forward

1. **v0.19 approved** (pending James).
2. **The model paper's mathematical section,** written from the derived propositions.
3. **A cleaner G25 test** (no contamination) and a more precise priority test.
4. **The G12 mapping fault** to be named before any re-look at H1.
5. **The model paper, then a preprint.** The Representation Gap paper stays the observational half (the pattern and where to measure it).

## 14. Terms

- **Governor:** the function that holds the levels persistence depends on, by regulating access to resources. Allocation is the resulting flow.
- **Access:** what a part can draw, set by the network, its gates and the governor's signals.
- **Rank (πᵣ):** for each resource, the order in which parts lose adequate access when it is scarce; fixed at mapping from documented properties of access. A single "rank" is shorthand where the orders coincide.
- **Part:** a working part (including intake and control), made of units; it has no demand of its own.
- **Repair network:** the repair workforce (resident and mobile), a set of parts whose work is renewing and rebuilding other parts' units; governed like any part.
- **Unit states:** active, switched off, lost, scarred.
- **Switched off:** the unit keeps its route back, receives basal maintenance only, and does little or no work.
- **Throttled:** active units working below capacity, declared at mapping; they return at once with no reactivation cost.
- **Renewal:** the repair network's work on active units: a baseline per active unit plus **wear** per unit of work done.
- **Economising:** a magnitude, the share by which ordinary parts' work access is cut; realised by consolidation by default.
- **Part death:** severance of a part's route back.
- **Load:** the shortfall, per resource, between a part's reference allocation and what reaches it.
- **Residue:** the state change left by absorbing load (units switched off, lost or scarred; work not done).
- **Record:** the routine output of the top, divided by its level.
- **The expected frequency of shortfall:** how often supply falls short, learned from experience; it sets the stores' value.
- **Severance:** a pathway's minimum cut at zero. **Constriction:** above zero but below need.
- **Steal:** displaced flow drawn from another part's branch when flow divides by physics.
- **Viable set:** the states in which the record and the levels it depends on hold. **Capture basin:** the states from which some admissible course of access returns the system to the viable set. **Collapse:** outside the viable set, inside the capture basin. **Death:** outside the capture basin.
- **Capture** (extension): a nested system changing the signals or gates that set its own access.

## 15. Extension layer (proposed, phase 3): nested systems

**Status:**
- **Approved by James as a proposed extension** (6 October 2026).
- **It does not change the core.** It is used only in mappings that need it (institutions; host and tumour), and only with the mapping guard.
- **It is kept out of the first model paper's core claims** unless it has passed a pre-committed test of its own.

1. **Part or system.**
   - A component is a **part** if its access is set by the containing system's governor, and its own state affects future access only through that governor.
   - It is a **nested system** if it has its own closed loop that regulates its own access and viability, possibly against the containing system's.
   - **Examples:** a tumour that recruits blood supply and alters host metabolism; a person in an institution.
2. **Supply through a part needs nothing extra.**
   - Where one system supplies another through a part the first system governs, ordinary access is enough. **Example:** the placenta, a temporary maternal part, supplying the fetus downstream.
   - More is needed only if the downstream system has independent control over the upstream access that cannot be represented as ordinary governance signalling.
3. **Institutions have two architectures in the same space.**
   - **The functional graph:** roles, functions and departments, as parts.
   - **The embedded systems:** the people, each a complete persistence system.
   - **A role is where they meet.** Strain on a role is load pushed across a system boundary into a person. The person draws their own stores (time, sleep, health) until they protect their own viability by withdrawing, falling sick or leaving.
4. **Capture.**
   - A nested system changes the signals or gates that set its own access.
   - **The structural conflict of interest:** the measured system helps produce the signal that allocates back to it. **Examples:** reporting capacity conservatively to protect headcount; spending to budget; metric inflation.
   - This is where the Beyond Nash behaviours and the Representation Gap enter the model's signal path.
5. **Mapping guard** (Section 8, item 7):
   - Nested systems are listed before outcomes, with independent evidence of their own access loop.
   - Reclassifying a part as a nested system after an outcome is a fitted change.
6. **First test of the criterion:**
   - Classify components by criterion 1 **before** outcomes, across domains (biology, organisations, computing, ecology).
   - Check that those classed as systems behave as systems and the parts as parts.
   - **Discard the criterion if they do not.**
7. **Drain against capture** (propositions P18; James, 7 October 2026).
   - A nested system that only drains is, for the host, exactly a supply cut by its **net** drain: its draw less the former draw of the tissue it displaced.
   - So a host carrying it should match a host whose supply is cut by that amount, with the same tissues losing in the same order. (A pair-fed control matches intake, not the drain.)
   - **Capture** shows as departure from that control, at the gates the nested system acts on.
   - **Example:** in mice, the MAC13 tumour took more glucose than MAC16, yet only MAC16 caused cachexia (Mulligan and Tisdale 1991): the drain alone did not produce the wasting.

## Consolidation notes (for James's check)

Every place where v0.19's wording differs from v0.18 as amended, and why. Nothing here is a new decision; each item applies an approved one.

| No. | Where | v0.18 text | v0.19 text | Approved by |
|---|---|---|---|---|
| 1 | Header and "Changes" table | Long status line of dated corrections; table of changes from v0.17 | One consolidation status; table of changes from v0.18 | Consolidation (James, 7 October: "consolidate at paper time") |
| 2 | Section 3, governor | No note on two regulators | One sentence: two regulators that can each take control are two modes of one governor function | James, 7 October (Straub absorbed) |
| 3 | Section 3, unit states | Active, switched off ("coasting on minimal maintenance"), lost, scarred | Switched off defined: keeps its route back, basal maintenance only, little or no work; quiescence an instance | Approved for v0.19 (changelog) |
| 4 | Section 3, repair network | Strict rank stated in G23(b) only; no renewal composition | "Served strictly by rank"; renewal as baseline plus wear | Flag 5 (strict rank); wear restored (James, 7 October) |
| 5 | Section 3, stores and spill | "Release can taper as it empties (the knee)"; spill once stores are full | Proportional release by default; full release as alternative, possibly mode-dependent; knee as engine form; spill with a recovery fraction; resources as a flow | DEB imports; flow correction (James, 7 October) |
| 6 | Section 4, item 1 | Order of claims ending "from surplus only... at their value (the expected frequency of shortfall)" | Ordered draw from the flow; item 5 by marginal value; renewal named in phases 3 and 4 | Flow correction; marginal-value amendment |
| 7 | Section 4, item 2 | Rank examples without affinity; strict or shared not addressed | Affinity added to examples; strict or shared by separation of affinities | Flag I |
| 8 | Section 4, item 3 | "Access is cut early and evenly. Units switch off in an orderly way" | Economising as a magnitude; consolidation default, throttled share declared; no loss at any speed; saving timing; remodelling as economising | Approved for v0.19; flag F; remodelling folded in (probe register) |
| 9 | Section 4, item 5 | Recovery text sat in Section 6 | Moved to Section 4 as what the governor does; G26's fractile added | Marginal-value amendment; flag D |
| 10 | Section 5 | "Unchanged from v0.17" pointer | Written out; basal shortfall now shrinks the part (DEB); unused resource stays in the flow; throttled realisation; rate decides harm and rising requirement summarised | DEB imports; flow correction; flags B and F; P14 |
| 11 | Section 6, pathways | Losing routes saturates the rest | Constriction defined; rerouting by physics or by choice; steal | Flags C and H |
| 12 | Section 6, reference allocation | Not specified as a rule in the text | "Fixed at mapping as a rule (basal maintenance, work, and renewal with wear...)" | Maths Section 7; wear restored |
| 13 | Section 7 | "Unchanged from v0.17" plus additions | Written out; record dynamics with lead time; scarred units in state signals | P5; consolidation |
| 14 | Section 8, step 2 | Substitutable inputs "mapped as one resource, or declared" | Example added: for the brain, glucose and ketones are one resource (energy); release profile and turnover named | S11597 correction (James, 7 October); DEB imports |
| 15 | Section 8, step 4 | No economising realisation | "How economising is realised in it" added | Approved for v0.19 |
| 16 | Section 8, step 6 | Routes listed | "Whether flow divides by physics or is reallocated by choice" added | Flag H |
| 17 | Section 9 | "Unchanged from v0.17" pointer | Written out from v0.17 Section 8 and v0.16 Section 7; "price-clustered" read as "clustered by rank" (as v0.18) | Consolidation |
| 18 | Section 10 | "As v0.17, Section 9 (G1 to G23)" plus an additions table | One table, G1 to G26, each in its current approved wording; statuses add the deriving proposition; evidence labels stated | Consolidation; flags A to J; evidence labels (7 October) |
| 19 | Section 10, G1 | v0.17 wording | Silence condition added in words; the H1 G1 check recorded in the status | P2 (derived, no wording flag); H1 record |
| 20 | Section 10, G21 | "Their unused share is returned and spilled" | "What it cannot use stays in the flow, and surplus is spilled" | Flow correction (James, 7 October) |
| 21 | Section 10, G25 | Examples without affinity | Affinity added to the examples | Flag I |
| 22 | Section 11 | "As v0.17, Section 10" plus updates | Written out; engine departures updated (DEB forms not in engine; wear in engine) | Maths Section 12 and flag 7 |
| 23 | Section 12 | Tier 2 "governors as modes, and whether rarity sets which wins" | Reworded to "which wins when two are signalled at once", with Straub's cases as evidence; the cascade rule listed; "For the paper" block gathers the novelty position | James, 7 October (Straub; novelty as unification) |
| 24 | Section 13 | v0.18's way-forward list | Updated to the current plan | CONTROL.md |
| 25 | Section 14 | Terms list | Adds switched off, throttled, renewal (wear), economising, load, residue, record, constriction, steal, viable set, capture basin | Approved decisions above |
| 26 | Section 15 | Items 1 to 6 | Item 7, drain against capture | Flag J |

**Checked, not changed:**
- The central claim is verbatim from v0.18 as corrected and amended.
- The scope section is verbatim.
- G9, G14, G15 and G17 are carried from v0.16 unexamined, as before.
