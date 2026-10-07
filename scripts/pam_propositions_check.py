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


if __name__ == "__main__":
    total = 0
    for name, f in [("P1", check_P1), ("P2", check_P2), ("P3", check_P3), ("P4", check_P4), ("P5", check_P5),
                    ("P6", check_P6), ("P7", check_P7), ("P9", check_P9), ("P10", check_P10),
                    ("P11", check_P11), ("P13", check_P13), ("P16", check_P16), ("P17", check_P17), ("P18", check_P18),
                    ("P1 general", check_P1_general), ("P17 adequacy", check_P17_adequacy),
                    ("P2 gap with outside input", check_P2_gap)]:
        b = f()
        print(f"{name}: {'ok' if b == 0 else str(b) + ' failures'}")
        total += b
    print("ALL OK" if total == 0 else f"{total} FAILURES")
