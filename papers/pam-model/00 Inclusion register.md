# Model paper: inclusion register (draft 1, 7 October 2026)

**Purpose:** decide what goes in the paper, where, and at what length, in one place, before the remaining sections are drafted (James, 7 October 2026). Every proposition, prediction, piece of evidence, example, citation and figure gets a tier and a word cost. Sections are then drafted to the register, not to the length of their working files.

**Status:** decided (James, 7 October 2026). The ◆ tiers were settled as listed in Section 6.

## 1. The paper's five jobs

An item earns main-text space by serving one of these; being true or interesting is not enough.

| Job | What the paper must do |
|---|---|
| **J1** | State the model: architecture, reduced form, load and ledgers |
| **J2** | Show it is a general architecture, not one domain |
| **J3** | Back the three components no prior theory carries (unification table): **Pre**, rank fixed beforehand from documented access; **Led**, the conserved load ledger; **Sys**, application outside bodies |
| **J4** | Give predictions that separate it from its neighbours (DEB, Selfish Brain, allostasis, control theory) |
| **J5** | Report the tests honestly, failures included, and state its limits |

## 2. Tiers and scoring

| Tier | Code | Test | Where |
|---|---|---|---|
| Critical | **C** | Removing it breaks a claim, a proof a claim depends on, or a distinguishing prediction | Main text |
| Supporting | **S** | Strengthens a critical item: the strongest precedent, one example | Main text, short |
| Supplementary | **Sup** | Needed to check the work, not to follow the argument (full proofs, secondary results, numerical checks) | Supplement |
| Explanatory | **E** | Kept only if a reader cannot follow without it (one worked example or figure per idea) | Main text, sparingly |
| Nice to have | **N** | Decorates, or duplicates another item | Cut (stays in the working files) |

**Quick scoring:** three questions.
- **Dep:** does another included item depend on it?
- **Nov:** does it fill a unique column (Pre, Led, Sys)?
- **Test:** does it give a prediction someone could test?

Two or more yeses usually means C. Then judge value per word.

**Diversification** is a value rule, not a tier: an extra example counts only if it widens the range. One example from a body, one from an organisation and one from an engineered network shows generality (J2); five from physiology do not.

## 3. Word budget

| Section | Main text (words) | Supplement |
|---|---|---|
| 1. Introduction (the problem; the claim; what is new) | 900 | |
| 2. Prior work and convergence (one strongest precedent per neighbour; the unification table) | 1,200 | Full unification table with all rows |
| 3. The model in formal terms (architecture, reduced form, load, assumptions, critical propositions) | 3,000 | Full proofs; supplementary propositions; numerical checks and code |
| 4. Predictions and how they separate the model from its neighbours | 1,100 | Full G1 to G26 list with status |
| 5. Tests so far (H1, PT1; natural-system convergence in one table) | 1,300 | Natural tests in full; probe register; adjudication records |
| 6. Scope, limits and failures | 700 | Logged non-conforming findings |
| 7. Discussion (what follows; how to map a system; what would refute it) | 900 | Mapping procedure in full; reverse mode |
| **Total** | **≈ 9,100** | |

## 4. The register

### 4.1 Model content (v0.19)

| Item | Jobs | Dep | Nov | Test | Tier | Words | Note |
|---|---|---|---|---|---|---|---|
| Architecture: governor sets access, network makes flow, parts have no demand | J1 | Y | | | **C** | 300 | The frame every result uses |
| Units and their four states | J1 | Y | | Y | **C** | 120 | Needed for P8, P13 |
| The reduced form (phases, order, flow, nothing returned) | J1 | Y | Pre | | **C** | 400 | |
| Rank defined and fixed from documented access | J1, J3 | Y | **Pre** | Y | **C** | 200 | The paper's central methodological claim |
| Stores (proportional release default; full release alternative) | J1 | Y | | Y | **C** | 120 | Needed for P2, P3 |
| Renewal as baseline plus wear | J1 | Y | | | **S** | 50 | One sentence |
| Repair network, governed like any part, strict rank | J1, J3 | Y | | Y | **C** | 150 | Needed for P16 |
| Load, reference allocation, two ledgers | J1, J3 | Y | **Led** | | **C** | 350 | |
| Three origins of load and the access guard | J1 | Y | Led | Y | **C** | 150 | Needed for P1's two regimes |
| Chronic as a backlog | J1 | | | Y | **S** | 80 | |
| Modes and gates (build against consolidate) | J1 | Y | | | **S** | 100 | Needed for the access-limited regime |
| Economising as a magnitude | J1 | | | Y | **Sup** | (40) | One clause in main text |
| Collapse and death by viability | J1, J5 | Y | | Y | **S** | 150 | |
| Recovery by marginal value | J1 | Y | | Y | **S** | 120 | Needed for P14 |
| Scope (viability constraint; terminal reproduction out; no redrawing) | J5 | | | Y | **C** | 250 | Section 6 |
| Mapping procedure (nine steps) | J2, J5 | | Pre | | **S** ◆ | 250 | Main text summary; full in supplement |
| Bias ledger | J5 | | | | **Sup** | | |
| Reverse mode | | | | | **Sup** | | |
| Nested-systems extension, drain against capture | | | Sys | Y | **N** for this paper ◆ | 0 | Out of core claims (v0.19 Section 15). One sentence in Discussion as future work |
| Engine and simulations TQ1 to TQ13b | | | | | **Sup** | | The propositions replace them as evidence of what the model implies |

### 4.2 Propositions (paper numbering)

| Paper | Working | Content | Jobs | Dep | Nov | Test | Tier | Words (main) |
|---|---|---|---|---|---|---|---|---|
| 1 | P1 | Relocation under scarcity; creation by gating | J1, J3, J4 | Y | **Led** | Y | **C** | 220 |
| 2 | P2 | The silence; two thresholds | J1, J4 | Y | | Y | **C** | 150 |
| 3 | P4 | Store left at the break | J4 | | | Y | **S** | 150 |
| 4 | P5 | Warning lead time | J4, J5 | | | Y | **Sup** ◆ | (40) |
| 5 | P3 | Order of loss | J1, J3 | Y | **Pre** | Y | **C** | 120 |
| 6 | P17 | Rank under saturable uptake (adequacy threshold) | J3, J4 | | **Pre** | Y | **C** | 200 |
| 7 | P16 | Conflicting orders: the limit | J5 | | | | **Sup** | (40) |
| 8 | P6 | Rate decides harm; scar threshold | J4 | Y | | Y | **C** | 200 |
| 9 | P7 | Shrinking (DEB import) | J1 | | | | **Sup** | |
| 10 | P11 | Economising loses no units | J4 | | | Y | **Sup** | (30) |
| 11 | P8 | Exhaustion against severance or constriction | J4 | | | Y | **C** | 150 |
| 12 | P13 | Rerouting by physics or choice; steal | J2, J4 | | Sys | Y | **S** | 180 |
| 13 | P15 | Collapse, not death (constructive) | J1, J5 | | | Y | **S** | 120 |
| 14 | P9 | Recovery order; partial refill as critical fractile | J4 | | | Y | **C** | 180 |
| 15 | P12 | The fuse | | | | Y | **Sup** | |
| 16 | P10 | Repair under strict rank | J3, J4 | | (repair) | Y | **C** ◆ | 150 |
| 17 | P14 | Rising requirement | | | | Y | **Sup** | |
| out | P18 | Drain against capture | | | Sys | Y | **N** for this paper | 0 |

**Main text: 8 critical and 3 supporting propositions, about 1,870 words** (inside the 3,000 for Section 3). Proofs of these go in a short appendix; all others, and the numerical checks, go in the supplement.

### 4.3 Predictions (G1 to G26)

| G | Short | Tier | Why |
|---|---|---|---|
| G1 | Record flat while lower parts and stores move | **C** | Core read-out; tested (H1 check, low weight) |
| G2 | Lower ranks lose access first | **C** | Rank in use |
| G3 | Break and the store left (rate) | **S** | Derived; new; untested |
| G4 | Larger store, longer silence | **Sup** | Follows from G1 |
| G5 | Loss compounds down the ranks | **Sup** | |
| G6 | Intake first; record before state | **S** | Natural observation |
| G7 | Fixed capital keeps losses | **Sup** | |
| G8 | Rate decides harm; scar | **C** | Distinguishing (P8) |
| G9 | Re-tuning cost | **N** | Carried from v0.16, unexamined |
| G10 | Recovery crossover | **S** | |
| G12 | Warning before the break | **C** | **Failed at H1 (half weight): must be reported (J5)** |
| G13 | The fuse | **Sup** | |
| G14 | Felicity read-out | **N** | Carried, unexamined |
| G15 | Store memory | **N** | Carried, unexamined |
| G16 | Economising loses no units | **Sup** | |
| G17 | Economising against growth | **N** | Carried, unexamined |
| G18 | Co-movement by shared dependency | **S** ◆ | Distinguishes dependency from rank; untested |
| G19 | Three outcomes distinguishable | **S** | |
| G20 | Severance or constriction diagnostic | **C** | Distinguishing (P11) |
| G21 | Law of the minimum | **Sup** | Known (Liebig) |
| G22 | Intake coasts | **Sup** | Example only |
| G23 | Repair: (a) slows under shortfall; (b) strict rank; (c) pre-positioning | **C** for (b); **S** for (a) | (b) distinguishing; (a) compatible |
| G24 | Cascade by physics or choice | **S** | Cross-domain (J2) |
| G25 | Order from documented access | **C** | **Tested: supported at half weight (PT1); G25-C not supported: both reported** |
| G26 | Partial refill | **S** | Derived; new |

**The N items (G9, G14, G15, G17)** are carried from v0.16 without re-examination. Leave them out of the paper rather than present unexamined claims.

### 4.4 Evidence

| Item | Tier | Note |
|---|---|---|
| **H1** VitalDB, G12: fails at half weight | **C** | J5. Report with both qualifications |
| **PT1** councils: inconclusive (full); G25 supported (half); G25-C not supported (half) | **C** | J2 (outside bodies) and J5 |
| Natural-system convergence: one table across blood loss, fasting, kidney, plants in drought, honeybee | **S** | J2. Labelled "natural-system observation" and "compatible but non-diagnostic", with contamination declared. **Not** presented as tests |
| Each natural test in full (1 to 12) | **Sup** | |
| Theory-building probes (salmon, cancer, pregnancy, grid, skin; P1 to P12) | **Sup** | Never presented as support |
| Logged non-conforming findings (Krieger 1921 equal organ losses; plant segmentation negative result; spruce drought legacy) | **Sup**, with one main-text sentence | J5: their existence is stated; weights given |
| Numerical checks of the propositions | **Sup** | One main-text paragraph |
| Systematic searches (check 1: two searches, deviations D-1 and D-2; check 2) | **Sup** | One main-text sentence in Section 2 |

### 4.5 Examples and cases (illustrations, not tests)

Rule: at most **one example per idea in the main text**, chosen for range across domain types (body, organisation, engineered network) and for having numbers.

| Example | Idea | Domain | Tier | Note |
|---|---|---|---|---|
| Councils: statutory against discretionary lines | Rank from documented access; outside bodies | Organisation | **C** | Also the PT1 evidence |
| Haemorrhage: splanchnic and renal constriction before brain and heart | Order of loss | Body | **S** | |
| Sheep haemorrhage: same loss at the break at a fivefold rate difference | Store behaviour (P3) | Body | **S** | Numbers; reads on the release profile |
| Growth signalling holding autophagy shut while nutrients are present | Access-limited load (P1 regime 2) | Body (cell) | **E** | The one clear example of gated load |
| Intensive insulin after stroke (infarct growth) | Relocation (P1 regime 1) | Body | **S** ◆ | **Only after Rosso et al. 2012 is read in the original** |
| Hypertension under stepwise drug treatment | Relocation along routes | Body | **N** | Duplicates the stroke example; Sterling's account is narrative |
| Subclavian steal | Rerouting by physics (P12) | Body | **E** | |
| Power-line outage redistribution | Rerouting by physics | Engineered network | **E** | Diversification (J2) |
| Budget reallocation after a cut channel | Rerouting by choice | Organisation | **E** | Diversification; pairs with the line-outage example |
| Fasting penguins: phase III at a fat threshold | Break at a set depletion; switch | Body | **Sup** ◆ | Strong, but one more physiology case |
| Kidney: creatinine flat to about half the nephrons lost | The silence | Body | **S** ◆ | Clean numbers; competes with sheep for the same idea |
| Plants in drought: green canopy with 25 to 31% embolism | The silence | Plant | **S** | Diversification beyond animals |
| Honeybee colony collapse | Silence; workforce turnover | Social system | **Sup** ◆ | Diversification; but surface-level only |
| Fly brain disabling costly memory under starvation (Plaçais and Preat) | Units switched off in the top | Body (insect) | **Sup** | |
| MAC13 against MAC16 tumours | Drain against capture | Body | **N** for this paper | Extension |
| Dehnel's phenomenon (shrews) | Reversible economising | Body | **N** | Probe; ranking not predicted |

### 4.6 Citations, by role

| Role | Rule | Items |
|---|---|---|
| **Source of an imported form** | Must cite | Kooijman 2010 (DEB: release, shrinking, synthesising units, recovery fraction); Ford and Fulkerson 1956 (max-flow); Aubin 1991 and Doyen and Saint-Pierre 1997 (viability); Sherbrooke 1968 and the newsvendor literature (recovery); Ibaraki and Katoh 1988 (marginal allocation); Martin 2004 (cost of restoration); Liebig or Leontief (the minimum) |
| **Strongest precedent per neighbour** | One, at most two, each | DEB: Kooijman 2010. Selfish Brain: Peters et al. 2004; Göbel et al. 2010 (formal); Sprengell et al. 2021a (pre-registered method). EMAL: Bobba-Alves, Juster and Picard 2022. Triage: Ames 2006. Plants: Minchin, Thorpe and Farrar 1993 (access-derived priority); Grossman and DeJong 1994 (strict priority). Allostasis: Sterling 2012. Central governor: Noakes 2012 (with one critique cited alongside, for balance). Selfish immune system: Straub 2014. Hypoxia: Hochachka et al. 1996. Cell hierarchy: Buttgereit and Brand 1995. Control: Powers 1973 |
| **Convergence, secondary** | Unification table in the supplement | Peters and Langemann 2009; Sprengell et al. 2021b; Marcelis and Heuvelink 2007; Mauritsson and Jonsson 2023; Schulkin and Sterling 2019; McCann and Ames 2009, 2011; haemodynamic models (Guyton tradition; fetal circulation models); neuron-glia models; Shaulson, Cohen and Picard 2024; disposable soma (Drenos and Kirkwood 2005); Kiecolt-Glaser et al. 1995 |
| **Evidence for a reported test or observation** | Must cite where used | VitalDB; council revenue outturn data; Scully et al. 2016 (sheep); the natural-test sources used in the convergence table |
| **Mathematical context** | One each | Scheffer et al. 2009 (early warning); metabolic control analysis (one review); Michaelis-Menten competition (textbook); Dominant Resource Fairness (Ghodsi et al. 2011) for the conflicting-orders limit |
| **Background** | Cut | General physiology texts; reviews cited only for colour |

**Before any citation is used:** verify it against the original (several are from abstracts or memory; the maths section's list is marked "to check").

### 4.7 Figures and tables

| Item | Tier | Note |
|---|---|---|
| Figure 1: the architecture (governor, network, parts, stores, ledgers) | **C** | The diagram is not yet updated to v0.19 |
| Figure 2: the silence and the break (record flat, stores and lower parts drawn; two thresholds) | **C** | One schematic |
| Figure 3: rate decides harm (loss against speed and depth; scar region) | **S** | From P8 |
| Table: prior theories against the model's components (unification table, condensed to six rows) | **C** | J3 |
| Table: what the model predicts that neighbours do not state | **C** | J4 (maths section Section 3.7) |
| Table: tests and results (H1, PT1, G25, G25-C) | **C** | J5 |
| Table: natural-system convergence | **S** | J2 |

## 5. What the register cuts or moves (summary)

- **Moved to the supplement:** six propositions (paper 4, 7, 9, 10, 15, 17), full proofs, the numerical checks, most G predictions, the natural tests in full, the probes, the systematic searches, the mapping procedure in full, reverse mode.
- **Cut from this paper:**
  - four unexamined carried predictions (G9, G14, G15, G17);
  - the nested-systems extension (one sentence as future work);
  - duplicate physiology examples;
  - background citations.
- **Kept in the main text:** about 9,100 words, three figures, four tables.

## 6. Calls for James (◆)

**All eight decided as Claude suggested (James, 7 October 2026):** repair under strict rank critical; warning lead time supplementary; G18 supporting, one sentence; stroke example held until Rosso et al. 2012 is read; sheep plus plants for the silence, kidney to the supplement; honeybee and fasting penguins to the supplement; mapping procedure summarised in the main text; the extension as one sentence of future work.

1. **Repair under strict rank (paper Proposition 16) as critical.** It is the only formal claim about the repair network, a component no prior theory formalises, but it is untested. Claude: critical.
2. **The warning lead time (paper Proposition 4) as supplementary.** It bears on G12, which failed at H1. Promoting it could read as a rescue. Claude: supplementary, with G12's failure reported plainly in the main text.
3. **G18 (co-movement) as supporting.** It is the prediction that separates dependency from rank, but it is untested and needs a stochastic set-up. Claude: supporting, one sentence.
4. **The stroke example.** Use it only after reading Rosso et al. 2012 in the original. Claude: hold until read.
5. **One example for the silence:** kidney (clean numbers) or sheep (also reads on the release profile), with plants for diversification. Claude: sheep plus plants; kidney to the supplement.
6. **Honeybee and fasting penguins:** strong but surface-level, or one more physiology case. Claude: supplement.
7. **The mapping procedure:** a 250-word summary in the main text, or only in the supplement. Claude: summary in the main text, because rank fixed from documented access is the central method claim.
8. **The extension (drain against capture):** one sentence as future work, or nothing. Claude: one sentence.
