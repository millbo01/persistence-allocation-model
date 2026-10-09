"""Figures for the PAM paper (and a square version for a LinkedIn post). Written 8 October 2026.

Usage: python scripts/make_figures.py
Output: papers/pam-model/figures/ (PNG at 300 dpi and SVG)

Every quantity is computed from the reduced form in the paper (Section 3.2), using the same ordered draw as
scripts/pam_propositions_check.py; nothing is fitted. The PT1 panel reads tests/results/PT1/summary.json.
"""
import json
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "papers", "pam-model", "figures")
os.makedirs(OUT, exist_ok=True)

# Reference palette (light mode), categorical slots in fixed order; text in ink tokens, never series colour.
S1, S2, S3, S4 = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
INK, INK2, MUTED, GRID, SURF = "#0b0b0b", "#52514e", "#8a8984", "#e6e5e1", "#ffffff"
plt.rcParams.update({
    "font.family": ["Segoe UI", "DejaVu Sans"], "font.size": 9.5, "text.color": INK,
    "axes.edgecolor": MUTED, "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
    "axes.spines.top": False, "axes.spines.right": False, "axes.linewidth": 0.6,
    "xtick.major.width": 0.6, "ytick.major.width": 0.6, "axes.grid": True, "grid.color": GRID,
    "grid.linewidth": 0.6, "axes.axisbelow": True, "figure.facecolor": SURF, "axes.facecolor": SURF,
    "savefig.facecolor": SURF, "svg.fonttype": "none",
})


def save(fig, name):
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), dpi=300, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)


def draw(S, needs):
    """Ordered draw: each need in order takes min(remaining, need)."""
    out = []
    for n in needs:
        a = min(S, n)
        out.append(a)
        S -= a
    return out


# ---------------------------------------------------------------- Figure 1: the architecture
def fig_architecture():
    fig, ax = plt.subplots(figsize=(7.4, 5.0))
    ax.set_xlim(0, 100)
    ax.set_ylim(-4, 64)
    ax.axis("off")

    def box(x, y, w, h, title, body="", fc="#f4f6f9", tsize=9.5, bsize=8, bgap=5.6):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=1.2",
                                    fc=fc, ec=MUTED, lw=0.9))
        ax.text(x + w / 2, y + h - 2.0, title, ha="center", va="top", fontsize=tsize, fontweight="bold", color=INK)
        if body:
            ax.text(x + w / 2, y + h - bgap, body, ha="center", va="top", fontsize=bsize, color=INK2, linespacing=1.3)

    def arrow(p, q, color=INK2, lw=1.1, ls="-", rad=0.0):
        ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=10, color=color, lw=lw,
                                     linestyle=ls, connectionstyle=f"arc3,rad={rad}", shrinkA=2, shrinkB=2))

    # system boundary
    ax.add_patch(FancyBboxPatch((16, 9.5), 82.5, 53.5, boxstyle="round,pad=0.2,rounding_size=1.5",
                                fc="none", ec=MUTED, lw=0.8, ls=(0, (4, 3))))
    ax.text(97.5, 10.4, "System boundary", fontsize=7.5, color=MUTED, style="italic", ha="right", va="bottom")

    # inputs (left), shared flow and stores (centre-left)
    box(0.5, 39.5, 12.5, 12, "Supply", "through the\nintake", fc="#eef5ee", bsize=7.6)
    box(0.5, 23.5, 12.5, 12, "Outside", "input across\nthe boundary", fc="#eef5ee", bsize=7.6)
    box(21, 27, 18, 20, "Shared flow", "what reaches\nthe parts this\nstep; what a\npart does not\ndraw stays in\nthe flow", fc="#f4f6f9")
    box(21, 11.5, 18, 12, "Stores", "drawn first; release\nlimited (proportional\nby default)", fc="#eaf1fb", bsize=7.4)
    arrow((13.2, 45.5), (20.8, 42))
    arrow((13.2, 29.5), (20.8, 33))
    arrow((30, 23.7), (30, 26.8))
    ax.text(31, 25.2, "store draw", fontsize=7, color=INK2, va="center")

    # governor (top)
    box(24, 49.4, 31, 12, "Governor", "holds its targets by setting access:\nstore release, intake, gates, routes and\nthe access of each part whose access it sets", fc="#fff5ec", bsize=6.4, bgap=4.8)
    arrow((30, 49.2), (30, 47.3), color=S2, ls=(0, (3, 2)))

    # ordered draw ladder (right)
    lx, lw_, lh = 61.5, 33.5, 5.4
    ax.text(lx + lw_ / 2 + 2, 57.5, "The ordered draw", ha="center", fontsize=8.6, color=INK, fontweight="bold")
    ax.text(lx + lw_ / 2 + 2, 54.6, "each setting met in order of priority", ha="center", fontsize=7.4, color=INK2)
    steps = [("1  The top", "the protected flow; others limited first"),
             ("2  Supports and the intake", "full draws, in rank order"),
             ("3  Other parts, by rank", "full draws, upkeep before work"),
             ("4  What is left", "rebuild, or refill stores, by marginal value")]
    ys = []
    for i, (tt, b) in enumerate(steps):
        y = 40.5 - i * (lh + 1.0)
        ys.append(y)
        ax.add_patch(FancyBboxPatch((lx, y), lw_, lh, boxstyle="round,pad=0.15,rounding_size=0.8",
                                    fc="#fff5ec" if i == 0 else "#f4f6f9", ec=MUTED, lw=0.7))
        ax.text(lx + 1.4, y + lh / 2 + 0.95, tt, fontsize=8.1, fontweight="bold", va="center", color=INK)
        ax.text(lx + 1.4, y + lh / 2 - 1.25, b, fontsize=7.1, va="center", color=INK2)
    arrow((39.2, 44), (lx - 0.2, ys[0] + lh / 2))
    ax.text(50, 44.6, "access by\npriority", fontsize=7, color=INK2, ha="center", va="bottom")
    # the governor sets the access of the parts below the top (boxes 2 and 3), not the top's
    gx, gy = 97.2, 60.2
    ax.plot([55.4, gx, gx], [gy, gy, ys[2] + lh / 2], color=S2, lw=1.1, ls=(0, (3, 2)))
    for i in (1, 2):
        arrow((gx, ys[i] + lh / 2), (lx + lw_ + 0.2, ys[i] + lh / 2), color=S2, ls=(0, (3, 2)))
    ax.text(76, gy + 0.5, "sets the access it controls", fontsize=7, color=INK2, ha="center", va="bottom")
    # refill: the last step back to the stores (below the arrow's foot, so the two do not cross)
    arrow((lx - 0.2, ys[3] + 1.6), (39.4, ys[3] + 1.6), ls=(0, (3, 2)), color=S1)
    ax.text(50, ys[3] + 0.4, "refill", fontsize=7, color=INK2, ha="center", va="top")
    # access is cut from the lowest-ranked part up
    s0, s1 = ys[3] + 0.7 * lh, ys[1] + lh
    ax.add_patch(FancyArrowPatch((59.6, s0), (59.6, s1), arrowstyle="-|>", mutation_scale=10, color=S2, lw=1.5))
    ax.text(58.4, (s0 + s1) / 2, "under scarcity, access\nis cut from the lowest-\nranked part up", rotation=90,
            fontsize=7.2, color=INK2, ha="right", va="center", linespacing=1.2)

    # footer: ledger, residue, collapse
    ax.text(0.5, 5.2, "The resource ledger:", fontsize=8, fontweight="bold", color=INK, va="center")
    ax.text(21.0, 5.2, "with the flow fully used and no part above its reference: gap = store draw + outside input + shortfall "
            "at named parts. Access decides which parts go short, not how much.", fontsize=6.9, color=INK2, va="center")
    ax.text(0.5, 1.4, "Residue in units:", fontsize=8, fontweight="bold", color=INK, va="center")
    ax.text(21.0, 1.4, "switched off (route back kept) → lost (rebuildable) → scarred (lost for good).",
            fontsize=7.6, color=INK2, va="center")
    ax.text(0.5, -2.4, "Failure:", fontsize=8, fontweight="bold", color=INK, va="center")
    ax.text(21.0, -2.4, "collapse when the protected flow cannot be met or a non-bypassable link is cut; death only when no route back remains.",
            fontsize=7.6, color=INK2, va="center")
    save(fig, "fig1_architecture")


# ---------------------------------------------------------------- Figure 2: the law (Proposition 1)
def law_data():
    ref = {"A": 3.0, "B": 3.0, "C": 3.0, "D": 3.0}

    def shortfall(order, supply):
        got = dict(zip(order, draw(supply, [ref[p] for p in order])))
        return {p: ref[p] - got[p] for p in "ABCD"}
    return [("Short by 5 units:\nrank A, B, C, D", shortfall("ABCD", 7.0)),
            ("Part D's deficit corrected,\nno resource added", shortfall("DABC", 7.0)),
            ("2 units of\nresource added", shortfall("ABCD", 9.0))]


def plot_law(ax, title_size=10.5):
    cols = {"A": S1, "B": S2, "C": S3, "D": S4}
    data = law_data()
    for i, (lab, sf) in enumerate(data):
        bottom = 0.0
        for p in "ABCD":
            v = sf[p]
            if v <= 0:
                continue
            ax.bar(i, v - 0.06, bottom=bottom + 0.03, width=0.55, color=cols[p], edgecolor=SURF, linewidth=1.5)
            ax.text(i, bottom + v / 2, f"Part {p}\n{v:g}", ha="center", va="center", fontsize=8.2, color=INK,
                    fontweight="bold")
            bottom += v
        ax.text(i, bottom + 0.25, f"total {bottom:g}", ha="center", va="bottom", fontsize=9, color=INK)
    ax.set_xticks(range(3))
    ax.set_xticklabels([d[0] for d in data], fontsize=8.6)
    ax.set_ylabel("Total shortfall, by the part that goes short (units)")
    ax.set_ylim(0, 6.6)
    ax.grid(axis="x", visible=False)
    ax.tick_params(axis="x", length=0)


def fig_law():
    fig, ax = plt.subplots(figsize=(6.4, 3.9))
    plot_law(ax)
    save(fig, "fig2_law")


# ---------------------------------------------------------------- Figure 3: the silence and the break
def silence_series(T=48):
    """Reading B (version 2): the top, then the support part in full, then the other parts A, B, C in full, in rank
    order; within each part, upkeep before work. Delivery to the top depends on the support part's work one step later."""
    N = 10.0
    sup = (1.0, 2.0)                                # (upkeep, work)
    others = [(1.0, 2.0), (1.0, 2.0), (1.0, 2.0)]   # parts A, B, C in rank order
    P, D = sum(sup), sum(b + w for b, w in others)
    U = 10.0
    need = N + P + D
    gap = need - U
    L, k = 300.0, 0.08
    rows, sup_prev = [], 1.0
    for t in range(T):
        d = min(k * L, gap, L)
        a = draw(U + d, [N, *sup] + [x for bw in others for x in bw])
        flow = sup_prev                             # delivery this step depends on last step's support part
        sup_prev = min(1.0, a[2] / sup[1])            # delivery depends on the support part's work
        part = lambda i: 100 * (a[3 + 2 * i] + a[4 + 2 * i]) / sum(others[i])
        rows.append(dict(t=t, record=100 * flow, store=100 * L / 300.0, A=part(0), B=part(1), C=part(2)))
        L -= d
    # Proposition 3: with delivery dependent on the support part, M is the other parts' full draws (D)
    lstar_pct = 100 * (gap - D) / k / 300.0
    return rows, lstar_pct


def fig_silence():
    rows, lstar = silence_series()
    t = [r["t"] for r in rows]
    brk = next(r["t"] for r in rows if r["record"] < 99.9)
    fig, axs = plt.subplots(3, 1, figsize=(6.4, 5.6), sharex=True,
                            gridspec_kw={"height_ratios": [1, 1, 1.3], "hspace": 0.32})
    axs[0].plot(t, [r["record"] for r in rows], color=INK, lw=2)
    axs[0].set_ylabel("Protected flow\n(% of the top's need)")
    axs[1].plot(t, [r["store"] for r in rows], color=S1, lw=2)
    axs[1].set_ylabel("Store\n(% of start)")
    axs[1].axhline(lstar, color=MUTED, lw=0.8, ls=(0, (1, 2)))
    axs[1].text(brk + 0.8, lstar + 22, "store when the margin is used up:\n" + r"$L^{*}=(\Gamma-M)/k$", fontsize=8,
                color=INK2, va="bottom", linespacing=1.3)
    names = {"A": "part A (ranked first)", "B": "part B", "C": "part C (ranked last)"}
    for (key, c), lev in zip((("A", S1), ("B", S2), ("C", S3)), (35, 50, 65)):
        axs[2].plot(t, [r[key] for r in rows], color=c, lw=2, label=names[key])
        # direct label on the line, at a staggered height so the three labels never meet
        j = next(i for i, r in enumerate(rows) if r[key] < lev)
        y0, y1 = rows[j - 1][key], rows[j][key]
        x_at = t[j - 1] + (y0 - lev) / (y0 - y1)
        axs[2].text(x_at, lev, f"part {key}", fontsize=7.6, color=INK2, ha="center", va="center",
                    bbox=dict(boxstyle="round,pad=0.15", fc=SURF, ec="none"))
    axs[2].legend(loc="upper right", frameon=False, fontsize=7.6, handlelength=1.6, labelcolor=INK2)
    axs[2].set_ylabel("Supply reaching\nlower parts (%)")
    axs[2].set_xlabel("Time (steps), constant gap between need and supply")
    for ax in axs:
        ax.set_ylim(-5, 112)
        ax.axvline(brk, color=INK2, lw=1, ls=(0, (3, 2)))
    axs[0].text(brk + 0.6, 22, "the break", color=INK2, fontsize=8.5)
    quiet_end = next(r["t"] for r in rows if r["C"] < 99.9)
    axs[0].annotate("", xy=(quiet_end, 112), xytext=(brk, 112), annotation_clip=False,
                    arrowprops=dict(arrowstyle="<->", color=MUTED, lw=0.8))
    axs[0].text((quiet_end + brk) / 2, 118, "the protected flow is held while lower parts go short", ha="center",
                fontsize=8, color=INK2, clip_on=False)
    save(fig, "fig3_silence_and_break")
    return brk


# ---------------------------------------------------------------- Figure 4: rate decides harm (Proposition 6)
def decline_loss(K, theta, tau, phi, Delta):
    n = R = K
    lost = 0.0
    steps = int(math.ceil(Delta / phi))
    for tt in range(steps + 20 * tau + 200):
        if tt < steps:
            R = max(K - Delta, R - phi)
        u = max(0.0, n - R)
        off = min(u, theta * K)
        fl = (u - off) / tau
        n -= off + fl
        lost += fl
    return lost


def fig_harm():
    K, theta, tau, Qs = 100.0, 0.05, 4, 10.0
    phis = [0.25 * i for i in range(1, 161)]
    fig, ax = plt.subplots(figsize=(6.4, 3.7))
    for Delta, c in ((8.0, S3), (20.0, S2), (40.0, S1)):
        loss = [decline_loss(K, theta, tau, p, Delta) for p in phis]
        ax.plot(phis, loss, color=c, lw=2)
        ax.text(40.4, loss[-1], f"fall of depth {Delta:g}", fontsize=8, color=INK2, va="center")
    ax.axhline(Qs, color=MUTED, lw=1, ls=(0, (3, 2)))
    ax.text(39.5, Qs + 0.5, "template limit: losses above it scar", fontsize=8, color=INK2, ha="right")
    ax.axvline(theta * K, color=MUTED, lw=0.8)
    ax.text(theta * K + 0.5, 17, "switch-off rate:\nno loss below it,\nat any depth", fontsize=8, color=INK2, va="center")
    ax.set_xlabel("Speed of the fall in what the part's access can renew (units per step)")
    ax.set_ylabel("Units lost")
    ax.set_xlim(0, 40)
    ax.set_ylim(0, 20)
    ax.set_yticks(range(0, 21, 5))
    save(fig, "fig4_rate_decides_harm")


# ---------------------------------------------------------------- Figure 5: PT1, the order of loss in councils
def fig_pt1():
    d = json.load(open(os.path.join(ROOT, "tests", "results", "PT1", "summary.json")))
    # The G25 summary records estimates and one-sided p-values, not standard errors. The analysis used cluster-robust
    # errors with a t distribution on G-1 degrees of freedom (implementation note 10), so the interval is recovered
    # from that distribution: SE = estimate / t(1-p), interval = estimate +/- t(0.975) SE. Approximate.
    from scipy.stats import t as tdist
    df = d["G25"]["councils"] - 1
    tcrit = tdist.ppf(0.975, df)

    def se_from_p(est, p_one):
        return abs(est) / tdist.isf(p_one, df)

    rows = [("Duty attaches (A)\nminus discretionary (C)", d["G25"]["delta_A"], d["G25"]["p_A"]),
            ("Duty of uncertain level (B)\nminus discretionary (C)", d["G25"]["delta_B"], d["G25"]["p_B"])]
    fig, ax = plt.subplots(figsize=(6.4, 2.4))
    for i, (lab, est, p) in enumerate(rows):
        se = se_from_p(est, p)
        y = len(rows) - 1 - i
        ax.plot([100 * (est - tcrit * se), 100 * (est + tcrit * se)], [y, y], color=S1, lw=2, solid_capstyle="round")
        ax.plot(100 * est, y, "o", color=S1, ms=8, mec=SURF, mew=2)
        ax.text(100 * (est + tcrit * se) + 0.25, y, f"{100 * est:.1f}", va="center", fontsize=8.5, color=INK)
    ax.axvline(0, color=MUTED, lw=0.8)
    ax.set_yticks([1, 0])
    ax.set_yticklabels([r[0] for r in rows], fontsize=8.6)
    ax.set_ylim(-0.6, 1.6)
    ax.set_xlabel("Difference in real spending growth per head (percentage points a year)")
    ax.grid(axis="y", visible=False)
    save(fig, "fig5_pt1_order_of_loss")


# ---------------------------------------------------------------- LinkedIn: square version of the law
def linkedin_square():
    fig = plt.figure(figsize=(6, 6))
    fig.text(0.07, 0.94, "Nothing is saved, only moved", fontsize=19, fontweight="bold", color=INK, va="top")
    fig.text(0.07, 0.875, "Under scarcity, no ordering of access reduces the total shortfall.\n"
             "It only decides which parts go short.", fontsize=11, color=INK2, va="top", linespacing=1.35)
    ax = fig.add_axes([0.12, 0.19, 0.84, 0.58])
    plot_law(ax)
    ax.set_ylabel("Shortfall, by the part that goes short")
    fig.text(0.07, 0.065, "From cells to councils: a conservation law of allocation under scarcity.\n"
             "J. Miller, SSRN 2026. doi:10.2139/ssrn.7579199", fontsize=8.5, color=MUTED, va="bottom",
             linespacing=1.4)
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(OUT, f"linkedin_law_square.{ext}"), dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    fig_architecture()
    fig_law()
    brk = fig_silence()
    fig_harm()
    fig_pt1()
    linkedin_square()
    print("figures written to", OUT, "| break at step", brk)
