"""
Generate source-based figures for STA237 Week 8 Study Notes and Answers & Practice.
All figures are saved to W8/Study-Notes-Markdown/figures/ in English.
"""

import os
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy import stats

OUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "figures",
)
os.makedirs(OUT_DIR, exist_ok=True)

plt.rcParams.update(
    {
        "font.size": 10,
        "axes.titlesize": 11,
        "axes.labelsize": 10,
        "legend.fontsize": 8.5,
        "figure.dpi": 180,
        "savefig.bbox": "tight",
    }
)


def gas_pdf(g):
    g = np.asarray(g, dtype=float)
    out = np.zeros_like(g)
    m1 = (g > 0) & (g < 1)
    m2 = (g >= 1) & (g < 2)
    out[m1] = g[m1]
    out[m2] = 2.0 - g[m2]
    return out


def gas_cdf(g):
    g = np.asarray(g, dtype=float)
    out = np.zeros_like(g)
    m1 = (g >= 0) & (g < 1)
    m2 = (g >= 1) & (g < 2)
    m3 = g >= 2
    out[m1] = 0.5 * g[m1] ** 2
    out[m2] = -0.5 * (g[m2] ** 2 - 4.0 * g[m2] + 2.0)
    out[m3] = 1.0
    return out


def make_fig1():
    """Fig 1: Gas station pump PDF/CDF comparing central 80% vs Chebyshev >= 80% intervals."""
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.4))
    g = np.linspace(-0.15, 2.15, 1000)
    y = gas_pdf(g)

    q10 = math.sqrt(0.2)
    q90 = 2.0 - math.sqrt(0.2)
    cheb_lo = 1.0 - math.sqrt(5.0 / 6.0)
    cheb_hi = 1.0 + math.sqrt(5.0 / 6.0)

    # Panel 1: Exact central 80% vs Chebyshev interval on PDF
    ax = axes[0]
    ax.plot(g, y, color="#1f4e79", lw=2.2, label="PDF $f(g)$")
    g_mid = np.linspace(q10, q90, 400)
    ax.fill_between(
        g_mid,
        0,
        gas_pdf(g_mid),
        color="#4a90d9",
        alpha=0.38,
        label="Exact central 80%: $[0.447, 1.553]$",
    )
    g_left = np.linspace(0, q10, 200)
    g_right = np.linspace(q90, 2, 200)
    ax.fill_between(
        g_left, 0, gas_pdf(g_left), color="#d9534f", alpha=0.28, label="10% tails each side"
    )
    ax.fill_between(g_right, 0, gas_pdf(g_right), color="#d9534f", alpha=0.28)
    ax.axvline(cheb_lo, color="#2e8b57", ls="--", lw=1.6, label=r"Chebyshev $\geq 80\%$ bounds: $[0.087, 1.913]$")
    ax.axvline(cheb_hi, color="#2e8b57", ls="--", lw=1.6)
    ax.annotate("80% exact\ncentral mass", xy=(1.0, 0.42), ha="center", fontsize=9, fontweight="bold", color="#103558")
    ax.annotate("10%", xy=(0.28, 0.10), ha="center", fontsize=8.5, color="#8b1e1b")
    ax.annotate("10%", xy=(1.72, 0.10), ha="center", fontsize=8.5, color="#8b1e1b")
    ax.annotate("Chebyshev\nleft bound", xy=(cheb_lo, 0.85), xytext=(0.02, 0.92),
                arrowprops=dict(arrowstyle="->", color="#2e8b57", lw=1.1), fontsize=8, color="#1d613b")
    ax.annotate("Chebyshev\nright bound", xy=(cheb_hi, 0.85), xytext=(1.55, 0.92),
                arrowprops=dict(arrowstyle="->", color="#2e8b57", lw=1.1), fontsize=8, color="#1d613b")
    ax.set_title("PDF: Exact Central 80% vs. Chebyshev Interval")
    ax.set_xlabel("$g$ (10,000 gallons/month)")
    ax.set_ylabel("Density $f(g)$")
    ax.set_xlim(-0.1, 2.1)
    ax.set_ylim(0, 1.18)
    ax.grid(alpha=0.25)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=2, frameon=True)

    # Panel 2: Piecewise CDF F(g) showing quantiles and actual coverage
    ax = axes[1]
    F = gas_cdf(g)
    ax.plot(g, F, color="#1f4e79", lw=2.2, label="CDF $F(g)$")
    ax.plot([q10, q10], [0, 0.10], color="#4a90d9", ls=":", lw=1.4)
    ax.plot([-0.1, q10], [0.10, 0.10], color="#4a90d9", ls=":", lw=1.4)
    ax.plot([q90, q90], [0, 0.90], color="#4a90d9", ls=":", lw=1.4)
    ax.plot([-0.1, q90], [0.90, 0.90], color="#4a90d9", ls=":", lw=1.4)
    ax.scatter([q10, q90], [0.10, 0.90], color="#4a90d9", zorder=5, label="10th & 90th percentiles ($0.447, 1.553$)")

    F_lo = gas_cdf(0.09)
    F_hi = gas_cdf(1.91)
    ax.scatter([0.09, 1.91], [F_lo, F_hi], color="#2e8b57", marker="s", zorder=5,
               label=f"Rounded Chebyshev $(0.09, 1.91)$: actual prob $= {F_hi - F_lo:.4f}$")
    ax.annotate("$(0.447, 0.10)$", xy=(q10, 0.10), xytext=(0.58, 0.12), fontsize=8.5, color="#103558")
    ax.annotate("$(1.553, 0.90)$", xy=(q90, 0.90), xytext=(1.02, 0.84), fontsize=8.5, color="#103558")
    ax.annotate(f"Actual coverage:\n$F(1.91)-F(0.09)=0.9919$\n(guarantee was $\\geq 0.80$)",
                xy=(1.91, F_hi), xytext=(0.65, 0.45),
                arrowprops=dict(arrowstyle="->", color="#2e8b57", lw=1.1),
                bbox=dict(boxstyle="round,pad=0.3", fc="#eef8f1", ec="#2e8b57", alpha=0.9),
                fontsize=8.3, color="#1d613b")
    ax.set_title("Piecewise CDF: Percentiles vs. Actual Coverage")
    ax.set_xlabel("$g$ (10,000 gallons/month)")
    ax.set_ylabel("Cumulative probability $F(g)$")
    ax.set_xlim(-0.1, 2.1)
    ax.set_ylim(-0.02, 1.06)
    ax.grid(alpha=0.25)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=1, frameon=True)

    fig.suptitle("Example 1 (PDF pp. 6–10): Gas Pump Exact 80% Interval vs. Chebyshev Guarantee", fontweight="bold", y=1.02)
    plt.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "fig1_gas_pump_intervals.png"))
    plt.close(fig)


def make_fig2():
    """Fig 2: 30 cm ruler Uniform(0,30) and surface area A = 6X^2 mapping."""
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.3))

    x_lo = math.sqrt(1000.0 / 6.0)
    x_hi = math.sqrt(2600.0 / 6.0)

    # Panel 1: Uniform PDF on [0, 30]
    ax = axes[0]
    x = np.linspace(-2, 32, 600)
    f = np.where((x >= 0) & (x <= 30), 1.0 / 30.0, 0.0)
    ax.plot(x, f, color="#1f4e79", lw=2.2, label=r"$X \sim \mathrm{Unif}(0, 30)$ PDF: $f(x)=\frac{1}{30}$")
    xm = np.linspace(x_lo, x_hi, 300)
    ax.fill_between(
        xm,
        0,
        1.0 / 30.0,
        color="#f0ad4e",
        alpha=0.45,
        label=f"Mapped event $[{x_lo:.2f}, {x_hi:.2f}]$ cm\nExact prob $= {(x_hi - x_lo)/30:.4f}$",
    )
    ax.axvline(15, color="#1f4e79", ls="--", lw=1.3, label="$E(X)=15$ cm")
    ax.set_title(r"Side Length $X \sim \mathrm{Unif}(0, 30)$ cm")
    ax.set_xlabel("Side length $x$ (cm)")
    ax.set_ylabel(r"Density $f_X(x)$ ($\mathrm{cm}^{-1}$)")
    ax.set_xlim(-2, 32)
    ax.set_ylim(0, 0.052)
    ax.set_yticks([0, 1 / 60, 1 / 30])
    ax.set_yticklabels(["0", "1/60", "1/30"])
    ax.grid(alpha=0.25)
    ax.legend(loc="upper right", frameon=True)

    # Panel 2: Nonlinear transformation A = 6X^2
    ax = axes[1]
    xs = np.linspace(0, 30, 400)
    As = 6.0 * xs ** 2
    ax.plot(xs, As, color="#1f4e79", lw=2.2, label=r"$A = 6X^2$ ($\mathrm{cm}^2$)")
    ax.axhspan(1000, 2600, color="#f0ad4e", alpha=0.22, label=r"Target $1000 \leq A \leq 2600\ \mathrm{cm}^2$")
    ax.axvspan(x_lo, x_hi, color="#4a90d9", alpha=0.18, label=r"Preimage $\sqrt{1000/6} \leq X \leq \sqrt{2600/6}$")
    ax.plot([x_lo, x_lo, 0], [0, 1000, 1000], color="#8a5a00", ls=":", lw=1.3)
    ax.plot([x_hi, x_hi, 0], [0, 2600, 2600], color="#8a5a00", ls=":", lw=1.3)
    ax.scatter([x_lo, x_hi], [1000, 2600], color="#d9534f", zorder=5)
    ax.annotate(f"({x_lo:.2f}, 1000)", xy=(x_lo, 1000), xytext=(3.0, 1300),
                arrowprops=dict(arrowstyle="->", color="#d9534f", lw=1.0), fontsize=8.5)
    ax.annotate(f"({x_hi:.2f}, 2600)", xy=(x_hi, 2600), xytext=(12.0, 3250),
                arrowprops=dict(arrowstyle="->", color="#d9534f", lw=1.0), fontsize=8.5)
    ax.set_title("Mapping Surface Area Back to Side Length")
    ax.set_xlabel("Side length $x$ (cm)")
    ax.set_ylabel(r"Cube surface area $A$ ($\mathrm{cm}^2$)")
    ax.set_xlim(0, 31)
    ax.set_ylim(0, 5600)
    ax.grid(alpha=0.25)
    ax.legend(loc="upper left", frameon=True)

    fig.suptitle("30 cm Ruler Problem (PDF pp. 12–13): Exact Probability Without a Transformed PDF", fontweight="bold", y=1.02)
    plt.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "fig2_ruler_uniform_mapping.png"))
    plt.close(fig)


def make_fig3():
    """Fig 3: Poisson count vs Exponential waiting time duality & memorylessness."""
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.1))

    # Panel 1: Timeline duality {T > t} <=> {N(t) = 0}
    ax = axes[0]
    ax.set_xlim(-0.3, 4.3)
    ax.set_ylim(-0.2, 2.3)
    ax.axis("off")
    ax.set_title("Poisson Count $N(t)$ vs. Exponential Wait $T$", fontweight="bold")

    # Timeline 1: Wait > t (No arrivals in [0, t])
    y1 = 1.55
    ax.plot([0.2, 3.8], [y1, y1], color="#1f4e79", lw=2.2)
    ax.plot([0.2, 0.2], [y1 - 0.1, y1 + 0.1], color="#1f4e79", lw=2.0)
    ax.plot([2.5, 2.5], [y1 - 0.1, y1 + 0.1], color="#1f4e79", lw=2.0)
    ax.scatter([3.3], [y1], color="#d9534f", s=65, zorder=5)
    ax.text(0.2, y1 - 0.25, "$0$", ha="center", fontsize=9.5)
    ax.text(2.5, y1 - 0.25, "$t$", ha="center", fontsize=9.5)
    ax.text(3.3, y1 + 0.18, "1st arrival ($T > t$)", ha="center", fontsize=8.8, color="#8b1e1b")
    ax.text(1.35, y1 + 0.18, "0 arrivals in $(0, t]$: $N(t)=0$", ha="center", fontsize=8.8, color="#1f4e79")
    ax.text(2.0, y1 + 0.45, r"Event Equivalence 1: $\{T > t\} \Leftrightarrow \{N(t) = 0\} \Rightarrow P(T > t) = e^{-\lambda t}$",
            ha="center", fontsize=9.0, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.25", fc="#eef4f9", ec="#1f4e79"))

    # Timeline 2: Wait <= t (At least 1 arrival in [0, t])
    y2 = 0.45
    ax.plot([0.2, 3.8], [y2, y2], color="#2e8b57", lw=2.2)
    ax.plot([0.2, 0.2], [y2 - 0.1, y2 + 0.1], color="#2e8b57", lw=2.0)
    ax.plot([2.5, 2.5], [y2 - 0.1, y2 + 0.1], color="#2e8b57", lw=2.0)
    ax.scatter([1.0, 1.9, 3.1], [y2, y2, y2], color="#2e8b57", s=55, zorder=5)
    ax.text(0.2, y2 - 0.25, "$0$", ha="center", fontsize=9.5)
    ax.text(2.5, y2 - 0.25, "$t$", ha="center", fontsize=9.5)
    ax.text(1.0, y2 + 0.18, r"1st arrival ($T \leq t$)", ha="center", fontsize=8.8, color="#1d613b")
    ax.text(2.0, y2 + 0.45, r"Event Equivalence 2: $\{T \leq t\} \Leftrightarrow \{N(t) \geq 1\} \Rightarrow F_T(t) = 1 - e^{-\lambda t}$",
            ha="center", fontsize=9.0, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.25", fc="#eef8f1", ec="#2e8b57"))

    # Panel 2: Memoryless conditional survival curve
    ax = axes[1]
    t = np.linspace(0, 12, 500)
    lam = 5.0 / 24.0
    f_t = lam * np.exp(-lam * t)
    ax.plot(t, f_t, color="#1f4e79", lw=2.2, label=r"$T \sim \mathrm{Exp}(\lambda = 5/24\ \mathrm{hr}^{-1})$")
    j, k = 3.0, 5.0
    t_cond = np.linspace(j, 12, 300)
    t_more = np.linspace(j + k, 12, 200)
    ax.fill_between(t_cond, 0, lam * np.exp(-lam * t_cond), color="#b0c4de", alpha=0.45,
                    label=r"Given elapsed $T \geq 3$ hr: $P(T \geq 3)$")
    ax.fill_between(t_more, 0, lam * np.exp(-lam * t_more), color="#d9534f", alpha=0.45,
                    label=r"Additional wait $\geq 5$ hr: $P(T \geq 8)$")
    ax.axvline(j, color="#1f4e79", ls="--", lw=1.3)
    ax.axvline(j + k, color="#8b1e1b", ls="--", lw=1.3)
    ax.annotate("$j=3$ hr\nelapsed", xy=(j, 0.14), xytext=(1.2, 0.16),
                arrowprops=dict(arrowstyle="->", color="#1f4e79"), fontsize=8.5)
    ax.annotate("$j+k=8$ hr\ntotal clock", xy=(j + k, 0.08), xytext=(7.2, 0.105),
                arrowprops=dict(arrowstyle="->", color="#8b1e1b"), fontsize=8.5)
    ax.text(3.75, 0.155, r"$P(T > j+k \mid T \geq j) = \frac{e^{-\lambda(j+k)}}{e^{-\lambda j}} = e^{-\lambda k} = P(T > k)$",
            fontsize=8.3, bbox=dict(boxstyle="round,pad=0.25", fc="#fff8e7", ec="#c58b00"))
    ax.set_title("Memoryless Property (Example 2b, PDF pp. 19–20)")
    ax.set_xlabel("Waiting time $t$ (hours)")
    ax.set_ylabel(r"Density $f_T(t)$ ($\mathrm{hr}^{-1}$)")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 0.22)
    ax.grid(alpha=0.25)
    ax.legend(loc="upper right", fontsize=8)

    plt.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "fig3_poisson_exponential_duality.png"))
    plt.close(fig)


def make_fig4():
    """Fig 4: Sum of 4 i.i.d. Exp(rate=5) simulation vs Exp & Gamma curves, plus Gamma shape comparison."""
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.3))

    # Panel 1: Simulation of 1000 sums of 4 Exp(rate=5)
    ax = axes[0]
    rng = np.random.default_rng(113)
    sums = rng.exponential(scale=0.2, size=(1000, 4)).sum(axis=1)
    ax.hist(sums, bins=30, density=True, fill=False, edgecolor="#444444", lw=1.1,
            label=r"1,000 simulated sums $\sum_{i=1}^4 T_i$")

    t_grid = np.linspace(0.01, 2.8, 400)
    ax.plot(t_grid, stats.expon.pdf(t_grid, scale=0.2), color="#d9534f", lw=2.0,
            label=r"Single gap $\mathrm{Exp}(\mathrm{rate}=5)$ (does NOT fit)")
    ax.plot(t_grid, stats.gamma.pdf(t_grid, a=4, scale=0.2), color="#1f4e79", lw=2.2, ls="--",
            label=r"Theoretical $\mathrm{Gamma}(\alpha=4, \theta=0.2)$")
    ax.set_title("Simulated Total Time of 4 Interarrival Gaps (1st to 5th Arrival)")
    ax.set_xlabel("Total elapsed time (days)")
    ax.set_ylabel("Density")
    ax.set_xlim(0, 2.8)
    ax.set_ylim(0, 2.6)
    ax.grid(alpha=0.25)
    ax.legend(loc="upper right", frameon=True)

    # Panel 2: Gamma density shape examples (MMSA scale convention beta=1/rate)
    ax = axes[1]
    x = np.linspace(0.05, 30, 500)
    specs = [
        (0.5, 1.0, "#7b3294", "-", r"$\alpha=0.5, \beta=1$ ($\alpha<1$: unbounded at $0$)"),
        (1.0, 2.0, "#d9534f", "--", r"$\alpha=1, \beta=2$ ($\mathrm{Exp}(\theta=2)$)"),
        (3.0, 2.0, "#1f4e79", "-", r"$\alpha=3, \beta=2$ ($\alpha>1$: unimodal, right-skewed)"),
        (5.0, 3.0, "#2e8b57", "-.", r"$\alpha=5, \beta=3$ (broader right-skewed peak)"),
    ]
    for a, b, col, ls, lbl in specs:
        ax.plot(x, stats.gamma.pdf(x, a=a, scale=b), color=col, ls=ls, lw=2.0, label=lbl)
    ax.set_title(r"Gamma Density Shapes $f(x; \alpha, \beta)$ (MMSA Scale Convention)")
    ax.set_xlabel("$x$")
    ax.set_ylabel("Density $f(x)$")
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 0.22)
    ax.grid(alpha=0.25)
    ax.legend(loc="upper right", frameon=True)

    fig.suptitle("Sums of Independent Common-Rate Exponentials and the Gamma Family (PDF pp. 24–27)", fontweight="bold", y=1.02)
    plt.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "fig4_sum_exponentials_gamma_sim.png"))
    plt.close(fig)


def make_fig5():
    """Fig 5: Reconstructed 5-component series system diagram for MMSA #79."""
    fig, ax = plt.subplots(figsize=(8.5, 1.8))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 2)
    ax.axis("off")

    ax.plot([0.5, 10.5], [1.0, 1.0], color="#1f4e79", lw=2.2, zorder=1)
    xs = [1.5, 3.5, 5.5, 7.5, 9.5]
    for idx, xc in enumerate(xs, start=1):
        rect = patches.FancyBboxPatch(
            (xc - 0.5, 0.65),
            1.0,
            0.7,
            boxstyle="round,pad=0.05",
            facecolor="#dce8f5",
            edgecolor="#1f4e79",
            linewidth=1.8,
            zorder=2,
        )
        ax.add_patch(rect)
        ax.text(xc, 1.0, f"{idx}", ha="center", va="center", fontsize=12, fontweight="bold", color="#103558", zorder=3)

    ax.text(5.5, 1.72, "MMSA #79 (Reconstructed Schematic): Five Identical Components in Series", ha="center", fontsize=10.5, fontweight="bold")
    ax.text(5.5, 0.18, r"Independent lifetimes $T_1,\dots,T_5 \sim \mathrm{Exp}(\lambda=0.01\ \mathrm{hr}^{-1})$; system fails at $X = \min(T_1,\dots,T_5)$", ha="center", fontsize=9.2, color="#333333")
    fig.savefig(os.path.join(OUT_DIR, "fig5_series_system_mmsa79.png"))
    plt.close(fig)


if __name__ == "__main__":
    make_fig1()
    make_fig2()
    make_fig3()
    make_fig4()
    make_fig5()
    print("Generated 5 figures in:", OUT_DIR)
