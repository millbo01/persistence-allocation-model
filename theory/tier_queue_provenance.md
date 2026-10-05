# Tier-queue model: provenance log (5 October 2026)

**Purpose (James, 5 October 2026).** If later reading finds work that resembles the model, the record must show what was built independently and what was built from sources. Independent convergence is stated as such ("developed independently; later found to converge with X, which differs in Y"). Elements that were built from a source cite that source as their basis.

**Evidence.** Git commit hashes and times in this repository (public deposit and private history). The prior Perplexity thread is James's own earlier work, stored at raw/2026-10-05_perplexity_scale-feedback-structural-load-thread.md. Its dates are not in the export, but it predates this repository's paper one restructure.

## Sources read before the model existed (from 3 to 5 October 2026)

| Source | Read on | Where recorded |
|---|---|---|
| Woods 2018 (graceful extensibility: saturation, decompensation) | 3 Oct | theory/woods2018_reading.md |
| Doyle and Csete 2011; Kitano 2007; Csete and Doyle 2002 (conservation of fragility) | 3 Oct | theory/doyle_kitano_reading.md |
| Miller 1970 (full text), Miller 1978 and 1960 (secondary), Selye (secondary), Rasmussen 1997 and Cook and Rasmussen 2005 (abstracts) | 4 Oct, 19:38 | d1ccfaf; theory/miller_selye_cook_reading.md |
| Natural fasting, blood loss, iron, plant, colony, sleep and hypothermia examples (search summaries, including Cherel and Groscolas's fasting phases and their threshold hypothesis) | 4 Oct evening, during the discussion with James | conserved_quantity_attempt.md, Section 7 |
| James's vacancy debt method (James's own, published earlier) | 5 Oct, 08:11 | ffba866 |

## Element by element

| Element | First committed | Origin | Built from a prior source? |
|---|---|---|---|
| Conservation as a flow ledger (generated = resolved + exported + backlog + abandoned) | Prior thread; paper one P1 | James's earlier work, with Claude's flow correction imported into that thread | No outside source. Precedents to cite as convergent: Bode and waterbed conservation (Csete and Doyle), compartmental systems |
| Survival hierarchy; subordinates buffer superiors; acute against chronic; a recovery window | 4c63b20 (4 Oct, 20:57) | James, in discussion | Partly. Miller's "hierarchy of values" and recruitment of components had been read 80 minutes earlier (d1ccfaf). James's tree and buffering framing are his own; Miller is a precedent to cite |
| Two directions (top-down and bottom-up); recovery top first and bottom last; late collapse of priority | 9f19a05 (4 Oct, 21:10) | James | No |
| Roles (reserve, intake, working); priority falls with renewability and redundancy; point of no return at parts that cannot be rebuilt | c372d7d (4 Oct, 22:48) | James and Claude, drawing on natural examples looked up that evening | The renewal classes (labile, stable, permanent) are textbook pathology (Bizzozero 1894). The priority rule built from them is the new combination |
| Signals mistranslated, not missing; chronic signals lose gain; identity as an institution's fixed capital; overhead proxy | 131a005 (5 Oct, 06:33) | James, in this session and in the prior thread ("downregulated" signals, "the Queen", S_o) | No outside source |
| The tier-queue join (parts as servers with reserves; export down the tree; the hockey stick as buffer exhaustion) | b5495f7 (5 Oct, 06:48) | Claude, joining James's queue work (prior thread) with the tier model | Partly convergent with Woods 2018 (saturation, decompensation), read 3 Oct. To be stated and differentiated in the novelty pass |
| Path of least resistance; unlabelled load cannot be refused and sinks to the lowest tier | water model 4c63b20; rule 4781785 (5 Oct, 07:28) | James | No. P2 (unlabelled export) is from James's paper one |
| Three states (optimal, stressed but coping, compromised); "the record sees compromise, not stress" | b995525 (5 Oct, 07:15) | James (states); Claude (the record line) | Selye's alarm, resistance and exhaustion (read 4 Oct, secondary) is a precedent for the states, to cite |
| Only working parts are compromised; compromise leaves a mark | 4781785 (07:28) | James | No |
| Wide base, turnover, vacancy cascade | TQ2 to TQ4; ffba866 | James's vacancy debt method and Claude's simulations | James's own prior method |
| Overload felt against current capacity (compounding) | 4f013e9 (08:28) | James | No |
| Starting state as an input; stage read from state signals | 3a44916 (08:41) | James | No |
| Refinement A, shared upstream supply | b8dbd1a (08:52) | Built after natural test 1, from blood loss findings (brain flow falling with cardiac output) | **Yes: built from literature** (LBNP studies) |
| Refinement B, active threshold switch | b8dbd1a | Built after natural test 1 (sympathetic withdrawal at about 30% loss; Schadt and Ludbrook 1991 as cited) | **Yes: built from literature** |
| Reserve release knee | b8dbd1a | Built for the fasting test | **Yes: this is Cherel and Groscolas's own hypothesis**, read 4 Oct |

## Matched after the build (convergence, not basis)

These were found after the elements they match were committed:
- the sheep rate-independence result;
- the heat-stress baseline effect;
- the fasting threshold adiposity and the lengthening of phase II;
- the kidney's creatinine-blind range, loss of renal reserve, and recovery after acute injury;
- honeybee precocious foraging and the definition of collapse disorder.

They are logged in the natural test files with the date each prediction was committed. Contamination is declared there: several were known to Claude in outline before the prediction.

## Raised after the build, not yet read (5 October 2026)

Named by another Claude chat reviewing v0.5 (relayed by James, 5 October 2026), after v0.5 was committed (53b240f). Logged for the novelty stage; not read and not acted on now (novelty deferred until after the stress tests).
- **Kleinrock's conservation law for priority queues (1965).** In a work-conserving queue, priority cannot reduce total weighted waiting time across classes; it only moves delay between them. A candidate formal anchor for the principle, in queueing theory. To check at the novelty stage how far it carries: it conserves weighted delay in a single queue, not load across a nested hierarchy with damage and recovery.
- **Dynamic energy budget theory (Kooijman) and the Add-my-Pet collection.** Organism-level mass and energy balance, reserves, maintenance priority and starvation rules. The closest formal theory at the organism level to check against; Add-my-Pet may also be an independent source of parameters (reserve capacity, maintenance rates).
- Penguin fasting thresholds and ischaemic preconditioning were also named. Both were already in the natural tests (fasting; re-tuning), so they are not new.

### Second review, 5 October 2026 (another Claude chat, relayed by James after v0.6, 7b71d7b)

Named, not read; logged for the novelty stage. Any element adopted from this review is recorded as **built from it**, not as independent.
- Precedents for downhill routing: Selye; McEwen (allostatic load); Cook ("how complex systems fail": running in degraded mode); Peters (the selfish brain).
- The record rule as actuator saturation (control engineering); integral windup as a rival explanation of overshoot after long deficits.
- The horizon term as convergent with Kirkwood (disposable soma) and Williams (terminal investment); Schaffer and Schaffer (agave: convex returns to reproductive effort).
- Optimal allocation: water-filling and KKT conditions (greedy marginal-value ordering is optimal only under concave, separable objectives).
- Quantum error correction: threshold theorem, Google 2024 below-threshold result, Terhal (decoder backlog), leakage.
- Firms: Dechow and Sloan 1991 (CEO horizon and R&D); savings and loans "gambling for resurrection".
- Cognitive reserve: Stern; Hall et al. 2007; Scarmeas et al. 2006; hippocampal hyperactivation in mild cognitive impairment.
- Critical slowing down: Scheffer et al. 2009; compensatory reserve measurement (US Army); Severson et al. 2019 (battery life before capacity degradation).
- Materials and ground: Kaiser and Felicity effects (acoustic emission); aquifer compaction below the historic low.
- Science and mathematics as institutions: Serra-Garcia and Gneezy 2021; formal verification (Voevodsky).
- Coral re-tuning and its cost; Hughes et al. 2019 (population filtering mimics re-tuning).
- Two layers: finite-stock feedback without goals (stellar main sequence; carbonate-silicate thermostat) against selection or design.

**Adopted in v0.7 (built from this review):** $\tau$ in the spending cost; the optimality condition and its departures (saturation, cliffs, increasing returns; semelparity needs increasing returns); record dynamics as a read-out (G12); tagging by layer; the G9 rule to follow individuals; windup as a rival explanation (open). The fuse term ($s_i$) and the control rule were added by Claude during the build, as consequences of the optimality condition, and confirmed by James (5 October 2026). Held, not adopted at v0.7: the Felicity ratio, two boundaries. **The Felicity read-out was adopted in v0.8** after the muscle check (natural test 11); built from this review (Kaiser and Felicity effects).

**Third review (5 October 2026; raw/2026-10-05_claude-chat_review3_astro-econ.md):** tested v0.7 against astrophysics and economics. Adopted in v0.9: the reserve's memory of the worst episode (from its R13, reworked as peak-referencing with fading) and James's system's-clock rule (James contested "only briefly"). Held: R11 (synchrony), R14 (horizon against budget). Logged only: physical-constant communities, spacecraft, fiscal labelling, monetary policy.

**Contamination check:** the review mentions the US Army compensatory reserve measurement, from the same programme as held-out candidate H1. Nothing beyond what the blood-loss surface test already read (S2) was reported. No other held-out candidate is touched.

### Perplexity review and exploratory applications (5 October 2026; relayed by James)

raw/2026-10-05_perplexity_review_tier-queue.md and raw/2026-10-05_perplexity_random-applications_bears-birds.md. **Built from them in v0.12:** the narrowed control rule (non-bypassable bottleneck); status labels and the fitted label; the engine-assumptions list; the central-claim formulation (combined with the record line and recovery half); structural capacity against deployed throughput (suppression, remodelling); task-relative value and the next-task horizon; reading state signals against the system's own phase reference. **James's own (5 October 2026):** chronic as a state, not a duration ("attrition comes to mind"). The anticipatory-economising candidate is Claude's derivation from the bear application, not adopted.

## How to word this in any paper

- **Elements with no outside source:** "Developed independently (dated record in the deposit). Later reading found convergence with [X], which [differs in or adds Y]."
- **Elements built from a source** (refinements A and B, the knee, Bizzozero's classes): cite the source as the basis.
- **Precedents read before an element was formed** (Miller for the hierarchy, Selye for the states, Woods for the hockey stick): cite them as precedents, with the date in the record. Do not claim independence for those elements.
