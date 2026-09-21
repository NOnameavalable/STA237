#!/usr/bin/env python3
"""
Generate publication-quality mathematical diagrams for STA237 Week 1 Study Notes.
Figures produced:
1. venn-complement.png
2. venn-two-events.png
3. venn-disjoint.png
4. venn-demorgan.png
5. venn-inclusion-exclusion.png
6. venn-three-events.png
7. dice-sample-space.png
8. venn-movie-survey.png
9. venn-par38.png
10. venn-mmsa10.png
"""

import os
import sys

# Ensure custom matplotlib config dir in scratch to avoid warnings
scratch_dir = "/tmp/codex_sta237_mpl"
os.makedirs(scratch_dir, exist_ok=True)
os.environ['MPLCONFIGDIR'] = scratch_dir

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Ensure target directory exists
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "graphs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.rcParams.update({
    'font.size': 11,
    'font.family': 'sans-serif',
    'figure.autolayout': True,
    'figure.dpi': 300
})

# -------------------------------------------------------------
# 1. Venn Diagram: Complement Event
# -------------------------------------------------------------
def create_venn_complement():
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Sample space S
    rect = patches.Rectangle((0.5, 0.5), 9, 6, linewidth=2, edgecolor='#1f2937', facecolor='#f3f4f6')
    ax.add_patch(rect)
    ax.text(0.8, 6.1, r'Sample Space $S$ ($\Omega$)', fontsize=13, fontweight='bold', color='#1f2937')

    # Event A
    circle_a = patches.Circle((4.5, 3.5), 2.2, linewidth=2, edgecolor='#1e40af', facecolor='#93c5fd', alpha=0.85)
    ax.add_patch(circle_a)
    ax.text(4.5, 3.5, r'Event $A$', fontsize=14, fontweight='bold', ha='center', va='center', color='#1e3a8a')

    # Complement A^c
    ax.text(7.8, 5.0, r'Complement $A^c$' + '\n' + r'($A^\prime$)', fontsize=13, fontweight='bold', ha='center', va='center', color='#374151')
    ax.text(7.8, 2.0, r'$A \cup A^c = S$' + '\n' + r'$A \cap A^c = \emptyset$', fontsize=11, ha='center', va='center', color='#4b5563',
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="#d1d5db", alpha=0.9))

    plt.savefig(os.path.join(OUTPUT_DIR, "venn-complement.png"), bbox_inches='tight')
    plt.close()

# -------------------------------------------------------------
# 2. Venn Diagram: Two Intersecting Events & 4 Disjoint Regions
# -------------------------------------------------------------
def create_venn_two_events():
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    # Sample space S
    rect = patches.Rectangle((0.5, 0.5), 10, 6.5, linewidth=2, edgecolor='#1f2937', facecolor='#f9fafb')
    ax.add_patch(rect)
    ax.text(0.9, 6.5, r'Sample Space $S$', fontsize=13, fontweight='bold', color='#1f2937')

    # Circle A and Circle B
    circle_a = patches.Circle((4.3, 3.8), 2.3, linewidth=2, edgecolor='#1d4ed8', facecolor='#bfdbfe', alpha=0.6)
    circle_b = patches.Circle((6.7, 3.8), 2.3, linewidth=2, edgecolor='#b91c1c', facecolor='#fecaca', alpha=0.6)
    ax.add_patch(circle_a)
    ax.add_patch(circle_b)

    # Labels for events
    ax.text(3.0, 5.8, r'Event $A$', fontsize=13, fontweight='bold', color='#1d4ed8', ha='center')
    ax.text(8.0, 5.8, r'Event $B$', fontsize=13, fontweight='bold', color='#b91c1c', ha='center')

    # Region labels
    ax.text(3.1, 3.8, r'$A \cap B^c$' + '\n' + r'($A$ only)', fontsize=11, ha='center', va='center', fontweight='bold', color='#1e3a8a')
    ax.text(5.5, 3.8, r'$A \cap B$' + '\n' + r'(both)', fontsize=11, ha='center', va='center', fontweight='bold', color='#4c1d95')
    ax.text(7.9, 3.8, r'$A^c \cap B$' + '\n' + r'($B$ only)', fontsize=11, ha='center', va='center', fontweight='bold', color='#991b1b')
    ax.text(9.0, 1.3, r'$(A \cup B)^c = A^c \cap B^c$' + '\n' + r'(neither)', fontsize=11, ha='center', va='center', fontweight='bold', color='#374151')

    # Partition equation box
    ax.text(5.5, 0.9, r'Partition: $S = (A \cap B^c) \cup (A \cap B) \cup (A^c \cap B) \cup (A \cup B)^c$',
            fontsize=10, ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#cbd5e1"))

    plt.savefig(os.path.join(OUTPUT_DIR, "venn-two-events.png"), bbox_inches='tight')
    plt.close()

# -------------------------------------------------------------
# 3. Venn Diagram: Mutually Exclusive (Disjoint) Events
# -------------------------------------------------------------
def create_venn_disjoint():
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis('off')

    rect = patches.Rectangle((0.5, 0.5), 10, 6, linewidth=2, edgecolor='#1f2937', facecolor='#f8fafc')
    ax.add_patch(rect)
    ax.text(0.9, 6.0, r'Sample Space $S$', fontsize=13, fontweight='bold', color='#1f2937')

    circle_a = patches.Circle((3.2, 3.5), 1.9, linewidth=2, edgecolor='#047857', facecolor='#a7f3d0', alpha=0.7)
    circle_b = patches.Circle((7.8, 3.5), 1.9, linewidth=2, edgecolor='#d97706', facecolor='#fde68a', alpha=0.7)
    ax.add_patch(circle_a)
    ax.add_patch(circle_b)

    ax.text(3.2, 3.5, r'Event $A$', fontsize=13, fontweight='bold', ha='center', va='center', color='#065f46')
    ax.text(7.8, 3.5, r'Event $B$', fontsize=13, fontweight='bold', ha='center', va='center', color='#92400e')

    # Distinct property box
    ax.text(5.5, 3.5, r'$A \cap B = \emptyset$' + '\n' + r'(Disjoint)', fontsize=12, fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#fee2e2", edgecolor="#ef4444"))

    ax.text(5.5, 1.2, r'Axiom 3 Additivity: $P(A \cup B) = P(A) + P(B)$' + '\n' +
            r'Note: If $P(A)>0$ and $P(B)>0$, disjoint events are ALWAYS DEPENDENT ($P(A \cap B) = 0 \ne P(A)P(B)$).',
            fontsize=10, ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="#cbd5e1"))

    plt.savefig(os.path.join(OUTPUT_DIR, "venn-disjoint.png"), bbox_inches='tight')
    plt.close()

# -------------------------------------------------------------
# 4. Venn Diagram: De Morgan's Laws
# -------------------------------------------------------------
def create_venn_demorgan():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
    
    # Left: (A U B)^c = A^c \cap B^c
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 7.5)
    ax1.axis('off')
    ax1.set_title(r"Law 1: $(A \cup B)^c = A^c \cap B^c$", fontsize=12, fontweight='bold', pad=10)
    
    # Outer rectangle shaded
    rect1 = patches.Rectangle((0.5, 0.5), 9, 6.5, linewidth=1.5, edgecolor='#1f2937', facecolor='#bae6fd')
    ax1.add_patch(rect1)
    
    # Circles unshaded (white)
    ca1 = patches.Circle((3.8, 3.8), 1.9, linewidth=1.8, edgecolor='#1e40af', facecolor='white')
    cb1 = patches.Circle((6.2, 3.8), 1.9, linewidth=1.8, edgecolor='#1e40af', facecolor='white')
    ax1.add_patch(ca1)
    ax1.add_patch(cb1)
    ax1.text(3.3, 3.8, r'$A$', fontsize=13, fontweight='bold', color='#1e40af')
    ax1.text(6.4, 3.8, r'$B$', fontsize=13, fontweight='bold', color='#1e40af')
    ax1.text(5.0, 1.2, 'Shaded: Neither $A$ nor $B$\n(Outside the union)', fontsize=10, ha='center',
             bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="#93c5fd"))

    # Right: (A \cap B)^c = A^c \cup B^c
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 7.5)
    ax2.axis('off')
    ax2.set_title(r"Law 2: $(A \cap B)^c = A^c \cup B^c$", fontsize=12, fontweight='bold', pad=10)
    
    # Outer rectangle shaded
    rect2 = patches.Rectangle((0.5, 0.5), 9, 6.5, linewidth=1.5, edgecolor='#1f2937', facecolor='#fed7aa')
    ax2.add_patch(rect2)
    
    # Draw circles also shaded
    ca2 = patches.Circle((3.8, 3.8), 1.9, linewidth=1.8, edgecolor='#c2410c', facecolor='#fed7aa')
    cb2 = patches.Circle((6.2, 3.8), 1.9, linewidth=1.8, edgecolor='#c2410c', facecolor='#fed7aa')
    ax2.add_patch(ca2)
    ax2.add_patch(cb2)
    
    # Central intersection left unshaded (white)
    theta = np.linspace(-np.pi/3, np.pi/3, 100)
    x_lens_a = 3.8 + 1.9 * np.cos(theta)
    y_lens_a = 3.8 + 1.9 * np.sin(theta)
    x_lens_b = 6.2 - 1.9 * np.cos(theta)
    y_lens_b = 3.8 + 1.9 * np.sin(theta)
    
    lens_x = np.concatenate([x_lens_b, x_lens_a[::-1]])
    lens_y = np.concatenate([y_lens_b, y_lens_a[::-1]])
    ax2.fill(lens_x, lens_y, facecolor='white', edgecolor='#c2410c', linewidth=1.5)
    
    ax2.text(3.0, 3.8, r'$A$', fontsize=13, fontweight='bold', color='#9a3412')
    ax2.text(6.7, 3.8, r'$B$', fontsize=13, fontweight='bold', color='#9a3412')
    ax2.text(5.0, 3.8, r'$A \cap B$' + '\n(unshaded)', fontsize=9, ha='center', va='center', color='#9a3412')
    ax2.text(5.0, 1.2, 'Shaded: Everything except both $A$ and $B$\n(Complement of intersection)', fontsize=10, ha='center',
             bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="#fdba74"))

    plt.savefig(os.path.join(OUTPUT_DIR, "venn-demorgan.png"), bbox_inches='tight')
    plt.close()

# -------------------------------------------------------------
# 5. Venn Diagram: Axiomatic Inclusion-Exclusion Decomposition
# -------------------------------------------------------------
def create_venn_inclusion_exclusion():
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    rect = patches.Rectangle((0.5, 0.5), 10, 6.5, linewidth=2, edgecolor='#1f2937', facecolor='#f8fafc')
    ax.add_patch(rect)
    ax.text(0.9, 6.5, r'Sample Space $S$', fontsize=13, fontweight='bold', color='#1f2937')

    # Circle A solid fill
    circle_a = patches.Circle((4.3, 3.8), 2.3, linewidth=2, edgecolor='#1d4ed8', facecolor='#93c5fd', alpha=0.85)
    ax.add_patch(circle_a)

    # Circle B dashed
    circle_b = patches.Circle((6.7, 3.8), 2.3, linewidth=2, linestyle='--', edgecolor='#b91c1c', facecolor='none')
    ax.add_patch(circle_b)

    # Shaded moon region: B \cap A^c
    theta = np.linspace(-np.pi, np.pi, 200)
    xb = 6.7 + 2.3 * np.cos(theta)
    yb = 3.8 + 2.3 * np.sin(theta)
    outside_a = ((xb - 4.3)**2 + (yb - 3.8)**2) >= 2.3**2
    ax.fill(xb[outside_a], yb[outside_a], facecolor='#fca5a5', edgecolor='#b91c1c', alpha=0.85)

    ax.text(3.6, 3.8, r'Entire Event $A$', fontsize=12, fontweight='bold', color='#1e3a8a', ha='center')
    ax.text(5.5, 3.8, r'$A \cap B$', fontsize=11, fontweight='bold', color='#1e3a8a', ha='center')
    ax.text(7.8, 3.8, r'Disjoint moon:' + '\n' + r'$B \cap A^c$', fontsize=11, fontweight='bold', color='#991b1b', ha='center')

    # Step annotations
    ax.text(5.5, 1.2, r'Partition of Union: $A \cup B = A \cup (B \cap A^c)$, with $A \cap (B \cap A^c) = \emptyset$' + '\n' +
            r'$\rightarrow P(A \cup B) = P(A) + P(B \cap A^c) = P(A) + [P(B) - P(A \cap B)]$',
            fontsize=10.5, ha='center', va='center', bbox=dict(boxstyle="round,pad=0.35", facecolor="white", edgecolor="#cbd5e1"))

    plt.savefig(os.path.join(OUTPUT_DIR, "venn-inclusion-exclusion.png"), bbox_inches='tight')
    plt.close()

# -------------------------------------------------------------
# 6. Venn Diagram: Three Events & 8-Region System (PAR #36)
# -------------------------------------------------------------
def create_venn_three_events():
    fig, ax = plt.subplots(figsize=(8, 6.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    rect = patches.Rectangle((0.5, 0.5), 11, 9, linewidth=2, edgecolor='#1f2937', facecolor='#f8fafc')
    ax.add_patch(rect)
    ax.text(0.9, 9.0, r'Sample Space $S$ ($\Omega$)', fontsize=13, fontweight='bold', color='#1f2937')

    # 3 circles: A (top-left), B (top-right), C (bottom)
    ca = patches.Circle((4.6, 6.0), 2.7, linewidth=2, edgecolor='#1d4ed8', facecolor='#bfdbfe', alpha=0.45)
    cb = patches.Circle((7.4, 6.0), 2.7, linewidth=2, edgecolor='#b91c1c', facecolor='#fecaca', alpha=0.45)
    cc = patches.Circle((6.0, 3.8), 2.7, linewidth=2, edgecolor='#047857', facecolor='#a7f3d0', alpha=0.45)
    ax.add_patch(ca)
    ax.add_patch(cb)
    ax.add_patch(cc)

    ax.text(2.6, 8.4, r'Event $A$', fontsize=14, fontweight='bold', color='#1d4ed8')
    ax.text(8.4, 8.4, r'Event $B$', fontsize=14, fontweight='bold', color='#b91c1c')
    ax.text(6.0, 0.8, r'Event $C$', fontsize=14, fontweight='bold', color='#047857', ha='center')

    # Region labels use the same letters as PAR Figure 1.5 / Exercise 1.36.
    ax.text(3.5, 6.8, r'$a$' + '\n($A$ only)', fontsize=9.5, ha='center', va='center', fontweight='bold', color='#1e3a8a')
    ax.text(8.5, 6.8, r'$c$' + '\n($B$ only)', fontsize=9.5, ha='center', va='center', fontweight='bold', color='#991b1b')
    ax.text(6.0, 2.5, r'$f$' + '\n($C$ only)', fontsize=9.5, ha='center', va='center', fontweight='bold', color='#065f46')
    ax.text(6.0, 6.9, r'$b$' + '\n($AB$ only)', fontsize=9, ha='center', va='center', fontweight='bold', color='#4c1d95')
    ax.text(4.4, 4.6, r'$d$' + '\n($AC$ only)', fontsize=9, ha='center', va='center', fontweight='bold', color='#0e7490')
    ax.text(7.6, 4.6, r'$e$' + '\n($BC$ only)', fontsize=9, ha='center', va='center', fontweight='bold', color='#b45309')
    ax.text(6.0, 5.2, r'$g$' + '\n($ABC$)', fontsize=9, ha='center', va='center', fontweight='bold', color='#111827')
    ax.text(10.2, 1.3, r'$h = (A \cup B \cup C)^c$' + '\n(none of the three)', fontsize=9.5, ha='center', va='center', fontweight='bold', color='#374151')

    plt.savefig(os.path.join(OUTPUT_DIR, "venn-three-events.png"), bbox_inches='tight')
    plt.close()

# -------------------------------------------------------------
# 7. Discrete Sample Space Grid: Rolling Two Dice (Lecture & PAR 1.3)
# -------------------------------------------------------------
def create_dice_sample_space():
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_xlim(0.5, 6.5)
    ax.set_ylim(0.5, 6.5)
    ax.set_xticks(range(1, 7))
    ax.set_yticks(range(1, 7))
    ax.set_xlabel("First Die ($i$)", fontsize=12, fontweight='bold')
    ax.set_ylabel("Second Die ($j$)", fontsize=12, fontweight='bold')
    ax.set_title(r"Sample Space $S = \{(i,j) \mid 1 \leq i,j \leq 6\}$ ($|S| = 36$ outcomes)", fontsize=12, fontweight='bold', pad=12)
    ax.grid(True, linestyle=':', color='#94a3b8', alpha=0.6)

    # Plot all 36 points and annotate special lecture events
    for i in range(1, 7):
        for j in range(1, 7):
            is_double = (i == j)
            is_sum_8 = (i + j == 8)
            is_ratio_2 = (i == 2*j or j == 2*i)
            
            if is_double and is_sum_8:
                ax.plot(i, j, marker='s', markersize=14, color='#7c3aed', markeredgecolor='black', linewidth=1.5)
                ax.text(i, j, f"({i},{j})", fontsize=7.5, ha='center', va='center', color='white', fontweight='bold')
            elif is_double:
                ax.plot(i, j, marker='o', markersize=13, color='#2563eb', markeredgecolor='black')
                ax.text(i, j, f"({i},{j})", fontsize=7.5, ha='center', va='center', color='white', fontweight='bold')
            elif is_sum_8:
                ax.plot(i, j, marker='D', markersize=13, color='#dc2626', markeredgecolor='black')
                ax.text(i, j, f"({i},{j})", fontsize=7.5, ha='center', va='center', color='white', fontweight='bold')
            elif is_ratio_2:
                ax.plot(i, j, marker='^', markersize=13, color='#059669', markeredgecolor='black')
                ax.text(i, j, f"({i},{j})", fontsize=7.5, ha='center', va='center', color='white', fontweight='bold')
            else:
                ax.plot(i, j, marker='o', markersize=11, color='#e2e8f0', markeredgecolor='#64748b')
                ax.text(i, j, f"({i},{j})", fontsize=7.5, ha='center', va='center', color='#1e293b')

    p_doubles = patches.Patch(color='#2563eb', label=r'Doubles $D: i=j$ ($|D|=6$)')
    p_sum8 = patches.Patch(color='#dc2626', label=r'Sum equals 8 $E: i+j=8$ ($|E|=5$)')
    p_both = patches.Patch(color='#7c3aed', label=r'Both Double & Sum 8: $(4,4)$')
    p_ratio = patches.Patch(color='#059669', label=r'Ratio 2:1 $T: i=2j$ or $j=2i$ ($|T|=6$)')
    ax.legend(handles=[p_doubles, p_sum8, p_both, p_ratio], loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=2, frameon=True)

    plt.savefig(os.path.join(OUTPUT_DIR, "dice-sample-space.png"), bbox_inches='tight')
    plt.close()

def create_movie_survey():
    fig, ax = plt.subplots(figsize=(7, 4.8))
    ax.set_xlim(0, 11); ax.set_ylim(0, 7.5); ax.axis('off')
    ax.add_patch(patches.Rectangle((0.5, 0.5), 10, 6.5, linewidth=2,
                                   edgecolor='#1f2937', facecolor='#f8fafc'))
    ax.add_patch(patches.Circle((4.3, 3.7), 2.2, edgecolor='#1d4ed8',
                                facecolor='#bfdbfe', alpha=.65, linewidth=2))
    ax.add_patch(patches.Circle((6.7, 3.7), 2.2, edgecolor='#b91c1c',
                                facecolor='#fecaca', alpha=.65, linewidth=2))
    ax.text(3.2, 5.8, r'$D$: Odyssey', color='#1d4ed8', weight='bold', ha='center')
    ax.text(7.8, 5.8, r'$M$: Spider-Man', color='#b91c1c', weight='bold', ha='center')
    ax.text(3.1, 3.7, '6\nonly $D$', ha='center', va='center', weight='bold')
    ax.text(5.5, 3.7, '2\nboth', ha='center', va='center', weight='bold')
    ax.text(7.9, 3.7, '7\nonly $M$', ha='center', va='center', weight='bold')
    ax.text(9.2, 1.3, '5\nneither', ha='center', va='center', weight='bold')
    ax.text(.9, 6.4, '20 friends total', weight='bold')
    plt.savefig(os.path.join(OUTPUT_DIR, 'venn-movie-survey.png'), bbox_inches='tight')
    plt.close()

def create_par38():
    fig, ax = plt.subplots(figsize=(7, 4.8))
    ax.set_xlim(0, 11); ax.set_ylim(0, 7.5); ax.axis('off')
    ax.add_patch(patches.Rectangle((0.5, 0.5), 10, 6.5, linewidth=2,
                                   edgecolor='#1f2937', facecolor='#f8fafc'))
    ax.add_patch(patches.Circle((2.8, 3.8), 1.55, edgecolor='#1d4ed8',
                                facecolor='#bfdbfe', alpha=.7, linewidth=2))
    ax.add_patch(patches.Circle((6.6, 4.1), 1.85, edgecolor='#b91c1c',
                                facecolor='#fecaca', alpha=.6, linewidth=2))
    ax.add_patch(patches.Circle((8.0, 3.3), 1.85, edgecolor='#047857',
                                facecolor='#a7f3d0', alpha=.6, linewidth=2))
    ax.text(2.8, 3.8, '$A$\n0.3375', ha='center', va='center', weight='bold')
    ax.text(6.0, 4.5, '$B$ only\n0.225', ha='center', va='center')
    ax.text(8.6, 2.9, '$C$ only\n0.225', ha='center', va='center')
    ax.text(7.3, 3.7, '$B\\cap C$\n0.1125', ha='center', va='center', weight='bold')
    ax.text(9.5, 1.1, 'none = 0.10', ha='center', weight='bold')
    ax.text(.9, 6.4, r'$A$ is disjoint from both $B$ and $C$', weight='bold')
    plt.savefig(os.path.join(OUTPUT_DIR, 'venn-par38.png'), bbox_inches='tight')
    plt.close()

def create_mmsa10():
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    titles = [r'(a) $A_1\cup A_2\cup A_3$', r'(b) $A_1\cap A_2\cap A_3$',
              r"(c) $A_1\cap A_2'\cap A_3'$", '(d) exactly one',
              r'(e) $A_1\cup(A_2\cap A_3)$']
    tests = [lambda a,b,c: a | b | c, lambda a,b,c: a & b & c,
             lambda a,b,c: a & ~b & ~c,
             lambda a,b,c: a.astype(int)+b.astype(int)+c.astype(int)==1,
             lambda a,b,c: a | (b & c)]
    x = np.linspace(0, 10, 420); y = np.linspace(0, 7, 300)
    X, Y = np.meshgrid(x, y)
    masks = [((X-4.0)**2+(Y-4.4)**2 < 2.25**2),
             ((X-6.0)**2+(Y-4.4)**2 < 2.25**2),
             ((X-5.0)**2+(Y-2.7)**2 < 2.25**2)]
    for ax, title, test in zip(axes.flat, titles, tests):
        Z = test(*masks)
        ax.contourf(X, Y, Z.astype(int), levels=[.5, 1.5], colors=['#fbbf24'], alpha=.7)
        for cx,cy,label,color in [(4,4.4,'$A_1$','#1d4ed8'),(6,4.4,'$A_2$','#b91c1c'),(5,2.7,'$A_3$','#047857')]:
            ax.add_patch(patches.Circle((cx,cy),2.25,fill=False,edgecolor=color,linewidth=1.7))
            ax.text(cx + (-1.7 if label=='$A_1$' else 1.7 if label=='$A_2$' else 0),
                    cy + (1.4 if label!='$A_3$' else -1.8), label, color=color, weight='bold')
        ax.set(xlim=(0,10),ylim=(0,7)); ax.axis('off'); ax.set_title(title, fontsize=11)
    axes.flat[-1].axis('off')
    fig.suptitle('MMSA Exercise 10: shaded regions', weight='bold')
    plt.savefig(os.path.join(OUTPUT_DIR, 'venn-mmsa10.png'), bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    print("Generating figures in", OUTPUT_DIR)
    create_venn_complement()
    create_venn_two_events()
    create_venn_disjoint()
    create_venn_demorgan()
    create_venn_inclusion_exclusion()
    create_venn_three_events()
    create_dice_sample_space()
    create_movie_survey()
    create_par38()
    create_mmsa10()
    print("Successfully generated all 10 figures!")
