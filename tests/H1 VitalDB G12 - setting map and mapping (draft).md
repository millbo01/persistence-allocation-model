# H1 VitalDB, test of G12: setting map and mapping (DRAFT, 6 October 2026)

**Status:** phase 5 preparation. **No VitalDB data has been opened.** The structure comes only from the documentation run (raw/2026-10-06_gemini_H1-VDB-S1.md; assessment in theory/tier_queue_heldout_datasets_DRAFT.md). Model: TIER_QUEUE_MODEL_v0.17.md (frozen vocabulary).

**Scope (James, option 1):**
- **Main:** G12.
- **Check:** G1.
- **Exploratory, not scored:** G18.
- **Not tested:** G3 (bleeding is recorded only as a total per case), kept for a later MIMIC-based test.

## 1. Setting map

| Item | Content |
|---|---|
| **The system** | One surgical patient under general anaesthesia **plus the anaesthetist**, treated as one system. The anaesthetist acts on the patient's circulation (infusions, fluids, ventilation) and is part of the governor that holds blood pressure: an outside defending loop, mapped explicitly (Section 2) |
| **Whose persistence** | The patient's |
| **The record (held output)** | Mean arterial pressure, watched and defended by the anaesthetist and by the patient's own reflexes |
| **Do the model's conditions hold?** | Yes. There is a governor (reflexes plus anaesthetist) holding a level (arterial pressure). There are finite parts (heart, vessel beds, organs), stores (blood in the veins and gut that can be shifted into circulation), and a load (blood loss) |
| **Confounds the setting produces** | (1) **The anaesthetist's boluses** of vasopressor are recorded only as case totals, not timed. Handled by selection (Section 3). (2) Infusions are timed (1 second) and fluids are case totals: both act on the record. (3) **Surgical events are not marked;** only case, anaesthesia and surgery start and end exist, with times from the electronic record rounded to 5 minutes. (4) **Arterial blood sampling** puts known artefacts into the pressure trace. (5) **Anaesthetic depth** and drugs lower pressure by themselves (vasodilation), independent of blood loss. (6) Cases differ in surgery type, position and patient |
| **Contrast setting** (where the model predicts a weaker effect) | **Falls in pressure soon after anaesthesia starts** (within a fixed window of the anaesthesia start marker), in cases with little blood loss. These falls come from drug-induced vasodilation acting at once, a switch with no store being depleted. So the model predicts no warning before them |
| **Contamination declared** | (1) The TQ-DS2a essay described dynamics before fainting in laboratory tests in general terms (a short volatile window; loss of a slow rhythm; micro-variation in the pulse waveform). (2) Claude knows in outline that falls in pressure during surgery can be predicted minutes ahead from features of the arterial waveform (commercial prediction indices). (3) Claude knows the two-phase physiology of blood loss (Section 2, item 5). **All three bear on G12; the result's weight is reduced accordingly** |

## 2. Mapping under v0.17 (Section 7 of the model)

1. **Boundary, currency and objective.**
   - **Boundary:** the patient's circulation plus the anaesthetist.
   - **Currency:** circulating blood volume and its delivery (pressure × flow).
   - **Objective:** the patient's persistence.
2. **Resources and stores.**
   - **Resource:** effective circulating volume.
   - **Stores, in order:**
     - **(i) blood held in the veins and the gut**, moved into circulation by reflex tightening of the veins (fast);
     - **(ii) fluid shifting from tissues into the blood** (slow);
     - **(iii) fluids and blood given by the anaesthetist** (outside supply, recorded as case totals).
   - **Spill:** not applicable.
3. **The governor and its levels.**
   - **X = mean arterial pressure.**
   - **Levels it depends on:** cardiac output and vascular resistance.
   - **The governor:** the patient's reflexes (blunted by anaesthesia) and the anaesthetist (infusions timed; boluses untimed, excluded by selection).
4. **Parts.**
   - **The heart:** a transporter, non-bypassable.
   - **Vessel beds by rank:** skin, gut and kidney lowest, giving up flow first; brain and heart highest.
   - **No units are tracked here.** The test reads only the record.
5. **The release profile: the decision G12 depends on.**
   - **The physiology (known):** in phase 1, reflex tightening of vessels holds pressure, drawing on blood held in the veins and gut. After roughly 20 to 35% of blood volume is lost, phase 2 begins: an abrupt reflex withdrawal of vessel tightening and slowing of the heart, with a steep fall in pressure (reviews PMC1918009, PMC2739247; general anaesthesia blunts these reflexes).
   - **What it means for the model:**
     - store (i) **tapers** as it empties: the blood that can be shifted out of the veins shrinks as volume is lost;
     - compensation can also end in a **switch** (phase 2).
   - **What G12 predicts under each:**
     - a taper gives a warning (slower recovery from small knocks, rising autocorrelation and variance of pressure before the fall);
     - a switch gives none.
   - **One must be committed before the data are opened. Options are in the box below.**
6. **Links.**
   - The heart is the severance point.
   - Shared dependency: heart rate, stroke volume and pressure all depend on the circulating volume (G18, exploratory).
7. **The clock.**
   - Pressure numerics every 2 seconds; the waveform at 500 Hz.
   - Windows are judged in minutes.

> **Decision for James: the release profile to commit for falls during substantial blood loss.** This bears on how refutable the test is.
>
> - **A (recommended): taper, then possibly a switch.**
>   - **Predicted:** before falls during substantial blood loss, the warning signs rise (recovery time, autocorrelation and variance of pressure, against matched control windows from the same cases). They rise **more than** before falls soon after anaesthesia starts (the contrast).
>   - **A null counts against G12 as mapped for this system.** It is logged as a failure, not explained away by "it was a switch".
> - **B: switch.**
>   - **Predicted:** no warning before falls during blood loss.
>   - **Why not recommended:** this tests only the absence of a signal, which is weak and easy to pass, so it is not a real test of G12's positive claim.
>
> **Claude's view:** A. It commits to the claim that can fail, it uses a contrast built into the data, and a failure is counted as one.

## 3. Selection (to be fixed in the pre-registration; outline)

**Cases:**
- general anaesthesia;
- an arterial line (SNUADC/ART or Solar8000/ART_MBP present);
- substantial estimated blood loss (a fixed absolute threshold to be set from clinical convention, not from the VitalDB distribution);
- **no bolus vasopressors** (intraop_phe = intraop_eph = intraop_epi = 0);
- vasopressor infusions allowed but timed, with a sensitivity analysis excluding falls preceded by any infusion change.

**Falls ("the break"):** a fixed definition of a sustained fall in mean arterial pressure, taken from clinical convention and set before data.

**Contrast falls:** falls within a fixed window after anaesthesia start, in cases with low estimated blood loss.

**Artefacts:** removed by a fixed rule (for example the known arterial blood-sampling spikes), set before data.

## 4. Next

1. **James decides the release profile** (A or B).
2. **Claude writes the pre-registration:**
   - predictions;
   - case and fall definitions;
   - windows and measures (recovery time after small dips, lag-one autocorrelation and variance of mean arterial pressure, against control windows);
   - pass and fail rules;
   - the analysis code plan;
   - contamination;
   - the adjudication and replication route.
3. **James confirms;** the pre-registration is frozen and committed.
4. **James accepts VitalDB's data-use terms.** Only then is data opened.
