# Natural test 3: loss of kidney filtering units (nephrons). Surface-level check (5 October 2026)

**Status:** theorising (phase 3). James asked for a surface-level look for patterns while the model is built out; hard testing comes later. The predictions below were written and committed before searching.

## Mapping to the tier-queue core

- **Working parts:** about a million nephrons, a wide base of parallel units with large spare capacity (redundancy).
- **Output:** total glomerular filtration rate (GFR).
- **Record:** serum creatinine, the routinely measured figure.
- **State signals:** single-nephron hyperfiltration and enlargement, loss of renal functional reserve (the rise in GFR after a protein load), and albumin in the urine.
- **Load:** the body's filtration demand, which is roughly constant.

## Predictions (committed before searching)

| No. | Prediction | Contamination |
|---|---|---|
| K1 | Creatinine (the record) stays in the normal range through large nephron loss, then rises steeply (a flat record, then the break) | **Known.** "Creatinine-blind range" appears in natural_systems_check.md (3 October) |
| K2 | State signals move first: renal reserve is lost and remaining nephrons hyperfilter before creatinine rises | Partly known |
| K3 | Compounding: hyperfiltering survivors are damaged by the extra load, so loss continues without a new insult. This is the vacancy cascade in a natural system | Known in outline (Brenner hyperfiltration hypothesis) |
| K4 | A low starting nephron number (a compromised start: low birth weight, preterm birth) leads to earlier and faster decline | Known in outline |
| K5 | After acute kidney injury, creatinine returns to baseline while reserve and capacity do not. Later chronic disease is more likely: the record recovers, the state does not (the hysteresis caused by opacity) | Not known in detail |
| K6 | Removing half the nephrons (kidney donation) gives a modest creatinine rise, hypertrophy of the remaining kidney, and GFR settling above 50% of the pre-donation figure. There is a small long-term cost | Partly known |

## Results (surface level, from search summaries, 5 October 2026)

| Prediction | Finding | Verdict |
|---|---|---|
| K1. Flat record, then a break | Creatinine stays roughly normal until about 50% of nephrons are lost, or until GFR nears 60 ml/min per 1.73 m²; creatinine is not an accurate marker above that GFR. The remaining nephrons hyperfilter, and creatinine rises only "when the reserves of the overworking nephrons are depleted" (PMC5678605; PMC3580707; reachmd summary) | Consistent (known) |
| K2. State signals move first | Renal functional reserve "begins to decline before CKD is clinically diagnosed". Its loss is "an indicator of silent loss of functioning nephron mass", seen "despite the presence of apparently normal kidney function measured by serum creatinine" | Consistent |
| K3. Compounding: the survivors are damaged by their own extra load | Brenner, 5/6 nephrectomy in rats: the remaining nephrons hyperfilter, and the altered haemodynamics lead to glomerular sclerosis, further nephron loss and renal failure (JCI 80818 and related) | Consistent (known in outline). This is the natural counterpart of the vacancy cascade |
| K4. A compromised start leads to earlier decline | Low birth weight goes with low nephron number. Glomerular size is inversely related to nephron number (hypertrophy at the start). Superimposed insults (diabetes, rapid catch-up growth) lead to hyperfiltration, proteinuria and progressive decline | Consistent |
| K5. The record recovers after acute injury; the state does not | After acute kidney injury, creatinine can return to baseline while renal functional reserve does not. Each episode loses nephrons, which the survivors mask by hyperfiltering. Later chronic disease is more likely even after "apparent renal recovery" (18.2% against 15.5% at 1 year in one cohort, as summarised). There are "no tools" in routine use to detect this hidden loss (PMC6837804; PMC7938179; VHA cohort) | Consistent. This is the opacity hysteresis of TQ1, in a natural system |
| K6. Half the nephrons removed | Within 6 weeks of donation, GFR is about 70% of the pre-donation figure, through compensatory hypertrophy. There is a slightly raised lifetime risk of end-stage disease against matched controls (PMC5820146 and related) | Consistent |

**Pattern.** The kidney is the cleanest natural example yet of four things the model predicts:
1. Spare capacity (redundancy) holds the record flat.
2. The state signal (reserve) falls first.
3. Survivors carrying extra load are damaged by it, so the loss compounds.
4. The record recovers after an acute injury while hidden capacity does not.

Weight: surface level only. Every finding is from search summaries, and K1 and K3 were known in advance.
