# PAM: register of theory-building probes (started 7 October 2026)

**What this is:** cases run informally (mostly in James's chats with GPT) to see whether the model's architecture makes sense of a known phenomenon.

**What it is not: evidence.**
- The outcomes were known before the mapping, so none counts as support (v0.18, Section 11).
- They are logged because they shaped the model, or because they point to tests.

**Two biases, stated (James, 7 October 2026):**
1. **The same model picks the case, maps it, predicts and searches.** Real tests need isolated models in sequence.
2. **Cases are chosen because they look promising.**

**Probes carry no evidential weight.** They serve only to debug the ontology and to check that the model lands near respectable explanations.

**The bias ledger** (adopted 7 October 2026). Before looking anything up, score the interpretive freedom of each mapping choice from 1 (forced) to 5 (open):
- boundary;
- part classification;
- resource;
- rank;
- reference state;
- prediction.

Mark coin-flip choices as ambiguous before the search; they cannot be resolved afterwards in the model's favour.

**What James wants from them** (7 October 2026): *convergence with current scientific thinking, not new discoveries.* "I want to validate the model, not discover new scientific findings."

| No. | Case | What the model said | Existing science it met | What it changed or pointed to | Source |
|---|---|---|---|---|---|
| P1 | Semelparous salmon (and Antechinus, monocarpic plants) | Individual persistence stops being the protected constraint after the reproductive switch | Endocrine-programmed reproductive death | **Scope:** terminal reproductive programmes are out of scope (v0.18, Section 2) | raw/2026-10-06_chatgpt_PAM-theory-chat.txt |
| P2 | Cancer | A tumour is not a dumb part. It closes its own loop around acquiring resources | Tumour metabolism, angiogenesis, cachexia | **The part-or-system criterion;** capture (extension layer, Section 15) | same |
| P3 | Pregnancy | The placenta is a temporary maternal part; the fetus is a system downstream | Placental nutrient transport, maternal and fetal regulation | **No bargaining mechanism needed** (F4) | same, part 2 |
| P4 | Power grid | Governance sets connections and capacity; physics sets the flow | Underfrequency load shedding; cascading failure | **The governor regulates access** (F1); severance and cascades (F3, G24) | same |
| P5 | Skin circulation in heat and haemorrhage | Not a rank test: the skin is dumb, and flow is moved | Thermoregulatory and haemorrhagic vasomotor control | **What a valid dynamic-priority test needs** (F2) | same, part 2 |
| P6 | Mammalian hibernation: periodic arousals | Torpor cuts access, renewal included, so residue builds while the record holds. Arousal is the governor restoring access before the first renewal bottleneck reaches its viability limit. With several such debts, the binding one is the minimum (the law of the minimum) | **The hourglass hypothesis:** an imbalance accumulates in torpor to a threshold, and is restored in arousal (a two-process model reproduces the cycles) | **Convergence.** A discriminating experiment follows: slow the deterioration of the limiting process, and bouts lengthen until the next bottleneck binds. **Mapping note:** torpor is not economising in the maths (which cuts work access only). It is a governor setting that also cuts renewal access, which needs no new mechanism ($g$ depends on sensed state) | raw/2026-10-07_chatgpt_PAM-probes-hibernation-ants.md |
| P7 | Inactive workers in ant colonies (ledger after the fact: part classification about 50/50) | Inactive workers are switched-off units. Loss or a rise in requirement recruits them before the function fails, through local thresholds with no central switch | **The reserve-labour hypothesis** (*Temnothorax*: removing active workers recruits inactive ones; task-specific reserve pools). Contested: some experiments fail to recruit, and stochastic task dynamics can produce inactivity | **Convergence, with the contest kept.** The model claims only that, *if* inactive units are recoverable capacity, a large enough loss recruits them before the function fails. **Derived response order** (results R14): spare throughput in active units, then reactivation, then loss of output | same |

**Unverified leads from P6 and P7** (to check before citing): the hourglass and two-process hibernation models; the *Temnothorax rugatulus* removal experiments (2017) and the later dynamic task-allocation study; the "lazy workers" response-threshold model.

## R14 (derived from the maths, added to the results)

**The response to rising requirement on a part with switched-off units** (maths, Sections 4 and 5):
1. **Within active capacity:** work rises with no change of state ($w=\min(\hat c,\dots)$, with $\hat c>w$).
2. **Beyond active capacity:** switched-off units are reactivated, at most $\theta_{\text{re}}K$ per step, each at the reactivation cost.
3. **If requirement rises faster than reactivation, or exceeds total capacity:** output falls, and load passes on.

This is the order the ant probe pointed to, and it follows from the existing rules. **It is a candidate prediction** (a recruitment sequence) for any system where active, switched-off and lost units can be counted.

## Further probes (7 October 2026)

| No. | Case | What the model said | Existing science it met | What it showed | Ledger |
|---|---|---|---|---|---|
| P8 | Drought in woody plants | Peripheral capacity is given up before the protected core | **The hydraulic vulnerability segmentation hypothesis** (leaves fail before stems; stem, then petiole, then leaflet in compound-leaved trees; treated as a drought strategy across 130 species) | **A negative result as well:** a 2025 study of 12 Australian species found segmentation absent or reversed, and reviews say it is not universal. **Lesson:** the prediction was too permissive (closing stomata, turgor loss, shedding and segmentation would all "fit"). A test must fix in advance which threshold comes first, in which tissue | Prediction freedom high |
| P9 | Dehnel's phenomenon in shrews | Reversible economising to lower the cost of upkeep ("when income cannot rise, make the system cheaper to keep alive") | Winter shrinkage of the body and organs, the brain included, with spring regrowth. Measurements show lower absolute energy use. The brain shrinks by cell shrinkage with neuron numbers stable. The change is seasonal and anticipatory | **Convergence** on reversible economising and on scaling down while keeping the route back. **The ranking of tissues was not predicted,** so it is not scored | Boundary 1, resource 2, part 1, **rank 5**, reference 2 to 3, prediction 2 |

**Unverified leads from P8 and P9:** the 2025 Australian segmentation study; the 130-species study (2024); the shrew metabolic measurements; the 2025 brain cell-shrinkage report.

## Probes from the Perplexity report (7 October 2026)

**Source:** raw/2026-10-07_perplexity_PAM-post-v018-report.md. **No ledger was scored before the search,** so bias cannot be assessed; shorebird phenotypic flexibility and muscle repair were already known (theory/deterioration_threshold_scan.md; natural test 8). Citations in the report are leads, not checked.

| No. | Case | What the model said | Existing science it met | What it showed |
|---|---|---|---|---|
| P10 | Cold-stressed guinea pigs | Requirement-limited load; early reproductive output held, later dependent stages degraded | Mixed: one study found no effect on reproductive output; another found coping by reduced activity; a review reported delayed weaning and slower offspring growth | **Mapping point:** a record can be a sequential pathway (birth, lactation, weaning); the early stage can hold while load appears downstream. Non-diagnostic for priority |
| P11 | Migratory shorebirds (refuelling against flight preparation) | Phase-specific access and reversible remodelling under governor modes, not rank reversal | Phenotypic flexibility: digestive organs grow while refuelling and shrink before departure; heart and flight muscle grow | **Sharpens v0.18 Section 4, item 3:** a change of mode changes allocation without changing rank; a dynamic-rank test also needs the mode controlled. Non-diagnostic for dynamic priority |
| P12 | Skeletal-muscle repair | Repair as a network that competes for access; strict rank under shortage (G23b) | Repair depends on satellite cells plus shared immune, vascular and stromal support; priming after one injury; impaired repair and fibrosis after repeated injury | **Repair capacity is itself a state** (primed, depleted, fibrotic, cut off). G23b remains untested: it needs simultaneous matched injuries sharing a limiting repair resource |

**Applied (James, 7 October 2026):** the three wording edits from P10 to P12 entered v0.18 as a dated amendment (sequential records; mode held constant; repair capacity as a state). Remodelling against deterioration is folded into the v0.19 item on economising as a magnitude. Evidence labels (modelling choice, derived prediction, simulation result, natural-system observation, direct test, compatible but non-diagnostic, unknown, contradicted, fitted) are adopted for this register and the paper.
