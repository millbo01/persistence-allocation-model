# The Persistence Allocation Model: derived propositions for the paper (DRAFT, batches 1 and 2, 7 October 2026)

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

### P1. Conservation of load: relocation under scarcity, creation by gating (the formal content of "relocated, never removed")

**Corrected 7 October 2026** after review (raw/2026-10-07_chatgpt-assumed_v019-and-maths-section-review.md). The first version asserted invariance of total load under **every** access setting. Its proof assumed the flow is fully used, which a closed gate need not leave true. Checked numerically: the general identity below holds in all random cases, gates included.

**Statement.**
1. **General identity** (from the full resource ledger, maths Section 7). In any step,
$$\sum_i\ell_i=\Gamma-\sum_sd_s-I+R_{\text{unused}}+X,$$
where $R_{\text{unused}}$ is the resource left unused (refilled, spilled, or left in the flow) and $X=\sum_i[a_i-q^0_i]_+$ is allocation above reference.
2. **Scarcity-limited regime: access relocates load.** Where the flow is fully used and no recipient receives above its reference allocation, under each of the settings compared, the total unmet load equals $\Gamma-\sum_sd_s-I$. It is the same under every access ordering at fixed supply, store draw and outside input. **Access decides only where that fixed deficit lands.**
3. **Access-limited regime: gating creates and removes load.** Where a gate leaves resource unused, total unmet load rises one for one with the resource it leaves unused, and the counterpart is refill or spill, so conservation holds. **Opening the gate removes that load, up to the idle resource, without any other part losing.**
   - **Example:** a part's reference allocation is 10 and supply is 10. Gate open: load 0. Gate closed: load 10, with 10 units refilled or spilled.
   - A **mode switch** that opens one class of work and closes another can move access-limited load from one class to the other, rather than remove it.

**Corollary (two intervention regimes).**
- **Where all resource is already used,** an intervention that restores one part's supply without adding resource moves the same amount of load onto other parts. Total load falls only by raising supply, drawing the stores harder (which needs release headroom), or bringing resource in from outside.
- **Where resource sits idle behind a closed gate,** opening the gate removes load up to the idle amount, at no cost in resource to any other part.

**Proof.** Conservation within the step: $U+I+\sum_sd_s=\sum_ia_i+R_{\text{unused}}$. Since $\sum_i(q^0_i-a_i)=\sum_i\ell_i-X$, we have $\sum_i\ell_i=\sum_iq^0_i-\sum_ia_i+X=\Gamma-\sum_sd_s-I+R_{\text{unused}}+X$. Item 2: $R_{\text{unused}}=0$ and $X=0$, so the total contains no access term. Item 3: $X=0$ and $R_{\text{unused}}$ equals the resource the gate leaves unused. ∎

**Established mathematics:** a conservation law (the continuity equation). What is PAM's own is the **bookkeeping of unmet requirement** against a fixed reference, and the **separation of two regimes** by whether resource is left unused.

**Reading:**
- **Scarcity-limited load is relocated, never removed** (the principle, for the resource gap).
- **Access-limited load is an opportunity cost of control architecture.** It can be created and undone by gating, while resource is idle, without relocation. This is the significance of the build and consolidate modes and of growth signalling holding autophagy shut while nutrients are present.
- **Testable patterns:**
  - in a resource-short system, correcting a visible figure without adding resource should be followed by a matching deficit elsewhere (stroke and intensive insulin, Sprengell et al. 2021b citing Rosso et al. 2012, to be read in the original; hypertension under treatment, Sterling 2018);
  - in an access-limited system, opening the gate should relieve the gated process with **no** matching deficit elsewhere, and with a matching fall in refill or spill.

**Check:** P1 (2,000 random instances: the general identity with random gates; invariance under reordering when the flow is fully used; the gated example).

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
| P11 | R9 | **Corrected:** economising never causes disorderly loss; speed changes only when the renewal saving arrives |
| P12 | R11 | **Condition added:** last back only if lowest in marginal value |
| P13 | R12 | **Condition added:** physical rerouting can overload with spare total capacity |
| P14 | R14 | Unchanged |
| P15 | none | New (viability: a constructive condition for collapse, not death) |
| P16 | none | New (conflicting orders: the stated limit) |
| P17 | none | New (rank from affinity; strict as a limit of shared uptake) |
| P18 | none | New (extension layer: a drain is a supply cut; capture is more) |

## 4. Batch 2 (7 October 2026)

### P11. Economising causes no unit loss, whatever its speed, and cuts wear at once (G16)

**Set-up.** Renewal need is a baseline per active unit plus wear per unit of work: $\kappa^n n^{\text{a}}+\kappa^u w$ (maths Sections 0 and 6; the wear term restored 7 October 2026 at James's prompt; the engine has carried it since TQ11). Economising cuts ordinary parts' **work** access by $\epsilon$; it does not cut their renewal access.

**Statement.**
1. **No units are lost through economising,** however fast $\epsilon$ rises.
2. **The saving per step arrives in two parts:**
   - **at once:** the work's own requirement and its wear renewal, $\sum_i(\kappa^w_i+\kappa^u_i)\,w^0_i\,\epsilon$;
   - **as units are switched off:** the baseline renewal of idle units, $\kappa^n$ per unit consolidated. Consolidation runs at up to $\theta K$ per step, so the excess is switched off within $\lceil\epsilon w^0/(\theta K)\rceil$ steps (one unit of work per active unit).
3. **The lower renewal burden lasts as long as work stays cut.** That is so after any repair backlog has been cleared too, and the flow it frees is available to the repair network for rebuilding once supply allows.

**Proof.** Loss arises only from unmet basal maintenance or unmet renewal (A6). Economising lowers the work draw, and with it the wear part of renewal need, by the same factor; the baseline need of units still active stays funded until they are switched off. So no renewal shortfall arises from economising. Consolidation is orderly by definition (maths Section 5, item 3). ∎

**Correction to R9 [flag F, accepted]:** R9 stated that economising is orderly only if it rises no faster than the switch-off rate. That applied the rate-decides-harm result (P6) to a cut in **work**, which is not a cut in renewal. Economising is always orderly. **What speed changes** is only how soon the baseline saving arrives; the work and wear saving is immediate.

**Check:** P11 (300 random instances, including very fast economising, with wear renewal tied to work).

### P12. The fuse, and when it is last back (G13)

**Statement.**
1. **The lowest-ranked part is the first to go short** (P3).
2. **It is last to come back only if its marginal value in recovery is also the lowest.** Phase 5 serves units by marginal value, $V_i=c_i\,\hat P(\text{binds})$ (maths Section 9), not by rank.
3. **The intake is the exception:** it is support, served in phase 3, so it comes back first whatever its rank (P9).

**Proof.** Item 1: P3. Item 2: phase 5 is a greedy allocation by marginal value. Rank enters only through which parts went short and so have binding units. ∎

**Reading [flag G, accepted]:** v0.17's G13 ("lowest-ranked parts take the load first and longest") was written under recovery by rank. Under the marginal-value rule adopted on 7 October 2026, **"longest" needs the condition** that the fuse's value in recovery is also lowest. That is the usual case, because a low-ranked part's shortfall costs least. But a mapping can make it fail (for example, a low-ranked part whose units bind often).

### P13. Cascade along substitutes depends on how flow is rerouted (G24)

**Statement.** A pathway has parallel routes with capacities $C_e$ and flows $f_e$. Route $e$ is lost.
1. **Optimal rerouting** (flow placed where there is headroom, as when a budget or a router reallocates): no surviving route is overloaded **if and only if** $\sum_{e'\neq e}(C_{e'}-f_{e'})\ge f_e$. In a general network: if and only if the remaining maximum flow covers the demand.
2. **Physical rerouting** (flow divides by a fixed rule, such as in proportion to conductance, as in blood vessels, pipes or power lines): a route can be overloaded **even when total headroom suffices.**
3. **Steal.** Where routes to different parts share a source, and a collateral connects one part's branch to another's, losing the second part's direct route sends flow to it through the collateral. At fixed supply, every unit arriving that way is taken from the first part's branch (conservation at the junction; P1). Under physical splitting this happens whether or not the first part can spare it; under reallocation by choice, only from headroom.
4. Whether an overloaded route then fails, and so spreads the cascade, depends on the overload rule, which stays open (maths flag 4).

**Proof.** Item 1: filling headroom route by route places $f_e$ exactly when the sum suffices; the general case is max-flow min-cut. Item 2: by example. Routes with capacities 10, 4 and 10 carry 5, 3.9 and 5. Losing the first leaves headroom of 5.1 for a flow of 5. A split in proportion to capacity sends $5\times4/14\approx1.43$ to the second route, which then carries 5.33 against a capacity of 4. ∎

**Established mathematics:** max-flow min-cut; in power systems, line outage distribution factors and cascading-failure models, where flow redistributes by physics, not choice. **Physiology:** subclavian steal (an occluded subclavian artery is supplied backwards through a vertebral artery, at the brain's expense) and coronary steal under vasodilators.

**What rerouting means here (James's question, 7 October 2026).** Severance or constriction of a route is the trigger, usually of the main, lowest-resistance route, since it carries the most flow. Rerouting is what follows: where the displaced flow goes. The question is **who sets the split**: the network's physics (resistance, impedance), or a choice (a budget holder, a router). In bodies, physics makes the first split and the governor's gates (autoregulation, constriction) correct it over seconds to minutes; where a bed has no effective gate, the physical split stands.

**Reading [flag H, accepted]:** G24 gains a condition that makes it more specific. **Overload cascades and steals are expected where flow divides physically, even with spare total capacity. Where flow is reallocated by choice, they are expected only when total headroom is short.** This separates physiological and engineered networks from budgeted ones in a testable way.

**Check:** P13 (2,000 random instances for item 1; a physical-split overload with sufficient headroom found).

### P14. The order of response to rising requirement (R14)

**Statement.** For a part with switched-off units, as requirement $w^0$ rises:
1. work rises within active capacity, with no change of state;
2. switched-off units are then reactivated, at most $\theta_{\text{re}}K$ per step, each at a cost $k_R$, from what is left in the flow (phase 5);
3. **output falls short** only when the rise per step outpaces reactivation, when reactivation cannot be paid for, or when requirement exceeds total capacity $K$.

**Proof.** From maths Sections 4 and 5: work is bounded by active capacity; reactivation is the only route from switched off to active, and it is rate-limited and paid from the flow. ∎ (No numerical check: it follows directly.)

**Reading:** a part held in reserve (switched off, not lost) responds to rising requirement with a **lag set by its reactivation rate.** It falls short when the rise is faster than that rate, even with spare units and resources. That is the colony probe (P7 in the probe register) in formal terms.

### P15. Collapse against death: a constructive condition for a route back (viability)

**Statement** (viability set $K$ and capture basin as in maths Section 8; the reduced form, no outside support unless admissible at mapping). A system outside $K$ is in **collapse, not death,** if all of the following hold:
1. supply can return to at least the top's need plus every surviving part's basal maintenance;
2. the top's units are not scarred below what the record requires;
3. every non-bypassable link on the top's pathway, and on the pathways of the parts the record depends on, has capacity above zero, or can be restored by the repair network;
4. every part the record depends on that has lost units has its template intact (lost, not scarred) and a pathway for the repair network.

**Proof** (constructive). Under 1, a governor setting exists that meets the top and all basal maintenance (P2), so no further units are lost (P3, P6). Under 2 to 4, the repair network can rebuild every needed part at rate $K_i/h_i$ from what is left in the flow (phase 5). So the state reaches $K$ in finite time and can stay there. That is membership of the capture basin. ∎

**Corollary (time of crisis).** The time to re-enter $K$ is at least the longest rebuild time $\max_i(\text{units to rebuild}_i\cdot h_i/K_i)$ among the parts the record depends on. It rises if supply allows only part of the rebuilding per step.

**Established mathematics:** viability theory (Aubin 1991): capture basin, time of crisis (Doyen and Saint-Pierre 1997). This proposition gives a **sufficient** condition. The full basin needs viability algorithms for a given mapping (maths Section 8).

**Reading:** the conditions name what to measure to tell collapse from death **before** the outcome: supply restorable, the top unscarred, critical links intact or restorable, templates intact. **Death needs one of them to fail.**

### P16. Conflicting orders under joint scarcity have no ordinal answer

**Statement.** Two parts, A and B, each need one unit of each of two complementary resources per unit of work. One unit of each resource is available. The order for resource 1 is A before B, and for resource 2, B before A.
1. **Allocating each resource by its own order** gives A all of resource 1 and B all of resource 2, so **neither part works.**
2. **Every split** $(z,1-z)$ of both resources gives total work 1, and all are Pareto efficient. **The two ordinal orders do not select among them;** a choice needs cardinal information (weights, or the explicit network).

**Proof.** Direct computation under the law of the minimum. ∎

**Established mathematics:** multi-resource allocation under Leontief preferences (Dominant Resource Fairness; lexicographic allocation), where ordinal priorities over complementary resources are known not to determine a joint allocation.

**Reading:** this is why the reduced form reports "explicit access model required" when binding resources have conflicting orders (maths Section 2, bundles). **It is a stated limit of the model, not a gap:** in such cases the order of loss is set by the network, which must be mapped.

**Check:** P16 (the deadlock and the frontier).

### P17. Rank under saturable uptake: affinity, capacity and requirement together (maths queue item 7)

**Corrected 7 October 2026** after review (raw/2026-10-07_chatgpt-assumed_v019-and-maths-section-review.md). The first version took the order of affinity as the order of loss. Rank is the order in which a part loses **adequate** access relative to its reference allocation, and that depends on capacity and requirement as well as affinity. Checked numerically, with a counter-example to the first version.

**Statement.** Parts take a shared resource from a common pool by saturable uptake, $v_i=V_iC/(K_i+C)$: $C$ is the pool's level, $K_i$ the half-saturation constant (inverse affinity) and $V_i$ the maximum uptake. Supply $S$ fixes $C$ through $\sum_iv_i(C)=S$. Let $r_i=q^0_i/V_i$ be the part's reference allocation as a share of its maximum uptake.
1. **Adequacy threshold.** Part $i$ is adequately supplied if and only if $C\ge C^\ast_i$, where
$$C^\ast_i=K_i\,\frac{r_i}{1-r_i}\qquad(r_i<1).$$
A part with $r_i\ge1$ is inadequate at any supply.
2. **Rank.** As supply falls, parts lose adequate access in **descending order of $C^\ast_i$**. Every term is a documented property ($K_i$, $V_i$, $q^0_i$), measurable before outcomes.
3. **Affinity alone** decides the order only where $r_i$ is equal across parts (then $C^\ast_i\propto K_i$), or where $K_i$ and $r_i/(1-r_i)$ are ordered the same way.
   - **Counter-example to affinity alone:** a high-affinity part whose requirement is close to its maximum ($V=1$, $K=1$, $q^0=0.9$; $C^\ast=9$) becomes inadequate before a low-affinity part with a large maximum and a small requirement ($V=10$, $K=10$, $q^0=0.5$; $C^\ast\approx0.53$).
4. **Fractional saturation** $C/(K_i+C)$ does fall with $K_i$ at every supply. That is the order of **saturation**, not of adequacy.
5. **Strict or shared.** Strict priority (P3) is approached when neighbouring thresholds $C^\ast_i$ are far apart. Where they are close, loss of adequacy is near-simultaneous and the shortfall is shared. In the saturation check (four parts, $V_i=1$, equal requirements), the largest deviation from strict filling was 0.15, 0.02 and 0.002 at neighbour separations of $10^2$, $10^4$ and $10^6$.

**Proof.** Item 1: $V_iC/(K_i+C)\ge q^0_i$ rearranges to $C\ge K_iq^0_i/(V_i-q^0_i)$. Item 2: $C$ falls monotonically as $S$ falls, so parts cross their thresholds in descending order of $C^\ast_i$. Items 3 and 4 follow from item 1. Item 5: with thresholds far apart, at any $C$ at most one part is near its threshold, so the shortfall falls on one part at a time. ∎

**Established mathematics:**
- Michaelis-Menten competition for a shared substrate;
- metabolic control analysis (Buttgereit and Brand 1995 measured a hierarchy of ATP consumers by sensitivity to supply);
- Ames's triage mechanism (binding affinity).

**Reading [flag I, revised]:**
- **The bridge from documented access to rank** that v0.18 left domain-specific (maths flag 6) is the adequacy threshold $C^\ast$, not affinity alone. Affinity is one determinant; capacity and the reference requirement are the others.
- **Strict or shared** is set by how far apart the thresholds are: the PT1 secondary question (strict against shared), with a measurable criterion.
- **For mapping:** where access is by saturable uptake, document $K_i$, $V_i$ and the reference allocation, and fix the rank as the order of $C^\ast_i$.

**Check:** P17 (adequacy order equals the order of $C^\ast$ in 200 random three-part cases; the counter-example; the saturation separations).

### P18. An autonomous drain is a supply cut; capture is more (extension layer: host and tumour)

**Prompted by James (7 October 2026).** A tumour draws resources outside the host governor's order. Is it, for the host, simply a reduction of supply?

**Statement.** A nested system draws $T$ per step from the flow before the governed phases (an autonomous drain), and occupies tissue whose former draw was $T_0$.
1. **For every governed part, the drain is exactly a supply cut** of $T_{\text{net}}=T-T_0$. The host's order of loss is the order it would have under starvation of that size (P3), and all the earlier propositions apply with $S$ replaced by $S-T_{\text{net}}$.
2. **Hence, if the tumour only drains,** a tumour-bearing host should match a tumour-free host whose supply is reduced by $T_{\text{net}}$: the same tissues losing, in the same order, by the same amounts. The right control is supply cut by the net drain. A pair-fed control matches food intake but not the drain, so it is not this control.
3. **If the tumour also changes the host's gates or signals (capture),** the host departs from that control: losses fall on tissues out of their rank order, or exceed what the net drain explains.

**Proof.** Item 1: the governed phases see only the flow left after the drain; the draw is otherwise unchanged (checked). Items 2 and 3 follow. ∎

**What the 1991 mouse study shows** (Mulligan and Tisdale, Biochem J 277:321; abstract only, the full text being a scanned PDF):
- The tumour became the second glucose consumer after the brain. Glucose use fell in fat pads, testes, colon, spleen, kidney and, most of all, the brain, "irrespective of cachexia".
- The brain's fall in glucose use was "at least as high as the metabolic demand by the tumour". But its energy was maintained by lactate and ketones.
  - **For the brain, the resource is energy, and glucose and ketones are substitutes.** The brain did not lose priority: it switched fuel, and that freed glucose for the tumour.
- **The decisive comparison is between the two tumours.** The MAC13 tumour took **more** glucose than MAC16, yet only MAC16 produced cachexia. The authors conclude that "alterations in glucose utilization are not responsible for the cachexia".
  - **In PAM's terms: the drain alone does not produce the wasting.** The cachexia-causing tumour does something the larger drain does not: it acts on the host's gates (capture).
  - This fits the Drosophila finding that wasting "is dependent on the genetic characteristics of the tumour", with "host malnutrition or tumour burden" not sufficient (S11891).

**James's question, answered as far as the evidence allows:**
- **Did only the brain lose out, or did the others lose harder?** The tissue-by-tissue figures are not available (the scanned full text is behind a bot check). The abstract says every listed tissue's glucose use fell, the brain's most, and the brain's energy was maintained.
- **So the pattern fits "the drain acts as a supply cut, and the host's order holds":**
  - the highest-ranked part kept its energy by substitution;
  - lower tissues gave up glucose;
  - the tumour is a sink drawing ahead of the order.
- **"It almost halves supply" cannot be checked** without the figures. The size of the cut is the net drain $T-T_0$, as James put it: the tumour's draw less what the tissue it displaced used to draw.
- **Cachexia is the part a pure drain does not explain.** The two-tumour comparison says capture is needed.

**Reading [flag J, accepted]:** P18 gives the extension layer a **test**:
- **Drain only:** a tumour-bearing host matches a host with supply cut by the net drain.
- **Capture:** it does not, and the departure is where the tumour's signals act.

**Testable** where tumour uptake, displaced-tissue draw and host tissue losses are measured together (isotope tracing in tumour models). It stays in the extension layer and **out of the first paper's core claims** (v0.18 Section 15).

**Check:** P18 (2,000 random instances: the draw with a drain equals the draw with supply cut by the drain).

**What batch 2 does not cover:**
- the general network form $\Phi$;
- dynamic priority (Tier 1);
- nested systems beyond the drain case;
- G18 (co-movement), which needs a stochastic set-up.

## 5. Flags for James

**All five accepted (James, 7 October 2026):** G3, G20 and G26 amended in v0.18; R3's wording corrected in theory/PAM_results_v0.18.md; P1's invariance stated beside the principle in v0.18 Section 1.

| No. | Prediction | What the derivation shows | Proposed change | Direction |
|---|---|---|---|---|
| A | G3 | Under the default (DEB) release, the rate-independent case does not occur. The store left at the break is $(\Gamma-M)/k$, rising linearly with the rate of shortfall | Add the quantitative form as a sharpened G3 or a new prediction | Harder to refute (more specific) |
| B | Scar threshold (results R3) | The earlier threshold is necessary, not sufficient; a sufficient form exists | Correct the results wording | Neutral (a correction) |
| C | G20 | Under maximum flow, failure with willing receivers intact means a link **cut or constricted below need,** or damage | Add "or constricted below need" | Slightly easier; neutral if capacity is measured independently |
| D | G26 | Refill level is a critical fractile of remembered episode depths | Add the quantitative form | Harder (more specific) |
| E | Principle (Section 1 of v0.18) | Total unmet load is invariant under access settings at fixed supply, stores and outside input | State P1's invariance as a derived result beside the principle | Neutral (identity) |

**Corrections after review (7 October 2026;** raw/2026-10-07_chatgpt-assumed_v019-and-maths-section-review.md**):** P1 restated with two regimes (relocation under scarcity; creation and removal by gating); P17 restated with the adequacy threshold. Both checked numerically. The corresponding v0.19 text is corrected in the draft; v0.18 carries the earlier forms until v0.19 is approved.

**Not decided here:** whether P4's sheep reading (rate-independence observed, so a high-turnover or full-release store in that setting) belongs in the paper. It is an observation about the release profile, not a test.

### Batch 2 flags

**All five accepted (James, 7 October 2026):** F (G16 and R9; renewal written with the wear term in the maths), G (G13), H (G24, with steal), I (rank from affinity in mapping), J (drain against capture in the extension).

| No. | Prediction | What the derivation shows | Proposed change | Direction |
|---|---|---|---|---|
| F | G16; results R9 | Economising cuts work, not renewal, so it causes no disorderly loss at any speed. R9's speed condition misapplied P6 | Correct R9; G16 holds unconditionally in the reduced form | Harder (any loss during economising would now count against it) |
| G | G13 | Under marginal-value recovery, the fuse is last back only if its recovery value is also lowest | Add the condition to G13 | Slightly easier (narrower) |
| H | G24 | Physical rerouting can overload a substitute even with spare total capacity; reallocation by choice cannot | Add the condition to G24 | Harder (more specific; separates physical from budgeted networks) |
| I | Mapping (Section 8); maths flag 6 | Where access is by saturable uptake, rank is the order of affinities, and strict against shared is set by their separation | Add as a mapping rule | Neutral (a measurement rule fixed before outcomes) |
| J | Extension layer (Section 15) | A drain is exactly a supply cut by the net drain; capture shows as departure from that control | Add as the extension's first test, outside the core | Neutral; keeps the extension testable |
