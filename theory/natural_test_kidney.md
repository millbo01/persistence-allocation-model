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
