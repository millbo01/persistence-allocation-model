# Check 2: formal models of the order of organ loss in starvation and haemorrhage (7 October 2026)

**Status:** phase 3 literature check (no gates). A targeted PubMed search, not a systematic review. Strings and counts are recorded so it can be repeated.

**Question.** Do formal or semi-formal models exist that set the order in which organs lose supply or mass under starvation or haemorrhage, and if so, how is the order set?

**Script:** scripts/check2_search.py (PubMed E-utilities; run 7 October 2026). Outputs: counts.json, records.tsv (1,281 rows; 1,279 unique PMIDs).

## Strings and counts

| Key | Aim | Hits |
|---|---|---|
| Q1 | Starvation or restriction, organ mass, model | 454 |
| Q2 | Haemorrhage or LBNP, regional flow, mathematical model | 502 |
| Q3 | "Chossat" (the classic starvation organ-loss table) | 75 |
| Q4 | Guyton model or HumMod, with haemorrhage or starvation | 77 |
| Q5 | Order or priority, organs or tissues, starvation or tissue loss, model or theory | 173 |

**Revision 1 (logged before screening).** Q4's first form used unindexed phrases ("integrative physiology model", "whole-body physiology model"), which PubMed split into single words: 38,758 hits. Re-run with field-tagged terms ((Guyton[tiab] AND model[tiab]) OR HumMod[tiab] OR "integrative physiological model"[tiab]). retmax was raised from 500 to 1,000 so Q2 (502) was retrieved in full.

## Screening (Claude, all 1,279 titles read)

Most Q1 hits use "model" for an animal model; most Q2 hits are vascular fluid dynamics or perfusion imaging. Q3 returned an unrelated author surname. Candidates kept on title, then read as abstracts:

| PMID | Record | Kind | How the order is set |
|---|---|---|---|
| 32218085 | Barnes et al. 2020, haemorrhage in BioGears, HumMod and Muse | Comparison of formal whole-body simulators | Baroreflex and fluid-balance control; all three reproduce tachycardia and hypotension; differences from human data "much larger than expected" |
| 33120539 | Curcio et al. 2020, Guyton against Zenker model in haemorrhagic shock | Formal | Control loops on resistances and volumes |
| 41676696 | Sadid et al. 2026, closed-loop porcine model, 43 swine, 10 to 30% haemorrhage | Formal, calibrated | "A preferential increase in renal resistance compared to carotid resistance, indicating flow redistribution to vital organs"; venous unstressed volume mobilised |
| 42213715 | Bergauer et al. 2026, sex-dependent LBNP model, 35 adults | Formal, calibrated | "Splanchnic vasoconstriction emerges as the dominant compensatory pathway in both sexes"; lower-limb resistance differs by sex |
| 8002508 | Melchior et al. 1994, LBNP simulation | Formal | Baroreflex modulation of peripheral resistances and heart rate |
| 2010373 | Schlichtig, Kramer and Pinsky 1991, progressive haemorrhage in dogs | Measured plus a semi-formal model | Liver and kidney shares of O2 delivery fell, carcass share rose; without redistribution, whole-body O2 supply dependency would begin earlier, kidney's much later |
| 24921933 | Garcia-Canadilla et al. 2014, fetal circulation model, IUGR | Formal, patient-fitted | Brain sparing from a fall in cerebral resistance against a rise in peripheral-placental resistance |
| 21871834 | Luria et al. 2012, fetal circulation model, FGR | Formal | Cerebral O2 availability depends on cardiac-output distribution; optimum at mildly reduced placental flow |
| 20844258 | Hampton et al. 2010, hibernator circulation model | Formal | Compartments by metabolic activity; not an order-of-loss model |
| 16449298 | Hall 2006, semistarvation and refeeding (Minnesota) | Formal | Fat and lean compartments only; no organ order |
| 40830369 | Falkenhain et al. 2025, CALERIE 2 organ size under caloric restriction | Empirical (MRI) | Adipose and skeletal muscle fell; metabolic adaptation beyond organ-mass prediction |
| 5715208 | Peters and Boyd 1968, organ weights in starvation, thirst and stress | Empirical (no abstract) | Not read |
| 23349289 | Plaçais and Preat 2013, *Science*, Drosophila | Empirical | Under starvation the brain disables costly aversive long-term memory; forcing it restores memory "at the price of a reduced survival" |
| 713541 | Moldawer et al. 1978, protein sparing in hypocaloric feeding | Empirical (no abstract) | Not read |

Known items re-found: the Selfish Brain review (21080380; 15172762).

## Answer

- **Haemorrhage: yes, a large formal tradition.** The Guyton model and its descendants (HumMod; BioGears, Muse), and lumped-parameter closed-loop models with baroreflex control, simulate regional flow redistribution. **The order among beds is not written in as a rule.** It emerges from each bed's resistance, its reflex (sympathetic) gain and autoregulation, and is fitted to data. That is order from access properties, the same class as the plant transport-resistance models (check 1).
- **Fetal brain sparing: yes, formal circulation models,** with the order again set by bed resistances.
- **Starvation, many organs: no formal model of the order of organ loss found here.** Formal models are two-compartment (Hall: fat and lean; Selfish Brain: brain and body). The multi-organ order (Chossat-type tables) is held as data, not as a model.
- **Limits:** PubMed only; one pass of titles by Claude; abstracts only; "not identified is not absent".
