import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs('W2/Study-Notes-Markdown/graphs', exist_ok=True)
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

# -------------------------------------------------------------
# Graph 1: Counting Decision Tree / Roadmap
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
ax.axis('off')

# Title
ax.text(5, 9.5, "Combinatorial Counting Decision Architecture", fontsize=16, fontweight='bold', ha='center', color='#1a365d')

# Root
bbox_root = dict(boxstyle="round,pad=0.5", fc="#e2e8f0", ec="#4a5568", lw=2)
ax.text(5, 8.2, "Counting Problem:\nSelecting $k$ items from $n$ objects", ha='center', va='center', bbox=bbox_root, fontsize=11, fontweight='bold')

# Branch 1: Does order matter?
ax.text(2.6, 7.8, "Order Matters\n(Sequences / Arrangements)", ha='center', va='center', fontsize=9, color="#2b6cb0", fontweight='bold')
ax.text(7.4, 7.8, "Order Does NOT Matter\n(Subsets / Groups)", ha='center', va='center', fontsize=9, color="#c53030", fontweight='bold')

ax.annotate("", xy=(2.5, 6.7), xytext=(3.4, 7.4), arrowprops=dict(arrowstyle="->", lw=2, color="#2b6cb0"))
ax.annotate("", xy=(7.5, 6.7), xytext=(6.6, 7.4), arrowprops=dict(arrowstyle="->", lw=2, color="#c53030"))

# Second Level: Repetition?
bbox_stage = dict(boxstyle="square,pad=0.4", fc="#ebf8ff", ec="#3182ce", lw=1.5)
ax.text(2.5, 6.2, "Is Repetition Allowed?", ha='center', va='center', bbox=bbox_stage, fontsize=10, fontweight='bold')

bbox_stage2 = dict(boxstyle="square,pad=0.4", fc="#fff5f5", ec="#e53e3e", lw=1.5)
ax.text(7.5, 6.2, "Is Repetition Allowed?", ha='center', va='center', bbox=bbox_stage2, fontsize=10, fontweight='bold')

# Sub-branches
# Order matters: With vs Without
ax.annotate("", xy=(1.3, 4.8), xytext=(2.1, 5.9), arrowprops=dict(arrowstyle="->", lw=1.5, color="#4a5568"))
ax.annotate("", xy=(3.7, 4.8), xytext=(2.9, 5.9), arrowprops=dict(arrowstyle="->", lw=1.5, color="#4a5568"))
ax.text(1.4, 5.5, "WITH replacement", ha='center', fontsize=8, style='italic')
ax.text(3.6, 5.5, "WITHOUT replacement", ha='center', fontsize=8, style='italic')

# Order doesn't matter: With vs Without
ax.annotate("", xy=(6.3, 4.8), xytext=(7.1, 5.9), arrowprops=dict(arrowstyle="->", lw=1.5, color="#4a5568"))
ax.annotate("", xy=(8.7, 4.8), xytext=(7.9, 5.9), arrowprops=dict(arrowstyle="->", lw=1.5, color="#4a5568"))
ax.text(6.4, 5.5, "WITHOUT replacement", ha='center', fontsize=8, style='italic')
ax.text(8.6, 5.5, "WITH replacement", ha='center', fontsize=8, style='italic')

# Leaf nodes (Formulas)
leaf1 = dict(boxstyle="round,pad=0.5", fc="#ffffff", ec="#3182ce", lw=1.5)
ax.text(1.3, 4.0, "Multiplication Rule\n(Exponential)\n\n$N = n^k$\n\nEx: PINs, coin tosses", ha='center', va='center', bbox=leaf1, fontsize=9)

leaf2 = dict(boxstyle="round,pad=0.5", fc="#ffffff", ec="#3182ce", lw=1.5)
ax.text(3.7, 4.0, "Permutations\n(${}_n P_k$)\n\n$P(n, k) = \\frac{n!}{(n-k)!}$\n\nEx: Officers, rankings", ha='center', va='center', bbox=leaf2, fontsize=9)

leaf3 = dict(boxstyle="round,pad=0.5", fc="#ffffff", ec="#e53e3e", lw=1.5)
ax.text(6.3, 4.0, "Combinations\n$\\binom{n}{k}$\n\n$\\binom{n}{k} = \\frac{n!}{k!(n-k)!}$\n\nEx: Committees, poker hands", ha='center', va='center', bbox=leaf3, fontsize=9)

leaf4 = dict(boxstyle="round,pad=0.5", fc="#ffffff", ec="#e53e3e", lw=1.5)
ax.text(8.7, 4.0, "Multisets / Stars & Bars\n(Supplementary)\n\n$\\binom{n+k-1}{k}$\n\nEx: Donut selections", ha='center', va='center', bbox=leaf4, fontsize=9)

# Additional Note: Permutations of Indistinguishable Objects
leaf5 = dict(boxstyle="round,pad=0.5", fc="#f7fafc", ec="#805ad5", lw=1.5)
ax.text(5, 1.8, "Special Case: Permutations of Non-Distinct (Repeated) Items\nPartitioning $n$ objects of $r$ types with counts $n_1, n_2, \\dots, n_r$ into a full sequence:\n$\\frac{n!}{n_1! \\, n_2! \\dots n_r!}$\nEx: Anagrams (MISSISSIPPI), Colored Balls, Multi-item Schedules", ha='center', va='center', bbox=leaf5, fontsize=9.5)

ax.set_xlim(0, 10)
ax.set_ylim(1.0, 10.0)
plt.tight_layout()
plt.savefig('W2/Study-Notes-Markdown/graphs/counting-decision-tree.png', bbox_inches='tight')
plt.close()

# -------------------------------------------------------------
# Graph 2: Inclusion-Exclusion Venn Diagram (3 Events)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 7), dpi=300)
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.axis('off')

# Centers of 3 circles
c_a = (-0.6, 0.5)
c_b = (0.6, 0.5)
c_c = (0.0, -0.6)
r = 1.3

circle_a = plt.Circle(c_a, r, color='#3182ce', alpha=0.3, ec='#2b6cb0', lw=2)
circle_b = plt.Circle(c_b, r, color='#e53e3e', alpha=0.3, ec='#c53030', lw=2)
circle_c = plt.Circle(c_c, r, color='#38a169', alpha=0.3, ec='#276749', lw=2)

ax.add_patch(circle_a)
ax.add_patch(circle_b)
ax.add_patch(circle_c)

ax.text(-1.4, 1.5, "Event $A$", fontsize=13, fontweight='bold', color='#2b6cb0')
ax.text(1.4, 1.5, "Event $B$", fontsize=13, fontweight='bold', color='#c53030')
ax.text(0.0, -2.1, "Event $C$", fontsize=13, fontweight='bold', color='#276749', ha='center')

# Labels of regions
ax.text(-1.0, 0.7, "$A$ only\n$A \\cap B^c \\cap C^c$", fontsize=8, ha='center', va='center')
ax.text(1.0, 0.7, "$B$ only\n$A^c \\cap B \\cap C^c$", fontsize=8, ha='center', va='center')
ax.text(0.0, -1.2, "$C$ only\n$A^c \\cap B^c \\cap C$", fontsize=8, ha='center', va='center')

ax.text(0.0, 0.9, "$A \\cap B \\cap C^c$", fontsize=8, ha='center', va='center')
ax.text(-0.6, -0.2, "$A \\cap C \\cap B^c$", fontsize=8, ha='center', va='center')
ax.text(0.6, -0.2, "$B \\cap C \\cap A^c$", fontsize=8, ha='center', va='center')

ax.text(0.0, 0.15, "$A \\cap B \\cap C$", fontsize=9, fontweight='bold', ha='center', va='center', color='#742a2a')

plt.title("Principle of Inclusion-Exclusion (Three Events):\n$P(A \\cup B \\cup C) = \\sum P(A) - \\sum P(A \\cap B) + P(A \\cap B \\cap C)$", fontsize=12, pad=20, fontweight='bold')
plt.tight_layout()
plt.savefig('W2/Study-Notes-Markdown/graphs/inclusion-exclusion-3-events.png', bbox_inches='tight')
plt.close()

# -------------------------------------------------------------
# Graph 3: WLLN Simulation Plot
# -------------------------------------------------------------
np.random.seed(42)
n_trials = 1000
p_true = 1.0 / 3.0  # Rock-Paper-Scissors win prob against random bot

fig, ax = plt.subplots(figsize=(9, 5), dpi=300)

for sim in range(5):
    outcomes = (np.random.rand(n_trials) < p_true).astype(int)
    cum_freq = np.cumsum(outcomes) / np.arange(1, n_trials + 1)
    ax.plot(np.arange(1, n_trials + 1), cum_freq, alpha=0.7, lw=1.5, label=f"Simulation Run {sim+1}")

ax.axhline(p_true, color='#e53e3e', linestyle='--', lw=2.5, label=f"Theoretical Probability $P(A) = 1/3$")

ax.set_title("Weak Law of Large Numbers (WLLN) Simulation:\nConvergence of Relative Frequency $\\bar{X}_n$ to $P(A) = 1/3$", fontsize=13, fontweight='bold')
ax.set_xlabel("Number of Trials ($n$)", fontsize=11)
ax.set_ylabel("Relative Frequency of Success $\\bar{X}_n$", fontsize=11)
ax.set_ylim(0.1, 0.6)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right', frameon=True)

plt.tight_layout()
plt.savefig('W2/Study-Notes-Markdown/graphs/wlln-simulation.png', bbox_inches='tight')
plt.close()

# -------------------------------------------------------------
# Graph 4: Birthday Problem Curve
# -------------------------------------------------------------
k_vals = np.arange(1, 61)
p_no_match = np.zeros(len(k_vals))
curr = 1.0
for i, k in enumerate(k_vals):
    curr *= (365 - k + 1) / 365.0
    p_no_match[i] = curr
p_match = 1.0 - p_no_match

fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
ax.plot(k_vals, p_match, color='#2b6cb0', lw=2.5, label="P(At least 2 people share a birthday)")

# Highlight k = 10 (lecture example)
p10 = p_match[9]
ax.plot(10, p10, 'ro', markersize=8)
ax.annotate(f"k = 10: P = {p10:.4f} (11.69%)\n[Lecture Example]", xy=(10, p10), xytext=(14, 0.2),
            arrowprops=dict(arrowstyle="->", color='#c53030', lw=1.5),
            fontsize=9, fontweight='bold', color='#c53030')

# Highlight k = 23 (classic threshold > 50%)
p23 = p_match[22]
ax.plot(23, p23, 'go', markersize=8)
ax.annotate(f"k = 23: P = {p23:.4f} (50.73%)\n[Classic Paradox Threshold]", xy=(23, p23), xytext=(27, 0.45),
            arrowprops=dict(arrowstyle="->", color='#276749', lw=1.5),
            fontsize=9, fontweight='bold', color='#276749')

ax.axhline(0.5, color='gray', linestyle=':', lw=1.5, alpha=0.7)
ax.set_title("The Birthday Problem: Probability of at Least One Shared Birthday vs. Group Size $k$", fontsize=12, fontweight='bold')
ax.set_xlabel("Number of People in Group ($k$)", fontsize=11)
ax.set_ylabel("Probability of Coincidence $P(A)$", fontsize=11)
ax.set_xlim(0, 60)
ax.set_ylim(0, 1.05)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='lower right', frameon=True)

plt.tight_layout()
plt.savefig('W2/Study-Notes-Markdown/graphs/birthday-problem.png', bbox_inches='tight')
plt.close()

print("Graphs generated successfully!")
