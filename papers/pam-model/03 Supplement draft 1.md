# Supplementary material (draft 1, 7 October 2026)

*S1 is written in full. S2 to S9 are an assembly plan: each names its content and the working file it is to be built from (internal paths, to be replaced by the assembled text before submission).*

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
