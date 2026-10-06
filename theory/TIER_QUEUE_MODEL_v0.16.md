# The tier-queue model, v0.16 (canonical state, 6 October 2026)

**Status:** working model (phase 3).

This is the single reference for the model as it stands. History is in theory/tier_queue_changelog.md, and the decisions behind v0.16 are in theory/v0.16_pending.md. The maths is in theory/tier_queue_math_v0.16.md (the model's target form; theory/tier_queue_math_v0.15.md still describes the engine), and the diagram is theory/figures/tier_queue_diagram_v016.png; the engine is theory/sim/tq_core.py, specified in theory/tier_queue_core_spec.md. **The engine has not yet been updated to v0.16** (Section 10 lists where it departs). Changes go into new versions, with what changed and why recorded in the changelog.

![Tier-queue model](figures/tier_queue_diagram_v016.png)

## 1. The principle

**Central claim** (confirmed by James, 5 October 2026; revised for v0.16 on Claude's recommendation, James deferring, 6 October 2026; a plainer version for abstracts and short pieces is to come, with this statement kept as the reference):

> In a goal-directed system with finite-capacity parts and limited reserves, load is routed according to each part's current marginal value to the persistence of the level being protected, judged against the next task that persistence depends on. The system holds its routine output steady by drawing reserves, taking resources from lower-value or expendable parts, which absorb the load, lowering demand and capacity where it can, or exporting it. So the record sees compromise, not stress: it moves only when the buffers, sacrificial parts and routing capacity can no longer absorb the demand. Recovery runs the other way. It begins once demand falls back within current capacity and supply flows again, rebuilds the intake and the capacity the next task needs first, and refills reserves according to how scarce the system has learned its world to be. Load without enough slack to restore what the next task needs makes the system chronic: that state, not the passage of time, permits deterioration, and deterioration becomes a scar only when it destroys what rebuilds a part.

**In parts.** A goal-directed system is a network of working parts and reserves. Priority, which is dynamic, sets the routing; it needs no strict hierarchy, and dependencies can form loops. Each working part does work only it can do, and has a limited capacity; a reserve is a stock and does no work. Work never moves between parts; load does. When demand exceeds what a working part can do, or its supply is diverted, the excess is not removed: it is drawn from a reserve, taken as resources from working parts of lower priority, which absorb it as load, held at the part as deterioration, or sent out across the boundary.
- Load therefore runs downhill, from protected parts to expendable ones, and can back up along a dependency to the part that started it.
- The protected part's output, which is what the system records, stays normal while the parts below absorb the excess. It changes only when they can absorb no more. **The record sees compromise, not stress.**
- Recovery runs the other way, starting with the intake. It begins once demand falls back within what a part can currently do and supply flows again, so no new excess is generated; it does not need demand to stop. Deterioration nobody knows about is never addressed (a prediction about unobserved state, not a universal law).
- Priority is not a fixed rank. It is each part's current value to the system's persistence, which changes with the part's state and the situation.
- What a system becomes after an episode depends on its state, not its length. Load that is signalled and recovered from with slack (the acute state) can leave a part stronger, or leave the system re-tuned to that threat. Load without enough slack to restore what the next task needs (the chronic state) permits deterioration; it leaves a scar where it destroys what rebuilds a part, and parts that cannot be rebuilt keep their losses.

## 2. The parts

The system's components are **working parts** (including intakes and control parts) and **reserves**. In this document "part" means a working part; a reserve is always named as one.

| Kind | What it is | Examples |
|---|---|---|
| **Working part** | Does a job with a limited capacity | Brain, heart, nephron, nurse bee, front-line staff |
| **Intake** | A working part whose job brings resource in. Every refill depends on it | Gut, leaves, roots, foragers, a referral or recruitment function |
| **Control part** | A working part whose job is routing. It holds the threshold switch. Priced as a cliff only when it is a necessary, non-bypassable routing bottleneck; distributed, redundant or bypassable control is priced like any other part | Vasomotor centre, hypothalamus, an institution's management (non-bypassable); a honeybee colony's task allocation (distributed) |
| **Reserve** | A stock that is drawn on and refilled. It runs full, drawing or empty, and is not itself damaged | Fat, iron stores, venous blood volume, honey stores, budget reserves |

A reserve is a stock. Spare capacity (headroom) in a working part is not a reserve: "contractile reserve" or "cognitive reserve" are redundancy and compensation. The brain holds almost no fuel stock; it is protected through priority of supply, redundancy and compensation.

**What counts as one part.**
- Units that duplicate each other, share resources and balance load are **one part**, and their number is its capacity (processor cores, nephrons, the two kidneys). Losing one lowers the part's capacity and the rest work harder.
- Units in **series** are separate parts linked by dependency: load has to clear each in turn. Each series link is non-bypassable.

Each working part has these properties:
- a **capacity**;
- how **vital** it is: the share of the system's persistence that depends on it;
- a **renewal class**, which sets its **rebuild time**: fast (a conveyor such as the gut lining), slow (liver), or none (fixed capital: neurons, heart muscle);
- a **template:** what rebuilds it like-for-like (its stem cells, its supporting scaffold, its own boundary, its living growth tissue). Fixed capital has little or none. A renewable part whose template is lost behaves as fixed capital;
- a **ceiling**, lowered by scars or raised by growth after acute load;
- its **spare capacity** (redundancy), which enters through its value (Section 3);
- a **demand floor:** its minimum running cost, below which its demand cannot be lowered;
- its **structural capacity** and its **deployed throughput**, which can differ. Many parts flex deployed throughput to meet demand and drop back when the task ends; some cannot. Deployed throughput tracks demand continuously, up to the part's ceiling, whenever supply (reserves included) covers it. There is no throughput target: demand is whatever the governor needs to hold its level (the record), so in a body it changes from moment to moment. "Sustained capacity" is simply the throughput ongoing supply supports without drawing a reserve. A part may deliberately run below its structural capacity: **suppression** (a hibernating bear's kidney filters less while nitrogen is recycled elsewhere) or **remodelling** (a migrating bird's gut shrinks for a non-stop flight and is rebuilt at stopover; a python's gut shrinks between meals). Both are reversed in full when demand returns. Neither is deterioration or compromise.

A part's priority is not one of its properties. It is computed from them and from the part's current state (Section 3).

**State, for working parts:**
- **Optimal:** within capacity, reserve full.
- **Stressed but coping:** covering the excess from the reserve or from the slack of other parts, or deteriorating while its template is intact, so it can still refill. Protective slowing begins here, giving up some capacity to protect the part.
- **Compromised:** deterioration has destroyed the template, or repair has stalled, so lost capacity cannot be rebuilt like-for-like.

Losses compound, because overload is felt against what the part can do now, not what it could do before.

## 3. Priority

**The objective.** Every system's first objective is its own persistence; its output comes second. A system cannot do its function if it no longer exists. This holds for every system the model is applied to; there is no separate slot for an institution's stated purpose.

**Whose persistence.** The mapping names the level whose persistence $W$ measures. Parts can be spent for the level above when $W$ sits there: a worker bee dies for the colony, and a Pacific salmon, an octopus or an agave spends its whole body on reproduction. Setting $W$ one level too low predicts the wrong order, so these cases test the model.

**Marginal value.** A part's value at time *t* is how much the system's persistence would lose if the part lost a unit of capacity:

$$v_i(t)=\frac{\partial W}{\partial c_i}\bigg|_t$$

It is a shadow price, judged against the **next task** persistence depends on: a migrating bird's gut is valuable at stopover and payload in flight. It is near zero for a part with spare capacity, or for one whose work is not needed now (the gut when there is no food), and high for the part that limits the system. In the engine, $v_i=\text{vital}_i\times b(L_i)$, where $b$ rises from 0.05 to 1 as the load on the part approaches its current capacity.

**Non-bypassable links are priced as a cliff.** A part or link with no alternative route (central control, through which every routed unit passes; a transporter such as the heart; any link in series) breaks the system if it is lost, even with every other part intact. Its value is therefore its full vital weight ($b=1$), not its own workload. Natural systems with central control protect it to the end (the brain in starvation and in blood loss). Distributed, redundant or bypassable control (a colony's task allocation; local reflexes; systems that can route around a damaged node) is priced by its marginal value like any other part. Which links are non-bypassable is a mapping decision, made before predicting.

**One value, two decisions:**

| Decision | Formula | Meaning |
|---|---|---|
| **Who pays first** under load | Ascending $p_i=v_i\,s_i\,\min(\tau+h_i,\;T)$ | What the system loses if the part is spent: its value now ($v_i$), times the share of its capacity still at stake ($s_i$), times how long the system would go without it: the rest of the episode ($\tau$) plus the part's rebuild time ($h_i$; very large for fixed capital), never more than the remaining horizon ($T$). $T$ can be the deadline of the next task persistence depends on (the next flight, the next winter) rather than the remaining life |
| **Who is resupplied first** in recovery | Descending $q_i=v_i/k_i$ | The order in which returning supply reaches parts: value restored per unit of resource ($k_i$: the cost of restoring a unit of capacity). There is no separate repair pool; a part refills only once its own load is back within capacity (Section 4, item 7) |

**The terms of the spending cost.**
- **Time without the part.** Losing a part costs its value for as long as the system goes without it: the rest of the episode, $\tau$, plus its rebuild time, $h_i$, but never longer than the system has left, $T$. The system must estimate $\tau$; the engine uses the length of the current episode so far.
- **Consequences of the time term.** With a long horizon, fixed capital is the dearest thing to spend. As the horizon shortens, or as an episode lengthens, spending a part that cannot be rebuilt costs little more than spending one that can. A system whose prospects are falling therefore spends parts it used to protect (terminal investment, with the objective set at the level of the lineage). Long episodes should likewise erode the protection of slow-rebuild parts; **this was not reproduced in the engine**, where a strained fast part stays the fuse (open).
- **Capacity still at stake.** Damage saturates: a part can lose only what it still has, so $s_i$ runs from 1 (healthy) to 0 (at its floor). A part that has lost all it can lose costs nothing more to load. It becomes the system's **fuse**, and load is concentrated on it rather than spread (leaves and fine roots in drought; old leaves shed first).

**When spending by marginal value is the best policy.** Spending in ascending order of marginal value is optimal only when each part's returns diminish and parts can be priced separately (a concave, separable objective: the water-filling solution). Three departures matter:
1. **Saturating damage** favours concentration on a sacrificial part over spreading: the fuse, handled by $s_i$.
2. **Cliff-shaped losses** (a non-bypassable part or link whose loss breaks the whole system) are never priced at the margin.
3. **Increasing returns to an output** make the best choice all or nothing. A short horizon alone erodes protection gradually; spending the whole body (semelparity: Pacific salmon, octopus, agave) needs a short horizon and increasing returns to reproductive effort (in agave, pollinators favour taller flowering stalks). Not yet in the engine, which has no explicit objective.

**The reserve's value is the expected shortfall:** how likely the system is to face demand above its capacity, learned from experience (in the engine, how often total demand has recently exceeded total current capacity). Chronic or unpredictable scarcity therefore raises the reserve's value and its place in the recovery order.

**The reserve also remembers the worst it has met.** Like a part (Section 4, item 8), the reserve is peak-referenced: an episode whose total shortfall exceeded the reserve's base size enlarges the reserve towards that depth, and the memory fades on the system's own clock. **Frequency sets the order; depth sets the size.** After a single severe acute episode, the reserve is still refilled after the working parts (G10), but to a larger size than before. Repeated episodes raise both: the system holds a larger reserve and refills it earlier.

**Control sees value through state signals.** In a coupled system the signals carry the load each part actually carries, including what landed on it from elsewhere. In an opaque one, control sees only nominal demand against nominal capacity, so a strained lower part looks as if it has spare capacity: **opacity corrupts the priority calculation itself, not only the routing.** Even in natural systems, a signal that stays high loses gain over time (adaptation, as in baroreceptor resetting), so long-lasting strain is undervalued.

**What this explains that a fixed ranking only asserted:**
1. a redundant organ that cannot be rebuilt (the kidney) is cut after cheap tissue (gut, skin);
2. the gut is spent first in a fast and rebuilt first at refeeding: its value changes, not a rank;
3. the recovery order after acute and after chronic load (G10) follows from the reserve's expected-shortfall value;
4. "next demand", dependency (a dependent infant's muscle has low value) and insurance are all expressions of value;
5. with a shrinking horizon, parts that cannot be rebuilt lose their protection (the terminal-investment direction; shown in the engine, not yet checked in natural systems);
6. under saturating damage, a lost part becomes a fuse and takes the load (shown in the engine; consistent with plant hydraulic fuses).

## 4. How the parts interact

1. **Routing.** Work is local: it is what only that part can do, and it never moves. What moves is load. Load arises at a part in two ways: its throughput is maxed, or its supply is diverted elsewhere. A change of priority is a condition for diversion, not a third cause.
   - **Resources taken by priority.** A part whose demand exceeds what it can do draws first on the reserve, then on the resources of lower-priority parts, lowest first. They give up their slack first, at no cost to them. Beyond their slack they can no longer do all their own work, and that is the load landing on them. The receiving part does not do the giver's work; it absorbs load. Priority here is the spending order of Section 3.
   - **Load backing up a dependency.** A part whose throughput is maxed leaves its excess unprocessed, and it backs up along its dependency onto the part that feeds it, as more of that part's own work.
   - **What is left.** Load that cannot be placed stays on the part, where it deteriorates (item 7), or leaves across the boundary.
2. **Labelled and unlabelled load.** Load that arrives with its origin can be refused by a part already under strain, which keeps the strain visible higher up. Load passed on through opacity has no origin, so it cannot be refused and sinks to the lowest tier.
3. **Coupling.**
   - **Shared supply.** A protected part depends on upstream supply, so it is protected only partly when that supply falls (brain flow falls with cardiac output).
   - **Coupling is shared dependency.** Parts are coupled when they share an input, a stressor, a reserve or the machinery that repairs them, not when they are the same type of part. The links form a network, and load can travel back to the part that started it: in heart failure, the kidney's retention of fluid lands as extra load on the heart, whose weakness triggered it. That loop is load backing up a dependency; it needs no new mechanism.
   - **Shared dependency synchronises strain.** Parts loaded through the same input strain together. Before any of them crosses a visible threshold, their state signals move together more and more; when their buffers run down together, the break is sharp. Where buffers are separate and run down at different times, the combined break is smooth.
4. **Threshold switch.** At a set point, not at exhaustion, control changes mode: it sheds a commitment, changes metabolism or behaviour, and often makes the record move. The set point lies in the gap between the shortfall still expected and the reserve held; with nothing more expected, it is a set depletion of the buffer. Where the switch acts ahead of load, a signal must reach control, or a persistent signal must cross a threshold (temperature, day length, food availability, the reserve itself); which signal is a mapping question.
   - **Economising, the graded form of the switch.** Control lowers a part's demand and capacity together, on purpose and reversibly, ahead of or alongside load. Supply and demand can also fall together without control. Economising lowers deployed throughput (suppression), and sometimes structure too (remodelling), down to each part's demand floor; the top and non-bypassable links are never cut. In a body: less heat, less activity, reproduction and immune work cut, organs shrunk.
   - **How it follows expectation.** Economising follows an S-curve in the gap between the shortfall still expected and the reserve held: zero below a threshold, rising, then levelling at the floor.
     - For a predictable episode (a season, a known fast), the remaining need is known, so economising starts at onset, before the reserve is drawn (a bear entering its den).
     - For a kind of episode met before, the expected length is the usual length.
     - Beyond the system's experience, it expects as much shortfall again as so far.

     Time matters only through what it does to the expected shortfall and the reserve. Economising eases as the reserve is refilled, not when supply returns, so it persists into refeeding and the reserve is refilled faster than intake alone allows (catch-up fat). A short restriction that never brings the gap to the threshold triggers none of it; breaks long enough to refill the reserve prevent it.
   - **The ledger.** What economising cuts is shed: commitments cross the boundary for good (heat not made, activity and reproduction forgone), and a part's output to its dependants falls with its throughput. **Economising causes no deterioration.** A smaller part needs less upkeep, and what is reduced is restored in full when demand returns (python gut, shorebird organs, ground-squirrel synapses; theory/deterioration_threshold_scan.md).
   - **Value and expected shortfall are measured against normal demand.** The system's own economising does not change what a part is for, and does not count as the environment easing.
   - **Economising and growth compete.** Economising spares working parts and the record, which removes the strain that growth needs (G17).
5. **Outright failure.** There are two routes.
   - **Exhaustion.** No part fails outright while there is still somewhere for its load to go. When there is nowhere left, the part that goes is the one priority spends (the fuse).
   - **Severance.** Cutting a non-bypassable link breaks the system while willing receivers are still intact: central control, a transporter, any link in series (an obstructed ureter stops urine with the nephrons intact; a girdled stem starves the roots with the leaves intact).
   - **Control failure is severance of routing.** If load reaches the control part beyond its capacity, routing stops following priority: protected parts are hit while buffers remain (division of labour breaks down in collapsing colonies).
6. **Compounding on survivors.** Parts absorbing load deteriorate under it, and their failure adds load to the rest: hyperfiltration in the kidney, precocious foraging in bees, the vacancy cascade in teams.
7. **Deterioration and recovery.**
   - **The container.** Each part, with or without a reserve, is treated as a container for its own upkeep. Load or work beyond its capacity, or supply diverted away, is a leak. While the leak continues the part deteriorates, and it cannot refill however much flows in. Once demand settles within capacity and supply flows again, the part refills: that is repair. The work is the part's own; it happens locally, and only once demand through the chain recovers.
   - **No separate repair pool.** Returning supply reaches parts in descending value (Section 3), and each part refills from its own supply once its own leak has stopped. The order therefore depends on the state the past load left:
     - after **acute** deprivation: intake first, then the working parts the next task needs, then reserves;
     - after a **chronic** state of scarcity: the system expects more scarcity, and the reserve is enlarged first, often overshooting; lean and working tissue follow more slowly;
     - after a **single severe** episode: reserves still come last, but are refilled to a larger size, which lasts.
   - **The intake comes first whenever it was run down.** It is spent early when there is nothing to take in, and rebuilt first when supply returns.
   - **Speed and order are different things.** How fast a part recovers depends on its renewal rate; the order in which supply reaches parts is priority. The gut has both: fast renewal, plus supply diverted to it at refeeding.
   - **Recovery requires slack:** demand below current capacity. It does not need demand to stop, so partial recovery under reduced demand is expected.
   - **Dose and the template.** Deterioration is reversible while the part's template survives. Its extent grows with the dose: how far load exceeds capacity, multiplied by how long. Where the dose destroys the template, or repair stalls, the lost capacity is patched rather than rebuilt: the patch keeps the part intact without its function (fibrosis), a scar. The patch itself may be removable until it matures (cross-linked scar tissue in the liver). Fixed capital has little or no template, so it keeps any loss: the point of no return.
8. **What the system becomes after an episode.** Four outcomes, which can occur together in different parts:
   - **Growth:** capacity rises above its old level. Conditions: the load was acute, state signals reached control (coupling), slack followed, the part is renewable, and the challenge strained the part without threatening the reserve (otherwise economising spares the part and removes the stimulus). Examples: muscle after hard work; an institution that sees staffing strain and adds capacity.
   - **Re-tuning:** the system changes demand, allocation, thresholds or reserve size in line with the threat it met; capacity need not change. **Protection is set by the peak load met, not by cumulative load:**
     - after a recovered episode, a part carries loads up to that peak without strain;
     - above it, strain builds at a reduced rate;
     - the protection above normal capacity fades with time, and a scar removes it;
     - this holds even while the part is still recovering, so repeated loading at or below the earlier peak during recovery adds no damage.

     Examples: spruce cutting leaf area after drought; small birds carrying more fat when food is unpredictable; brief ischaemia protecting the heart against a later, larger one.
   - **Scar:** a lower ceiling where the template was lost and the capacity patched. A scar can also cut **demand** (spruce leaf area); whether a past injury makes a system more or less vulnerable depends on whether it cut demand more than capacity.
   - **Loss:** fixed capital keeps what it lost.

   Suppression and remodelling are not outcomes: they are reversed in full.

   **The acute-chronic flip:** the same kind of load can produce growth when the system is in the acute state (signalled, buffered, recovered from with slack) and deterioration when it is in the chronic state (not enough slack to restore what the next task needs). Deterioration becomes a scar only where the dose destroys the template. **The state decides whether deterioration builds, not the duration; the dose decides whether it scars.** A long, prepared and buffered episode need not deteriorate at all (a hibernating bear fasts for months with muscle and bone preserved; a migrating bird repeats planned remodelling every year).

   **The cost of re-tuning:** if conditions change, a system tuned to a past threat can be mistuned for the new one (to test).
9. **Starting state.** A system need not start optimal. Its stage at the start sets how much room it has, and is read from state signals, because the record cannot show it.

## 5. Read-outs

- **The record:** the output the system routinely watches, which is the top's served demand. It is flat through stress and moves at compromise, or at the switch.
- **The record's dynamics.** The record's level is silent until the break, but its dynamics need not be.
  - A small knock leaves a deficit that the reserve restores at its release rate $\rho(R)$, so recovery takes about knock $\div\,\rho(R)$.
  - Where release tapers as the reserve shrinks, recovery time rises as $1/R$ and grows without limit as the reserve empties. The record recovers more slowly from each knock, and its autocorrelation and variance rise while its mean stays flat (critical slowing down).
  - Where release stays at full rate until a switch, the break comes with no warning in the record.
  - When state signals are filtered, watch how long the record takes to recover, not where it sits (G12).
- **State signals:** each part's strain, deterioration, capacity and reserve level. They move from the start of stress. In opaque systems they are filtered, mistranslated or lost. Each is judged against the system's own reference state for its current phase.
- **Co-movement across parts.** Where parts share a loaded dependency, their state signals move together more and more before any of them crosses a visible threshold, and before the record moves (G18). Rising co-movement points to a shared input upstream.
- **Three kinds of capacity loss** (G19):

  | | Timing | Recovery |
  |---|---|---|
  | **Economising** (suppression or remodelling) | Capacity falls before or with lower demand, with no strain beforehand | Full and fast when demand returns |
  | **Deterioration** | Capacity falls after load exceeds it | Full once the leak stops, if the template survives; time set by the dose |
  | **Scar** | | Incomplete: integrity kept, function lost |
- **Where strain begins (the Felicity read-out).** Raise the load and note where strain signals first appear ($D_{\text{on}}$). Compare it with the part's previous peak load ($D^\ast$) and its normal capacity ($\kappa c$):
  - $D_{\text{on}}\ge D^\ast$ (Felicity ratio $F=D_{\text{on}}/D^\ast\ge1$): protected, or grown;
  - $\kappa c\le D_{\text{on}}<D^\ast$: protected, but the protection is fading;
  - $D_{\text{on}}<\kappa c$: scarred (compromised).

  It separates "recovering" from "scarred", which the record cannot, and needs no record at all. It follows from the re-tuning and scar rules (G7, G8).
- **The ledger:** demand = work done + reserves drawn + load absorbed by other parts + load held at the part (deterioration) + load leaving the boundary. Nothing leaves the ledger except through work done or the boundary.
- **Reading a compensating part's output** (insulin, brain-sparing blood flow): it rises while the part copes and falls when it is compromised. A fall is therefore ambiguous: the load may have eased, or the compensator may be failing. Check the load at its source before reading a fall as improvement.

## 6. Mapping a system

Do this before opening any outcome data.

1. **Boundary and currency.** Name the system and its boundary, and choose a currency that obeys a balance (energy, blood volume, filtration, labour hours, cases). Name whose persistence the objective measures (the organism, the colony, the lineage), and which parts may be spent for that level.
2. **Demand and load.** What work is asked of each part, and from where? Where can demand exceed capacity, or supply be diverted, and so become load?
3. **The record.** What figure does the system, or its observer, routinely watch and defend? It must be a **held output:** delivered below capacity, and kept up by buffers or a defending loop. A capacity test (maximal force, a time trial, a stress test) or a direct measure on the working units (nerve-fibre thickness, synapse counts, the control hormone) is a state signal, not the record.
4. **The top.** Which part's output is that figure? Is it fixed capital? This is the only part whose place is named in advance; every other part's priority is computed.
5. **The parts.** List the parts that do work. Units that duplicate each other, share resources and balance load are one part; units in series are separate parts. For each part, decide:
   - its **role**: working, intake or control; for control, whether it is non-bypassable or distributed, redundant or bypassable;
   - how **vital** it is to the system's persistence;
   - its **renewal class**, rebuild time and **template** (what rebuilds it);
   - how much **spare capacity** it normally has;
   - whether its throughput **flexes** with demand, and its **demand floor**;
   - for an intake, what it takes in, and when that is unavailable.

   **Fix these from independent sources before predicting any order:** lesion or knockout studies, regeneration and turnover rates, the cost of rebuilding tissue. Log each source. A value chosen with the expected order in mind is declared as such, and that part of the result counts as fitted.
6. **The reserves.** Which stocks are drawn first? Does release slow as they shrink?
   - **The remaining horizon.** How long are the system's prospects (life stage, season, age, the next task's deadline)? Is it shrinking?
   - **The system's clock.** Fix the unit in which durations are judged before checking anything: the reserve's refill time, a part's rebuild time, decision cycles, generations, depending on the level the objective measures. "Brief", "lasting" and "permanent" are claims on that clock.
   - **Expected episodes.** Which episodes are predictable (seasons, known fasts), and what is the typical length of familiar ones?
7. **Labelled or not, dependencies and links.**
   - Does load passed down arrive with its origin? Can the receiver refuse it? Do state signals reach the top?
   - Which parts share an input, a stressor, a reserve or repair machinery? Draw these links: they decide which parts should strain together.
   - **Which links are non-bypassable** (central control, transporters, series links)? These are the severance points.
8. **Control and the switch.** What routes load? Is there a known mode change, and at what point (the gap between expected shortfall and reserve; with nothing expected, a set depletion)? Where it acts ahead of load, what signal reaches control?
9. **State signals.** For each part, what measure shows its strain, deterioration or reserve? Judge each against the system's own reference state for its current phase: a hibernating bear's creatinine read against an active-season range would misread coping as failure.
10. **Starting stage.** From baseline state markers, classify the system as optimal, stressed or compromised. Population "normal" ranges may describe the stressed stage. Where the load can be raised and strain signals watched, the Felicity read-out separates a protected, a fading and a scarred part.
11. **Predictions.** Write the generic predictions in Section 8 for this system before looking at outcomes.

## 7. Using the model in reverse

**Forward,** the model takes a mapped system and its load and predicts where strain lands, and in what order. **In reverse,** it starts from what can be seen failing, and in what order, and points back to where load must have entered, which parts were buffering it unseen, and which dependency the failing parts share. It suggests **where to look**; it never names a cause.

Because the record sees compromise, not stress, the history of a failure is written in the lower tiers and shared inputs long before the protected output moves. Reverse mode is a method for reading that history; it adds no mechanism.

**Three disciplines:**
1. **A hypothesis generator, not evidence.** Its output is a set of candidate shared inputs and buffering parts, checked against values fixed independently, never against the failure order it was read from.
2. **Correct for visibility.** Biological onset, compensation, detection, diagnosis and decompensation are different moments. Each part has its own read-out and threshold, so states can move together while labels arrive one at a time. The order in which failures surface is not the order in which parts failed.
3. **Name a set, not a cause:** shared exposures, shared delivery pathways, a shared reserve deficit, and the earliest point at which the effects converge.

**Two routes to clustered failure:**
- **Price-clustered:** parts with similar spending prices are spent at the same point by routing. They strain in sequence, with little co-movement beforehand.
- **Dependency-clustered:** parts loaded through the same input co-move before either fails, even when their prices differ (G18).

Reverse mode has to know which route it is looking at. A failure with willing receivers intact points to a severed link (G20).

## 8. Generic predictions

**Two layers.** Some predictions hold for any negative-feedback loop with a finite stock, with no goal at all (a star leaves the main sequence with most of its hydrogen unburned; Earth's carbonate-silicate thermostat). Confirming them is cheap and says nothing about priority. Others need selection or design. Each prediction and each piece of evidence is tagged **layer 1** (any finite-stock feedback loop) or **layer 2** (needs selection or design).

**Contrast case.** Systems with load mechanics but no system-level objective, such as road traffic (diversion, backpressure and loops, but routing by individual choice and no held output), show layer 1 behaviour without a tier queue. They are contrasts, not tests (theory/framing_crosscheck.md).

| No. | Prediction | Layer | Status |
|---|---|---|---|
| G1 | The record stays near normal while state signals and reserves move | 1 | Natural observation: consistent in all surface tests (non-diagnostic for priority) |
| G2 | Lower-priority parts are drawn down first, in reverse priority | 2 | Natural observation: consistent (blood loss, fasting, bees); known in outline beforehand |
| G3 | The break comes at a set depletion of the buffer, not at exhaustion. If the buffer is a stock, the break comes at the same cumulative load whatever the rate | 1 | Natural observation: partly consistent (sheep rate-independence; fasting threshold at a fat share); stress-test candidate (H1, H2) |
| G4 | A larger buffer gives a longer silence and a sharper break; a stressed or compromised start breaks sooner | 1 | Natural observation: consistent (heat stress, initial fat, low nephron number); stress-test candidate |
| G5 | Survivors that absorb extra load deteriorate under it, so loss compounds | 1 | Natural observation: consistent (kidney hyperfiltration, precocious foraging) |
| G6 | Recovery runs intake first and reserves last, and needs slack. Unknown deterioration is not addressed, so the record recovers before the state does | 2 (order); 1 (record before state) | Natural observation: consistent for record before state (kidney); order, see G10 |
| G7 | Parts without a template (fixed capital) keep their losses. Renewable parts recover fully if their template survives, and return with a scar (a patch) if it does not | 1 | Natural observation: consistent (nephrons, spruce, scarred muscle); scan of template loss across tissues (theory/deterioration_threshold_scan.md; compatible, non-diagnostic) |
| G8 | Load that is signalled and recovered from with slack (the acute state) leaves growth or re-tuning. Load without enough slack to restore what the next task needs (the chronic state) leaves deterioration, which becomes a scar only where the dose destroys the template. The same load can do either: the state decides whether deterioration builds, not the duration | 2 | Natural observation: consistent (muscle, fetal hypoxia); simulation result for the earlier wording (TQ7, TQ8) |
| G9 | A system re-tuned to a past threat does better against that threat again, and may do worse if conditions change. Tests must follow the same individuals: at population level, the death of the susceptible mimics re-tuning | 2 | Natural observation: partly consistent (starlings, primed plants); cost of mistuning not found |
| G10 | After acute deprivation (recovered with slack), working tissue and intake recover before reserves. After a chronic state of scarcity, reserves recover first and overshoot | 2 | Natural observation: consistent (recovery-order test); simulation result, with a fitted shortfall definition and the pooled repair rule (TQ8). **Under v0.16 rules:** not reproduced without protective slowing (TQ10, V8); **reproduced with it** (TQ10b, economising off: parts first after the acute episode, reserve first after the chronic one). With economising on, the episodes leave no lasting deterioration, so there is no order to observe |
| G12 | **Record dynamics.** Where reserve release tapers as the reserve empties, the record recovers more slowly from small knocks as the break approaches, with rising autocorrelation and variance at a steady mean. Where release is full until a switch, the break gives no warning in the record | 1 (conditional on the release profile) | Derived prediction (maths); simulation result (TQ9: rise before the break in 20 of 20 seeds with a knee, flat with full release until a switch; mechanism check; TQ10 under v0.16 rules: 19 of 20, rise only in the last 30 steps); untested against data; blood-loss contamination declared |
| G13 | **Fuses.** Once a part has lost what it can lose, further load is concentrated on it rather than spread to healthy parts | 2 | Simulation result (TQ8); compatible but non-diagnostic (plant fuses); prepared systems (bears, migrants) show remodelling rather than fuses |
| G14 | **Peak-referenced protection.** After a recovered episode, strain signals appear only above the previous peak load; protection depends on that peak, not on the volume of the episode; it fades with time; after a scar, strain appears below normal capacity | 2 | Natural observation: partly consistent (muscle, natural test 11); simulation result (TQ8 C7) |
| G15 | **Reserve memory.** After a shortfall deeper than the reserve's base size, the reserve is enlarged towards that depth and stays enlarged for longer than after shallower ones, on the system's own clock. After a single acute episode it is still refilled after the working parts. Repeated episodes enlarge it and raise its place in the refill order. At equal total load, one deep episode leaves a larger reserve than several shallow ones unless the shallow ones are frequent enough to raise the expected shortfall | 2 | Simulation result (TQ8 C8; cap and memory fitted); natural observation: partly consistent (weight cycling, natural test 12) |
| G16 | **Economising.** Demand and capacity are lowered together when the shortfall still expected outruns the reserve held: at onset for a predictable long episode, later (with depletion) for an open-ended one, not at all for short episodes of a learned length. It levels off at the parts' demand floors, never touches protected parts or non-bypassable links, persists until the reserve is refilled, and is reversed in full | 2 | Simulation result for the earlier form with deferral (TQ8 C9, C10); compatible: intermittent restriction, bear hibernation, remodelling in pythons and shorebirds (scan) |
| G17 | **Economising and growth compete.** A challenge that threatens the reserve triggers economising, which spares working parts and the record but removes the strain that growth needs. Growth after acute load needs strain without economising | 2 | Simulation result (TQ8 C11); not yet checked in natural systems |
| G18 | **Co-movement before the break.** Where parts share a loaded dependency, their state signals move together more and more before any of them crosses a visible threshold, and before the protected output moves. The break is sharp where their buffers run down together and smooth where separate buffers run down at different times. Parts clustered only by spending price strain in sequence without this co-movement | 1 (shared dependency) and 2 (against price clustering) | Derived prediction; simulation result for the shared-dependency part (TQ9: co-movement rises once the shared input runs short, before either part strains; none with separate inputs; size scales with shared against own variation; TQ10 under v0.16 rules: reproduced at lower own noise, weak at the highest); untested against data; candidate test in a repeated-measures cohort (UK Biobank, reserve list R6), with a dependency map fixed first |
| G19 | **Three kinds of capacity loss.** Economising lowers capacity before or with lower demand, with no prior strain, and is reversed fully and fast. Deterioration follows load beyond capacity and is reversed once the leak stops, in a time set by the dose. A scar follows a dose that destroys the template and is never fully reversed. The same dose deteriorates a part with a robust template and scars one without | 1 (deterioration and scar); 2 (economising) | Derived prediction; simulation result, partly (TQ10: economising, small deterioration with recovery time rising with dose, weak templates and fixed capital separate as predicted; large doses run away to an empty part that never recovers; TQ10b with protective slowing: graded deterioration, scars from starvation below the demand floor or from dose built over repeated slowing); compatible: scan (python gut, shorebird organs, ground-squirrel synapses; ischaemic heart muscle, coral, bone, trees; muscle stem cells, kidney, liver); untested against data |
| G20 | **Two routes to outright failure.** No part fails outright while there is somewhere for its load to go; under exhaustion, the part that goes is the one priority spends. Failure with willing receivers intact happens only where a non-bypassable link is cut | 1 | Derived prediction; simulation result (TQ10: no part emptied while lower-priced parts held supply, except one whose load backed up a loop, which no other part can take; cutting a transporter broke the record with the reserve full); compatible: crosscheck (the out-of-memory killer in computing; staged load shedding on grids; urinary obstruction; girdling); untested against data |

G11 was withdrawn and is not reused; internal numbers keep the gap, and any public version is renumbered with a crosswalk.

**The test only layer 2 can pass:** a reserve that is easy to reach but valuable. Drawing in order of access would spend it; drawing by value would hold it. A clean natural case is still to find (muscle glycogen is weak: muscle lacks the enzyme to release it as blood glucose, so its retention is fixed design).

## 9. Evidence so far, and its weight

- **Simulations TQ1 to TQ9** (illustrative parameters).
  - TQ8 (theory/sim/outputs/2026-10-05_TQ8/README.md) shows computed priority reproducing the earlier results without hand-set ranks, and checks each later element.
  - TQ9 (theory/sim/outputs/2026-10-05_TQ9/README.md) adds loops, local stocks and record dynamics.
  - Both ran under v0.15 rules (Section 10).
- **Surface checks in natural systems.**
  - Systems checked: blood loss, fasting, kidney, honeybees, plants under drought, fetal growth restriction, recovery order, muscle injury against disuse, the record rule, re-tuning (natural tests 1 to 10), the Felicity read-out in muscle (test 11) and weight cycling (test 12) (theory/natural_test_*.md; theory/natural_tests_patterns.md).
  - All broadly consistent; each mismatch led to a refinement.
  - Unexplained or contrary items are logged in those files (for example, female rats did not lose weight more slowly in a second cycle).
- **By layer** (detail in theory/natural_tests_patterns.md):
  - **layer 1 only:** the kidney test and the record-rule test;
  - **layer 2 evidence:** the order of loss in blood loss and in fasting; the fasting switch; honeybee allocation; hydraulic fuses and the spruce demand cut; fetal brain sparing and the acute-chronic flip; recovery order after acute against chronic scarcity; growth against scar in muscle; re-tuning; peak-referenced protection in muscle; faster regain after weight cycling;
  - **layer 1 parts of the other tests:** the flat record and break at a set depletion; rate-independence (sheep); starting state.
  - **Re-tuning evidence and individuals:** starlings, preconditioning, primed plants, fetal sheep and muscle followed individuals; the human food-insecurity link is population-level; spruce survivor filtering is not ruled out (to check).
- **Definition checks, not tests** (6 October 2026). They sharpened definitions and carry no evidential weight:
  - a crosscheck of the framing against engineered and natural systems (theory/framing_crosscheck.md);
  - a scan of deterioration against scarring (theory/deterioration_threshold_scan.md; summaries and abstracts only).
- **Exploratory applications, not tests:** a reviewer applied the model to systems it chose arbitrarily (hibernating bears, migratory birds, heart failure, a cardiometabolic disease cluster), looking at evidence after choosing (raw/2026-10-05_perplexity_*.md). Fit strong but non-diagnostic. They prompted the state reading of chronic load, structural against deployed capacity, task-relative value, anticipatory economising, coupling as shared dependency, and using the model in reverse.
- **Limits:**
  - much of the layer 2 evidence was known in outline before the predictions were written;
  - the sources were read through summaries;
  - refinements A and B and the reserve knee were built from the literature;
  - the most informative predictions are untested against data: G3 across rates, G12, G18, F7 (whether energy demand moves the fasting threshold), G19 and G20. G12 and G18 are simulation results (TQ9).

## 10. Status, engine assumptions and working rules

**Status labels** for every major claim: **modelling choice**; **derived prediction**; **simulation result** (holds in the engine under its rules); **natural-system observation** (surface checks, with weight stated); **direct test** (pre-registered, against data not used to build the model; none yet); **compatible but non-diagnostic**; **unknown or contradicted**. Any value chosen after seeing an outcome is labelled **fitted**.

**Fitted so far:**
- the definition of a shortfall (chosen while reproducing G10);
- the skin's vital weight in the blood-loss check;
- the reserve's size cap and memory length;
- the economising thresholds, ceiling and response time;
- the default expectation beyond experience ("as much again as so far") and how fast episode length is learned;
- all rates and thresholds in the engine.

The deferred share of economised demand (0.5) was fitted, and is withdrawn with deferral.

**Engine assumptions** (results so far hold under the v0.15 rules):
1. the objective is persistence at a named level, then output;
2. a part's shortfall goes to the reserve, then to spare capacity of lower-priority parts, then displaced downhill; then debt or the boundary;
3. non-bypassable control is priced as a cliff;
4. damage saturates (a lost part becomes a fuse);
5. a part's value rises as its load approaches its current capacity;
6. the reserve's value is the expected shortfall (frequency), and its size also remembers the deepest shortfall;
7. recovery follows value, from slack pooled across parts (restoration cost uniform in the engine);
8. protection after a recovered episode is set by the peak load met, and fades;
9. economising is driven by the gap between the shortfall still expected and the reserve held, and splits into shed and debt;
10. overload is felt against current capacity (compounding).

**The v0.16 engine** (theory/sim/tq16.py, TQ10; the v0.15 engine is kept for TQ5 to TQ9). It implements the v0.16 rules, with protective slowing built in TQ10b (`slowing=True`; never below the demand floor). Without slowing, TQ10 found deterioration all-or-nothing. With it, deterioration is graded, and serious damage needs starvation below the demand floor or dose built over repeated slowing (theory/sim/outputs/2026-10-06_TQ10b/README.md). Open for James: whether control can override protective slowing (overuse scars), and whether a dependant's need falls in step when its supplier economises.

**Where the v0.15 engine departs from v0.16:**
- **Routing:** the engine moves a part's shortfall into receivers' spare capacity as work they do. Under v0.16 routing takes resources from the receivers.
- **Receivers' room** for load is never exhausted, so exhaustion cannot occur.
- **Repair** is pooled across parts, not each part refilling once its own leak stops.
- **Economising** defers half its cut as debt. A part's economised demand is counted as served for its dependants.
- **Scars** are set at a high exposure stage, not on template loss.
- **Still to come:** severance as an event, and several shared reserves (one shared reserve with local stocks at present).

The heart-failure spiral is partly reproduced (TQ9): where slack is small and the fall large, the loop raises strain and relieving the kidney removes it. The record did not break: there was always somewhere for load to go, which v0.16 reads as consistent with exhaustion, given that the engine's room never runs out.

**Evidence rule:** "no contributor was identified within the measured exposures" is not "no contributor existed". A null result on the exposures a study measured, at the times it measured them, does not show that no load entered elsewhere (also in CLAUDE.md).

**Standing check:** before anything enters the model, ask whether it follows from the existing rules once the system is mapped. If it does, it is an application note or a read-out, not a model element. Why a system does what it does (hormones, nerves, management decisions) is not the model's business; where load goes, where it lands and what it does to capacity is.

## 11. Way forward (James, 5 October 2026)

1. **Test, revise, test again,** in more natural systems, at surface level first, updating this file with each version.
2. **Keep the best datasets unopened** for a final stress test once the model is consistent (theory/tier_queue_heldout_datasets_DRAFT.md).
3. **Run full stress tests on those held-out datasets,** with predictions committed in advance.
4. **Only then, novelty** (theory/novelty_tier_queue_pass1.md and theory/tier_queue_provenance.md are kept for that stage).

## 12. Terms

- **Part:** a working part, including intakes and control parts. A reserve is not a part: it is a stock and does no work.
- **Demand:** the work asked of a part.
- **Work:** what only that part can do. Work never moves between parts.
- **Load:** demand beyond what a part's capacity or supply allows. It arises when throughput is maxed or supply is diverted. It is held at the part as deterioration, absorbed by other parts (resources taken from them, or backing up a dependency), or exported. Load is not work.
- **Reserve:** a stock that is drawn on and refilled. Spare capacity in a part is not a reserve.
- **Template:** what rebuilds a part like-for-like: its stem cells, scaffold, own boundary or living growth tissue.
- **Deterioration:** loss of capacity while load or work beyond capacity continues (the leak). Reversible once the leak stops and supply returns, if the template survives.
- **Scar:** lost capacity patched rather than rebuilt, after the template is lost or repair stalls. The patch keeps the part intact without its function.
- **Acute (a state):** load exceeds current capacity, but reserves, slack and a response are in place, so what the next task needs can be restored.
- **Attrition (a state):** the system deliberately draws reserves or tissue to sustain its current objective; it can be planned and reversible, and has no set length.
- **Chronic (a state, not a duration):** attrition or load without enough slack to restore the capacity the next task needs. Deterioration builds while the leak continues; ceilings fall only where templates are lost.
- **Suppression and remodelling:** deliberate reduction of a part's throughput (suppression) or structure (remodelling), reversed in full before the next task needs it. Neither is deterioration or compromise.
- **Economising:** the graded threshold switch. Control lowers working parts' demand and capacity together, reversibly, down to their demand floors. What it cuts is shed; it causes no deterioration.
- **Demand floor:** a part's minimum running cost.
- **Exhaustion:** outright failure when there is nowhere left for a part's load to go.
- **Severance:** outright failure when a non-bypassable link is cut, with willing receivers intact.
- **Incomplete recovery:** a part does not return to its previous capacity (a scar, or a loss in fixed capital).
- **Point of no return (system):** death, or the complete failure of an organ or of the system.

## 13. Open questions

- Is the threshold switch always protective (an active choice) or sometimes simply failure?
- Does a high-reserve system decline faster after its break? (Cognitive reserve suggests so; to check.)
- Restriction against starvation: does the type of load change the recovery order?
- What sets the boundary between "labelled" and "unlabelled" in natural systems?
- When does acute load give growth rather than re-tuning, and how long must recovery be for either?
- Are institutions able to grow or re-tune after strain, given that their deterioration is often unknown?
- What would distinguish dynamic priority from fixed priority plus role reassignment in data: order among parts that are not bottlenecks should be set by replaceability alone.
- **The remaining horizon.** What sets it in natural systems, and can it be measured independently of the order it predicts? Terminal investment and semelparity are the first cases to check.
- **The shortfall definition.** Check it against a case not used to build it: reserve enlargement after one severe acute episode should be smaller than after a long mild one with the same total load.
- **Episode length.** Do long episodes erode the protection of slow-rebuild parts (heart muscle in prolonged starvation against short acute load)? Not reproduced in the engine.
- **What signal starts anticipatory economising** in each system (temperature, day length, food, the reserve itself)?
- **Economising and the opaque trap.** An opaque system can escape the trap by economising, paying in shed commitments; the trap should return where load beyond capacity persists despite it.
- **Economising against growth (G17).** Check against controlled studies of training during energy deficit (same individuals followed), predictions committed first. **Cortisol as the state signal of economising:** it rises when the reserve is threatened and switches off growth, repair, reproduction and some immune work; the prediction is that, in the same individuals, training gains are smaller while it is raised. Blood sugar spikes test something else: release of reserve ahead of need, with glucose (normally a held output) moved deliberately by control.
- **The dose that destroys a template.** Is it predictable from a part's renewal class? When does a patch mature, in tissues other than the liver?
- **Relieving a part control cannot see** (from TQ9). With a part's state signal filtered, control prices it on its normal capacity. Cutting the demand on a part that has lost capacity then lowers its price, so it is spent first and absorbs load. In the engine, relieving the heart in the spiral made it worse unless the heart's signal reached control. This follows from the existing rules (opacity as signal gain) and is not a new element. Is there a natural case where relieving a damaged, unsignalled part leads to more load landing on it?
- **Price-clustered against dependency-clustered failure.** With a dependency map fixed first, do parts that share an input co-move before failing, while parts with similar prices but separate inputs strain in sequence?
- **How a system forms its expectation** of the shortfall ahead: does a first-ever episode of a kind trigger more precautionary economising than a familiar one?
- **Depletion against time:** the discriminating test needs the same depletion reached fast and slow, compared after the response lag.
- **Weight cycling.** Two weak results against G15 (female rats; one null study) to read in full.
- **Horizon against budget:** tests of the horizon term need the budget held constant while the horizon shrinks (held from the third review).
- **Expected shortfall against integral windup.** The same total deficit as one block or scattered at random. The engine cannot yet tell unpredictability from frequency.
- **How a part raises its no-strain ceiling within days** while its maximal force is still reduced: below the model's level; candidate mechanisms are not the model's to choose.
- **Two boundaries** (held). Load that leaves only the record's accounts, not the system, may return unlabelled and hit neighbours. Needs a natural case.
- **A clean layer 2 test:** an easily reached but valuable reserve, held while less valuable ones are drawn.
- **Vital weights:** which independent sources give them reliably?
- **Whose persistence.** Where the level is unclear (a mother and fetus, a colony and its workers), does setting the objective at each level give different, checkable orders?
