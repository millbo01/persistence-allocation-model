# Tier-queue core: specification (5 October 2026)

**Status:** theorising (phase 3).

**Code:** theory/sim/tq_core.py. Institutional features (turnover, hiring, cover) are kept out of the core.

**Builds on:** theory/tier_queue_model_DRAFT.md and the plan in theory/tier_queue_natural_tests_plan.md.

## Parts

| Kind | What it does | States |
|---|---|---|
| Working part | Serves its own demand. Has a priority, a capacity, a renewal type (renewable or permanent) and a ceiling | Optimal, coping, slowing (protective), compromised |
| Intake | A working part whose work brings resource in. It is first in line for repayment | As a working part |
| Control part | A working part whose job is routing. If it is compromised, routing by priority fails | As a working part |
| Reserve | A shared stock with a release limit. Drawn first, refilled last | Full, drawing, empty |

## Each step

1. **Effective capacity** = ceiling × capacity × (1 − loss(exposure)), with a floor of 20%.
   - Loss is 0 below exposure 4.
   - Protective slowing gives a 10% loss from 4 to 13, and halves the build-up of exposure.
   - Compromise loss runs from 13% at exposure 13 to 50% at 78. These are the bands of James's vacancy debt method.
2. **Routing,** highest priority first. A shortfall goes in this order:
   - to the reserve;
   - to spare capacity in lower-priority parts;
   - displaced onto lower-priority parts, lowest first, up to 35% of each receiver's capacity;
   - whatever is left becomes the part's own debt.

   Unlabelled load (the opaque regime) cannot be refused. Labelled load (the coupled regime) is refused by parts already slowing or compromised.
3. **Control failure.** If a control part is compromised, the shortfall is spread across all other parts by capacity, protected parts included.
4. **Exposure.** Overload is felt against current capacity (James, 5 October 2026): exposure builds with (carried demand ÷ effective capacity − 1) ÷ 0.25. Carried demand is the part's own demand plus what was passed to it, excluding what it passed on. When carried demand is under capacity, exposure falls at half that rate. Losses therefore compound.
5. **Coupled regime only:**
   - the top sheds demand, visibly, when lagged state signals show slowing below (the stage 3 switch, dropping the egg);
   - a coupled top drops work it cannot place, rather than carrying it as debt;
   - parts that are slowing or compromised are rested: their own demand is cut to 80% of capacity.
6. **Repayment.** Slack repays a part's own debt. In the coupled regime, the top's slack repays the intake first, then the other parts. The reserve is refilled last.
7. **Scars and permanent loss.** A renewable part leaving compromise loses half its peak loss from its ceiling (floor 50%). A permanent part keeps any loss.

## The starting state is an input (James, 5 October 2026)

Exposure, ceiling and reserve level can start anywhere, so a run need not begin optimal. `classify_baseline` reads the starting stage from state signals first.
- **Opaque system:** the record sees compromise, not stress.
- **Coupled system:** the record moves early, because shedding is visible, so it cannot by itself separate stress from compromise.

## Two read-outs every run

- **The record:** the share of the top's raw demand served, counting shed demand as unserved.
- **State signals:** each part's exposure, stage, effective capacity and debt, and the reserve level.

## Rule for tests against natural systems

1. Read the system's starting stage from baseline state markers, before predicting anything.
2. State predictions conditional on that stage.
3. Population reference ranges are not optimal. Many study populations start stressed (James: a standard Western diet), so "normal" baselines may be the stressed stage.

## Refinements after natural test 1 (James approved, 5 October 2026)

- **A. Shared upstream supply.** A part can depend on an upstream part (`supply`, `supply_w`). Its capacity then follows that part's served share from the previous step, so a protected part is protected only partly when the supply itself falls. This comes from blood loss: brain blood flow fell with cardiac output while pressure was held.
- **B. Active threshold switch in control (`Switch`).** When the buffer reaches a set depletion, control changes mode and sheds part of the top's demand until the buffer recovers. This comes from blood loss (sympathetic withdrawal at about 30% loss), and is intended to unify the fasting stage 3 switch and the abandoned egg.
- **Reserve release knee.** Below `knee` × max, release falls in proportion to level: a small store cannot release fast enough.

TQ5 outputs are unchanged by these additions; they are off by default.

## v0.4 additions (5 October 2026; on only with `run(..., adapt=True)`)

- Growth after acute, coupled episodes (ceiling up, capped at 1.3).
- Re-tuning protection against the same load (fades, time constant 100 steps).
- Demand-cutting scars for parts flagged `cut_on_scar`.
- Recovery funded in order: own slack first; then, after a chronic episode, the reserve is enlarged and refilled first; otherwise intake, then the other parts, then the reserve.

See TQ7 (theory/sim/outputs/2026-10-05_TQ7/README.md) for what these generate and where the engine still departs from the written model.

## v0.5 additions (5 October 2026; on only with `run(..., priority="computed")`)

No priority numbers are set by hand except the top, named because its output is the record. Parts carry `vital`, `rebuild` and, for an intake, `supply_input`.
- **Value** each step: vital × b(L), where b rises from 0.05 (below 70% use) to 1 (full use). L is measured against current capacity. An intake with nothing to take in has no value.
- **Spending order (v0.6):** ascending value × (1 + min(rebuild, T)), where T is the remaining horizon (default 100 steps; `run(horizon=...)` may be a function of time). The parts are re-sorted every step. (v0.5 used value × (1 + rebuild ÷ 100), which made fixed capital dearer as the horizon shortened.)
- **Recovery:** slack is pooled across parts and allocated in descending value. The reserve competes on its own value, the expected shortfall (a 30-step running average of steps on which total demand exceeded total current capacity), and waits while a part of higher value is still under repair. The reserve's size is base × (1 + expected shortfall).
- **Signal gain:** control sees value through each part's gain (default 1 coupled, 0 opaque; a part may carry its own). A sustained signal (load above capacity) loses gain with a time constant of 30 steps and recovers when strain ends.

See TQ8 (theory/sim/outputs/2026-10-05_TQ8/README.md) for what these generate, the fixes made during the build, and where the engine still departs from the written model.
