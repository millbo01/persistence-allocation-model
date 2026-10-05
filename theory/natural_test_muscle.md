# Natural test 8: muscle after acute injury, chronic overload and disuse. Surface level (5 October 2026)

**Status:** theorising (phase 3); testing v0.3. The predictions below were committed before searching.

**Contamination, declared.** Muscle physiology is well known to Claude in outline: the repeated-bout effect, satellite-cell repair, training hypertrophy, overtraining syndrome, disuse atrophy and "muscle memory" (myonuclei retained). Most predictions here can only be "consistent". The value is in checking whether the model's categories sort these known facts without strain, and whether any of them fails.

## Mapping

- **Working part:** skeletal muscle (renewable through satellite cells; slower than the gut lining).
- **Load:** mechanical work.
- **Record:** performance, meaning force or time.
- **State signals:** soreness, creatine kinase, heart-rate variability, mood and fatigue scores, hormones.
- **Intake:** blood supply and protein synthesis.
- **Control:** the nervous and endocrine systems.

## Three conditions

1. Acute damage with recovery (a single bout of unaccustomed eccentric exercise).
2. Chronic overload without recovery (overtraining).
3. Chronic disuse (immobilisation, bed rest, spaceflight): demand removed.

## Predictions (committed before searching)

| No. | Prediction | Model source |
|---|---|---|
| M1 | Acute damage with recovery heals fully within days to weeks, and leaves **re-tuning**: the same bout causes less damage next time (repeated-bout effect). Repeated bouts with recovery between them give **growth** (hypertrophy) | v0.2 growth and re-tuning; G8 |
| M2 | Chronic overload without recovery gives **compromise**. Performance falls despite training, and recovery takes weeks to months (non-functional overreaching, overtraining syndrome) | G8 chronic side |
| M3 | **The record sees compromise, not stress.** In overload, state signals (heart-rate variability, mood and fatigue, hormones) shift before performance falls | G1 |
| M4 | **The acute-chronic flip in one tissue.** The same stimulus (eccentric load) builds muscle when acute and recovered from, and injures when repeated without recovery (overuse injury) | G8 |
| M5 | Disuse **re-tunes capacity down to demand:** atrophy, fast early loss. Regain on reloading is slower than the loss | Re-tuning to lower demand |
| M6 | **Memory:** muscle that was trained before regains faster after disuse (re-tuning kept as retained structure) | Re-tuning; G9 |
| M7 | **Starting state:** older or compromised muscle loses more in disuse and regains less (anabolic resistance) | G4 |
| M8 | **The type of past load sets recovery order (v0.3 G10).** After acute damage, the working tissue is rebuilt first. After chronic disuse or scarcity, fat (intramuscular or whole-body) recovers first or overshoots relative to lean during reloading | G10 |

## Results (surface level, from search summaries, 5 October 2026)

| Prediction | Finding | Verdict |
|---|---|---|
| M1. Acute damage: full healing, then re-tuning | After one damaging eccentric bout, "an adaptation occurs which significantly attenuates the magnitude of muscle damage induced by future bouts". The protection lasts up to 6 months after a maximal bout, and about 3 weeks after a low-intensity one (repeated-bout reviews, via search). Hypertrophy with repeated recovered bouts was not searched (known) | Consistent (known). The dose sets how long the re-tuning lasts |
| M2. Chronic overload: compromise | After overtraining syndrome, "it may take weeks, months or years to restore proper sports form" | Consistent (known) |
| M3. State signals move before the record | "Performance and psychological disruptions precede physiological changes." Mood worsens with high training volume, and heart-rate variability fell during intensive camps; overreaching was not obvious until day 7 | **Partly consistent.** Mood (a state signal) moves early, but so does performance (the record). In this system the record is not clearly late. Logged as found |
| M4. The acute-chronic flip in one tissue | Not searched (overuse injury is known) | Not tested |
| M5. Disuse re-tunes capacity down; regain is slower | Disuse loses about 0.5 to 0.6% of muscle mass a day over 10 to 42 days, fastest early (substantial loss within 5 days). In older adults, the loss from 14 days' immobilisation "cannot be regained with 4 weeks of aggressive resistance exercise training" | Consistent |
| M6. Memory | Myonuclei added in training are not lost in detraining ("myonuclear permanence"). Lost muscle and strength came back up to four times faster than in the original training | Consistent: re-tuning kept as structure |
| M7. Starting state | Older adults lose more in short bed rest and show anabolic resistance (blunted protein synthesis), with raised breakdown markers; younger adults do not | Consistent |
| M8. Type of past load and recovery order (G10) | After chronic restriction (dieting), fat came back before lean: 81% of weight regained over 12 months was fat, against 67% of the loss (preferential catch-up fat; thrifty metabolism with lower muscle protein turnover). Fat within muscle rises during immobilisation and inactivity | **Consistent with G10** for chronic restriction. Disuse-specific regain order was not found. Recovery after acute damage was not checked |

## What muscle adds

- **Re-tuning has a dose-dependent memory.** A bigger insult gives longer protection (6 months against 3 weeks). Myonuclei keep a structural memory of past training.
- **Loss and regain are asymmetric.** In older muscle, losing takes days and regaining takes longer than weeks. That fits "recovery needs slack, and compromised starts recover less".
- **A mismatch: the record is not always late (M3).** In overreaching, performance falls alongside mood. A possible explanation, to check before it counts: muscle performance is measured directly on the working part, not through a buffered top part, so it is a state signal, not a protected record. If so, the model's G1 applies only where the record is the output of a buffered, protected part. That is a mapping rule to make explicit (Section 5, step 3).

Weight: surface level; most findings were known in advance.
