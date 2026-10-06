# The tier-queue model in mathematical form (v0.16, 6 October 2026)

**Status:** theorising (phase 3).

**What this is.** The canonical model (TIER_QUEUE_MODEL_v0.16.md) as one set of equations, in the order a step would apply them. **It is the target for the engine, not a description of it.** The engine (theory/sim/tq_core.py) still runs v0.15 rules, written up in theory/tier_queue_math_v0.15.md, which stays the reference for every simulation result to date (TQ5 to TQ9).

**Labels.** The functional forms are choices, and every parameter is illustrative. Where a form is new in v0.16 it is labelled **new**. Where it is carried over from v0.15, the engine constant is given in brackets.

**What changed from v0.15.**
- Routing is written in supply and demand.
- Deferral and debt are replaced by a per-part condition (the container), which leaks under load and refills once the load stops.
- Scars follow loss of the template.
- Economising lowers demand and capacity together, with no deferral.
- Room to take resources from other parts is finite, which allows exhaustion; severance is a cut link.

## 0. Symbols

| Symbol | Meaning |
|---|---|
| $d_i$ | demand on part *i* (work asked of it), normal; $d_i^{\text{run}}$ after economising |
| $c_i$, $\kappa_i$, $c_i^{\text{eff}}$ | nominal (structural) capacity, ceiling, current effective capacity |
| $u_i$ | supply reaching part *i* (resources, in work units) **new** |
| $w_i$ | work done by part *i* **new** |
| $\Lambda_i$ | load at part *i*: demand it cannot meet **new** |
| $L_i$ | load ratio: demand over what the part can do now, $d_i^{\text{run}}/\min(c_i^{\text{eff}},u_i)$ |
| $H_i$ | condition: the part's container, from 1 (full) to 0 (empty) **new** |
| $\Theta_i$ | template: the share of the part whose like-for-like rebuild is still possible, from 1 to 0 **new** |
| $Q_i$ | dose: accumulated load ratio above 1 in the current episode **new** |
| $f_i$ | demand floor (minimum running cost) **new** |
| $R$, $R^0_{\max}$, $R_{\max}$ | reserve level, base size, current size |
| $v_i$, $p_i$, $q_i$ | value, spending price, resupply priority |
| $h_i$, $T$, $\tau$ | rebuild time, remaining horizon, rest of the episode |
| $\rho_s$ | expected shortfall (the reserve's value) |
| $\epsilon$ | economising: the share by which working parts' demand and deployed capacity are lowered |

## 1. The ledger (conservation, in supply and demand)

**New.** Two balances hold for any currency that obeys one.

**Demand:**

$$\sum_i d_i(t)\;=\;\sum_i w_i(t)\;+\;\sum_i \Lambda_i(t)\;+\;b(t)$$

Demand is met by work done, held as load at a part, or sent across the boundary ($b$: shed commitments, exported load).

**Supply:**

$$U(t)+r(t)\;=\;\sum_i u_i(t)\;+\;\dot R^{+}(t)$$

Supply coming in through the intake ($U$), plus reserve drawn ($r$), is shared out to parts or banked in the reserve ($\dot R^+$).

**Work is local:**

$$w_i=\min\big(d_i^{\text{run}},\;c_i^{\text{eff}},\;u_i\big)$$

**Load arises in two ways:**

$$\Lambda_i=\big[d_i^{\text{run}}-\min(c_i^{\text{eff}},u_i)\big]_+$$

Either throughput is maxed ($c_i^{\text{eff}}<d_i^{\text{run}}$) or supply falls short ($u_i<d_i^{\text{run}}$). Nothing leaves the ledger except through work done or the boundary.

## 2. Capacity and condition

**Effective capacity** (compounding, with shared upstream supply):

$$c_i^{\text{eff}}\;=\;(1-\epsilon_i)\,\kappa_i\,c_i\,\big[1-\lambda\,(1-H_i)\big]\,\big[(1-\omega_i)+\omega_i\,s_{u(i)}\big]$$

- $\epsilon_i$ is the economising cut to deployed capacity (Section 6; zero for the top and non-bypassable links).
- $\lambda$ is the largest share of capacity that condition can take away (a choice, **new**; v0.15 used $\lambda_{\max}=0.5$).
- $s_{u(i)}$ is the served share of the part's upstream supply, measured against **normal** demand: $s_j=w_j/d_j$. Work a part does not do, for whatever reason, reaches its dependants.

**The container** (**new**):

$$\dot H_i=\begin{cases}-\alpha\,(L_i-1) & L_i>1\ \ \text{(the leak)}\\[2pt] +\min\!\Big(\dfrac{1}{h_i},\;\dfrac{\min(c_i^{\text{eff}},u_i)-d_i^{\text{run}}}{c_i}\Big)\,\Theta_i\,(1-H_i) & L_i\le1\ \ \text{(refilling)}\end{cases}$$

- While the part carries load ($L_i>1$), it deteriorates, and it cannot refill however much supply arrives.
- Once demand is back within what it can do, it refills from its own slack, no faster than its renewal rate ($1/h_i$), and only in the share whose template survives ($\Theta_i$).
- There is no repair pool: the only inflow is the part's own supply beyond its own demand.
- A part with no reserve is treated the same way.
- Fixed capital has $h_i\to\infty$, so its condition does not refill.

**Dose and the template** (**new**):

$$Q_i=\int_{\text{episode}}[L_i-1]_+\,dt,\qquad \Theta_i\leftarrow\Theta_i\,\Big[1-\big[\tfrac{Q_i-Q_i^\ast}{Q_i^\ast}\big]_+\Big]_+\ \text{also when } H_i=0$$

- The template survives until the dose passes a part-specific threshold $Q_i^\ast$, large for a robust template and near zero for fixed capital. After that it is lost in proportion to the excess.
- It is also lost when condition reaches zero: the part can no longer hold its own boundary.
- The form is a choice. The scan supports a dose (excess × time) and a template threshold (theory/deterioration_threshold_scan.md), not this particular shape.

**Compounding.** $L_i$ is measured against what the part can do now. That falls as $H_i$ falls, so a leak feeds itself (Section 10, B).

## 3. Value and priority

**Value** (a shadow price, $\partial W/\partial c_i$; carried over from v0.15):

$$v_i=\text{vital}_i\;b(\hat L_i),\qquad b(L)=\epsilon_0+(1-\epsilon_0)\,\min\!\Big(1,\Big[\tfrac{L-L_0}{1-L_0}\Big]_+\Big)$$

[$\epsilon_0=0.05$, $L_0=0.7$].
- **Non-bypassable links** (central control, transporters, series links) have $b\equiv1$.
- An intake with nothing to take in has value scaled by its supply.
- $\hat L_i$ is what control sees through state signals with gain $g_i$, as in v0.15, measured against **normal** demand.

**Spending price** (who pays first: ascending $p_i$):

$$p_i=v_i\,s_i\,\min(\tau+h_i,\;T),\qquad s_i=1-\lambda^{-1}\big(1-c_i^{\text{eff}}/\kappa_ic_i\big)$$

- $s_i$ is the share of capacity still at stake; a part with nothing left to lose is the fuse.
- $\tau$ is the episode's length so far, $h_i$ the rebuild time, and $T$ the remaining horizon or the next task's deadline.
- The top (the held output) is defended by definition.

**Resupply priority** (descending $q_i=v_i/k_i$, with the reserve competing at value $\rho_s$). This is the order in which returning supply reaches parts (Section 7). It is not a separate repair budget.

**Optimality.** Ascending $p_i$ is the best policy only for a concave, separable objective (water-filling). $s_i$ handles saturating damage (the fuse), and the non-bypassable rule handles cliffs. Increasing returns to an output (semelparity) are not represented.

## 4. Routing (supply and demand)

**New.** Each step:

1. **Supply is shared out by priority.** Incoming supply $U$ goes to parts in descending price, each up to its need $\min(d_i^{\text{run}},c_i^{\text{eff}})$. What is left banks in the reserve.
2. **A short part draws on the reserve.** Part *i* with $u_i<\min(d_i^{\text{run}},c_i^{\text{eff}})$ draws $r_i=\min(\text{gap},\rho(R),R)$, with $\rho(R)=\rho_0\min\!\big(1,\tfrac{R}{k_RR_{\max}}\big)$ (the knee; carried over).
3. **Then it takes resources from lower-priority parts,** lowest price first. From part *j* it takes
   $$a_{ij}\le u_j,$$
   first from *j*'s slack $[u_j-\min(d_j^{\text{run}},c_j^{\text{eff}})]_+$, which costs *j* nothing, then beyond it. Beyond its slack, *j* can no longer meet its own demand: $\Lambda_j>0$, and *j*'s container leaks. Labelled load can be refused by a part already carrying load; unlabelled load cannot.
4. **A maxed part backs load up.** A part whose throughput is maxed ($c_i^{\text{eff}}<d_i^{\text{run}}$) cannot use more supply. A share $\lambda_{ij}$ of its unprocessed excess backs up along its dependency as demand on the part that feeds it: $d_j\leftarrow d_j+\lambda_{ij}[d_i^{\text{run}}-c_i^{\text{eff}}]_+$. This is the loop in TQ9.
5. **What is left** stays at the part as load (its container leaks), or crosses the boundary.

**Reserves and throughput** (James, 6 October 2026). A reserve supplies resources.
- Within its ceiling $c_i^{	ext{eff}}$, a part's work tracks its demand whenever supply, including the reserve, covers it: $w_i=\min(d_i^{	ext{run}},c_i^{	ext{eff}},u_i)$.
- "Sustained capacity" is not a separate limit. It is the throughput that ongoing supply supports without the reserve. A reserve lifts work above that, never above the ceiling.
- Where the binding limit is removing a by-product (a processor's heat), the removal rate plays the part of supply and the heat sink the part of a reserve.
- There is no throughput target: demand is whatever the governor needs to hold its level, so work changes continuously.

**Room is finite: exhaustion.** Taking stops at $u_j=0$. When the reserve is empty and every lower-priority part's supply has been taken, there is nowhere left. Load then falls on the top (the record breaks), and the part whose condition and template run out first is the one priority spent (the fuse).

**Severance.** A cut link sets the supply it carried to zero ($\omega$-edge or series link: $u_j=0$ downstream), whatever spare exists elsewhere. If the link is non-bypassable control, step 3 stops following priority and supply is spread by capacity (control failure).

## 5. The reserve

Carried over from v0.15.

**Value: the expected shortfall.**

$$\dot\rho_s=\frac{\mathbf 1\!\big[\textstyle\sum_i d_i>\sum_i \min(c_i^{\text{eff}},u_i^{\text{max}})\big]-\rho_s}{\tau_\rho}\qquad[\tau_\rho=30]$$

**Size: frequency and remembered depth.**

$$X_R\leftarrow\max(X_R,\,D_e-R^0_{\max}),\quad \dot X_R=-\frac{X_R}{\tau_m},\quad R_{\max}=\max\!\Big(R^0_{\max}(1+\gamma\rho_s),\;R^0_{\max}+\min(X_R,R^0_{\max})\Big)$$

[$\gamma=1$, $\tau_m=100$]. **Frequency sets the order; depth sets the size.**

## 6. Economising (the switch's graded action)

**The driver** is carried over: the gap between the shortfall still expected and the reserve.

$$g=\frac{\hat D-R}{R^0_{\max}},\qquad x=\min\!\Big(1,\frac{[g-g_0]_+}{g_1-g_0}\Big),\qquad \hat D=A(t)+\frac{D_e}{\ell}\,[\ell^\ast-\ell]_+$$

[$g_0=-0.5$, $g_1=-0.1$].
- $A(t)$ is a need known in advance, which requires a signal reaching control.
- $\ell^\ast$ is the typical episode length if the episode is shorter than that, otherwise twice the length so far.

**Response** (**new**: demand and capacity together, down to the floor, no deferral):

$$\dot\epsilon=\frac{\epsilon_{\max}S(x)-\epsilon}{\tau_\epsilon},\quad S(x)=x^2(3-2x),\qquad d_i^{\text{run}}=\max\big(f_i,(1-\epsilon)d_i\big),\quad \epsilon_i=1-\frac{d_i^{\text{run}}}{d_i}$$

[$\epsilon_{\max}=0.3$, $\tau_\epsilon=5$], for $i\neq$ top and non-bypassable links.

- **Demand and capacity fall together.** Each part's deployed capacity is lowered by the same share as its demand (Section 2), so its supply need falls and supply can cover it: no leak.
- **What is cut is shed** across the boundary: $b\mathrel{+}=\epsilon_i d_i$. Dependants see the cut through $s_j=w_j/d_j$.
- **Reversal is full.** When $\epsilon$ returns to zero, deployed capacity returns at the part's flex rate, which is fast. Where structure was remodelled, it returns at the rebuild rate with the template intact.
- **No deterioration, no debt.**

## 7. Recovery

**New: no pool.**
- Each step, supply is shared out in descending $q_i$, with the reserve competing at value $\rho_s$ (it waits while any part of higher value is still refilling).
- Each part's container then refills from its own slack (Section 2).
- A part refills only once its own leak has stopped ($L_i\le1$).

**The orders after acute and chronic load (G10) are to be rechecked under this rule.** In v0.15 they came from pooled slack.

## 8. What a part becomes after an episode

An episode ends after a calm spell with no part carrying load.

- **Growth** (carried over). Conditions: acute, coupled, renewable, template intact, peak dose at least the growth threshold and below the template threshold. Effect: $\kappa_i\leftarrow\min(\kappa_{\max},\kappa_i(1+g\,v))$ [$g=0.10$, $\kappa_{\max}=1.3$].
- **Protection, set by the peak** (carried over): $X_i\leftarrow\max(X_i,\,D_i^\ast-\kappa_ic_i)$, fading as $\dot X_i=-X_i/\tau_m$. The leak in Section 2 starts above $\max(c_i^{\text{eff}},\kappa_ic_i+X_i)$ rather than $c_i^{\text{eff}}$.
- **Scar** (**new**: template loss, not exposure stage): the share of lost capacity whose template is gone cannot refill and is patched,
  $$\kappa_i\leftarrow\kappa_i\Big[1-\lambda\,(1-H_i^{\min})\,(1-\Theta_i)\Big]$$
  with $H_i^{\min}$ the lowest condition in the episode. Protection is reset. A scar that cuts demand sets a lasting demand cut.
- **Loss** (fixed capital, $\Theta_i\approx0$): lost capacity is kept.
- **Suppression and remodelling** are not outcomes: they are reversed in full.

## 9. Read-outs

- **Record:** $y(t)=w_{\text{top}}/d_{\text{top}}$, a held output.
- **Record dynamics (G12).** A knock $k$ is restored at the release left, $\rho(R)-r$, so $t_{\text{rec}}\approx k/\rho(R)$. This equals $k/\rho_0$ above the knee and grows as $1/R$ below it. Simulation result under v0.15 rules (TQ9); unchanged in form.
- **State signals:** $L_i$, $H_i$, $c_i^{\text{eff}}/c_i$, $\Lambda_i$, $R/R_{\max}$, $\epsilon$, judged against the system's own phase reference.
- **Co-movement (G18):** with $Z_i=a_i\Lambda+\varepsilon_i$ for parts sharing an input carrying $\Lambda$,
  $$\operatorname{corr}(Z_i,Z_j)=\frac{a_ia_j\operatorname{Var}\Lambda}{\sqrt{(a_i^2\operatorname{Var}\Lambda+\sigma_i^2)(a_j^2\operatorname{Var}\Lambda+\sigma_j^2)}}$$
  Simulation result under v0.15 rules (TQ9).
- **Three kinds of capacity loss (G19)** (**new**), separated by timing and by $\Theta$:

  | Kind | What changes | Timing | Recovery |
  |---|---|---|---|
  | Economising | $\epsilon_i>0$, with $\Lambda_i=0$ throughout | Capacity falls with or before demand | Full at the flex or rebuild rate |
  | Deterioration | $H_i<1$ with $\Theta_i=1$ | Capacity falls after $L_i>1$ | Full once $L_i\le1$, in a time set by the dose |
  | Scar | $\Theta_i<1$ | | Lasting fall in $\kappa_i$ |
- **Felicity read-out** (carried over): $D_{\text{on}}\ge D^\ast$ protected or grown; $\kappa c\le D_{\text{on}}<D^\ast$ protection fading; $D_{\text{on}}<\kappa c$ scarred.

## 10. Results that follow

**A. How long the record stays flat.** With the top short of supply by $G_0$, the record holds while

$$G_0\le\rho(R)+\sum_{j\,\text{below}}u_j$$

That is, while the reserve's release and the supply of lower-priority parts can cover it. While the reserve carries the gap $G$ left after lower parts' slack is taken, the break time is $T^\ast\approx R_0/G$, independent of the rate at which the shortfall arrives (G3). Taking beyond lower parts' slack lengthens the silence but makes their containers leak, so their capacity falls and the break, when it comes, is sharper. Economising lowers lower parts' needs, which frees supply and lengthens the silence without any leak.

**B. Compounding.** For one part under constant demand above what it can do,
$$\dot H=-\alpha\Big(\frac{d}{c[1-\lambda(1-H)]}-1\Big),$$
which speeds up as $H$ falls: deterioration accelerates as it accumulates, until the template threshold or $H=0$.

**C. When recovery is possible.** A part refills only if its leak stops: $d_i^{\text{run}}\le\min(c_i^{\text{eff}},u_i)$. With demand close to capacity, a part that has begun to deteriorate cannot recover without relief (the opaque trap) unless economising lowers its demand below what it can do. The trap returns where load beyond capacity persists despite economising. After a scar, a part whose demand exceeds its lowered ceiling never refills unless its demand is cut.

**D. Growth needs coupling, slack and strain without economising** (G17). Economising lowers demand with capacity, so the part never reaches the strain growth needs.

**E. Three kinds of loss (G19).** Economising leaves $H$ and $\Theta$ untouched, deterioration lowers $H$ only, and a scar lowers $\Theta$. Recovery time is set by the flex rate, the dose and the renewal rate respectively. Whether loss is permanent is set by $\Theta$.

**F. Two routes to failure (G20).** Under exhaustion, a part fails only after every source the router can take from is at zero. A part that fails while lower-priority parts still hold supply implies a cut link.

## 11. What the formalisation does not settle

- **Functional forms:** the container's leak and refill, the template threshold and its loss, the S-curve, exponential fading. All are choices. The template law in particular is a placeholder for what the scan supports qualitatively.
- **Fitted values carried over:** the shortfall definition, the reserve's cap and memory, the economising settings, the first-time expectation ("as much again"), and all rates and thresholds. No parameter has been estimated from data. The deferred share is withdrawn.
- **Reserves and throughput:** settled (James, 6 October 2026; Section 4).
- **Not yet in the engine:** everything marked **new**; several shared reserves; an explicit objective (so increasing returns and semelparity are not represented).
