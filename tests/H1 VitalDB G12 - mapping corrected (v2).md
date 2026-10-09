# H1 VitalDB G12: mapping corrected (v2), 8 October 2026

**The frozen file remains the test record.** It is `tests/H1 VitalDB G12 - setting map and mapping (draft).md` (6 October 2026), frozen with the pre-registration. This file corrects the mapping under CANON.md and the v2 decisions (D6; James's Step A answers, 8 October 2026).

**What this file does not do:**
- **It changes no verdict.** H1's verdicts stand: G12 Fails, at half weight; the G1 check is Not consistent, at low weight.
- **It is not a new test.** Any test that uses this mapping is pre-registered separately, before its data are opened.

**What it is:** a worked example of mapping in the v2 model (paper, Supplement S9).

**Corrected 9 October 2026 (James, after FINAL_CHECK round 2).** The frozen file is not edited, and no verdict changes.
- **The protected flow** is the oxygen the brain draws from its blood supply, measured against its resting need, not oxygenated blood flow. In blood loss the resource is oxygen. Blood flow and oxygen delivery are means: oxygen delivered but not drawn returns in the venous blood (CANON 2; CANON 5, "Name the resource, never its carrier or its route").
- **Mean arterial pressure** is an indicator. It tracks a level the governor holds: the stretch of the arterial wall at the carotid sinus and aortic arch, sensed by the baroreceptors (the arterial baroreflex).
- **What changed in this file:** the protected flow (Section 1), "Resource and currency", the indicator, the slips table's currency row and the bias ledger's resource row. The 8 October record of James's resolution (end of Section 4) is kept as written.

**Order of mapping (CANON 5):** the boundary first, then the top and the protected flow, then everything else.

## 1. The mapping

| Component | In this setting |
|---|---|
| **Boundary** | The patient. The anaesthetist is an outside loop acting on the patient from beyond the boundary. Fluids and blood given are outside input |
| **Top** | The brain |
| **Protected flow** | The oxygen the brain draws from its blood supply, measured against its resting need, fixed in advance (to be sourced) |
| **Governor** | Brainstem reflexes, and nerve and hormone signals. Its targets are on sensed levels, each to be sourced: (i) wall stretch at the carotid sinus and the aortic arch, the inlet to the top's supply; (ii) stretch in the heart's filling chambers and the great veins, which reports the store's level; (iii) oxygen and carbon dioxide. The governor owns the signals and does no work. Tissue that makes or carries the signals does work, so it is parts (CANON 3) |
| **Network** | The vessels, as routes |
| **Parts** | (i) The heart, a support part: delivery of the protected flow depends on its work. (ii) Vessel-wall muscle, which does the narrowing work on the governor's signal. (iii) The kidney, gut, skin and muscle beds, ordinary parts ordered by documented constriction under sympathetic drive (to be sourced bed by bed; the paper cites Bergauer et al. 2026 for splanchnic and Sadid et al. 2026 for renal constriction) |
| **Stores** | Blood held in the veins and gut (fast release) and tissue fluid (slow release). A vein is a route; the blood it holds is a store (CANON 3: roles, not objects) |
| **Outside input** | Fluids and blood given |

**Resource and currency** (corrected 9 October 2026).
- **The resource** is oxygen. Blood is its carrier and the vessels its route (CANON 5).
- **The currency** is the oxygen the brain draws, counted against its resting need. Blood flow and oxygen delivery are means: oxygen delivered but not drawn returns in the venous blood.
- **Oxygen content per unit of blood** is treated as fixed, and this is declared, so blood held in the stores can be counted by volume. If fluids dilute it, that no longer holds, and the stores are counted in the oxygen they carry.

**Indicator.** Mean arterial pressure is an indicator. It tracks a level the governor holds: the stretch of the arterial wall at the carotid sinus and aortic arch, sensed by the baroreceptors (the arterial baroreflex; Chapleau, Hajduczok and Abboud 1991). It is not the protected flow (CANON 3).

**Mode.** The decompensation switch (sympathetic withdrawal; Evans et al. 2001) is a mode change. It ends the snapshot (CANON 4).

**Dependency and the margin.**
- **The dependency:** delivery to the top depends on the heart's work, a support part.
- **The margin:** the protected flow holds while what goes unmet stays within the other parts' full draws (the vessel beds below the heart), so $M=D$, the case with the dependency (paper, Proposition 2).

**Release profile.** Not committed here. The frozen map committed a store that tapers as it empties, possibly ending in a switch; the pre-registration named the release profile as the first candidate for revision if G12 failed, and it is logged as that. Which release profile held in the VitalDB cases is untested. The pre-registration bars explaining the null as a switch, and it is not explained (corrected 9 October 2026, James's ruling J2).
- **Evidence elsewhere:** Table 4's sheep result (the same blood volume removed at a 30 mmHg fall in pressure across a fivefold difference in bleeding rate; Scully et al. 2016) fits full release, or a store with high turnover relative to the gap, if that fall marks the protected flow's break, which was not observed.
- **Under anaesthesia:** a later test must fix its release profile from evidence under anaesthesia: in Evans et al. (2001), anaesthetic agents blunted or abolished the compensation (for example, halothane) or the switch (for example, alfentanil).

**Access settings set from outside.** The anaesthetist's drugs change access settings from beyond the boundary. Within a snapshot every setting is fixed (CANON 3), so a change of drug or infusion rate either starts a new snapshot or is a confound. A test must name which, in advance.

**Units.** Not tracked. Units take their part's access (CANON 3).

**What the reduced form leaves out.**
- **The observation:** the brain's own vessels narrowed as its blood flow fell, in simulated blood loss (rising cerebrovascular resistance; Bondar et al. 1995).
- **What the model does with it:** the reduced form simplifies this away. It is logged against the model in Supplement S7.3.
- **A candidate cause, logged but uncited:** lower carbon dioxide from faster breathing narrowing the brain's vessels. It stays uncited until a source is read and checked.
- **A second candidate, logged, not yet checked:** as flow falls, the brain can draw a larger share of the oxygen reaching it, so its draw may have held for part of the fall (paper, S7.3).

## 2. What H1 measured, in these terms

- **G12 as tested:**
  - G12's derivation put the warning in the protected flow. Proposition 2 says the protected flow is silent before the break.
  - H1 measured mean arterial pressure, an indicator, not the protected flow.
  - G12 as stated failed, and the verdict stands.
- **G27,** the corrected prediction: as the break approaches, fluctuations in the gap show first in the store's release while it has headroom, then in the access of the lowest-ranked bed still supplied, then in each bed above it in turn, and in the protected flow only at the break.
  - **What a test needs:** measures of flow to each bed (or the store's level, and each bed's flow), which VitalDB does not record.
  - **The lead time here:** not predicted; the release profile under anaesthesia is untested.
- **G18 as mapped in H1** paired heart rate and stroke volume (two outputs of one part, the heart) with mean arterial pressure (an indicator). It was not a test of G18 as stated, which concerns parts sharing a dependency. A G18 test would pair two parts that share a dependency, for example two vessel beds.

## 3. Slips in the frozen map

Each slip is quoted from the frozen file, with its line number.

| Slip | Frozen text (line) | Corrected here |
|---|---|---|
| The heart called a "transporter" | "**The heart:** a transporter, non-bypassable." (41) | The heart is a support part. The vessels are the network |
| The heart called "the severance point" | "The heart is the severance point." (54) | Severance is a cut in a non-bypassable route. The heart is a part whose work delivery depends on |
| The heart counted twice | As the pump (41), and as a vessel bed among "brain and heart highest" (42) | Counted once, as the support part |
| The anaesthetist's fluids listed as a store | "(iii) fluids and blood given by the anaesthetist (outside supply, recorded as case totals)", under "Stores, in order" (34) | Outside input |
| Volume, pressure × flow and pressure used as one currency | "Currency: circulating blood volume and its delivery (pressure × flow)" (27); "Resource: effective circulating volume" (30); "X = mean arterial pressure" (37) | Resource: oxygen, as the brain draws it (corrected 9 October 2026). Blood volume: the store. Pressure: the indicator |
| The top never named | "brain and heart highest" (42); no top is stated | The top is the brain |
| G18 paired two dials of one part with the indicator | "Shared dependency: heart rate, stroke volume and pressure all depend on the circulating volume (G18, exploratory)." (55) | See Section 2 |
| The test read only the indicator | "No units are tracked here. The test reads only the record." (43) | Mean arterial pressure is an indicator, not the protected flow |
| The anaesthetist inside the boundary, as part of the governor | "One surgical patient ... plus the anaesthetist, treated as one system" (15); "Boundary: the patient's circulation plus the anaesthetist" (26) | The anaesthetist is an outside loop. The boundary is the patient |
| A store that tapers, possibly ending in a switch, committed | "store (i) tapers as it empties" (47); option A committed (60) | Not committed; logged as the first candidate for revision, as the pre-registration named it. Which release profile held is untested (Section 1) |

**Weight of the slips.** They are mapping faults, named under CANON 6. The verdicts stand, and the frozen file is not edited.

## 4. Bias ledger (S9.4) for this mapping

| Choice | Score (1 forced, 5 open) | Note |
|---|---|---|
| Boundary | 2 | The patient; treatment is outside input |
| Part classification | 2 | Heart (support), vessel-wall muscle, beds (ordinary) |
| Resource | 2 | Oxygen, as the brain draws it, declared (corrected 9 October 2026); blood is its carrier; oxygen content per unit of blood fixed |
| Rank | 2 | Documented constriction under sympathetic drive (to be sourced bed by bed) |
| Reference state | 3 | The brain's resting need, fixed in advance (to be sourced) |
| Prediction | 2 | G27 as stated |

**No coin-flips remain.** James resolved them on 8 October 2026: the top is the brain alone, and the currency is oxygenated blood flow.

## 5. Sources

**Already cited in the paper, and checked:**
- Evans et al. 2001;
- Scully et al. 2016;
- Bergauer et al. 2026;
- Sadid et al. 2026 (preprint);
- Bondar et al. 1995 (checked 8 October 2026; abstract read);
- Chapleau, Hajduczok and Abboud 1991 (the arterial baroreflex; abstract read, 9 October 2026; to be verified externally).

**To be sourced** (marked in the text above):
- the governor's sensed levels;
- the brain's resting need;
- the bed-by-bed constriction order;
- the carbon dioxide candidate.

None of these goes into the paper until it is checked by the method in `papers/pam-model/Citation check.md`.
