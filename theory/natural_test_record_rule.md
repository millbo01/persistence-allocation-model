# Natural test 9: what counts as a record? (5 October 2026)

**Status:** theorising (phase 3); testing a mapping rule. The predictions below were committed before searching.

## The mismatch being tested

In overtraining, performance fell alongside mood rather than after it (natural_test_muscle.md, M3). G1 (the record stays flat while state signals move) seemed not to hold there.

**Proposed rule R.** A measure stays flat until compromise only if it is a **held output**: delivered below capacity, and kept up by buffers (spare capacity, recruitment, compensation, a reserve or a control loop defending it). A measure taken **at capacity**, or directly on the working units, is a state signal: it tracks strain and loss from the start.

**Applied to the muscle mismatch:** overtraining is usually detected with maximal tests (time trials, maximal force). Those probe capacity directly, so they are state signals, and moving early is what rule R predicts. A held output in muscle would be force at a submaximal level, kept up by recruiting more motor units as fatigue builds.

## Cases and predictions

Each case pairs a held output with a direct or capacity measure in the same system.

| Case | Held output (predicted flat until large loss) | Direct or capacity measure (predicted to move first) | Contamination |
|---|---|---|---|
| R1. Muscle fatigue | Submaximal force or task output, held by recruiting more motor units | Maximal force; the electrical activity needed to hold the same submaximal force | Known in outline |
| R2. Noise-induced cochlear damage | Hearing thresholds (the audiogram) | Counts of synapses between hair cells and nerve fibres; the amplitude of the auditory nerve response | Known in outline ("hidden hearing loss") |
| R3. Glaucoma | Visual field (what the patient sees) | Retinal nerve fibre layer thickness and ganglion-cell counts | Known in outline |
| R4. Glucose regulation | Fasting blood glucose, defended by insulin | Insulin level and beta-cell function | Known in outline |
| R5. Thyroid | Thyroxine (T4), defended by the drive hormone | Thyroid-stimulating hormone (TSH), the control signal | Known in outline |

**Contamination is heavy:** all five are known to Claude in outline. The test is whether rule R sorts them **all** correctly, and whether any case breaks it (a held output that moves early, or a direct measure that stays flat). One clear break would count against rule R.

**If rule R holds,** it is added to the mapping procedure (Section 5, step 3): the record must be a held output, not a capacity test or a direct measure on the working units.

## Results (surface level, from search summaries, 5 October 2026)

| Case | Held output | Direct or capacity measure | Verdict |
|---|---|---|---|
| R1. Muscle fatigue | Submaximal force is held: "additional motor recruitment is required to sustain the same level of submaximal force" | Surface EMG "shows a progressive increase in total activity as the muscle fatigues", while force-generating capacity falls | Consistent |
| R2. Noise and the cochlea | Hearing thresholds return to normal after noise | About 50% of the synapses between inner hair cells and the auditory nerve are irreversibly lost, and the auditory nerve response (ABR wave I) is smaller (Kujawa and Liberman 2009, in animals) | Consistent in animals. **Caveat:** human evidence is contested (Guest et al. 2018 found no evidence of synaptopathy in people with normal audiograms) |
| R3. Glaucoma | Visual field defects appear only after 25 to 40% of ganglion cells are lost (an average of 28% at the first defect, range 6 to 57%) | Thinning of the retinal nerve fibre layer precedes functional loss by up to 5 years | Consistent |
| R4. Glucose | Fasting glucose stays near normal through the compensation phase | Insulin rises during the normal-glucose and prediabetes phases, then falls once fasting glucose passes about 5.5 mM. About 80% of beta-cell function is lost by diagnosis | Consistent. **Note:** the compensation's own measure (insulin) rises, then falls at the break, the same shape as cerebral blood velocity before collapse in growth restriction |
| R5. Thyroid | Free T4 normal | TSH raised (subclinical hypothyroidism) | Consistent |

## Verdict

**Rule R sorted all five cases, and none broke it.** All five were known in outline, so this confirms the rule's coherence, not its novelty or truth. It also resolves the muscle mismatch: overtraining is detected with capacity tests, which are state signals, so moving early is what rule R predicts.

**Added to the model in v0.4:**
- Mapping step 3: the record must be a held output, below capacity and kept up by buffers or a defending loop. Capacity tests and direct measures on the working units are state signals.
- Candidate generic prediction G11: a compensation's own measure rises while it holds the record, then falls at the break (insulin; cerebral blood velocity in growth restriction). A falling compensation measure can look like improvement.

**Update (James, 5 October 2026).** G11 was withdrawn as a generic prediction because it adds no mechanism. The pancreas compensates for load generated elsewhere (insulin resistance), its output rises while it copes and falls when it is exhausted. That is the existing cascade. It is kept only as a reading note in v0.4, Section 4: a falling compensation measure is ambiguous until the load at its source is checked.
