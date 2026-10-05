# Natural test 6: fetal growth restriction (FGR), testing v0.2. Surface level (5 October 2026)

**Status:** theorising (phase 3). The predictions below were committed before searching.

**Scope.** theory/fgr_mapping.md (3 October) already mapped FGR and checked the order and timing of the Doppler and heart-rate changes (G1 to G3), so that is contaminated and not repeated here. This test targets what v0.2 adds:
- the acute-chronic flip;
- the four recovery outcomes (growth, re-tuning, scar, loss);
- the cost of re-tuning when conditions change;
- refinement A (the top is protected only partly).

**Contamination, declared.** Claude knows in outline:
- the developmental origins of adult disease (Barker; the thrifty phenotype);
- the predictive adaptive response (Gluckman and Hanson);
- that nephron number is lower after FGR;
- catch-up fat after early growth restriction (Dulloo);
- that brain sparing does not fully protect the brain.

FG3, FG4 and FG6 can only be "consistent". FG1 and FG2 carry more weight. FG5 is a test **between two rules** of the model.

## Mapping (summary; full mapping in fgr_mapping.md)

- **Top:** the brain, protected by redistribution (brain sparing), and the heart.
- **Lower priority:** kidney, gut, liver, body growth.
- **Load:** reduced oxygen and nutrient supply from the placenta.
- **Record:** the heart-rate trace and biophysical profile.
- **State signals:** Doppler indices and growth velocity.
- **Fixed capital:** nephrons (formation ends late in gestation) and neurons.

## Predictions (committed before searching)

| No. | Prediction | Model source | Contamination |
|---|---|---|---|
| FG1 | **Acute against chronic.** Acute hypoxia in a previously healthy fetus brings a redistribution that reverses fully when it ends. Chronic placental insufficiency brings lasting structural change (heart, brain, kidney, body composition) | v0.2 acute-chronic flip | Partly known |
| FG2 | **Re-tuning and its signal cost.** Fetuses that have had chronic hypoxia respond differently to a later acute hypoxia. (a) Their fast protective reflexes are **blunted**, because chronic signals lose gain. (b) Slower structural changes (for example more oxygen-carrying capacity) raise tolerance to the same threat | v0.1 chronic signals lose gain; v0.2 re-tuning | Not known to Claude in detail |
| FG3 | **Loss of fixed capital.** Nephron number is permanently lower after FGR, with later raised blood pressure and kidney disease (as in kidney test K4) | G7 | Known in outline |
| FG4 | **The cost of re-tuning.** A fetus tuned to scarcity, then given plentiful nutrition after birth (rapid catch-up), carries a higher risk of adult metabolic and cardiovascular disease than one whose conditions stayed matched | G9 | Known (Barker; Gluckman and Hanson) |
| FG5 | **Recovery order after birth: a test between two rules.** Rule v0.1 ("reserves last") predicts lean tissue and organs recover before fat. Rule v0.2 (re-tuning: enlarge the reserve after scarcity) predicts fat recovers first and overshoots. Both are written down; the evidence decides which applies | v0.1 against v0.2 | Claude knows catch-up fat in outline, which favours v0.2. Declared |
| FG6 | **The top is protected only partly.** Even with head growth spared, there are neurodevelopmental deficits | Refinement A | Known (in fgr_mapping.md) |
| FG7 | **Starting state.** A fetus already under chronic strain tolerates the acute hypoxia of labour worse | G4 | Partly known |

## Results (surface level, from search summaries, 5 October 2026)

| Prediction | Finding | Verdict |
|---|---|---|
| FG1. Acute against chronic | Repeated acute hypoxaemia in fetal sheep (arterial oxygen about 13 mmHg for 1 hour a day for 14 days, recovering between episodes) "does not affect cardiovascular development or growth": there was no difference in heart rate, blood pressure, baroreflexes or chemoreflexes, femoral flow or growth. **Only kidney weight was reduced** (Steyn and Hanson 1998, PMC2231184). Longer chronic hypoxia (21 days or more) produced hypertension in other studies, as discussed there | **Consistent, and informative:** not known to Claude. Acute load with recovery left no mark on the protected systems. Even so, the lowest-priority organ (kidney) paid |
| FG2. Re-tuning and its signal cost | "The cardiovascular responses to acute hypoxia are blunted in the chronically hypoxic fetus." The authors read this as "a change in control strategy" towards "compensatory mechanisms that are more cost-effective in terms of oxygen uptake" (Giussani group: brain-sparing review, PMC4721497; Andean altiplano fetal sheep, Herrera et al. 2016) | **(a) Consistent:** the fast reflexes lose gain. **(b) Consistent as the authors interpret it:** re-tuning to a cheaper strategy. Whether tolerance to the same threat actually rose was not read |
| FG3. Loss of fixed capital | Nephron formation ends by about 32 to 36 weeks of gestation, with no new nephrons afterwards. After hypoxic insult, nephron number stays reduced into postnatal life, "suggesting that the effects of hypoxia on the developing kidney are permanent". Growth restriction leaves a permanent nephron deficit in the rat (PMC3434386 and related) | Consistent (known in outline). Links to kidney test K4 |
| FG4. The cost of re-tuning | Not re-searched: developmental origins of adult disease and the predictive adaptive response are known to Claude in outline | Consistent (known), not re-checked |
| FG5. Recovery order after birth (v0.1 against v0.2) | Catch-up growth after growth restriction "favored fat mass accretion over lean mass and linear growth" by 6 to 8 weeks. Severe growth restriction had lower lean mass at similar weight. In early childhood, children born growth-restricted had lower lean mass but no reduction in fat mass (higher percent fat), then more abdominal and central fat (PMC4437590 and related, as summarised) | **v0.2's re-tuning rule fits; v0.1's "reserves last" does not, here.** Contaminated: catch-up fat was known in outline and declared |
| FG6. The top is protected only partly | Brain sparing "fails to fully protect brain development" (fgr_mapping.md sources) | Consistent (known) |
| FG7. Starting state: labour tolerated worse | Fetuses with an abnormal cerebroplacental ratio have more distress in labour requiring emergency caesarean, lower cord pH and more neonatal intensive care. The inability "to tolerate the stress of parturition" suggests "reduced fetoplacental reserve before labour commences" | Consistent |

## What FGR adds: the type of past load may set the recovery order (theorising, for v0.3)

The two recovery results now line up:

| Past load | Recovery order |
|---|---|
| Acute, severe deprivation: total starvation in rats | Protein (working tissue) regained before fat. Reserves last, as in v0.1 |
| Chronic, partial scarcity: food restriction in rats; fetal growth restriction | Fat first, overshooting. The reserve is enlarged, as in v0.2's re-tuning |

**Candidate rule.** After acute deprivation, the system rebuilds what it needs to work and refills reserves last. After chronic scarcity, it re-tunes to expect more scarcity and enlarges its reserve first, at a later cost if conditions are now plentiful (FG4).

This is the acute-chronic flip applied to recovery. It was formed after seeing the evidence, so it must be tested on new cases before it counts. It would explain why catch-up fat and "reserves last" are both found: they follow different kinds of load.

Weight: surface level, from search summaries; FG3, FG4 and FG6 known in advance; FG5 contaminated.
