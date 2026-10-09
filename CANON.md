# CANON: the laws of the model

Only James changes this file. Each change is dated in the log at the end, with what changed and why. Everything else in the repository (model documents, the paper, mappings, tests) is checked against this file. Where anything conflicts with it, this file wins: stop and ask James.

## 1. The law
Under scarcity, allocation is zero-sum. At a fixed, fully used inflow, raising one part's access lowers another's. While no part receives more than it requires, no setting of access reduces the total shortfall; it only decides which parts go short. The exceptions are named: adding resource, lowering what parts require, opening a gate that holds resource back, and taking back what a part receives beyond what it requires. Drawing a store meets the gap now and leaves less for later. Drawing from outside meets it from beyond the boundary.

## 2. The seven components
1. Boundary: fixed first. It decides everything else, including which part is the top.
2. Governor: a set of targets on sensed levels. If a level crosses its threshold, the governor acts until it returns. It owns the signals and does no work.
3. Parts: anything that does work. Parts are dumb: they have no demand of their own. Each part has a rank. One part is the top.
4. Protected flow: the flow of the resource to the top, which has to be maintained, and is being maintained, at all costs, measured against the top's need.
5. Network: the routes the resource moves along.
6. Stores: hold resource and release it.
7. Outside input: resource or energy from across the boundary.

Everything else is a mapping aid, never a component.

## 3. Classification rules
- If it does work, it is a part. That includes work done on the governor's signal: the signal is the governor's, the work is the part's. Parts pay the cost of signalling.
- Components are roles, not objects. One structure can play two roles (for example, a vein is a route and the blood in it is a store). Classify the role.
- An indicator is whatever an observer watches. It may be the protected flow, a level the governor holds, or neither. Never assume which.
- Nothing passes between parts. All parts draw on one shared flow of each resource, and each part's access to it is limited separately. Parts do not set their own access (a part that does, such as a tumour, is a separate case). Access is either set by the governor or built into the part or route, and both kinds of setting are fixed within a mode. A setting is the rule that gives a part's access at each sensed level, so a part's access can change within a mode while its setting does not. A built-in setting is not set by the governor: it fixes the part's access within its layer, and a change in the part's requirement can move its place in the order. The governor's regulation works through stores, intake, gates and the settings it does control; where it sets a part's access, a change in requirement changes that part's draw in its own turn, not its place. When a sensed level crosses its threshold and the governor acts, the setting is acting, not changing: access changes and the order does not. A mode change is a change in the order, or in which levels the governor holds, other than through built-in access. It ends the snapshot. A shortfall is a count at a part, not something that moves.
- What a part is made of are its units (cells in an organ, staff in a department), not parts. Units take their part's access. Which units within a part go first (for example, by distance from the supply) is a mapping aid. Count work once, at the part.
- Where the governor sets a part's access, it sets it as a whole. It does not split a part's draw between upkeep and work: what reaches a part covers its upkeep first, then its work.
- Repair is work like any other. Routine repair (renewing worn units) is part of each part's own draw. Damage raises the damaged part's requirement. The governor meets it as it meets any requirement: by opening that part's access, where it sets that access, and releasing stores into the flow, within the part's rank. The part's response to what arrives is a consequence. Units lost to a shortfall are not damage, and rebuilding them is not repair: it is paid from what is left once every part has drawn. No rule puts repair first or last.
- The model describes an arrangement, not an intention. Nothing in it decides, wants or chooses.

## 4. Hierarchy
- The top is the part everything else is sacrificed to keep going. Anything sacrificed before it is not the top.
- The governor protects the top by limiting everyone else's access first.
- Rank runs from the top down by dependency: the top, then the parts whose work feeds the top, then the parts that feed those. Within a layer, rank comes from documented access and, where access is built in, from requirement.
- The top never changes within a boundary. Below it, the order follows from access and requirement. Access settings are fixed within a governor mode and change only when the mode changes. The model applies to one mode at a time, which is a snapshot. A threshold switch is a mode change: crossing its threshold changes the order, or which levels the governor holds, and ends the snapshot.

## 5. How to map
- Boundary first, then the top and the protected flow, then everything else.
- Name the resource, never its carrier or its route.
- A scenario is a load applied to a system, not a system.
- Never work backwards from a scenario, an outcome or a data set. Never choose the top, the protected flow or an indicator because a data set happens to record it.
- The core of the model contains no domain-specific term.
- Use the fewest components that do the job.

## 6. When a test fails
- The verdict stands. A failure is logged, never explained away.
- A mapping fault is named and corrected in a new file beside the frozen one.
- A correction is published as a new version, with its changes stated. Nothing is redacted.

## 7. Signal integrity
- The model assumes the governor's signals are true: what it senses matches the real levels, and the access it sets is put into effect; the realised flow may still be limited by the network. A system with a signal fault is outside the propositions.
- Used in reverse, the gap between what a governor with true signals would do and what is observed points to where a signal failed:
  - a false alarm: access cut while the flow is ample, with no documented mode;
  - a missed alarm: the order broken, with a higher part short while a lower part still draws, and no part it depends on short in the step before. A documented dependency lag, or a recovery lag (units of the top or a support part still coming back after an earlier shortfall), is not a fault, but the earlier shortfall must be observed, not inferred from the later one;
  - a setting not carried out: a part's access not matching the setting commanded.
- A signal fault is never a rescue. It can be named only if it is documented independently, or logged in advance as a candidate and then checked.

## Log
- 2026-10-08: created (James).
- 2026-10-08: CANON 1 reworded to remove movement language, matching CANON 3 (James).
- 2026-10-08: CANON 4 line reworded after Bondar et al. 1995 (James).
- 2026-10-08: access set per part as a whole (James).
- 2026-10-09: section 7, signal integrity (James).
- 2026-10-09: repair as rising requirement met through access (James).
- 2026-10-09: arrangement, not intention (James).
- 2026-10-09: one shared flow of each resource (James).
- 2026-10-09: 'fully used' added to the law, matching Proposition 1 (James).
- 2026-10-09: signal integrity means commanded access is put into effect (James).
- 2026-10-09: built-in settings fix rank; the governor regulates around them (James).
- 2026-10-09: built-in settings fix access within a layer (James).
- 2026-10-09: within a mode the settings are fixed; the order follows from settings and requirement (James).
- 2026-10-09: CANON 7 wording aligned with the paper (James).
- 2026-10-09: rank within a layer from access and, where built in, requirement (James).
- 2026-10-09: repair line matches built-in access (James).
- 2026-10-09: fourth exception, allocation beyond requirement (James).
- 2026-10-09: a setting acts within a mode; mode change defined; built-in and governor-set access distinguished (James).
- 2026-10-09: rebuilding after a shortfall is not repair (James).
- 2026-10-09: dependency lag excluded from the missed alarm (James).
- 2026-10-09: CANON 5: name the resource, never its carrier or its route (James).
- 2026-10-09: a setting defined as a rule; threshold switch defined (James).
- 2026-10-09: recovery lag excluded from the missed alarm (James).
- 2026-10-09: the law's condition on allocation beyond requirement stated in the rule (James).
