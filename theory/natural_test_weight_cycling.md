# Natural test 12: weight cycling (results, 5 October 2026)

**Status:** theorising (phase 3); surface level. Predictions WC1 to WC7 were committed before any source was opened (theory/natural_test_weight_cycling_predictions.md, commit ae7d8a2). Model version v0.9.

**Sources** (web search summaries and one full text; controlled designs only, per James's rule):
- S1. Brownell, Greenwood, Stellar and Shrager 1986, Physiology and Behavior: obese male rats, two cycles of restriction and refeeding, against obese and chow controls (same animals followed).
- S2. "Effects of weight cycling in female rats" (PubMed 2623063): female rats, two cycles.
- S3. Mouse weight-cycling experiments (summaries; Leiden, TUM, FASEB J 2024 on cycling in diet-induced obese mice, J Transl Med 2025): cycles of high-fat and normal diet, same mice followed.
- S4. A rodent study summarised as finding no adverse effect of cycling (experts.mcmaster.ca record; details not read).
- S5. Dulloo and colleagues: semistarvation and refeeding in rats (catch-up fat; review PDFs). Rat experiments only; the human work in this line draws on the Minnesota experiment and is not used.
- S6. Leibel, Rosenbaum and Hirsch 1995: metabolic-ward study, the same people held at usual weight, 10% below and 10% above.
- S7. Seimon et al. 2016, PLoS ONE (full text read): obese mice, continuous against intermittent moderate restriction for 12 weeks, then 3 weeks of refeeding; the same mice followed.
- **Excluded under James's rule:** Rosenbaum et al. 2008 (persistence of reduced energy expenditure more than a year after weight loss). It compares different people at usual weight, recent loss and sustained loss, rather than following the same people. Logged as found; not counted.

## Results

| Prediction | Finding | Verdict |
|---|---|---|
| WC1. Cycling leaves a larger reserve than stable controls | Cycled rats had about four times the food efficiency of obese controls of the same weight at the end (S1). Mice that had cycled gained more weight than continuously high-fat-fed mice over the same feeding period, even after returning to baseline weight (S3). One rodent study found no adverse effect, and lower body fat in cyclers (S4) | **Partly consistent.** The evidence is about faster gain and efficiency rather than reserve size at a fixed time; one null result |
| WC2. Slower loss in later cycles | Second-cycle loss at half the rate (male rats, S1; known in advance). Time to lose weight not affected by cycling (female rats, S2) | **Partly consistent;** differs by sex |
| WC3. Faster regain, fat before lean, in later cycles | Second-cycle regain about three times faster (S1); higher food efficiency in the second gain (S2); enhanced gain at each high-fat phase (S3); fat recovered ahead of lean tissue on refeeding (S5) | **Consistent** (partly known in advance) |
| WC4. Fat first with overshoot after restriction, more after chronic than acute | Catch-up fat after semistarvation in rats, sustained by suppressed thermogenesis (S5) | **Consistent** for chronic restriction; the chronic against acute comparison was not found |
| WC5. Energy expenditure falls beyond the loss of mass, persists after refeeding, then fades | In the same people, energy expenditure fell more than mass and composition predicted at lower weight (S6; known). Suppressed thermogenesis persisted into refeeding in rats (S5). Fading not found in an admissible source; the one study of persistence (more than a year) is excluded by design | **Partly consistent;** fading not found |
| WC6. At equal total restriction, one deep restriction leaves a larger lasting reserve than several shallow ones | Not tested as specified. Continuous and intermittent restriction left the same fat regain over 3 weeks of refeeding (S7) | **Not found** |
| WC7. Effects fade within a few cycle lengths after cycling stops | Not found | **Not found** |

**Logged as found against the model:** the female-rat result (no slower loss in the second cycle, S2) and the rodent study with no adverse effect of cycling (S4). Neither has been read beyond summaries; their weight is low until read.

## Found but not predicted

1. **Breaks during restriction change the response.** Mice on intermittent moderate restriction (5 to 6 days restricted, 1 to 3 days free) lost more weight per unit of energy deficit than mice on continuous restriction (S7), and the MATADOR trial in men is framed around the same idea (title known; not read). In model terms: continuous restriction is one long (chronic) episode; breaks keep each episode short. If the demand cut (suppressed thermogenesis) builds with episode length, breaks would limit it. That is the acute-chronic flip applied to the demand cut, and it links to the open episode-length question (TQ8 C6), where the engine could not reproduce an episode-length effect on part protection. **Theorising, not tested:** the demand cut grows with the length of the episode and a break resets the episode clock.
2. **Intake re-tunes too.** Cycled mice ate more, especially in the first hours after the high-fat diet returned (S3). The model's intake is "rebuilt first when supply returns" (the gut flip); this is the behavioural side of the same priority.
3. **A memory below the model's level.** One mouse study attributes faster regain to gut microbial changes that persist after weight loss (S3). A mechanism for the reserve's memory, not the model's to choose.

## Weight

Surface level; mostly summaries; WC2, WC3 and WC5 known in outline beforehand; mostly rodents; sex differences unexamined in the model. Layer 2 throughout (allocation and re-tuning, not finite-stock dynamics).

## For James

- The core of G15 (repeated episodes leave the system quicker to regain and more efficient) is consistent, with two weak results against.
- The clearest candidate for shaping the model is the unpredicted one: **breaks within a long restriction appear to limit the economising response.** If adopted, the demand cut would build with episode length and reset at breaks, which would also give the episode-length term (τ) a job it does not yet have in the engine.
