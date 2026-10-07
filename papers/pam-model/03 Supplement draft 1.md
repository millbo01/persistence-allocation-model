# Supplementary material (draft 1, 7 October 2026)

*S1 and S11 are written in full. S2 to S9 are an assembly plan: each names its content and the working file it is to be built from (internal paths, to be replaced by the assembled text before submission).*

## S1. Supplementary propositions and proofs

Notation and assumptions as in the main text, Section 3.3. Main-text propositions are cited by their paper numbers.

**S1.1 Warning before the break, and its lead time.** Under proportional release ($\rho=kL$) and a constant gap $\Gamma$ with $M<\Gamma\le kL_0$:
- release headroom $kL-\Gamma$ falls linearly in time while the store carries the gap, and reaches zero at $L=\Gamma/k$. From then on, recovery from small perturbations of the record cannot draw on the store and slows;
- the break follows after a lead time $T_{\text{lead}}\approx\ln\big(\Gamma/(\Gamma-M)\big)/\big(-\ln(1-k)\big)\approx k^{-1}\ln\big(\Gamma/(\Gamma-M)\big)$, which shortens as the gap grows relative to the margin and vanishes as the margin goes to zero;
- under full release, headroom is constant until the store holds less than one step's release, so there is no slowing before the store empties.

*Proof.* Headroom is zero at $L_w=\Gamma/k$. Thereafter $L$ decays by the factor $(1-k)$ per step until $L<(\Gamma-M)/k$ (Proposition 3); the number of steps is $\ln(L_w/L^\ast)/(-\ln(1-k))$. ∎

*Note.* This bears on G12, which failed its first held-out test (main text, Section 5.1). It is reported here, not in the main text, so that it is not read as a rescue: using it would require the margin and the store's turnover to be fixed in advance in a new test.

**S1.2 The limit of rank under joint scarcity.** Two parts each need one unit of each of two complementary resources per unit of work; one unit of each is available; the orders conflict (part A first for resource 1, part B first for resource 2).
- Allocating each resource by its own order gives neither part any work.
- Every split $(z,1-z)$ of both resources gives total work 1 and is Pareto efficient. The two ordinal orders do not choose among them.

*Proof.* Under the law of the minimum, allocation by order gives A both units of resource 1 and none of resource 2, and B the reverse. Any common split gives work $z$ and $1-z$. ∎ Consistent with multi-resource allocation under Leontief preferences (Ghodsi A, Zaharia M, Hindman B, Konwinski A, Shenker S, Stoica I (2011), Dominant resource fairness: fair allocation of multiple resource types, Proceedings of the 8th USENIX Symposium on Networked Systems Design and Implementation). Where this case arises, the order of loss is set by the network, which must be mapped.

**S1.3 Shrinking when upkeep goes unpaid.** A part whose basal maintenance is short pays from its own units and loses $u=[\kappa^bn-a^b]_+/(\kappa^b+m/y)$ of them, where $m$ is the resource recoverable per unit broken down and $y\ge1$ the overhead. The remaining units are exactly funded, and $u\le n(1-\beta)$ (the unfunded share), with equality when units hold nothing usable.

*Proof.* $u$ solves $\kappa^b(n-u)=a^b+(m/y)u$. ∎ This is the DEB shrinking rule with absolute preference for reserve (Kooijman 2010, Sections 4.1.5 and 3.7.4, eq. 4.6).

**S1.4 Economising loses no units.** Economising cuts ordinary parts' work access by a share $\epsilon$; it does not cut renewal. It therefore causes no unit loss at any speed. Its saving arrives at once for the work and its wear, $\sum_i(\kappa^w_i+\kappa^u_i)w^0_i\epsilon$ per step, and as idle units are switched off for their baseline renewal.

*Proof.* Units are lost only through unmet basal maintenance or renewal. Economising lowers the work draw, and with it the wear part of renewal need; the baseline need of units still active stays funded until they are switched off. ∎

**S1.5 The fuse.** The lowest-ranked part is the first to go short (Proposition 4). It is the last to come back only if its marginal value in recovery is also lowest, since recovery allocates by marginal value (Proposition 10). The intake is the exception: it comes back first whatever its rank.

**S1.6 Rising requirement.** For a part with switched-off units, rising requirement is met first within active capacity, then by reactivation at up to $\theta_{\text{re}}K$ per step at a cost. Output falls short only when the rise outpaces reactivation, reactivation cannot be paid for, or requirement exceeds total capacity.

*Proof.* Work is bounded by active capacity; reactivation is the only route from switched off to active, and it is rate-limited and paid from what is left in the flow. ∎

## S2. Numerical checks (assembly plan)

- **Content:** the reference implementation of the reduced form, written from the equations and independent of the simulation engine used earlier; the random-instance design (up to 2,000 instances per result); each check and its outcome.
- **Results:** every quantitative proposition passes:
  - Propositions 1 (both regimes, including allocation above reference), 2, 3, 4, 5 (adequacy order, with the counter-example to affinity alone), 6 (both bounds), 8, 10 and 11;
  - S1.1 (lead time within one step), S1.2, S1.3 and S1.4.
- **Corrections the checks or review made,** stated plainly:
  - the loss expression in Proposition 6 is an upper bound, not an estimate;
  - economising speed does not cause loss;
  - total load is invariant only where the flow is fully used;
  - rank under saturable uptake depends on capacity and requirement as well as affinity.
- **Code:** `pam_propositions_check.py`, with its output.
- **Build from:** scripts/pam_propositions_check.py; theory/PAM_propositions_DRAFT.md.

## S3. Prior theories against the model's components (assembly plan)

- **Content:** the full comparison table: sixteen theories by twelve components, with notes on each cell, and cells read from abstracts marked as such.
- **Build from:** theory/PAM_unification_table.md; theory/PAM_open_checks.md (N1 to N11).

## S4. All predictions, with status (assembly plan)

- **Content:** G1 to G26 in their current wording, layer, the deriving proposition and evidential status, using the evidence labels (modelling choice, derived, simulation result, natural-system observation, direct test, compatible but non-diagnostic, unknown, contradicted, fitted).
- **Excluded from the paper:** G9, G14, G15 and G17, carried from an earlier version without re-examination. The supplement lists them as excluded, not as predictions.
- **Build from:** theory/PERSISTENCE_ALLOCATION_MODEL_v0.19.md, Section 10.

## S5. Held-out test records (assembly plan)

- **For each of H1 and PT1:**
  - the pre-registration (with its hash);
  - the setting map and mapping;
  - the analysis code (with its hash), tested on synthetic data first;
  - the procedure log and deviations, each with its direction;
  - the computed result, the replication, the blind adjudication (verbatim) and the sensitivity analyses.
- **Build from:** tests/ (H1 VitalDB and PT1 files); tests/results/H1-VDB, H1-VDB-R1, PT1, PT1-R1; raw/ (adjudications); tests/ADJUDICATION_RULES.md.

## S6. Natural-system observations (assembly plan)

- **Content:**
  - the checks in full (blood loss, fasting, kidney, plants in drought, honeybee, fetal growth restriction, muscle, weight cycling, recovery order, re-tuning), each with predictions written before sources were opened, contamination declared, verdicts and weights;
  - the kidney and fasting-penguin cases (moved here from the main text);
  - the honeybee colony.
- **Build from:** theory/natural_test_*.md; theory/natural_tests_patterns.md.

## S7. Findings logged against the model (assembly plan)

- **Content:** every non-conforming or possibly non-conforming finding, with source, the place it bears on, its weight, and any explanation logged in advance (none yet):
  - Krieger (1921) organ losses;
  - the plant hydraulic-segmentation negative result;
  - the spruce drought legacy;
  - the H1 G1 check;
  - a corrected entry (fuel substitution in the tumour-bearing brain, first logged as against brain priority, withdrawn on reading the full abstract), kept for the record.
- **Build from:** theory/PAM_open_checks.md; theory/PAM_probe_register.md; theory/natural_test_plants_drought.md; theory/search_check1_s2/STATUS.md.

## S8. Literature searches (assembly plan)

- **Content:**
  - check 1, two systematic searches for formal models of priority among parts under shortage: protocols, strings, known-item sensitivity design, revision and deviations D-1 (plant strand by reviews) and D-2 (an agent-assisted title pass checked against a blind sample), counts, screening decisions, and the held-out miss explained;
  - check 2, models of the order of organ loss in starvation and haemorrhage.
- **Build from:** theory/PAM_check1_search_protocol.md; theory/PAM_check1_search2_protocol.md; theory/search_check1/; theory/search_check1_s2/; theory/search_check2/.

## S9. Mapping a system, in full (assembly plan)

- **Content:**
  - the nine mapping steps;
  - the access guard for modes and gates;
  - the rule for rank under saturable uptake;
  - the bias ledger (scoring interpretive freedom before looking anything up);
  - the reverse mode, which suggests where to look and never names a cause.
- **Build from:** theory/PERSISTENCE_ALLOCATION_MODEL_v0.19.md, Sections 8 and 9; theory/PAM_probe_register.md (bias ledger).

## S10. Compatible illustrations (not tests)

Cases whose direction fits a proposition but which cannot bear weight. They are known outcomes, read after the model was built.

**S10.1 Intensive insulin after ischaemic stroke (Proposition 1, scarcity regime).**
- **The trial:** Rosso et al. (2012), INSULINFARCT, *Stroke* 43:2343-2349 (abstract read; closed access). 180 patients with hyperacute ischaemic stroke were randomised to intensive or usual subcutaneous insulin for 24 hours.
- **Results:**
  - intensive insulin gave better glucose control (mean below 7 mmol/L in 95.4% against 67.4%);
  - it went with larger infarct growth, a secondary outcome (median 27.9 against 10.8 cm³; P = 0.04);
  - three-month function was identical (45.6% in both groups);
  - deaths were 10% against 15.6%, not reported as significant.
- **Reading under the model:** correcting a visible figure (blood glucose) without adding resource reopens the insulin-dependent route into muscle and fat. Under the Selfish Brain account, post-stroke hyperglycaemia is the brain's own pull on supply (Sprengell, Kubera and Peters 2021b), so the deficit would move to the injured brain.
- **Why it is not support:**
  - one trial;
  - a secondary outcome at P = 0.04;
  - no difference in function or death;
  - where the glucose went was not measured;
  - the outcome was known before the model was applied.
- **What a test would need:** a pre-registered study in a system mapped as resource-short, measuring the delivery of the resource to each part before and after a correction that adds none, with the matching deficit predicted in advance.

**Reference added to the supplement:** Sprengell M, Kubera B, Peters A (2021b). Proximal disruption of brain energy supply raises systemic blood glucose: a systematic review. *Front Neurosci* 15:685031. doi:10.3389/fnins.2021.685031 (read in full).

## S11. Dated record of the model's development

**What this is.** A dated record of the model's development, with the time stamps of each step. It is not evidence for the model.
- **Sources:** the public repository's commit history, and the first author's earlier framework for institutions (dated 27 September 2026).
- **The earlier framework** is held privately and is available from the first author on request. Its fingerprint (the SHA-256 of each file) is given in the public repository's README, so a copy supplied on request can be checked against it.
- **Wording:** "first author" is the human author; "AI collaborator" is Claude (Anthropic).
- **Rule:** convergence with earlier work is reported as convergence, never as a successful prediction.

### S11.1 How the model grew

| Date (2026) | Step | What changed |
|---|---|---|
| By 27 September | The first author's earlier framework for institutions | About 60 principles. Candidate formal models: a load ledger, priority queueing and a drift threshold |
| 30 September | First notes on natural systems | Coupling and drift; living systems tie parts' fate to the whole; cancer as a part optimising for itself |
| 3 October | Turn to natural systems | Load conservation stated as a principle; cross-domain cases gathered |
| 4 October | Conserved quantity attempt | Hierarchy of parts, lower parts buffering higher ones, two directions of load, recovery order, part roles (store, intake, working part) |
| 5 October | First queueing form of the model | Parts as servers with stores; load passed down; the break as a store running out |
| 5 October | Ten natural surface checks, each with predictions committed before sources were opened | Blood loss, fasting, kidney, honeybee colony, plants in drought, fetal growth restriction, rival recovery-order rules, muscle, the record rule, re-tuning |
| 5 October | Priority as a formula | Order derived from marginal value, not assigned |
| 5 October | Outside reviews absorbed, each logged as a source | Network rather than tree; use in reverse; economising |
| 6 October | Simplifications by the first author | Work is local and load is displaced; repair as a store refilling; economising as the governor's action |
| 6 October | The present architecture | The system dies, not its parts; a separate governor that only allocates; parts with no demand of their own; units as state; repair cut first; basal maintenance before support work |
| 6 October | First held-out test (H1) | Pre-registered and frozen before any data were opened |
| 7 October | Literature read; current version | Established mathematics imported (DEB forms, viability theory, max-flow min-cut); the formal instances in Section 2 found; propositions proved and checked |

### S11.2 Theorised before the matching work was read (class A)

**How the work ran.** The AI collaborator drafted. The first author shaped the model mainly by contesting drafts that did not fit the first author's principles or observations. Most class A ideas came from those corrections.

| Idea (date fixed in the record) | Whose | Matching work, and when it was found | Agreement and difference |
|---|---|---|---|
| Load is conserved: relocated, not removed (earlier framework; restated 3 October) | First author | Bode integral and conservation of fragility (Csete and Doyle 2002; Doyle and Csete 2011), read 3 October, after the statement. Kleinrock's (1965) conservation law, named 5 October | Same form: priority moves cost but cannot remove it. Theirs holds across frequencies or within one queue; ours across the parts of a system (Proposition 1) |
| The governor is a separate function that only allocates; parts have no demand of their own (6 October) | First author, correcting a draft in which the governor set targets | Supply-chain form of the Selfish Brain (Peters and Langemann 2009) and the central governor (Noakes 2012), read 7 October | Same split between a ranking regulator and passive parts. Perceptual control theory (Powers 1973) was noted by the AI collaborator when the idea was recorded |
| Ordered draw: parts drawn in a fixed order from one flow (6 October) | AI collaborator, formalising the first author's governor rule | Plant sink priority (Grossman and DeJong 1994; Minchin, Thorpe and Farrar 1993) and the hierarchy of ATP consumers (Buttgereit and Brand 1995), found 7 October | Same architecture in plants and in the cell; neither has unit loss, scars, a ledger or use in other domains |
| Repair is the first thing cut when supply falls (6 October) | First author | Triage theory (Ames 2006); Bobba-Alves, Juster and Picard (2022); translational arrest (Hochachka et al. 1996), found 7 October | Same order of cuts. DEB pays maintenance first; the model reconciles the two (basal upkeep first, renewal cut first) |
| Economising: the governor lowers demand and capacity together, on purpose and reversibly (6 October) | Joint | Balanced metabolic suppression (Hochachka et al. 1996), found 7 October | Same reversible, regulated reduction |
| A tumour acts as a cut in total supply, with the order among the other parts kept (7 October) | First author | DEB tumour-in-host models, found in a screening completed the same afternoon | Same treatment of a tumour as a competing sink. The first author had not seen these records |
| With a store carrying the gap and its release not binding, the break comes at the same cumulative shortfall whatever the rate (G3, first clause, 5 October) | AI collaborator | Fast and slow haemorrhage in sheep (Scully et al. 2016); fast and slow drought in trees (Dai, Wang and Wan 2018), matched after | Matches the first clause. The AI collaborator knew both in outline beforehand |

### S11.3 Known when the idea was formed (class B: precedent, no independence claimed)

| Idea | Source, and when it was known |
|---|---|
| Brain spared while organs lose mass in starvation | The Selfish Brain account and Krieger's organ data, logged by the AI collaborator on 3 October. The first author did not read it; no claim is made either way |
| A hierarchy of parts recruited under stress | Miller's Living Systems Theory, read 4 October |
| Three states of a part (coping, stressed, compromised) | Selye's general adaptation syndrome, read 4 October (secondary source) |
| Saturation and sudden decompensation | Woods (2018), read 3 October |
| Renewal classes of tissues | Bizzozero (textbook pathology) |
| The point at which a store begins to release | Cherel and Groscolas's fasting phases, read 4 October |
| The compensatory reserve in blood loss | Convertino's work, known when the blood-loss predictions were written on 5 October |
| Shared upstream supply and a threshold switch | Built from blood-loss findings after the first natural check, 5 October |

### S11.4 Imported (class C: cited as the basis)

Taken from existing work and cited as such:
- DEB forms (shrinking, synthesising units, proportional release);
- viability theory;
- max-flow min-cut;
- the newsvendor critical fractile;
- metabolic control analysis;
- Michaelis-Menten competition;
- greedy allocation by marginal value.

Elements adopted from outside reviews are logged in the repository with their source.

### S11.5 The caveat that governs class A

- The AI collaborator helped build the model, and its training very likely included the Selfish Brain, DEB, allostasis, Hochachka's and Ames's work, and plant allocation models.
- Only the first author's route is independent. The model's wording is not.
- Class A is therefore reported as ideas **theorised beforehand and later found in the literature**, not as predictions and not as evidence.
- The evidence that the architecture is real is the agreement among the four fields in Section 2, which developed separately.
