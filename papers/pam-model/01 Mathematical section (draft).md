# The Persistence Allocation Model: mathematical section (draft 1, 7 October 2026)

*Working draft for the model paper. Written against model version 0.19 (consolidation draft). Title, venue and the final selection of results are for James. Internal note: proposition numbers below are renumbered for the paper; the crosswalk to the working file (theory/PAM_propositions_DRAFT.md) is at the end. The nested-systems result (working P18) is left out, as the extension is outside the first paper's core claims.*

---

## 3. The model in formal terms

We write the model for a system that regulates its own persistence: a set of working parts drawing on finite shared resources, a set of stores, a network that carries resources to parts, and a governor that sets access. We state the architecture, then a reduced form that can be analysed, then the results that follow from it. Proofs are in Appendix A. Every quantitative result was also checked numerically against an independent implementation of the reduced form (Section 3.6).

### 3.1 Architecture

Time runs in steps. In each step three functions apply:

$$g(t)=G\big(\text{sensed state}(t),\ \text{environment}(t)\big),$$
$$a_{ir}(t)=\Phi_{ir}\big(\{U_r,\ \text{stores}\},\ \text{network},\ g(t),\ s_i(t)\big),$$
$$s_i(t+1)=F_i\big(s_i(t),\ \{a_{ir}(t)\}_r\big).$$

- **The governor** $G$ sets access, $g$: store release, intake, the capacity of pathways and gates, and the repair network's access. It does not set allocations directly, and it does not switch units.
- **The network** $\Phi$ turns access into the realised flow $a_{ir}$ of resource $r$ to part $i$. In bodies it is physical (pressure over resistance; transporters); in organisations it can be a budget.
- **A part** $F_i$ changes state only through what reaches it. It has no utility, claim or demand. Damage from outside (trauma, toxin, pathogen) is the one exogenous input, entering as a loss of units or of pathway capacity.

A part consists of $K_i$ units, each **active**, **switched off** (its route back kept, basal maintenance only, little or no work), **lost** (rebuildable) or **scarred** (lost with its template): $n_i^{\text{a}}+n_i^{\text{o}}+n_i^{\ell}+n_i^{\sigma}=K_i$. One part, the **top**, produces the routine output whose level the governor protects; the ratio of that output to its level is the **record**, $y(t)$.

### 3.2 The reduced form

Where the network is not modelled explicitly, we write the flow as an ordered draw.

**Resources as a flow.** For resource $r$ the available flow in a step is

$$S_r=U_r+I_r+\sum_{s\in r}d_s,$$

supply through the intake, resource drawn in across the boundary, and store draws. Parts draw from it in **phases**, and within a phase in a fixed **order** $\pi_r$, each up to its draw:

1. the top's full need;
2. every other part's basal maintenance;
3. support parts' work and renewal (parts the top depends on, and the intake while it has something to take in);
4. every other part's work and renewal, with work cut by the economising share $\epsilon$;
5. what is left: reactivation and rebuilding, against refilling the stores, by marginal value.

What a part does not draw stays in the flow for later parts; nothing is returned.

**Rank.** $\pi_r$ is the order in which parts lose adequate access to $r$ when $r$ alone is scarce. It is fixed in advance from documented properties of access (constriction under sympathetic drive, autoregulation, affinity, redundancy, discretionary status), never read off an observed order of loss.

**Work and requirements.** A part's work is limited by its scarcest resource:

$$w_i=\min\Big(\hat c_i,\ (1-\epsilon_i)\,w_i^0,\ \min_r A^{w}_{ir}/\kappa^{w}_{ir}\Big),$$

where $\hat c_i$ is effective capacity (active units, scaled by dependency on another part's output), $w^0_i$ the reference work and $A^w_{ir}$ the part's access to $r$ for work. Near co-limitation, the synthesising-unit form of Kooijman (2010, Section 3.7) gives less work smoothly and has the minimum as its limit. A part's requirements are $\kappa^b$ per unit kept in existence (basal maintenance), $\kappa^w$ per unit of work, and renewal $\kappa^n n^{\text{a}}+\kappa^u w$: a baseline per active unit plus wear per unit of work.

**Stores.** Store $s$ releases at most $\rho_s(L_s)$ per step. The default is release proportional to content, $\rho_s=k_sL_s$, as in DEB reserve mobilisation (Kooijman 2010, Section 2.3); the alternative is full release at a constant rate until empty. Of the flow left undrawn, a fraction $\phi_r$ refills the stores and the rest is spilled.

**Units change only through supply.** Unmet basal maintenance is paid from the part's own units, which shrinks the part: with resource yield $m$ per unit broken down and overhead $y\ge1$, the units lost are $u=[\kappa^bn-a^b]_+/(\kappa^b+m/y)$, the DEB shrinking rule with absolute preference for reserve. Unmet renewal switches units off at up to $\theta K$ per step; the rest fail at rate $1/\tau_f$. Losses within one episode beyond a template limit $Q^\ast K$ are scarred. Switched-off units are reactivated at up to $\theta_{\text{re}}K$ per step at a cost; lost units are rebuilt by the repair network, a set of parts governed like any other.

### 3.3 Load and the two ledgers

For each part and resource, the **reference allocation** $q^0_{ir}(t)$ is fixed in advance as a rule (basal maintenance, work and renewal for the reference state under current conditions), and is never lowered because units have switched off. **Load** is the unmet part of it:

$$\ell_{ir}=\big[q^0_{ir}-a_{ir}\big]_+ .$$

Load arises from three origins: falling supply, rising requirement, or a governor setting that restricts access while resources suffice (admitted only for a setting and gate documented independently in advance). With the gap $\Gamma_r=\sum_iq^0_{ir}-U_r$, the **resource ledger** in a shortfall is

$$\Gamma_r=\sum_sd_s+I_r+\sum_i\ell_{ir}:$$

every unit of the gap is carried by a store, met from outside, or left unmet at a named part. The **state ledger** records what unmet load leaves behind: units switched off, lost or scarred, and work not done, which may land on another system. Residue is a consequence of load and is never added to the resource ledger.

### 3.4 Assumptions for the results

| | Assumption |
|---|---|
| A1 | Results hold resource by resource; where several bind, the record holds only if it holds for each |
| A2 | The ordered draw of Section 3.2 |
| A3 | The order $\pi_r$ is fixed over the period considered |
| A4 | Store release as in Section 3.2; a store is drawn only for need left after supply |
| A5 | The reference allocation is fixed in advance and never lowered |
| A6 | Units change only through supply, as in Section 3.2, except damage from outside |
| A7 | The **margin** $M$ is what can go unmet below the top before the record moves: ordinary parts' draws $D_4$ if the top depends on its supports, and $D_4+P+B$ (adding support parts' draws and basal maintenance) if it does not |

Notation: $N$, the top's full need; $B$, other parts' basal maintenance; $P$, support parts' draws; $D_4$, ordinary parts' draws.

### 3.5 Results

**Conservation**

**Proposition 1 (relocation).** In a shortfall, $\Gamma=\sum_sd_s+I+\sum_i\ell_i$. For fixed supply, store draws and outside input, the total unmet load $\sum_i\ell_i$ is the same under every access setting: every order, every phase assignment, every gate. Access settings decide only where load lands.

*Reading.* This is the formal content of the model's principle that load is relocated, never removed. It is an identity, not an empirical claim. Its consequence is testable: an intervention that restores one part's supply without adding resource must leave an equal deficit elsewhere. Total load can fall only through supply, store draw (which requires release headroom) or resource from outside.

**The silence and the break**

**Proposition 2 (silence).** The top's draw is met if and only if $S\ge N$; every part's basal maintenance and every support part's draw is met if and only if $S\ge N+B+P$. Hence the record is flat this step and the next if and only if $\Gamma\le\sum_sd_s+M$.

*Reading.* Within that region the record carries no information about load below the top. The record breaks at two thresholds: at once when $S<N$, and one step later, through dependency, when $N\le S<N+B+P$. The condition is the leftover-service bound for the highest-priority flow under pre-emptive priority.

**Proposition 3 (store left at the break).** Let a constant gap $\Gamma$ per step be carried by one store from level $L_0$, with $M<\Gamma\le kL_0$.
1. Under full release ($\rho^0\ge\Gamma$), the record breaks when the store is empty, after a cumulative shortfall of $L_0$, whatever $\Gamma$.
2. Under proportional release ($\rho=kL$), the record breaks when the store falls to
$$L^\ast=\frac{\Gamma-M}{k}.$$
So a faster shortfall leaves more of the store unused at the break, linearly in $\Gamma$, with slope $1/k$.
3. If $\Gamma\le M$, the record never breaks.

*Reading.* The rate-independence of the break, an intuitive consequence of a store carrying a gap, holds only for full release, or in the limit $kL_0\gg\Gamma-M$. Under the default release, the reserve remaining at decompensation should rise with the rate of loss.

**Proposition 4 (warning and its lead time).** Under proportional release, release headroom $kL-\Gamma$ reaches zero at $L=\Gamma/k$; from then on recovery from small perturbations of the record slows. The break follows after a lead time
$$T_{\text{lead}}\approx\frac{\ln\big(\Gamma/(\Gamma-M)\big)}{-\ln(1-k)}\approx\frac1k\ln\frac{\Gamma}{\Gamma-M}.$$
Under full release there is no slowing before the store empties.

*Reading.* This is a version of critical slowing down before a transition (Scheffer et al. 2009), with a lead time that shortens as the shortfall grows relative to the margin and vanishes as the margin goes to zero.

**The order of loss**

**Proposition 5 (order).** Within a phase, the parts short of their draw form a lower segment of $\pi$. No part loses basal maintenance while any part draws for work. The top goes short last.

*Reading.* With equal switch-off rates, units are switched off and then lost in ascending order of rank. Strict lexicographic priority is assumed in hierarchical plant allocation models (Wermelinger et al. 1991; Grossman and DeJong 1994). Here it is the reduced form of an access network, with the order fixed in advance from access.

**Proposition 6 (rank from affinity).** Let parts take a shared resource from a pool at level $C$ by saturable uptake, $v_i=V_iC/(K_i+C)$, with $\sum_iv_i(C)=S$.
1. At every level of supply, a part's fractional supply falls with $K_i$: parts lose access in order of affinity, lowest first.
2. As neighbouring affinities separate ($K_{i+1}/K_i\to\infty$), the allocation tends to the strict priority of Proposition 5. Between, loss is shared.

*Reading.* Where access is by saturable uptake, the rank is a measurable property (half-saturation constants), and whether priority is strict or shared is set by their separation. In our checks, with four parts the largest deviation from strict order was 0.15 at a hundredfold separation, 0.02 at $10^4$ and 0.002 at $10^6$. This links the model's rank to Michaelis-Menten competition, to metabolic control analysis (measured hierarchies of ATP consumers; Buttgereit and Brand 1995), and to triage of micronutrients by binding affinity (Ames 2006).

**Proposition 7 (the limit of rank).** Two parts each need one unit of each of two complementary resources per unit of work, one unit of each is available, and the orders conflict (part A first for resource 1, part B first for resource 2). Allocating each resource by its own order gives neither part any work. Every split $(z,1-z)$ of both resources gives total work 1 and is Pareto efficient; the two ordinal orders do not choose among them.

*Reading.* Under joint scarcity with conflicting orders, the order of loss is set by the network, which must then be mapped explicitly. This is a stated limit of the reduced form, consistent with results on multi-resource allocation under Leontief preferences.

**Harm**

**Proposition 8 (rate decides harm).** For a renewable part with basal maintenance met, let the units the repair network can renew fall by $\varphi$ per step to a depth $\Delta$.
1. If $\varphi\le\theta K$, no units are lost at any depth.
2. If $\varphi>\theta K$, the loss $\Lambda$ satisfies
$$\Delta\Big(1-\frac{\theta K}{\varphi}\Big)-\tau_f(\varphi-\theta K)\ \le\ \Lambda\ \le\ \Delta\Big(1-\frac{\theta K}{\varphi}\Big).$$
3. A scar is possible only if $\Delta(1-\theta K/\varphi)>Q^\ast K$, and certain if $\Delta(1-\theta K/\varphi)-\tau_f(\varphi-\theta K)>Q^\ast K$.

*Reading.* Depth without speed never harms; speed without depth never scars; a scar needs both, and the threshold depth falls as speed rises. Fixed capital ($Q^\ast=0$) is scarred by any fall faster than its switch-off rate.

**Proposition 9 (shrinking).** A part whose basal maintenance is short pays from its own units and loses $u=[\kappa^bn-a^b]_+/(\kappa^b+m/y)$ of them. The remaining units are exactly funded, and $u$ is never larger than the unfunded share $n(1-\beta)$, with equality when units hold nothing usable ($m=0$).

**Proposition 10 (economising).** Economising cuts work access, not renewal. It therefore loses no units at any speed. Its saving arrives at once for work and its wear, $\sum_i(\kappa^w_i+\kappa^u_i)w^0_i\epsilon$ per step, and as idle units are switched off for their baseline renewal.

**Failure**

**Proposition 11 (exhaustion, severance and constriction).** Let delivery to the top and its supports be bounded by pathway capacity, the minimum cut between source and part. If the record falls while some ordinary part still draws for work, or a store still has release headroom, then either the minimum cut to the top or a support part is below its need (severance at zero, constriction above zero), or damage from outside has removed units of the top or a support part.

*Reading.* Failure with willing receivers still supplied identifies a cut or narrowed link, or outside damage, and each is observable independently. The bound is the max-flow min-cut theorem (Ford and Fulkerson 1956).

**Proposition 12 (rerouting).** A pathway with parallel routes, capacities $C_e$ and flows $f_e$, loses route $e$.
1. If displaced flow is reallocated to where there is headroom, no surviving route is overloaded if and only if $\sum_{e'\ne e}(C_{e'}-f_{e'})\ge f_e$ (in a general network, if and only if the remaining maximum flow covers demand).
2. If flow divides by a fixed physical rule, such as in proportion to conductance, a surviving route can be overloaded even when total headroom suffices.
3. Where routes to different parts share a source and a collateral joins them, flow reaching one part through the collateral is taken from the other's branch at fixed supply (steal).

*Reading.* Cascades and steals are expected in physically divided networks (vessels, pipes, power lines) even with spare capacity, and in networks reallocated by choice (budgets, routers) only when total capacity is short. Subclavian and coronary steal are physiological instances; line-outage redistribution is the engineering one.

**Proposition 13 (collapse, not death).** A system outside its viable set is inside the capture basin (Aubin 1991), so in collapse rather than death, if:
- supply can return to at least the top's need plus every surviving part's basal maintenance;
- the top is not scarred below what the record requires;
- every non-bypassable link the record depends on has capacity above zero or can be restored;
- every part the record depends on has its template intact and a pathway for repair.

The time to re-enter the viable set is at least the longest rebuild time among those parts.

*Reading.* The conditions are measurable before the outcome; death requires one of them to fail. The condition is sufficient; the full capture basin of a given mapping needs viability algorithms.

**Recovery**

**Proposition 14 (recovery order and partial refill).** The intake comes back first after refeeding, whatever its rank. Thereafter surplus goes by marginal value. With $F$ the distribution of remembered episode depths, $c_S$ the cost per unit of a store being short, $\rho$ the expected frequency of shortfall, and $V$ the best competing value of a part's binding units, the store refills to
$$L^\ast=F^{-1}\!\Big(1-\frac{V}{c_S\,\rho}\Big)\quad (V<c_S\rho),\qquad L^\ast=0\ \text{otherwise}.$$

*Reading.* Stores refill only part way while parts still bind, deeper after frequent or deep shortfalls. After short episodes parts come back first; after long ones, stores do. The refill level is the newsvendor critical fractile; the allocation rule is that of marginal analysis for spares (Sherbrooke 1968) and state-dependent reserves (McNamara and Houston).

**Proposition 15 (the fuse).** The lowest-ranked part is the first to go short. It is the last to come back only if its marginal value in recovery is also lowest.

**Proposition 16 (repair under competition).** With repair work $W$ per step binding and damage $D_j$ to parts in rank order, part $i$ finishes healing at step $\lceil\sum_{j\le i}D_j/W\rceil$. The highest-ranked damaged part heals as fast as it would alone; each lower-ranked part is delayed by the damage ranked above it. Under a sustained shortfall the repair parts lose access, so every finishing time rises.

*Reading.* Strict-rank repair is distinguishable from shared repair: under strict rank, the most important damaged part does not slow when others are damaged too.

**Proposition 17 (rising requirement).** For a part with switched-off units, rising requirement is met first within active capacity, then by reactivation at up to $\theta_{\text{re}}K$ per step at a cost; output falls short only when the rise outpaces reactivation, reactivation cannot be paid for, or requirement exceeds total capacity.

### 3.6 Numerical verification

Each quantitative claim was checked against a minimal implementation of the reduced form, written from the equations above and independent of the simulation engine used earlier in the work. The checks draw random instances (up to 2,000 per result) and test the stated equalities, bounds and orderings: Propositions 1 to 3, 4 (lead time within one step), 5, 6, 7, 8 (both bounds), 9, 10, 12, 14 and 16. All pass. Code is in the supplementary material (`pam_propositions_check.py`).

Two of the checks corrected earlier statements of the same results. The rate-decides-harm expression, first written as an estimate of loss, proved to be an upper bound, so the scar threshold derived from it is necessary rather than sufficient (Proposition 8). And the speed of economising, first thought to matter for loss, does not, because economising cuts work rather than renewal (Proposition 10).

### 3.7 What the model predicts that neighbouring theories do not state

The model converges with several established theories, and we treat that convergence as support. The table lists results that follow in the model but are **not stated** in the neighbouring theories as we have read them (sources in Section 2). Silence is not contradiction: the entries mark where the model makes a claim those theories do not make.

| Result | Dynamic Energy Budget theory | Selfish Brain theory | Allostasis and allostatic load | Control theory |
|---|---|---|---|---|
| Total unmet load is invariant under access settings (P1) | Conserves mass and energy; keeps no reference requirement against which unmet load is counted | A supply chain with build-ups in front of bottlenecks; no account of unmet requirement across many parts | Load hidden from total expenditure, stated in words | No resource ledger |
| The record carries no information inside the silence region (P2) | Not stated | Brain energy held while body loses, for two compartments | Stated in words (the hidden cost) | A regulated variable held by feedback, without a shortfall budget |
| Store left at the break rises with the rate of shortfall (P3) | Reserve dynamics give the release form; the decompensation threshold with a margin is not stated | Not stated | Not stated | Not stated |
| Rank from affinity; strict as the limit of shared uptake (P6) | Not stated across parts | Access by insulin dependence, two compartments | Not stated | Not stated |
| Scar threshold in speed and depth (P8) | No unit loss or scarring; ageing damage is irreparable | Not stated | Wear of structures, in words | Not stated |
| Failure with receivers supplied implies a cut or narrowed link, or damage (P11) | Not stated | Not stated | Not stated | Not stated |
| Physical against chosen rerouting (P12) | Not stated | Not stated | Not stated | Known in power systems; not stated as a cross-domain prediction |
| Repair served strictly by rank (P16) | No repair allocation | Not stated | Repair squeezed under load, in words | Not stated |

## Appendix A. Proofs

**Proposition 1.** In a shortfall the flow is exhausted, so $\sum_ia_i=S=U+I+\sum_sd_s$. Then $\sum_i\ell_i=\sum_i(q^0_i-a_i)=\sum_iq^0_i-S=\Gamma-\sum_sd_s-I$, which contains no access term. ∎

**Proposition 2.** The top draws first, then all basal maintenance, then support parts (A2). So the top is met if and only if $S\ge N$, and basal maintenance and supports if and only if $S\ge N+B+P$. The top's work next step falls only through its own units (impossible while it is met) or through dependency on supports (excluded when they are met). Since $\sum_iq^0_i=N+B+P+D_4$, $S\ge N+B+P$ is equivalent to $\Gamma\le\sum_sd_s+D_4$; without dependency, the top's work is unaffected by shortfalls below it, giving $M=D_4+P+B$. ∎

**Proposition 3.** While $kL\ge\Gamma$ the store releases the whole gap, so $L$ falls by $\Gamma$ per step. Once $kL<\Gamma$, the store releases $kL$, $L$ falls by the factor $(1-k)$ per step, and $\Gamma-kL$ falls below the top. By Proposition 2 the record breaks at the first step with $\Gamma-kL>M$, that is $L<(\Gamma-M)/k$; in discrete time the level at the break lies in $((1-k)L^\ast,L^\ast]$. Under full release with $\rho^0\ge\Gamma$, the store carries the whole gap until empty, after cumulative draw $L_0$, independent of $\Gamma$. If $\Gamma\le M$ the unmet share never exceeds $M$. ∎

**Proposition 4.** Headroom $kL-\Gamma$ is positive above $L_w=\Gamma/k$ and zero there. Thereafter $L$ decays geometrically by $(1-k)$ until $L<L^\ast=(\Gamma-M)/k$ (Proposition 3). The number of steps is $\ln(L_w/L^\ast)/(-\ln(1-k))=\ln(\Gamma/(\Gamma-M))/(-\ln(1-k))$. Under full release, headroom $\rho^0-\Gamma$ is constant until the store holds less than one step's release. ∎

**Proposition 5.** Draws are sequential within a phase: a part is short only if the flow is exhausted at its turn, so every later part in that phase draws nothing. Phases complete in order, so a basal shortfall implies that phases 3 and 4 drew nothing, and a shortfall at the top implies that every other draw was zero. ∎

**Proposition 6.** The fractional supply $C/(K_i+C)$ is decreasing in $K_i$ for every $C>0$. For $K_i\ll C\ll K_{i+1}$, part $i$ is near saturation and part $i+1$ near zero; as the ratios $K_{i+1}/K_i$ grow, the interval of $C$ in which two neighbouring parts are both partly supplied shrinks relative to the scale of $C$, and the allocation approaches the lexicographic filling of Proposition 5. ∎

**Proposition 7.** Under the law of the minimum, allocating each resource by its own order gives A both units of resource 1 and none of resource 2, and B the reverse, so both work zero. Any common split $(z,1-z)$ gives work $z$ and $1-z$, total 1, and no allocation gives more, since each resource limits total work to 1. ∎

**Proposition 8.** Over the episode the active units fall from $K$ to $K-\Delta$, so switched-off and lost units together number $\Delta$. During the decline, which lasts at least $\Delta/\varphi$ steps, the excess $x$ of active over renewable units satisfies $x_{t+1}=(x_t-\theta K)(1-1/\tau_f)+\varphi\ge\varphi>\theta K$, so $\theta K$ units are switched off each step and at least $\theta K\Delta/\varphi$ in all; hence $\Lambda\le\Delta(1-\theta K/\varphi)$. At the end of the decline the excess is at most its steady value $x^\ast=\theta K+\tau_f(\varphi-\theta K)$, and no more than that can be switched off in the tail; hence $\Lambda\ge\Delta(1-\theta K/\varphi)-\tau_f(\varphi-\theta K)$. If $\varphi\le\theta K$, every unit not renewed is switched off within the step, so $\Lambda=0$. The scar conditions follow from $\Lambda>Q^\ast K$. ∎

**Proposition 9.** $u$ solves $\kappa^b(n-u)=a^b+(m/y)u$. Since $m/y\ge0$, $u\le[\kappa^bn-a^b]_+/\kappa^b=n(1-\beta)$, with equality at $m=0$. ∎

**Proposition 10.** Units are lost only through unmet basal maintenance or unmet renewal (A6). Economising lowers the work draw, and with it the wear part of renewal need, by the same factor; the baseline renewal of units still active remains funded until they are switched off. So no renewal shortfall arises. The immediate saving is the requirement of the work cut and its wear. ∎

**Proposition 11.** If an ordinary part still draws for work, or a store has headroom, then $S\ge N+B+P$ (Proposition 2), so the flow could meet the top and its supports. If they are short, another bound binds: the pathway, whose capacity is the minimum cut (Ford and Fulkerson 1956), or their own capacity, which falls only through supply (excluded) or damage. ∎

**Proposition 12.** Item 1: placing $f_e$ into surviving headroom succeeds exactly when the headroom sums to at least $f_e$; in a general network this is max-flow min-cut. Item 2, by example: routes with capacities 10, 4 and 10 carry 5, 3.9 and 5; losing the first leaves headroom 5.1 for flow 5, but a split in proportion to capacity sends $5\times4/14\approx1.43$ to the second route, which then carries 5.33 against capacity 4. Item 3: at fixed supply, conservation at the junction means flow leaving one branch through the collateral is subtracted from that branch (Proposition 1). ∎

**Proposition 13.** Under the first condition, an access setting exists that meets the top and all basal maintenance (Proposition 2), so no further units are lost (Propositions 5 and 8). Under the remaining conditions, the repair network can rebuild each needed part at its rebuild rate from what is left in the flow. The system therefore reaches the viable set in finite time and can remain there, which is membership of the capture basin. The time bound follows from the rebuild rates. ∎

**Proposition 14.** The intake is a support part, served in phase 3. A store's marginal value $c_S\rho(1-F(L))$ is non-increasing in $L$, since $1-F$ is a survival function; allocating surplus greedily by marginal value stops refilling where that value falls to $V$, the stated quantile. Greedy allocation is optimal for separable concave value (Ibaraki and Katoh 1988). ∎

**Proposition 15.** The first part follows from Proposition 5. Phase 5 allocates by marginal value, so the order of return follows value, which agrees with rank only where the mapping makes it so. ∎

**Proposition 16.** Under strict priority, cumulative repair work after $t$ steps is $tW$, applied to damage in rank order; part $i$ is complete when $tW\ge\sum_{j\le i}D_j$. ∎

**Proposition 17.** Work is bounded by active capacity; reactivation is the only route from switched off to active, and it is rate-limited and paid from what is left in the flow. ∎

## References to add or check

- Ames BN (2006). PNAS 103:17589.
- Aubin J-P (1991). *Viability Theory*. Birkhäuser.
- Buttgereit F, Brand MD (1995). Biochem J 312:163.
- Ford LR, Fulkerson DR (1956). Can J Math 8:399.
- Grossman YL, DeJong TM (1994). Tree Physiol 14:329.
- Ibaraki T, Katoh N (1988). *Resource Allocation Problems*. MIT Press.
- Kooijman SALM (2010). *Dynamic Energy Budget Theory for Metabolic Organisation*, 3rd edn. Cambridge University Press.
- McNamara JM, Houston AI (state-dependent reserves; exact reference to select).
- Scheffer M et al. (2009). Nature 461:53.
- Sherbrooke CC (1968). Oper Res 16:122.
- Wermelinger B, Baumgärtner J, Gutierrez AP (1991). Ecol Model 53:1.

## Crosswalk (internal; remove before submission)

| Paper | Working file |
|---|---|
| Prop. 1 | P1 |
| Prop. 2 | P2 |
| Prop. 3 | P4 |
| Prop. 4 | P5 |
| Prop. 5 | P3 |
| Prop. 6 | P17 |
| Prop. 7 | P16 |
| Prop. 8 | P6 |
| Prop. 9 | P7 |
| Prop. 10 | P11 |
| Prop. 11 | P8 |
| Prop. 12 | P13 |
| Prop. 13 | P15 |
| Prop. 14 | P9 (with P10's intake rule, results R10) |
| Prop. 15 | P12 |
| Prop. 16 | P10 |
| Prop. 17 | P14 |
| (left out) | P18, the nested-systems drain test |

**For James:**
- The selection: all of P1 to P17 are in. A shorter main text could keep Propositions 1 to 6, 8, 11, 12 and 14, and move the rest to a supplement.
- The comparison table (Section 3.7) is worded as "not stated in the theories as we read them". It should be checked against the full texts before submission, especially the DEB column.
- References marked "to add or check" are from memory or from abstracts and must be verified before use.
