# The tier-queue model, v0.15 (canonical state, 5 October 2026)

**Status:** working model (phase 3).

This is the single reference for the model as it stands. v0.15 consolidates v0.14: the content is the same, version tags have been taken out of the body, and the history is in theory/tier_queue_changelog.md. The maths is in theory/tier_queue_math_v0.15.md; the engine is theory/sim/tq_core.py, specified in theory/tier_queue_core_spec.md. Changes go into new versions, with what changed and why recorded in the changelog.

![Tier-queue model](figures/tier_queue_diagram_v015.png)

## 1. The principle

**Central claim** (confirmed by James, 5 October 2026; a plainer version for abstracts and short pieces is to come, with this statement kept as the reference):

> In a goal-directed system with finite-capacity parts and limited reserves, load is routed according to each part's current marginal value to the persistence of the level being protected, judged against the next task that persistence depends on. The system holds its routine output steady by drawing reserves, passing load to lower-value or expendable parts, reducing or reshaping their work, deferring it as debt, or exporting it. So the record sees compromise, not stress: it moves only when the buffers, sacrificial parts and routing capacity can no longer absorb the demand. Recovery runs the other way. It begins once demand falls below current capacity, rebuilds the intake and the capacity the next task needs first, and refills reserves according to how scarce the system has learned its world to be. Attrition becomes a scar only when there is not enough slack to restore what the next task needs: that state, not the passage of time, is what makes load chronic.

**In parts.** A goal-directed system is a network of parts. Priority, which is dynamic, sets the routing; it needs no strict hierarchy, and dependencies can form loops. Each part does work and has a limited capacity. When demand exceeds what a part can do, the excess is not removed: it is drawn from a reserve, passed to parts of lower priority, deferred as debt, or sent out across the boundary.
- Load therefore runs downhill, from protected parts to expendable ones.
- The protected part's output, which is what the system records, stays normal while the parts below absorb the excess. It changes only when they can absorb no more. **The record sees compromise, not stress.**
- Recovery runs the other way, starting with the intake. It begins once demand falls below what a part can currently do, so no new excess is generated; it does not need demand to stop. Debt nobody knows about is never repaid (a prediction about unobserved state, not a universal law).
- Priority is not a fixed rank. It is each part's current value to the system's persistence, which changes with the part's state and the situation.
- What a system becomes after an episode depends on its state, not its length. Load that is signalled and recovered from with slack (the acute state) can leave a part stronger, or leave the system re-tuned to that threat. Load without enough slack to restore what the next task needs (the chronic state) leaves scars, and parts that cannot be rebuilt keep their losses.

## 2. The parts

| Kind | What it is | Examples |
|---|---|---|
| **Working part** | Does a job with a limited capacity | Brain, heart, nephron, nurse bee, front-line staff |
| **Intake** | A working part whose job brings resource in. Every repayment depends on it | Gut, leaves, roots, foragers, a referral or recruitment function |
| **Control part** | A working part whose job is routing. It holds the threshold switch. Priced as a cliff only when it is a necessary, non-bypassable routing bottleneck; distributed, redundant or bypassable control is priced like any other part | Vasomotor centre, hypothalamus, an institution's management (non-bypassable); a honeybee colony's task allocation (distributed) |
| **Reserve** | A stock that is drawn on and refilled. It runs full, drawing or empty, and is not itself damaged | Fat, iron stores, venous blood volume, honey stores, budget reserves |

A reserve is a stock. Spare capacity (headroom) in a working part is not a reserve: "contractile reserve" or "cognitive reserve" are redundancy and compensation. The brain holds almost no fuel stock; it is protected through priority of supply, redundancy and compensation.

Each working part has these properties:
- a **capacity**;
- how **vital** it is: the share of the system's persistence that depends on it;
- a **renewal class**, which sets its **rebuild time**: fast (a conveyor such as the gut lining), slow (liver), or none (fixed capital: neurons, heart muscle);
- a **ceiling**, lowered by scars or raised by growth after acute load;
- its **spare capacity** (redundancy), which enters through its value (Section 3);
- its **structural capacity** and its **deployed throughput**, which can differ. A part may deliberately run below its structural capacity: **suppression** (a hibernating bear's kidney filters less while nitrogen is recycled elsewhere) or **remodelling** (a migrating bird's gut shrinks for a non-stop flight and is rebuilt at stopover). Reduced throughput with structure intact is suppression, not compromise; reduced structure rebuilt before the next task is remodelling, not a scar. Compromise means structural capacity lost and not restored.

A part's priority is not one of its properties. It is computed from them and from the part's current state (Section 3).

**State, for working parts:**
- **Optimal:** within capacity, reserve full.
- **Stressed but coping:** covering the excess from reserve, spare capacity or debt still within its recovery window. Protective slowing begins here, giving up some capacity to protect the part.
- **Compromised:** debt held beyond the recovery window, so capacity is eroding.

Losses compound, because overload is felt against what the part can do now, not what it could do before.

## 3. Priority

**The objective.** Every system's first objective is its own persistence; its output comes second. A system cannot do its function if it no longer exists. This holds for every system the model is applied to; there is no separate slot for an institution's stated purpose.

**Whose persistence.** The mapping names the level whose persistence $W$ measures. Parts can be spent for the level above when $W$ sits there: a worker bee dies for the colony, and a Pacific salmon, an octopus or an agave spends its whole body on reproduction. Setting $W$ one level too low predicts the wrong order, so these cases test the model.

**Marginal value.** A part's value at time *t* is how much the system's persistence would lose if the part lost a unit of capacity:

$$v_i(t)=\frac{\partial W}{\partial c_i}\bigg|_t$$

It is a shadow price, judged against the **next task** persistence depends on: a migrating bird's gut is valuable at stopover and payload in flight. It is near zero for a part with spare capacity, or for one whose work is not needed now (the gut when there is no food), and high for the part that limits the system. In the engine, $v_i=\text{vital}_i\times b(L_i)$, where $b$ rises from 0.05 to 1 as the demand the part carries (its own plus any passed to it) approaches its current capacity.

**Non-bypassable control is priced as a cliff.** Where control is a necessary, non-bypassable routing bottleneck (every routed unit passes through it), losing it breaks routing for the whole system, so its value is its full vital weight ($b=1$), not its own workload. Natural systems with central control protect it to the end (the brain in starvation and in blood loss). Distributed, redundant or bypassable control (a colony's task allocation; local reflexes; systems that can route around a damaged node) is priced by its marginal value like any other part. Which kind a system has is a mapping decision, made before predicting.

**One value, two decisions:**

| Decision | Formula | Meaning |
|---|---|---|
| **Who pays first** under load | Ascending $p_i=v_i\,s_i\,\min(\tau+h_i,\;T)$ | What the system loses if the part is spent: its value now ($v_i$), times the share of its capacity still at stake ($s_i$), times how long the system would go without it: the rest of the episode ($\tau$) plus the part's rebuild time ($h_i$; very large for fixed capital), never more than the remaining horizon ($T$). $T$ can be the deadline of the next task persistence depends on (the next flight, the next winter) rather than the remaining life |
| **Who is rebuilt first** in recovery | Descending $q_i=v_i/k_i$ | Value restored per unit of resource ($k_i$: the cost of restoring a unit of capacity) |

**The terms of the spending cost.**
- **Time without the part.** Losing a part costs its value for as long as the system goes without it: the rest of the episode, $\tau$, plus its rebuild time, $h_i$, but never longer than the system has left, $T$. The system must estimate $\tau$; the engine uses the length of the current episode so far.
- **Consequences of the time term.** With a long horizon, fixed capital is the dearest thing to spend. As the horizon shortens, or as an episode lengthens, spending a part that cannot be rebuilt costs little more than spending one that can. A system whose prospects are falling therefore spends parts it used to protect (terminal investment, with the objective set at the level of the lineage). Long episodes should likewise erode the protection of slow-rebuild parts; **this was not reproduced in the engine**, where a strained fast part stays the fuse (open).
- **Capacity still at stake.** Damage saturates: a part can lose only what it still has, so $s_i$ runs from 1 (healthy) to 0 (at its floor). A part that has lost all it can lose costs nothing more to load. It becomes the system's **fuse**, and load is concentrated on it rather than spread (leaves and fine roots in drought; old leaves shed first).

**When spending by marginal value is the best policy.** Spending in ascending order of marginal value is optimal only when each part's returns diminish and parts can be priced separately (a concave, separable objective: the water-filling solution). Three departures matter:
1. **Saturating damage** favours concentration on a sacrificial part over spreading: the fuse, handled by $s_i$.
2. **Cliff-shaped losses** (a non-bypassable part whose loss breaks the whole system) are never priced at the margin.
3. **Increasing returns to an output** make the best choice all or nothing. A short horizon alone erodes protection gradually; spending the whole body (semelparity: Pacific salmon, octopus, agave) needs a short horizon and increasing returns to reproductive effort (in agave, pollinators favour taller flowering stalks). Not yet in the engine, which has no explicit objective.

**The reserve's value is the expected shortfall:** how likely the system is to face demand above its capacity, learned from experience (in the engine, how often total demand has recently exceeded total current capacity). Chronic or unpredictable scarcity therefore raises the reserve's value and its place in the recovery order.

**The reserve also remembers the worst it has met.** Like a part (Section 4, item 8), the reserve is peak-referenced: an episode whose total shortfall exceeded the reserve's base size enlarges the reserve towards that depth, and the memory fades on the system's own clock. **Frequency sets the order; depth sets the size.** After a single severe acute episode, the reserve is still refilled after the working parts (G10), but to a larger size than before. Repeated episodes raise both: the system holds a larger reserve and refills it earlier.

**Control sees value through state signals.** In a coupled system the signals carry the demand each part actually carries, including what was passed to it. In an opaque one, control sees only nominal demand against nominal capacity, so a strained lower part looks as if it has spare capacity: **opacity corrupts the priority calculation itself, not only the routing.** Even in natural systems, a signal that stays high loses gain over time (adaptation, as in baroreceptor resetting), so long-lasting strain is undervalued.

**What this explains that a fixed ranking only asserted:**
1. a redundant organ that cannot be rebuilt (the kidney) is cut after cheap tissue (gut, skin);
2. the gut is spent first in a fast and rebuilt first at refeeding: its value changes, not a rank;
3. the recovery order after acute and after chronic load (G10) follows from the reserve's expected-shortfall value;
4. "next demand", dependency (a dependent infant's muscle has low value) and insurance are all expressions of value;
5. with a shrinking horizon, parts that cannot be rebuilt lose their protection (the terminal-investment direction; shown in the engine, not yet checked in natural systems);
6. under saturating damage, a lost part becomes a fuse and takes the load (shown in the engine; consistent with plant hydraulic fuses).

## 4. How the parts interact

1. **Routing.** A part's shortfall goes first to the reserve, then to spare capacity in lower-priority parts, then is displaced onto them (lowest first). Priority here is the spending order of Section 3. Whatever cannot be placed becomes the part's own debt, or leaves across the boundary.
2. **Labelled and unlabelled load.** Load that arrives with its origin can be refused by a part already under strain, which keeps the strain visible higher up. Load passed on through opacity has no origin, so it cannot be refused and sinks to the lowest tier.
3. **Coupling.**
   - **Shared supply.** A protected part depends on upstream supply, so it is protected only partly when that supply falls (brain flow falls with cardiac output).
   - **Coupling is shared dependency.** Parts are coupled when they share an input, a stressor, a reserve or the machinery that repairs them, not when they are the same type of part. The links form a network, and displaced load can travel back to the part that started it: in heart failure, the kidney's retention of fluid lands as extra load on the heart, whose weakness triggered it. That loop is displacement over a network; it needs no new mechanism.
   - **Shared dependency synchronises strain.** Parts loaded through the same input strain together. Before any of them crosses a visible threshold, their state signals move together more and more; when their buffers run down together, the break is sharp. Where buffers are separate and run down at different times, the combined break is smooth.
4. **Threshold switch.** At a set point, not at exhaustion, control changes mode: it sheds a commitment, changes metabolism or behaviour, and often makes the record move. The set point lies in the gap between the shortfall still expected and the reserve held; with nothing more expected, it is a set depletion of the buffer.
   - **Economising, the graded form of the switch.** The system cuts the running demand of its working parts below what their current size needs (in a body: less heat, less activity, reproduction and immune work cut). It follows an S-curve in the gap between the shortfall still expected and the reserve held: zero below a threshold, rising, then levelling at a floor set by what must be protected (the top and non-bypassable control are never cut). What the system expects: for a predictable episode (a season, a known fast), the remaining need is known, so economising starts at onset, before the reserve is drawn (a bear entering its den); for a kind of episode met before, the usual length; beyond its experience, as much shortfall again as so far. Time matters only through what it does to the expected shortfall and the reserve. Economising eases as the reserve is refilled, not when supply returns, so it persists into refeeding and the reserve is refilled faster than intake alone allows (catch-up fat). A short restriction that never brings the gap to the threshold triggers none of it; breaks long enough to refill the reserve prevent it.
   - **The ledger.** Economised demand is not removed. It splits into **shed commitments**, which cross the boundary for good (heat not made, activity and reproduction forgone), and **deferred maintenance**, which becomes the part's debt and is repaid from slack later (repair, immune work). The share deferred is a property of the part, fixed from sources when mapping. The more is deferred, the deeper the reserve is drawn and the slower recovery is: borrowing is not saving.
   - **Value and expected shortfall are measured against normal demand.** The system's own economising does not change what a part is for, and does not count as the environment easing.
   - **Economising and growth compete.** Economising spares working parts and the record, which removes the strain that growth needs (G17).
5. **Control failure.** If debt reaches the control part, routing stops following priority: protected parts are hit while buffers remain (division of labour breaks down in collapsing colonies).
6. **Compounding on survivors.** Parts carrying displaced or covered load are damaged by it, and their failure adds load to the rest: hyperfiltration in the kidney, precocious foraging in bees, the vacancy cascade in teams.
7. **Recovery.**
   - Slack repays debt and refills reserves, in descending value (Section 3). The order therefore depends on the state the past load left:
     - after **acute** deprivation: intake first, then the working parts the next task needs, then reserves;
     - after a **chronic** state of scarcity: the system expects more scarcity, and the reserve is enlarged first, often overshooting; lean and working tissue follow more slowly;
     - after a **single severe** episode: reserves still come last, but are refilled to a larger size, which lasts.
   - **The intake comes first whenever it was run down.** It is spent early when there is nothing to take in, and rebuilt first when supply returns.
   - **Speed and order are different things.** How fast a part recovers depends on its renewal rate; the order in which resources go to parts is priority. The gut has both: fast renewal, plus resources diverted to it at refeeding.
   - Recovery requires slack: demand below current capacity. It does not need demand to stop, so partial recovery under reduced demand is expected.
   - After compromise, renewable parts return with a scar (a lower ceiling, a shorter tolerance window, more resistance). Fixed capital keeps its loss: the point of no return.
8. **What the system becomes after an episode.** Four outcomes, which can occur together in different parts:
   - **Growth:** capacity rises above its old level. Conditions: the load was acute, state signals reached control (coupling), slack followed, the part is renewable, and the challenge strained the part without threatening the reserve (otherwise economising spares the part and removes the stimulus). Examples: muscle after hard work; an institution that sees staffing strain and adds capacity.
   - **Re-tuning:** the system changes demand, allocation, thresholds or reserve size in line with the threat it met; capacity need not change. **Protection is set by the peak load met, not by cumulative load:** after a recovered episode, a part carries loads up to that peak without strain; above it, strain builds at a reduced rate; the protection above normal capacity fades with time; a scar removes it. This holds even while the part is still recovering, so repeated loading at or below the earlier peak during recovery adds no damage. Examples: spruce cutting leaf area after drought; small birds carrying more fat when food is unpredictable; brief ischaemia protecting the heart against a later, larger one.
   - **Scar:** a lower ceiling after compromise. A scar can also cut **demand** (spruce leaf area); whether a past injury makes a system more or less vulnerable depends on whether it cut demand more than capacity.
   - **Loss:** fixed capital keeps what it lost.

   **The acute-chronic flip:** the same kind of load can produce growth when the system is in the acute state (signalled, buffered, recovered from with slack), and damage when it is in the chronic state (not enough slack to restore what the next task needs). **The state decides, not the duration:** a short episode that leaves a scar has made the part chronic; a long, prepared and buffered episode need not (a hibernating bear fasts for months with muscle and bone preserved; a migrating bird repeats planned attrition every year).

   **The cost of re-tuning:** if conditions change, a system tuned to a past threat can be mistuned for the new one (to test).
9. **Starting state.** A system need not start optimal. Its stage at the start sets how much room it has, and is read from state signals, because the record cannot show it.

## 5. Read-outs

- **The record:** the output the system routinely watches, which is the top's served demand. It is flat through stress and moves at compromise, or at the switch.
- **The record's dynamics.** The record's level is silent until the break, but its dynamics need not be. A small knock leaves a deficit that the reserve restores at its release rate $\rho(R)$, so recovery takes about knock $\div\,\rho(R)$. Where release tapers as the reserve shrinks, recovery time rises as $1/R$ and grows without limit as the reserve empties: the record recovers more slowly from each knock, and its autocorrelation and variance rise while its mean stays flat (critical slowing down). Where release stays at full rate until a switch, the break comes with no warning in the record. When state signals are filtered, watch how long the record takes to recover, not where it sits (G12).
- **State signals:** each part's strain, debt, capacity and reserve level. They move from the start of stress. In opaque systems they are filtered, mistranslated or lost. Each is judged against the system's own reference state for its current phase.
- **Co-movement across parts.** Where parts share a loaded dependency, their state signals move together more and more before any of them crosses a visible threshold, and before the record moves (G18). Rising co-movement points to a shared input upstream.
- **Where strain begins (the Felicity read-out).** Raise the load and note where strain signals first appear ($D_{\text{on}}$). Compare it with the part's previous peak load ($D^\ast$) and its normal capacity ($\kappa c$):
  - $D_{\text{on}}\ge D^\ast$ (Felicity ratio $F=D_{\text{on}}/D^\ast\ge1$): protected, or grown;
  - $\kappa c\le D_{\text{on}}<D^\ast$: protected, but the protection is fading;
  - $D_{\text{on}}<\kappa c$: scarred (compromised).

  It separates "recovering" from "scarred", which the record cannot, and needs no record at all. It follows from the re-tuning and scar rules (G7, G8).
- **The ledger:** demand = work done + reserves drawn + debt + load leaving the boundary. Nothing leaves the ledger except through work done or the boundary.
- **Reading a compensating part's output** (insulin, brain-sparing blood flow): it rises while the part copes and falls when it is compromised. A fall is therefore ambiguous: the load may have eased, or the compensator may be failing. Check the load at its source before reading a fall as improvement.

## 6. Mapping a system

Do this before opening any outcome data.

1. **Boundary and currency.** Name the system and its boundary, and choose a currency that obeys a balance (energy, blood volume, filtration, labour hours, cases). Name whose persistence the objective measures (the organism, the colony, the lineage), and which parts may be spent for that level.
2. **Demand and load.** What work is asked of each part, and from where? Where can it exceed capacity, and so become load?
3. **The record.** What figure does the system, or its observer, routinely watch and defend? It must be a **held output:** delivered below capacity, and kept up by buffers or a defending loop. A capacity test (maximal force, a time trial, a stress test) or a direct measure on the working units (nerve-fibre thickness, synapse counts, the control hormone) is a state signal, not the record.
4. **The top.** Which part's output is that figure? Is it fixed capital? This is the only part whose place is named in advance; every other part's priority is computed.
5. **The parts.** List the parts that do work. For each, decide:
   - its **role**: working, intake or control; for control, whether it is non-bypassable or distributed, redundant or bypassable;
   - how **vital** it is to the system's persistence;
   - its **renewal class** and rebuild time;
   - how much **spare capacity** it normally has;
   - for an intake, what it takes in, and when that is unavailable;
   - the share of its economised demand that would be deferred maintenance.

   **Fix these from independent sources before predicting any order:** lesion or knockout studies, regeneration and turnover rates, the cost of rebuilding tissue. Log each source. A value chosen with the expected order in mind is declared as such, and that part of the result counts as fitted.
6. **The reserves.** Which stocks are drawn first? Does release slow as they shrink?
   - **The remaining horizon.** How long are the system's prospects (life stage, season, age, the next task's deadline)? Is it shrinking?
   - **The system's clock.** Fix the unit in which durations are judged before checking anything: the reserve's refill time, a part's rebuild time, decision cycles, generations, depending on the level the objective measures. "Brief", "lasting" and "permanent" are claims on that clock.
   - **Expected episodes.** Which episodes are predictable (seasons, known fasts), and what is the typical length of familiar ones?
7. **Labelled or not, and dependencies.** Does load passed down arrive with its origin? Can the receiver refuse it? Do state signals reach the top? Which parts share an input, a stressor, a reserve or repair machinery? Draw these links: they decide which parts should strain together.
8. **Control and the switch.** What routes load? Is there a known mode change, and at what point (the gap between expected shortfall and reserve; with nothing expected, a set depletion)?
9. **State signals.** For each part, what measure shows its strain, debt or reserve? Judge each against the system's own reference state for its current phase: a hibernating bear's creatinine read against an active-season range would misread coping as failure.
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

Reverse mode has to know which route it is looking at.

## 8. Generic predictions

**Two layers.** Some predictions hold for any negative-feedback loop with a finite stock, with no goal at all (a star leaves the main sequence with most of its hydrogen unburned; Earth's carbonate-silicate thermostat). Confirming them is cheap and says nothing about priority. Others need selection or design. Each prediction and each piece of evidence is tagged **layer 1** (any finite-stock feedback loop) or **layer 2** (needs selection or design).

| No. | Prediction | Layer | Status |
|---|---|---|---|
| G1 | The record stays near normal while state signals and reserves move | 1 | Natural observation: consistent in all surface tests (non-diagnostic for priority) |
| G2 | Lower-priority parts are drawn down first, in reverse priority | 2 | Natural observation: consistent (blood loss, fasting, bees); known in outline beforehand |
| G3 | The break comes at a set depletion of the buffer, not at exhaustion. If the buffer is a stock, the break comes at the same cumulative load whatever the rate | 1 | Natural observation: partly consistent (sheep rate-independence; fasting threshold at a fat share); stress-test candidate (H1, H2) |
| G4 | A larger buffer gives a longer silence and a sharper break; a stressed or compromised start breaks sooner | 1 | Natural observation: consistent (heat stress, initial fat, low nephron number); stress-test candidate |
| G5 | Survivors that carry extra load are damaged by it, so loss compounds | 1 | Natural observation: consistent (kidney hyperfiltration, precocious foraging) |
| G6 | Recovery runs intake first and reserves last, and needs slack. Unknown debt is not repaid, so the record recovers before the state does | 2 (order); 1 (record before state) | Natural observation: consistent for record before state (kidney); order, see G10 |
| G7 | Parts that cannot be rebuilt keep their losses; renewable parts return with a scar | 1 | Natural observation: consistent (nephrons, spruce, scarred muscle) |
| G8 | Load that is signalled and recovered from with slack (the acute state) leaves growth or re-tuning. Load without enough slack to restore what the next task needs (the chronic state) leaves scars. The same load can do either: the state decides, not the duration | 2 | Natural observation: consistent (muscle, fetal hypoxia); simulation result (TQ7, TQ8) |
| G9 | A system re-tuned to a past threat does better against that threat again, and may do worse if conditions change. Tests must follow the same individuals: at population level, the death of the susceptible mimics re-tuning | 2 | Natural observation: partly consistent (starlings, primed plants); cost of mistuning not found |
| G10 | After acute deprivation (recovered with slack), working tissue and intake recover before reserves. After a chronic state of scarcity, reserves recover first and overshoot | 2 | Natural observation: consistent (recovery-order test); simulation result, with a fitted shortfall definition (TQ8) |
| G12 | **Record dynamics.** Where reserve release tapers as the reserve empties, the record recovers more slowly from small knocks as the break approaches, with rising autocorrelation and variance at a steady mean. Where release is full until a switch, the break gives no warning in the record | 1 (conditional on the release profile) | Derived prediction (maths); untested; blood-loss contamination declared |
| G13 | **Fuses.** Once a part has lost what it can lose, further load is concentrated on it rather than spread to healthy parts | 2 | Simulation result (TQ8); compatible but non-diagnostic (plant fuses); prepared systems (bears, migrants) show remodelling rather than fuses |
| G14 | **Peak-referenced protection.** After a recovered episode, strain signals appear only above the previous peak load; protection depends on that peak, not on the volume of the episode; it fades with time; after a scar, strain appears below normal capacity | 2 | Natural observation: partly consistent (muscle, natural test 11); simulation result (TQ8 C7) |
| G15 | **Reserve memory.** After a shortfall deeper than the reserve's base size, the reserve is enlarged towards that depth and stays enlarged for longer than after shallower ones, on the system's own clock. After a single acute episode it is still refilled after the working parts. Repeated episodes enlarge it and raise its place in the refill order. At equal total load, one deep episode leaves a larger reserve than several shallow ones unless the shallow ones are frequent enough to raise the expected shortfall | 2 | Simulation result (TQ8 C8; cap and memory fitted); natural observation: partly consistent (weight cycling, natural test 12) |
| G16 | **Economising.** Running demand is cut when the shortfall still expected outruns the reserve held: at onset for a predictable long episode, later (with depletion) for an open-ended one, not at all for short episodes of a learned length. It levels off at a floor, never touches protected parts, and persists until the reserve is refilled | 2 | Simulation result (TQ8 C9, C10); compatible: intermittent restriction, bear hibernation |
| G17 | **Economising and growth compete.** A challenge that threatens the reserve triggers economising, which spares working parts and the record but removes the strain that growth needs. Growth after acute load needs strain without economising | 2 | Simulation result (TQ8 C11); not yet checked in natural systems |
| G18 | **Co-movement before the break.** Where parts share a loaded dependency, their state signals move together more and more before any of them crosses a visible threshold, and before the protected output moves. The break is sharp where their buffers run down together and smooth where separate buffers run down at different times. Parts clustered only by spending price strain in sequence without this co-movement | 1 (shared dependency) and 2 (against price clustering) | Derived prediction; untested; candidate test in a repeated-measures cohort (UK Biobank, reserve list R6), with a dependency map fixed first |

G11 was withdrawn and is not reused; internal numbers keep the gap, and any public version is renumbered with a crosswalk.

**The test only layer 2 can pass:** a reserve that is easy to reach but valuable. Drawing in order of access would spend it; drawing by value would hold it. A clean natural case is still to find (muscle glycogen is weak: muscle lacks the enzyme to release it as blood glucose, so its retention is fixed design).

## 9. Evidence so far, and its weight

- **Simulations TQ1 to TQ8** (illustrative parameters). TQ8 (theory/sim/outputs/2026-10-05_TQ8/README.md) shows computed priority reproducing the earlier results without hand-set ranks, and checks each later element.
- **Surface checks in natural systems:** blood loss, fasting, kidney, honeybees, plants under drought, fetal growth restriction, recovery order, muscle injury against disuse, the record rule, re-tuning (natural tests 1 to 10), the Felicity read-out in muscle (test 11) and weight cycling (test 12) (theory/natural_test_*.md; theory/natural_tests_patterns.md). All broadly consistent; each mismatch led to a refinement, and unexplained or contrary items are logged in those files (for example, female rats did not lose weight more slowly in a second cycle).
- **By layer** (detail in theory/natural_tests_patterns.md):
  - **layer 1 only:** the kidney test and the record-rule test;
  - **layer 2 evidence:** the order of loss in blood loss and in fasting; the fasting switch; honeybee allocation; hydraulic fuses and the spruce demand cut; fetal brain sparing and the acute-chronic flip; recovery order after acute against chronic scarcity; growth against scar in muscle; re-tuning; peak-referenced protection in muscle; faster regain after weight cycling;
  - **layer 1 parts of the other tests:** the flat record and break at a set depletion; rate-independence (sheep); starting state.
  - **Re-tuning evidence and individuals:** starlings, preconditioning, primed plants, fetal sheep and muscle followed individuals; the human food-insecurity link is population-level; spruce survivor filtering is not ruled out (to check).
- **Exploratory applications, not tests:** a reviewer applied the model to systems it chose arbitrarily (hibernating bears, migratory birds, heart failure, a cardiometabolic disease cluster), looking at evidence after choosing (raw/2026-10-05_perplexity_*.md). Fit strong but non-diagnostic. They prompted the state reading of chronic load, structural against deployed capacity, task-relative value, anticipatory economising, coupling as shared dependency, and using the model in reverse.
- **Limits:** much of the layer 2 evidence was known in outline before the predictions were written; the sources were read through summaries; refinements A and B and the reserve knee were built from the literature; the most informative predictions (G3 across rates, G12, G18, F7 on whether energy demand moves the fasting threshold) are untested.

## 10. Status, engine assumptions and working rules

**Status labels** for every major claim: **modelling choice**; **derived prediction**; **simulation result** (holds in the engine under its rules); **natural-system observation** (surface checks, with weight stated); **direct test** (pre-registered, against data not used to build the model; none yet); **compatible but non-diagnostic**; **unknown or contradicted**. Any value chosen after seeing an outcome is labelled **fitted**.

**Fitted so far:** the definition of a shortfall (chosen while reproducing G10); the skin's vital weight in the blood-loss check; the reserve's size cap and memory length; the economising thresholds, ceiling and response time; the default expectation beyond experience ("as much again as so far") and how fast episode length is learned; the deferred share of economised demand (0.5); all rates and thresholds in the engine.

**Engine assumptions** (results hold under these rules):
1. the objective is persistence at a named level, then output;
2. a part's shortfall goes to the reserve, then to spare capacity of lower-priority parts, then displaced downhill; then debt or the boundary;
3. non-bypassable control is priced as a cliff;
4. damage saturates (a lost part becomes a fuse);
5. a part's value rises as its carried demand approaches its current capacity;
6. the reserve's value is the expected shortfall (frequency), and its size also remembers the deepest shortfall;
7. recovery follows value (restoration cost uniform in the engine);
8. protection after a recovered episode is set by the peak load met, and fades;
9. economising is driven by the gap between the shortfall still expected and the reserve held, and splits into shed and debt;
10. overload is felt against current capacity (compounding).

**Engine limitations:** no loops in which one part's response adds demand to another; a single reserve; no restoring dynamics in the record. So G12, G18 and the heart-failure spiral are written in the model but not yet simulated.

**Evidence rule:** "no contributor was identified within the measured exposures" is not "no contributor existed". A null result on the exposures a study measured, at the times it measured them, does not show that no load entered elsewhere (also in CLAUDE.md).

**Standing check:** before anything enters the model, ask whether it follows from the existing rules once the system is mapped. If it does, it is an application note or a read-out, not a model element. Why a system does what it does (hormones, nerves, management decisions) is not the model's business; where load goes, where it lands and what it does to capacity is.

## 11. Way forward (James, 5 October 2026)

1. **Test, revise, test again,** in more natural systems, at surface level first, updating this file with each version.
2. **Keep the best datasets unopened** for a final stress test once the model is consistent (theory/tier_queue_heldout_datasets_DRAFT.md).
3. **Run full stress tests on those held-out datasets,** with predictions committed in advance.
4. **Only then, novelty** (theory/novelty_tier_queue_pass1.md and theory/tier_queue_provenance.md are kept for that stage).

## 12. Terms

- **Demand:** the work asked of a part.
- **Load:** what spills over beyond a part's capacity, held as latent load (debt) or displaced to another part. Load is not work.
- **Reserve:** a stock that is drawn on and refilled. Spare capacity in a part is not a reserve.
- **Acute (a state):** load exceeds current capacity, but reserves, slack and a response are in place, so what the next task needs can be restored.
- **Attrition (a state):** the system deliberately draws reserves or tissue to sustain its current objective; it can be planned and reversible, and has no set length.
- **Chronic (a state, not a duration):** attrition or load without enough slack to restore the capacity the next task needs. Debt goes unrepaid and ceilings fall.
- **Suppression and remodelling:** deliberate reduction of a part's throughput (suppression) or structure (remodelling), reversed before the next task needs it. Neither is compromise.
- **Economising:** the system's own cut in the running demand of its working parts; split into shed commitments and deferred maintenance.
- **Incomplete recovery:** a part does not return to its previous capacity (a scar, or a loss in fixed capital).
- **Point of no return (system):** death, or the complete failure of an organ or of the system.

## 13. Open questions

- Is the threshold switch always protective (an active choice) or sometimes simply failure?
- Does a high-reserve system decline faster after its break? (Cognitive reserve suggests so; to check.)
- Restriction against starvation: does the type of load change the recovery order?
- What sets the boundary between "labelled" and "unlabelled" in natural systems?
- When does acute load give growth rather than re-tuning, and how long must recovery be for either?
- Are institutions able to grow or re-tune after strain, given that their debt is often unknown?
- What would distinguish dynamic priority from fixed priority plus role reassignment in data: order among parts that are not bottlenecks should be set by replaceability alone.
- **The remaining horizon.** What sets it in natural systems, and can it be measured independently of the order it predicts? Terminal investment and semelparity are the first cases to check.
- **The shortfall definition.** Check it against a case not used to build it: reserve enlargement after one severe acute episode should be smaller than after a long mild one with the same total load.
- **Episode length.** Do long episodes erode the protection of slow-rebuild parts (heart muscle in prolonged starvation against short acute load)? Not reproduced in the engine.
- **Where economised demand lands:** what share is deferred in each natural system (a mapping value to fix from sources)?
- **Economising and the opaque trap.** An opaque system can escape the trap by economising, paying in shed commitments and deferred debt; the trap should return where deferred debt cannot be repaid before the next load.
- **Economising against growth (G17).** Check against controlled studies of training during energy deficit (same individuals followed), predictions committed first. **Cortisol as the state signal of economising:** it rises when the reserve is threatened and switches off growth, repair, reproduction and some immune work; the prediction is that, in the same individuals, training gains are smaller while it is raised. Blood sugar spikes test something else: release of reserve ahead of need, with glucose (normally a held output) moved deliberately by control.
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
