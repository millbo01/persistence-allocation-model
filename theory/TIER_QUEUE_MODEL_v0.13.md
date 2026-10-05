# The tier-queue model, v0.13 (canonical state, 5 October 2026)

**Status:** working model (phase 3).

This is the single reference for the model as it stands. Earlier documents are its working history: theory/tier_queue_model_DRAFT.md, theory/tier_queue_core_spec.md, theory/sim/tq_core.py, the natural test files, and versions v0.1 to v0.12. The maths is in theory/tier_queue_math_v0.4.md and, for priority, theory/priority_formula.md. Changes go here as new versions, with what changed and why.

![Tier-queue model](figures/tier_queue_diagram.png)

## 1. The principle

**Central claim (v0.12; from the Perplexity review, combined with the record line and the recovery half at James's request). Confirmed by James (5 October 2026). James may revise it for readability: abstracts and short versions may need a plainer form, with this statement kept as the reference.**

> In a goal-directed system with finite-capacity parts and limited reserves, load is routed according to each part's current marginal value to the persistence of the level being protected, judged against the next task that persistence depends on. The system holds its routine output steady by drawing reserves, passing load to lower-value or expendable parts, reducing or reshaping their work, deferring it as debt, or exporting it. So the record sees compromise, not stress: it moves only when the buffers, sacrificial parts and routing capacity can no longer absorb the demand. Recovery runs the other way. It begins once demand falls below current capacity, rebuilds the intake and the capacity the next task needs first, and refills reserves according to how scarce the system has learned its world to be. Attrition becomes a scar only when there is not enough slack to restore what the next task needs: that state, not the passage of time, is what makes load chronic.

**In parts:** a goal-directed system is a tree of parts. Each part does work and has a limited capacity. When demand exceeds what a part can do, the excess is not removed. It is drawn from a reserve, passed to parts of lower priority, deferred as debt, or sent out across the boundary.
- Load therefore runs downhill, from protected parts to expendable ones.
- The protected part's output, which is what the system records, stays normal while the parts below absorb the excess. It changes only when they can absorb no more. **The record sees compromise, not stress.**
- Recovery runs the other way, starting with the intake. It begins only once demand falls below what a part can currently do, so no new excess is generated. It does not need demand to stop. Debt nobody knows about is never repaid (a prediction about unobserved state, not a universal law).
- **Priority is not a fixed rank (v0.5).** It is each part's current value to the system's persistence, which changes with the part's state and the situation.
- **What a system becomes after an episode depends on its state, not its length (v0.12; James: chronic is a state and can have no timeline).** Load that is signalled and recovered from with slack (the acute state) can leave a part stronger, or leave the system re-tuned to that threat. Load without enough slack to restore what the next task needs (the chronic state) leaves scars, and parts that cannot be rebuilt keep their losses.

## 2. The parts

| Kind | What it is | Examples |
|---|---|---|
| **Working part** | Does a job with a limited capacity | Brain, heart, nephron, nurse bee, front-line staff |
| **Intake** | A working part whose job brings resource in. Every repayment depends on it | Gut, leaves, roots, foragers, a referral or recruitment function |
| **Control part** | A working part whose job is routing. It holds the threshold switch. Priced as a cliff only when it is a necessary, non-bypassable routing bottleneck (v0.12); distributed, redundant or bypassable control is priced like any other part | Vasomotor centre, hypothalamus, an institution's management (non-bypassable); a honeybee colony's task allocation (distributed) |
| **Reserve** | A stock that is drawn on and refilled. It runs full, drawing or empty, and is not itself damaged | Fat, iron stores, venous blood volume, honey stores, budget reserves |

Each working part has these properties:
- a **capacity**;
- how **vital** it is: the share of the system's persistence that depends on it;
- a **renewal class**, which sets its **rebuild time**: fast (a conveyor such as the gut lining), slow (liver), or none (fixed capital: neurons, heart muscle);
- a **ceiling**, lowered by scars or raised by growth after acute load;
- its **spare capacity** (redundancy), which now enters through its value (Section 2a);
- its **structural capacity** and its **deployed throughput**, which can differ (v0.12). A part may deliberately run below its structural capacity: **suppression** (a hibernating bear's kidney filters less while nitrogen is recycled elsewhere) or **remodelling** (a migrating bird's gut shrinks for a non-stop flight and is rebuilt at stopover). Reduced throughput with structure intact is suppression, not compromise; reduced structure rebuilt before the next task is remodelling, not a scar. Compromise means structural capacity lost and not restored.

Its priority is not one of its properties. It is computed from them and from the part's current state (Section 2a).

**State, for working parts only:**
- **Optimal:** within capacity, reserve full.
- **Stressed but coping:** covering the excess from reserve, spare capacity or debt still within its recovery window. Protective slowing begins here, giving up some capacity to protect the part.
- **Compromised:** debt held beyond the recovery window, so capacity is eroding.

Losses compound, because overload is felt against what the part can do now, not what it could do before.

## 2a. Priority (v0.5, revised in v0.6 and v0.7)

**The objective.** Every system's first objective is its own persistence; its output comes second. A system cannot do its function if it no longer exists (James, 5 October 2026). This holds for every system the model is applied to. There is no separate slot for an institution's stated purpose.

**Whose persistence.** The mapping names the level whose persistence $W$ measures. Parts can be spent for the level above when $W$ sits there: a worker bee dies for the colony, and a Pacific salmon, an octopus or an agave spends its whole body on reproduction. These cases do not break the model, but they test it: setting $W$ one level too low predicts the wrong order.

**Marginal value.** A part's value at time *t* is how much the system's persistence would lose if the part lost a unit of capacity:

$$v_i(t)=\frac{\partial W}{\partial c_i}\bigg|_t$$

This is a shadow price, judged against the **next task** persistence depends on (v0.12): a migrating bird's gut is valuable at stopover and payload in flight. It is near zero for a part with spare capacity, or for one whose work is not needed now (the gut when there is no food). It is high for the part that limits the system. In the engine, $v_i=\text{vital}_i\times b(L_i)$, where $b$ rises from 0.05 to 1 as the demand the part carries (its own plus any passed to it) approaches its current capacity.

**A non-bypassable control part is priced as a cliff (v0.7, narrowed in v0.12).** Where control is a necessary, non-bypassable routing bottleneck (every routed unit passes through it), its value is not its own workload: losing it breaks routing for the whole system, so its value is its full vital weight ($b=1$). Without this, a long episode priced control below working parts and spent it, and routing failed (TQ8). Natural systems with central control protect it to the end (the brain in starvation and in blood loss). **Distributed, redundant or bypassable control** (a colony's task allocation; local reflexes; systems that can route around a damaged node) is priced by its marginal value like any other part. Which kind a system has is a mapping decision, made before predicting.

**One value, two decisions:**

| Decision | Formula | Meaning |
|---|---|---|
| **Who pays first** under load | Ascending $p_i=v_i\,s_i\,\min(\tau+h_i,\;T)$ | What the system loses if the part is spent: its value now ($v_i$), times the share of its capacity still at stake ($s_i$), times how long the system would go without it: the rest of the episode ($\tau$) plus the part's rebuild time ($h_i$; very large for fixed capital), never more than the remaining horizon ($T$) (v0.7). $T$ can be the deadline of the next task persistence depends on (the next flight, the next winter) rather than the remaining life (v0.12) |
| **Who is rebuilt first** in recovery | Descending $q_i=v_i/k_i$ | Value restored per unit of resource ($k_i$: the cost of restoring a unit of capacity) |

**The terms of the spending cost.**
- **Time without the part (v0.6, corrected in v0.7).** Losing a part costs its value for as long as the system goes without it: the rest of the episode, $\tau$, plus its rebuild time, $h_i$. A system cannot go without it for longer than it has left, $T$. In v0.6 the cost was $v_i(1+\min(h_i,T))$: the "1" had no units, so the order of fast-renewing parts depended on whether time was counted in days or years. $\tau$ is the time that "1" stood for. The system must estimate it; the engine uses the length of the current episode so far.
- **Consequences of the time term.** With a long horizon, fixed capital is the dearest thing to spend. As the horizon shortens, or as an episode lengthens, spending a part that cannot be rebuilt costs little more than spending one that can. A system whose prospects are falling therefore spends parts it used to protect (terminal investment, with the objective set at the level of the lineage). Long episodes should likewise erode the protection of slow-rebuild parts, while short acute load protects them harder. **This last prediction was not reproduced in the engine** (TQ8 C6): there, a strained fast part loses capacity at stake faster than the slow part loses its premium, so the fast part stays the fuse. Open.
- **Capacity still at stake (v0.7).** Damage saturates: a part can lose only what it still has, so $s_i$ runs from 1 (healthy) to 0 (at its floor). A part that has lost all it can lose costs nothing more to load. It becomes the system's **fuse**, and load is concentrated on it rather than spread (leaves and fine roots in drought; old leaves shed first). Without this term, long episodes in the engine spread load across every part until all failed together.

**When spending by marginal value is the best policy (v0.7).** Spending in ascending order of marginal value is optimal only when each part's returns diminish and parts can be priced separately (a concave, separable objective: the water-filling solution). Three departures matter:
1. **Saturating damage** favours concentration on a sacrificial part over spreading: the fuse, handled by $s_i$.
2. **Cliff-shaped losses** (a part whose loss breaks the whole system, such as control) are never priced at the margin: control's value is its full vital weight.
3. **Increasing returns to an output** make the best choice all or nothing. A short horizon alone erodes protection gradually. **Spending the whole body (semelparity: Pacific salmon, octopus, agave) needs a short horizon and increasing returns to reproductive effort.** In agave, pollinators favour taller flowering stalks, so returns to effort rise (Schaffer and Schaffer; not read, from the second review). This corrects the v0.6 text, which called semelparity the limit of the horizon term alone. Not yet in the engine, which has no explicit objective.

**The reserve's value is the expected shortfall:** how likely the system is to face demand above its capacity, learned from experience (in the engine, how often total demand has recently exceeded total current capacity). Chronic or unpredictable scarcity therefore raises the reserve's value and its place in the recovery order.

**The reserve also remembers the worst it has met (v0.9).** Like a part (Section 3, item 8), the reserve is peak-referenced: an episode whose total shortfall exceeded the reserve's base size enlarges the reserve towards that depth, and the memory fades on the system's own clock. A shortfall deeper than any before therefore leaves a larger reserve for longer. **Frequency sets the order; depth sets the size.** So after a single severe acute episode, the reserve is still refilled after the working parts (G10), but to a larger size than before. Repeated episodes raise both: the system holds a larger reserve, and refills it earlier (the pattern reported after repeated weight loss and regain; to check).

**Control sees value through state signals.** In a coupled system the signals carry the demand each part actually carries, including what was passed to it. In an opaque one, control sees only nominal demand against nominal capacity, so a strained lower part looks as if it has spare capacity. **Opacity corrupts the priority calculation itself, not only the routing.** Even in natural systems, a signal that stays high loses gain over time (adaptation, as in baroreceptor resetting), so long-lasting strain is undervalued.

**What this explains that a fixed ranking only asserted:**
1. a redundant organ that cannot be rebuilt (the kidney) is cut after cheap tissue (gut, skin);
2. the gut is spent first in a fast and rebuilt first at refeeding: its value changes, not a rank;
3. the recovery order after acute and after chronic load (G10) follows from the reserve's expected-shortfall value;
4. "next demand", dependency (a dependent infant's muscle has low value) and insurance are all expressions of value;
5. with a shrinking horizon, parts that cannot be rebuilt lose their protection (the terminal-investment direction; shown in the engine, TQ8 C5, not yet checked in natural systems);
6. under saturating damage, a lost part becomes a fuse and takes the load (shown in the engine, TQ8 S4; consistent with plant hydraulic fuses).

## 3. How the parts interact

1. **Routing.** A part's shortfall goes first to the reserve, then to spare capacity in lower-priority parts, then is displaced onto them (lowest first). Priority here is the spending order of Section 2a. Whatever cannot be placed becomes the part's own debt, or leaves across the boundary.
2. **Labelled and unlabelled load.** Load that arrives with its origin can be refused by a part already under strain, which keeps the strain visible higher up. Load passed on through opacity has no origin, so it cannot be refused and sinks to the lowest tier.
3. **Shared supply.** A protected part depends on upstream supply, so it is protected only partly when that supply falls. (Brain flow falls with cardiac output.)
4. **Threshold switch.** At a set depletion of the buffer, not at exhaustion, control changes mode. It sheds a commitment, changes metabolism or behaviour, and often makes the record move.
   - **Economising, the graded form of the switch (v0.10).** As the reserve is drawn past a threshold, the system cuts the running demand of its working parts below what their current size needs (in a body: adaptive thermogenesis; less heat, less activity, reproduction and immune work cut). It follows an S-curve in the **gap between the shortfall still expected and the reserve held** (v0.13, anticipatory; James adopted it after the bear application): zero below a threshold, rising, then levelling at a floor set by what must be protected (the top and control are never cut). What the system expects: for a predictable episode (a season, a known fast), the remaining need is known, so economising starts at onset, before the reserve is drawn (a bear entering its den); for a kind of episode met before, it expects the usual length; beyond its experience, as much shortfall again as so far. With nothing more expected, the gap is minus the reserve, and the rule is the earlier depletion rule. Time matters only through what it does to the expected shortfall and the reserve. It eases as the reserve is refilled, not when supply returns, so it persists into refeeding: the reserve is then refilled faster than intake alone allows (catch-up fat), which is the chronic side of G10. A short restriction that never draws the reserve past the threshold triggers none of it, and breaks long enough to refill the reserve prevent it (intermittent restriction).
   - **The ledger (v0.11; James: split shed and debt):** economised demand is not removed. Each part's economised demand splits into **shed commitments**, which cross the boundary for good (heat not made, activity and reproduction forgone), and **deferred maintenance**, which becomes that part's debt and is repaid from slack later (repair, immune work). The share deferred is a property of the part, fixed from sources when mapping. The more of the economising that is deferred, the deeper the reserve is drawn and the slower recovery is: borrowing is not saving.
   - **Value and expected shortfall are measured against normal demand.** The system's own economising does not change what a part is for, and does not count as the environment easing.
5. **Control failure.** If debt reaches the control part, routing stops following priority: protected parts are hit while buffers remain. (Division of labour breaks down in collapsing colonies.)
6. **Compounding on survivors.** Parts carrying displaced or covered load are damaged by it. Their failure adds load to the rest: hyperfiltration in the kidney, precocious foraging in bees, the vacancy cascade in teams.
7. **Recovery.**
   - Slack repays debt and refills reserves, in descending value (Section 2a). **The order therefore depends on the type of past load (v0.3; derived in v0.5):**
     - after **acute** deprivation: intake first, then the working parts the next job needs, then reserves;
     - after **chronic** scarcity: the system re-tunes to expect more scarcity, and the reserve is enlarged first, often overshooting. Lean and working tissue follow more slowly.
     - after a **single severe** episode: reserves still come last, but are refilled to a larger size, which lasts (v0.9).
   - **The intake comes first whenever it was run down.** It is spent early when there is nothing to take in, and rebuilt first when supply returns.
   - **Speed and order are different things.** How fast a part recovers depends on its renewal rate (a conveyor such as the gut lining is fastest). The order in which resources go to parts is priority. The gut has both: fast renewal, plus resources actively diverted to it at refeeding (repair starts before food arrives in stage 3 rats; migrating blackcaps move protein from muscle to gut).
   - Recovery requires slack: demand below current capacity. It does not need demand to stop, so partial recovery under reduced demand is expected.
   - Debt nobody knows about is not repaid.
   - After compromise, renewable parts return with a scar (a lower ceiling, a shorter tolerance window, more resistance). Fixed capital keeps its loss: the point of no return.
8. **What the system becomes after an episode (v0.2).** There are four outcomes, which can occur together in different parts:
   - **Growth:** capacity rises above its old level. Conditions: the load was acute (repaid within the recovery window), state signals reached control (coupling), slack followed, and the part is renewable. Examples: muscle after hard work; an institution that sees staffing strain and adds capacity.
   - **Re-tuning:** the system changes demand, allocation, thresholds or reserve size in line with the threat it met. Capacity need not change. **Protection is set by the peak load met, not by cumulative load (v0.8):** after a recovered episode, a part carries loads up to that peak without strain; above it, strain builds at a reduced rate (graded protection); the protection above normal capacity fades with time; a scar removes it. This holds even while the part is still recovering, so repeated loading at or below the earlier peak during recovery adds no damage (muscle: natural test 11). This is short-term adaptation from experience, like a vaccine. Examples: spruce cutting leaf area after drought, so less water is needed next time; small birds carrying more fat when food is unpredictable; brief ischaemia protecting the heart against a later, larger one (checked in natural_test_retuning.md: Murry, Jennings and Reimer 1986).
   - **Scar:** a lower ceiling after compromise. A scar can also cut **demand** (spruce leaf area). Whether a past injury makes a system more or less vulnerable depends on whether it cut demand more than capacity.
   - **Loss:** fixed capital keeps what it lost.

   **The acute-chronic flip:** the same kind of load can produce growth when the system is in the acute state (signalled, buffered, recovered from with slack), and damage when it is in the chronic state (not enough slack to restore what the next task needs). **The state decides, not the duration (v0.12; James).** A short episode that leaves a scar has made the part chronic; a long, prepared and buffered episode need not (a hibernating bear fasts for months with muscle and bone preserved; a migrating bird repeats planned attrition every year). In the engine's computed mode there is no duration flag: chronic effects arise from the expected shortfall (frequency), depletion and unrepaid debt. The fixed (v0.4) engine's 20-step chronic flag is a legacy duration proxy.

   **The cost of re-tuning:** if conditions change, a system tuned to a past threat can be mistuned for the new one. (To test.)
9. **Starting state.** A system need not start optimal. Its stage at the start sets how much room it has. The stage is read from state signals, because the record cannot show it.

## 4. Read-outs

- **The record:** the output the system routinely watches, which is the top's served demand. It is flat through stress and moves at compromise, or at the switch.
- **The record's dynamics (v0.7).** The record's level is silent until the break, but its dynamics need not be. A small knock leaves a deficit that the reserve must restore at its release rate $\rho(R)$, so recovery takes about knock $\div\,\rho(R)$. **Where release tapers as the reserve shrinks** (the knee: $\rho$ falls in proportion to $R$), recovery time rises as $1/R$ and grows without limit as the reserve empties: the record recovers more slowly from each knock, and its autocorrelation and variance rise, while its mean stays flat. This is critical slowing down. **Where release stays at full rate until a switch**, recovery time is constant until the switch, and the break comes with no warning in the record. So when state signals are filtered, watch how long the record takes to recover, not where it sits. (Derived in the maths; the engine's record has no restoring dynamics, so it cannot show this. Built from the second review: Scheffer et al. 2009, not read.)
- **State signals:** each part's strain, debt, capacity and reserve level. They move from the start of stress. In opaque systems they are filtered, mistranslated or lost.
- **Where strain begins: the Felicity read-out (v0.8).** Raise the load and note where strain signals first appear ($D_{\text{on}}$). Compare it with the part's previous peak load ($D^\ast$) and its normal capacity ($\kappa c$):
  - $D_{\text{on}}\ge D^\ast$ (Felicity ratio $F=D_{\text{on}}/D^\ast\ge1$): protected, or grown;
  - $\kappa c\le D_{\text{on}}<D^\ast$: protected but the protection is fading;
  - $D_{\text{on}}<\kappa c$: **scarred** (compromised).

  It separates "recovering" from "scarred", which the record cannot, and needs no record at all. It follows from the re-tuning and scar rules (G7, G8); it is not a separate mechanism. (From materials science, where a reloaded structure is silent until it passes its previous peak load (Kaiser effect) unless it is damaged (Felicity effect); built from the second review; checked in muscle, natural test 11.)
- **The ledger:** demand = work done + reserves drawn + debt + load leaving the boundary. Nothing leaves the ledger except through work done or the boundary.
- **Reading a compensating part's output** (insulin, brain-sparing blood flow): it rises while the part copes and falls when it is compromised. A fall is therefore ambiguous: it can mean the load has eased, or that the compensator is failing. Check the load at its source (insulin resistance; placental resistance) before reading a fall as improvement. This follows from the rules; it is not a separate claim.

## 5. Mapping a system: how to identify the parts and assign labels

Do this before opening any outcome data.

1. **Boundary and currency.** Name the system and its boundary, and choose a currency that obeys a balance (energy, blood volume, filtration, labour hours, cases).
   - **Name whose persistence the objective measures** (v0.6): the organism, the colony, the lineage. Say which parts may be spent for that level.
2. **Demand and load.** What work is asked of each part, and from where? Where can it exceed capacity, and so become load?
3. **The record.** What figure does the system, or its observer, routinely watch and defend? (Blood pressure, creatinine, stores and brood, a performance indicator.) **It must be a held output (v0.4):** delivered below capacity, and kept up by buffers or a defending loop. A capacity test (maximal force, a time trial, a stress test) or a direct measure on the working units (nerve-fibre thickness, synapse counts, the control hormone) is a state signal, not the record.
4. **The top.** Which part's output is that figure? Is it fixed capital? This is the only part whose place is named in advance; every other part's priority is computed.
5. **The parts.** List the parts that do work. For each, decide:
   - its **role**: working, intake or control; for control, whether it is **non-bypassable** (every routed load passes through it) or distributed, redundant or bypassable;
   - how **vital** it is to the system's persistence;
   - its **renewal class** and rebuild time: fast, slow or none;
   - how much **spare capacity** it normally has;
   - for an intake, what it takes in, and when that is unavailable.

   **Fix these from independent sources before predicting any order (v0.6).** Vital weight, rebuild time and restoration cost come from sources that do not report the order being predicted: lesion or knockout studies, regeneration and turnover rates, the cost of rebuilding tissue. Log each source. A value chosen with the expected order in mind is declared as such, and that part of the result counts as built in.
6. **The reserves.** Which stocks are drawn first? Does release slow as they shrink?
   - **The remaining horizon.** How long are the system's prospects (life stage, season, age)? Is it shrinking?
   - **The system's clock (v0.9; James, 5 October 2026).** Fix the unit in which durations are judged before checking anything: the reserve's refill time, a part's rebuild time, decision cycles, generations, depending on the level the objective measures. "Brief", "lasting" and "permanent" are claims on that clock. A re-tuning that lasts a lifetime is lasting for an individual and brief for a population that replaces its members. Without a unit fixed in advance, any duration can be rescaled to fit.
7. **Labelled or not.** Does load passed down arrive with its origin? Can the receiver refuse it? Do state signals reach the top?
8. **Control and the switch.** What routes load? Is there a known mode change at a set depletion?
9. **State signals.** For each part, what measure shows its strain, debt or reserve? Judge each against the system's own reference state for its current phase (v0.12): a hibernating bear's creatinine read against an active-season range would misread coping as failure.
10. **Starting stage.** From baseline state markers, classify the system as optimal, stressed or compromised. Population "normal" ranges may describe the stressed stage. Where the load can be raised and strain signals watched, the Felicity read-out (Section 4) separates a protected, a fading and a scarred part.
11. **Predictions.** Write the generic predictions in Section 6 for this system before looking at outcomes.

## 6. Generic predictions (what the model always says)

**Two layers (v0.7).** Some predictions hold for any negative-feedback loop with a finite stock, with no goal at all (a star leaves the main sequence with most of its hydrogen unburned; Earth's carbonate-silicate thermostat). Confirming them is cheap and says nothing about priority. Others need selection or design. Each prediction and each piece of evidence is tagged: **layer 1** (any finite-stock feedback loop) or **layer 2** (needs selection or design).

| No. | Prediction | Layer | Status (v0.12) |
|---|---|---|---|
| G1 | The record stays near normal while state signals and reserves move | 1 | Natural observation: consistent in all surface tests (non-diagnostic for priority) |
| G2 | Lower-priority parts are drawn down first, in reverse priority | 2 | Natural observation: consistent (blood loss, fasting, bees); known in outline beforehand |
| G3 | The break comes at a set depletion of the buffer, not at exhaustion. If the buffer is a stock, the break comes at the same cumulative load whatever the rate | 1 | Natural observation: partly consistent (sheep rate-independence; fasting threshold at a fat share); stress-test candidate (H1, H2) |
| G4 | A larger buffer gives a longer silence and a sharper break; a stressed or compromised start breaks sooner | 1 | Natural observation: consistent (heat stress, initial fat, low nephron number); stress-test candidate |
| G5 | Survivors that carry extra load are damaged by it, so loss compounds | 1 | Natural observation: consistent (kidney hyperfiltration, precocious foraging) |
| G6 | Recovery runs intake first and reserves last, and needs slack. Unknown debt is not repaid, so the record recovers before the state does | 2 (order); 1 (record before state) | Natural observation: consistent for record before state (kidney); order, see G10 |
| G7 | Parts that cannot be rebuilt keep their losses; renewable parts return with a scar | 1 | Natural observation: consistent (nephrons, spruce, scarred muscle) |
| G8 | Load that is signalled and recovered from with slack (the acute state) leaves growth or re-tuning. Load without enough slack to restore what the next task needs (the chronic state) leaves scars. The same load can do either: the state decides, not the duration | 2 | Natural observation: consistent (muscle, fetal hypoxia); simulation result (TQ7, TQ8) |
| G9 | A system re-tuned to a past threat does better against that threat again, and may do worse if conditions change (the cost of being mistuned). **Tests must follow the same individuals (v0.7):** at population level, the death of the susceptible mimics re-tuning (coral after repeated bleaching) | 2 | Natural observation: partly consistent (starlings, primed plants); cost of mistuning not found |
| G10 | After acute deprivation (recovered with slack), working tissue and intake recover before reserves. After a chronic state of scarcity (repeated or sustained shortfall without repayment slack), reserves recover first and overshoot. (Derived from the reserve's expected-shortfall value in v0.5) | 2 | Natural observation: consistent (recovery-order test); simulation result, with a fitted shortfall definition (TQ8) |
| G12 | **Record dynamics (v0.7).** Where reserve release tapers as the reserve empties, the record recovers more slowly from small knocks as the break approaches, with rising autocorrelation and variance at a steady mean. Where release is full until a switch, the break gives no warning in the record | 1 (conditional on the release profile) | Derived prediction (maths); untested; blood-loss contamination declared (TQ-DS2a) |
| G13 | **Fuses (v0.7).** Once a part has lost what it can lose, further load is concentrated on it rather than spread to healthy parts | 2 | Simulation result (TQ8); compatible but non-diagnostic (plant fuses); prepared systems (bears, migrants) show remodelling rather than fuses |
| G14 | **Peak-referenced protection (v0.8).** After a recovered episode, strain signals appear only above the previous peak load; protection depends on that peak, not on the volume of the episode; it fades with time; after a scar, strain appears below normal capacity | 2 | Natural observation: partly consistent (muscle, natural test 11); simulation result (TQ8 C7) |
| G15 | **Reserve memory (v0.9).** After a shortfall deeper than the reserve's base size, the reserve is enlarged towards that depth and stays enlarged for longer than after shallower ones, measured on the system's own clock. After a single acute episode it is still refilled after the working parts. Repeated episodes enlarge it and raise its place in the refill order. At equal total load, one deep episode leaves a larger reserve than several shallow ones unless the shallow ones are frequent enough to raise the expected shortfall | 2 | Simulation result (TQ8 C8; cap and memory fitted); natural observation: partly consistent (weight cycling) |
| G16 | **Economising (v0.10; anticipatory in v0.13).** Running demand is cut when the shortfall still expected outruns the reserve held: at onset for a predictable long episode, later (with depletion) for an open-ended one, not at all for short episodes of a learned length. It levels off at a floor, never touches protected parts, and persists until the reserve is refilled | 2 | Simulation result (TQ8 C9, C10); compatible: intermittent restriction (found before writing), bear hibernation (prompted the revision) |
| G17 | **Economising and growth compete (v0.13).** A challenge that threatens the reserve triggers economising, which spares working parts and the record but removes the strain that growth needs. Growth after acute load needs strain without economising: a challenge that strains the parts but does not threaten the reserve | 2 | Simulation result (TQ8 C11); not yet checked in natural systems (training in energy deficit is a candidate) |

(G11 was withdrawn in v0.4 and is not reused. Internal numbers keep the gap; any public version is renumbered, with a crosswalk (v0.12).)

**The test only layer 2 can pass:** a reserve that is easy to reach but valuable. Drawing in order of access would spend it; drawing by value would hold it. A clean natural case is still to find. Muscle glycogen, suggested in the second review, is weak: muscle lacks the enzyme to release it as blood glucose, so its retention is fixed design, not a decision made in the episode.

## 7. Evidence so far, and its weight

- **Exploratory applications (not tests; v0.12):** a reviewer (Perplexity) applied the model to two systems it chose arbitrarily, hibernating brown bears and long-distance migratory birds, looking at evidence after choosing (raw/2026-10-05_perplexity_random-applications_bears-birds.md). Fit: strong but non-diagnostic. They prompted the state reading of chronic load, the structural against deployed capacity distinction, task-relative value, and a challenge to G16 (bears economise before depletion).
- **Simulations TQ1 to TQ8:** illustrative parameters. Natural test 11 (the Felicity read-out in muscle) added in v0.8. TQ8 (theory/sim/outputs/2026-10-05_TQ8/README.md) shows computed priority reproducing the earlier results without hand-set ranks.
- **Surface checks in natural systems:** blood loss, fasting, kidney, honeybees, plants under drought, fetal growth restriction, recovery order, muscle injury against disuse, the record rule, and re-tuning (theory/natural_test_*.md; theory/natural_tests_patterns.md). All were broadly consistent. Each mismatch led to a refinement, and the unexplained items are logged in those files.
- **By layer (v0.7; detail in theory/natural_tests_patterns.md).**
  - **Layer 1 only:** the kidney test (flat creatinine, break at about half the nephrons, compounding hyperfiltration, low nephron start) and the record-rule test.
  - **Layer 2 evidence:** the order of loss in blood loss (skin, gut and muscle before kidney; brain protected) and in fasting (fat, then gut and liver, then muscle); the fasting switch (phase III, egg desertion); honeybee allocation (maintenance and guarding cut, brood care held; brood eaten when protein is short); hydraulic fuses and the spruce demand cut; fetal brain sparing and the acute-chronic flip; recovery order after acute against chronic scarcity (lambs, piglets, sparrows, people after undernutrition); growth against scar in muscle; and re-tuning (starlings, preconditioning, primed plants).
  - **Layer 1 parts of the other tests:** the flat record and break at a set depletion in blood loss, fasting, honeybees and plants; rate-independence (sheep); starting state (heat stress, initial fat, drought legacies).
  - **Re-tuning evidence and individuals (v0.7 test rule):** starlings, preconditioning, primed plants, fetal sheep and muscle followed individuals. The human food-insecurity link is population-level and cross-sectional. Spruce: the experimental plots probably followed the same trees, but survivor filtering is not ruled out from the abstract (to check).
- **Limits:**
  - much of the layer 2 evidence was known in outline before the predictions were written;
  - the sources were read through summaries;
  - several predictions were known in advance;
  - refinements A and B and the reserve knee were built from the literature;
  - the most informative predictions are untested: whether higher energy demand moves the fasting threshold, and whether a larger buffer gives flatter pressure.

## 7a. Status of claims and engine assumptions (v0.12)

**Status labels** used for every major claim: **modelling choice** (an assumption of the model or engine); **derived prediction** (follows from the rules); **simulation result** (holds in the engine under its rules); **natural-system observation** (surface checks against published findings, with the weight stated); **direct test** (a pre-registered test against data not used to build the model; none yet); **compatible but non-diagnostic** (consistent, but would be expected without the model's distinctive rules); **unknown or contradicted**. Any value chosen after seeing an outcome is labelled **fitted**, not predictive. The status of each generic prediction is in the table in Section 6.

**Fitted so far:** the definition of a shortfall (chosen while reproducing G10); the skin's vital weight in the blood-loss check; the reserve's size cap and memory length; the economising thresholds, ceiling and response time; the default expectation beyond experience ("as much again as so far") and how fast episode length is learned; the deferred share of economised demand (0.5); all rates and thresholds in the engine.

**Engine assumptions (results hold under these rules):**
1. the objective is persistence at a named level, then output;
2. a part's shortfall goes to the reserve, then to spare capacity of lower-priority parts, then displaced downhill; then debt or the boundary;
3. non-bypassable control is priced as a cliff;
4. damage saturates (a lost part becomes a fuse);
5. a part's value rises as its carried demand approaches its current capacity;
6. the reserve's value is the expected shortfall (frequency), and its size also remembers the deepest shortfall;
7. recovery follows value (value per restoration cost, with restoration cost uniform in the engine);
8. protection after a recovered episode is set by the peak load met, and fades;
9. economising is driven by the gap between the shortfall still expected and the reserve held (v0.13), and splits into shed and debt;
10. overload is felt against current capacity (compounding);
11. the record has no restoring dynamics (so G12 is derived, not simulated).

## 8. Way forward (James, 5 October 2026)

1. **Test, revise, test again,** in more natural systems, at surface level first, updating this file with each version.
2. **Keep the best datasets unopened** for a final stress test once the model is consistent. That list is to be agreed before any of them is used.
3. **Run full stress tests on those held-out datasets,** with predictions committed in advance.
4. **Only then, novelty.** Hand pass 1 (theory/novelty_tier_queue_pass1.md) and the provenance log (theory/tier_queue_provenance.md) are kept for that stage and are not acted on now.

## 9. Changes in v0.13 (James approved, 5 October 2026)

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

## 10. Changes in v0.12 (James approved, 5 October 2026)

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

## 11. Changes in v0.11 (James approved, 5 October 2026)

- **Economised demand split into shed and debt** (Section 3, item 4). Each part carries the share of its economised demand that is deferred maintenance (illustrative 0.5 in the engine; to be fixed from sources when mapping).
- **Engine (computed mode; TQ5 and TQ7 unchanged).** Continuous restriction with none, half or all of the economising deferred: lowest reserve 42, 2 and 0 (of 200); reserve back to 95% after 4, 7 and 24 steps; debt cleared after 0, 1 and 20 steps.
- **A fault found and fixed in the build:** economising decayed towards zero without reaching it, adding slivers of debt every step, so episodes never ended and no protection was granted (S1's second pulse lost its protection). Economising now ends below a small tolerance.
- **The opaque trap does not return in S2** with the split: each part repaid its deferred debt from its own slack in the gap between pulses. A first run suggested it had partly returned (second-pulse strain 7.3); that came from the fault above and is withdrawn. The trap would return where deferred debt cannot be repaid before the next load (short gaps, or parts with no slack); open.

## 12. Changes in v0.10 (James approved, 5 October 2026)

- **Not a new principle (James).** The model already had the acute-chronic flip and a threshold switch at a set depletion. The weight-cycling test (natural test 12) found, before this was written, that intermittent restriction gives more weight loss per unit of deficit than continuous restriction in mice; that is supporting evidence. v0.10 makes the economising response explicit as the graded form of the switch (Section 3, item 4). Predictions E1 to E5 were committed before the build (theory/v0.10_economising_predictions.md).
- **Shape (James's question):** an S-curve in depletion (threshold, rise, floor), not a line: a line would have no threshold (contradicting G3) and no floor (contradicting protection of control and fixed capital).
- **Faults found and fixed during the build,** both by principles the model already states: economising first lowered the working parts' apparent value (they looked spare) and lowered the expected shortfall (economising hid the scarcity), which reversed both halves of G10. Value and expected shortfall are now measured against normal demand.
- **Engine (computed mode; TQ5 and TQ7 unchanged).** TQ8 C9, equal total extra demand: continuous restriction economised up to 21% and shed 508 units of working demand; with breaks long enough to refill the reserve, none; with 2-step breaks, up to 14% and 250 units. Economising persisted 12 to 15 steps after the load ended, easing as the reserve refilled. At the same depletion (70%) a slower route showed slightly more economising (0.049 against 0.037) because the response lags by a few steps.
- **Against the predictions:** E3 said short breaks give no advantage; the engine gives a partial one (half the economising).
- **A result that changed: the opaque trap.** In S2 the opaque system no longer traps its base after the first pulse (second-pulse strain 0, against 18 in v0.9): economising cuts the working parts' demand below their capacity, so they recover. Its price is paid as shed commitments, which the record does not see. The v0.4 finding "opaque systems do not get the benefit of an acute challenge" holds only where the system cannot economise; this needs re-examining.
- G10 holds (S3, S3b). C3: the kidney is now strained later (step 26).

## 13. Changes in v0.9 (James approved, 5 October 2026)

From the third review (relayed by James; raw/2026-10-05_claude-chat_review3_astro-econ.md), which tested v0.7 against economics: one severe crisis (Asia 1997) left reserves enlarged for about 15 years, against v0.5's text that a single acute episode raises the reserve "only briefly". James contested the comparison: brief relative to what?
- **The system's clock** (Section 5, step 6): every duration claim is made in units fixed in advance and native to the level being modelled. "Only briefly" now has to name its unit.
- **The reserve is peak-referenced** (Section 2a), as parts became in v0.8: depth sets the size and its persistence, frequency sets the place in the refill order. New prediction G15.
- **Already covered for parts by v0.8:** because protection fades from the peak excess, a larger peak stays protective for longer (duration grows with the log of the peak's excess), matching the muscle durations (2 weeks after low intensity, up to about 24 weeks after maximal).
- **Held (James):** R11 (sharpness of the break depends on how synchronised the buffers' depletion is) and R14 (tests of the horizon need the budget held constant).
- **Engine (computed mode; TQ5 and TQ7 unchanged).** TQ8 C8, same total extra load in three shapes: one severe pulse enlarged the reserve to twice its base, still twice 150 steps later (the size cap binds); four short pulses enlarged it to 1.72 times, 1.30 times 150 steps later; a long mild load within spare capacity left it unchanged. After the severe pulse the reserve still refilled after the working parts. G10 holds in S3 and S3b. The balance between depth and frequency depends on the size cap (twice base) and memory length, both arbitrary.

## 14. Changes in v0.8 (5 October 2026; Claude's call, delegated by James)

James: "I provide the observation, the pattern and some predictions; you translate that into text and formula. Your call."
- **The Felicity read-out adopted** (Section 4), from the muscle check (natural test 11): protection follows the previous peak load (10 maximal contractions protected as well as 45); it is graded (lower-intensity first bouts protected partly against a maximal one); it fades (2 weeks but not 3 for low intensity; up to about 24 weeks for maximal); and a scar lowers the load at which strain appears (previous hamstring strain: two to six times the re-injury risk, higher strain next to the scar). The prediction that strain appears below the previous peak during ordinary recovery failed; the stage had been misassigned, and the scar case checked.
- **Re-tuning is now set by the episode's peak load, not its cumulative strain** (Section 3, item 8; computed mode in the engine). In v0.7 protection grew with peak exposure, which mixes in volume.
- **New prediction G14.**
- **Engine (computed mode only; TQ5 and TQ7 unchanged):** after a recovered episode a part carries demand up to its normal capacity plus the excess it met at the peak without strain; that excess fades with the re-tuning memory; a scar resets it. TQ8 C7 reproduces the muscle pattern: strain onset in a ramped second bout sits at the previous peak after a low-peak first bout, just below it after a high-peak bout 60 steps earlier (fading), at normal capacity with no first bout, and below normal capacity after a scar (ratio 0.69). High-peak first bouts of short and long duration protect about equally. In S1 the base's strain in the second identical pulse falls from 3.42 to 0.91.

## 15. Changes in v0.7 (James approved, 5 October 2026)

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

## 16. Changes in v0.6 (James approved all four, 5 October 2026)

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

## 17. Changes in v0.5

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

## 18. Changes in v0.4

- **Rule R for the record** (natural_test_record_rule.md): only a held output behaves as a flat record. This resolved the muscle mismatch, where performance had been measured with capacity tests. It sorted five paired cases without a break: submaximal force against EMG and maximal force; hearing thresholds against synapse counts; visual field against nerve-fibre thickness; glucose against insulin; T4 against TSH. All five were known in outline.
- **G11 withdrawn (James, 5 October 2026).** It adds no mechanism. A compensating part carries load passed to it, so its output rises while it copes and falls when it is compromised. That already follows from the existing rules. It is kept only as a reading note in Section 4.

## 19. Changes in v0.3

- **Recovery order depends on the type of past load.** This was formed after the growth-restriction result, then checked on three cases it was not built from: adults after long-term undernutrition, growth-restricted lambs and piglets, and food-limited migrating sparrows. All three fitted (natural_test_recovery_order.md; surface level, one case contaminated).
- **Speed separated from order,** with the intake's double advantage.
- **A rule not yet found: the next demand.** When a system builds without prior deprivation, it builds for what is coming (ground squirrels multiply their fat before hibernation; warblers fuel for the next leg). The gut's history suggests a form for it (theorising): **a part's priority follows its value to the system's current bottleneck.** The gut is spent when there is nothing to absorb (low value) and rebuilt first when food returns (it becomes the bottleneck). Fat is built ahead of a known fast. This would unify state-dependent priority, role reassignment and the next demand. To test.
- **New generic prediction** G10.

## 20. Changes from v0.1 to v0.2

- **Scars can cut demand as well as capacity.** From the plant check: spruce leaf area was down 60% after drought and still 30% down four years later, and the trees coped better with the next drought. The explanation was named, then checked.
- **Four recovery outcomes** (growth, re-tuning, scar, loss), with their conditions. This includes the acute-chronic flip, from James (5 October 2026): resilience exists in too many places to leave out. Muscle growing after hard work is a healthy, coupled system adding capacity. The leaf cut is short-term adaptation from experience, like a vaccine.
- **New generic predictions** G8 and G9.

## Terms (James, 5 October 2026)

- **Demand:** the work asked of a part.
- **Load:** what spills over beyond a part's capacity, held as latent load (debt) or displaced to another part. Load is not work. "Acute load", "displaced load" and "load leaving the boundary" all refer to this excess.

- **Acute (a state; v0.12):** load exceeds current capacity, but reserves, slack and a response are in place, so what the next task needs can be restored.
- **Attrition (a state; v0.12):** the system deliberately draws reserves or tissue to sustain its current objective. It can be planned and reversible (a migrant in flight) and has no set length.
- **Chronic (a state, not a duration; James, 5 October 2026):** attrition or load without enough slack to restore the capacity the next task needs. Debt goes unrepaid and ceilings fall. A short episode that leaves a scar is chronic; a long, prepared, buffered episode need not be.
- **Suppression and remodelling (v0.12):** deliberate reduction of a part's throughput (suppression) or structure (remodelling), reversed before the next task needs it. Neither is compromise.

- **Incomplete recovery:** a part does not return to its previous capacity (a scar, or a loss in fixed capital). This is what earlier notes called the "point of no return" for a part.
- **Point of no return (system):** death, or the complete failure of an organ or of the system.

## 21. Open questions

- ~~How does priority combine vital, irreplaceable and redundant?~~ Answered in v0.5: vital and redundancy combine in the marginal value, and irreplaceability scales it in the spending order.
- Is the threshold switch always protective (an active choice) or sometimes simply failure?
- Does a high-reserve system decline faster after its break? (Cognitive reserve may say yes, from recall, to check.)
- Restriction against starvation: does the type of load change the recovery order?
- What sets the boundary between "labelled" and "unlabelled" in natural systems?
- When does acute load give growth rather than re-tuning, and how long must recovery be for either?
- Are institutions able to grow or re-tune after strain, given that their debt is often unknown?
- ~~Does priority follow value to the current bottleneck?~~ Adopted in v0.5. What would still distinguish it from fixed priority plus role reassignment in data: order among parts that are not bottlenecks should be set by replaceability alone.
- **The remaining horizon.** What sets it in natural systems (life stage, season, age), and can it be measured independently of the order it predicts? Terminal investment and semelparity are the first cases to check.
- **The shortfall definition.** Check it against a case not used to build it: reserve enlargement after one severe acute episode should be smaller than after a long mild one with the same total load.
- ~~The demand-cut sink.~~ Withdrawn in v0.7 (an artefact of mispricing parts at their floor).
- **Episode length.** Do long episodes erode the protection of slow-rebuild parts (heart muscle in prolonged starvation against short acute load)? Not reproduced in the engine, where the fuse dominates. A natural check would settle whether the theory or the engine is missing something.
- ~~Where economised demand lands.~~ Split into shed and debt in v0.11. Open: what share is deferred in each natural system (a mapping value to fix from sources).
- **Economising and the opaque trap.** An opaque system can escape the trap by economising, paying in shed commitments and deferred debt. The trap should return where deferred debt cannot be repaid before the next load. Does it, in nature?
- ~~Anticipatory economising.~~ Adopted in v0.13.
- **Economising against growth (G17).** Check against controlled studies of training during energy deficit (same individuals followed), predictions committed first.
- **How a system forms its expectation** of the shortfall ahead (season, learned episode length, the first-time default) needs a natural case: does a first-ever episode of a kind trigger more precautionary economising than a familiar one?
- **Depletion against time (E1):** the discriminating test needs the same depletion reached fast and slow, compared after the response lag.
- **Weight cycling (James, 5 October 2026).** Does repeated loss and regain make a body defend its fat harder (larger reserve, refilled earlier)? G15 says yes. A natural check, with predictions committed first.
- **Synchrony (R11, held)** and **horizon against budget (R14, held)**: from the third review; not adopted.
- **Expected shortfall against integral windup.** Windup says overshoot after a deficit scales with how long the last deficit lasted; the expected-shortfall rule says it scales with how frequent and unpredictable deficits are. Test: the same total deficit as one block or scattered at random. The starling result (unpredictable supply, same average, larger reserves) favours expected shortfall if those birds faced no longer deficits: to check. The engine's measure (frequency in a 30-step window) cannot yet tell unpredictability from frequency.
- ~~Felicity ratio.~~ Adopted in v0.8 as the Felicity read-out (Section 4). Repeated loading during ordinary recovery adds no damage because the load does not exceed the raised no-strain ceiling (James, 5 October 2026): the model already says this. What remains open is below the model's level: **how** a part raises its ceiling within days while its maximal force is still reduced. The same load damaged the muscle the first time, so the ceiling that governs strain is not maximal force (consistent with rule R: maximal force is a state signal). Candidate mechanisms (loss of the most susceptible fibres, a fuse inside the part; neural or connective-tissue adaptation) are not the model's to choose.
- **Two boundaries** (held). Load that leaves only the record's accounts, not the system, may return unlabelled and hit neighbours. Needs a natural case (theorising: fat-soluble toxins stored in fat and released when fat is drawn in a fast).
- **A clean layer 2 test:** an easily reached but valuable reserve, held while less valuable ones are drawn.
- **Vital weights** must now come from independent sources (Section 5, step 5). Which sources give them reliably: lesion and knockout studies, or what fails first when a part is removed?
- **Whose persistence.** Where the level is unclear (a mother and fetus, a colony and its workers), does setting the objective at each level give different, checkable orders?
