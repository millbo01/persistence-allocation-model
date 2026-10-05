# Natural test 5: plants in drought. Surface-level check (5 October 2026)

**Status:** theorising (phase 3). Mapped with the procedure in TIER_QUEUE_MODEL_v0.1.md, Section 5. The predictions below were committed before searching.

**Contamination, declared.** Claude knows the outlines of:
- plant hydraulics: vulnerability segmentation (leaves embolise before stems), stem embolism thresholds (P50 and P88), and runaway embolism;
- isohydric and anisohydric strategies;
- the general existence of drought legacy effects.

So P2, P3, P5 and P7 can only be "consistent". P1 (the record lag) and P4 (rate independence) carry more weight.

## Mapping

| Step | Plant in drought |
|---|---|
| Boundary and currency | Whole plant; water, with carbon as the second currency |
| Load | Evaporative demand and soil water deficit |
| Record | What an observer routinely watches: canopy greenness and leaf area (field and satellite indices). The plant itself defends leaf water potential (most strongly in isohydric species) |
| Top (protected, fixed capital) | Stem xylem and meristems, which are costly and largely not refillable once embolised |
| Working parts | Leaves (intake for carbon; cheap and replaceable, so lower priority); fine roots (intake for water) |
| Reserves | Stored water (stem and bark capacitance); non-structural carbohydrates |
| Labelled or not | Partly labelled: hydraulic and hormonal signals (root-sourced abscisic acid) carry strain to the leaves |
| Control and switch | Stomatal closure at a set water potential, before hydraulic failure; leaf shedding |
| State signals | Leaf and stem water potential, percentage loss of conductivity, carbohydrate reserves, sap flow |
| Starting stage | Set by previous droughts and carbohydrate reserves |

## Predictions (committed before searching)

| No. | Prediction | Contamination |
|---|---|---|
| P1 (G1) | Canopy greenness and leaf area (the record) hold while water potential, conductivity and reserves fall. Visible dieback lags hydraulic damage | Partly known |
| P2 (G2) | Lower-priority parts are sacrificed first: leaves and petioles embolise and are shed before stem xylem (a hydraulic "fuse"); older leaves before younger | Known |
| P3 (G3) | The break comes at a set depletion: stomata close at a set water potential before failure, and death follows a set percentage loss of stem conductivity, not exhaustion of all water | Known in outline |
| P4 (G3, stock) | The failure threshold (percentage loss of conductivity at death) is the same whether drought comes fast or slow. Speed changes the time to failure, not the threshold | Not known to Claude |
| P5 (G5) | Compounding: embolism raises tension in the remaining vessels, which causes more embolism (runaway) | Known in outline |
| P6 (G4) | A stressed start (previous drought, low reserves) fails sooner or dies more in the next drought | Partly known (legacy effects) |
| P7 (G6, G7) | Recovery needs new xylem (embolised stem vessels are mostly not refilled): fixed capital loss and a scar. Growth and conductivity stay reduced for years after the drought ends, while the canopy may look recovered | Partly known |
| P8 (strategy) | Two strategies map onto the model's regimes. Isohydric plants shed demand early (they close stomata), keep their water potential and pay in carbon. Anisohydric plants keep their output and let the strain run into the xylem, which risks hydraulic failure | Known (the strategies). The mapping to the model is new |

## Results (surface level, from search summaries, 5 October 2026)

| Prediction | Finding | Verdict |
|---|---|---|
| P1. The record lags hydraulic damage | "Foliar color changes lagged behind hydraulic failure", best predicting when trees "had been dead for some time, rather than when they were dying" (Hammond et al. 2019, New Phytologist, PMC6771894). In eucalypt forests after extreme drought, healthy-looking trees showed 25 to 31% native embolism; partial dieback went with 72 to 78%, and fully dead canopies with 78 to 100% (PMC9751299) | **Consistent, and informative:** the record lag was not known to Claude. A green canopy is a record that sees compromise, not stress, and sees it late |
| P2. Lower-priority parts are sacrificed first | The vulnerability segmentation hypothesis: distal, low-investment organs (leaves, fine roots) embolise first and act as "hydraulic fuses", protecting perennial, carbon-rich organs. A multi-ecosystem test exists ("Out on a limb"); its result was not read | Consistent (known). Not every species shows it; to check |
| P3. The break comes at a set depletion | A lethal threshold at about 80% loss of conductivity, beyond which trees are more likely to die than survive (Hammond 2019). The proposed thresholds are about 50% for conifers and 88% for angiosperms, varying by species | Consistent (known in outline) |
| P4. The threshold does not depend on drought speed | "Trees killed by drought stress showed identical loss of xylem conductivity but different degrees of carbon depletion depending on the duration of drought exposure" (PMC5774510, as summarised) | **Consistent, and informative:** the same rate-independence as the sheep blood-loss result. Duration changed the carbon reserve, not the hydraulic threshold |
| P5. Compounding (runaway embolism) | In adult Norway spruce, conductivity losses in the middle range (20 to 99%) were hardly seen in the field: "the tree hydraulic system collapsed in a very short time" once cavitation began (Arend et al. 2021, PNAS) | Consistent. It also shows a steep break: very few trees were caught mid-collapse |
| P6. A stressed start fails sooner | Growth stayed low and recovery incomplete for 1 to 4 years after severe drought, most in dry sites and species with low safety margins (Anderegg et al.). Negative legacies were more common after repeated droughts. Heavily defoliated pines formed 60% of the tracheids of undamaged trees and were more prone to die. Drought is most damaging when the return interval is shorter than recovery time. **Non-conforming finding:** "drought legacy in mature spruce alleviates physiological stress" during a later drought (SLU; title and summary only) | Mostly consistent, with one finding logged against it (below) |
| P7. Recovery needs new xylem; growth and conductivity stay reduced while the canopy can look recovered | Legacy growth reductions for 1 to 5 years; canopies can resprout after dieback (PMC9751299) | Consistent (partly known) |
| P8. Isohydric and anisohydric strategies as the coupled and opaque regimes | Not searched in this pass | Not tested |

## Non-conforming finding (logged as found; James's rule)

In mature spruce, an earlier drought reduced physiological stress in a later one. The model's G4 says a stressed start should fare worse.

**Named place to check (theorising):** the earlier drought may have permanently cut leaf area. A scar that sheds demand means less transpiration load on the same xylem in the next drought. If so, this is the scar rule working as "more resistance" (shed demand), not a failure of G4. **To check against the paper:** leaf area or sapwood-to-leaf ratio before and after the first drought. If leaf area did not fall, the explanation is struck and the finding stands against G4.

## What plants add

- **A second rate-independent threshold.** Sheep blood loss and tree hydraulics both break at the same depletion whatever the speed. The buffer behaves as a stock in two kingdoms.
- **The clearest record lag so far.** Canopy colour reports death after it has happened.
- **Priority by replaceability is built into the anatomy.** Cheap, renewable organs are made more vulnerable on purpose, to protect fixed capital (hydraulic fuses).
- **A possible refinement:** a scar can lower future demand (less leaf area) as well as lowering capacity. That may make a previously stressed system more tolerant, not less. Whether a scar raises or lowers future vulnerability depends on whether it cuts demand more than capacity.

Weight: surface level, from search summaries; P2, P3 and P5 were known in advance.
