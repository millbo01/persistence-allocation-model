# The Persistence Allocation Model, v0.20 (9 October 2026)

**Status:** working model (phase 3). Written from James's decisions of 8 and 9 October 2026 (DECISIONS.md, PAM paper and PAM model sections) and checked against **CANON.md**, which governs it. **Approved by James, 9 October 2026: the canonical state.** v0.19 is kept as the record. **Amended 9 October 2026** (James): repair as rising requirement met through access; no part death; arrangement, not intention; a setting includes the governor's response; signal integrity; order from access and requirement; FINAL_CHECK round 1 fixes; corrections after FINAL_CHECK round 2 (changes table, rows 14 to 21).

**What v0.20 is:** v0.19 rebuilt on the seven components of CANON.md, with:
- the protected flow and indicators in place of the record;
- the shortfall in place of load, with no movement language;
- the reduced form in rank order, part by part;
- modes and snapshots;
- the correction to G12 and the new G27;
- the H1 mapping fault named.

Every change from v0.19 is listed in the consolidation notes at the end, with its source.

**Rules carried forward:**
- **CANON.md wins every conflict;** only James edits it.
- **The standing check:** no new mechanism enters unless an existing mapping fails a pre-committed test (Section 10).

**References:**
- **The laws:** CANON.md.
- **The paper:** papers/pam-model/From cells to councils.md (version 2), and its supplement. Propositions 1 to 4 are in the main text; S1.1 to S1.13 are in the supplement.
- **Numerical checks:** scripts/pam_propositions_check.py. The version 2 checks are the reading-B checks; version 1's and the alternative considered are kept as records.
- **Previous canonical state:** theory/PERSISTENCE_ALLOCATION_MODEL_v0.19.md, kept as the record; earlier versions likewise.
- **The worked mapping:** tests/H1 VitalDB G12 - mapping corrected (v2).md.
- **The reference implementation:** theory/sim/tq_units.py (frozen; held privately, not in the public record; its departures are in Section 11).

## Changes from v0.19 (James, 8 and 9 October 2026)

| No. | Change | Source |
|---|---|---|
| 1 | **Seven components** (boundary, governor, parts, protected flow, network, stores, outside input). Only these are components; everything else is a mapping aid | D1; CANON 2 |
| 2 | **Classification rules:** anything that does work is a part; components are roles, not objects; units are not parts; nothing passes between parts; where the governor sets a part's access, it sets it as a whole | D1; CANON 3 |
| 3 | **"Record" retired.** The protected flow (the flow of the resource to the top, against the top's need) is what is maintained; an indicator is whatever an observer watches | D2; Step A answers |
| 4 | **Shortfall, not load;** no movement language. The law is stated as access: at a fixed, fully used inflow, raising one part's access lowers another's | Answers to the v2 reports; CANON 1 |
| 5 | **Rank in two layers** (dependency, then documented access); **modes and snapshots;** the top never changes within a boundary | D3; CANON 4 |
| 6 | **The reduced form in rank order, part by part:** the top, the support parts in full, every other part in full; what reaches a part covers its upkeep first | Answers to reports 19 and 20; CANON 3 and 4 |
| 7 | **The network is routes only;** work moving resource is a part's. Edge cases decided (transporters, xylem, phloem, veins, the carrier, signal tissue, organisations, the intake) | D1; Step A answers |
| 8 | **The governor protects the top by limiting everyone else's access first** (the old "never limits the top's access" withdrawn after Bondar et al. 1995) | CANON 4 as reworded |
| 9 | **G12's derivation found inconsistent with Proposition 2; G27 added.** The H1 mapping fault is named. Verdicts unchanged | Addendum A; D5; D6 |
| 10 | **Economising is a governor mode,** documented like any other, not the default order | Report 20 |
| 11 | **Repair parts** replaced "the repair network" (Step A). Withdrawn on 9 October: see row 14 | Step A answers; report 20 |
| 12 | **Peer cascades** are a requirement dependency named in advance; work not done across the boundary is outside this boundary's ledger | Answers to the v2 reports |
| 13 | **G20 restated:** no part loses units while a lower-ranked part still draws anything | Report 20 |
| 14 | **Repair is work like any other.** Routine repair is part of each part's own draw; damage raises the damaged part's requirement, met within the part's rank; no rule puts repair first or last. Repair parts withdrawn: a producer of a repair resource is a part like the intake, and repair cells at a damaged part are its units. G23 and S1.13 restated | CANON 3 (9 October); James, 9 October |
| 15 | **No part death.** Units are lost for good (scarred) when the losses destroy what rebuilds them or the route back is cut; the system dies, not its parts | James, 9 October (#10) |
| 16 | **Arrangement, not intention.** Wording that gave the governor, parts or system an intention is restated as an arrangement or a consequence | CANON 3 (9 October) |
| 17 | **A setting includes the governor's response** to its sensed levels: opening a damaged part's access is the setting acting, not a change of setting, so damage does not end a snapshot | James, 9 October (CANON 3, reading (a)) |
| 18 | **Signal integrity.** The results assume the governor's signals are true (sensing and command). A system with a signal fault is outside the propositions, and for it the model is diagnostic only (Section 9) | CANON 7; James, 9 October |
| 19 | **Order, access and requirement.** Below the top the order follows from access and requirement; access settings are fixed within a mode; a built-in setting fixes a part's access within its layer; under saturable uptake damage can move a part's place (S1.7) | CANON 3 and 4 (9 October); James, 9 October |
| 20 | **FINAL_CHECK round 1 fixes** (9 October): the fourth exception; settings, modes and built-in access per CANON 3; the dependency lag; G27 reworded; rebuilding after a shortfall is not repair; intake recovery; indicators not counted as tests of the protected flow; the one observation of the protected flow "by a proxy"; rank direction and "approaches strict" | CANON 1, 3 and 7 (9 October); James's rulings J1 to J11 and R1 to R15 |
| 21 | **After FINAL_CHECK round 2** (9 October): the whole-body protected flow named by its resource (the oxygen the brain draws); mean arterial pressure an indicator tracking arterial wall stretch; the top kept out of economising (scope); the engine's order named (reading A); the break as the protected flow failing, with L* the store when the margin is used up (Proposition 3); simulation labels limited to the development engines; opening a gate by the resource it leaves unused; rank fixed in two steps; units, lost units and modes defined per CANON 3; H1's boundary change and qualifications stated; then James's rulings on round 2: the recovery lag; recovery as draws served first and units back by marginal value; the release profile; Hikino logged against G4; G27's wording; a setting defined as a rule, and the threshold switch | CANON 3, 4, 5 and 7 (9 October); James, 9 October; FINAL_CHECK round 2 (papers/pam-model/26) |

## 1. The law and the principle

**The law** (CANON 1, verbatim):

> Under scarcity, allocation is zero-sum. At a fixed, fully used inflow, raising one part's access lowers another's. While no part receives more than it requires, no setting of access reduces the total shortfall; it only decides which parts go short. The exceptions are named: adding resource, lowering what parts require, opening a gate that holds resource back, and taking back what a part receives beyond what it requires. Drawing a store meets the gap now and leaves less for later. Drawing from outside meets it from beyond the boundary.

**The principle** (the central claim, as approved for the paper's version 2):

> In a system that regulates its own persistence, all parts draw on one shared flow of each resource, and each part's access to it is limited separately, by a setting the part does not control. A governor holds the levels the system's persistence depends on by acting through those settings; it protects the top by limiting everyone else's access first. Parts have no demand of their own. Each part works to the limit of the scarcest resource it can draw. When what a part draws falls short of what the reference state requires, whether supply falls, requirement rises or access is restricted, a shortfall is counted at that part. Where the system as a whole is short, the governor draws its stores and turns down the access of lower-ranked parts first, and they switch units off. The protected flow holds until nothing more can be taken: it shows compromise, not stress. At a fixed, fully used inflow, raising one part's access lowers another's: the resource gap is met from stores, met from outside the boundary, or left unmet at a named part, and a shortfall leaves its residue in switched-off, lost or scarred units, or in work not done. A part scales down without harm when its supply falls no faster than it can switch units off and its upkeep is still met; units are lost when supply falls faster, or below its upkeep; the part is scarred, with those units lost for good, only when the losses destroy what rebuilds it or its route back is cut. Repair is work like any other: damage raises the damaged part's requirement, which is met, like any requirement, within the part's rank. Recovery runs the other way: after the top, the support parts' draws, the intake's among them, are served before every other part's; switched-off and lost units, and stores, come back by marginal value (S1.12). The system collapses when the protected flow can no longer be met or a non-bypassable link is cut, and dies only when no route back remains.

**Derived result** (paper, Proposition 1). Two regimes:
- **Scarcity-limited.** Where the flow is fully used and no part receives above its reference allocation, total shortfall is the same under every setting of access at fixed supply, store draw and outside input. Access decides only which parts go short. A correction at one part that adds no resource (from outside or from a store), lowers no part's requirement, opens no gate and takes back no allocation beyond a part's requirement leaves an equal shortfall elsewhere.
- **Access-limited.** Where a gate leaves resource unused, total shortfall rises one for one with the resource left unused, balanced by refill or spill. Opening the gate by the resource it leaves unused removes that shortfall without any other part losing; opening it further is a change of access in the scarcity-limited regime.
- **Neither is an empirical claim.** Both follow from the resource identity. The empirical content is which parts go short, and which regime a system is in.

## 2. Scope

1. **Persistence is a viability constraint.**
   - The governor keeps the system within the states compatible with its continued existence. Within that envelope, the model says nothing about what the parts' work is for.
   - Where other work competes with what persistence requires, that work's access can be turned down: an institution that does not persist does no work at all.
   - The model describes the dynamics while persistence is being governed. It does not claim that a system's own settings can never end it.
2. **Terminal reproductive programmes are out of scope** (semelparous salmon, males of some dasyurid marsupials, monocarpic plants). The model should work before the reproductive switch and fail after it.
   - **A counterexample** would be an ordinary system, in ordinary conditions, whose own regulation destroys recoverable viability with no higher-level system being protected.
3. **The model is not a theory of action selection.**
4. **No redrawing after a counterexample.** The boundary, the top, the protected flow and the classification of components are fixed at mapping (Section 8). Changing them after an outcome is seen is a fitted change.
5. **A scenario is a load applied to a system, not a system** (CANON 5).
6. **Signal integrity** (CANON 7). The results assume the governor's signals are true: what it senses matches the real levels, and the access it sets is put into effect; the realised flow may still be limited by the network (S1.9). A system with a signal fault is outside the propositions; for it the model is diagnostic only (Section 9).

## 3. The seven components

| Component | What it is |
|---|---|
| **Boundary** | Fixed first. It decides everything else, including which part is the top |
| **Governor** | A set of targets on sensed levels. If a level crosses its threshold, the governor acts until it returns. It owns the signals and does no work. Its sensing and signalling are carried out by parts, which pay their cost. It is a function, not a place. The results assume its signals are true, in sensing and in command (Section 2, item 6) |
| **Parts** | Anything that does work. Parts have no demand of their own. Each part has a rank, fixed in two steps: its dependency layer, then its order within the layer (Section 4, item 2). One part is the top: the part everything else is sacrificed to keep going |
| **Protected flow** | The flow of the resource to the top, which has to be maintained, and is being maintained, at all costs, measured against the top's need |
| **Network** | The routes the resource moves along |
| **Stores** | They hold resource and release it |
| **Outside input** | Resource or energy from across the boundary |

**Everything else is a mapping aid, never a component.** That covers units and their states, the reference allocation, the shortfall, the two ledgers, the gap, the margin, rank detail, modes and gates, economising, repair, templates and scars, viability and the capture basin.

**Classification rules** (CANON 3).
- **Work.** If it does work, it is a part. That includes work done on the governor's signal: the signal is the governor's, the work is the part's. Parts pay the cost of signalling.
- **Roles.** Components are roles, not objects. One structure can play two roles: a vein is a route, and the blood in it is a store.
- **Indicators.** An indicator is whatever an observer watches. It may be the protected flow, a level the governor holds, or neither. Never assume which.
- **One shared flow.** Nothing passes between parts. No work or shortfall is handed from one part to another. Resource moves only through the shared flow and its routes, and one part's state changes another's only through a dependency or through the physics of the network (S1.10). All parts draw on one shared flow of each resource, and each part's access to it is limited separately. Parts do not set their own access; a part that does, such as a tumour, is a separate case (Section 15). Access is either set by the governor or built into the part or route, and both kinds of setting are fixed within a mode. A setting is the rule that gives a part's access at each sensed level, so a part's access can change within a mode while its setting does not. A built-in setting is not set by the governor: it fixes the part's access within its layer, and a change in the part's requirement can move its place in the order. The governor's regulation works through stores, intake, gates and the settings it does control; where it sets a part's access, a change in requirement changes that part's draw in its own turn, not its place. When a sensed level crosses its threshold and the governor acts, as in opening a damaged part's access where it sets that access, the setting is acting, not changing: access changes and the order does not. A mode change is a change in the order, or in which levels the governor holds, other than through built-in access. It ends the snapshot. A shortfall is a count at a part, not something that moves.
- **Units.** What a part is made of are its units (cells in an organ, staff in a department), not parts. Units take their part's access. Which units within a part go first is a mapping aid. Work is counted once, at the part.
- **Access as a whole.** Where the governor sets a part's access, it sets it as a whole. It does not split a part's draw between upkeep and work: what reaches a part covers its upkeep first, then its work.

**The governor.**
- **What it holds:** targets on sensed levels: the levels the protected flow depends on, and the levels the stores and supports depend on.
- **What it acts through:** it sets access:
  - releasing, filling and spilling stores;
  - opening and closing intake;
  - the capacity of routes and gates;
  - the access of each part whose access it sets, including a damaged part's.
- **What it does not do:**
  - It does not set allocations, which are the resulting flow.
  - It does not switch units off. Units switch off when what reaches their part falls short.
  - Explicit allocation (a budget line, a rota) is one way of setting access.
- **How it acts:** largely by broadcast. A signal reaches many parts and routes, and each responds by rules encoded locally. Tissue that makes or carries the signal does work, so it is parts.
- **Where it sits:** it is a function, not a place, so two regulators that can each take control are two modes of one governor function (Section 4, item 3).
- **How it protects the top:** by limiting everyone else's access first. The top's own routes can still narrow (Bondar et al. 1995). The reduced form simplifies this away, and the finding is logged against the model (Section 11).

**Parts.**
- **What they are:** simple processors. A part does the work only it can do, to the limit of the scarcest resource it can draw.
- **Requirement.** Parts have no demand of their own: what a part requires is set by a rule fixed in advance (its reference), which rises only as that rule provides: under a load applied to the system, with damage, or through a documented requirement link, never because the part asks. The governor sets access, never requirement.
- **Units:** a part is made of units. Elements that duplicate each other and share resources are units of one part; elements in series are separate parts.
- **Unit states:**
  - **active;**
  - **switched off:** the unit keeps its route back, receives basal maintenance (upkeep) only, and does little or no work;
  - **lost:** gone, but rebuildable from what is left once every part has drawn;
  - **scarred:** lost for good, because the losses destroyed what rebuilds it or its route back is cut.
- **Capacity** is active units, scaled by any dependency on another part's work.
- **Route back:** the template, the supply of what rebuilding needs, and the reconnection. Units whose route back is cut are scarred. Parts do not die; the system does (Section 6). Fixed capital has no route back.
- **Temporary parts** may appear for a period and take a rank when they do.
- **The intake** is a part (absorption is its work) and ranks with the support parts.
- **Repair** is work like any other (CANON 3).
  - **Routine repair** (renewing worn units) is part of each part's own draw, so it falls when that part's access falls.
  - **Damage** from outside removes units or route capacity and raises the damaged part's requirement (rising requirement). The governor meets it as it meets any requirement: by opening that part's access, where it sets that access, and releasing stores into the flow, within the part's rank. Local signals that open a damaged part's access belong to the governor. The part's response to what arrives is a consequence. Under saturable uptake, raised requirement also raises the part's adequacy threshold (S1.7), so damage can move the part's place in the order. Where the governor sets access, a raised requirement enlarges the part's draw in its own turn and does not move its rank. The model contains no damage mechanism.
  - **Producers and repair cells:** a part whose work produces a resource that repair needs (for example, bone marrow) adds it to the flow, like the intake. Repair cells working at a damaged part are counted at that part, as its units.
  - **Units lost to a shortfall are not damage, and rebuilding them is not repair:** it is paid from what is left once every part has drawn.
  - **No rule puts repair first or last.**

**The protected flow and indicators.**
- The protected flow is measured against the top's need, fixed in advance.
- Proposition 2 concerns the protected flow only; it says nothing about indicators in general.
- Where an indicator is a level the governor holds, the governor's action holds it while its levers last. A formal statement of that is a candidate only (Section 12).
- *Terminology:* in the author's earlier institutional framework, "record" meant what institutions measure; that corresponds to an indicator here.

**The network.**
- **Routes only.** Work that moves resource along a route is a part's work: a heart pumping, an energy-spending transporter (the receiving part's work), loading and unloading in phloem, the finance function moving money.
- **What counts as a route:** a channel or passive carrier, the xylem, sieve tubes, vessels, and budget lines in organisations.
- **A drive no part makes** (evaporation driven by the sun) is outside input.
- **The carrier:** name the resource, never its carrier or its route (CANON 5). In blood loss the resource is oxygen; blood is its carrier and the vessels are its route.
- **Route capacity** is the maximum flow from source to part. Severance is that capacity at zero; constriction is above zero but below need.

**Stores.**
- **Release:** in proportion to content by default (DEB), or full until empty. The profile may depend on the governor's mode, and is fixed at mapping.
- **Refill and spill:** of the flow left undrawn, a share refills the stores and the rest is spilled.
- **What a store is not:** a part. It does no work.

**Outside input.** Resource or energy drawn from across the boundary. Whether outside support is admissible decides collapse against death (Section 6), and is fixed at mapping.

## 4. The reduced form, and what the governor does

1. **The ordered draw** (each resource, each step). Where the network is not modelled explicitly, the flow is written as an ordered draw. The flow available is $S_r=U_r+I_r+\sum_sd_s$. Parts draw from it in a fixed order $\pi_r$, each up to its full draw:
   1. the top's full need;
   2. the support parts' full draws, in rank order (parts the top depends on, and the intake);
   3. every other part's full draw, in rank order;
   4. what is left: reactivation and rebuilding against refilling the stores, by marginal value (item 5).

   **The arithmetic of the draw:**
   - Each part is drawn in full in its turn.
   - What reaches a part covers its upkeep first, then its work and renewal. So a part that is short loses work before upkeep, and the lowest-ranked part is cut fully before the next is touched.
   - What a part does not draw stays in the flow; nothing is returned.
   - A requirement raised by damage is met within the damaged part's rank, because the governor, where it sets the part's access, opens that access in response to local signals of the damage. Units lost to a shortfall are not damage, and rebuilding them is not repair. They are rebuilt from what is left: rebuilding them is not part of the part's draw, so it competes for the surplus by marginal value as supply returns (S1.12).
   - The ordered draw is the arithmetic of the access settings, not a queue: a part's place in it is its priority, not its location.
   - **Where the network is known,** it replaces the ordered draw.
2. **Rank.**
   - **Two steps.** First comes the dependency layer, from the top down: the top, then the parts whose work feeds the top, then the parts that feed those. Second, within a layer, the order comes from documented access and, where access is built in, from requirement.
   - **Depth:** the reduced form keeps one support layer. Deeper layers extend the order, and the propositions are not claimed for that case.
   - **Per resource:** each resource has its own order $\pi_r$. Where the orders coincide, a single "rank" is shorthand, and the mapping says so.
   - **Under joint scarcity:** where complementary resources bind together and their orders conflict, ordinal ranks do not decide the outcome (paper S1.2), and the network must be mapped.
   - **How it is fixed:** at mapping, from documented properties of access and, where access is built in, from the rules for requirement. Examples: constriction under sympathetic drive; autoregulation; redundant routes; under saturable uptake, the adequacy threshold $C^\ast=K^{\mathrm M}\eta/(1-\eta)$ with $\eta=q^0/V$ (S1.7); statutory duty or discretionary status.
   - **It is never read off the observed order of loss.**
   - **Strict or shared:** under saturable uptake, priority approaches strict where neighbouring thresholds are far apart (S2), and parts go short together where they are close.
3. **Modes and snapshots.**
   - **The top never changes within a boundary.** Below it, the order follows from access and requirement. Access settings are fixed within a governor mode and change only when the mode changes. A setting acting changes access, not the order; a mode change is a change in the order, or in which levels the governor holds, other than through built-in access.
   - **Documentation:** modes are documented independently, before outcomes.
   - **One mode at a time:** the model applies to one mode at a time, which is a snapshot. A threshold switch (decompensation in blood loss) is a mode change: crossing its threshold changes the order, or which levels the governor holds, and ends the snapshot.
   - **Access-limited shortfall:** a mode that opens one class of work and closes another is the source of it (Section 6).
   - **The open question (Tier 1):** do access settings change when the mode changes, and only then? Under built-in access, a requirement that rises by its rule can move a part within its layer; the move is computed in advance (S1.7). A valid test needs two recipients competing for the same scarce resource at the same time, with the mode documented, comparing the order within one mode and across a change of mode.
4. **Economising** is a governor mode, documented in advance like any other, in which every part below the top and its supports has its access lowered by the same share of its work draw. Work is cut evenly while what reaches each part still covers its upkeep first. Economising lowers access, not the reference; what goes unmet is still counted as shortfall.
   - **It is not the default order.**
   - **It causes no unit loss at any speed,** because work is cut, not renewal.
   - **Its saving** arrives at once for work and wear, and as units are switched off for their baseline renewal (S1.4).
   - **Realisation:** consolidation (units switched off) is the default; a mapping may declare a throttled share.
5. **Recovery by marginal value.**
   - After the top, the support parts' draws, the intake's among them, are served before every part outside the supports. Switched-off and lost units, and stores, come back from what is left: each unit of surplus goes to whichever is worth more, a unit of store or a unit of a part.
   - **Not derived:** that parts come back first after a short episode, and stores after a long one, is prediction G10, untested; S1.12 gives only the refill level.
   - **A store refills only to a critical fractile** of past episode depths while parts are still short (G26; S1.12).

## 5. What a part does with what reaches it

1. **Upkeep first, then work.** What reaches a part covers its upkeep (basal maintenance, for active and switched-off units) first, then its work and renewal.
2. **Work** is the minimum of active capacity and, for each required resource, what reaches the part for work divided by its requirement (the law of the minimum). The synthesising-unit form is the smooth general case. What the part cannot use stays in the flow.
3. **Renewal** is a baseline per active unit plus wear per unit of work.
4. **Units change only through supply:**

   | What is short | What happens | Kind |
   |---|---|---|
   | Work | Units are switched off (consolidation), or held active below capacity where the mapping declares a throttled share | Switched off, or throttled |
   | Renewal | Units that cannot be renewed are switched off, up to the part's switch-off rate; the rest fail and are lost | Switched off: orderly. Lost: disorderly |
   | Upkeep (only once work is cut to nothing) | The part pays the unmet upkeep from its own units, so it shrinks (S1.3) | Lost |
   | Nothing (supply returns) | Switched-off units are reactivated at a limited rate and cost; lost units are rebuilt from what is left once every part has drawn, unless scarred | Coming back |
5. **Scar.** Losses in one episode beyond the part's template limit are scarred, as are units whose route back is cut. Fixed capital is scarred by any loss.

**Rate decides harm** (S1.8). A fall in renewal no faster than the switch-off rate loses nothing at any depth. A faster fall loses units; with the route back intact, a scar needs both speed and depth, and the threshold depth falls as speed rises.

**Rising requirement** (S1.6). Work rises within active capacity, then switched-off units are reactivated at a limited rate and cost. Output falls short only when the rise outpaces reactivation, reactivation cannot be paid for, requirement exceeds total capacity, or what reaches the part at its turn falls short of the raised requirement. Requirement that rises when another part's work falls counts only for a requirement link documented in advance (Section 6).

## 6. Shortfall, ledgers and how systems fail

**Shortfall, defined.**
- **The reference allocation** $q^0_{ir}$ is fixed at mapping as a rule, and never lowered because units have switched off.
- **The shortfall** is $\ell_{ir}=[q^0_{ir}-a_{ir}]_+$. It is a vector, one value per resource.
- **If a part switches units off,** the shortfall has not vanished: it is still counted against the fixed reference.

**Two ledgers, kept apart.**
- **The resource ledger** (per resource). In the scarcity-limited regime (the flow fully used, no part above its reference), the gap $\Gamma_r=\sum_iq^0_{ir}-U_r$ equals store draw plus total shortfall plus outside input; in general, resource left unused and allocation above reference enter as well (Proposition 1). Every unit of the gap is met from a store, met from outside, or left unmet at a named part.
- **The state ledger.** It records what a shortfall leaves behind: units switched off, lost or scarred, and work not done.
  - **Work not done that falls on another system, across the boundary,** is outside this ledger and belongs to that system's mapping.
  - **Residue is a consequence of shortfall** and is never added to the resource ledger.

**Three origins of shortfall:**
- falling supply;
- rising requirement;
- a governor mode that restricts access while resources suffice.

**Guards:**
- **Access restriction:** it counts only for a mode and a gate documented independently and named at mapping (Section 8).
- **Rising requirement traced to another part:** it counts only for a requirement link documented at mapping. A part whose requirement rises when another part's work falls depends on that part's work; nothing passes between them.
- **Requirement raised by damage:** its rule is fixed at mapping with the reference allocation, and it counts only for damage documented independently.
- **Vacancy debt:** most of it sits inside one part. Staff are units, a vacancy is a lost unit, and the team's requirement is unchanged.

**Chronic.** A part's shortfall is chronic when it recurs, over the period that matters, faster than the part can rebuild what it leaves behind.

**Two real chains.**
- **Dependency.** A support part's shortfall lowers its work, and with it the delivery that depends on that work. The new shortfall is counted at each dependent part.
- **Network physics.** Where flow divides by physics, losing or narrowing a route raises flow on the others. A surviving route can be overloaded, or flow drawn from another part's branch (steal), even with spare total capacity. Where flow is placed by access settings, this happens only when total spare capacity is short. Overloaded routes fail in turn (G24; S1.10).

**Order of exhaustion.**
- Parts are cut from the lowest rank up, each fully (work, then upkeep) before the next is touched.
- **In steps whose support parts were met in the step before, and in which no unit of the top or a support part is still coming back from an earlier shortfall, no part loses units while a lower-ranked part still draws anything, and the top goes last** (G20; Proposition 4). Where the supports were not met, the top can be short while every other part draws in full: the dependency lag, counted at the top, not a break in the order. Where units of the top or a support part are still coming back, the same can happen: the recovery lag, not a break in the order either. In both, the earlier shortfall must be observed.
- Severance of a non-bypassable link stops the protected flow, and constriction lowers it below need, while stores hold and other parts are funded (S1.9).

**Collapse and death** (viability theory; S1.11).
- **The viable set** is the states in which the protected flow and the levels it depends on hold.
- **Collapse:** outside the viable set, with a route back (inside the capture basin).
- **Death:** no admissible route back.
- **Outside support:** whether it is admissible is fixed at mapping. The same state can be collapse with it and death without it.

## 7. Read-outs

- **The protected flow,** against the top's need.
  - It is met while $S\ge N$, in steps whose support parts were met in the step before and in which no unit of the top or a support part is still coming back from an earlier shortfall; the support parts are met while $S\ge N+P$.
  - Where the support parts were not met in the step before, the top can be short while every other part draws in full (the dependency lag).
  - Where units of the top or a support part are still coming back from an earlier shortfall, the same can happen (the recovery lag).
  - It holds while $\Gamma\le\sum_sd_s+I+M$, with $M=P+D$ without the delivery dependency and $M=D$ with it (Proposition 2).
  - It breaks at two thresholds: at once, and one step later through the dependency.
- **Store when the margin is used up:** $L^\ast=(\Gamma-M)/k$ under proportional release; the break comes in that step without a delivery dependency, and one step later with one (Proposition 3).
- **The G27 window:** the steps between the store's release headroom running out ($L_w=\Gamma/k$) and the break. During them, fluctuations in the gap show in the access of parts below the top, lowest-ranked first (G27). Its length is $T_{\text{lead}}\approx\ln\big(\Gamma/(\Gamma-M)\big)/\big(-\ln(1-k)\big)$ (S1.1, read in version 2's terms), one step more with a delivery dependency.
- **Indicators,** each classed at mapping as the protected flow, a level the governor holds, or neither.
- **State signals:** active, switched-off, lost and scarred units per part; store levels; the repair backlog.
- **Co-movement (G18):** parts sharing a dependency that is short move together before the break.
- **The three outcomes** (switched off, lost, scarred), told apart by what comes back and how fast (G19).
- **The ledgers** (Section 6); **time of crisis;** **cost of restoration.**

## 8. Mapping a system

**Do this before opening any outcome data, in CANON 5's order:** the boundary first, then the top and the protected flow, then everything else. Never work backwards from a scenario, an outcome or a data set, and never choose the top, the protected flow or an indicator because a data set happens to record it. Use the fewest components that do the job.

1. **Boundary, top and protected flow.**
   - Fix the boundary first.
   - Name the top (the part everything else is sacrificed to keep going) and the protected flow (the flow of the resource to the top, against the top's need). Declare the currency.
   - Fix the viable set, and whether outside support is admissible.
   - Where the top's work is an early stage of a longer pathway, fix whether viability requires the early output, the downstream completion, or both.
2. **Resources and stores.**
   - Which resources does work need, and in what ratio?
   - Are they complementary? Substitutable inputs are mapped as one resource, or declared.
   - Which routes do they move along?
   - Which stores, with what release profile and turnover?
   - What can be spilled?
3. **The governor and its targets.**
   - Which levels does it hold, and with what targets?
   - What does it act through?
   - Which indicators will be watched, and what kind is each?
4. **Parts.** For each part:
   - its units and capacity;
   - its rank for each resource (dependency layer, then, within the layer, documented access and, where access is built in, requirement);
   - under saturable uptake, $K^{\mathrm M}$, $V$ and $q^0$ (S1.7);
   - its rebuild time, template limit and route back;
   - its upkeep and its requirements per unit of work and renewal;
   - its reference allocation;
   - whether it is a support part, the intake, or temporary.
5. **Repair:** routine repair is in each part's renewal requirement (item 4). Damage raises the damaged part's requirement, met within its rank. Name any part whose work produces a resource that repair needs, with its rank, as for the intake. Repair cells at a damaged part are counted at that part.
6. **Links and routes:**
   - dependencies;
   - requirement links;
   - routes and redundancy, and whether flow divides by physics or is placed by access settings;
   - non-bypassable links.
7. **Nested systems:** only if Section 15 is used. List every part treated as a nested system, with evidence for its own access loop. A part not listed stays an ordinary part.
8. **Modes, gates and requirement links:** only if access-limited shortfall or a requirement link is claimed. Name each with independent documentation, before outcomes.
9. **The clock.**

**The bias ledger.** Before looking anything up, score the interpretive freedom of each mapping choice from 1 (forced) to 5 (open):
- the boundary;
- part classification;
- the resource;
- rank;
- the reference state;
- the prediction.

Coin-flips are marked as ambiguous and cannot be resolved afterwards in the model's favour.

**The worked example:** tests/H1 VitalDB G12 - mapping corrected (v2).md.

## 9. Using the model in reverse

- **What it does:** reverse mode starts from what is seen failing. It points to where the shortfall began, which parts' access was turned down unseen, and which dependency the failing parts share.
- **It suggests where to look; it never names a cause.** It generates hypotheses and is not evidence. It corrects for what is visible, and names a set, not a cause.
- **It must tell two kinds of failure apart:** failure clustered by rank from failure clustered by dependency.
- **Signal faults** (CANON 7). Used in reverse, the gap between what a governor with true signals would do and what is observed points to where a signal failed:
  - a false alarm: access cut while the flow is ample, with no documented mode;
  - a missed alarm: the order broken, with a higher part short while a lower part still draws, and no part it depends on short in the step before; a documented dependency lag, or a recovery lag (units of the top or a support part still coming back after an earlier shortfall), is not a fault, but the earlier shortfall must be observed, not inferred from the later one (with true signals, S1.9 traces the same pattern, for the top or a support part, to a cut or narrowed link, or outside damage; reverse mode keeps both in the set);
  - a setting not carried out: a part's access not matching the setting commanded (like the missed alarm, it must be told apart from a narrowed route, S1.9).
- **The guard:** a signal fault is never a rescue. It can be named only if it is documented independently, or logged in advance as a candidate and then checked. The access guard (Section 6) applies as well.

## 10. Generic predictions

**Layers:** layer 1 is what any feedback loop that holds a flow by drawing a finite store would be expected to show; layer 2 needs selection or design.

**Evidence labels:** derived; simulation result in a development engine (version 1's order or earlier) (paper, S4); natural-system observation; compatible; direct test; not yet tested.

| No. | Prediction | Layer | Status |
|---|---|---|---|
| G1 | The protected flow stays at the top's need while lower parts and stores move. It holds while the gap is no larger than what the stores release, plus outside input, plus what can go unmet below the top | 1 | Derived (Proposition 2); simulation result in a development engine (version 1's order or earlier). Natural observations of held indicators do not test G1. The one observation of the protected flow (by a proxy; Bondar et al. 1995) fell before the break and is logged against the model. H1 check (on an indicator) not consistent, low weight |
| G2 | Lower-ranked parts lose access first, in ascending rank | 2 | Derived (Proposition 4). Compatible: calibrated haemodynamic models. Krieger (1921) logged against, not yet weighed |
| G3 | With a store meeting the gap and its release not binding, the break comes at the same cumulative gap whatever the rate to within one step's gap (Proposition 3); with a delivery dependency, the cumulative gap at the break is larger by one step's gap, so it rises slightly with the rate. Where release binds (a tapering store, or a gap above the release rate), faster onset breaks earlier. Under proportional release, the margin is used up when the store left is (gap minus margin) divided by the store's turnover rate, so a larger gap per step leaves more of the store unused, rising linearly with the gap; the break comes then, or one step later where delivery to the top depends on the support parts | 1 | Derived (Proposition 3). Not yet tested; indicator-defined events in sheep and trees fit the first clause, and no break of the protected flow was observed |
| G4 | A larger store gives a longer silence; a depleted start breaks sooner | 1 | Derived (Proposition 2). Natural observations of indicator-defined events fit; they do not test the protected flow. Hikino et al. (2026) logged against, not yet weighed |
| G5 | A part whose access is cut loses work, then upkeep, and with them units (switched off first, lost if supply falls too fast). Loss begins at the lowest-ranked part; each part above it goes short only once the part below has nothing | 1 and 2 | Derived (Proposition 4, S1.8) |
| G6 | After the top, the support parts' draws, the intake's among them, are served before every part outside the supports, and their switched-off and lost units come back by marginal value; the protected flow recovers before the state does | 2 | Not yet tested. The kidney observation is of an indicator, so it does not test the protected-flow clause |
| G7 | Fixed capital keeps what it loses; renewable parts rebuild lost units, except scarred ones | 1 | Simulation result in a development engine (version 1's order or earlier); natural observation: consistent |
| G8 | Rate decides harm; with the route back intact, a scar needs speed and depth | 1 | Derived with bounds (S1.8); simulation result in a development engine (version 1's order or earlier). Not yet tested |
| G9 | Re-tuning to a past threat | 2 | Carried from v0.16, not re-examined; excluded from the paper |
| G10 | After a short episode parts come back before stores; after a long one stores come first | 2 | Natural observation: consistent; qualitative unless costs are mapped (S1.12) |
| G12 | Recovery from small knocks slows before the break where release headroom shrinks | 1 | **Fails in its first held-out test** (H1, half weight; two qualifications: runnable only under the pre-data reading of missing bins, and the step-down inside the fallback cohort not stated in the pre-registration). **Its derivation put the warning in the protected flow, which Proposition 2 says is silent; H1 measured an indicator. Replaced by G27.** The verdict stands |
| G13 | The lowest-ranked part goes short first and is cut fully before the next is touched; it stays short longest where its value in recovery is also lowest | 2 | Derived (S1.5) |
| G14 | Peak-referenced protection | 2 | Carried from v0.16; excluded from the paper |
| G15 | Store memory | 2 | Carried from v0.16; excluded from the paper |
| G16 | Economising is a governor mode in which every part below the top and its supports has its access lowered by the same share of its work draw; it causes no unit loss at any speed; it is not the default order. The top is kept out of economising; whether a top cuts its own work is left to a later version (paper, S1.4) | 2 | Derived (S1.4); simulation result in a development engine (version 1's order or earlier) |
| G17 | Economising and growth compete | 2 | Carried from v0.16; excluded from the paper |
| G18 | Parts sharing a dependency that is short move together before the break; parts clustered only by rank do not | 1 and 2 | Simulation result in a development engine (version 1's order or earlier). Not yet tested (H1's exploratory G18 paired one part's outputs with an indicator, so it was not a test) |
| G19 | Three outcomes (switched off, lost, scarred) can be told apart by what comes back and how fast | 1 | Simulation result in a development engine (version 1's order or earlier). Not yet tested |
| G20 | With routes intact and no outside damage, the support parts met in the step before and no unit of the top or a support part still coming back, no part loses units while a lower-ranked part still draws anything, and the top goes last. Failure while a part outside the top and its supports is still supplied, under the same conditions, means a link cut or constricted below need, or outside damage. Where the supports were short in the step before, the top can be short while every other part draws in full (the dependency lag); where units of the top or a support part are still coming back, the same can happen (the recovery lag) | 1 and 2 | Derived (Proposition 4; S1.9). Not yet tested |
| G21 | The law of the minimum | 1 | Simulation result in a development engine (version 1's order or earlier). Known (Liebig); general form in DEB |
| G22 | The intake coasts; at refeeding its draw, as a support part, is served before every part outside the supports, and its units come back by marginal value | 2 | Derived (S1.12) |
| G23 | Repair is work like any other: damage raises the damaged part's requirement, met within the part's rank. (a) Under a sustained shortfall, a damaged part's raised requirement goes short in rank order like any other, so repair slows; this is a consequence, not a rule. (b) Strict rank: with a limited repair resource as the flow, when several parts are damaged at once, those ranked after another damaged part heal more slowly than alone; the highest-ranked damaged part heals as fast as alone. (c) An acute threat leads to store release on a sensed level before damage occurs; this is not a mode | 2 | (a), (c) compatible with the earlier statement, not re-weighed; (b) derived (S1.13). Not yet tested |
| G24 | Cascade along substitutes where flow divides by physics, even with spare capacity | 1 | Derived (S1.10). Not yet tested as a cross-domain prediction |
| G25 | The order of loss is predicted by properties of access documented beforehand | 2 | **Supported in its first held-out test, half weight** (PT1). **G25-C (the scarcity version) not supported, half weight** |
| G26 | Partial refill to a critical fractile of past episode depths | 2 | Derived (S1.12). Not yet tested |
| G27 | As the break approaches, fluctuations in the gap show first in the store's release while it has headroom, then in the access of the lowest-ranked part still supplied, then in each part above it in turn, and in the protected flow only at the break. A test of G27 needs a system whose final store tapers | 1 and 2 | Derived (Propositions 2 and 4; window S1.1). Not yet tested. Added in v0.20 |

**Log of this section:**
- **9 October 2026 (v0.20), G12:** the H1 mapping fault is now named. The derivation put the warning in the protected flow; H1 measured an indicator (mean arterial pressure, which tracks a level the governor holds: the stretch of the arterial wall at the carotid sinus and aortic arch, sensed by the baroreceptors); the mapping committed a store that tapers as it empties, possibly ending in a switch; the pre-registration named the release profile as the first candidate for revision. Corrected, post hoc, in tests/H1 VitalDB G12 - mapping corrected (v2).md, which also redraws the frozen boundary (the patient's circulation plus the anaesthetist) to the patient, with the anaesthetist as an outside loop. The verdict is unchanged.
- **9 October 2026 (v0.20), G27:** added, untested. G5, G13, G16, G20 and G23 restated for the rank-first order.
- **9 October 2026 (amendment), G23:** restated with repair as work like any other; (a) is a consequence, (b) is S1.13 with a limited repair resource as the flow, (c) is store release on a sensed level. G1, G7, G20 and G26 reworded (arrangement, not intention; scar).

**The standing check:** before adding any rule, attempt a complete mapping with the existing components and mapping aids. Add a mechanism only after a confirmed qualitative failure in a pre-committed test.

## 11. Status and evidence

- **H1 (G12):** Fails, half weight, with two qualifications: runnable only under the pre-data reading of missing bins, and the step-down inside the fallback cohort not stated in the pre-registration.
  - The G1 check is not consistent, low weight.
  - The exploratory G18 is reported in full (paper, S5.1).
  - The mapping fault is named (Section 10).
- **PT1:**
  - the primary question (fixed against dynamic priority) is Inconclusive, full weight;
  - G25 is Supported, half weight;
  - G25-C is Not supported, half weight.
- **Logged against the model:** in simulated blood loss, blood velocity in the middle cerebral artery (a proxy for the brain's blood flow, which tracks the oxygen the brain draws only while the share it extracts is unchanged) fell by 27% at presyncope, with arterial pressure unchanged, while the brain's estimated vascular resistance rose (Bondar et al. 1995).
  - It is the one observation of the protected flow (by a proxy), and the top's own routes narrowed.
  - The candidate explanation (lower carbon dioxide narrowing the brain's vessels) is uncited until a source is checked.
  - A second candidate (as flow falls, the brain drawing a larger share of the oxygen reaching it) is logged and not yet checked; until it is checked against a source that measured the brain's oxygen extraction or oxygenation up to presyncope, the finding counts against the model (paper, S7.3).
  - The top is fixed by the boundary, so the finding is not a reason to move the top.
- **The frozen engine** (theory/sim/tq_units.py) departs from v0.20:
  - **Claim order:** it funds the support parts in full, then every other part's upkeep, then their work. That is the alternative order considered and not adopted (reading A).
  - **Repair:** it renews inside each part, which matches routine repair here; it has no damage (below).
  - **Access:** one rank for all resources.
  - **Forms:** the knee and the earlier unit-loss rule.
  - **Not in the engine:** the reference allocation and ledgers, route capacity, damage, a cut route back.
  - **What follows:** results that depend on these are engine artefacts.
- **Natural-system checks and probes** are compatible observations, not tests.

## 12. Open questions, tiered

**Tier 1: could threaten the model.**
- **Mode and order.** Do access settings change when the mode changes, and only then? PT1's primary question was inconclusive. Straub's chronic case, the immune system as a standing claimant that changes the order, belongs to this question.
- **The protected flow before the break.** The one observation of it (by a proxy) fell (Bondar et al. 1995).
- **Independence of inputs.** Can the top, the protected flow, ranks, requirements and reference allocations be fixed independently of the outcome?
- **Out-of-sample prediction** (G25, G27) and the three outcomes in held-out data (G19).

**Tier 2: refining a surviving model.**
- **The release profile:** proportional, a knee, or full release until a switch.
- **Repair resources:** which parts produce a resource that repair needs, and their rank in each mapping.
- **Modes:** what starts the economising mode, and what sets the expected frequency of shortfall.
- **Governors as modes,** and which wins when two are signalled at once.
- **The cascade rule** (G24).
- **Deeper dependency layers** in the reduced form.
- **Candidate proposition, words only:** a level the governor holds stays in its band while some lever acting on it has headroom, and leaves it only when every such lever is at its limit. It needs a model of the governor's levers. Check the literature on control with actuator saturation and anti-windup first.

**Tier 3: niche or application.** Requirement links in institutions; institutions growing or re-tuning; signal faults, including by design in institutions, located against the baseline of a governor with true signals.

## 13. Way forward

1. **The paper's version 2:** approved by James on 9 October 2026 and frozen; the final check (FINAL_CHECK.md) is run in full before release; then Step D (release v2.0 and the SSRN revision, both by James).
2. **A G27 test** in a system whose final store tapers, mapped before opening. Settings where the governor's own reflexes are intact are preferred (for example, awake volunteers under lower-body negative pressure). This is test selection, not an explanation of H1; the verdict stands.
3. **A cleaner G25 test,** and a test of mode and order.
4. **The journal version,** derived from version 2, after its release.

## 14. Terms

- **Boundary, governor, parts, protected flow, network, stores, outside input:** the seven components (Section 3).
- **Top:** the part everything else is sacrificed to keep going; fixed by the boundary.
- **Indicator:** whatever an observer watches: the protected flow, a level the governor holds, or neither.
- **Access:** what a part can draw; set as a whole per part by the governor, or built into the part or route.
- **Rank ($\pi_r$):** the order of priority for $r$; parts lose adequate access to $r$, when $r$ alone is scarce, in the reverse order. It is fixed in two steps (the dependency layer, then, within a layer, documented access and, where access is built in, requirement); access settings are fixed for a snapshot.
- **Mode:** a state of the governor that fixes the access settings it controls and which levels it holds; a mode change is a change in the order, or in which levels the governor holds, other than through built-in access. **Snapshot:** one mode. A threshold switch is a mode change: crossing its threshold changes the order, or which levels the governor holds.
- **Signal fault:** the governor sensing a false level, or a setting not carried out (CANON 7). It puts a system outside the propositions.
- **Support parts:** parts whose work feeds the top, and the intake.
- **Repair:** work like any other. Routine repair is part of each part's own draw; damage raises the damaged part's requirement, met within its rank.
- **Unit states:** active, switched off, lost, scarred (lost for good: the losses destroyed what rebuilds it, or its route back is cut). **Throttled:** active units working below capacity, declared at mapping.
- **Upkeep (basal maintenance):** what keeps a part's units in existence. **Renewal:** a baseline per active unit plus wear per unit of work.
- **Shortfall ($\ell$):** the unmet part of the reference allocation, per resource. **Residue:** the state change a shortfall leaves.
- **Margin ($M$):** what can go unmet below the top before the protected flow moves.
- **Requirement link:** a documented dependency by which a part's requirement rises when another part's work falls.
- **Economising:** a governor mode lowering the access of every part below the top and its supports by the same share of its work draw.
- **Severance; constriction; steal:** as in Section 6.
- **Viable set; capture basin; collapse; death:** as in Section 6.
- **Capture** (extension): a nested system changing the signals or gates that set its own access.

## 15. Extension layer (proposed, phase 3): nested systems

**Status:** a proposed extension, approved by James on 6 October 2026. It does not change the core, and it is used only in mappings that need it, with the mapping guard.

1. **Part or system.** A part's access is set by the containing system's governor, or built into the part or route (CANON 3: parts do not set their own access). A nested system has its own closed loop that regulates its own access and viability. Examples: a tumour; a person in an institution.
2. **Supply through a part needs nothing extra** (the placenta).
3. **Institutions have two architectures in the same space:** the functional graph (roles, departments, as parts) and the embedded systems (the people, each a complete persistence system).
   - **A role is where they meet.** Work a role requires that the institution does not fund is work not done in the institution's ledger.
   - **Where it falls on the person,** it belongs to the person's own mapping, as rising requirement in that system. The person draws their own stores (time, sleep, health) until their own governor protects their viability, and they withdraw, fall sick or leave.
4. **Capture.** A nested system changes the signals or gates that set its own access.
5. **Mapping guard:** nested systems are listed before outcomes, with independent evidence of their own access loop.
6. **First test of the criterion:** classify before outcomes across domains, and discard the criterion if those classed as systems do not behave as systems.
7. **Drain against capture.**
   - **The rule:** a nested system that only drains is, for the host, exactly a supply cut by its net drain.
   - **The prediction:** a host with such a part should match a host whose supply is cut by that amount, with the same parts going short in the same order. Capture shows as departure from that control.
   - **Example:** Mulligan and Tisdale 1991.

## Consolidation notes (for James's check)

Every change from v0.19, and its source.

| No. | Where | v0.19 | v0.20 | Source |
|---|---|---|---|---|
| 1 | Header | Canonical state, 7 October | Canonical state, approved 9 October; CANON.md governs | D9; CANON.md; James, 9 October |
| 2 | Section 1 | Central claim with "load", "record", "relocated", "its own network" | The law (CANON 1, verbatim) and the central claim as approved for version 2 | Answers to the v2 reports (2a, 2b); answers 4 to 6 |
| 3 | Section 1, derived result | "access relocates load" | "access decides only which parts go short" | Load sweep (approved) |
| 4 | Section 2 | "the purpose can become a recipient of load"; "the protected level" | "the purpose's access can be turned down"; "the top, the protected flow"; scenario line | Load sweep; D2; CANON 5 |
| 5 | Section 3 | Governor, working parts, special roles, repair network, resources and carriers | The seven components, classification rules, and each component; repair parts (withdrawn 9 October; row 18); network as routes with the edge cases | D1; CANON 2 and 3; Step A answers |
| 6 | Section 4, item 1 | Five phases, every part's basal maintenance before support work | Rank order, part by part; upkeep before work inside each part | Reports 19 and 20 |
| 7 | Section 4, items 2 and 3 | One rank layer; "is the order fixed or does it reverse?" | Two layers; modes and snapshots; the open question restated | D3; CANON 4 |
| 8 | Section 4, economising | A magnitude cut from ordinary parts' work access | A governor mode, not the default order | Report 20 |
| 9 | Section 5 | "Basal maintenance first" across parts; repair as the network's work | Upkeep before work within a part (CANON 3); repair parts (withdrawn 9 October; row 18) | Report 20; CANON 3 |
| 10 | Section 6 | "How load moves"; load flow; "load passing on"; "exported load"; "the exhaustion cascade" | Shortfall and ledgers; work not done across the boundary outside this ledger; requirement links; two real chains; the order of exhaustion | Load sweep; answers 4 and 5; report 20 |
| 11 | Section 7 | The record and its dynamics (G12) | The protected flow (Proposition 2 in version 2 form); indicators; the G27 window | D2; reports 19 and 20 |
| 12 | Section 8 | "Boundary, currency and protected level"; "What is X (the record)?" | CANON 5's order; the governor's targets and the indicators; requirement links; the worked example | D1, D2, D6; CANON 5 |
| 13 | Section 10 | G1 to G26 in v0.19 wording | G1 to G27 in version 2 wording; G12's derivation and mapping fault named; the section log | D5; report 20 |
| 14 | Section 11 | H1 and PT1; engine departures | Adds the Bondar finding; the engine's order identified as reading A | Step A answers; report 20 |
| 15 | Section 12 | Tier lists | Adds the protected flow before the break, deeper layers, and the candidate proposition (words only) | Step A answers |
| 16 | Section 14 | Load, residue, record, repair network | Protected flow, indicator, shortfall, repair parts (withdrawn 9 October; row 18), mode, snapshot, requirement link | D1, D2; load sweep |
| 17 | Section 15 | "Strain on a role is load pushed across a system boundary"; "a host carrying it" | Work not done in the institution's ledger, rising requirement in the person's own mapping; "a host with such a part" | Answer 4 (M97); load sweep (M98) |
| 18 | Sections 1, 3, 5, 8, 10, 12 and 14 (amended 9 October) | Repair parts, "when repair is cut first", "when a shortfall reaches their rank" | Repair as work like any other: routine repair in each part's draw; damage raises the damaged part's requirement, met within its rank; G23 restated | CANON 3 (9 October); James, 9 October |
| 19 | Sections 1, 3, 5 and 14 (amended 9 October) | "A part dies only when its route back is cut"; "Part death" | Scarred: lost for good when the losses destroy what rebuilds it or the route back is cut; parts do not die | James, 9 October (#10); DECISIONS 2026-10-06 |
| 20 | Sections 1, 2, 4, 6, 8, 10, 12 and 15 (amended 9 October) | "has learned", "pursues its purposes", "choose to dissolve", "by choice", "remembered", "willing receivers", "is learned", "can give up" | Restated as arrangement or consequence | CANON 3 (9 October) |
| 21 | Section 3, classification rules (amended 9 October) | Not stated | A setting includes the governor's response to its sensed levels; opening a damaged part's access is the setting acting | James, 9 October (CANON 3, reading (a)) |
| 22 | Sections 2, 3, 9, 12, 13 and 14 (amended 9 October) | Signal integrity not stated | The assumption (sensing and command), the scope, the three signatures and the guard, the G27 test setting, future work, the term | CANON 7; James, 9 October |
| 23 | Sections 1 and 3 to 15 (amended 9 October) | The wordings named in papers/pam-model/25 (claim register) | As in changes row 20 | FINAL_CHECK round 1; James's rulings |
| 24 | Sections 1, 3, 4, 7, 10, 11 and 14 (amended 9 October) | The wordings named in papers/pam-model/25 (claim register), after round 2 | As in changes row 21 | James's corrections after FINAL_CHECK round 2 |

**Checked, not changed:** the scope's examples; G9, G14, G15 and G17 (carried, excluded from the paper); the verdicts.
