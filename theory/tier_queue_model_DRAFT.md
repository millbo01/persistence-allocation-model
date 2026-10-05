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

**Where export goes.** It goes to the lowest-priority part that still has reserve or spare capacity. In a body that means the part that is cheapest to spend. Whether export must pass tier by tier, or can jump to any low-priority part, is open (question 1 in Section 10).

**Why harm happens below.** Imported load arrives as demand on the receiver (m_k). It first uses the receiver's reserve, then displaces the receiver's own work, which becomes the receiver's debt D_k. This is James's point: load does harm by displacing the receiving part's own work, not by being "foreign".

## 4. Conservation

Summed over all parts and the boundary, in any currency that obeys a balance law:

total demand = work served + reserves drawn + debt accumulated + load exported across the system boundary.

This is the flow identity of the prior thread (generated = resolved + exported + backlog increase + abandoned or suppressed), with reserves and debt made explicit, and it is the C1 form of P1. Nothing leaves the ledger except through work done or the boundary. "Abandoned" work is debt sitting somewhere.

## 5. Why the top looks steady, then breaks (the hockey stick)

While any lower part has reserve or spare capacity, the top exports its shortfall and its output A_top stays near μ_top. Its record is flat however far demand rises. The excess is visible only as falling reserves and growing debt below.

Let the overload be E = demand − capacity at the top, and let the usable buffer below be the sum of reserves and spare capacity in the parts that can receive. The time before the top's own output must fall is roughly

T ≈ usable buffer ÷ E

(the rate at which buffers can be released also caps it). When the buffer runs out, the excess has nowhere to go but the top's own work or other high-priority parts. The effective service rate drops from capacity plus buffer release to bare capacity, utilisation jumps past 1, and the change is abrupt. In queue terms, the buffer was holding ρ below 1. Its exhaustion pushes ρ past 1, and waiting and debt rise steeply (W ∝ 1/(1 − ρ) as ρ approaches 1).

This links to paper one. Receiver withholding is a tier holding back unresolved work, so the record reaching the top is the served work A, and the record is flat for the same reason. It also fits the K1b bee result already logged: stores held flat at the cap while about 70% of hive bees were lost, and the record (weight, stores) lagged by months.

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

## 9. Signals and the record

Each part produces two things the top can see:

- **its output**, which feeds the record. The record is produced through the part's strained capacity;
- **a state signal through its own channel** (hunger, pain, fatigue in the body).

Two candidate rules:

- **Chronic signals lose gain.** A sustained signal makes its receiver turn down its gain (leptin and insulin resistance, receptor adaptation, p53 desensitisation, load degrading reporting). Pulsed signals keep their weight. So the warning fades just as load becomes chronic, which is when it matters most.
- **Institutions lack separate state channels.** They hear mainly through the output record, which a buffering tier keeps flat. What state signals there are, are mistranslated: filtered, rationalised, blocked by incentives, silenced through fatigue, or lost when people leave (Section 7.5 of the theory note; the "downregulation" of the prior thread).

## 10. Questions for James

1. **Does export pass tier by tier,** each part handing its excess to the one directly below, or can it go straight to the lowest-priority part anywhere in the tree? The body seems to do the second: blood loss cuts skin, gut and kidney at once, not in sequence.
2. **Is recovery "repayment" or "rebuilding"?** Does the top pay back the debt it exported, so the lower part is made whole by the part that borrowed? Or does each part simply rebuild itself once load falls? The ledger works either way, but they predict different recovery times.
3. **Does a part's priority ever change with depletion,** apart from role reassignment? For example, does a nearly exhausted reserve become protected (fat at the stage 3 threshold triggers the switch)?

## 11. Candidate predictions (for later; none frozen)

- **Order down:** depletion follows reverse priority, and priority correlates negatively with renewal rate and with spare capacity.
- **Lag:** the delay before the top's record changes scales with usable buffer ÷ overload. Larger reserves give longer silence and a sharper break.
- **Order up:** recovery starts at the intake, and full recovery time is dominated by reserves and by any debt on low-renewal parts.
- **Signal shape:** for the same total, sustained warnings lose weight relative to pulsed ones.
- **Past control failure:** the depletion order breaks, and fixed capital is hit while buffers remain.

## 12. What this does not yet have

- A worked example with numbers (a small simulation would show the flat record and the break; the paper one simulation is a single-tier special case).
- A check that the recovery-order argument (bottleneck first) holds when intake and reserves compete for the same slack.
- Any test. All the cases cited are the ones that suggested the model, so they illustrate it and do not confirm it.
