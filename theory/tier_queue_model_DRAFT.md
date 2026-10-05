# The tier-queue model (draft, 5 October 2026)

Status: theorising (phase 3, no gates). Drafted by Claude at James's request. It joins the queue and flow model of the prior thread (theory/prior_thread_digest.md) with the tier model of 4 to 5 October (theory/conserved_quantity_attempt.md, Section 7). Nothing here is checked against data. Wording of any principle derived from it goes to James.

## 1. The idea in one paragraph

A system is a tree of parts. Each part is a server: work arrives, and the part processes it with finite capacity. When work arrives faster than a part can serve it, the excess does not vanish (P1). It is drawn from the part's own reserve, handed to a part of lower priority, or deferred as debt. Load therefore runs down the tree from protected parts to expendable ones. The top's output stays steady while the buffers below absorb the excess, then changes abruptly when they run out: the hockey stick. Recovery runs the other way, starting with the intake, because nothing can be repaid until income returns. A part that cannot be rebuilt sets the point of no return.

## 2. Parts

Each part *i* has five properties:

| Property | Symbol | Meaning |
|---|---|---|
| Role | reserve, intake or working | What it does now. The state can reassign it (the warbler's fat is fuel mid-migration) |
| Priority | π_i | How strongly it is protected. Higher means spent later |
| Capacity | μ_i | Rate at which it can do work, now |
| Reserve | R_i, up to R_i^max | Stock it can draw on before it must export or defer |
| Renewal rate | g_i | How fast lost capacity is rebuilt: high (labile, a conveyor such as the gut lining), low (stable, the liver), zero (permanent, fixed capital such as neurons and heart muscle) |

Spare capacity (redundancy) is μ_i^max minus the capacity the part needs for its own work. The kidney has a lot of it.

**Priority rule (candidate, James):** π_i rises with how vital the part is and falls with its renewal rate and its spare capacity. Protect what is vital and cannot be rebuilt; spend what can be regrown or has surplus.

## 3. Flow at one part

Work reaching part *i* is its own demand d_i plus load imported from higher-priority parts, m_i. It serves

A_i = min(d_i + m_i, μ_i)

and has a shortfall e_i = d_i + m_i − A_i. The shortfall goes three ways:

- **draw on its own reserve**, at rate r_i, while R_i > 0;
- **export** to a part of lower priority, at rate x_i, if one has reserve or spare capacity;
- **defer** as debt, at rate δ_i, when it has nowhere to export: its own work goes undone.

So e_i = r_i + x_i + δ_i, with Ṙ_i = −r_i (plus repayment) and Ḋ_i = δ_i (minus repayment), where D_i is the part's debt of undone work.

**Where export goes: the path of least resistance (James, 5 October 2026).** The hierarchy is a tier list, not a pipe: load is not passed hand to hand down the reporting line. It can land on any lower-tier part, as in the body, where blood loss cuts skin, gut and kidney at once. Which part takes it is set like flow in a hydraulic network. Each candidate receiver k offers a resistance Ω_k, and the export splits in inverse proportion:

x_{i→k} = x_i · (1/Ω_k) / Σ_j (1/Ω_j)

over the receivers that still have reserve or spare capacity.

**What sets resistance (James, 5 October 2026, for systems with low or no feedback coupling).** Load passed on through opacity has no origin from the receiver's point of view. It cannot be refused, because there is no one to refuse it to. Resistance exists only where the load arrives with a direct link to the part that generated it. So the model has two forces, as in water:

- **Priority is height.** Load flows downhill, from protected parts towards expendable ones.
- **Resistance is a barrier,** and only labelled load meets it. A part that can see where load came from can push back, so labelled load can be held at a tier.

Unlabelled load meets no barrier anywhere, so it runs all the way to the lowest tier. This ties the destination of load to paper one's P2 (exported load arrives without its origin): the missing label is the reason it sinks to the bottom.

*Earlier reading, superseded:* First-degree links resist load. People are invested in, and care for, their own team and direct reports, so the parts nearest someone with power are buffered against harm. Resistance is therefore high where the receiver's state is felt first-degree by someone who can push back, and low where the receiver is distant, has no voice, or sits outside the boundary. Load flows to the parts whose strain is felt least. This is the prior thread's "value to the centre, load to the weakest-feedback boundary", given a mechanism. In the body, the equivalent of resistance is priority enforced by control: the vessels to the brain and heart barely respond to the signals that cut flow elsewhere.

**Why harm happens below.** Imported load arrives as demand on the receiver (m_k). It first uses the receiver's reserve, then displaces the receiver's own work, which becomes the receiver's debt D_k. This is James's point: load does harm by displacing the receiving part's own work, not by being "foreign".

## 4. Conservation

Summed over all parts and the boundary, in any currency that obeys a balance law:

total demand = work served + reserves drawn + debt accumulated + load exported across the system boundary.

This is the flow identity of the prior thread (generated = resolved + exported + backlog increase + abandoned or suppressed), with reserves and debt made explicit, and it is the C1 form of P1. Nothing leaves the ledger except through work done or the boundary. "Abandoned" work is debt sitting somewhere.

## 4a. Three states of a part (James, 5 October 2026)

Each part is in one of three states:

| State | Condition | Output | What the record shows |
|---|---|---|---|
| **Optimal** | Demand within capacity, reserve full, no debt | Normal | Normal |
| **Stressed but coping** | Demand above capacity, covered by drawing reserve, exporting or using spare capacity; any debt still inside the recovery window τ | Maintained | Normal |
| **Compromised** | Reserve gone and debt older than τ, so capacity is eroding | Falls | A change, at last |

For a permanent part (g = 0), compromise is the point of no return (Section 7).

**Which parts can be compromised (James, 5 October 2026).** Only working parts. Intake is a kind of working part: its work is bringing resource in (gut, leaves, roots, gills, a colony's foragers; in an institution, the functions that bring in revenue, referrals or staff). It is named separately only because of where it sits in the repayment path. Reserves are not compromised. They run full, drawing and empty, and refill (iron, fat, root carbohydrate). When a reserve is empty, the working parts that depended on it go into compromise. Edge case: a reserve that is also structural, such as bone as the calcium reserve, can be damaged, but only in its working role.

**Compromise leaves a mark (James, 5 October 2026).** A burnt-out staff member who returns has changed: slower, more cautious, protective, possibly critical of the institution. In the body, a renewable organ under chronic injury heals with scar tissue rather than full regeneration (fibrosis in the liver, kidney and heart; Claude's recall, to verify), and an earlier insult blunts the next response (p53). So recovery from compromise restores the part with changed parameters:

- **a lower ceiling** (μ_max falls);
- **a shorter tolerance window** (τ falls);
- **higher resistance:** the part now pushes back on load, which is James's "protective".

Theorising: if recovered parts resist, unlabelled load shifts to parts without scars, such as new hires, who take a disproportionate share.

**The record sees compromise, not stress.** A part's output, and so the record produced through it, stays normal through the whole stressed state. The only evidence of stress lies in the part's state signal and its falling reserve, which is where P4 places the warning. The stressed state is the buffer; its length is the silence before the break.

Priors: Selye's alarm, resistance and exhaustion (resistance corresponds to stressed but coping, exhaustion to compromised), and Miller's range of stability. The fasting stages also line up: stage 2 is coping on fat with protein spared, and stage 3 is the switch as the reserve reaches its threshold.

## 5. Why the top looks steady, then breaks (the hockey stick)

While any lower part has reserve or spare capacity, the top exports its shortfall and its output A_top stays near μ_top. Its record is flat however far demand rises. The excess is visible only as falling reserves and growing debt below.

Let the overload be E = demand − capacity at the top, and let the usable buffer below be the sum of reserves and spare capacity in the parts that can receive. The time before the top's own output must fall is roughly

T ≈ usable buffer ÷ E

(the rate at which buffers can be released also caps it). When the buffer runs out, the excess has nowhere to go but the top's own work or other high-priority parts. The effective service rate drops from capacity plus buffer release to bare capacity, utilisation jumps past 1, and the change is abrupt. In queue terms, the buffer was holding ρ below 1. Its exhaustion pushes ρ past 1, and waiting and debt rise steeply (W ∝ 1/(1 − ρ) as ρ approaches 1).

This links to paper one. Receiver withholding is a tier holding back unresolved work, so the record reaching the top is the served work A, and the record is flat for the same reason. It also fits the K1b bee result already logged: stores held flat at the cap while about 70% of hive bees were lost, and the record (weight, stores) lagged by months.

## 5a. The wide base and turnover (5 October 2026; simulation TQ2)

**Sharing across the base.** The widest tier is many parallel units. If load is shared across them (a common pool), they reach compromise together. If it lands on whoever is nearest (fixed teams), they reach it in turn. This is the fibre-bundle result (Peirce 1926; Daniels 1945). In TQ2, sharing set the timing and synchrony of base failure. The steepness of the record's break was set mainly by how fast a compromised part loses capacity. A sharp break needs fast collapse inside parts (decompensation), not only shared load.

**Turnover as an external buffer (James).** In an institution, compromised units leave, and the debt they carry leaves with them across the boundary. Fresh, unscarred units are brought in from outside, a "foreign" fix. The units are restored; the cause is not. If load is still being generated, fresh units are compromised in turn. In TQ2 the load that kept generating was the turnover itself (corrected after TQ3): each vacancy's work is covered by colleagues near capacity, which overloads them, a vacancy cascade. The result is permanent churn, a revolving door, while the record reads normal. Turnover then becomes a channel for exporting load: burnt-out people carry it out. It is visible only in a different signal type: people withdrawing, not the work.

**The scar rule (TQ3).** When scarred units take less of the shared load, nothing changed about the churn, because the base was over capacity as a whole. Shifting load among parts that are all over their limit has no effect. The one effect was that resistance at the base sent strain back up: the top's record dipped further. Testing whether load moves onto newcomers needs a graded compromise rule and a base with room in total.

**Calibrated to the vacancy debt method (TQ4).** With graded presenteeism losses and exit hazards rising with time overloaded, the revolving door did not appear. The base settled into chronic presenteeism instead: most staff present at reduced capacity, no exits, the record at 100%, and undone work leaving unrecorded. Whether it settles there or collapses into a revolving door turns on one question: does a worker in presenteeism feel overload against their baseline capacity or against what they can do now? (Open question for James.) **James's answer (5 October 2026):** the load and expectation stay the same, so the protective slowing and presenteeism compound the problem. Pressure is constant while local effectiveness falls as stress rises. Overload is therefore felt against what the part can do now. The local hockey stick is the day that stress shows as calling in sick, often the start of a long absence.

## 6. Control has a part too

Routing load by priority is itself work, done by control parts: signalling, sensing, the vasomotor centre, the hypothalamus. Those parts have capacity, reserve and priority like any other.

**Control failure.** If debt reaches the control parts, the routing rule fails. Load no longer flows by priority, and fixed capital can be hit while buffers remain. Shock (acidosis blunting the vessels' response to nerve signals; the brain's vasomotor centre short of blood) and hypothermia (vasodilation below about 34 °C) are the named mechanisms. This is James's "free for all" past the critical point.

## 7. The point of no return

Debt left on a part longer than its recovery window erodes its capacity:

- capacity falls (μ̇_i < 0) while D_i stays above zero for longer than τ_i;
- once debt is cleared, capacity is rebuilt at rate g_i towards its original level.

For permanent parts g_i = 0, so capacity lost there is lost for good. **The point of no return is the first moment debt erodes the capacity of a part with g = 0.** Before it, full recovery is possible. After it, the system can return, but not to the same state: head growth after severe early malnutrition; a plant's water pipes; neurons lost to stroke, with function rerouted rather than replaced.

Acute load is load repaid within τ. Chronic load is load that outlasts τ. The p53 result in the thread fits: pulses (acute, with recovery between them) led to recovery, while a sustained signal at a similar total led to permanent arrest.

## 8. Recovery

When demand at the top falls below capacity, the slack repays debt and refills reserves. The order follows from queue logic:

1. **Intake first.** Every repayment is financed by inflow, and the intake caps inflow. Rebuilding the bottleneck in the repayment path first maximises the speed of all later repayment. Hence the gut lining is rebuilt before food arrives (rats in stage 3), and the gut before fat at stopovers.
2. **Working parts the next demand needs**, in priority order. This is where the state reassigns roles (fat before muscle for a migrating bird).
3. **Reserves last.** Iron stores after haemoglobin, root carbohydrate after leaves, winter stores after the brood.

Time to full recovery is set by the slowest term: debt divided by renewal rate in each part. Recovery is complete only when no part carries debt and reserves are full. Capacity lost in permanent parts never returns.

**Unknown debt cannot be repaid (James, 5 October 2026).** The order above assumes the debt is known. In the body it is, because each part signals its own state (hunger, hormones, the gut repairing itself in stage 3). In the systems this work cares about, shrouded in opacity, the debt below is unknown, so it cannot be repaid. Two consequences:

- **What is recorded recovers; what is not, stays.** When pressure eases, the measures the record holds come back. Unrecorded debt (exhaustion, deferred maintenance, eroded skills) remains, keeps wearing down capacity after load has fallen, and can carry a renewable part into compromise and a permanent one past the point of no return. The system returns to a lower baseline. That is hysteresis produced by opacity.
- **Self-rebuilding needs local slack.** A renewable part can rebuild itself without anyone above knowing, but only if its own load actually falls. If capacity above was set from the flat record, the load on the part does not fall, and it gets no slack to rebuild in.

## 9. Signals and the record

Each part produces two things the top can see:

- **its output**, which feeds the record. The record is produced through the part's strained capacity;
- **a state signal through its own channel** (hunger, pain, fatigue in the body).

Two candidate rules:

- **Chronic signals lose gain.** A sustained signal makes its receiver turn down its gain (leptin and insulin resistance, receptor adaptation, p53 desensitisation, load degrading reporting). Pulsed signals keep their weight. So the warning fades just as load becomes chronic, which is when it matters most.
- **Institutions lack separate state channels.** They hear mainly through the output record, which a buffering tier keeps flat. What state signals there are, are mistranslated: filtered, rationalised, blocked by incentives, silenced through fatigue, or lost when people leave (Section 7.5 of the theory note; the "downregulation" of the prior thread).

## 10. Questions for James

Answered 5 October 2026:

1. **Tier by tier, or anywhere lower?** Anywhere lower, as in the body. The hierarchy is a tier list, and the path of least resistance governs where load lands. First-degree links buffer against harm (Section 3).
2. **Repayment or rebuilding?** In opaque systems the debt is unknown, and what is unknown cannot be repaid (Section 8).
3. **Does priority change with depletion?** Each part has an optimal, a stressed but coping, and a compromised state (Section 4a).

Open:

4. **Resistance.** Answered: load passed on through opacity has no origin and cannot be refused; resistance needs a direct link to the generating part (Section 3).
5. **Recovery of a compromised part.** Answered: compromise leaves a mark; only working parts are compromised (Section 4a).

## 11. Candidate predictions (for later; none frozen)

- **Order down:** depletion follows reverse priority, and priority correlates negatively with renewal rate and with spare capacity.
- **Lag:** the delay before the top's record changes scales with usable buffer ÷ overload. Larger reserves give longer silence and a sharper break.
- **Order up:** recovery starts at the intake, and full recovery time is dominated by reserves and by any debt on low-renewal parts.
- **Signal shape:** for the same total, sustained warnings lose weight relative to pulsed ones.
- **Past control failure:** the depletion order breaks, and fixed capital is hit while buffers remain.
- **Where load lands:** in low-coupling systems, unlabelled load sinks to the lowest tier. Labelled load can be held higher up, where a part can see its origin and refuse it.
- **Scars:** parts that recover from compromise carry a lower ceiling and push back more. Unlabelled load then shifts towards parts without scars (new hires).
- **Record and state:** a part's output record changes only at compromise. Its state signal and its reserve change from the start of stress.
- **Opacity hysteresis:** after pressure eases, recorded measures recover and unrecorded debt does not. Capacity in the parts carrying it keeps falling after load has fallen.

## 12. What this does not yet have

- A worked example with numbers (a small simulation would show the flat record and the break; the paper one simulation is a single-tier special case).
- A check that the recovery-order argument (bottleneck first) holds when intake and reserves compete for the same slack.
- Any test. All the cases cited are the ones that suggested the model, so they illustrate it and do not confirm it.
