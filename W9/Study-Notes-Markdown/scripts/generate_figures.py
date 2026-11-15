#!/usr/bin/env python3
"""Generate publication-quality PNG figures for STA237 Week 9 Study Notes."""

import math
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")


def norm_pdf(x, mu=0.0, sd=1.0):
    z = (x - mu) / sd
    return np.exp(-0.5 * z * z) / (sd * math.sqrt(2.0 * math.pi))


def gamma_pdf(x, alpha, beta):
    x = np.asarray(x, dtype=float)
    coef = 1.0 / (math.gamma(alpha) * (beta ** alpha))
    out = np.zeros_like(x)
    pos = x > 0
    out[pos] = coef * (x[pos] ** (alpha - 1.0)) * np.exp(-x[pos] / beta)
    return out


def make_fig1():
    plt.rcParams.update({
        "font.size": 10,
        "axes.titlesize": 10.8,
        "axes.labelsize": 10,
        "legend.fontsize": 8.5,
        "axes.edgecolor": "#444444",
    })
    fig, axes = plt.subplots(1, 2, figsize=(12.4, 4.8), dpi=220)

    # Panel A: Gamma family shape comparison (scale parameterization beta = 2)
    ax = axes[0]
    x = np.linspace(0.05, 25.0, 800)
    curves = [
        (0.5, 2.0, "#8e44ad", "--", r"$\Gamma(\alpha=0.5, \beta=2)$ (non-integer $\alpha < 1$, asymptote at $0^+$)"),
        (1.0, 2.0, "#d35400", "-", r"$\Gamma(\alpha=1, \beta=2) = \mathrm{Exp}(\theta=2)$ (single wait)"),
        (3.0, 2.0, "#1f77b4", "-", r"$\Gamma(\alpha=3, \beta=2)$ (sum of 3 i.i.d. Exp waits)"),
        (5.0, 2.0, "#117a65", "-.", r"$\Gamma(\alpha=5, \beta=2)$ (sum of 5 waits, less right-skew)"),
    ]
    for a, b, col, ls, lbl in curves:
        y = gamma_pdf(x, a, b)
        ax.plot(x, y, color=col, linestyle=ls, linewidth=2.1, label=lbl)
    ax.set_xlim(0, 25)
    ax.set_ylim(0, 0.52)
    ax.set_xlabel("x")
    ax.set_ylabel("Density f(x)")
    ax.set_title("(a) Gamma PDF Shapes (Scale Parameterization beta = 2)")
    ax.grid(True, linestyle=":", alpha=0.45)
    ax.legend(loc="upper right", frameon=True, facecolor="white", framealpha=0.94)
    ax.annotate("Mode = (alpha - 1)*beta = 4", xy=(4.0, gamma_pdf(4.0, 3.0, 2.0)),
                xytext=(6.8, 0.22),
                arrowprops=dict(arrowstyle="->", color="#1f77b4", lw=1.2),
                fontsize=8.6, color="#1f77b4", fontweight="bold")

    # Panel B: Example 2 TikTok video length T ~ Gamma(2, 3) Chebyshev vs Exact
    ax = axes[1]
    t_pos = np.linspace(0.001, 22.0, 700)
    y_pos = gamma_pdf(t_pos, 2.0, 3.0)
    ax.plot(t_pos, y_pos, color="#1b4f72", linewidth=2.2,
            label=r"$T \sim \Gamma(\alpha=2, \beta=3)$ ($\mu=6, \sigma=\sqrt{18}\approx 4.24$)")

    u_bound = 6.0 + math.sqrt(5.0 * 18.0)  # 15.4868...
    l_bound = 6.0 - math.sqrt(5.0 * 18.0)  # -3.4868...
    ax.fill_between(t_pos, 0, y_pos, where=(t_pos >= 0.0) & (t_pos <= 15.49),
                    color="#85c1e9", alpha=0.55,
                    label="Support capture [0, 15.49): Exact prob = 0.9647")
    ax.fill_between(t_pos, 0, y_pos, where=(t_pos >= 15.49),
                    color="#e74c3c", alpha=0.38,
                    label="Upper tail [15.49, Inf): prob = 0.0353")

    ax.axvline(0.0, color="#2c3e50", linestyle="-", linewidth=1.3)
    ax.axvline(6.0, color="#1b4f72", linestyle=":", linewidth=1.3)
    ax.axvline(l_bound, color="#7f8c8d", linestyle="--", linewidth=1.4)
    ax.axvline(15.49, color="#c0392b", linestyle="--", linewidth=1.4)

    ax.axvspan(l_bound, 0.0, color="#d5dbdb", alpha=0.45)
    ax.text((l_bound + 0.0) / 2.0, 0.068, "Raw lower\n-3.49\n(outside\nsupport)",
            ha="center", va="center", fontsize=8.0, color="#424949",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#bdc3c7", alpha=0.9))
    ax.text(6.2, 0.006, "mean = 6", fontsize=8.4, color="#1b4f72")
    ax.text(15.7, 0.042, "15.49 min", fontsize=8.5, color="#922b21", fontweight="bold")
    ax.annotate("Chebyshev bound >= 0.80\nActual Gamma area = 0.9647",
                xy=(5.2, 0.062), xytext=(8.6, 0.095),
                arrowprops=dict(arrowstyle="->", color="#1b4f72", lw=1.2),
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#1f77b4", alpha=0.94),
                fontsize=8.5, color="#1b4f72")

    ax.set_xlim(-4.6, 22.0)
    ax.set_ylim(0, 0.145)
    ax.set_xlabel("Video length t (minutes)")
    ax.set_ylabel("Density f(t)")
    ax.set_title("(b) Example 2: Chebyshev Bound (>= 80%) vs. Exact Area")
    ax.grid(True, linestyle=":", alpha=0.45)
    ax.legend(loc="upper right", frameon=True, facecolor="white", framealpha=0.94, fontsize=8.0)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "fig1_gamma_shapes_and_chebyshev.png"))
    plt.close(fig)


def make_fig2():
    plt.rcParams.update({
        "font.size": 10,
        "axes.titlesize": 10.8,
        "axes.labelsize": 10,
        "axes.edgecolor": "#444444",
    })
    fig = plt.figure(figsize=(12.8, 5.4), dpi=220)
    gs = fig.add_gridspec(2, 4, width_ratios=[1.12, 1.12, 1.0, 1.0], hspace=0.46, wspace=0.30)

    # Left large panel (spans both rows, cols 0..1): Water Dispenser Example 3
    ax = fig.add_subplot(gs[:, :2])
    mu, sd = 64.0, 0.78
    x = np.linspace(mu - 3.6 * sd, mu + 3.6 * sd, 700)
    y = norm_pdf(x, mu, sd)
    ax.plot(x, y, color="#1b4f72", linewidth=2.2)

    ax.fill_between(x, 0, y, where=(x >= mu - sd) & (x <= mu + sd),
                    color="#aed6f1", alpha=0.72,
                    label="Within 1 SD [63.22, 64.78]: p = 0.6827")

    c_val = 66.00915
    ax.fill_between(x, 0, y, where=(x >= c_val),
                    color="#e74c3c", alpha=0.68,
                    label="Overflow tail D > 66.01: P(D > c) = 0.005")

    ax.axvline(mu, color="#1b4f72", linestyle=":", linewidth=1.3)
    ax.axvline(c_val, color="#c0392b", linestyle="--", linewidth=1.4)
    ax.annotate("c = qnorm(0.995, mean=64, sd=0.78)\n  = 66.01 oz (z = +2.576)",
                xy=(c_val, 0.015), xytext=(64.95, 0.30),
                arrowprops=dict(arrowstyle="->", color="#c0392b", lw=1.3),
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#c0392b", alpha=0.95),
                fontsize=8.3, color="#922b21")
    ax.text(mu, 0.16, "Center = 64 oz\n(Z = 0)", ha="center", fontsize=8.8,
            color="#1b4f72", fontweight="bold")

    ax.set_xlim(mu - 3.5 * sd, mu + 3.5 * sd)
    ax.set_ylim(0, 0.60)
    ax.set_xlabel("Dispensed water D (oz)  [top ticks: Z = (D - 64) / 0.78]")
    ax.set_ylabel("Density f(x)")
    ax.set_title("(a) Example 3: Standardization & Overflow Quantile")
    ax.grid(True, linestyle=":", alpha=0.4)
    ax.legend(loc="upper left", fontsize=8.3, frameon=True, facecolor="white", framealpha=0.95)

    ax_top = ax.twiny()
    ax_top.set_xlim(-3.5, 3.5)
    ax_top.set_xticks([-3, -2, -1, 0, 1, 2, 3])
    ax_top.set_xlabel("Standard normal scale z = (x - mu) / sigma", fontsize=9.2, color="#4a235a")
    ax_top.tick_params(axis="x", colors="#4a235a", labelsize=8.8)

    # Right 4 small panels: 4 Standard Normal geometric patterns
    z = np.linspace(-3.4, 3.4, 500)
    phi = norm_pdf(z, 0.0, 1.0)

    specs = [
        (0, 2, "(b1) Lower-Tail CDF\nP(Z <= b) = Phi(b)", [(lambda zz: zz <= 1.1)],
         [1.1], ["b"], "pnorm(b, mean, sd)", "#3498db"),
        (0, 3, "(b2) Upper-Tail & z_alpha\nP(Z >= z_alpha) = alpha", [(lambda zz: zz >= 1.4)],
         [1.4], ["z_alpha"], "lower.tail = FALSE", "#e67e22"),
        (1, 2, "(b3) Central Interval\nP(-c <= Z <= c) = p", [(lambda zz: np.abs(zz) <= 1.25)],
         [-1.25, 1.25], ["-c", "c"], "Phi(c) = (1 + p)/2", "#2ecc71"),
        (1, 3, "(b4) Two-Tailed Event\nP(|Z| >= c) = alpha",
         [(lambda zz: zz <= -1.75), (lambda zz: zz >= 1.75)],
         [-1.75, 1.75], ["-c", "c"], "Each tail = alpha / 2", "#9b59b6"),
    ]
    for r, c_col, title, mask_fns, vlines, vlabels, note, col in specs:
        sax = fig.add_subplot(gs[r, c_col])
        sax.plot(z, phi, color="#2c3e50", linewidth=1.6)
        for mfn in mask_fns:
            sax.fill_between(z, 0, phi, where=mfn(z), color=col, alpha=0.50)
        for vx, vlbl in zip(vlines, vlabels):
            sax.axvline(vx, color="#2c3e50", linestyle="--", linewidth=1.0)
            sax.text(vx, 0.02, vlbl, ha="center", va="bottom", fontsize=7.8,
                     bbox=dict(boxstyle="square,pad=0.1", fc="white", ec="none", alpha=0.9))
        sax.text(0.5, 0.94, note, transform=sax.transAxes, ha="center", va="top",
                 fontsize=7.8, color="#1b2631",
                 bbox=dict(boxstyle="round,pad=0.22", fc="white", ec=col, alpha=0.95))
        sax.set_xlim(-3.4, 3.4)
        sax.set_ylim(0, 0.54)
        sax.set_yticks([])
        sax.set_xticks([-2, 0, 2])
        sax.set_title(title, fontsize=9.2)
        sax.grid(True, linestyle=":", alpha=0.35)

    fig.subplots_adjust(left=0.06, right=0.98, top=0.87, bottom=0.11)
    fig.savefig(os.path.join(OUT_DIR, "fig2_normal_standardization_and_tails.png"))
    plt.close(fig)


def make_fig3():
    plt.rcParams.update({
        "font.size": 9.8,
        "axes.titlesize": 10.5,
        "axes.labelsize": 9.8,
        "axes.edgecolor": "#444444",
    })
    fig, axes = plt.subplots(1, 3, figsize=(13.6, 4.5), dpi=220)

    # Panel A: Ruler Example 5 (A = 6X^2 for X ~ Unif(0, 30))
    ax = axes[0]
    x = np.linspace(0, 30, 400)
    a_curve = 6.0 * (x ** 2)
    ax.plot(x, a_curve, color="#1b4f72", linewidth=2.2)

    x1 = math.sqrt(1000.0 / 6.0)
    x2 = math.sqrt(2600.0 / 6.0)
    xm = np.linspace(x1, x2, 150)
    ax.fill_between(xm, 0, 6.0 * xm ** 2, color="#85c1e9", alpha=0.55)
    ax.axhspan(1000, 2600, color="#d6eaf8", alpha=0.32)
    ax.axvspan(x1, x2, color="#aed6f1", alpha=0.32)
    ax.plot([0, x1, x1], [1000, 1000, 0], color="#2874a6", linestyle="--", lw=1.2)
    ax.plot([0, x2, x2], [2600, 2600, 0], color="#2874a6", linestyle="--", lw=1.2)

    # Handwritten threshold A = 2400 -> X = 20
    ax.plot([0, 20, 20], [2400, 2400, 0], color="#c0392b", linestyle=":", lw=1.4)
    ax.scatter([x1, x2, 20], [1000, 2600, 2400], color=["#2874a6", "#2874a6", "#c0392b"], zorder=5, s=28)
    ax.text(1.0, 3950, "Typed interval: (1000, 2600)\n  -> X in (12.91, 20.82), P = 0.2636",
            fontsize=8.1, color="#1b4f72", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="#2874a6", alpha=0.92))
    ax.text(1.0, 2950, "Handwritten note: A <= 2400\n  -> X <= 20, P = 2/3",
            fontsize=8.0, color="#922b21",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="#c0392b", alpha=0.92))
    ax.text(16.9, 180, f"[{x1:.2f}, {x2:.2f}]", ha="center", fontsize=8.0, color="#1b4f72",
            bbox=dict(boxstyle="square,pad=0.15", fc="white", ec="none", alpha=0.9))
    ax.set_xlim(0, 30.5)
    ax.set_ylim(0, 5600)
    ax.set_xlabel("Side length X (cm) ~ Unif(0, 30)")
    ax.set_ylabel("Surface area A = 6X^2 (cm^2)")
    ax.set_title("(a) Example 5: Mapping Area Back to X")
    ax.grid(True, linestyle=":", alpha=0.4)

    # Panel B: Decreasing g(X) = -ln(X) reverses inequality (MMSA #116)
    ax = axes[1]
    xu = np.linspace(0.02, 1.0, 400)
    yu = -np.log(xu)
    ax.plot(xu, yu, color="#8e44ad", linewidth=2.2, label=r"$Y = -\ln(X)$ (strictly decreasing)")
    y0 = 0.8
    x0 = math.exp(-y0)
    ax.fill_between(xu, 0, yu, where=(xu >= x0), color="#d7bde2", alpha=0.55,
                    label=r"$\{Y \leq y\} \Longleftrightarrow \{X \geq e^{-y}\}$")
    ax.plot([0, x0, x0], [y0, y0, 0], color="#6c3483", linestyle="--", lw=1.3)
    ax.scatter([x0], [y0], color="#6c3483", s=34, zorder=5)
    ax.text(0.04, y0 + 0.12, f"y = {y0:.1f}", fontsize=8.4, color="#6c3483", fontweight="bold")
    ax.annotate("", xy=(0.98, 0.25), xytext=(x0, 0.25),
                arrowprops=dict(arrowstyle="<->", color="#6c3483", lw=1.6))
    ax.text((x0 + 1.0) / 2.0, 0.36, "X >= e^(-y)\n(reversed!)", ha="center",
            fontsize=8.2, color="#6c3483", fontweight="bold")
    ax.set_xlim(0, 1.02)
    ax.set_ylim(0, 3.9)
    ax.set_xlabel("X ~ Unif(0, 1)")
    ax.set_ylabel("Y = -ln(X) > 0")
    ax.set_title("(b) MMSA #116: Decreasing Map Reverses Inequality")
    ax.grid(True, linestyle=":", alpha=0.4)
    ax.legend(loc="upper right", fontsize=8.0, frameon=True, facecolor="white", framealpha=0.94)

    # Panel C: Two-sided non-monotonic transformation Y = |X| (MMSA #121)
    ax = axes[2]
    z = np.linspace(-3.4, 3.4, 500)
    phi = norm_pdf(z, 0.0, 1.0)
    ax.plot(z, phi, color="#117a65", linewidth=2.1, label="X ~ N(0, 1) density")
    y_cut = 1.3
    ax.fill_between(z, 0, phi, where=(np.abs(z) <= y_cut), color="#a3e4d7", alpha=0.72,
                    label=r"$\{|X| \leq y\} \Longleftrightarrow \{-y \leq X \leq y\}$")
    ax.axvline(-y_cut, color="#0e6251", linestyle="--", lw=1.3)
    ax.axvline(y_cut, color="#0e6251", linestyle="--", lw=1.3)
    ax.text(-y_cut - 0.12, 0.03, "-y", ha="right", fontsize=8.8, color="#0e6251", fontweight="bold")
    ax.text(y_cut + 0.12, 0.03, "+y", ha="left", fontsize=8.8, color="#0e6251", fontweight="bold")
    ax.text(0.0, 0.13, "F_Y(y) = Phi(y) - Phi(-y)\n      = 2 Phi(y) - 1\n(for y >= 0)",
            ha="center", fontsize=8.3, color="#0b5345",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#117a65", alpha=0.94))
    ax.set_xlim(-3.4, 3.4)
    ax.set_ylim(0, 0.51)
    ax.set_xlabel("X ~ N(0, 1)")
    ax.set_ylabel("Density phi(x)")
    ax.set_title("(c) MMSA #121: Two-Sided Event for Y = |X|")
    ax.grid(True, linestyle=":", alpha=0.4)
    ax.legend(loc="upper right", fontsize=8.0, frameon=True, facecolor="white", framealpha=0.94)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "fig3_transformation_cdf_method.png"))
    plt.close(fig)


def make_fig4():
    plt.rcParams.update({
        "font.size": 10,
        "axes.titlesize": 11.2,
        "axes.labelsize": 10.2,
        "axes.edgecolor": "#444444",
        "axes.linewidth": 0.8,
        "figure.dpi": 200,
    })

    fig, ax = plt.subplots(figsize=(7.6, 4.0))

    # Flat density branches outside and inside [0, 30]
    ax.plot([-6, 0], [0, 0], color="#1f618d", linewidth=2.2)
    ax.plot([30, 36], [0, 0], color="#1f618d", linewidth=2.2)
    ax.plot([0, 30], [1 / 30.0, 1 / 30.0], color="#1f618d", linewidth=2.5,
            label=r"$f_X(x) = \frac{1}{30}$ for $0 \leq x \leq 30$ ($0$ otherwise)")
    ax.fill_between([0, 30], [0, 0], [1 / 30.0, 1 / 30.0], color="#aed6f1", alpha=0.62)

    # Vertical guides at support boundaries
    ax.plot([0, 0], [0, 1 / 30.0], color="#1f618d", linestyle="--", linewidth=1.3)
    ax.plot([30, 30], [0, 1 / 30.0], color="#1f618d", linestyle="--", linewidth=1.3)

    # Endpoint markers (closed on rectangle top, open on x-axis boundaries)
    ax.scatter([0, 30], [1 / 30.0, 1 / 30.0], color="#1f618d", s=38, zorder=5)
    ax.scatter([0, 30], [0, 0], facecolors="white", edgecolors="#1f618d", s=38, linewidth=1.4, zorder=5)

    # Mean line at E(X) = 15 cm
    ax.axvline(15.0, color="#c0392b", linestyle=":", linewidth=1.8, label=r"Mean $E(X) = 15$ cm (symmetry center)")

    # Annotations for height, base width, and area = 1
    ax.text(15.0, 0.0175, "Rectangle Area = Base x Height = 30 x (1/30) = 1",
            ha="center", va="center", fontsize=9.2, color="#154360", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#1f618d", alpha=0.92))
    ax.annotate("", xy=(30, 0.0045), xytext=(0, 0.0045),
                arrowprops=dict(arrowstyle="<->", color="#1f618d", lw=1.4))
    ax.text(15.0, 0.0068, "Base width = 30 cm", ha="center", fontsize=8.6, color="#154360",
            bbox=dict(boxstyle="square,pad=0.12", fc="#aed6f1", ec="none", alpha=0.85))
    ax.annotate("Height = 1/30\n(~0.0333 per cm)", xy=(2.2, 1 / 30.0), xytext=(3.6, 0.042),
                arrowprops=dict(arrowstyle="->", color="#1f618d", lw=1.2),
                fontsize=8.6, color="#154360", fontweight="bold")

    ax.set_xlim(-5.5, 35.5)
    ax.set_ylim(-0.003, 0.052)
    ax.set_yticks([0.0, 1 / 60.0, 1 / 30.0])
    ax.set_yticklabels(["0", "1/60", "1/30\n(~0.0333)"])
    ax.set_xticks([0, 5, 10, 15, 20, 25, 30])
    ax.set_xlabel("Ruler measurement x (cm)")
    ax.set_ylabel("Density f_X(x)")
    ax.set_title("SQ-07(a): Uniform(0, 30) Density Sketch for a 30 cm Ruler Measurement")
    ax.grid(True, linestyle=":", alpha=0.45)
    ax.legend(loc="upper right", fontsize=8.5, frameon=True, facecolor="white", framealpha=0.95)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "fig4_ruler_uniform_density.png"))
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    make_fig1()
    make_fig2()
    make_fig3()
    make_fig4()
    print("Regenerated 4 figures in:", OUT_DIR)
