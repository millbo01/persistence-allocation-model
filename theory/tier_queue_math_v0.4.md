# The tier-queue model in mathematical form (v0.4, 5 October 2026)

**Status:** theorising (phase 3). This writes the canonical model (TIER_QUEUE_MODEL_v0.4.md) and its engine (theory/sim/tq_core.py) as equations. The symbols match the code's constants, given in brackets. It is a candidate formalisation: the functional forms are choices, and only the qualitative behaviour has been checked against natural systems.

## 1. The core in three equations

**(1) The ledger (conservation).** For any currency that obeys a balance, summed over all parts *i*:

$$\sum_i d_i(t) \;=\; \sum_i w_i(t) \;+\; r(t) \;+\; \sum_i \dot D_i(t) \;+\; b(t)$$

Demand equals work done, plus reserve drawn, plus debt added, plus load leaving across the boundary. Nothing leaves except through work done or the boundary.

**(2) Effective capacity, which compounds:**

$$c_i^{\text{eff}} \;=\; \kappa_i\,c_i\,\big[1-\ell(E_i)\big]\,\big[(1-\omega_i)+\omega_i\,s_{u(i)}\big]$$

- $\kappa_i$: the ceiling;
- $\ell(E)$: loss from exposure;
- $s_{u(i)}$: the served share of the part's upstream supply;
- $\omega_i$: how strongly the part depends on that supply (refinement A).

**(3) Exposure, felt against current capacity:**

$$\frac{dE_i}{dt} \;=\; \frac{(1-\pi_i)\,\sigma(E_i)\,[L_i-1]_+ \;-\; \beta_i\,\psi\,[1-L_i]_+}{u}, \qquad L_i=\frac{\text{demand carried by } i}{c_i^{\text{eff}}}$$

(Terms, v0.6: **demand** is the work asked of a part; **load** is the excess beyond capacity. Demand carried by *i* is its own demand plus what was passed to it, less what it passed on.)

- $u$: the exposure unit, so one step at 125% of current capacity adds 1 [EXPO_UNIT = 0.25];
- $\pi_i$: re-tuning protection;
- $\sigma$: protective slowing, which halves build-up between the slowing and compromise thresholds;
- $\psi$: the base recovery rate [RECOVER];
- $\beta_i$: the funded share of repair (up to the boost factor after acute load).

Because $L_i$ is measured against $c_i^{\text{eff}}$, and $c_i^{\text{eff}}$ falls as $E_i$ rises, overload feeds itself.

## 2. The loss function and stages

$$\ell(E)=\begin{cases}0 & E<E_s \;(\text{optimal or coping})\\ \lambda_s & E_s\le E<E_c \;(\text{protective slowing})\\ \lambda_c+(\lambda_{\max}-\lambda_c)\min\!\big(1,\tfrac{E-E_c}{E_{\max}-E_c}\big) & E\ge E_c \;(\text{compromised})\end{cases}$$

Values: $E_s=4$, $E_c=13$, $\lambda_s=0.10$, $\lambda_c=0.13$, $\lambda_{\max}=0.50$, $E_{\max}=78$. The bands come from James's vacancy debt method.

## 3. Routing (where a shortfall goes)

Parts are processed from highest priority down. Part *i*'s shortfall is

$$S_i=\big[d_i(1-\delta_i)+m_i-(c_i^{\text{eff}}-x_i)\big]_+$$

where $m_i$ is load passed to *i* and absorbed in its spare capacity, $x_i$ is load displaced onto *i*, and $\delta_i$ is any lasting demand cut. The shortfall is placed in order:

1. **Reserve:** $\;r_i=\min\!\big(S_i,\;\rho(R),\;R\big)$, with $\rho(R)=\rho_0\min\!\big(1,\tfrac{R}{k\,R_{\max}}\big)$. A small store cannot release fast (the knee).
2. **Spare capacity of lower-priority parts** $j$, in ascending priority: up to $\big[c_j^{\text{eff}}-d_j-m_j-x_j\big]_+$. No exposure.
3. **Displacement** onto lower-priority parts, lowest first: up to $\theta\,c_j^{\text{eff}}$ each [DISPLACE_CAP = 0.35]. It is borne as exposure. Unlabelled load cannot be refused; labelled load is refused by parts with $E_j\ge E_s$.
4. **Residual:** the part's own debt, $\dot D_i \mathrel{+}= S_i-\sum(\ldots)$. In a coupled system the top sheds it visibly instead.

**Control failure:** if a control part has $E\ge E_c$, steps 2 and 3 ignore priority. The shortfall is spread across all parts by capacity, protected parts included.

**Threshold switch** (refinement B): if $R/R_{\max}\le a$, the top sheds a share of its demand until $R/R_{\max}\ge a'$.

## 4. The two read-outs

- **The record:** $\;y(t)=\dfrac{\text{demand served at the top}}{\text{raw top demand}}$. It must be a held output (rule R).
- **State signals:** $\;E_i(t)$, $c_i^{\text{eff}}(t)/c_i$, $D_i(t)$, $R(t)/R_{\max}$.

## 5. Recovery and what a part becomes (v0.4)

**Repair is funded.** Removing $\Delta E$ costs $\kappa_r\,c_i\,\Delta E$ of resource [REPAIR_COST = 0.02]. A part's own slack pays first; the top's slack is then allocated:

$$\text{chronic episode: } R \;\rightarrow\; \text{repair (intake first)}; \qquad \text{acute episode: repair (intake first, rate up to } \beta_{\max}\psi) \;\rightarrow\; R \text{ only once all } E_i=0$$

Here $\beta_{\max}=3$ [REPAIR_BOOST]. An episode is chronic once strain has lasted $T_c=20$ steps [CHRONIC_STEPS].

**At the end of an episode for part *i*,** with severity $v=\min(1,E^{\text{peak}}_i/E_c)$:

| Outcome | Condition | Update |
|---|---|---|
| Growth | Acute ($E^{\text{peak}}<E_c$), coupled, renewable | $\kappa_i\leftarrow\min\!\big(\kappa_{\max},\,\kappa_i(1+g\,v)\big)$, with $g=0.10$, $\kappa_{\max}=1.3$ |
| Re-tuning | Acute | $\pi_i\leftarrow\min(\pi_{\max},\,\pi_i+\nu\,v)$, fading as $\dot\pi_i=-\pi_i/\tau_m$, with $\nu=0.5$, $\tau_m=100$ |
| Scar | Renewable, after compromise | $\kappa_i\leftarrow\max\!\big(0.5,\,\kappa_i-\varsigma\,\ell^{\text{peak}}_i\big)$, with $\varsigma=0.5$ |
| Loss | Fixed capital | $\kappa_i\le 1-\ell(E_i)$ (never recovered) |
| Demand cut | Parts flagged to cut demand, as compromise sets in | $\delta_i\leftarrow\min\!\big(\delta_{\max},\,\max(\delta_i,\,\zeta\,\ell(E_i))\big)$, with $\zeta=0.5$ |
| Reserve re-tuning | Chronic episode | $R_{\max}\leftarrow\min\!\big(2R^0_{\max},\,(1+\eta)R_{\max}\big)$, $\eta=0.3$, fading back towards $R^0_{\max}$ when unused |

## 6. Results that follow from the equations

**A. How long the record stays flat.** With a constant overload at the top, $\Delta=d_{\text{top}}-c_{\text{top}}$, the record holds while the buffers can take the excess:

$$y(t)=1 \iff \Delta \;\le\; \rho\big(R(t)\big)\;+\;\sum_j\big[c_j^{\text{eff}}(t)-d_j\big]_+\;+\;\theta\sum_j c_j^{\text{eff}}(t)$$

The break comes at the first $t$ where this fails. While the reserve carries the gap $G=\Delta-\text{spare}-\text{displacement room}$, the break time is approximately

$$T^\ast \approx \frac{R_0}{G}$$

That is usable buffer over excess, and it is independent of the rate at which the excess arrives. This is why the break comes at the same cumulative loss for slow and fast blood loss, and the same loss of conductivity for slow and fast drought. Because displacement erodes $c_j^{\text{eff}}$ through equation (3), the buffer shrinks as it is used, which brings the break forward and sharpens it.

**B. Compounding.** For one part under constant load $d>c\,[1-\ell(E)]$:

$$\frac{dE}{dt}=\frac{1}{u}\left(\frac{d}{c\,[1-\ell(E)]}-1\right)$$

This increases with $E$, so strain accelerates as it accumulates. It is the same structure as James's earlier structural-load law, $\dot\Lambda=kS/F(\Lambda)$, with $F$ falling as $\Lambda$ rises: exposure plays the part of accumulated load, and $c\,[1-\ell(E)]$ plays the part of the capacity that bounds it. In this engine, $\ell$ is capped at 50%, so the runaway saturates at the floor instead of diverging.

**C. When recovery is possible at all.** A part recovers only if the demand it carries falls below its current capacity (it does not need demand to stop):

$$d_i(1-\delta_i)+m_i+x_i \;<\; \kappa_i\,c_i\,\big[1-\ell(E_i)\big]$$

Two consequences:
- **The opaque trap.** If $d_i/c_i \ge 1-\lambda_s$ (demand at or above 90% of capacity), a part that enters protective slowing cannot leave it without outside relief. That is TQ7's opaque result, and James's "the slow-down compounds the problem".
- **Incomplete recovery.** After a scar, a part whose demand exceeds its lowered ceiling, $d_i>\kappa_i c_i$, never returns to its old state unless its demand is cut (the spruce case).

**D. Growth requires coupling and slack.** Growth needs an acute episode that ends: $E^{\text{peak}}<E_c$, and then the recovery condition in C must hold for long enough to end the episode. In an opaque system near capacity, C fails, the episode never ends, and neither growth nor re-tuning occurs.

## 7. Compressed statement

> Strain is conserved (1). It moves downhill through buffers in priority order (section 3). Each part's capacity falls with the strain it carries, and the strain grows faster as capacity falls (2 and 3). The held output stays flat until the buffers cannot take the excess (A). After an episode, a part becomes stronger, re-tuned, scarred or lost, depending on whether the load was acute or chronic, whether the system was coupled, and whether the part can be rebuilt (section 5).

## 8. What the formalisation does not settle

- **The functional forms** (the piecewise loss, a linear exposure rate, a fixed displacement room) are choices. Others would give the same qualitative behaviour.
- **The priority rule** is now a formula (v0.5, with the remaining-horizon correction in v0.6): see theory/priority_formula.md and Section 2a of TIER_QUEUE_MODEL_v0.7.md; the v0.7 form is in Section 9 below. The equations above hold with priority computed from marginal value.
- **No parameter has been estimated from data.** The held-out stress tests would do that.

## 9. Additions in v0.7

**Spending cost.**

$$p_i \;=\; v_i\,s_i\,\min(\tau+h_i,\;T),\qquad s_i \;=\; 1-\frac{\ell(E_i)}{\lambda_{\max}}$$

- $\tau$: the rest of the episode (time units), estimated in the engine as the episode's length so far (at least one step);
- $h_i$: rebuild time; $T$: remaining horizon;
- $s_i$: the share of capacity still at stake, 1 when healthy and 0 at the floor;
- for a control part, $v_i=\text{vital}_i$ (always at the bottleneck).

Spending in ascending $p_i$ is the optimal policy only for a concave, separable objective (the water-filling or KKT solution). $s_i$ handles saturating damage (the fuse) and the control rule handles a cliff-shaped loss. Increasing returns to an output (semelparity) are not yet represented.

**Record dynamics (G12).** Let a knock of size $k$ leave a deficit that the reserve restores at its release rate, with the knee from Section 3:

$$\rho(R)=\rho_0\min\!\Big(1,\frac{R}{\kappa R_{\max}}\Big)\quad\Rightarrow\quad t_{\text{rec}}\approx\frac{k}{\rho(R)}=\begin{cases}k/\rho_0 & R\ge\kappa R_{\max}\\[4pt] \dfrac{k\,\kappa R_{\max}}{\rho_0\,R} & R<\kappa R_{\max}\end{cases}$$

Below the knee, recovery time grows as $1/R$ and has no upper bound as $R\to0$. This is critical slowing down: the record's mean stays at its setpoint while its recovery from each knock slows, so its lag-one autocorrelation and variance rise before the break. With no knee ($\kappa=0$) and a threshold switch, $t_{\text{rec}}$ is constant until the switch, and the record gives no warning. The engine's record is recalculated each step without restoring dynamics, so it cannot show this; the derivation stands on the release function alone.

## 10. Additions in v0.8: peak-referenced protection and the Felicity read-out

After a recovered episode in which part *i* carried a peak demand $D_i^\ast$ above its normal capacity $\kappa_i c_i$, the part carries without strain up to

$$D_i^{k}(t)=\kappa_i c_i+X_i(t),\qquad X_i(t)=\big(D_i^\ast-\kappa_i c_i\big)\,e^{-t/\tau_m}$$

where $t$ is the time since the episode ended and $\tau_m$ the re-tuning memory. Exposure, equation (3), then builds with

$$\frac{dE_i}{dt}\propto\frac{\big[D_i-\max(c_i^{\text{eff}},\,D_i^{k})\big]_+}{c_i^{\text{eff}}}\,(1-\pi_i)$$

with the graded protection $\pi_i$ also set by the peak overload, $\pi_i\mathrel{+}=\nu\min\!\big(1,(D_i^\ast/\kappa_i c_i-1)/u\big)$. A scar sets $X_i=\pi_i=0$. Because the threshold is $\max(c^{\text{eff}},D^k)$, protection covers loads up to the earlier peak even while capacity is still reduced during recovery.

**The Felicity read-out.** With $D_{\text{on}}$ the demand at which strain first appears when load is raised:

$$F=\frac{D_{\text{on}}}{D^\ast}\qquad\begin{cases}D_{\text{on}}\ge D^\ast & \text{protected or grown}\\ \kappa c\le D_{\text{on}}<D^\ast & \text{protection fading}\\ D_{\text{on}}<\kappa c & \text{scarred}\end{cases}$$

## 11. Additions in v0.9: reserve memory and the system's clock

Let $D_e=\sum_{t\in e}\big[\sum_i d_i(t)-\sum_i c_i^{\text{eff}}(t)\big]_+$ be the total shortfall of episode $e$. At the end of each episode the reserve's remembered excess is updated, and it fades between episodes:

$$X_R\leftarrow\max\!\big(X_R,\;D_e-R^0_{\max}\big),\qquad \dot X_R=-X_R/\tau_m$$

The reserve's size is $R_{\max}=\max\!\big(R^0_{\max}(1+\gamma\,\rho_s),\;R^0_{\max}+\min(X_R,\,R^0_{\max})\big)$, where $\rho_s$ is the expected shortfall (frequency) and $\gamma$ its gain. The reserve's place in the recovery order is still set by $\rho_s$ alone: **frequency sets the order, depth sets the size.**

**Durations** ($\tau_m$, the expected-shortfall memory, "brief", "lasting") are stated in units of the system's own clock, fixed before checking: refill time, rebuild time, decision cycles or generations.

## 12. Additions in v0.10: economising

With depletion $\delta(t)=\big[1-R(t)/R^0_{\max}\big]_+$ and a smooth step $S(x)=x^2(3-2x)$ on $x=\min\!\big(1,[\delta-\delta_0]_+/(\delta_1-\delta_0)\big)$:

$$\dot\epsilon=\frac{\epsilon_{\max}\,S(x)-\epsilon}{\tau_\epsilon},\qquad d_i^{\text{run}}=(1-\epsilon)\,d_i\quad(i\neq\text{top, control})$$

with $\delta_0=0.5$, $\delta_1=0.9$, $\epsilon_{\max}=0.3$, $\tau_\epsilon=5$ steps (all illustrative). The economised demand $\epsilon\,d_i$ splits (v0.11): a share $\phi_i$ is deferred maintenance, $\dot D_i\mathrel{+}=\phi_i\,\epsilon\,d_i$, repaid from slack later; the rest, $(1-\phi_i)\,\epsilon\,d_i$, is shed across the boundary. It is not removed. Parts' value and the expected shortfall use $d_i$, not $d_i^{\text{run}}$.
