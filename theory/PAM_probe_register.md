# PAM: register of theory-building probes (started 7 October 2026)

**What this is:** cases run informally (mostly in James's chats with GPT) to see whether the model's architecture makes sense of a known phenomenon.

**What it is not: evidence.**
- The outcomes were known before the mapping, so none counts as support (v0.18, Section 11).
- They are logged because they shaped the model, or because they point to tests.

**What James wants from them** (7 October 2026): *convergence with current scientific thinking, not new discoveries.* "I want to validate the model, not discover new scientific findings."

| No. | Case | What the model said | Existing science it met | What it changed or pointed to | Source |
|---|---|---|---|---|---|
| P1 | Semelparous salmon (and Antechinus, monocarpic plants) | Individual persistence stops being the protected constraint after the reproductive switch | Endocrine-programmed reproductive death | **Scope:** terminal reproductive programmes are out of scope (v0.18, Section 2) | raw/2026-10-06_chatgpt_PAM-theory-chat.txt |
| P2 | Cancer | A tumour is not a dumb part. It closes its own loop around acquiring resources | Tumour metabolism, angiogenesis, cachexia | **The part-or-system criterion;** capture (extension layer, Section 15) | same |
| P3 | Pregnancy | The placenta is a temporary maternal part; the fetus is a system downstream | Placental nutrient transport, maternal and fetal regulation | **No bargaining mechanism needed** (F4) | same, part 2 |
| P4 | Power grid | Governance sets connections and capacity; physics sets the flow | Underfrequency load shedding; cascading failure | **The governor regulates access** (F1); severance and cascades (F3, G24) | same |
| P5 | Skin circulation in heat and haemorrhage | Not a rank test: the skin is dumb, and flow is moved | Thermoregulatory and haemorrhagic vasomotor control | **What a valid dynamic-priority test needs** (F2) | same, part 2 |
| P6 | Mammalian hibernation: periodic arousals | Torpor cuts access, renewal included, so residue builds while the record holds. Arousal is the governor restoring access before the first renewal bottleneck reaches its viability limit. With several such debts, the binding one is the minimum (the law of the minimum) | **The hourglass hypothesis:** an imbalance accumulates in torpor to a threshold, and is restored in arousal (a two-process model reproduces the cycles) | **Convergence.** A discriminating experiment follows: slow the deterioration of the limiting process, and bouts lengthen until the next bottleneck binds. **Mapping note:** torpor is not economising in the maths (which cuts work access only). It is a governor setting that also cuts renewal access, which needs no new mechanism ($g$ depends on sensed state) | raw/2026-10-07_chatgpt_PAM-probes-hibernation-ants.md |
| P7 | Inactive workers in ant colonies | Inactive workers are switched-off units. Loss or a rise in requirement recruits them before the function fails, through local thresholds with no central switch | **The reserve-labour hypothesis** (*Temnothorax*: removing active workers recruits inactive ones; task-specific reserve pools). Contested: some experiments fail to recruit, and stochastic task dynamics can produce inactivity | **Convergence, with the contest kept.** The model claims only that, *if* inactive units are recoverable capacity, a large enough loss recruits them before the function fails. **Derived response order** (results R14): spare throughput in active units, then reactivation, then loss of output | same |

**Unverified leads from P6 and P7** (to check before citing): the hourglass and two-process hibernation models; the *Temnothorax rugatulus* removal experiments (2017) and the later dynamic task-allocation study; the "lazy workers" response-threshold model.

## R14 (derived from the maths, added to the results)

**The response to rising requirement on a part with switched-off units** (maths, Sections 4 and 5):
1. **Within active capacity:** work rises with no change of state ($w=\min(\hat c,\dots)$, with $\hat c>w$).
2. **Beyond active capacity:** switched-off units are reactivated, at most $\theta_{\text{re}}K$ per step, each at the reactivation cost.
3. **If requirement rises faster than reactivation, or exceeds total capacity:** output falls, and load passes on.

This is the order the ant probe pointed to, and it follows from the existing rules. **It is a candidate prediction** (a recruitment sequence) for any system where active, switched-off and lost units can be counted.
