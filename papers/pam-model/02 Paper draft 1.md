# [Title: James's call] The Persistence Allocation Model: how systems that regulate their own persistence ration finite resources

*Draft 1, 7 October 2026. Drafted to the inclusion register (00 Inclusion register.md). **Citations verified 7 October 2026** (record: 04 Citation check.md): every reference's bibliographic details checked against Crossref, PubMed or OpenAlex, and every claim attributed to a source checked against the text read (full text, or abstract where stated in the record). Supplementary material is in 03 Supplement draft 1.md.*

---

## Abstract

*[To write last, about 200 words.]*

## 1. Introduction

Systems that persist under finite resources show a recurring pattern. When resources run short, the output that matters most is held steady, while parts that matter less are run down out of sight. A bleeding patient's blood pressure holds while gut and kidney are starved of flow; a starving animal's brain keeps its mass while the body loses a third of its own; a council under austerity keeps its statutory services funded while discretionary ones are cut; a tree in drought stays green while its water-conducting tissue fails. The visible figure says little about the strain beneath it, until it breaks.

Parts of this pattern are well described, each in its own domain. Dynamic Energy Budget theory gives maintenance priority over growth in all organisms (Kooijman 2010). The Selfish Brain theory treats the brain as both the protected consumer and the regulator of the body's energy supply (Peters et al. 2004), with formal models and pre-registered tests. The energetic model of allostatic load describes how stress squeezes growth, maintenance and repair while total energy expenditure hides it (Bobba-Alves, Juster and Picard 2022). The triage theory of micronutrients describes scarce vitamins and minerals being allocated to short-term survival at the expense of DNA repair (Ames 2006). Plant models allocate carbon among organs by strict priority or by transport (Minchin, Thorpe and Farrar 1993). Each is a domain case of the same architecture.

This paper states that architecture as a general model, the Persistence Allocation Model, and derives its consequences. Its central claim is:

> In a system that regulates its own persistence, a governor holds the levels its persistence depends on by regulating access to finite shared resources among parts that have no demand of their own; the allocation among parts is the resulting flow. Each part works to the limit of the scarcest resource that reaches it. When what reaches a part falls short of what the reference state requires, whether supply falls, requirement rises or access is restricted, load appears at that part. Where the system as a whole is short, the governor draws its stores, and lower-ranked parts lose access first and switch units off. The routine output, the record, holds until nothing more can be taken: the record sees compromise, not stress. Load is relocated, never removed: the resource gap is met from stores, met from outside the boundary, or left unmet at a named part, and unmet load leaves its residue in switched-off, lost or scarred units, or in work not done, which may land across the boundary. A part scales down without harm when supply falls no faster than it can switch units off; units are lost when supply falls faster; the part is scarred only when those losses destroy what rebuilds it. Repair is its own network, governed like any part: under a sustained shortfall it loses access and lost units wait. Recovery runs the other way: the intake first, then parts and stores in order of value, with stores first when the system has learned its world is scarce. A part dies only when its route back is cut; the system collapses when load reaches the top or a non-bypassable link is cut, and dies only when no route back remains.

**What is new.** We present the model as a unification, not a discovery. Several of its components have precedents (Section 2), and the independence of our route to them is partial: the model was built from the same physiology those theories draw on. Three components, however, are not carried by any prior theory we have found:
1. **the order of loss is fixed in advance from documented properties of access** (pathway constriction, autoregulation, affinity, statutory status), never read off the observed order;
2. **a conserved ledger of load,** which counts unmet requirement against a fixed reference and records where every unit of it lands;
3. **application outside bodies,** with the same rules mapped onto organisations and engineered networks.

**This paper:**
- Section 2: the neighbouring theories;
- Section 3: the model in formal terms, with eleven propositions derived from it;
- Section 4: the predictions, and how they separate the model from its neighbours;
- Section 5: two held-out tests, one failure and one partial support, and a summary of natural-system observations;
- Section 6: scope, limits and failures;
- Section 7: what follows.

## 2. Prior work and convergence

We searched for formal models of priority among parts under shortage, systematically in two databases and by reading the nearest theories in full (search protocols and records in Supplement S8). The results fall into five groups.

**Energetics of the whole organism.** Dynamic Energy Budget (DEB) theory (Kooijman 2010) is the most complete quantitative theory of resource use in organisms. It conserves mass and energy, pays somatic maintenance before growth and reproduction (the κ rule), releases reserve in proportion to its content, shrinks structure when reserve cannot pay maintenance, and treats defence as "more facultative" than somatic maintenance. We import four of its forms (Section 3.2). DEB does not order organs under shortage from their access, keep a ledger of unmet requirement, or allocate repair: damage in DEB is irreparable.

**The brain as protected consumer and regulator.** The Selfish Brain theory (Peters et al. 2004) holds that the brain gives priority to its own energy supply, including by inhibiting glucose uptake into muscle and fat. In later formulations the brain suppresses insulin and so closes the insulin-dependent route into muscle and fat while drawing through an insulin-independent one, set out as an energy-conserving supply-chain model (Peters and Langemann 2009). A brain-centred compartment model has been analysed formally (Göbel and Langemann 2011). It is tested by pre-registered systematic reviews: under caloric restriction the brain lost almost no mass while the body lost a great deal (Sprengell, Kubera and Peters 2021). This is the nearest formal precedent for an order of loss set by access, for two compartments and one resource.

**Stress, maintenance and repair.** The energetic model of allostatic load (Bobba-Alves, Juster and Picard 2022) proposes that the energetic cost of stress first uses up reserve capacity and then squeezes growth, maintenance and repair, potentially without raising total energy expenditure. That is the model's hidden load and its repair cut first, stated in words. Allostasis more broadly (Sterling 2012) treats regulation as predictive and brain-led. The central governor model of exercise (Noakes 2012; for a critique, see Shephard 2009) holds that exercise is stopped before any system fails, with a reserve of motor units always kept. The selfish immune system (Straub 2014) adds the immune and repair system as a second claimant that can take control of the body's spare energy. In this model, the brain and immune settings are two modes of one governor function. A unifying theory of hypoxia tolerance (Hochachka et al. 1996) describes a balanced suppression of energy supply and demand, in which ion pumping and protein synthesis are cut back (channel and translational arrest) while the cell's energy state is held.

**Allocation by access in cells and plants.** In thymocytes, a measured hierarchy of ATP consumers loses supply in order: macromolecule synthesis first, ion pumping later, proton leak last (Buttgereit and Brand 1995). Triage theory (Ames 2006) proposes that scarce micronutrients go to proteins needed for short-term survival over those needed for long-term health, partly through binding affinity, at the level of enzymes, cells and organs. Plant growth models allocate carbon among organs either by strict priority (Grossman and DeJong 1994; classified as hierarchical by Marcelis and Heuvelink 2007) or by transport, where "sink priority" emerges from the transport network and sink kinetics (Minchin, Thorpe and Farrar 1993).

**Control.** Perceptual control theory (Powers 1973) describes hierarchies in which higher levels set the reference values of lower ones. It gives the governor its form, but has no resource, store or ledger.

**Convergence.** These theories converge on the model's components: a protected top that is also the regulator; access as the means of priority; stores drawn first; repair and renewal cut first; costs hidden from the visible figure. We take that convergence as support. Table 1 condenses the comparison (the full table, with sixteen theories, is Supplement S3). What no prior theory carries is the combination: an order fixed in advance from access, for any resource; a conserved ledger of load; and the same rules applied outside bodies.

**Table 1. Prior theories against the model's components** (F, formal; W, stated in words; E, measured, without a general model; p, partial or different form; blank, not found in what we read).

| Theory | Governor | Order from access | Order fixed in advance | Stores drawn first | Repair cut first | Load ledger | Outside bodies |
|---|---|---|---|---|---|---|---|
| Dynamic Energy Budget | p | p | | F | | p | p |
| Selfish Brain | F | F (two compartments) | p | F | | p | |
| Allostatic load (energetic) | W | W | | W | W | W | |
| Triage theory | | W | p | W | W | W | |
| Plant allocation models | | F | | p | | p | |
| Cell ATP hierarchy | | E (measured) | | | E | | |
| **This model** | F | F | **F** | F | F | **F** | **F** |

## 3. The model in formal terms

### 3.1 Architecture

Time runs in steps. In each step three functions apply:

$$g(t)=G\big(\text{sensed state}(t),\ \text{environment}(t)\big),\quad a_{ir}(t)=\Phi_{ir}\big(\{U_r,\ \text{stores}\},\ \text{network},\ g(t),\ s_i(t)\big),\quad s_i(t+1)=F_i\big(s_i(t),\ \{a_{ir}(t)\}_r\big).$$

- **The governor** $G$ sets access, $g$: store release, intake, the capacity of pathways and gates, and the repair network's access. It does not set allocations, and it does not switch units. It is a function, not necessarily a place: a signal produced inside a part belongs to it.
- **The network** $\Phi$ turns access into the realised flow $a_{ir}$ of resource $r$ to part $i$: physical in bodies (pressure over resistance; transporters), a budget in organisations.
- **A part** $F_i$ changes state only through what reaches it. It has no utility, claim or demand. Damage from outside enters as a loss of units or of pathway capacity.

A part consists of $K_i$ units, each **active**, **switched off** (its route back kept, basal maintenance only, little or no work), **lost** (rebuildable) or **scarred** (lost with its template). One part, the **top**, produces the routine output whose level the governor protects; the ratio of that output to its level is the **record**.

### 3.2 The reduced form

Where the network is not modelled explicitly, the flow is written as an ordered draw. For resource $r$ the available flow in a step is $S_r=U_r+I_r+\sum_sd_s$: supply through the intake, resource drawn in across the boundary, and store draws. Parts draw from it in phases, and within a phase in a fixed **order** $\pi_r$, each up to its draw:
1. the top's full need;
2. every other part's basal maintenance;
3. support parts' work and renewal (parts the top depends on, and the intake);
4. every other part's work and renewal, with work cut by economising;
5. what is left: reactivation and rebuilding against refilling the stores, by marginal value.

What a part does not draw stays in the flow; nothing is returned.

**Rank.** $\pi_r$ is the order in which parts lose adequate access to $r$ when $r$ alone is scarce. **It is fixed in advance from documented properties of access** and never read off an observed order of loss.

**Work, stores and units.**
- **Work** is limited by the scarcest resource, $w_i=\min\big(\hat c_i,(1-\epsilon_i)w^0_i,\min_rA^w_{ir}/\kappa^w_{ir}\big)$, with $\hat c_i$ effective capacity and $w^0_i$ reference work. The synthesising-unit form (Kooijman 2010) is the smooth general case.
- **Renewal** needs a baseline per active unit plus wear per unit of work, $\kappa^nn^{\text{a}}+\kappa^uw$.
- **Stores** release in proportion to content by default, $\rho_s=k_sL_s$ (DEB), or at a constant rate until empty. A fraction of undrawn flow refills them; the rest is spilled.
- **Units change only through supply.** Unpaid basal maintenance is paid from the part's own units, so the part shrinks (DEB). Unmet renewal switches units off at up to $\theta K$ per step, and the rest fail at rate $1/\tau_f$. Losses in one episode beyond a template limit $Q^\ast K$ are scarred.
- **Repair** is the work of a set of parts, the repair network, governed like any other and serving damaged parts strictly by rank.

### 3.3 Load and the two ledgers

For each part and resource, the **reference allocation** $q^0_{ir}$ is fixed in advance as a rule and never lowered because units have switched off. **Load** is its unmet part, $\ell_{ir}=[q^0_{ir}-a_{ir}]_+$. It has three origins: falling supply, rising requirement, or a governor setting (a mode) that restricts access while resources suffice. The last is admitted only for a setting and gate documented independently in advance.

**The resource ledger.** With the gap $\Gamma_r=\sum_iq^0_{ir}-U_r$, every unit of the gap is carried by a store, met from outside, or left unmet at a named part (Proposition 1).

**The state ledger.** It records what unmet load leaves behind: units switched off, lost or scarred, and work not done, which may land on another system. Residue is a consequence of load and is never added to the resource ledger.

**Assumptions for the results:**
- results hold resource by resource;
- the ordered draw above, with a fixed order;
- the store release forms above;
- a reference fixed in advance;
- units changing only through supply, except by outside damage.

**The margin** $M$ is what can go unmet below the top before the record moves. It is ordinary parts' draws $D_4$ if the top depends on its supports, and $D_4$ plus support parts' draws $P$ and basal maintenance $B$ if it does not. $N$ is the top's full need.

### 3.4 Propositions

Proofs are in Appendix A. Six further results (a warning lead time, the limit under conflicting orders, shrinking, economising, the fuse, rising requirement) are in Supplement S1. **Every quantitative statement was checked numerically** against an independent implementation of the reduced form (Supplement S2). Two of the checks corrected earlier statements of the same results, and review corrected two more, each then confirmed numerically.

**Conservation**

**Proposition 1 (relocation under scarcity, creation by gating).** In any step, $\sum_i\ell_i=\Gamma-\sum_sd_s-I+R_{\text{unused}}+X$, where $R_{\text{unused}}$ is resource left unused (refilled, spilled or left in the flow) and $X$ is allocation above reference.
1. **Scarcity-limited regime.** Where the flow is fully used and no part receives above its reference, total unmet load is the same under every access ordering at fixed supply, store draw and outside input. Access decides only where it lands.
2. **Access-limited regime.** Where a gate leaves resource unused, total unmet load rises one for one with the resource left unused, balanced by refill or spill. Opening the gate removes that load without any other part losing.

In a resource-short system, restoring one part's supply without adding resource leaves an equal deficit elsewhere. In an access-limited system (growth signalling holding a maintenance process shut while nutrients are present), opening the gate relieves the process with no deficit elsewhere. The two regimes predict different consequences of the same intervention.

**The silence and the break**

**Proposition 2 (silence).** The top's draw is met if and only if $S\ge N$; every part's basal maintenance and every support part's draw is met if and only if $S\ge N+B+P$. Hence the record is flat this step and the next if and only if $\Gamma\le\sum_sd_s+M$.

Inside that region the record carries no information about load below the top. It breaks at two thresholds: at once, and one step later through dependency.

**Proposition 3 (store left at the break).** A constant gap $\Gamma$ per step is carried by one store from level $L_0$, with $M<\Gamma\le kL_0$. Under full release the record breaks when the store is empty, whatever $\Gamma$. Under proportional release it breaks when the store falls to $L^\ast=(\Gamma-M)/k$: **a faster shortfall leaves more of the store unused,** linearly, with slope $1/k$.

The intuitive rate-independence of the break holds only for full release. Under the default release, the reserve remaining at decompensation should rise with the rate of loss.

**The order of loss**

**Proposition 4 (order).** Within a phase, the parts short of their draw form a lower segment of $\pi$. No part loses basal maintenance while any part draws for work. The top goes short last.

Strict priority of this kind is an assumption in hierarchical plant models (Grossman and DeJong 1994; Marcelis and Heuvelink 2007). Here it is the reduced form of an access network, with the order fixed in advance.

**Proposition 5 (rank under saturable uptake).** Parts take a shared resource by saturable uptake, $v_i=V_iC/(K_i+C)$, from a pool at level $C$. Let $r_i=q^0_i/V_i$ be each part's reference requirement as a share of its maximum uptake. Part $i$ is adequately supplied if and only if $C\ge C^\ast_i=K_ir_i/(1-r_i)$, so parts lose adequate access in descending order of $C^\ast_i$. Affinity ($K_i$) alone decides the order only where $r_i$ is equal across parts. Priority is strict where neighbouring thresholds are far apart, and shared where they are close.

Rank is then a measurable property, fixed before outcomes. It combines affinity, capacity and requirement: a high-affinity part working near its maximum can lose adequate supply before a low-affinity part with large capacity and a small requirement. This connects the model's rank to Michaelis-Menten competition, to measured hierarchies of ATP consumers (Buttgereit and Brand 1995) and to triage by binding affinity (Ames 2006).

**Harm**

**Proposition 6 (rate decides harm).** For a renewable part with basal maintenance met, let the units the repair network can renew fall by $\varphi$ per step to a depth $\Delta$.
1. If $\varphi\le\theta K$, no units are lost at any depth.
2. If $\varphi>\theta K$, the loss satisfies $\Delta(1-\theta K/\varphi)-\tau_f(\varphi-\theta K)\le\Lambda\le\Delta(1-\theta K/\varphi)$.
3. A scar is possible only if $\Delta(1-\theta K/\varphi)>Q^\ast K$, and certain if the lower bound exceeds $Q^\ast K$.

Depth without speed never harms; speed without depth never scars; a scar needs both, and the threshold depth falls as speed rises. Fixed capital ($Q^\ast=0$) is scarred by any fall faster than its switch-off rate.

**Failure**

**Proposition 7 (exhaustion, severance and constriction).** Let delivery to the top and its supports be bounded by pathway capacity, the minimum cut between source and part (Ford and Fulkerson 1956). If the record falls while some ordinary part still draws for work, or a store still has release headroom, then either the minimum cut to the top or a support part is below its need (severance at zero, constriction above zero), or damage from outside has removed units of the top or a support part.

Failure while willing receivers are still supplied identifies a cut or narrowed link, or outside damage. Each is observable independently.

**Proposition 8 (rerouting).** A pathway with parallel routes loses route $e$. If its flow is reallocated where there is headroom, no surviving route is overloaded if and only if the surviving headroom covers the lost flow. If flow divides by a physical rule (in proportion to conductance), a surviving route can be overloaded even when total headroom suffices. Where a collateral joins two parts' branches, flow reaching one through it is taken from the other at fixed supply (steal).

Cascades and steals are expected in physically divided networks (vessels, pipes, power lines) even with spare capacity, and in networks reallocated by choice (budgets, routers) only when total capacity is short. Subclavian steal and line-outage redistribution are instances of the first; a budget moved to a channel with room is the second.

**Proposition 9 (collapse, not death).** A system outside its viable set is inside the capture basin (Aubin 1991), so in collapse rather than death, if:
- supply can return to at least the top's need plus every surviving part's basal maintenance;
- the top is not scarred below what the record requires;
- every non-bypassable link the record depends on has capacity above zero or can be restored;
- every part the record depends on has its template intact and a pathway for repair.

The time to re-enter the viable set is at least the longest rebuild time among those parts. The conditions are measurable before the outcome.

**Recovery and repair**

**Proposition 10 (recovery order and partial refill).** The intake comes back first after refeeding, whatever its rank. Thereafter surplus goes by marginal value. With $F$ the distribution of remembered episode depths, $c_S$ the cost per unit of a store being short, $\rho$ the expected frequency of shortfall and $V$ the best competing value of a part's binding units, the store refills to $L^\ast=F^{-1}(1-V/(c_S\rho))$ if $V<c_S\rho$, and not at all otherwise.

Stores refill only part way while parts still bind, deeper after frequent or deep shortfalls. After short episodes parts come back first; after long ones, stores do. The refill level is the newsvendor critical fractile; the allocation rule is marginal analysis of spares (Sherbrooke 1968).

**Proposition 11 (repair under strict rank).** With repair work $W$ per step binding and damage $D_j$ to parts in rank order, part $i$ finishes healing at step $\lceil\sum_{j\le i}D_j/W\rceil$. The highest-ranked damaged part heals as fast as alone; each lower-ranked part is delayed by the damage ranked above it. Under a sustained shortfall the repair parts lose access, so every finishing time rises.

Strict-rank repair is distinguishable from shared repair: under strict rank, the most important damaged part does not slow when others are damaged too.

## 4. Predictions, and how they separate the model from its neighbours

The model's predictions fall into two layers. **Layer 1** holds for any feedback loop with a finite stock: the record is flat while a buffer is drawn (G1), the break comes at a set depletion, and a larger buffer gives a longer silence. Confirming layer 1 says little about the model. **Layer 2** needs selection or design: the order of loss, switches, the order of recovery, repair competition. Table 2 lists the critical and supporting predictions; the full list, with status, is Supplement S4.

**Table 2. Main predictions.**

| No. | Prediction | Derived from | Status |
|---|---|---|---|
| G1 | The record stays near normal while lower parts and stores move | Prop. 2 | Natural observation: consistent; H1 check not consistent (low weight) |
| G2 | Lower-ranked parts lose access first, in ascending rank | Prop. 4 | Natural observation: consistent |
| G3 | Under proportional release, a faster shortfall leaves more store unused at the break | Prop. 3 | Untested |
| G8 | Rate decides harm; a scar needs speed and depth | Prop. 6 | Compatible; untested |
| G12 | Recovery from small knocks slows before the break where release headroom shrinks | Section 3; Supplement S1 | **Failed its first held-out test (half weight)** |
| G18 | Parts sharing a loaded dependency move together before the break; parts sharing only rank do not | Section 3.3 | Untested |
| G20 | Failure with willing receivers supplied means a cut or constricted link, or outside damage | Prop. 7 | Untested |
| G23(b) | Under strict-rank repair, the highest-ranked damaged part heals as fast as alone | Prop. 11 | Untested |
| G24 | Cascades and steals along substitutes where flow divides by physics, even with spare capacity | Prop. 8 | Known in power systems; untested as a cross-domain prediction |
| G25 | The order of loss is predicted by properties of access documented beforehand | Props. 4, 5 | **Supported at half weight in its first held-out test;** the scarcity version not supported |
| G26 | Stores refill only to a critical fractile while parts still bind | Prop. 10 | Untested |

**What the model predicts that neighbouring theories do not state.** Table 3 lists results that follow in the model but are not stated in the neighbouring theories as we have read them. Silence is not contradiction: the entries mark where the model makes a claim those theories do not make, and where a test can tell them apart.

**Table 3. Results not stated in neighbouring theories.**

| Result | DEB | Selfish Brain | Allostasis and allostatic load | Control theory |
|---|---|---|---|---|
| Scarcity load is relocated; gating creates and removes load (Prop. 1) | Conserves mass and energy; no ledger of unmet requirement | Build-ups in front of bottlenecks; no ledger across many parts | Hidden load, in words | No resource ledger |
| The record carries no information inside the silence region (Prop. 2) | Not stated | Brain held while body loses, two compartments | Stated in words | Not stated as a shortfall budget |
| Store left at the break rises with the rate of shortfall (Prop. 3) | Gives the release form; not the break | Not stated | Not stated | Not stated |
| Rank under saturable uptake from affinity, capacity and requirement (Prop. 5) | Not stated across parts | Access by insulin dependence, two compartments | Not stated | Not stated |
| Scar threshold in speed and depth (Prop. 6) | No unit loss or scar; damage irreparable | Not stated | Wear, in words | Not stated |
| Failure with receivers supplied implies a cut or narrowed link, or damage (Prop. 7) | Not stated | Not stated | Not stated | Not stated |
| Physical against chosen rerouting (Prop. 8) | Not stated | Not stated | Not stated | Known in power-systems engineering; not stated across domains |
| Repair served strictly by rank (Prop. 11) | No repair allocation | Not stated | Repair squeezed, in words | Not stated |

The sharpest discriminating tests are these:
- **Relocation:** in a resource-short system, a matching deficit should follow any correction that adds no resource.
- **The order of loss from access** (G25) in systems the model was not built on.
- **The scar threshold:** harm needs speed and depth together.
- **Strict-rank repair** (G23 b).

## 5. Tests so far

### 5.1 Held-out tests

Both tests were pre-registered before any outcome data were opened. Each computation was replicated by a second analyst (a language model working from the same files), and each verdict was given blind by a separate model against fixed adjudication rules. Records are in Supplement S5.

**H1: warning before decompensation in surgical blood loss (G12).**
- **Data:** VitalDB, an open database of high-resolution intraoperative recordings (Lee et al. 2022).
- **Prediction:** before falls in arterial pressure in cases with high blood loss, recovery from small fluctuations should slow. This was measured as a rise in the lag-1 autocorrelation of mean arterial pressure, against controls from the same case.
- **Cohorts:** the primary cohort (no fluid boluses) had no qualifying high-loss cases. The fallback cohort, with a loss threshold of 15% of estimated blood volume, gave 25 high-loss and 42 low-loss cases, analysed at half weight.
- **Result:** the median excess rise was −0.072 (one-sided p = 0.48), and high-loss cases did not exceed low-loss ones (p = 0.78). **G12 failed,** at half weight, with two qualifications:
  - the test is runnable only under the pre-data reading of missing 10-second bins;
  - the step-down of the loss threshold inside the fallback cohort was fixed in code before the data were opened, but not stated in the pre-registration.
- **G1 check (low weight):** pressure stayed within 20% of baseline while haemoglobin fell in 10.7% of 75 cases, against a pre-stated "more than half". Not consistent.
- **Reading under the model's standing rule:** the first candidate for revision is the mapping (the store's release profile under anaesthesia, where an anaesthetist acts as an outside loop holding pressure), not a new mechanism. One failure at half weight does not remove G12. Any explanation must name a specific fault and be tested in advance.

**PT1: order of loss from documented access in English local government (G25).**
- **Data:** single-tier councils in England, 2014-15 to 2019-20: 121 councils and 93 spending lines.
- **Access property:** each line was classified **blind**, before any spending data were opened, by whether a statutory duty attaches to it: class A, a duty; class B, a duty of uncertain level; class C, discretionary.
- **Primary question (fixed against dynamic priority): inconclusive** at full weight. Projected client growth published before each budget showed no detectable effect on which lines were protected (β = 0.05; 95% interval −0.75 to 0.86), but the interval includes the smallest effect set in advance as meaningful (0.25).
- **G25: supported, at half weight** (the broad pattern was known in advance). Within a council and year, real spending per head on class A lines grew about 4.6 percentage points a year faster than on class C lines (one-sided p = 2×10⁻¹¹). Class B was not distinguishable from class C, and that step fails its ordering when London is excluded.
- **G25-C: not supported, at half weight.** The scarcity version, that the gap widens where funding fell more, failed: the interaction was 0.22 (SE 0.25).

This is the model's first application outside bodies, and its first held-out support, for order of loss only.

### 5.2 Natural-system observations

Before the held-out tests, the model was checked against published findings in several natural systems, with predictions written down before the sources were opened. These checks are **not tests**: the model was partly built from the same physiology, some outcomes were known in advance, and sources were often read through summaries. We report them as compatible observations (Table 4; full records in Supplement S6).

**Table 4. Natural-system observations (compatible, not diagnostic).**

| Feature | Blood loss | Plants in drought |
|---|---|---|
| Record held while load rises | Arterial pressure well maintained while cardiac output falls (Evans et al. 2001); vital signs stable in early bleeding while the compensatory reserve falls (Convertino et al. 2016) | Changes in foliage colour lag hydraulic failure, best predicting trees already dead rather than dying (loblolly pine saplings; Hammond et al. 2019) |
| Lower priority pays first | Splanchnic vasoconstriction the dominant compensation in a model calibrated to 35 adults under lower-body negative pressure (Bergauer et al. 2026); renal resistance rising before carotid in a model calibrated to 43 swine (Sadid et al. 2026, preprint) | Not used here: the leaves-first ordering is contested (Section 6) |
| Buffer behaves as a stock | Blood volume removed at a 30 mmHg fall in mean pressure: 27.0 ± 4.2% at about 0.4% of blood volume a minute against 27.3 ± 3.2% at about 2% a minute (mean ± SE; 8 sheep, crossover; Scully et al. 2016) | Saplings died at the same loss of conductivity under fast and slow drought, with species-specific thresholds (about 95% and 45%; Dai, Wang and Wan 2018) |
| Break at a set depletion | Decompensation (sympathetic withdrawal) once cardiac output falls to 50 to 60% of rest, about 30% blood loss (Evans et al. 2001) | About 80% loss of conductivity in loblolly pine saplings (Hammond et al. 2019) |

The sheep result fits full release, or a store with turnover high relative to the gap (Proposition 3). It is an observation about the release profile in that setting, not a test.

## 6. Scope, limits and failures

**Scope.**
- **Persistence is a viability constraint, not something maximised.** The governor keeps the system within the states compatible with its continued existence; within that envelope the system pursues its purposes.
- **Terminal reproductive programmes are out of scope** (semelparous salmon, some marsupial males, monocarpic plants). There, individual persistence stops being the protected constraint. The model should work before the reproductive switch and fail after it.
- **The model is not a theory of action selection.**
- **Boundaries, protected levels and the classification of components are fixed before outcomes** and are not redrawn after a counterexample.

**Limits of the formal results.**
- The propositions hold for the reduced form, not for a general network. Where several complementary resources bind together and their orders conflict, ordinal ranks do not decide the outcome (Supplement S1): the network must be mapped explicitly.
- The order of loss is assumed fixed. **Whether it is fixed or reverses with conditions is open:** PT1 was inconclusive. A valid test needs two recipients competing for the same scarce resource at the same time, with the governor's mode held constant.
- The functional forms not taken from DEB (switch-off and failure rates, the scar rule) are modelling choices. No parameter has been estimated from data.

**Failures and findings against the model.**
- **G12 failed** its first held-out test, at half weight (Section 5.1).
- **G25-C was not supported.**
- **PT1 was inconclusive.**
- **Findings logged against the model, not yet weighed:**
  - autopsies after prolonged inanition (Krieger 1921, as cited by Peters and Langemann 2009) found heart, liver, pancreas and kidney all losing about 40% of their mass while the brain lost under 2%, with no order among the organs below the brain. Whether this conflicts with the model depends on the order fixed for energy and protein at a starvation mapping;
  - in 12 Australian tree species, the predicted leaves-before-stems order of hydraulic failure (vulnerability segmentation) was "universally absent or negative" (Peters and Choat 2025);
  - in mature spruce, an earlier drought eased physiological stress in a later one (Hikino et al. 2026), where a stressed start should fare worse.

  Details and weights are in Supplement S7.
- **Independence is partial.** The model was built from the same physiology its neighbours describe. Its natural-system observations support it only as compatibility.

## 7. Discussion

**Mapping a system.** The model's main methodological claim is that the order of loss can be fixed before outcomes. Mapping a system (Supplement S9 in full) means fixing, before any outcome data are opened:
- the boundary, the protected level and the viable set, and whether outside support counts;
- the resources, whether they are complementary or substitutable, their stores and release profiles;
- the governor's levels and what it acts through;
- each part's units, rank for each resource from documented properties of access, requirements, reference allocation, rebuild time and template limit;
- the repair network;
- the pathways, and whether flow among routes divides by physics or by choice;
- any modes and gates invoked for access-limited load, each documented independently;
- the clock.

Anything chosen with the expected outcome in mind is declared fitted. **Where access is by saturable uptake, the rank is the order of adequacy thresholds** (Proposition 5), computable from measured affinity, capacity and requirement.

**What would count against the model:**
- in a system resource-short by its own mapping, an intervention that restores one part's supply without adding resource and without a matching deficit appearing elsewhere;
- in a held-out system, an order of loss that contradicts the order fixed in advance from documented access (G25);
- harm without speed: units lost or scarred under a fall in renewal slower than the documented switch-off rate (Proposition 6);
- an ordinary system, in ordinary conditions, whose own regulation destroys recoverable viability with no higher-level system being protected.

**Next tests:**
- a cleaner test of the order of loss from access, in a system the authors did not know in advance;
- a test of the release profile in blood loss, with the failure of G12 named as a mapping fault in advance;
- a test of fixed against dynamic priority with the mode held constant;
- tests of the scar threshold and of strict-rank repair.

A proposed extension treats components with their own access loops (a tumour; a person in an institution) as nested systems; its first test, whether a tumour that only drains a host matches a host whose supply is cut by the same amount, is future work.

## Appendix A. Proofs of the main-text propositions

**Proposition 1.** Conservation within the step gives $U+I+\sum_sd_s=\sum_ia_i+R_{\text{unused}}$. With $\ell_i=[q^0_i-a_i]_+$, $\sum_i(q^0_i-a_i)=\sum_i\ell_i-X$. Hence $\sum_i\ell_i=\sum_iq^0_i-U-I-\sum_sd_s+R_{\text{unused}}+X$, the identity stated. Regime 1: $R_{\text{unused}}=0$ and $X=0$, so the total contains no access term. Regime 2: $X=0$ and $R_{\text{unused}}$ equals the resource the gate leaves unused. ∎

**Proposition 2.** The top draws first, then all basal maintenance, then support parts. So the top is met if and only if $S\ge N$, and basal maintenance and supports if and only if $S\ge N+B+P$. The top's work next step falls only through its own units (impossible while it is met) or through dependency on supports (excluded when they are met). Since $\sum_iq^0_i=N+B+P+D_4$, $S\ge N+B+P$ is equivalent to $\Gamma\le\sum_sd_s+D_4$; without dependency, $M=D_4+P+B$. ∎

**Proposition 3.** While $kL\ge\Gamma$ the store releases the whole gap, so $L$ falls by $\Gamma$ per step. Once $kL<\Gamma$ the store releases $kL$, $L$ falls by the factor $(1-k)$ per step, and $\Gamma-kL$ falls below the top. By Proposition 2 the record breaks at the first step with $\Gamma-kL>M$, that is $L<(\Gamma-M)/k$; in discrete time the level at the break lies in $((1-k)L^\ast,L^\ast]$. Under full release with rate at least $\Gamma$, the store carries the whole gap until empty, independent of $\Gamma$. ∎

**Proposition 4.** Draws are sequential within a phase: a part is short only if the flow is exhausted at its turn, so every later part draws nothing. Phases complete in order. ∎

**Proposition 5.** $V_iC/(K_i+C)\ge q^0_i$ rearranges to $C\ge K_iq^0_i/(V_i-q^0_i)=C^\ast_i$. The pool level falls monotonically with supply, so parts cross their thresholds in descending order of $C^\ast_i$. With $r_i$ equal, $C^\ast_i\propto K_i$. With thresholds far apart, at most one part is near its threshold at any $C$ (strict); otherwise several are short together (shared). ∎

**Proposition 6.** Over the episode, switched-off and lost units together number $\Delta$. During the decline, which lasts at least $\Delta/\varphi$ steps, the excess $x$ of active over renewable units satisfies $x_{t+1}=(x_t-\theta K)(1-1/\tau_f)+\varphi\ge\varphi>\theta K$, so $\theta K$ units are switched off each step and at least $\theta K\Delta/\varphi$ in all: hence the upper bound. At the end of the decline the excess is at most $\theta K+\tau_f(\varphi-\theta K)$, and no more can be switched off in the tail: hence the lower bound. If $\varphi\le\theta K$, every unit not renewed is switched off within the step. ∎

**Proposition 7.** If an ordinary part still draws for work, or a store has headroom, then $S\ge N+B+P$ (Proposition 2), so the flow could meet the top and its supports. If they are short, another bound binds: the pathway, whose capacity is the minimum cut, or their own capacity, which falls only through supply (excluded) or damage. ∎

**Proposition 8.** Placing the lost flow into surviving headroom succeeds exactly when the headroom suffices; in a general network this is max-flow min-cut. By example: routes with capacities 10, 4 and 10 carry 5, 3.9 and 5. Losing the first leaves headroom 5.1 for flow 5, but a split in proportion to capacity sends about 1.43 to the second route, which then carries 5.33 against capacity 4. At fixed supply, conservation at a junction means flow leaving one branch through a collateral is subtracted from it. ∎

**Proposition 9.** Under the first condition, an access setting exists that meets the top and all basal maintenance (Proposition 2), so no further units are lost (Propositions 4 and 6). Under the others, the repair network can rebuild each needed part at its rebuild rate from what is left in the flow. The system therefore reaches the viable set in finite time and can stay there: membership of the capture basin. ∎

**Proposition 10.** The intake is a support part, served in phase 3. A store's marginal value $c_S\rho(1-F(L))$ is non-increasing in $L$; greedy allocation by marginal value stops refilling where it falls to $V$, the stated quantile. Greedy allocation is optimal for separable concave value (Ibaraki and Katoh 1988). ∎

**Proposition 11.** Under strict priority, cumulative repair work after $t$ steps is $tW$, applied to damage in rank order; part $i$ is complete when $tW\ge\sum_{j\le i}D_j$. ∎

## References

- Ames BN (2006). Low micronutrient intake may accelerate the degenerative diseases of aging through allocation of scarce micronutrients by triage. *PNAS* 103:17589-17594. doi:10.1073/pnas.0608757103
- Aubin J-P (1991). *Viability Theory*. Birkhäuser, Boston.
- Bergauer A, Urevc J, Halilovič M, Batzel J, Pivec V, Goswami N (2026). Modeling sex-dependent cardiovascular responses to lower body negative pressure. *Am J Physiol Heart Circ Physiol* 331:H240-H259. doi:10.1152/ajpheart.00258.2026
- Bobba-Alves N, Juster R-P, Picard M (2022). The energetic cost of allostasis and allostatic load. *Psychoneuroendocrinology* 146:105951. doi:10.1016/j.psyneuen.2022.105951
- Buttgereit F, Brand MD (1995). A hierarchy of ATP-consuming processes in mammalian cells. *Biochem J* 312:163-167. doi:10.1042/bj3120163
- Convertino VA, Hinojosa-Laborde C, Muniz GW, Carter R III (2016). Integrated compensatory responses in a human model of hemorrhage. *J Vis Exp* 117:54737. doi:10.3791/54737
- Dai Y, Wang L, Wan X (2018). Relative contributions of hydraulic dysfunction and carbohydrate depletion during tree mortality caused by drought. *AoB Plants* 10:plx069. doi:10.1093/aobpla/plx069
- Evans RG, Ventura S, Dampney RA, Ludbrook J (2001). Neural mechanisms in the cardiovascular responses to acute central hypovolaemia. *Clin Exp Pharmacol Physiol* 28:479-487. doi:10.1046/j.1440-1681.2001.03473.x
- Ford LR, Fulkerson DR (1956). Maximal flow through a network. *Can J Math* 8:399-404. doi:10.4153/CJM-1956-045-5
- Göbel B, Langemann D (2011). Systemic investigation of a brain-centered model of the human energy metabolism. *Theory Biosci* 130:5-18. doi:10.1007/s12064-010-0105-9
- Grossman YL, DeJong TM (1994). PEACH: a simulation model of reproductive and vegetative growth in peach trees. *Tree Physiol* 14:329-345. doi:10.1093/treephys/14.4.329
- Hammond WM, Yu K, Wilson LA, Will RE, Anderegg WRL, Adams HD (2019). Dead or dying? Quantifying the point of no return from hydraulic failure in drought-induced tree mortality. *New Phytol* 223:1834-1843. doi:10.1111/nph.15922
- Hikino K, Hesse BD, Gebhardt T, Hafner BD, Buchhart C, et al. (2026). Drought legacy in mature spruce alleviates physiological stress during recurrent drought. *Plant Biol* 28:637-648. doi:10.1111/plb.70039
- Hochachka PW, Buck LT, Doll CJ, Land SC (1996). Unifying theory of hypoxia tolerance: molecular/metabolic defense and rescue mechanisms for surviving oxygen lack. *PNAS* 93:9493-9498. doi:10.1073/pnas.93.18.9493
- Ibaraki T, Katoh N (1988). *Resource Allocation Problems: Algorithmic Approaches*. MIT Press, Cambridge, MA.
- Kooijman SALM (2010). *Dynamic Energy Budget Theory for Metabolic Organisation*, 3rd edn. Cambridge University Press. doi:10.1017/CBO9780511805400
- Krieger M (1921). As cited in Peters and Langemann (2009); original not read.
- Lee H-C, Park Y, Yoon SB, Yang SM, Park D, Jung C-W (2022). VitalDB, a high-fidelity multi-parameter vital signs database in surgical patients. *Sci Data* 9:279. doi:10.1038/s41597-022-01411-5
- Marcelis LFM, Heuvelink E (2007). Concepts of modelling carbon allocation among plant organs. In: Vos J, Marcelis LFM, de Visser PHB, Struik PC, Evers JB (eds) *Functional-Structural Plant Modelling in Crop Production*. Springer, pp 103-111. doi:10.1007/1-4020-6034-3_9
- Minchin PEH, Thorpe MR, Farrar JF (1993). A simple mechanistic model of phloem transport which explains sink priority. *J Exp Bot* 44:947-955. doi:10.1093/jxb/44.5.947
- Noakes TD (2012). Fatigue is a brain-derived emotion that regulates the exercise behavior to ensure the protection of whole body homeostasis. *Front Physiol* 3:82. doi:10.3389/fphys.2012.00082
- Peters A, Schweiger U, Pellerin L, Hubold C, Oltmanns KM, Conrad M, Schultes B, Born J, Fehm HL (2004). The selfish brain: competition for energy resources. *Neurosci Biobehav Rev* 28:143-180. doi:10.1016/j.neubiorev.2004.03.002
- Peters JMR, Choat B (2025). Out on a limb: testing the hydraulic vulnerability segmentation hypothesis in trees across multiple ecosystems. *Plant Cell Environ* 48:2162-2177. doi:10.1111/pce.15249
- Peters A, Langemann D (2009). Build-ups in the supply chain of the brain: on the neuroenergetic cause of obesity and type 2 diabetes mellitus. *Front Neuroenergetics* 1:2. doi:10.3389/neuro.14.002.2009
- Powers WT (1973). Feedback: beyond behaviorism. *Science* 179:351-356. doi:10.1126/science.179.4071.351
- Sadid S, Eden MJ, Mobin FU, Gomez MK, Januszko S, et al. (2026). Calibration of a closed-loop model of porcine aortic hemodynamics during hemorrhage. *bioRxiv* preprint. doi:10.64898/2026.01.30.702699
- Scully CG, Daluwatte C, Marques NR, Khan M, Salter M, Wolf J, et al. (2016). Effect of hemorrhage rate on early hemodynamic responses in conscious sheep. *Physiol Rep* 4:e12739. doi:10.14814/phy2.12739
- Shephard RJ (2009). Is it time to retire the "central governor"? *Sports Med* 39:709-721. doi:10.2165/11315130-000000000-00000
- Sherbrooke CC (1968). METRIC: a multi-echelon technique for recoverable item control. *Oper Res* 16:122-141. doi:10.1287/opre.16.1.122
- Sprengell M, Kubera B, Peters A (2021). Brain more resistant to energy restriction than body: a systematic review. *Front Neurosci* 15:639617. doi:10.3389/fnins.2021.639617
- Sterling P (2012). Allostasis: a model of predictive regulation. *Physiol Behav* 106:5-15. doi:10.1016/j.physbeh.2011.06.004
- Straub RH (2014). Insulin resistance, selfish brain, and selfish immune system: an evolutionarily positively selected program used in chronic inflammatory diseases. *Arthritis Res Ther* 16(Suppl 2):S4. doi:10.1186/ar4688
