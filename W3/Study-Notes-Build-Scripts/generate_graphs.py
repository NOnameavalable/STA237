import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

os.makedirs('W3/Study-Notes-Markdown/graphs', exist_ok=True)
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

# -------------------------------------------------------------
# Graph 1: Conditional Probability as Sample Space Restriction
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
ax.set_xlim(-0.5, 9.5)
ax.set_ylim(-0.5, 6.5)
ax.axis('off')

# Universal set Omega
rect_omega = patches.Rectangle((0, 0), 9, 6, linewidth=2, edgecolor='#2d3748', facecolor='#f7fafc')
ax.add_patch(rect_omega)
ax.text(8.6, 5.5, r'$\Omega$', fontsize=18, fontweight='bold', color='#2d3748')

# Conditioning event B (the new universe)
circle_b = patches.Circle((5.5, 3.0), 2.2, facecolor='#bee3f8', edgecolor='#2b6cb0', linewidth=2.5, alpha=0.6)
ax.add_patch(circle_b)

# Event A
circle_a = patches.Circle((3.2, 3.0), 2.0, facecolor='#fed7d7', edgecolor='#c53030', linewidth=2, alpha=0.4)
ax.add_patch(circle_a)

ax.text(4.4, 3.0, r'$A \cap B$', fontsize=13, fontweight='bold', ha='center', va='center', color='#2c5282')

# Labels
ax.text(2.2, 3.0, r'Event $A$', fontsize=14, fontweight='bold', color='#9b2c2c', ha='center')
ax.text(6.8, 3.0, 'Conditioning Event $B$\n(New Restricted Sample Space)', fontsize=12, fontweight='bold', color='#2b6cb0', ha='center')

# Annotations explaining the shrinkage
bbox_note = dict(boxstyle='round,pad=0.5', fc='#ffffff', ec='#4a5568', lw=1.5)
formula_text = (
    "Sample Space Restriction:\n"
    r"• Original Universe: $\Omega \rightarrow P(\Omega) = 1$" + "\n"
    r"• Given $B$ occurred: Outer space $(\Omega \setminus B)$ is discarded" + "\n"
    r"• New Universe: $B \rightarrow P(B|B) = 1$" + "\n"
    r"• Favorable region inside $B$: $A \cap B$" + "\n"
    r"• Formula: $P(A|B) = \frac{P(A \cap B)}{P(B)}$" + "\n"
    r"• Normalizes probability mass of $(A \cap B)$ relative to $B$."
)
ax.text(0.3, 0.4, formula_text, fontsize=9.5, bbox=bbox_note, va='bottom', ha='left')

plt.title(r"Conditional Probability: Sample Space Reduction from $\Omega$ to $B$", fontsize=14, fontweight='bold', color='#1a365d', pad=12)
plt.tight_layout()
plt.savefig('W3/Study-Notes-Markdown/graphs/conditional-sample-space-reduction.png', bbox_inches='tight')
plt.close()

# -------------------------------------------------------------
# Graph 2: Independent vs. Mutually Exclusive (Disjoint) Events
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5), dpi=300)

for ax in (ax1, ax2):
    ax.set_xlim(-0.2, 5.2)
    ax.set_ylim(-0.2, 4.2)
    ax.axis('off')
    rect = patches.Rectangle((0, 0), 5, 4, linewidth=1.5, edgecolor='#4a5568', facecolor='#f7fafc')
    ax.add_patch(rect)
    ax.text(4.6, 3.6, r'$\Omega$', fontsize=14, fontweight='bold', color='#4a5568')

# Panel 1: Mutually Exclusive (Disjoint)
c1 = patches.Circle((1.5, 2.0), 1.0, facecolor='#feb2b2', edgecolor='#e53e3e', lw=2, alpha=0.6)
c2 = patches.Circle((3.5, 2.0), 1.0, facecolor='#bee3f8', edgecolor='#3182ce', lw=2, alpha=0.6)
ax1.add_patch(c1)
ax1.add_patch(c2)
ax1.text(1.5, 2.0, r'$A$', fontsize=14, fontweight='bold', ha='center', va='center')
ax1.text(3.5, 2.0, r'$B$', fontsize=14, fontweight='bold', ha='center', va='center')
ax1.set_title("Mutually Exclusive (Disjoint)\n" + r"$A \cap B = \emptyset \rightarrow P(A \cap B) = 0$", fontsize=12, fontweight='bold', color='#c53030')
bbox_box1 = dict(boxstyle='square,pad=0.4', fc='#fff5f5', ec='#e53e3e', lw=1.2)
ax1.text(2.5, 0.4, "Cannot occur together!\nIf $P(A), P(B) > 0$, disjoint events\nare NEVER independent:\n$P(A|B) = 0 \neq P(A)$.", ha='center', fontsize=9, bbox=bbox_box1)

# Panel 2: Independent Events
c3 = patches.Circle((2.0, 2.0), 1.1, facecolor='#fed7d7', edgecolor='#e53e3e', lw=2, alpha=0.5)
c4 = patches.Circle((3.0, 2.0), 1.1, facecolor='#bee3f8', edgecolor='#3182ce', lw=2, alpha=0.5)
ax2.add_patch(c3)
ax2.add_patch(c4)
ax2.text(1.5, 2.0, r'$A$', fontsize=14, fontweight='bold', ha='center', va='center')
ax2.text(3.5, 2.0, r'$B$', fontsize=14, fontweight='bold', ha='center', va='center')
ax2.text(2.5, 2.0, r'$A \cap B$', fontsize=10, fontweight='bold', ha='center', va='center', color='#2b6cb0')
ax2.set_title("Statistically Independent\n" + r"$P(A \cap B) = P(A) \cdot P(B)$", fontsize=12, fontweight='bold', color='#2b6cb0')
bbox_box2 = dict(boxstyle='square,pad=0.4', fc='#ebf8ff', ec='#3182ce', lw=1.2)
ax2.text(2.5, 0.4, "CAN occur together!\nOccurrence of $B$ does NOT alter chance of $A$:\n$P(A|B) = P(A)$ and $P(B|A) = P(B)$.", ha='center', fontsize=9, bbox=bbox_box2)

plt.tight_layout()
plt.savefig('W3/Study-Notes-Markdown/graphs/independent-vs-mutually-exclusive.png', bbox_inches='tight')
plt.close()

# -------------------------------------------------------------
# Graph 3: System Reliability Circuit Configurations
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6.5), dpi=300)

for ax in (ax1, ax2):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')

# Circuit 1: Lecture Example 3 (Bridge/Hybrid: Parallel 1,2 in Series with 3)
ax1.set_title("System 1: Lecture Example 3 — Parallel Subsystem in Series with Component 3", fontsize=11, fontweight='bold', color='#1a365d')
# Input wire
ax1.plot([0.5, 1.8], [2.5, 2.5], 'k-', lw=2.5)
# Split
ax1.plot([1.8, 1.8], [1.3, 3.7], 'k-', lw=2.5)
ax1.plot([1.8, 2.5], [3.7, 3.7], 'k-', lw=2.5)
ax1.plot([1.8, 2.5], [1.3, 1.3], 'k-', lw=2.5)
# Box 1
b1 = patches.Rectangle((2.5, 3.1), 2.2, 1.2, fc='#feebc8', ec='#dd6b20', lw=2)
ax1.add_patch(b1)
ax1.text(3.6, 3.7, "Component 1\n$p_1 = 0.90$", ha='center', va='center', fontsize=9, fontweight='bold')
# Box 2
b2 = patches.Rectangle((2.5, 0.7), 2.2, 1.2, fc='#feebc8', ec='#dd6b20', lw=2)
ax1.add_patch(b2)
ax1.text(3.6, 1.3, "Component 2\n$p_2 = 0.95$", ha='center', va='center', fontsize=9, fontweight='bold')
# Merge parallel
ax1.plot([4.7, 5.4], [3.7, 3.7], 'k-', lw=2.5)
ax1.plot([4.7, 5.4], [1.3, 1.3], 'k-', lw=2.5)
ax1.plot([5.4, 5.4], [1.3, 3.7], 'k-', lw=2.5)
ax1.plot([5.4, 6.2], [2.5, 2.5], 'k-', lw=2.5)
# Box 3
b3 = patches.Rectangle((6.2, 1.9), 2.2, 1.2, fc='#c6f6d5', ec='#38a169', lw=2)
ax1.add_patch(b3)
ax1.text(7.3, 2.5, "Component 3\n$p_3 = 0.99$", ha='center', va='center', fontsize=9, fontweight='bold')
# Output wire
ax1.plot([8.4, 9.5], [2.5, 2.5], 'k-', lw=2.5)
ax1.text(9.6, 2.5, "Output", va='center', fontsize=10, fontweight='bold')
ax1.text(0.4, 2.5, "Input", va='center', ha='right', fontsize=10, fontweight='bold')

# Formula annotation
ax1.text(5.0, 0.1, r"$P(\mathrm{System\ Works}) = [1 - (1 - p_1)(1 - p_2)] \cdot p_3 = [1 - (0.10)(0.05)] \cdot 0.99 = 0.995 \cdot 0.99 = 0.98505$", ha='center', fontsize=9.5, color='#2c5282', fontweight='bold')

# Circuit 2: MMSA Exercise 83 (Parallel Subsystem A in Parallel with Series Subsystem B)
ax2.set_title("System 2: MMSA Exercise 83 — Parallel Subsystem (1 || 2) in Parallel with Series Subsystem (3 -- 4)", fontsize=11, fontweight='bold', color='#1a365d')
# Input wire
ax2.plot([0.5, 1.5], [2.5, 2.5], 'k-', lw=2.5)
# Split top and bottom
ax2.plot([1.5, 1.5], [1.1, 3.9], 'k-', lw=2.5)
# Top branch: Subsystem A (1 and 2 in parallel)
ax2.plot([1.5, 2.2], [3.9, 3.9], 'k-', lw=2)
ax2.plot([2.2, 2.2], [3.2, 4.6], 'k-', lw=2)
ax2.plot([2.2, 2.6], [4.6, 4.6], 'k-', lw=2)
ax2.plot([2.2, 2.6], [3.2, 3.2], 'k-', lw=2)
b_m1 = patches.Rectangle((2.6, 4.1), 1.5, 1.0, fc='#e9d8fd', ec='#805ad5', lw=1.5)
b_m2 = patches.Rectangle((2.6, 2.7), 1.5, 1.0, fc='#e9d8fd', ec='#805ad5', lw=1.5)
ax2.add_patch(b_m1)
ax2.add_patch(b_m2)
ax2.text(3.35, 4.6, "1 (0.9)", ha='center', va='center', fontsize=8.5, fontweight='bold')
ax2.text(3.35, 3.2, "2 (0.9)", ha='center', va='center', fontsize=8.5, fontweight='bold')
ax2.plot([4.1, 4.5], [4.6, 4.6], 'k-', lw=2)
ax2.plot([4.1, 4.5], [3.2, 3.2], 'k-', lw=2)
ax2.plot([4.5, 4.5], [3.2, 4.6], 'k-', lw=2)
ax2.plot([4.5, 8.5], [3.9, 3.9], 'k-', lw=2)

# Bottom branch: Subsystem B (3 and 4 in series)
ax2.plot([1.5, 3.0], [1.1, 1.1], 'k-', lw=2)
b_m3 = patches.Rectangle((3.0, 0.6), 1.5, 1.0, fc='#bee3f8', ec='#3182ce', lw=1.5)
b_m4 = patches.Rectangle((5.5, 0.6), 1.5, 1.0, fc='#bee3f8', ec='#3182ce', lw=1.5)
ax2.add_patch(b_m3)
ax2.add_patch(b_m4)
ax2.text(3.75, 1.1, "3 (0.9)", ha='center', va='center', fontsize=8.5, fontweight='bold')
ax2.text(6.25, 1.1, "4 (0.9)", ha='center', va='center', fontsize=8.5, fontweight='bold')
ax2.plot([4.5, 5.5], [1.1, 1.1], 'k-', lw=2)
ax2.plot([7.0, 8.5], [1.1, 1.1], 'k-', lw=2)

# Merge top and bottom branches at output
ax2.plot([8.5, 8.5], [1.1, 3.9], 'k-', lw=2.5)
ax2.plot([8.5, 9.5], [2.5, 2.5], 'k-', lw=2.5)
ax2.text(9.6, 2.5, "Output", va='center', fontsize=10, fontweight='bold')
ax2.text(0.4, 2.5, "Input", va='center', ha='right', fontsize=10, fontweight='bold')

# Formula annotation
ax2.text(5.0, 0.05, r"$P(\mathrm{Works}) = 1 - P(\mathrm{Both\ Branches\ Fail}) = 1 - [1 - (1 - 0.1^2)][1 - 0.9^2] = 1 - (0.01)(0.19) = 0.9981$", ha='center', fontsize=9.5, color='#2c5282', fontweight='bold')

plt.tight_layout()
plt.savefig('W3/Study-Notes-Markdown/graphs/circuit-reliability-diagrams.png', bbox_inches='tight')
plt.close()

# -------------------------------------------------------------
# Graph 4: Law of Total Probability (Partition of Sample Space)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.5, 6.5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

# Bounding box Omega
rect = patches.Rectangle((0.5, 1.5), 9, 4.8, facecolor='#f7fafc', edgecolor='#2d3748', lw=2)
ax.add_patch(rect)
ax.text(9.2, 5.75, r'$\Omega$', fontsize=16, fontweight='bold', color='#2d3748')

# Partition lines for B1, B2, B3, B4, B5
x_divs = [0.5, 2.3, 4.1, 5.9, 7.7, 9.5]
colors_part = ['#edf2f7', '#feebc8', '#e6fffa', '#ebf8ff', '#faf5ff']
for i in range(5):
    sub_rect = patches.Rectangle((x_divs[i], 1.5), x_divs[i+1]-x_divs[i], 4.8, facecolor=colors_part[i], edgecolor='#718096', lw=1.5, linestyle='--')
    ax.add_patch(sub_rect)
    ax.text((x_divs[i]+x_divs[i+1])/2, 5.95, f'$B_{i+1}$', fontsize=12, fontweight='bold', ha='center', color='#4a5568')

# Event A cutting across all partitions
ellipse_a = patches.Ellipse((5.0, 4.1), 8.1, 2.7, facecolor='#feb2b2', edgecolor='#e53e3e', lw=2.5, alpha=0.55)
ax.add_patch(ellipse_a)
ax.text(5.0, 4.85, r'Target Event $A = \bigcup_{i=1}^k (A \cap B_i)$', fontsize=11, fontweight='bold', ha='center', color='#9b2c2c')

for i in range(5):
    x_c = (x_divs[i]+x_divs[i+1])/2
    ax.text(x_c, 4.1, f'$A \\cap B_{i+1}$', fontsize=11, fontweight='bold', ha='center', va='center', color='#742a2a')

# Mathematical summary box
bbox_ltp = dict(boxstyle='round,pad=0.5', fc='#ffffff', ec='#2b6cb0', lw=1.5)
ltp_formula = (
    r"If $\{B_1, \dots, B_k\}$ partitions $\Omega$ ($B_i \cap B_j = \emptyset, \bigcup B_i = \Omega$), then for any event $A$:" + "\n"
    r"$P(A) = \sum_{i=1}^k P(A \cap B_i) = \sum_{i=1}^k P(A|B_i) \cdot P(B_i)$"
)
ax.text(5.0, 1.9, "Law of Total Probability", ha='center', va='center', fontsize=11, fontweight='bold', color='#1a365d')
ax.text(5.0, 0.12, ltp_formula, ha='center', va='bottom', fontsize=9.5, bbox=bbox_ltp)

plt.title(r"Law of Total Probability: Decomposing Event $A$ Across a Partition $\{B_i\}$", fontsize=13, fontweight='bold', color='#1a365d', pad=10)
plt.tight_layout()
plt.savefig('W3/Study-Notes-Markdown/graphs/law-of-total-probability-partition.png', bbox_inches='tight')
plt.close()

# -------------------------------------------------------------
# Graph 5: Bayes' Theorem Probability Tree (Diagnostic Testing)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6.2), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(-0.8, 6)
ax.axis('off')

# Root
ax.text(0.5, 3.0, "Population\nSample", ha='center', va='center', bbox=dict(boxstyle='round,pad=0.4', fc='#edf2f7', ec='#4a5568', lw=1.5), fontsize=10, fontweight='bold')

# Prior Branches
ax.annotate("", xy=(3.0, 4.5), xytext=(1.2, 3.2), arrowprops=dict(arrowstyle="->", lw=2, color="#c53030"))
ax.annotate("", xy=(3.0, 1.5), xytext=(1.2, 2.8), arrowprops=dict(arrowstyle="->", lw=2, color="#3182ce"))

ax.text(2.0, 4.2, "Has Disease ($D$)\nPrior: $P(D) = 0.02$", ha='center', fontsize=9, color="#9b2c2c", fontweight='bold')
ax.text(2.0, 1.8, "Healthy ($D^c$)\nPrior: $P(D^c) = 0.98$", ha='center', fontsize=9, color="#2b6cb0", fontweight='bold')

# Stage 1 Nodes
ax.text(3.3, 4.5, "Infected ($D$)", ha='left', va='center', bbox=dict(boxstyle='square,pad=0.3', fc='#fff5f5', ec='#e53e3e', lw=1.2), fontsize=9, fontweight='bold')
ax.text(3.3, 1.5, "Healthy ($D^c$)", ha='left', va='center', bbox=dict(boxstyle='square,pad=0.3', fc='#ebf8ff', ec='#3182ce', lw=1.2), fontsize=9, fontweight='bold')

# Conditional Branches from D
ax.annotate("", xy=(6.5, 5.2), xytext=(4.7, 4.6), arrowprops=dict(arrowstyle="->", lw=1.5, color="#4a5568"))
ax.annotate("", xy=(6.5, 3.8), xytext=(4.7, 4.4), arrowprops=dict(arrowstyle="->", lw=1.5, color="#4a5568"))
ax.text(5.5, 5.2, "Test $+$ (Sensitivity)\n$P(+|D) = 0.95$", ha='center', fontsize=8, color="#2d3748")
ax.text(5.5, 3.8, "Test $-$ (False Neg)\n$P(-|D) = 0.05$", ha='center', fontsize=8, color="#718096")

# Conditional Branches from D^c
ax.annotate("", xy=(6.5, 2.2), xytext=(4.7, 1.6), arrowprops=dict(arrowstyle="->", lw=1.5, color="#4a5568"))
ax.annotate("", xy=(6.5, 0.8), xytext=(4.7, 1.4), arrowprops=dict(arrowstyle="->", lw=1.5, color="#4a5568"))
ax.text(5.5, 2.2, "Test $+$ (False Pos)\n$P(+|D^c) = 0.01$", ha='center', fontsize=8, color="#e53e3e", fontweight='bold')
ax.text(5.5, 0.8, "Test $-$ (Specificity)\n$P(-|D^c) = 0.99$", ha='center', fontsize=8, color="#2d3748")

# Leaf Outcomes & Joint Probabilities
leaf_box1 = dict(boxstyle='round,pad=0.4', fc='#fed7d7', ec='#e53e3e', lw=1.5)
leaf_box2 = dict(boxstyle='round,pad=0.3', fc='#ffffff', ec='#a0aec0', lw=1.0)
leaf_box3 = dict(boxstyle='round,pad=0.4', fc='#feebc8', ec='#dd6b20', lw=1.5)
leaf_box4 = dict(boxstyle='round,pad=0.3', fc='#ffffff', ec='#a0aec0', lw=1.0)

ax.text(8.3, 5.2, r"$P(D \cap +) = 0.02 \cdot 0.95 = 0.0190$" + "\n" + "(True Positive)", ha='center', va='center', bbox=leaf_box1, fontsize=8.5)
ax.text(8.3, 3.8, r"$P(D \cap -) = 0.02 \cdot 0.05 = 0.0010$" + "\n" + "(False Negative)", ha='center', va='center', bbox=leaf_box2, fontsize=8)
ax.text(8.3, 2.2, r"$P(D^c \cap +) = 0.98 \cdot 0.01 = 0.0098$" + "\n" + "(False Positive)", ha='center', va='center', bbox=leaf_box3, fontsize=8.5)
ax.text(8.3, 0.8, r"$P(D^c \cap -) = 0.98 \cdot 0.99 = 0.9702$" + "\n" + "(True Negative)", ha='center', va='center', bbox=leaf_box4, fontsize=8)

# Bayes Inversion Formula Box
bbox_post = dict(boxstyle='round,pad=0.5', fc='#f7fafc', ec='#2b6cb0', lw=2)
bayes_text = (
    "Bayes' Inversion (Positive Predictive Value):\n"
    r"$P(D|+) = \frac{P(D \cap +)}{P(+)} = \frac{P(+|D)P(D)}{P(+|D)P(D) + P(+|D^c)P(D^c)} = \frac{0.0190}{0.0190 + 0.0098} = \frac{0.0190}{0.0288} \approx \mathbf{65.97\%}$"
)
ax.text(5.0, -0.4, bayes_text, ha='center', va='top', fontsize=9.5, bbox=bbox_post)

plt.title("Tree Diagram for Bayes' Rule: Medical Diagnostic Screening & Base Rate Effect", fontsize=13, fontweight='bold', color='#1a365d', pad=10)
plt.tight_layout()
plt.savefig('W3/Study-Notes-Markdown/graphs/bayes-diagnostic-testing-tree.png', bbox_inches='tight')
plt.close()

# -------------------------------------------------------------
# Graph 6: Discrete PMF Distribution (Histogram & Line Graph)
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8), dpi=300)

x_vals = np.array([0, 1, 2, 3, 4])
p_vals = np.array([0.30, 0.25, 0.20, 0.15, 0.10])

# Subplot 1: Probability Histogram
ax1.bar(x_vals, p_vals, width=1.0, edgecolor='#2b6cb0', facecolor='#bee3f8', alpha=0.7, align='center', lw=1.5)
ax1.set_xticks(x_vals)
ax1.set_xlabel('Number of Students ($x$)', fontsize=11, fontweight='bold')
ax1.set_ylabel('Probability $P(X = x)$', fontsize=11, fontweight='bold')
ax1.set_title('Probability Histogram\n(Rectangle Area = Probability)', fontsize=11, fontweight='bold', color='#1a365d')
ax1.set_ylim(0, 0.35)
for x, p in zip(x_vals, p_vals):
    ax1.text(x, p + 0.01, f'{p:.2f}', ha='center', fontsize=9.5, fontweight='bold', color='#2b6cb0')
ax1.grid(axis='y', linestyle=':', alpha=0.6)

# Subplot 2: Line Graph / Spike Plot
markerline, stemlines, baseline = ax2.stem(x_vals, p_vals)
plt.setp(stemlines, 'linewidth', 2, 'color', '#3182ce')
plt.setp(markerline, 'markersize', 8, 'color', '#2b6cb0')
ax2.set_xticks(x_vals)
ax2.set_xlabel('Number of Students ($x$)', fontsize=11, fontweight='bold')
ax2.set_ylabel('Probability $p(x)$', fontsize=11, fontweight='bold')
ax2.set_title('Line Graph (Spike Plot)\n(Vertical Line Height = Probability Mass)', fontsize=11, fontweight='bold', color='#1a365d')
ax2.set_ylim(0, 0.35)
for x, p in zip(x_vals, p_vals):
    ax2.text(x, p + 0.01, f'{p:.2f}', ha='center', fontsize=9.5, fontweight='bold', color='#2b6cb0')
ax2.grid(axis='y', linestyle=':', alpha=0.6)

fig.text(0.5, -0.05, r"$\mathbf{Valid\ PMF\ Axioms:}\quad \mathrm{(1)}\ 0 \leq P(X=x) \leq 1\quad \forall x \in \mathcal{X}, \quad \mathrm{and}\quad \mathrm{(2)}\ \sum_{x \in \mathcal{X}} P(X=x) = 0.30+0.25+0.20+0.15+0.10 = 1.00$", ha='center', fontsize=10, bbox=dict(boxstyle='round,pad=0.4', fc='#f7fafc', ec='#4a5568', lw=1.2))

plt.suptitle("Probability Mass Function (PMF) Visual Representations (MMSA Ch. 3 #11)", fontsize=13, fontweight='bold', color='#1a365d', y=1.03)
plt.tight_layout()
plt.savefig('W3/Study-Notes-Markdown/graphs/pmf-distribution-visualization.png', bbox_inches='tight')
plt.close()

print("All 6 figures generated successfully in W3/Study-Notes-Markdown/graphs/")
