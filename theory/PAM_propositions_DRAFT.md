# The Persistence Allocation Model: derived propositions for the paper (DRAFT, batch 1, 7 October 2026)

**Status:** theorising (phase 3). Draft for James. This is GPT's condition 3 for a significant contribution ("propositions derived analytically, not only simulated"), written for the model paper.

**Relation to earlier work:**
- It supersedes theory/PAM_results_v0.18.md (R1 to R14) for the paper, which stays as the record.
- It takes in what has changed since R1 to R14 were written:
  - the four DEB imports (proportional release, shrinking from units, synthesising units, recovery fraction);
  - the marginal-value recovery rule and viability (theory/PAM_recovery_value_and_viability.md);
  - pathway capacity as maximum flow;
  - the strict-rank decision for repair.
- It states each result as a proposition with its assumptions.
- It names the established mathematics each result instances (literature before formula).
- **Every proposition with a quantitative claim is checked numerically** against a reference implementation of the reduced form, written from the maths and not from the frozen engine (scripts/pam_propositions_check.py; all checks pass).

**Rules kept:**
- **Nothing here adds a mechanism.**
- Where a derivation sharpens or corrects a v0.18 prediction, it is marked **[flag]** and listed at the end. **Changing a prediction's wording is James's call.**
- Proofs are proofs for the reduced form under the stated assumptions, not for the general network $\Phi$.

## 1. Assumptions (the reduced form)

| No. | Assumption | Source |
|---|---|---|
| A1 | **One resource at a time.** Results hold resource by resource. Where several resources bind, a part's work is the minimum over them (or the synthesising-unit form, which is never larger), so the record holds only if it holds for every resource | maths Section 2 |
| A2 | **The ordered draw.** The available flow $S=U+I+\sum_s d_s$ is drawn in phases: (1) the top's full need; (2) every other part's basal maintenance; (3) support parts' work and renewal; (4) every other part's work and renewal. Within a phase, parts draw in the fixed order $\pi$, each up to its draw | maths Section 2 |
| A3 | **Fixed order.** $\pi$ is fixed over the period considered (no dynamic priority) | v0.18, Tier 1 alternative excluded |
| A4 | **Stores.** Store $s$ releases at most $\rho_s(L_s)$ per step. The default is proportional release, $\rho_s=k_sL_s$ with $0<k_s\le1$ (DEB). The alternative is full release, a constant rate $\rho_s=\rho^0_s$ until the store is empty. A store is drawn only for the need left after supply | maths Section 3 |
| A5 | **Reference.** $q^0_i$ is fixed at mapping as a rule and is never lowered because units switched off | maths Section 7 |
| A6 | **Units change only through supply,** except damage from outside. Switch-off rate $\theta K$ per step; disorderly failure at $1/\tau_f$ per step; unmet basal maintenance is paid from the part's own units with yield $m$ and overhead $y\ge1$ | maths Section 5 |
| A7 | **Margin.** $M$ is the most the system can leave unmet below the top before the record moves. $M=D_4$ (ordinary parts' work and renewal) when the top depends on its supports ($\omega_{\text{top}}>0$); $M=D_4+P+B$ when it does not | maths Section 4; results R1 |

**Notation:**
- $N$: the top's full need;
- $B$: other parts' basal maintenance;
- $P$: support parts' draws;
- $D_4$: ordinary parts' draws;
- $\Gamma=\sum_iq^0_i-U$: the gap between reference requirement and supply;
- $\ell_i=[q^0_i-a_i]_+$: local load.

## 2. Propositions

### P1. Conservation of load, and its invariance under access (the formal content of "relocated, never removed")

**Statement.** In a shortfall (no part above reference, nothing refilled or spilled):
1. **Ledger closure:** $\Gamma=\sum_sd_s+I+\sum_i\ell_i$.
2. **Invariance:** for fixed supply $U$, outside input $I$ and store draws $d_s$, **the total unmet load $\sum_i\ell_i$ is the same under every access setting** (every order $\pi$, every phase assignment, every gate the governor sets). Access settings decide only **where** the load lands.

**Proof.** Conservation of the resource within the step: everything drawn is $\sum_ia_i=S=U+I+\sum_sd_s$ when the flow is exhausted, which it is in a shortfall. Then $\sum_i\ell_i=\sum_i(q^0_i-a_i)=\sum_iq^0_i-S=\Gamma-\sum_sd_s-I$. The right side contains no access term. ∎

**Corollary (the only levers on total load).** Total unmet load falls only by:
- raising supply;
- drawing the stores harder (which needs release headroom);
- bringing resource in from outside.

**Any intervention that restores one part's supply at fixed supply, stores and outside input moves the same amount of load onto other parts.**

**Established mathematics:** a conservation law (the continuity equation) for a single conserved flow; the same identity underlies DEB's mass balance and the Peters and Langemann supply chain. What is PAM's own is the **bookkeeping of unmet requirement** against a fixed reference (A5), which those models do not keep.

**Reading:**
- This is the formal statement of the principle. It is an identity of the model, not an empirical claim.
- The empirical content is where the load lands (P3, P6, P7).
- The corollary is testable as a pattern: an intervention that corrects a visible figure without adding resource should be followed by a matching deficit elsewhere. Two candidate illustrations from the reading:
  - **stroke:** restoring blood glucose with intensive insulin reopened the periphery's route, and in one trial infarct growth was 2.5 times larger (Sprengell et al. 2021b, citing Rosso et al. 2012; **to be read in the original before use**);
  - **hypertension under treatment:** blocking one compensatory route moves the load to the next (Sterling 2018).

**Check:** P1 (2,000 random instances: closure, and total load unchanged under random reorderings).

### P2. The silence: when the record holds (G1, G4)

**Statement.** In any step:
1. The top's draw is met if and only if $S\ge N$.
2. Every part's basal maintenance and every support part's draw is met if and only if $S\ge N+B+P$.
3. Hence, under A7, **the record is flat this step and the next if and only if $\Gamma\le\sum_sd_s+M$.** In particular, with the top dependent on its supports, the record is flat while the gap is no larger than what the stores release plus everything ordinary parts draw for work and renewal.

**Proof.** Items 1 and 2 follow from the phase order: the top draws first, then all basal maintenance, then supports. The top's work next step falls only through its own units (impossible while item 1 holds) or its dependency on supports (excluded by item 2 when $\omega_{\text{top}}>0$). Item 3: $S\ge N+B+P$ is equivalent to $\Gamma\le\sum d+D_4$, since $\sum q^0=N+B+P+D_4$. ∎

**Two thresholds** [flag 6 of R1, accepted]:
- $S<N$: the record falls at once;
- $N\le S<N+B+P$: it falls one step later, through dependency.

**Established mathematics:** pre-emptive (strict) priority service; the condition is the "leftover service" bound of network calculus applied to the top as the highest-priority flow.

**Reading:** inside the region $\Gamma\le\sum d+M$, the record carries **no information** about load below the top. "The record sees compromise, not stress."

**Check:** P2 (2,000 random instances: both thresholds exact).

### P3. The order of loss (G2, G5, G13, G20 first part)

**Statement.**
1. **Within a phase, the parts short of their draw form a lower segment of $\pi$:** if part $i$ is short, every part after $i$ in $\pi$ draws nothing in that phase.
2. **Basal before work:** no part loses basal maintenance while any part draws in phases 3 or 4.
3. **The top goes last:** if the top is short, every other part draws nothing.

**Proof.** The draw is sequential: a part is short only if the flow is exhausted at its turn, so every later draw is zero. Phases are completed in order. ∎

**Established mathematics:** lexicographic (pre-emptive) priority, as in hierarchical plant allocation models (Wermelinger et al. 1991; Grossman and DeJong 1994), which have it as an assumption. In PAM it is the reduced form of an access network, with $\pi$ fixed from documented access before outcomes (A3, mapping).

**Reading:** with equal switch-off rates, units are switched off, then lost, in ascending order of rank. **Under several resources whose orders conflict, this proposition does not apply:** the joint allocation is underdetermined, and the model requires the explicit network (maths Section 2, bundles).

**Check:** P3 (2,000 random instances).

### P4. The break, and how much store is left (G3 under proportional release)

**Set-up.** A constant gap $\Gamma$ per step (the rate of shortfall) is carried by one store with level $L$, from $L_0$, with margin $M$ (A7) and $M<\Gamma\le kL_0$.

**Statement.**
1. **Full release** ($\rho^0\ge\Gamma$): the record breaks when the store is empty, after a cumulative shortfall of $L_0$ (to within one step), **whatever $\Gamma$.** This is G3's rate-independent case. (The numerical check uses the limit $\rho^0\to\infty$; the result holds for any $\rho^0\ge\Gamma$.)
2. **Proportional release ($\rho=kL$):** the store carries the whole gap while $kL\ge\Gamma$. Below $L=\Gamma/k$, it releases $kL<\Gamma$ and decays geometrically, and the difference falls on parts below the top. **The record breaks when the store falls to**
$$L^\ast=\frac{\Gamma-M}{k}$$
(in discrete time, within the step: $L^\ast(1-k)<L_{\text{break}}\le L^\ast$).
3. **Hence a faster shortfall leaves more of the store unused at the break,** linearly in $\Gamma$. G3's rate-independence holds under proportional release only in the limit $kL_0\gg\Gamma-M$.
4. If $\Gamma\le M$, the record never breaks; the store decays towards zero and parts below the top carry the rest.

**Proof.** While $kL\ge\Gamma$, $d=\Gamma$. Once $kL<\Gamma$, $d=kL$ and the unmet share $\Gamma-kL$ falls below the top. By P2 the record breaks at the first step with $\Gamma-kL>M$, that is $L<(\Gamma-M)/k$. The store's level falls monotonically, by $\Gamma$ then by the factor $(1-k)$ per step, which gives the discrete bound. ∎

**Established mathematics:** first passage of a linear reservoir (exponential depletion) to a threshold; DEB's reserve mobilisation gives the release form (Kooijman 2010, Section 2.3).

**Reading and prediction [flag A]:**
- **Under the model's default release, G3's rate-independent case does not occur.** Instead:
  - **the store left unused at the break rises linearly with the rate of shortfall;**
  - **its slope is $1/k$, the store's turnover time.**
- This is testable wherever the store's level at decompensation and the rate of loss are both measured. In blood loss, for example: is more reserve left at decompensation after faster bleeding?
- The sheep data (natural test 1: cumulative loss at the break 27.0% against 27.3% at a fivefold rate difference) are the rate-independent pattern. Read through P4, they suggest either a high turnover ($kL_0\gg\Gamma-M$) or a full-release store **in that setting**. This is an observation about which release profile fits, not a rescue.

**Check:** P4 (500 random instances: store left at the break within the discrete bound; full release leaves nothing; monotone in $\Gamma$; no break when $\Gamma\le M$).

### P5. Warning before the break, and its lead time (G12)

**Statement** (set-up as P4, proportional release).
1. **Release headroom,** $h=kL-\Gamma$, falls linearly in time while the store carries the gap, and reaches zero at $L=\Gamma/k$. From then on, a knock to the record cannot be restored from the store, so recovery from knocks slows towards the break (results R5).
2. **The break follows headroom loss after a lead time**
$$T_{\text{lead}}\approx\frac{\ln\big(\Gamma/(\Gamma-M)\big)}{-\ln(1-k)}\ \approx\ \frac1k\ln\frac{\Gamma}{\Gamma-M}$$
(within one step).
3. **Hence the warning is shorter the larger the gap relative to the margin,** and vanishes as $M\to0$ (no parts below the top left to carry load, so headroom loss and break coincide).
4. **Full release gives no slowing before the store empties:** headroom $\rho^0-\Gamma$ is constant until the store holds less than one step's release, so there is no warning beyond the final step.

**Proof.** Headroom zero at $L_w=\Gamma/k$. Thereafter $L$ decays by the factor $(1-k)$ per step until $L<(\Gamma-M)/k$ (P4). The number of steps is $\ln(L_w/L^\ast)/(-\ln(1-k))$. ∎

**Established mathematics:** critical slowing down before a transition (Scheffer et al. 2009, early-warning signals): recovery rate falls to zero as a stability margin closes.

**Reading:**
- A quantitative form of G12's first case, adding a **lead time** that shrinks with the rate of shortfall.
- **On H1:** the H1 failure (no slowing before falls in blood loss under anaesthesia, fallback cohort, half weight) is not re-examined here.
  - P5 adds only that a fast shortfall relative to the margin gives a short warning.
  - That reading would need the margin $M$ and the turnover $k$ named in advance in a new test. It is **not** an explanation of the H1 null.
  - Under the conservation-principle rules, any explanation of the null must name a specific fault and be logged as a prediction before anyone looks.

**Check:** P5 (500 random instances: lead time within one step of the formula).

### P6. Rate decides harm: the scar threshold (G8)

**Set-up.** A renewable part of $K$ units, basal maintenance met. The units the repair network can renew fall by $\varphi$ per step, to a depth $\Delta$, then hold. Units not renewed are switched off up to $\theta K$ per step; the rest fail at $1/\tau_f$ per step (A6).

**Statement.**
1. **If $\varphi\le\theta K$: no disorderly loss at any depth.**
2. **If $\varphi>\theta K$:** the disorderly loss $\Lambda$ satisfies
$$\Delta\Big(1-\frac{\theta K}{\varphi}\Big)-\tau_f(\varphi-\theta K)\ \le\ \Lambda\ \le\ \Delta\Big(1-\frac{\theta K}{\varphi}\Big).$$
3. **Scar:** with template limit $Q^\ast K$:
   - a scar is **possible only if** $\Delta(1-\theta K/\varphi)>Q^\ast K$ (necessary);
   - it is **certain if** $\Delta(1-\theta K/\varphi)-\tau_f(\varphi-\theta K)>Q^\ast K$ (sufficient).

**Proof.**
- Total units leaving the active state over the episode equal $\Delta$, since the excess of active over renewable units returns to zero.
- While the decline lasts (at least $\Delta/\varphi$ steps), the excess is at least $\varphi>\theta K$ every step, so $\theta K$ units are switched off each step. Hence switched-off units are at least $\theta K\Delta/\varphi$, giving the upper bound on $\Lambda$.
- At the end of the decline, the excess is at most its steady value $x^\ast=\theta K+\tau_f(\varphi-\theta K)$. At most that much more can be switched off in the tail, giving the lower bound. ∎

**Correction to R3 [flag B]:** R3 gave $\Lambda\approx\Delta(1-\theta K/\varphi)$ and the scar threshold as an equality. The derivation shows that expression is an **upper bound**, so R3's threshold is **necessary, not sufficient.** The gap closes as $\Delta$ grows relative to $\tau_f(\varphi-\theta K)$, that is, for deep declines of moderate speed.

**Reading:**
- Depth without speed never harms.
- Speed without depth never scars.
- A scar needs both, and the threshold depth falls as speed rises.
- **Fixed capital** ($Q^\ast=0$) is scarred by any fall faster than the switch-off rate.

**Established mathematics:** a first-order linear system with saturating outflow (a leaky bucket with a capped orderly drain).

**Check:** P6 (400 random instances, both bounds; the upper bound held in every case and was approached for slow, deep declines).

### P7. Shrinking, not collapse, when upkeep goes unpaid (DEB import)

**Statement.** If a part's basal maintenance is short by $[\kappa^bn-a^b]_+$, it loses
$$u=\frac{[\kappa^bn-a^b]_+}{\kappa^b+m/y}$$
units. The remaining $n-u$ units are then exactly funded.
1. $u$ falls as the yield $m$ rises and as the overhead $y$ falls.
2. $u\le n(1-\beta)$, the earlier rule, with equality when $m=0$.

**Proof.** $u$ solves $\kappa^b(n-u)=a^b+(m/y)u$. ∎

**Established mathematics:** DEB's shrinking rule with absolute preference for reserve (Tolla et al. 2007; Kooijman 2010, eq. 4.6).

**Reading:** a part paying its upkeep from its own units **shrinks** rather than losing its whole unfunded share. Shrinkage counts as disorderly loss towards the template limit, so P6's scar rule applies to it.

**Check:** P7 (2,000 random instances).

### P8. Exhaustion against severance, with pathway capacity as maximum flow (G20 second part)

**Statement.** Let the top's (or a support part's) delivery be bounded by its pathway capacity $C_P$, the minimum cut between source and part (maths Section 8). If the record falls while:
- (a) some ordinary part still draws in phase 4, or
- (b) a store still has release headroom,

then one of the following holds:
- **the pathway's minimum cut is below the top's or a support part's need** (severance is the case $C_P=0$; **constriction** is $0<C_P<$ need);
- **damage from outside** has removed units of the top or a support part.

**Proof.** Under (a) or (b), $S\ge N+B+P$ (P2), so the flow could meet the top and supports. If they are short, a bound other than the flow binds: the pathway (its minimum cut), or their own capacity, which falls only through supply (excluded) or damage. ∎

**Established mathematics:** the max-flow min-cut theorem (Ford and Fulkerson 1956).

**Reading and [flag C]:**
- v0.18's G20 (sharpened) names "a cut link or damage from outside".
- The derivation under maximum flow gives "**a link cut or constricted below need,** or damage from outside". A constricted pathway (stenosis, a partial blockage, a narrowed budget channel) fails the top while the flow is still there.
- This widens the diagnostic slightly. It stays usable because constriction is observable independently (measured capacity against need).

**Check:** none numerical; it follows from P2 and the theorem.

### P9. Recovery order, and partial refill as a critical fractile (G10, G22, G26)

**Statement** (phase 5, marginal-value recovery, maths Section 9).
1. **The intake comes first** after refeeding, whatever its rank, because it is support (phase 3) (G22).
2. **Partial refill (G26).** Let $F$ be the distribution of remembered episode depths. With $c_S$ the cost per unit of a store being short and $\rho$ the expected frequency of shortfall, a unit of surplus refills the store while its marginal value $c_S\,\rho\,(1-F(L))$ exceeds the best competing value $V$ (a part's units still binding). **The store refills to**
$$L^\ast=F^{-1}\!\Big(1-\frac{V}{c_S\,\rho}\Big)\quad\text{if }V<c_S\rho,\qquad L^\ast=0\ \text{otherwise.}$$
3. **Hence:**
   - refill stops short of full while parts still bind;
   - it is deeper after frequent shortfall (high $\rho$) or deep remembered episodes (heavy $F$);
   - **after a short episode** (low $\rho$), parts' binding units outbid the store and come back first. **After a long one,** the store does (G10, qualitative unless costs are mapped).

**Proof.**
- Item 1: phase order.
- Item 2: the store's marginal value is non-increasing in $L$, because $1-F$ is a survival function. Greedy allocation by marginal value stops where the store's value falls to $V$, which is the stated quantile.
- Greedy allocation is optimal for separable concave value (the discrete resource-allocation problem; Ibaraki and Katoh 1988). ∎

**Established mathematics:** the newsvendor critical fractile; METRIC-style marginal allocation of spares (Sherbrooke 1968); state-dependent reserves (McNamara and Houston).

**Reading [flag D]:** G26 gains a quantitative form: **the refill level is the $(1-V/(c_S\rho))$ quantile of remembered episode depths.** It is testable where store refill after an episode and the history of episode depths can both be measured (seasonal fat stores; organisational reserves).

**Check:** P9 (greedy refill against the quantile, five value levels).

### P10. Repair under competition, strict rank (G23)

**Statement.** With repair work $W$ per step binding and damage $D_j$ to parts in rank order:
1. part $i$ finishes healing at step $\big\lceil\sum_{j\le i}D_j/W\big\rceil$;
2. **the highest-ranked damaged part heals as fast as alone;**
3. every lower-ranked damaged part is delayed by the damage ranked above it;
4. under a sustained shortfall the repair parts lose access (phase 4), so $W$ falls and every finishing time rises (G23 a).

**Proof.** Strict priority service of cumulative work. ∎

**Established mathematics:** pre-emptive priority queues (finishing time of class $i$ equals the cumulative work of classes $1..i$ over the service rate).

**Reading:** the strict-against-shared choice (James, 7 October 2026: strict) is testable. Does the most important damaged part slow when others are damaged too? Under strict rank it does not.

**Check:** P10 (1,000 random instances).

## 3. Crosswalk to the earlier results

| Here | Earlier | Change |
|---|---|---|
| P1 | R13 | **Invariance added:** total load is fixed under every access setting at fixed supply, stores and outside input |
| P2 | R1 | Stated as "if and only if"; margin $M$ defined |
| P3 | R2 | Unchanged; the conflict case named |
| P4 | R4 | **Exact form under the DEB default:** store left at the break $=(\Gamma-M)/k$ |
| P5 | R5 | **Lead time added** |
| P6 | R3 | **Corrected:** the approximation is an upper bound; the scar threshold is necessary, with a sufficient form |
| P7 | none | New (DEB shrinking) |
| P8 | R6 | **Constriction added** under maximum flow |
| P9 | R7, R10 | **Replaced:** marginal-value recovery, refill as a critical fractile |
| P10 | R8 | Unchanged, strict rank |

## 4. Batch 2 (to write next)

- **P11. Economising is orderly** if it rises no faster than the switch-off rate (R9), with the stores' saving per step.
- **P12. The fuse** (R11): the lowest-ranked part takes load first and longest; the intake is the exception.
- **P13. Cascade along substitutes** (R12): no overload if and only if the surviving routes' headroom covers the lost flow; the cascade rule stays open (maths flag 4).
- **P14. The order of response to rising requirement** (R14): work within capacity, then reactivation, then output falls.
- **P15. Collapse and death** (viability theory): conditions under which a mapped system is in the capture basin; time of crisis.
- **P16. Conflicting orders under joint scarcity:** a constructive example that no ordinal rule decides; why the explicit network is required.
- **P17. Rank as an ordering of elasticities** (metabolic control analysis; maths queue item 7): whether strict priority is the limit of shared control as consumers' elasticities to supply separate.

**What these do not cover:**
- the general network form $\Phi$;
- dynamic priority (Tier 1);
- nested systems;
- G18 (co-movement), which needs a stochastic set-up.

## 5. Flags for James

| No. | Prediction | What the derivation shows | Proposed change | Direction |
|---|---|---|---|---|
| A | G3 | Under the default (DEB) release, the rate-independent case does not occur. The store left at the break is $(\Gamma-M)/k$, rising linearly with the rate of shortfall | Add the quantitative form as a sharpened G3 or a new prediction | Harder to refute (more specific) |
| B | Scar threshold (results R3) | The earlier threshold is necessary, not sufficient; a sufficient form exists | Correct the results wording | Neutral (a correction) |
| C | G20 | Under maximum flow, failure with willing receivers intact means a link **cut or constricted below need,** or damage | Add "or constricted below need" | Slightly easier; neutral if capacity is measured independently |
| D | G26 | Refill level is a critical fractile of remembered episode depths | Add the quantitative form | Harder (more specific) |
| E | Principle (Section 1 of v0.18) | Total unmet load is invariant under access settings at fixed supply, stores and outside input | State P1's invariance as a derived result beside the principle | Neutral (identity) |

**Not decided here:** whether P4's sheep reading (rate-independence observed, so a high-turnover or full-release store in that setting) belongs in the paper. It is an observation about the release profile, not a test.
