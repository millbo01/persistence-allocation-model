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

## How to word this in any paper

- **Elements with no outside source:** "Developed independently (dated record in the deposit). Later reading found convergence with [X], which [differs in or adds Y]."
- **Elements built from a source** (refinements A and B, the knee, Bizzozero's classes): cite the source as the basis.
- **Precedents read before an element was formed** (Miller for the hierarchy, Selye for the states, Woods for the hockey stick): cite them as precedents, with the date in the record. Do not claim independence for those elements.
