# The tier-queue model in mathematical form (v0.15, 5 October 2026)

**Status:** theorising (phase 3). This writes the canonical model (TIER_QUEUE_MODEL_v0.15.md) and its engine's computed mode (theory/sim/tq_core.py, `priority="computed"`, `adapt=True`) as one set of equations, in the order the engine applies them each step. Engine constants are given in brackets. The functional forms are choices; only the qualitative behaviour has been checked against natural systems, and every parameter is illustrative. The legacy fixed-priority engine (v0.4: fixed ranks, a 20-step chronic flag, a fixed recovery order) is written up in theory/tier_queue_math_v0.4.md, kept as history.

## 0. Symbols

| Symbol | Meaning |
|---|---|
| $d_i$ | demand on part *i* (work asked of it); $d_i^{\text{run}}$ after economising |
| $c_i$, $\kappa_i$, $c_i^{\text{eff}}$ | nominal capacity, ceiling, current effective capacity |
| $E_i$ | exposure (accumulated strain) of part *i* |
| $L_i$ | demand carried by *i* (its own plus any passed to it, less what it passed on) over $c_i^{\text{eff}}$ |
| $D_i$ | debt held by part *i* |
| $R$, $R^0_{\max}$, $R_{\max}$ | reserve level, base size, current size |
| $v_i$, $p_i$, $q_i$ | value, spending price, recovery priority |
| $h_i$, $T$, $\tau$ | rebuild time, remaining horizon, rest of the episode |
| $\rho_s$ | expected shortfall (the reserve's value) |
| $\epsilon$ | economising: share of working parts' running demand cut |
| $\phi_i$ | share of a part's economised demand that is deferred maintenance |

## 1. The ledger (conservation)

For any currency that obeys a balance, summed over parts:

$$\sum_i d_i(t) \;=\; \sum_i w_i(t) \;+\; r(t) \;+\; \sum_i \dot D_i(t) \;+\; b(t)$$

Demand equals work done, plus reserve drawn, plus debt added, plus load leaving across the boundary (including shed commitments). Nothing leaves except through work done or the boundary.

## 2. Capacity and exposure

**Effective capacity** (compounding, with shared upstream supply):

$$c_i^{\text{eff}} \;=\; \kappa_i\,c_i\,\big[1-\ell(E_i)\big]\,\big[(1-\omega_i)+\omega_i\,s_{u(i)}\big]$$

where $s_{u(i)}$ is the served share of the part's upstream supply and $\omega_i$ how strongly it depends on it.

**Loss and stages:**

$$\ell(E)=\begin{cases}0 & E<E_s\ \ \text{(optimal or coping)}\\ \lambda_s & E_s\le E<E_c\ \ \text{(protective slowing)}\\ \lambda_c+(\lambda_{\max}-\lambda_c)\min\!\big(1,\tfrac{E-E_c}{E_{\max}-E_c}\big) & E\ge E_c\ \ \text{(compromised)}\end{cases}$$

[$E_s=4$, $E_c=13$, $\lambda_s=0.10$, $\lambda_c=0.13$, $\lambda_{\max}=0.50$, $E_{\max}=78$; bands from James's vacancy debt method.]

**Exposure**, felt against current capacity, above any protected level:

$$\frac{dE_i}{dt}=\frac{(1-\pi_i)\,\sigma(E_i)\,\big[D_i^{\text{car}}-\max(c_i^{\text{eff}},D_i^{k})\big]_+/c_i^{\text{eff}}\;-\;\beta_i\,\psi\,[1-L_i]_+}{u}$$

- $D_i^{\text{car}}$: demand carried by *i*; $D_i^{k}$: the protected level after a recovered episode (Section 8); with no protection it equals $c_i^{\text{eff}}$ and the strain term is $[L_i-1]_+$;
- $u$: exposure unit [0.25]; $\sigma$ halves build-up during protective slowing; $\psi$ the base recovery rate [0.5]; $\beta_i$ the funded share of repair, up to a boost [3];
- $\pi_i$: graded protection (Section 8).

Because $L_i$ is measured against $c_i^{\text{eff}}$, and $c_i^{\text{eff}}$ falls as $E_i$ rises, overload feeds itself.

## 3. Value and priority

**Value** (a shadow price, $\partial W/\partial c_i$, approximated in the engine):

$$v_i=\text{vital}_i\;b(\hat L_i),\qquad b(L)=\epsilon_0+(1-\epsilon_0)\,\min\!\Big(1,\Big[\tfrac{L-L_0}{1-L_0}\Big]_+\Big)$$

[$\epsilon_0=0.05$, $L_0=0.7$]. For a non-bypassable control part, $b\equiv1$. An intake with nothing to take in has value scaled by its supply. $\hat L_i$ is what control sees through state signals with gain $g_i$:

$$\hat L_i=(1-g_i)\,\frac{d_i}{\kappa_i c_i}+g_i\,\max\!\Big(L_i^{\text{prev}},\frac{d_i}{c_i^{\text{eff}}}\Big),\qquad \dot g_i=\begin{cases}-g_i/\tau_g & L_i>1\\ (g_i^0-g_i)\cdot0.1 & \text{otherwise}\end{cases}$$

[$g^0=1$ coupled, $0$ opaque; $\tau_g=30$]. Demand here is normal demand, before economising.

**Spending price** (who pays first: ascending $p_i$):

$$p_i=v_i\,s_i\,\min(\tau+h_i,\;T),\qquad s_i=1-\frac{\ell(E_i)}{\lambda_{\max}}$$

$\tau$ is the episode's length so far (at least 1); $h_i$ the rebuild time (very large for fixed capital); $T$ the remaining horizon [100], or the next task's deadline. The top (the held output) is defended by definition.

**Recovery priority** (who is rebuilt first: descending $q_i=v_i/k_i$; restoration cost $k_i$ uniform in the engine).

**Optimality.** Ascending $p_i$ is the best policy only for a concave, separable objective (water-filling). $s_i$ handles saturating damage (the fuse); the control rule handles a cliff; increasing returns to an output (semelparity) are not represented.

## 4. Routing

Parts are processed in priority order. Part *i*'s shortfall is

$$S_i=\big[d_i^{\text{run}}(1-\delta_i)+m_i-(c_i^{\text{eff}}-x_i)\big]_+$$

($m_i$ load passed to *i* and absorbed in its spare capacity, $x_i$ load displaced onto it, $\delta_i$ a lasting demand cut from a scar). It is placed:
1. **reserve:** $r_i=\min(S_i,\rho(R),R)$, with $\rho(R)=\rho_0\min\!\big(1,\tfrac{R}{k_RR_{\max}}\big)$ (the knee);
2. **spare capacity** of lower-priority parts, in ascending price: up to $[c_j^{\text{eff}}-d_j-m_j-x_j]_+$, no exposure;
3. **displacement** onto lower-priority parts, lowest price first, up to $\theta c_j^{\text{eff}}$ each [0.35], borne as exposure; unlabelled load cannot be refused, labelled load is refused by parts with $E_j\ge E_s$;
4. **residual:** the part's own debt; a coupled top sheds it visibly instead.

**Control failure:** if a non-bypassable control part has $E\ge E_c$, steps 2 and 3 ignore priority and spread the shortfall by capacity.

**Network.** In the model, parts are linked by shared input, stressor, reserve or repair (edges), and a part's response can land as demand on another, so displaced load can travel back along a loop. **The engine has supply edges ($\omega_i$) but no such loops yet.**

## 5. The reserve

**Value: the expected shortfall**, a running average of steps on which total normal demand exceeded total current capacity:

$$\dot\rho_s=\frac{\mathbf 1\!\big[\textstyle\sum_i d_i>\sum_i c_i^{\text{eff}}\big]-\rho_s}{\tau_\rho}\qquad[\tau_\rho=30]$$

**Size: frequency and remembered depth.** With $D_e$ the total shortfall of episode $e$:

$$X_R\leftarrow\max(X_R,\,D_e-R^0_{\max})\ \text{at each episode's end},\quad \dot X_R=-\frac{X_R}{\tau_m},\qquad R_{\max}=\max\!\Big(R^0_{\max}(1+\gamma\rho_s),\;R^0_{\max}+\min(X_R,R^0_{\max})\Big)$$

[$\gamma=1$, $\tau_m=100$]. **Frequency sets the order; depth sets the size.**

## 6. Economising (the graded switch)

The driver is the gap between the shortfall still expected, $\hat D$, and the reserve:

$$g=\frac{\hat D-R}{R^0_{\max}},\qquad x=\min\!\Big(1,\frac{[g-g_0]_+}{g_1-g_0}\Big),\qquad g_0=-(1-\delta_0),\ g_1=-(1-\delta_1)$$

[$\delta_0=0.5$, $\delta_1=0.9$]. With $\hat D=0$ this is a set depletion of the reserve. The expectation:

$$\hat D=A(t)+\frac{D_e}{\ell}\,\big[\ell^\ast-\ell\big]_+,\qquad \ell^\ast=\begin{cases}\bar\ell & \ell<\bar\ell\\ 2\ell & \text{otherwise}\end{cases}$$

$A(t)$: need known in advance (a predictable episode); $D_e$, $\ell$: shortfall and length of the episode so far; $\bar\ell$: typical episode length, from a mapping prior and updated at each episode's end (half weight).

**Response and ledger:**

$$\dot\epsilon=\frac{\epsilon_{\max}S(x)-\epsilon}{\tau_\epsilon},\quad S(x)=x^2(3-2x),\qquad d_i^{\text{run}}=(1-\epsilon)\,d_i\ \ (i\neq\text{top, control})$$

[$\epsilon_{\max}=0.3$, $\tau_\epsilon=5$; $\epsilon$ set to 0 below $10^{-4}$]. The economised demand $\epsilon d_i$ splits: $\phi_i\,\epsilon d_i$ is added to the part's debt (deferred maintenance, repaid from slack later) and $(1-\phi_i)\,\epsilon d_i$ is shed across the boundary [$\phi_i=0.5$].

## 7. Recovery allocation

Slack is pooled across parts. Each part's own slack first repays its debt; the pooled slack is then allocated in descending value among parts (funding repair) and the reserve (value $\rho_s$). The reserve waits while any part of higher value is still under repair, and unspent slack is not banked while it waits. Repair of $\Delta E$ costs $\kappa_r c_i\Delta E$ [0.02].

## 8. What a part becomes after an episode

An episode ends after a calm spell [5 steps] with no load, exposure or debt. With $D_i^\ast$ the peak demand the part carried:
- **growth** (acute, coupled, renewable, not compromised, peak exposure at least 1): $\kappa_i\leftarrow\min(\kappa_{\max},\kappa_i(1+g\,v))$, with severity $v=\min(1,E^{\text{peak}}_i/E_c)$ [$g=0.10$, $\kappa_{\max}=1.3$];
- **protection, set by the peak** (not compromised): $X_i\leftarrow\max(X_i,\,D_i^\ast-\kappa_ic_i)$ with $D_i^{k}=\kappa_ic_i+X_i$, fading as $\dot X_i=-X_i/\tau_m$; graded protection $\pi_i\mathrel{+}=\nu\min\!\big(1,(D_i^\ast/\kappa_ic_i-1)/u\big)$, fading likewise [$\nu=0.5$];
- **scar** (renewable, after compromise): $\kappa_i\leftarrow\max(0.5,\kappa_i-\varsigma\,\ell^{\text{peak}}_i)$ [$\varsigma=0.5$]; protection reset, $X_i=\pi_i=0$; a scar flagged to cut demand sets $\delta_i$;
- **loss** (fixed capital): $\kappa_i\le1-\ell(E_i)$, never recovered.

## 9. Read-outs

- **Record:** $y(t)=\dfrac{\text{demand served at the top}}{\text{raw top demand}}$, a held output.
- **Record dynamics (G12):** a knock $k$ is restored at $\rho(R)$, so $t_{\text{rec}}\approx k/\rho(R)$, which equals $k/\rho_0$ above the knee and $k\,k_RR_{\max}/(\rho_0R)$ below it: recovery time grows as $1/R$ without bound as the reserve empties (critical slowing down; rising autocorrelation and variance at a steady mean). With full release until a switch, $t_{\text{rec}}$ is constant and the break gives no warning. **Derived, not simulated** (the engine's record has no restoring dynamics).
- **State signals:** $E_i$, $c_i^{\text{eff}}/c_i$, $D_i$, $R/R_{\max}$, $\epsilon$, judged against the system's own phase reference.
- **Co-movement (G18):** if parts *i* and *j* both load from a shared input carrying $\Lambda(t)$, write their state signals as $Z_i=a_i\Lambda+\varepsilon_i$ and $Z_j=a_j\Lambda+\varepsilon_j$, with independent part-level noise. Then

$$\operatorname{corr}(Z_i,Z_j)=\frac{a_ia_j\operatorname{Var}\Lambda}{\sqrt{(a_i^2\operatorname{Var}\Lambda+\sigma_i^2)(a_j^2\operatorname{Var}\Lambda+\sigma_j^2)}}$$

which rises towards 1 as the shared load comes to dominate the parts' own variation, before either crosses a threshold. Parts clustered only by price have no common $\Lambda$ and no such rise. **Derived, not simulated** (no loops in the engine).
- **Felicity read-out:** with $D_{\text{on}}$ the demand at which strain first appears when load is raised, $D_{\text{on}}\ge D^\ast$ protected or grown; $\kappa c\le D_{\text{on}}<D^\ast$ protection fading; $D_{\text{on}}<\kappa c$ scarred.

## 10. Results that follow

**A. How long the record stays flat.** Under a constant overload at the top, $\Delta=d_{\text{top}}-c_{\text{top}}$, the record holds while

$$\Delta\le\rho(R)+\sum_j\big[c_j^{\text{eff}}-d_j^{\text{run}}\big]_++\theta\sum_jc_j^{\text{eff}}$$

While the reserve carries the gap $G$ left after spare capacity and displacement room, the break time is $T^\ast\approx R_0/G$: usable buffer over excess, independent of the rate at which the excess arrives (G3). Economising widens the right-hand side (it frees working capacity), so it lengthens the silence; displacement erodes $c_j^{\text{eff}}$, which shortens it and sharpens the break.

**B. Compounding.** For one part under constant demand $d>c[1-\ell(E)]$, $\dot E=\frac1u\big(\frac{d}{c[1-\ell(E)]}-1\big)$, which increases with $E$: strain accelerates as it accumulates (the structure of James's $\dot\Lambda=kS/F(\Lambda)$), saturating at the loss cap.

**C. When recovery is possible.** A part recovers only if the demand it carries falls below its current capacity: $d_i^{\text{run}}(1-\delta_i)+m_i+x_i<\kappa_ic_i[1-\ell(E_i)]$. With demand at or above $1-\lambda_s$ of capacity, a part that enters protective slowing cannot leave it without relief (the opaque trap) unless economising cuts its demand by more than the gap; the trap returns where deferred debt cannot be repaid before the next load. After a scar, a part whose demand exceeds its lowered ceiling never returns unless its demand is cut.

**D. Growth needs coupling, slack and strain without economising.** Growth needs an acute episode that ends with peak exposure at least 1 and below $E_c$. Economising lowers carried demand by $\epsilon d_i$; when that removes the overload, the part never reaches the strain growth needs (G17).

## 11. What the formalisation does not settle

- **The functional forms** (piecewise loss, linear exposure, fixed displacement room, the S-curve, exponential fading) are choices.
- **Fitted values:** the shortfall definition, the reserve's cap and memory, the economising settings, the first-time expectation ("as much again"), the deferred share, and all rates and thresholds. No parameter has been estimated from data; the held-out stress tests would do that.
- **Not yet in the engine:** loops in which one part's response adds demand to another; more than one reserve; restoring dynamics in the record; an explicit objective (so increasing returns and semelparity are not represented).
