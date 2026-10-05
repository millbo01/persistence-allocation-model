# Patterns across the natural tests so far (5 October 2026)

**Status:** theorising (phase 3). Surface-level patterns while the model is built out (James, 5 October 2026). Hard testing comes later. Details are in natural_test_blood_loss.md, natural_test_fasting.md and natural_test_kidney.md.

| Model feature | Blood loss | Fasting | Kidney |
|---|---|---|---|
| Record held flat while load rises | Blood pressure | Function of the protected organs (glucose not checked) | Creatinine, to about 50% nephron loss |
| State signals move first | Stroke volume, compensatory reserve | Fat mass, nitrogen excretion | Renal functional reserve, hyperfiltration |
| Buffer | Venous volume, constriction of lower-priority beds | Fat | Spare nephrons (redundancy) |
| Buffer behaves as a stock | Yes: same loss at the break across rates (sheep) | Threshold at a fat share, not a duration | Threshold at a share of nephrons lost |
| Break at a set depletion, not exhaustion | About 30% blood loss | About 3 to 9% fat, with 18 to 25% of the initial fat left | About 50% nephrons |
| Active switch at the threshold | Sympathetic withdrawal | Phase III, egg desertion, food search | None found |
| Compounding on survivors | Not examined | Not examined | Hyperfiltration causes sclerosis, which causes more loss |
| Starting state shapes the course | Heat stress: tolerance down about 70% | Initial fat sets phase II; a lean start skips it | Low nephron number leads to earlier decline |
| Record recovers, state does not | Not examined | Restriction and starvation recover in opposite orders (weak) | After acute injury, creatinine returns while reserve does not |
| Lower priority pays first | Skin, gut and muscle, then kidney; brain only partly protected | Fat, then gut and liver, then muscle | Not applicable |

**Recurring shape.** In all three systems, a defended figure is held steady while a buffer is drawn down. State markers show the drawdown and the figure does not. The break comes at a set depletion rather than at exhaustion, often through an active switch. The starting state sets how much room there is.

**Gaps to fill in later tests:**
- compounding in blood loss and fasting;
- an active switch in the kidney;
- recovery order in blood loss;
- F7 (whether energy demand moves the threshold).
