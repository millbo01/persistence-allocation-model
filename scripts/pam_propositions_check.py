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


if __name__ == "__main__":
    total = 0
    for name, f in [("P1", check_P1), ("P2", check_P2), ("P3", check_P3), ("P4", check_P4), ("P5", check_P5),
                    ("P6", check_P6), ("P7", check_P7), ("P9", check_P9), ("P10", check_P10)]:
        b = f()
        print(f"{name}: {'ok' if b == 0 else str(b) + ' failures'}")
        total += b
    print("ALL OK" if total == 0 else f"{total} FAILURES")
