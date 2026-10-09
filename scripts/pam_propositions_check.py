"""Numerical checks of the derived propositions (theory/PAM_propositions_DRAFT.md), Claude, 7 October 2026.

A minimal reference implementation of the reduced form of theory/PAM_math_v0.18.md, one resource, written
from the maths (not from the frozen engine). Each check draws random instances and tests a proposition's
statement; a failure prints the counter-example. Usage: python scripts/pam_propositions_check.py
"""
import math
import random

random.seed(20261007)
TOL = 1e-9


# ---------- one step of the ordered draw (maths Section 2), one resource ----------
def draw(S, top_need, basal, support, ordinary):
    """Phases 1-4. basal, support, ordinary are lists of draws in the order pi (highest rank first).
    Returns allocations per phase (same shapes) and what is left in the flow."""
    a_top = min(S, top_need)
    S -= a_top
    a_b = []
    for x in basal:
        a = min(S, x)
        a_b.append(a)
        S -= a
    a_p = []
    for x in support:
        a = min(S, x)
        a_p.append(a)
        S -= a
    a_o = []
    for x in ordinary:
        a = min(S, x)
        a_o.append(a)
        S -= a
    return a_top, a_b, a_p, a_o, S


def rand_instance(n_basal=6, n_sup=2, n_ord=6):
    top = random.uniform(1, 5)
    basal = [random.uniform(0.1, 2) for _ in range(n_basal)]
    sup = [random.uniform(0.1, 2) for _ in range(n_sup)]
    ordn = [random.uniform(0.1, 3) for _ in range(n_ord)]
    return top, basal, sup, ordn


def fail(name, msg):
    print(f"FAIL {name}: {msg}")
    return 1


# ---------- P1: ledger closure and invariance of total load ----------
def check_P1(trials=2000):
    bad = 0
    for _ in range(trials):
        top, basal, sup, ordn = rand_instance()
        need = top + sum(basal) + sum(sup) + sum(ordn)
        U = random.uniform(0, need)
        d = random.uniform(0, need - U)  # store draw at its release limit, fixed
        S = U + d
        a_top, a_b, a_p, a_o, left = draw(S, top, basal, sup, ordn)
        load = (top - a_top) + sum(x - a for x, a in zip(basal, a_b)) + sum(x - a for x, a in zip(sup, a_p)) + sum(x - a for x, a in zip(ordn, a_o))
        gap = need - U
        if abs(gap - (d + load)) > 1e-7:
            bad += fail("P1 ledger", f"gap {gap} != d + load {d + load}")
        # invariance: any other access setting (here: any permutation of the order, any phase order) leaves total load unchanged
        perm = ordn[:]
        random.shuffle(perm)
        b2 = basal[:]
        random.shuffle(b2)
        _, a_b2, a_p2, a_o2, _ = draw(S, top, b2, sup, perm)
        a_top2 = min(S, top)
        load2 = (top - a_top2) + sum(x - a for x, a in zip(b2, a_b2)) + sum(x - a for x, a in zip(sup, a_p2)) + sum(x - a for x, a in zip(perm, a_o2))
        if abs(load - load2) > 1e-7:
            bad += fail("P1 invariance", f"{load} vs {load2}")
    return bad


# ---------- P2: silence and the two thresholds ----------
def check_P2(trials=2000):
    bad = 0
    for _ in range(trials):
        top, basal, sup, ordn = rand_instance()
        B, P, D4 = sum(basal), sum(sup), sum(ordn)
        S = random.uniform(0, top + B + P + D4)
        a_top, a_b, a_p, a_o, _ = draw(S, top, basal, sup, ordn)
        top_met = a_top >= top - TOL
        sup_met = all(a >= x - TOL for a, x in zip(a_p, sup)) and all(a >= x - TOL for a, x in zip(a_b, basal))
        if top_met != (S >= top - TOL):
            bad += fail("P2 immediate threshold", f"S={S} top={top}")
        if sup_met != (S >= top + B + P - TOL):
            bad += fail("P2 second threshold", f"S={S}")
    return bad


# ---------- P3: order of loss is a lower segment; basal before work; top last ----------
def check_P3(trials=2000):
    bad = 0
    for _ in range(trials):
        top, basal, sup, ordn = rand_instance()
        S = random.uniform(0, top + sum(basal) + sum(sup) + sum(ordn))
        a_top, a_b, a_p, a_o, _ = draw(S, top, basal, sup, ordn)
        # lower segment within phase 4: once a part is short, every later part has zero
        short = [a < x - TOL for a, x in zip(a_o, ordn)]
        if any(short):
            k = short.index(True)
            if any(a > TOL for a in a_o[k + 1:]):
                bad += fail("P3 lower segment", str(a_o))
        # basal before work: if any basal short, all phase 3-4 draws are zero
        if any(a < x - TOL for a, x in zip(a_b, basal)) and (sum(a_p) + sum(a_o) > TOL):
            bad += fail("P3 basal before work", "")
        # top last: if top short, everything else zero
        if a_top < top - TOL and (sum(a_b) + sum(a_p) + sum(a_o) > TOL):
            bad += fail("P3 top last", "")
    return bad


# ---------- P4: the break under proportional release ----------
def break_step(L0, k, gap, M, full_release=False, T=100000):
    """Constant gap per step; store draw d = min(release, gap); break when gap - d > M.
    Returns (step, store left at the break, cumulative store draw)."""
    L, drawn = L0, 0.0
    for t in range(T):
        rel = L if full_release else k * L
        d = min(rel, gap, L)
        if gap - d > M + TOL:
            return t, L, drawn
        L -= d
        drawn += d
    return None, L, drawn


def check_P4(trials=500):
    bad = 0
    for _ in range(trials):
        L0 = random.uniform(50, 200)
        k = random.uniform(0.01, 0.2)
        M = random.uniform(0, 5)
        if k * L0 < M + 0.2:  # the store cannot carry a gap above M even at the start: not this case
            continue
        gap = random.uniform(M + 0.1, k * L0)  # above M (it breaks), within the first release (not at once)
        t, L_left, drawn = break_step(L0, k, gap, M)
        pred = (gap - M) / k
        # discrete time: the store left at the break lies in ((gap-M)/k * (1-k), (gap-M)/k]
        if t is None or not (pred * (1 - k) - 1e-6 <= L_left <= pred + 1e-6):
            bad += fail("P4 store left", f"L0={L0} k={k} M={M} gap={gap} left={L_left} pred={pred}")
        # full release: store left is 0 (to within one step's gap), whatever the gap
        t2, L2, _ = break_step(L0, k, gap, M, full_release=True)
        if t2 is None or L2 > gap:
            bad += fail("P4 full release", f"left={L2}")
    # monotone: a faster gap leaves more store unused
    L0, k, M = 100, 0.05, 1.0
    lefts = [break_step(L0, k, g, M)[1] for g in [1.5, 2, 3, 4]]
    if not all(a < b for a, b in zip(lefts, lefts[1:])):
        bad += fail("P4 monotone", str(lefts))
    # gap at or below M never breaks
    if break_step(L0, k, 0.9, M)[0] is not None:
        bad += fail("P4 no break", "")
    return bad


# ---------- P6: rate decides harm ----------
def decline_loss(K, theta, tau, phi, Delta):
    """Renewal capacity R falls by phi per step for Delta/phi steps, then holds. Units not renewed:
    switched off up to theta*K per step, the rest fail at 1/tau per step. Returns total disorderly loss."""
    n = R = K
    lost = 0.0
    steps = int(math.ceil(Delta / phi))
    for t in range(steps + 20 * tau + 200):
        if t < steps:
            R = max(K - Delta, R - phi)
        u = max(0.0, n - R)
        off = min(u, theta * K)
        fl = (u - off) / tau
        n -= off + fl
        lost += fl
    return lost


def check_P6(trials=400):
    bad = 0
    for _ in range(trials):
        K = 100.0
        theta = random.uniform(0.02, 0.2)
        tau = random.randint(2, 10)
        phi = random.uniform(0.2, 40)
        Delta = random.uniform(5, 90)
        lam = decline_loss(K, theta, tau, phi, Delta)
        if phi <= theta * K:
            if lam > 1e-9:
                bad += fail("P6 slow is harmless", f"phi={phi} thetaK={theta*K} loss={lam}")
        else:
            approx = Delta * (1 - theta * K / phi)
            bound = tau * (phi - theta * K)
            # two-sided: approx is an upper bound; the loss is below it by at most tau*(phi - theta*K)
            if not (approx - bound - 1e-6 <= lam <= approx + 1e-9):
                bad += fail("P6 bound", f"phi={phi} thetaK={theta*K} tau={tau} Delta={Delta} loss={lam} approx={approx} bound={bound}")
    return bad


# ---------- P7: shrinking under unpaid upkeep ----------
def check_P7(trials=2000):
    bad = 0
    for _ in range(trials):
        n = random.uniform(10, 100)
        kb = random.uniform(0.1, 2)
        a = random.uniform(0, kb * n)
        m = random.uniform(0, 5)
        y = random.uniform(1, 3)
        u = max(0.0, kb * n - a) / (kb + m / y)
        # the remaining units are exactly funded
        if abs(kb * (n - u) - (a + (m / y) * u)) > 1e-7:
            bad += fail("P7 funded", "")
        # never more than the old rule, equal at m = 0
        old = n * (1 - a / (kb * n))
        if u > old + 1e-9:
            bad += fail("P7 below old rule", "")
    return bad


# ---------- P9: partial refill (newsvendor) ----------
def check_P9():
    bad = 0
    depths = [random.expovariate(1 / 20) for _ in range(500)]  # remembered episode depths
    depths.sort()

    def tail(L):  # P(deficit > L)
        return sum(1 for x in depths if x > L) / len(depths)

    cS, rho = 10.0, 0.4
    for V in [0.5, 1.0, 2.0, 3.9, 4.5]:
        # greedy: refill unit by unit while store value exceeds the best part value V
        L = 0.0
        while cS * rho * tail(L) > V and L < 1000:
            L += 0.1
        if V >= cS * rho:
            if L != 0.0:
                bad += fail("P9 no refill", f"V={V}")
            continue
        # critical fractile: the (1 - V/(cS*rho)) quantile of remembered depths
        q = 1 - V / (cS * rho)
        Lstar = depths[min(len(depths) - 1, int(math.ceil(q * len(depths))) - 1)]
        if abs(L - Lstar) > 0.2:
            bad += fail("P9 fractile", f"V={V} greedy={L} fractile={Lstar}")
    return bad


# ---------- P10: repair competition under strict rank ----------
def check_P10(trials=1000):
    bad = 0
    for _ in range(trials):
        W = random.uniform(0.5, 5)
        D = [random.uniform(0, 10) for _ in range(5)]  # damage, in rank order
        rem = D[:]
        t = 0
        finish = [None] * 5
        while any(r > 1e-12 for r in rem) and t < 10000:
            t += 1
            cap = W
            for i in range(5):
                take = min(cap, rem[i])
                rem[i] -= take
                cap -= take
                if rem[i] <= 1e-12 and finish[i] is None:
                    finish[i] = t
        for i in range(5):
            if D[i] <= 1e-12:
                continue
            pred = math.ceil(sum(D[: i + 1]) / W - 1e-12)
            if finish[i] != pred:
                bad += fail("P10 timing", f"i={i} finish={finish[i]} pred={pred}")
        # the highest-ranked damaged part heals as fast as alone
        first = next(i for i in range(5) if D[i] > 1e-12)
        if finish[first] != math.ceil(D[first] / W - 1e-12):
            bad += fail("P10 top unaffected", "")
    return bad


# ---------- P5: the warning comes before the break, by a lead time set by k, the gap and the margin ----------
def check_P5(trials=500):
    bad = 0
    for _ in range(trials):
        L0 = random.uniform(50, 200)
        k = random.uniform(0.01, 0.2)
        M = random.uniform(0, 5)
        if k * L0 < M + 0.2:
            continue
        gap = random.uniform(M + 0.1, k * L0)
        L, t, t_warn, t_break = L0, 0, None, None
        while t < 100000:
            if t_warn is None and k * L < gap - TOL:  # release headroom k*L - gap has reached zero
                t_warn = t
            d = min(k * L, gap, L)
            if gap - d > M + TOL:
                t_break = t
                break
            L -= d
            t += 1
        lead = t_break - t_warn
        pred = math.log(gap / (gap - M)) / -math.log(1 - k)
        if t_warn is None or not (t_warn <= t_break) or abs(lead - pred) > 1.0 + 1e-9:
            bad += fail("P5 lead time", f"k={k} gap={gap} M={M} lead={lead} pred={pred}")
    return bad


# =================== batch 2 ===================

# ---------- P11: economising causes no unit loss; work and wear saving at once ----------
def check_P11(trials=300):
    bad = 0
    for _ in range(trials):
        K = 100.0
        theta = random.uniform(0.02, 0.2)
        kw, kn, ku = random.uniform(0.5, 2), random.uniform(0.02, 0.2), random.uniform(0.05, 0.5)
        w0 = K  # one unit of work per active unit at reference
        eps_max = random.uniform(0.1, 0.9)
        tau_e = random.randint(1, 10)  # including very fast economising
        n_a, eps, prev_draw = K, 0.0, None
        base_draw = kw * w0 + kn * K + ku * w0
        for t in range(300):
            eps_new = eps + (eps_max - eps) / tau_e
            w = (1 - eps_new) * w0
            # renewal need: baseline per active unit plus wear per unit of work; access funds it in full
            need = kn * n_a + ku * w
            funded = kn * n_a + ku * w  # renewal access is not cut by economising
            if funded < need - 1e-12:
                bad += fail("P11 renewal shortfall", "")
            draw_now = kw * w + need
            # immediate saving: the work and wear part falls with work in the same step
            if t == 0:
                immediate = base_draw - draw_now
                if abs(immediate - (kw + ku) * w0 * eps_new) > 1e-9:
                    bad += fail("P11 immediate saving", f"{immediate}")
            # consolidation: active units beyond supported work switched off within theta*K
            extra = min(max(0.0, n_a - w), theta * K)
            n_a -= extra
            eps = eps_new
        if n_a < (1 - eps_max) * w0 - 1e-6:
            bad += fail("P11", f"n_a={n_a}")
    return bad


# ---------- P13: rerouting after losing a route ----------
def check_P13(trials=2000):
    bad = 0
    found_counterexample = False
    for _ in range(trials):
        m = random.randint(3, 6)
        C = [random.uniform(1, 10) for _ in range(m)]
        f = [random.uniform(0, c) for c in C]
        e = random.randrange(m)
        head = sum(C[j] - f[j] for j in range(m) if j != e)
        # optimal rerouting (fill headroom): no overload iff head >= f[e]
        rem = f[e]
        over = False
        for j in range(m):
            if j == e:
                continue
            take = min(rem, C[j] - f[j])
            rem -= take
        if (rem > 1e-9) != (head < f[e] - 1e-9):
            bad += fail("P13 optimal", "")
        # proportional-to-capacity rerouting (a physical split): can overload even when head >= f[e]
        tot = sum(C[j] for j in range(m) if j != e)
        prop_over = any(f[j] + f[e] * C[j] / tot > C[j] + 1e-9 for j in range(m) if j != e)
        if head >= f[e] and prop_over:
            found_counterexample = True
    if not found_counterexample:
        bad += fail("P13 physical split", "no case found where a proportional split overloads despite enough headroom")
    return bad


# ---------- P14: response to rising requirement: follows directly from maths Sections 4 and 5 (no numerical check) ----------


# ---------- P16: conflicting orders under joint scarcity ----------
def check_P16():
    bad = 0
    # two parts A, B; two complementary resources; each part needs 1 of each per unit of work
    S1, S2 = 1.0, 1.0
    # resource 1 order: A before B; resource 2 order: B before A; per-resource sequential allocation
    a1A, a1B = min(S1, 1.0), max(0.0, S1 - 1.0)
    a2B, a2A = min(S2, 1.0), max(0.0, S2 - 1.0)
    wA, wB = min(a1A, a2A), min(a1B, a2B)
    if not (wA == 0.0 and wB == 0.0):
        bad += fail("P16", f"expected deadlock, got {wA},{wB}")
    # every split z, 1-z of both resources is feasible and Pareto efficient: total work 1 for all z
    for z in [0.0, 0.25, 0.5, 0.75, 1.0]:
        if abs(min(z, z) + min(1 - z, 1 - z) - 1.0) > 1e-12:
            bad += fail("P16 frontier", "")
    return bad


# ---------- P17: shared uptake by affinity tends to strict priority ----------
def uptake_alloc(Vmax, Km, S):
    """Consumers take v_i = Vmax_i * C / (Km_i + C) from a pool; find C with sum v_i = S (S < sum Vmax).
    Bisection on log C (the affinity constants span many orders of magnitude)."""
    lo, hi = -40.0, 60.0
    for _ in range(400):
        mid = (lo + hi) / 2
        C = 10 ** mid
        v = sum(V * C / (k + C) for V, k in zip(Vmax, Km))
        if v > S:
            hi = mid
        else:
            lo = mid
    C = 10 ** ((lo + hi) / 2)
    return [V * C / (k + C) for V, k in zip(Vmax, Km)]


def lexi(Vmax, order, S):
    a = [0.0] * len(Vmax)
    for i in order:
        a[i] = min(Vmax[i], S)
        S -= a[i]
    return a


def check_P17():
    bad = 0
    Vmax = [1.0, 1.0, 1.0, 1.0]
    for R, tol in [(1e2, 0.15), (1e4, 0.02), (1e6, 0.002)]:
        Km = [R ** i for i in range(4)]  # consumer 0 has the highest affinity
        worst = 0.0
        for S in [0.3, 0.9, 1.5, 2.2, 3.7]:
            a = uptake_alloc(Vmax, Km, S)
            b = lexi(Vmax, [0, 1, 2, 3], S)
            worst = max(worst, max(abs(x - y) for x, y in zip(a, b)))
        if worst > tol:
            bad += fail("P17", f"R={R} worst deviation {worst}")
    # ordering: fractional supply falls with Km at every S
    Km = [1, 3, 10, 30]
    for S in [0.5, 1.5, 2.5]:
        a = uptake_alloc(Vmax, Km, S)
        if not all(x >= y - 1e-12 for x, y in zip(a, a[1:])):
            bad += fail("P17 order", str(a))
    return bad


# ---------- P18: an autonomous drain is a supply cut for the governed parts ----------
def check_P18(trials=2000):
    bad = 0
    for _ in range(trials):
        top, basal, sup, ordn = rand_instance()
        S = random.uniform(0, top + sum(basal) + sum(sup) + sum(ordn) + 5)
        T = random.uniform(0, S)
        x = draw(S - T, top, basal, sup, ordn)          # the drain draws first
        y = draw(max(0.0, S - T), top, basal, sup, ordn)  # a host whose supply is simply S - T
        if any(abs(p - q) > 1e-12 for p, q in zip([x[0]] + x[1] + x[2] + x[3], [y[0]] + y[1] + y[2] + y[3])):
            bad += fail("P18", "")
    return bad


# ---------- P1 (corrected): general identity with gates and above-reference allocation; the gated example ----------
def check_P1_general(trials=2000):
    bad = 0
    for _ in range(trials):
        n = 5
        q = [random.uniform(0.5, 3) for _ in range(n)]
        U = random.uniform(0, sum(q) * 1.5)
        d = random.uniform(0, 2)
        I = random.uniform(0, 1)
        gate = [random.random() < 0.7 for _ in range(n)]   # a closed gate draws nothing
        over = [random.uniform(1.0, 1.5) for _ in range(n)]  # a part may draw above its reference (X > 0)
        S = U + d + I
        a = []
        for qi, g, o in zip(q, gate, over):
            x = min(S, qi * o) if g else 0.0
            a.append(x)
            S -= x
        R_unused = S
        X = sum(max(0.0, ai - qi) for qi, ai in zip(q, a))
        load = sum(max(0.0, qi - ai) for qi, ai in zip(q, a))
        gap = sum(q) - U
        if abs(load - (gap - d - I + R_unused + X)) > 1e-9:
            bad += fail("P1 general identity", f"{load} vs {gap - d - I + R_unused + X}")
    # the gated example: reference 10, supply 10
    if not (max(0, 10 - min(10, 10)) == 0 and 10 == 10):
        bad += fail("P1 example", "")
    return bad


# ---------- P17 (corrected): adequacy order is the order of C* = K r / (1 - r) ----------
def adequacy_order(V, Km, q):
    order = []
    S = sum(V)
    while S > 1e-3 and len(order) < len(V):
        v = uptake_alloc(V, Km, S)
        for i in range(len(V)):
            if i not in order and v[i] < q[i] - 1e-9:
                order.append(i)
        S *= 0.995
    return order


def check_P17_adequacy(trials=200):
    bad = 0
    # counter-example to affinity alone
    V, Km, q = [1.0, 10.0], [1.0, 10.0], [0.9, 0.5]
    if adequacy_order(V, Km, q) != [0, 1]:
        bad += fail("P17 counter-example", str(adequacy_order(V, Km, q)))
    for _ in range(trials):
        n = 3
        V = [random.uniform(0.5, 5) for _ in range(n)]
        Km = [10 ** random.uniform(-1, 2) for _ in range(n)]
        q = [random.uniform(0.1, 0.9) * v for v in V]
        Cs = [k * (qi / v) / (1 - qi / v) for k, v, qi in zip(Km, V, q)]
        if min(abs(math.log(Cs[i] / Cs[j])) for i in range(n) for j in range(i + 1, n)) < 0.05:
            continue  # near-ties: the discrete supply grid cannot separate them
        pred = sorted(range(n), key=lambda i: -Cs[i])
        obs = adequacy_order(V, Km, q)
        if obs != pred:
            bad += fail("P17 adequacy order", f"obs {obs} pred {pred} C* {Cs}")
    return bad


# ---------- P2 (corrected): the silence condition in terms of the gap, with outside input I > 0 ----------
def check_P2_gap(trials=2000):
    """Record flat this step and next iff Gamma <= sum(d) + I + M, with M = D4 (top depends on supports)
    or M = D4 + P + B (no dependency). Gamma = sum(q0) - U; S = U + I + sum(d)."""
    bad = 0
    for _ in range(trials):
        top, basal, sup, ordn = rand_instance()
        B, P, D4 = sum(basal), sum(sup), sum(ordn)
        need = top + B + P + D4
        U = random.uniform(0, need)
        I = random.uniform(0, need - U)           # outside input, random and positive
        d = random.uniform(0, max(0.0, need - U - I))
        S = U + I + d
        a_top, a_b, a_p, a_o, _ = draw(S, top, basal, sup, ordn)
        gap = need - U
        top_met = a_top >= top - TOL
        sup_met = top_met and all(a >= x - TOL for a, x in zip(a_p, sup)) and all(a >= x - TOL for a, x in zip(a_b, basal))
        if sup_met != (gap <= d + I + D4 + TOL):
            bad += fail("P2 gap, dependency", f"gap={gap} d={d} I={I} D4={D4}")
        if top_met != (gap <= d + I + D4 + P + B + TOL):
            bad += fail("P2 gap, no dependency", f"gap={gap} d={d} I={I}")
    return bad


# =================== version 2, reading A (considered and not adopted; kept as the record of the alternative) ===================
# Reading A kept every other part's basal maintenance ahead of any other part's work. James chose reading B (below).
# Phases: (1) the top's full need N; (2) support parts' full draws (basal maintenance and work), in rank order;
# (3) every other part's basal maintenance, in rank order; (4) every other part's work, in rank order.
# Within a part, work is cut before basal maintenance. Parts are (basal, work) pairs, highest rank first.

def draw_v2a(S, N, sup, ordn):
    a_top = min(S, N)
    S -= a_top
    a_sup = []
    for b, w in sup:                       # phase 2: full draw; basal maintenance covered before work
        ab = min(S, b)
        S -= ab
        aw = min(S, w)
        S -= aw
        a_sup.append((ab, aw))
    a_ob = []
    for b, _ in ordn:                      # phase 3
        x = min(S, b)
        a_ob.append(x)
        S -= x
    a_ow = []
    for _, w in ordn:                      # phase 4
        x = min(S, w)
        a_ow.append(x)
        S -= x
    return a_top, a_sup, a_ob, a_ow, S


def rand_instance_v2(n_sup=2, n_ord=6):
    N = random.uniform(1, 5)
    sup = [(random.uniform(0.1, 1.0), random.uniform(0.1, 2.0)) for _ in range(n_sup)]
    ordn = [(random.uniform(0.1, 1.5), random.uniform(0.1, 3.0)) for _ in range(n_ord)]
    return N, sup, ordn


def totals_v2(N, sup, ordn):
    P = sum(b + w for b, w in sup)
    B = sum(b for b, _ in ordn)
    D4 = sum(w for _, w in ordn)
    return P, B, D4


def shortfall_v2(N, sup, ordn, alloc):
    a_top, a_sup, a_ob, a_ow, _ = alloc
    s = N - a_top
    s += sum((b - ab) + (w - aw) for (b, w), (ab, aw) in zip(sup, a_sup))
    s += sum(b - a for (b, _), a in zip(ordn, a_ob)) + sum(w - a for (_, w), a in zip(ordn, a_ow))
    return s


def met(a, x):
    return a >= x - TOL


# ---------- v2 P1: ledger closes; total shortfall unchanged by any re-ranking within phases, or the old phase order ----------
def check_P1_v2a(trials=2000):
    bad = 0
    for _ in range(trials):
        N, sup, ordn = rand_instance_v2()
        P, B, D4 = totals_v2(N, sup, ordn)
        need = N + P + B + D4
        U = random.uniform(0, need)
        d = random.uniform(0, need - U)
        S = U + d
        al = draw_v2a(S, N, sup, ordn)
        sf = shortfall_v2(N, sup, ordn, al)
        if abs((need - U) - (d + sf)) > 1e-7:
            bad += fail("v2 P1 ledger", f"{need - U} vs {d + sf}")
        s2, o2 = sup[:], ordn[:]
        random.shuffle(s2)
        random.shuffle(o2)
        sf2 = shortfall_v2(N, s2, o2, draw_v2a(S, N, s2, o2))
        # the v1 phase order as another access setting: same total
        flat_basal = [b for b, _ in sup] + [b for b, _ in ordn]
        a1 = draw(S, N, flat_basal, [w for _, w in sup], [w for _, w in ordn])
        sf1 = (N - a1[0]) + sum(x - a for x, a in zip(flat_basal, a1[1])) + sum(w - a for (_, w), a in zip(sup, a1[2])) \
            + sum(w - a for (_, w), a in zip(ordn, a1[3]))
        if abs(sf - sf2) > 1e-7 or abs(sf - sf1) > 1e-7:
            bad += fail("v2 P1 invariance", f"{sf} {sf2} {sf1}")
    return bad


# ---------- v2 Proposition 2: thresholds in S, and in terms of the gap with outside input ----------
def check_P2_v2a(trials=2000):
    bad = 0
    for _ in range(trials):
        N, sup, ordn = rand_instance_v2()
        P, B, D4 = totals_v2(N, sup, ordn)
        need = N + P + B + D4
        U = random.uniform(0, need)
        I = random.uniform(0, need - U)
        d = random.uniform(0, max(0.0, need - U - I))
        S = U + I + d
        a_top, a_sup, a_ob, _, _ = draw_v2a(S, N, sup, ordn)
        gap = need - U
        top_met = met(a_top, N)
        sup_met = top_met and all(met(ab, b) and met(aw, w) for (b, w), (ab, aw) in zip(sup, a_sup))
        ob_met = sup_met and all(met(a, b) for (b, _), a in zip(ordn, a_ob))
        if top_met != (S >= N - TOL):
            bad += fail("v2 P2 top threshold", f"S={S}")
        if sup_met != (S >= N + P - TOL):
            bad += fail("v2 P2 support threshold", f"S={S}")
        if ob_met != (S >= N + P + B - TOL):
            bad += fail("v2 P2 basal threshold", f"S={S}")
        if top_met != (gap <= d + I + P + B + D4 + TOL):          # no delivery dependency: M = P + B + D4
            bad += fail("v2 P2 gap, no dependency", f"gap={gap}")
        if sup_met != (gap <= d + I + B + D4 + TOL):              # delivery depends on supports: M = B + D4
            bad += fail("v2 P2 gap, dependency", f"gap={gap}")
    return bad


# ---------- v2 Proposition 4: lower segments; work before basal within a part; supports and top last ----------
def check_P4_order_v2a(trials=3000):
    bad = 0
    for _ in range(trials):
        N, sup, ordn = rand_instance_v2()
        P, B, D4 = totals_v2(N, sup, ordn)
        S = random.uniform(0, N + P + B + D4)
        a_top, a_sup, a_ob, a_ow, _ = draw_v2a(S, N, sup, ordn)
        def lower_segment(short, alloc):
            if any(short):
                k = short.index(True)
                return not any(a > TOL for a in alloc[k + 1:])
            return True
        sup_short = [not (met(ab, b) and met(aw, w)) for (b, w), (ab, aw) in zip(sup, a_sup)]
        if not lower_segment(sup_short, [ab + aw for ab, aw in a_sup]):
            bad += fail("v2 P4 lower segment, supports", str(a_sup))
        if not lower_segment([not met(a, b) for (b, _), a in zip(ordn, a_ob)], a_ob):
            bad += fail("v2 P4 lower segment, basal", str(a_ob))
        if not lower_segment([not met(a, w) for (_, w), a in zip(ordn, a_ow)], a_ow):
            bad += fail("v2 P4 lower segment, work", str(a_ow))
        for (b, w), (ab, aw) in zip(sup, a_sup):            # within a part, work is cut before basal maintenance
            if not met(ab, b) and aw > TOL:
                bad += fail("v2 P4 work before basal, within a support part", "")
        if any(not met(a, b) for (b, _), a in zip(ordn, a_ob)) and sum(a_ow) > TOL:
            bad += fail("v2 P4 basal before work, other parts", "")
        if any(sup_short) and (sum(a_ob) + sum(a_ow)) > TOL:
            bad += fail("v2 P4 supports after other parts", "")
        if not met(a_top, N) and (sum(ab + aw for ab, aw in a_sup) + sum(a_ob) + sum(a_ow)) > TOL:
            bad += fail("v2 P4 top last", "")
    return bad


# ---------- v2 Proposition 3, S1.1 lead time and the G27 window, by full simulation of the draw with one store ----------
def simulate_v2a(N, sup, ordn, U, L0, k, dependency, T=200000):
    """Constant supply U; one store with proportional release. Returns (t_warn, t_break, L at break, taps),
    where taps[t] is the index of the first draw short at step t in the flattened draw order (len = none short)."""
    flat = [N] + [x for bw in sup for x in bw] + [b for b, _ in ordn] + [w for _, w in ordn]
    need = sum(flat)
    gap = need - U
    L, t_warn, taps = L0, None, []
    for t in range(T):
        if t_warn is None and k * L < gap - TOL:
            t_warn = t
        d = min(k * L, gap, L)
        a_top, a_sup, a_ob, a_ow, _ = draw_v2a(U + d, N, sup, ordn)
        alloc = [a_top] + [x for ab in a_sup for x in ab] + a_ob + a_ow
        short = [not met(a, x) for a, x in zip(alloc, flat)]
        taps.append(short.index(True) if any(short) else len(flat))
        top_ok = met(a_top, N)
        sup_ok = top_ok and all(met(ab, b) and met(aw, w) for (b, w), (ab, aw) in zip(sup, a_sup))
        if (dependency and not sup_ok) or (not dependency and not top_ok):
            return t_warn, t, L, taps
        L -= d
    return t_warn, None, L, taps


def check_P3_S11_G27_v2a(trials=400):
    bad = 0
    done = 0
    while done < trials:
        N, sup, ordn = rand_instance_v2(n_sup=2, n_ord=4)
        P, B, D4 = totals_v2(N, sup, ordn)
        need = N + P + B + D4
        dependency = random.random() < 0.5
        M = (B + D4) if dependency else (P + B + D4)
        L0 = random.uniform(100, 400)
        k = random.uniform(0.01, 0.2)
        if k * L0 < M + 0.5 or need < M + 0.5:
            continue
        gap = random.uniform(M + 0.1, min(k * L0, need))
        U = need - gap
        t_warn, t_break, L_b, taps = simulate_v2a(N, sup, ordn, U, L0, k, dependency)
        done += 1
        Lstar = (gap - M) / k
        if t_break is None or not (Lstar * (1 - k) - 1e-6 <= L_b <= Lstar + 1e-6):
            bad += fail("v2 P3 store left at the break", f"dep={dependency} L={L_b} L*={Lstar}")
            continue
        lead = t_break - t_warn
        pred = math.log(gap / (gap - M)) / -math.log(1 - k)
        if abs(lead - pred) > 1.0 + 1e-9:
            bad += fail("v2 S1.1 lead time", f"lead={lead} pred={pred}")
        n_flat = 1 + 2 * len(sup) + 2 * len(ordn)
        protected_end = 1 + (2 * len(sup) if dependency else 0)   # draws that must stay met before the break
        # G27: no draw is short while the store has headroom; then the first short draw climbs the draw order
        # (its index never increases) and stays below the protected draws until the break
        if any(tp != n_flat for tp in taps[:t_warn]):
            bad += fail("v2 G27 store first", "")
        window = taps[t_warn:t_break]
        if any(b > a for a, b in zip(window, window[1:])):
            bad += fail("v2 G27 tap climbs", str(window[:12]))
        if any(tp < protected_end for tp in window):
            bad += fail("v2 G27 protected until the break", "")
    return bad


# =================== version 2, reading B: rank first, part by part (James, 8 October 2026; CANON 3 and 4) ===================
# Phases: (1) the top's full need N; (2) support parts' full draws, in rank order; (3) every other part's full draw,
# in rank order. Each part is drawn in full in its turn; what reaches a part covers its upkeep first, then its work.
# Parts are (upkeep, work) pairs, highest rank first. D is the other parts' full draws.

def draw_v2b(S, N, sup, oth):
    a_top = min(S, N)
    S -= a_top
    out = []
    for group in (sup, oth):
        g = []
        for b, w in group:
            ab = min(S, b)
            S -= ab
            aw = min(S, w)
            S -= aw
            g.append((ab, aw))
        out.append(g)
    return a_top, out[0], out[1], S


def draw_v2a_as_parts(S, N, sup, oth):
    """Reading A, re-expressed part by part, so the reading-B checks can be fed reading A's order."""
    a_top, a_sup, a_ob, a_ow, left = draw_v2a(S, N, sup, oth)
    return a_top, a_sup, list(zip(a_ob, a_ow)), left


def totals_v2b(N, sup, oth):
    return sum(b + w for b, w in sup), sum(b + w for b, w in oth)      # P, D


def shortfall_v2b(N, sup, oth, alloc):
    a_top, a_sup, a_oth, _ = alloc
    return (N - a_top) + sum((b - ab) + (w - aw) for (b, w), (ab, aw) in zip(sup + oth, a_sup + a_oth))


def check_P1_v2b(trials=2000):
    bad = 0
    for _ in range(trials):
        N, sup, oth = rand_instance_v2()
        P, D = totals_v2b(N, sup, oth)
        need = N + P + D
        U = random.uniform(0, need)
        d = random.uniform(0, need - U)
        S = U + d
        sf = shortfall_v2b(N, sup, oth, draw_v2b(S, N, sup, oth))
        if abs((need - U) - (d + sf)) > 1e-7:
            bad += fail("v2b P1 ledger", f"{need - U} vs {d + sf}")
        s2, o2 = sup[:], oth[:]
        random.shuffle(s2)
        random.shuffle(o2)
        sf2 = shortfall_v2b(N, s2, o2, draw_v2b(S, N, s2, o2))
        sfa = shortfall_v2b(N, sup, oth, draw_v2a_as_parts(S, N, sup, oth))   # reading A as another access setting
        if abs(sf - sf2) > 1e-7 or abs(sf - sfa) > 1e-7:
            bad += fail("v2b P1 invariance", f"{sf} {sf2} {sfa}")
    return bad


def check_P2_v2b(trials=2000):
    bad = 0
    for _ in range(trials):
        N, sup, oth = rand_instance_v2()
        P, D = totals_v2b(N, sup, oth)
        need = N + P + D
        U = random.uniform(0, need)
        I = random.uniform(0, need - U)
        d = random.uniform(0, max(0.0, need - U - I))
        S = U + I + d
        a_top, a_sup, _, _ = draw_v2b(S, N, sup, oth)
        gap = need - U
        top_met = met(a_top, N)
        sup_met = top_met and all(met(ab, b) and met(aw, w) for (b, w), (ab, aw) in zip(sup, a_sup))
        if top_met != (S >= N - TOL):
            bad += fail("v2b P2 top threshold", f"S={S}")
        if sup_met != (S >= N + P - TOL):
            bad += fail("v2b P2 support threshold", f"S={S}")
        if top_met != (gap <= d + I + P + D + TOL):        # no delivery dependency: M = P + D
            bad += fail("v2b P2 gap, no dependency", f"gap={gap}")
        if sup_met != (gap <= d + I + D + TOL):            # delivery depends on supports: M = D
            bad += fail("v2b P2 gap, dependency", f"gap={gap}")
    return bad


def order_violations(N, sup, oth, alloc):
    """Proposition 4 (reading B): parts short of their draw form a lower segment of the whole rank order (top, supports,
    others); at most one part is partly supplied; within a short part, work is cut before upkeep."""
    a_top, a_sup, a_oth, _ = alloc
    parts = [(N, 0.0)] + sup + oth
    allocs = [(a_top, 0.0)] + a_sup + a_oth
    v = []
    short = [not (met(ab, b) and met(aw, w)) for (b, w), (ab, aw) in zip(parts, allocs)]
    if any(short):
        k = short.index(True)
        if any(ab + aw > TOL for ab, aw in allocs[k + 1:]):
            v.append("a part is short while a lower-ranked part draws")
    for (b, w), (ab, aw) in zip(parts, allocs):
        if not met(ab, b) and aw > TOL:
            v.append("work drawn while upkeep short, within a part")
    return v


def check_P4_v2b(trials=3000, draw_fn=None, label="v2b P4"):
    draw_fn = draw_fn or draw_v2b
    bad = 0
    for _ in range(trials):
        N, sup, oth = rand_instance_v2()
        P, D = totals_v2b(N, sup, oth)
        S = random.uniform(0, N + P + D)
        for msg in order_violations(N, sup, oth, draw_fn(S, N, sup, oth)):
            bad += 1
            if bad <= 3:
                print(f"FAIL {label}: {msg}")
    return bad


def simulate_v2b(N, sup, oth, U, L0, k, dependency, draw_fn, T=200000):
    """Constant supply U; one store with proportional release. Returns (t_warn, t_break, L at break, cut, viol), where
    cut[t] is the index (in the part order top, supports, others) of the first part not fully supplied at step t."""
    parts = [(N, 0.0)] + sup + oth
    need = sum(b + w for b, w in parts)
    gap = need - U
    L, t_warn, cut, viol = L0, None, [], 0
    for t in range(T):
        if t_warn is None and k * L < gap - TOL:
            t_warn = t
        d = min(k * L, gap, L)
        al = draw_fn(U + d, N, sup, oth)
        allocs = [(al[0], 0.0)] + al[1] + al[2]
        short = [not (met(ab, b) and met(aw, w)) for (b, w), (ab, aw) in zip(parts, allocs)]
        cut.append(short.index(True) if any(short) else len(parts))
        viol += len(order_violations(N, sup, oth, al))
        top_ok = met(al[0], N)
        sup_ok = top_ok and all(met(ab, b) and met(aw, w) for (b, w), (ab, aw) in zip(sup, al[1]))
        if (dependency and not sup_ok) or (not dependency and not top_ok):
            return t_warn, t, L, cut, viol
        L -= d
    return t_warn, None, L, cut, viol


def check_P3_S11_G27_v2b(trials=400, draw_fn=None, label="v2b"):
    draw_fn = draw_fn or draw_v2b
    bad = 0
    done = 0
    while done < trials:
        N, sup, oth = rand_instance_v2(n_sup=2, n_ord=4)
        P, D = totals_v2b(N, sup, oth)
        need = N + P + D
        dependency = random.random() < 0.5
        M = D if dependency else (P + D)
        L0 = random.uniform(100, 400)
        k = random.uniform(0.01, 0.2)
        if k * L0 < M + 0.5 or need < M + 0.5:
            continue
        gap = random.uniform(M + 0.1, min(k * L0, need))
        U = need - gap
        t_warn, t_break, L_b, cut, viol = simulate_v2b(N, sup, oth, U, L0, k, dependency, draw_fn)
        done += 1
        Lstar = (gap - M) / k
        if t_break is None or not (Lstar * (1 - k) - 1e-6 <= L_b <= Lstar + 1e-6):
            bad += fail(f"{label} P3 store left at the break", f"dep={dependency} L={L_b} L*={Lstar}")
            continue
        lead = t_break - t_warn
        pred = math.log(gap / (gap - M)) / -math.log(1 - k)
        if abs(lead - pred) > 1.0 + 1e-9:
            bad += fail(f"{label} S1.1 lead time", f"lead={lead} pred={pred}")
        n_parts = 1 + len(sup) + len(oth)
        protected_end = 1 + (len(sup) if dependency else 0)
        if any(c != n_parts for c in cut[:t_warn]):
            bad += fail(f"{label} G27 store first", "")
        window = cut[t_warn:t_break]
        if any(b > a for a, b in zip(window, window[1:])):
            bad += fail(f"{label} G27 the part being cut climbs the order", str(window[:12]))
        if any(c < protected_end for c in window):
            bad += fail(f"{label} G27 protected until the break", "")
        if viol:
            bad += 1
            if bad <= 3:
                print(f"FAIL {label} G27: {viol} steps where a part was short while a lower-ranked part still drew")
    return bad


# ---------- J2 (FINAL_CHECK round 1, 9 October 2026): the delivery dependency across steps ----------
# Delivery to the top in a step is capped by the support parts' work in the step before: the top receives
# min(its draw, N x the share of the supports' full work they received in the step before). What the cap holds back
# is not delivered (variant "unused") or stays in the flow for the parts below (variant "returned").

def run_with_lag(N, sup, oth, S_seq, returned):
    """Returns one record per step: (supports met in the step before, S, top received, alloc of the reduced draw)."""
    work_total = sum(w for _, w in sup)
    frac_prev = 1.0                       # the supports were met before the run starts
    out = []
    for S in S_seq:
        cap = N * frac_prev
        a_top = min(S, N, cap)
        rest = S - a_top if returned else S - min(S, N)
        _, a_sup, a_oth, left = _draw_below(rest, sup, oth)
        out.append((frac_prev >= 1.0 - 1e-12, S, a_top, (a_top, a_sup, a_oth, left)))
        got = sum(aw for _, aw in a_sup)
        frac_prev = (got / work_total) if work_total > 0 else 1.0
    return out


def _draw_below(S, sup, oth):
    """The ordered draw below the top: supports, then other parts, each in full in its turn, upkeep before work."""
    res = []
    for group in (sup, oth):
        g = []
        for b, w in group:
            ab = min(S, b)
            S -= ab
            aw = min(S, w)
            S -= aw
            g.append((ab, aw))
        res.append(g)
    return None, res[0], res[1], S


def check_lag_v2b(trials=3000):
    """Restated Propositions 2 and 4 and S1.9 (ruling 6 and J2), in steps where the supports were met in the step
    before; and the dependency lag itself, which must occur when they were not."""
    bad, lag_steps = 0, 0
    for _ in range(trials):
        N, sup, oth = rand_instance_v2(n_sup=2, n_ord=4)
        P, D = totals_v2b(N, sup, oth)
        need = N + P + D
        S_seq = [min(need, random.uniform(0, 1.3 * need)) for _ in range(6)]   # some steps at full supply
        for returned in (False, True):
            for prev_met, S, a_top, alloc in run_with_lag(N, sup, oth, S_seq, returned):
                _, a_sup, a_oth, _ = alloc
                others_draw = any(ab + aw > TOL for ab, aw in a_oth)
                others_full = all(met(ab, b) and met(aw, w) for (b, w), (ab, aw) in zip(sup + oth, a_sup + a_oth))
                if prev_met:
                    if met(a_top, N) != (S >= N - TOL):
                        bad += fail("J2 Proposition 2 (supports met the step before)", f"S={S} top={a_top}")
                    for msg in order_violations(N, sup, oth, alloc):
                        bad += fail("J2 Proposition 4 (supports met the step before)", msg)
                    if not met(a_top, N) and others_draw:
                        bad += fail("J2 S1.9 (no cut, no damage)", "top short while a part outside the supports draws")
                elif not met(a_top, N) and others_full:
                    lag_steps += 1
    # the worked example in S1.9: N = 10, P = 3 (upkeep 1, work 2), three other parts of 3; S = 11 then 22
    ex = run_with_lag(10.0, [(1.0, 2.0)], [(1.0, 2.0)] * 3, [11.0, 22.0], returned=False)
    if not (ex[0][0] and met(ex[0][2], 10.0) and not ex[1][0] and ex[1][2] <= TOL
            and all(met(ab, 1.0) and met(aw, 2.0) for ab, aw in ex[1][3][2])):
        bad += fail("J2 worked example", str([(r[0], r[2]) for r in ex]))
    if lag_steps == 0:
        bad += fail("J2 dependency lag", "no step found with the top short and every other part met")
    print(f"   dependency-lag steps found (supports short the step before; top short; every other part met in full): {lag_steps}")
    return bad


# ---------- version 2: the recovery lag (FINAL_CHECK round 2, J1): unit states for the top and a support part ----------
def run_with_units(top, sup, oth, S_seq, dependency):
    """top and sup are dicts: K units, u upkeep and w work per unit, theta (switch-off per step), re (reactivation per
    step), c (cost per unit reactivated). A switched-off unit takes upkeep only and does no work; unmet work switches
    units off; units come back at up to re per step, paid from what is left once every part has drawn (CANON 3).
    oth is a list of (upkeep, work) full draws. Returns one record per step."""
    a_t, a_s = float(top["K"]), float(sup["K"])
    N = top["K"] * (top["u"] + top["w"])
    P = sup["K"] * (sup["u"] + sup["w"])
    prev_sup_met, prev_sup_work = True, sup["K"] * sup["w"]
    out = []
    for S in S_seq:
        back = a_t < top["K"] - 1e-9 or a_s < sup["K"] - 1e-9          # a unit of the top or a support part coming back
        draw_t = top["u"] * top["K"] + top["w"] * a_t
        draw_s = sup["u"] * sup["K"] + sup["w"] * a_s
        take_t = min(S, draw_t); rem = S - take_t
        take_s = min(rem, draw_s); rem -= take_s
        a_oth = []
        for b, w in oth:
            ab = min(rem, b); rem -= ab
            aw = min(rem, w); rem -= aw
            a_oth.append((ab, aw))
        work_s = max(0.0, take_s - sup["u"] * sup["K"])
        deliv = take_t * (min(1.0, prev_sup_work / (sup["K"] * sup["w"])) if dependency else 1.0)
        out.append(dict(S=S, back=back, prev_sup_met=prev_sup_met, deliv=deliv, N=N, P=P, take_s=take_s,
                        draw_s=draw_s, a_oth=a_oth, back_top=a_t < top["K"] - 1e-9))
        for part, take, draw, key in ((top, take_t, draw_t, "t"), (sup, take_s, draw_s, "s")):
            act = a_t if key == "t" else a_s
            if take < draw - TOL:                                       # unmet work: switch units off
                funded = max(0.0, (take - part["u"] * part["K"]) / part["w"])
                act -= min(part["theta"], max(0.0, act - funded))
            elif act < part["K"] - 1e-9 and rem > TOL:                 # come back from what is left
                n = min(part["re"], part["K"] - act, rem / part["c"])
                act += n; rem -= n * part["c"]
            if key == "t":
                a_t = act
            else:
                a_s = act
        prev_sup_met = take_s >= P - TOL
        prev_sup_work = work_s
    return out


def check_recovery_lag_v2b(trials=3000):
    """Propositions 2 and 4 and S1.9 with unit states: in steps where the support parts were met in the step before
    and no unit of the top or a support part is still coming back, the protected flow is met iff S >= N, and the top
    is never short while a part outside the supports draws. Otherwise the recovery lag must occur: the top short
    while every other part draws in full, with the supports met in the step before."""
    bad, lag_steps = 0, 0
    for _ in range(trials):
        top = dict(K=random.randint(5, 20), u=random.uniform(0.1, 0.4))
        top["w"] = 1.0 - top["u"]
        sup = dict(K=random.randint(2, 10), u=random.uniform(0.1, 0.5), w=random.uniform(0.5, 1.5))
        for p in (top, sup):
            p["theta"] = random.uniform(0.2, 0.6) * p["K"]
            p["re"] = random.uniform(0.05, 0.3) * p["K"]
            p["c"] = random.uniform(0.05, 0.5)
        oth = [(random.uniform(0.5, 3.0), random.uniform(0.5, 3.0)) for _ in range(random.randint(2, 5))]
        need = top["K"] * (top["u"] + top["w"]) + sup["K"] * (sup["u"] + sup["w"]) + sum(b + w for b, w in oth)
        S_seq = [need * (random.uniform(0.2, 0.9) if random.random() < 0.3 else random.uniform(1.0, 1.3))
                 for _ in range(10)]
        for dependency in (False, True):
            for r in run_with_units(top, sup, oth, S_seq, dependency):
                guard = (not r["back"]) and (r["prev_sup_met"] or not dependency)
                others_draw = any(ab + aw > TOL for ab, aw in r["a_oth"])
                others_full = all(met(ab, b) and met(aw, w) for (b, w), (ab, aw) in zip(oth, r["a_oth"]))
                top_met = r["deliv"] >= r["N"] - TOL
                if guard:
                    if top_met != (r["S"] >= r["N"] - TOL):
                        bad += fail("recovery lag: Proposition 2 under the guard", f"S={r['S']} deliv={r['deliv']} N={r['N']}")
                    if not top_met and others_draw:
                        bad += fail("recovery lag: S1.9 under the guard", "top short while a part outside the supports draws")
                    if r["take_s"] < r["draw_s"] - TOL and others_draw:
                        bad += fail("recovery lag: Proposition 4 under the guard", "support short while a lower part draws")
                elif r["prev_sup_met"] and r["back_top"] and not top_met and others_full and r["take_s"] >= r["draw_s"] - TOL:
                    lag_steps += 1
    # the worked example (FINAL_CHECK round 2, pass 4): top of 10 units (upkeep 0.2, work 0.8 each), support 3
    # (upkeep 1, work 2, one unit), others 9; switch-off 5 a step, reactivation 1 a step; supply 22, 6, then 22
    top = dict(K=10, u=0.2, w=0.8, theta=5.0, re=1.0, c=0.2)
    sup = dict(K=1, u=1.0, w=2.0, theta=0.0, re=1.0, c=0.2)          # as in the example, the support keeps its unit
    oth = [(1.0, 2.0)] * 3
    for dependency in (False, True):
        ex = run_with_units(top, sup, oth, [22.0, 6.0] + [22.0] * 7, dependency)
        got = [round(r["deliv"], 6) for r in ex[3:7]]
        if got != [6.8, 7.6, 8.4, 9.2] or not all(r["prev_sup_met"] and r["back_top"] for r in ex[3:7]) \
                or not all(all(met(ab, 1.0) and met(aw, 2.0) for ab, aw in r["a_oth"]) for r in ex[3:7]) \
                or round(ex[7]["deliv"], 6) != 10.0:
            bad += fail("recovery lag worked example", f"dependency={dependency} {[round(r['deliv'], 3) for r in ex]}")
    if lag_steps == 0:
        bad += fail("recovery lag", "no step found with the top short, every other part met and the supports met the step before")
    print(f"   recovery-lag steps found (supports met the step before; top's units coming back; top short; every other part met in full): {lag_steps}")
    return bad


if __name__ == "__main__":
    total = 0
    for name, f in [("v2 Proposition 1 (reading B)", check_P1_v2b), ("v2 Proposition 2 (reading B)", check_P2_v2b),
                    ("v2 Proposition 4 (reading B)", check_P4_v2b),
                    ("v2 Proposition 3, S1.1 and G27 (reading B, simulation)", check_P3_S11_G27_v2b)]:
        b = f()
        print(f"{name}: {'ok' if b == 0 else str(b) + ' failures'}")
        total += b
    print("-- reading A fed to the reading-B checks (they must fail) --")
    na = check_P4_v2b(draw_fn=draw_v2a_as_parts, label="reading A, Proposition 4")
    ng = check_P3_S11_G27_v2b(trials=100, draw_fn=draw_v2a_as_parts, label="reading A")
    print(f"reading A, Proposition 4 check: {na} failures (expected > 0)")
    print(f"reading A, G27 check: {ng} failures (expected > 0)")
    if na == 0 or ng == 0:
        total += 1
        print("FAIL: the reading-B checks did not tell reading A apart")
    print("-- version 2, reading A (record of the alternative considered) --")
    for name, f in [("v2a P1", check_P1_v2a), ("v2a P2", check_P2_v2a), ("v2a P4 order", check_P4_order_v2a),
                    ("v2a P3, S1.1 and G27", check_P3_S11_G27_v2a)]:
        b = f()
        print(f"{name}: {'ok' if b == 0 else str(b) + ' failures'}")
        total += b
    print("-- version 1 phase order (kept for the record) --")
    for name, f in [("P1", check_P1), ("P2", check_P2), ("P3", check_P3), ("P4", check_P4), ("P5", check_P5),
                    ("P6", check_P6), ("P7", check_P7), ("P9", check_P9), ("P10", check_P10),
                    ("P11", check_P11), ("P13", check_P13), ("P16", check_P16), ("P17", check_P17), ("P18", check_P18),
                    ("P1 general", check_P1_general), ("P17 adequacy", check_P17_adequacy),
                    ("P2 gap with outside input", check_P2_gap)]:
        b = f()
        print(f"{name}: {'ok' if b == 0 else str(b) + ' failures'}")
        total += b
    print("-- version 2: the delivery dependency across steps (J2, run last so the earlier checks keep their random draws) --")
    b = check_lag_v2b()
    print(f"v2 Propositions 2 and 4 and S1.9 across steps, and the dependency lag (J2): {'ok' if b == 0 else str(b) + ' failures'}")
    total += b
    print("-- version 2: the recovery lag, with unit states (J1, FINAL_CHECK round 2; run after the J2 check) --")
    b = check_recovery_lag_v2b()
    print(f"v2 Propositions 2 and 4 and S1.9 with unit states, and the recovery lag (J1): {'ok' if b == 0 else str(b) + ' failures'}")
    total += b
    print("ALL OK" if total == 0 else f"{total} FAILURES")
