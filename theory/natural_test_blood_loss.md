# Natural test 1: blood loss and lower body negative pressure (5 October 2026)

**Status:** theorising (phase 3). This is a check of the tier-queue model against published findings. It is not a pre-registered data test.

**Predictions** N1 to N6 were committed before any source was opened: theory/tier_queue_natural_tests_plan.md, commit 4f013e9.

**Contamination, as declared there.** Claude knew the ATLS class scheme and the outline of the compensatory reserve work, so N1 to N3 can only be "consistent". N4 and N5 carry more weight.

**Sources** were found by web search and read through summaries of the open full texts, not read in full by Claude:

| Ref | Source | Notes |
|---|---|---|
| S1 | Scully et al. 2016, Physiological Reports | Conscious sheep, slow against fast haemorrhage. PMC4831318 |
| S2 | Convertino et al., Integrated compensatory responses in a human model of hemorrhage | PMC5226259 |
| S3 | Variability in integration of mechanisms associated with high tolerance to progressive reductions in central blood volume | PMC4759043 |
| S4 | Heat stress and LBNP tolerance, 60 paired trials | PMC4948742 |
| S5 | Regional vascular responses to prolonged LBNP; cerebral velocity at presyncope | Abstracts via search |
| S6 | Lower body negative pressure review | Physiological Reviews 2018 (search summary) |
| S7 | Schadt and Ludbrook 1991, as cited in S1 | Biphasic response |
| S8 | Earlier blood donation and iron sources in this conversation | Finnish Red Cross; Stanford Blood Center; PMC5094173 |

## Starting stage

- **Main studies (S2, S3, S5):** healthy volunteers with normal baseline heart rate and pressure, and conscious healthy sheep (S1). These are read as optimal or near optimal. The model cannot tell whether "healthy volunteer" baselines are truly optimal or the stressed stage (James's point about a Western diet). None of the studies reports reserve-type markers at baseline.
- **Natural experiment on starting state (S4):** whole-body heat stress before LBNP. At baseline, heart rate was "profoundly elevated" and mean arterial pressure "slightly decreased", with core temperature 38.3 °C and skin 38.5 °C. By the core's classifier, that is a stressed start: state signals moved, record near normal.

## Results by prediction

| Prediction | Finding | Verdict |
|---|---|---|
| **N1.** Blood pressure stays near baseline while heart rate rises and stroke volume falls from the start | Stroke volume and cardiac output fall from early LBNP, and the compensatory reserve index declines "early and progressively throughout", while blood pressure holds until late: changes after about 25 minutes, against an early fall in reserve (S2). Arterial pressure is held by reflex rises in heart rate and resistance at −40 mmHg (S6). In one representative subject, heart rate changed later than stroke volume and reserve (after about 15 minutes; S2) | **Consistent.** The state signals that move first are stroke volume and reserve; heart rate follows later |
| **N2.** Lower-priority beds are cut before the brain and heart | At −10 mmHg, forearm (skin and muscle) and splanchnic flow fell while renal flow did not; at −20 to −40 mmHg, splanchnic flow fell further and renal flow fell (S5). Cerebral velocity fell less than cardiac output (−15.5% against about −30%). **But** at presyncope, cerebral velocity was down 27.3% while mean arterial pressure was 2% above baseline (S5) | **Partly consistent.** The order of cuts among lower-priority beds matches. The brain's supply was protected only partly: it fell before the record moved. See mismatch 1 |
| **N3.** The break in blood pressure is steep against the earlier change; control failure breaks the order | "Sudden onset of hypotension and bradycardia" (S6). In sheep, a gradual decline over the first 90% of blood removed, then a sudden drop in the last 10% (S1). The break is the switch from sympathetic excitation to inhibition at about 30% blood loss (S7) | **Steepness consistent.** The mechanism differs: see mismatch 2 |
| **N4.** A buffer that is a stock gives the same cumulative loss at the break whatever the rate; a rate-limited buffer breaks earlier when loading is fast | Blood volume removed when pressure had fallen 30 mmHg: slow (0.4% of blood volume a minute) 27.0 ± 4.2%; fast (2% a minute) 27.3 ± 3.2%; P = 0.47; n = 8 sheep (S1). Rate was "not a significant factor" in tolerance. Fast bleeding raised heart rate earlier | **Consistent with a stock** over a fivefold range of rates. Small sample. A clinical statement that slow bleeding is better tolerated exists (search summary of a review) but was not traced to data |
| **N5.** A larger buffer means a longer time to the break | Tolerance is a property of the individual: one third of more than 250 people tested had low tolerance and two thirds high (S2). In sheep, blood volume lost at the break ranged from 13% to 48% (S1). The compensatory reserve index falls from full towards zero at decompensation in every subject (S2). Heat stress, a smaller effective buffer (sweat loss lowers blood volume; hot skin holds blood away from the centre), cut tolerance by about 70% (cumulative stress index 997 ± 437 to 303 ± 213 mmHg·min; time 19.8 to 9.1 minutes; last stage reached 80 to 40 mmHg; 60 paired trials; S4). Within high-tolerance subjects, different strategies (higher heart rate against higher stroke volume) gave the same tolerance (S3) | **Consistent.** Whether pressure stays flatter for longer with a larger buffer was not found |
| **N6.** On recovery, heart rate and pressure return quickly; lower-priority beds and reserves return last | After donation: volume within hours, red cells in 4 to 8 weeks, iron stores last (S8). After iron therapy, haemoglobin returns before stores. The return of renal and splanchnic flow after haemorrhage was not sought | **Partly consistent.** Reserves are last; the order of recovery among lower-priority beds was not checked |

## Starting state: the heat-stress experiment

Heat stress shows the core's point about baselines directly. The same challenge (graded LBNP) given to the same people from a stressed start produced a break about 70% sooner. The baseline record was near normal: mean pressure only slightly lower. The state signal (heart rate) was profoundly raised. A study that took the heat-stressed baseline as "normal" would misjudge tolerance badly. This is the TQ5 result in a natural system, and it is the closest thing in this test to a confirmation, since it was not among the predictions written down.

## Mismatches (logged as found)

1. **The top part is not fully protected before the break.** Brain blood flow (middle cerebral artery velocity) fell steadily, by 27% at presyncope, while the defended figure (pressure) was unchanged. In the model, the top's supply is protected until the buffer runs out. In reality, protection is partial and graded: the brain's share is defended, but its absolute supply falls with cardiac output.
   - **James's rule:** this is logged as found. The theorised place for the shortfall is that the brain's supply depends on cardiac output, which is itself falling (the brain cannot be supplied with blood the heart does not receive; PMC4166953's title). Whether that is a fault of the model or a feature to add (the top shares a common upstream supply) is for James.
   - **Note:** this strengthens the measurement rule. The defended figure (pressure) misread even the state of the most protected part.
2. **The break is an active switch, not a passive control failure.** Decompensation in haemorrhage is a switch from sympathetic excitation to inhibition, with bradycardia (S7). In the model, the break comes when debt reaches the control part and routing fails ("free for all"). The evidence points instead to a control decision at a threshold. One reading, Claude's theorising: it protects the heart by cutting its work when filling is too low, like the fasting stage 3 switch.
   - **Proposed refinement (for James):** a threshold switch in the control part. It sheds load, or changes mode, at a set depletion of the buffer, before passive failure. That would make blood loss, the fasting stage 3 switch and the abandoned egg the same mechanism.

## Verdict for the model

- **Consistent:** N1, N3 (steepness), N4 and N5.
- **Partly consistent:** N2 and N6.
- **Starting-state effect:** strongly shown by the heat-stress experiment.
- **Two mismatches, each with a proposed refinement:** the top shares an upstream supply, so it is protected only partly; and the break is an active threshold switch in control.
- **Weight:** N4 rests on 8 sheep. Nothing here is a pre-registered test, and N1 to N3 were partly known in advance.
