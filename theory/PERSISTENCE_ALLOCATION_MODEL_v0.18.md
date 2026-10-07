# The Persistence Allocation Model, v0.18 (canonical state, 6 October 2026)

**Status:** working model (phase 3). **The vocabulary is frozen** (James approved v0.18, 6 October 2026). **Corrected 7 October 2026** (James approved): three consistency fixes and one open question logged, no change of content; a second correction from the maths (exported load is residue, not a resource term; resources are drawn from a flow); and a third from the literature map (the stores' value renamed; bundles of activity under joint scarcity; pathway capacity as maximum flow; a complementarity check in mapping); and an amendment (7 October 2026: recovery by marginal value; collapse and death by viability; G3, G12 and G20 sharpened; the partial-refill prediction); and a correction for access-limited load and "chronic" (7 October 2026). **PT1 and G25 results recorded** (7 October 2026; Sections 10 to 13). See the changelog. The probing phase is over. No new mechanism enters unless an existing mapping fails a pre-committed test (the standing check, Section 10).

**The single reference** for the model as it stands.
- **History:** theory/tier_queue_changelog.md.
- **Decisions behind v0.18:** theory/PAM_proposals_from_GPT_chat.md, with the source chat in raw/.
- **The draft as approved:** theory/PERSISTENCE_ALLOCATION_MODEL_v0.18_DRAFT.md (revision 2), kept as the record.
- **Sections marked "as v0.17"** refer to theory/TIER_QUEUE_MODEL_v0.17.md, which is kept unchanged.
- **The reference implementation:** theory/sim/tq_units.py (frozen; a reduced form under v0.18, Section 11).
- **The maths:** theory/PAM_math_v0.18.md (step 1, restatement, 7 October 2026; six flags for James). The v0.16 maths is superseded. **The diagram** is not yet updated.

## Changes from v0.17

| No. | Change | Source |
|---|---|---|
| 1 | **The governor regulates access; the allocation is the resulting flow.** It releases stores, opens and closes intake, and sets the capacity of pathways and gates. Its signals are broadcast, and each pathway responds by rules encoded locally. Explicit allocation (a budget line) is one way of setting access. The central claim is reworded accordingly | F1 (James's cooling-loop question; GPT) |
| 2 | **Rank is the order in which parts lose adequate access when a shared resource is scarce.** It is a coarse-grained property of the network (topology, pathway capacity, gating, autoregulation), not a list held by the governor. It answers one question only: who absorbs the shortfall first. **It is fixed at mapping from documented properties of access,** never read off the observed order of sacrifice | F1, F2 |
| 3 | **A valid test of dynamic priority** needs two recipients competing for the same scarce resource at the same time, with their order of sacrifice reversing between conditions. A part receiving more in one condition and less in another (skin in heat and in haemorrhage) is not a test | F2 (James's correction) |
| 4 | **Severance is a pathway's capacity at zero.** A pathway's capacity is the sum of its routes. Losing some routes lowers capacity and moves flow onto the rest, which can saturate and fail in turn (a cascade). No partial-severance state | F3 (James; GPT) |
| 5 | **Load defined.** Load is resource redirection: the shortfall, per resource, between a reference allocation fixed at mapping and what a part actually receives. **Load flow** (the deficit moving) is kept separate from **load residue** (the state change left by absorbing it). The ledger becomes an identity | A1 (James's definition; GPT's formalisation) |
| 6 | **Governor and parts written formally.** The governor sets access from sensed state; each part's next state depends only on its state and what reaches it. A signal produced inside a part belongs to the governor function | A2, A3 |
| 7 | **Part death.** Collapse is not death. A part dies only when its route back (template, repair source, reconnection) is severed. "Parts do not die" becomes: parts die only by severance of their route back; the system dies by exhaustion or by severance of a non-bypassable link | A6 (James: "severance is the precondition to part death") |
| 8 | **Scope (new Section 2).** Persistence is a viability constraint, not something maximised. Terminal reproductive programmes are out of scope. The model is not a theory of action selection. No boundary may be redrawn after a counterexample | B1 to B4 |
| 9 | **Pregnancy resolved:** the placenta is a temporary part of the mother's system; the fetus is a separate system downstream. No bargaining between governors | F4 (James) |
| 10 | **Extension layer, proposed (Section 15): nested systems.** A component is a nested system when it has its own loop regulating its own access. People in institutions are systems attached to roles. Capture is an embedded system changing the signals or gates that set its own access. Used only with a mapping guard | Reduced C |
| 11 | **New predictions:** G24 (cascade along saturated substitutes); G25 (order of sacrifice predicted from documented access) | From F1, F3 |
| 12 | **Revision 2. Shortfall from either side.** The central claim says "when the resources available fall short of what the reference state requires", in place of "when supply falls short". Scarcity can come from falling supply or rising requirement (work, repair, pregnancy, infection) | GPT review, point 1 |
| 13 | **Revision 2. Two ledgers, not one.** The **resource ledger** accounts for the gap between reference requirement and supply: store draw + unmet reference allocations (the local loads) + resource drawn in from outside the boundary. The **state ledger** records what the unmet allocations leave behind (residue). Residue is a consequence of load, not a further destination for it; revision 1 added it to the same sum and so counted the deficit twice | GPT review, point 2 |
| 14 | **Revision 2. Rank is per resource.** Each resource r has its own order of sacrifice πᵣ. Where the orders coincide, a single "rank" is shorthand | GPT review, point 3 |
| 15 | **Revision 2. The governor does not switch units.** It sets access; units switch when the resulting flow crosses their local thresholds (units change only through supply). If direct state signals are ever needed, the part's state function would take the governor's signal as an input: that would be a new mechanism, under the standing check | GPT review, point 4 |
| 16 | **Revision 2. Damage enters from outside.** Trauma, toxins and pathogens enter as an exogenous loss of units or of pathway capacity; the model handles the resource consequences. No damage mechanism is added | GPT review (damage) |
| 17 | **Revision 2. "In a system that regulates its own persistence"** replaces "In a goal-directed system", which implied agency the model no longer assumes | GPT review (wording) |

## 1. The principle

**Central claim** (v0.18. It is v0.17's approved wording with these changes: the governor regulates access (F1), part death (A6), access in place of allocation where the mechanism is described, and, in revision 2, shortfall from either side and "a system that regulates its own persistence"):

> In a system that regulates its own persistence, a governor holds the levels its persistence depends on by regulating access to finite shared resources among parts that have no demand of their own; the allocation among parts is the resulting flow. Each part works to the limit of the scarcest resource that reaches it. When what reaches a part falls short of what the reference state requires, whether supply falls, requirement rises or access is restricted, the governor draws its stores, and lower-ranked parts lose access first and switch units off. The routine output, the record, holds until nothing more can be taken: the record sees compromise, not stress. Load is relocated, never removed: the resource gap is met from stores, met from outside the boundary, or left unmet at a named part, and unmet load leaves its residue in switched-off, lost or scarred units, or in work not done, which may land across the boundary. A part scales down without harm when supply falls no faster than it can switch units off; units are lost when supply falls faster; the part is scarred only when those losses destroy what rebuilds it. Repair is its own network, governed like any part: under a sustained shortfall it loses access and lost units wait. Recovery runs the other way: the intake first, then parts and stores in order of value, with stores first when the system has learned its world is scarce. A part dies only when its route back is cut; the system collapses when load reaches the top or a non-bypassable link is cut, and dies only when no route back remains.

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
- **What it does:** it **regulates access** to resources. It does this through:
  - releasing, filling and spilling stores;
  - opening and closing intake;
  - setting the capacity of pathways and gates (vascular tone; connection; transporters);
  - mobilising repair (giving the repair network access).

  **It does not switch units directly.** Units switch off or come back when the flow that reaches them crosses their local thresholds (Section 5: units change only through supply).

  **The realised allocation is the resulting flow,** set by the network and the state of the parts. **Explicit allocation** (a budget line, a rota) is one way of setting access; it is not excluded.
- **How it acts:** largely by broadcast. A signal reaches many parts and pathways, and each responds by rules encoded locally: its receptors, local metabolites, its own autoregulation. The same sympathetic signal constricts gut and kidney beds strongly, while the brain's autoregulation and the heart's local metabolic control hold their own flow.
- **Where it sits:**
  - it may be an organ, several organs, or distributed (sensors, signals and gates throughout the system);
  - a signal produced inside a part belongs to the governor function.

  It is a function, not a place.
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
- **Unit states:** **active**, **switched off** (coasting on minimal maintenance) or **lost**. Lost units can be rebuilt unless **scarred** (template gone).
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
- **How it is governed:** like any part. Its capacity is shared, so the parts it serves are coupled through it.
- **Under stress:**
  - **sustained shortfall:** it loses access, so healing slows even where the damaged part's own supply is ample;
  - **acute threat:** it is moved towards likely sites of damage.

**Resources, carriers and stores.**
- **Several resources.** Work, maintenance and renewal each need their own set of resources, in fixed ratio.
- **Carriers are not resources.** A carrier (blood, a power line, a supply chain) is part of the network. It is a resource only where its own stock is what is short (blood volume in haemorrhage).
- **Stores.** Each resource has one or more stores, drawn in order and refilled in order. Each has its own release rate, which can taper as it empties (the knee).
- **Spill.** A resource not needed is spilled once its stores are full. A resource that cannot be spilled (iron) is held by limiting intake.
- **A store is not a part:** it does no work.

**Damage.** Trauma, toxins and pathogens enter from outside as a loss of units or of pathway capacity. The model then handles the resource consequences (repair, load, access). It contains no damage mechanism.

## 4. What the governor does

1. **The order of access** (each resource, each step). In the engine, the network's outcome is written as an order of claims:
   1. the top's full need;
   2. **every part's basal maintenance,** by rank. Existence comes before anyone's work;
   3. support parts' work (parts the top depends on; the intake while it has something to take in);
   4. every other part's work, by rank, **with the repair network ranked among them;**
   5. **from surplus only:** reactivation and rebuilding (the repair network's backlog), against refilling the stores at their value (the expected frequency of shortfall).

   - **The repair network's own capacity** reaches the parts it serves in their rank order.
   - **When supply falls short,** stores are drawn (each up to its release rate), then lower-ranked parts lose access first.
2. **Rank.**
   - **Per resource:** each resource r has its own order of sacrifice, πᵣ. There is no reason the order for oxygen must match the order for protein, iron, staff time or money. **Where the orders coincide, a single "rank" is shorthand,** and the mapping says so.
   - **Under joint scarcity:** πᵣ is the order of sacrifice when resource r alone is limiting. Parts draw **bundles of activity**, never separate resources. Where several complementary resources bind together and their orders conflict, ordinal ranks do not decide the outcome: the explicit network is needed, and the reduced form reports the case as underdetermined (maths, Section 2).
   - **What it is:** for each resource, the order in which parts lose adequate access when it is scarce. It is a coarse-grained property of the network: topology, pathway capacity, gating, autoregulation, redundancy. **The engine's fixed ranks stand for that order.**
   - **What it answers:** who absorbs the shortfall first. It does not set how much each part receives in normal running, which the governor varies all the time.
   - **How it is fixed:** at mapping, from documented properties of access. **Examples:**
     - how strongly each vascular bed constricts under sympathetic drive;
     - autoregulation;
     - redundant routes;
     - which budget lines are discretionary.

     **It is never read off the observed order of sacrifice** in the data being tested.
   - **The open question (Tier 1):** is that order fixed, or does it reverse with conditions? The engine reproduces everything tested so far with fixed ranks, the intake rule and one dynamic quantity, the stores' value (the expected frequency of shortfall).
     - **A valid test needs two recipients competing for the same scarce resource at the same time,** with their order reversing between conditions.
     - A part receiving more in one condition and less in another is not such a test.
     - Under item 1, a reversal could also come from local autoregulation, so the test is designed with the network in view.
3. **Economising.** When the shortfall still expected outruns the stores, access is cut early and evenly. Units switch off in an orderly way and the stores are preserved. With a known need (a predictable season), it starts at onset.
4. **The switch,** and governors as modes (open; Section 12): signals from outside may select a different governor that overrides the routine one. **A mode is a setting of the governor that opens one class of work and closes another** (for example, a build or production setting and a consolidate or maintenance setting). That is the source of access-limited load (Section 6).

## 5. What a part does with what reaches it

**Unchanged from v0.17, Section 4,** with "receives" read as "what reaches it":
1. basal maintenance first;
2. then work. The part does not repair itself;
3. work is the minimum of active capacity and, for each required resource, what reaches the part for work divided by its requirement;
4. units change only through supply (the v0.17 table);
5. scar: disorderly loss past the template limit in one episode.

## 6. How load moves, and how systems fail

**Load, defined.**
- **What it is:** resource redirection. For each resource r and part i:
  - **qᵢᵣ⁰(t)** is the **reference allocation**: what the part would receive without the shortfall, fixed at mapping;
  - **aᵢᵣ(t)** is what actually reaches it;
  - **local load** is **ℓᵢᵣ(t) = max(0, qᵢᵣ⁰(t) − aᵢᵣ(t)).**
- **Load is a vector** (one value per resource). A single number is used only where a common currency exists.
- **The reference stays fixed.** If a part switches units off and its requirement is redefined downwards, the load has not vanished: it has been absorbed.
- **Load flow and load residue.**
  - **Load flow** is the deficit moving through the system.
  - **Load residue** is the state change left by absorbing it: units switched off, lost or scarred, and stores drawn.
- **Two ledgers, kept apart.**
  - **The resource ledger** (per resource, in units of that resource). The gap between the reference requirement and supply equals:
    - store draw;
    - plus the unmet reference allocations (the sum of the local loads ℓᵢᵣ);
    - plus resource drawn in from outside the boundary.

    **Every unit of gap is accounted for:** carried by a store, met from outside, or left unmet at a named part. **Exported load is not a resource term:** a commitment the system sheds shows as unmet load at the part whose work was shed, and the work not done, landing on another system, is residue (the state ledger). The reference allocation is never redefined to make an export disappear.
  - **The state ledger** (in units of state). What each unmet allocation leaves behind: units switched off, lost or scarred, and the work not done. **Residue is a consequence of load, not a further destination for it.** It is never added to the resource ledger.
  - **Load passing on:** where a part's unmet allocation reduces its output, parts depending on that output lose capacity. That is load moving through a dependency, counted at the receiving part.
- **Three origins of load** (all within $\ell_{ir}=[q^0_{ir}-a_{ir}]_+$, with $a_{ir}$ depending on the governor's settings):
  - **supply-limited:** the flow falls;
  - **requirement-limited:** the reference requirement rises;
  - **access-limited:** the governor's current setting restricts a part's access while resources are sufficient. For example, a growth or production setting holds a maintenance or recycling process shut, as growth signalling (mTORC1) suppresses autophagy even when nutrients are present. **An opportunity cost imposed by control architecture** (James).
  - **Guard:** an access restriction counts only if the setting (the mode) and the process it gates are **documented independently and named at mapping** (Section 8). It is never inferred from the shortfall it would explain.
- **Chronic** is a state in which a required restorative process persistently fails to keep pace with the deterioration it must clear, whatever the origin of the load (supply, requirement or access). For a maintenance class $M$ with backlog $B_M$:
$$B_M(t+1)=B_M(t)+\ell_M(t)-R_M(t),$$
  where $R_M$ is the clearing achieved. It is chronic when the expected load exceeds the expected clearing over the period that matters, so the backlog grows.
  - **Time is therefore an allocation dimension:** with resources held equal, a backlog grows with the share of time spent in settings that gate its process shut.

**Movement and failure.**
- **Load is relocated, never removed.** The resource gap is met from stores, met from outside the boundary, or left unmet at a named part. Unmet load leaves its residue in switched-off, lost or scarred units, or in work not done, which may land across the boundary on another system (the state ledger).
- **Load backs up a dependency:** a part limited by throughput leaves work undone, and parts depending on its output lose capacity.
- **Coupling is shared dependency.** Parts sharing an input, a stressor, a store or repair machinery move together (G18).
- **Pathways and severance.**
  - **A pathway's capacity** is the maximum flow from the resource's source to the part: the sum of its routes in the simplest parallel case.
  - **Losing some routes lowers capacity,** and flow moves onto the rest. If they saturate, they fail in turn: a cascade (G24).
  - **Severance is a pathway's capacity at zero** (the minimum cut between source and part has capacity zero), however many cuts that took.
  - **Severing a bypassable route relocates flow; severing a non-bypassable link stops it.**
- **The exhaustion cascade.** Parts switch off in ascending rank, then lose units in ascending rank. The top loses its last units last: **system collapse.**
- **Severance of a non-bypassable link** breaks the record while stores are full and other parts are funded.
- **Collapse and death** (viability theory; theory/PAM_recovery_value_and_viability.md).
  - **The viable set** is the states in which the record and the levels it depends on hold, fixed at mapping.
  - **Collapse:** the system is outside the viable set, but a route back exists: some admissible course of access returns it (the state is inside the capture basin).
  - **Death:** no admissible route back remains.
  - **Exhaustion and severance are the two routes to collapse.** They end in death only when the route back is lost too: the template is scarred, stores and intake cannot rebuild the top before other parts' basal maintenance fails, or a severed link cannot be repaired.
  - **Whether outside support is admissible** (an anaesthetist, a bail-out, a defibrillator) is fixed at mapping. The same state can be collapse with it and death without it.
- **Recovery runs the other way.**
  - The intake comes first.
  - Parts and stores then compete for surplus by **marginal value** (inventory theory; METRIC):
    - **a unit of store** is worth the probability that the next shortfall will be deeper than what is already stored, times the cost of being short. That is the expected frequency of shortfall times the chance of a deficit beyond the store's level, so its value falls as the store fills;
    - **a unit of a part** is worth the probability that it will be needed, times the cost of that part's output being short;
    - each unit of surplus goes to whichever is worth more.
  - After a short episode, parts come back first. After a long one, the stores do.

## 7. Read-outs

**Unchanged from v0.17, Section 6,** with one change: **the ledger is now an identity.** Per resource:
- supply in plus stores drawn = work done + maintenance and renewal + reactivation and rebuilding + stores refilled + spill;
- against the reference allocation, the resource ledger: gap = store draw + unmet reference allocations + resource drawn in from outside;
- separately, the state ledger: the residue each unmet allocation leaves (Section 6).

**Added read-outs:**
- **The record breaks at two thresholds:** at once when what is available falls below the top's own need, and one step later, through its dependence on support parts, when it falls below the top's need plus everyone's basal maintenance plus support parts' needs (results R1).
- **Time of crisis:** the time spent outside the viable set before re-entry.
- **Cost of restoration:** the resource needed to get back. Its inverse is resilience (Martin 2004).

## 8. Mapping a system

Do this before opening any outcome data.

1. **Boundary, currency and protected level.** Name the system, its boundary and the level whose viability is protected. Fix all three before outcomes are seen: they are the model's main safeguards. **Also fix the viable set,** and **whether outside support counts as admissible** (it decides collapse against death).
2. **Resources, carriers and stores.**
   - Which resources does work need, in what ratio?
   - **Are they complementary** (used in fixed proportion)? The law of the minimum applies only where they are. Substitutable inputs are mapped as one resource, or declared.
   - What carries them (the network)?
   - Which stores exist for each, in what order, with what release?
   - Which can be spilled?
3. **The governor and its levels.**
   - What is X (the record), and what levels does X depend on?
   - What does the governor act through: stores, intake, gates, pathway capacity, explicit budgets?
4. **Parts.** For each part:
   - its units and capacity;
   - **its rank for each resource, fixed from documented properties of access** (Section 4, item 2), or one shared rank if the orders are documented to coincide;
   - its rebuild time, template limit and route back (fixed capital: none);
   - its requirements per unit of work, basal maintenance and renewal;
   - **its reference allocation** (for load);
   - whether it is support for the top;
   - whether it is the intake;
   - whether it is temporary.

   Fix these from independent sources. Anything chosen with the expected outcome in mind is declared fitted.
5. **The repair network.** Its parts (resident and mobile), their capacity and source, their resources and reserves, and their rank.
6. **Links and pathways.**
   - Dependencies (supply edges) and loops.
   - Pathways and their routes (redundancy).
   - Non-bypassable links (severance points).
   - Which parts share the repair network.
7. **Nested systems** (only if the extension in Section 15 is used): list every component treated as a nested system, with the evidence for its own access loop, and its interfaces. **A component not listed here stays a part.**
8. **Modes and gates** (only if access-limited load is claimed): name each governor setting and the process it gates, with independent documentation of the gate. A gate not named here cannot be invoked to explain a shortfall later.
9. **The clock.** Fix the unit in which durations are judged.
10. **Predictions.** Write the generic predictions (Section 10) for this system before looking at outcomes.

## 9. Using the model in reverse

**Unchanged from v0.17, Section 8.**
- Reverse mode starts from what is seen failing and points to where load entered, which parts were absorbing it unseen, and which dependency the failing parts share.
- It suggests where to look; it never names a cause.
- It must distinguish failure clustered by rank from failure clustered by dependency.

## 10. Generic predictions

**As v0.17, Section 9 (G1 to G23),** with these additions and notes:

| No. | Prediction | Layer | Status |
|---|---|---|---|
| G2 (note) | Lower-ranked parts lose access first, in ascending rank | 2 | As v0.17; "supply" read as "access" |
| G3 (sharpened) | With a store carrying the gap and its release not binding, the break comes at the same cumulative shortfall whatever the rate. Where release binds (a tapering store, or a gap above the release rate), faster onset breaks earlier | 1 | Derived (results R4); stress-test candidate |
| G20 (sharpened) | No part loses units while there is somewhere else to take resources from. The top goes last. Failure with willing receivers intact means a cut link **or damage from outside** to the top or its supports | 1 | Derived (results R6); untested |
| G12 (sharpened) | Recovery from small knocks slows before the break when the break is approached through shrinking release headroom (a tapering store, or a gap rising towards the release rate). It does not when the break comes with headroom intact (a store with full release emptying, or a switch) | 1 | **Fails in its first held-out test** (H1 VitalDB, blood loss under anaesthesia, release profile committed as taper; adjudicated 7 October 2026). Weight: fallback cohort, half. Qualifications: runnable only under the pre-data reading of missing bins; step-down inside the fallback cohort not stated in the pre-registration. tests/results/H1-VDB/README.md |
| G24 | **Cascade along substitutes.** Losing some routes of a pathway moves their flow onto the rest; where those saturate, they fail in turn, so failure spreads along the substitutes, not by rank | 1 | Derived (F3); known in power systems; untested as a model prediction |
| G23(b) (sharpened) | **Repair competition, strict rank.** When several parts are damaged at once, those ranked after another damaged part heal more slowly than alone; the highest-ranked damaged part heals as fast as alone | 2 | Derived (results R8); untested. Distinguishable in data from shared repair, in which every damaged part slows |
| G26 | **Partial refill.** In recovery, a store refills only until its marginal value falls to that of the best competing use, so it need not refill to full while parts are still short | 2 | Derived (marginal analysis; theory/PAM_recovery_value_and_viability.md); untested |
| G25 | **Order of sacrifice from access.** Under scarcity, the order in which parts lose adequate supply is predicted by properties of access documented beforehand (constriction under sympathetic drive, autoregulation, redundancy; discretionary budgets) | 2 | Derived (F1); compatible: splanchnic and renal vasoconstriction protecting heart and brain in haemorrhage. **Supported in its first held-out test at half weight** (PT1, English single-tier councils 2014-15 to 2019-20, with statutory duty classified blind as the documented access property; adjudicated 7 October 2026): lines with a statutory duty were protected more than discretionary lines; lines with a duty of uncertain level were not distinguishable from discretionary ones, and that step fails without London (sensitivity only). **The scarcity version (G25-C) was not supported:** the gap did not widen detectably where funding fell more. tests/results/PT1/README.md |

**The standing check (unchanged):** before adding any rule, attempt a complete mapping with the existing parts, resources, stores, ranks, links, boundary, objective and clock. Add a mechanism only after a confirmed qualitative failure in a pre-committed test.

## 11. Status, evidence and working rules

**As v0.17, Section 10,** with three updates:
- **First held-out test:** H1 VitalDB (G12).
  - **Run, and the computation replicated by a second model.**
  - **Computed verdict:** Fails, fallback cohort at half weight. It depends on the reading of missing bins in the stable approach (tests/results/H1-VDB-R1/README.md).
  - **Adjudicated blind by GPT (7 October 2026): Fails, at half weight,** with two stated qualifications (raw/2026-10-07_chatgpt_H1-VDB-ADJ1.md).
  - **Under the standing check:** G12 as mapped for blood loss under anaesthesia has failed once. The first candidate for revision is that mapping (the release profile: taper or switch), not a new mechanism. One failure at half weight does not remove G12. The release-profile question (Tier 2) is now live.
  - **The G1 check in H1 was also not consistent** (10.7% of 75 cases, against more than half), at low weight. The anaesthetist defends pressure, and the check was not decomposed.
- **Second held-out test:** PT1, English single-tier councils, 2014-15 to 2019-20 (fixed against dynamic priority, with G25).
  - **Run, and the computation replicated exactly by a second model** (tests/results/PT1-R1/README.md). Deviations D-1 to D-5 logged, all neutral.
  - **Adjudicated blind by GPT (7 October 2026)** (raw/2026-10-07_chatgpt_PT1-ADJ1.md):
    - **PT1: Inconclusive, full weight.** Projected client growth published before the budget showed no detectable effect on which lines were protected (β = 0.05), but the 95% interval (−0.75 to 0.86) includes the smallest effect that mattered (0.25). Neither fixed nor dynamic priority is earned for this system.
    - **G25: Supported, half weight** (contamination: the broad pattern was known).
    - **G25-C: Not supported, half weight.**
    - **SS (descriptive):** in about 97% of council-years with a fall in spending, some statutory line also fell while discretionary lines kept more than half their 2014-15 total. A coarse measure; it does not show a strict queue at line level.
- **The frozen engine is a reduced form under v0.18.** It writes access as an explicit order of claims. Fixed ranks stand for the network's order of sacrifice. Its other departures from v0.17 (claim order; repair inside each part) stand.
- **The theory-building probes** of 6 October 2026 (salmon, cancer, pregnancy, the power grid, skin circulation) shaped v0.18. **They are not tests:** GPT knew the outcomes, and none counts as support.

## 12. Open questions, tiered

**Tier 1: could threaten the model.**
- **Fixed against dynamic priority.** Does the order of sacrifice reverse with conditions? It is tested by Section 4, item 2: two recipients, one scarce resource, the same time. **First test (PT1, councils, 7 October 2026): inconclusive,** for lack of precision. Still open.
- **Independence of inputs.** Can ranks (now from access), requirements, reference allocations, rebuild times and template limits be fixed independently of the outcome?
- **Out-of-sample prediction.** Does the model predict a new system's order of loss and recovery without fitting it (G25)? **First held-out support at half weight (PT1, councils),** for order of loss only; recovery untested.
- **The three outcomes in held-out data.**
- **G18 in data.**
- **Sensitivity to framing.**

**Tier 2: refining a surviving model.**
- **Collapse or death of the whole system: closed (7 October 2026).** The same criterion applies to the system: death is the loss of every route back (viability theory, Section 6).
- **The release profile** (a knee, or full release until a switch). **Live after H1:** the taper reading failed for blood loss under anaesthesia.
- **The repair network:** resident and mobile kept apart, or one workforce?
- **What starts anticipatory economising;** how the expected frequency of shortfall is learned; what sets a template limit.
- **Harmful inputs:** entered for now as exogenous loss of units or pathway capacity (Section 3, Damage). A mechanism is added only if a pre-committed test fails without one.
- **Governors as modes,** and whether rarity sets which wins.
- **The carried v0.16 mechanisms:** which predictions need them?

**Tier 3: niche or application.**
- the boundary between labelled and unlabelled load;
- whether a dependant's need falls with its supplier's economising;
- institutions growing or re-tuning.
- **Removed:** "objectives at two levels (mother and fetus)", resolved by the placenta as a temporary maternal part.

**For the novelty stage:**
- "No demand, only maintained levels", and the governor as regulation of access, against cascade control, perceptual control theory and allostasis.
  - Broadcast signals with selective receivers are textbook physiology.
  - **The claim to test is the general architecture, not the physiology.**
- Renewal cut before productive work, against Dynamic Energy Budget theory. DEB must be read in full first.
- **GPT's six conditions for a significant contribution:**
  1. formal load;
  2. the governor and parts written formally;
  3. **propositions derived analytically,** not only simulated;
  4. what the model predicts that DEB, allostasis and control theory do not;
  5. held-out tests;
  6. scope and stated failures.

  Items 1, 2 and 6 are in this version; item 3 is new work for the paper.

## 13. Way forward

1. **v0.18 approved** (6 October 2026); the vocabulary frozen again; the probing phase ended.
2. **H1 complete** (7 October 2026; Section 11). Resolve the release-profile question through the standing check.
3. **PT1 complete** (7 October 2026; Section 11): fixed against dynamic priority inconclusive; G25 supported at half weight. A cleaner G25 test (no contamination) and a more precise priority test remain.
4. **The model paper, then a preprint.** Before writing:
   - read DEB and the nearest work;
   - derive the main propositions analytically;
   - keep the Representation Gap paper as the observational half (the pattern and where to measure it).

## 14. Terms

- **Governor:** the function that holds the levels persistence depends on, by regulating access to resources. Allocation is the resulting flow.
- **Access:** what a part can draw, set by the network, its gates and the governor's signals.
- **Rank (πᵣ):** for each resource, the order in which parts lose adequate access when it is scarce; fixed at mapping from documented properties of access. A single "rank" is shorthand where the orders coincide.
- **Part:** a working part (including intake and control), made of units; it has no demand of its own.
- **Repair network:** the repair workforce (resident and mobile), a set of parts whose work is renewing and rebuilding other parts' units; governed like any part.
- **Unit states:** active, switched off, lost, scarred.
- **Part death:** severance of a part's route back.
- **Store:** a stock of one resource, drawn and refilled in order with others of its kind; it does no work.
- **Carrier:** the network that moves resources (blood, lines, supply chains); a resource only where its own stock is short.
- **Load:** resource redirection; the shortfall, per resource, between a part's reference allocation and what reaches it.
- **Damage:** an exogenous loss of units or of pathway capacity.
- **Load flow:** the deficit moving through the system.
- **Load residue:** the state change left by absorbing it; recorded in the state ledger, never added to the resource ledger.
- **Pathway capacity:** the maximum flow from a resource's source to a part (the sum of the routes in the parallel case).
- **Severance:** pathway capacity at zero.
- **Switched off, lost, scar, economising:** as v0.17.
- **Chronic:** a state in which a required restorative process persistently fails to keep pace with the deterioration it must clear, whatever the origin of the load.
- **Access-limited load:** load at a part caused by the governor's setting restricting its access while resources are sufficient; counted only for a gate named at mapping.
- **Exhaustion and severance:** the two routes to system collapse.
- **Viable set:** the states in which the record and the levels it depends on hold; fixed at mapping.
- **Collapse:** outside the viable set with a route back (inside the capture basin).
- **Death:** no admissible route back remains.
- **Time of crisis:** time spent outside the viable set before re-entry.
- **Nested system** (extension): a component with its own loop regulating its own access.
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
6. **First test of the extension:**
   - Classify components by criterion 1 **before** outcomes, across domains (biology, organisations, computing, ecology).
   - Check that those classed as systems behave as systems and the parts as parts.
   - **Discard the criterion if they do not.**
