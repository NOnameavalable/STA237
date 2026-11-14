#!/usr/bin/env python3
"""
Writes Section A to Answers-and-Practice.md.
"""

OUTPUT_PATH = "/Users/stevenli/Documents/University of toronto/STA237/W3/Study-Notes-Markdown/Answers-and-Practice.md"

section_a = """
## Section A: Problem Type Teaching-Example Solutions

### Problem Type PT-01: Direct Conditional Probability Computation and Sample Space Restriction

**Question reference:** [Study-Notes.md: Problem Type PT-01](Study-Notes.md#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction)

**Worked solution.**  
Let the total surveyed population be $N = 400$. We define the relevant events:
- $A$: Student has completed linear algebra ($n(A) = 240$, $P(A) = 240/400 = 0.60$).
- $A^c$: Student has not completed linear algebra ($n(A^c) = 160$, $P(A^c) = 160/400 = 0.40$).
- $L_1$: Student's primary programming language is Python ($n(L_1) = 280$, $P(L_1) = 280/400 = 0.70$).
- $L_2$: Student's primary programming language is R ($n(L_2) = 120$, $P(L_2) = 120/400 = 0.30$).

**(a) Probability student has completed linear algebra given primary language is R ($P(A \\mid L_2)$):**  
The conditioning event is $L_2$. The sample space is restricted from the entire student body ($400$) to the column of R users ($n(L_2) = 120$). Within this restricted sub-population, the count of students who completed linear algebra is $n(A \\cap L_2) = 60$.
$$P(A \\mid L_2) = \\frac{n(A \\cap L_2)}{n(L_2)} = \\frac{60}{120} = \\frac{1}{2} = 0.50$$
Alternatively, via probability definitions:
$$P(A \\mid L_2) = \\frac{P(A \\cap L_2)}{P(L_2)} = \\frac{60/400}{120/400} = \\frac{0.15}{0.30} = 0.50$$

**(b) Probability primary language is Python given no linear algebra ($P(L_1 \\mid A^c)$):**  
The conditioning event is $A^c$. The sample space is restricted to the row of students who have not completed linear algebra ($n(A^c) = 160$). Among these $160$ students, the count who use Python is $n(L_1 \\cap A^c) = 100$.
$$P(L_1 \\mid A^c) = \\frac{n(L_1 \\cap A^c)}{n(A^c)} = \\frac{100}{160} = \\frac{5}{8} = 0.625$$

**(c) Probability a student who completed linear algebra does not use Python ($P(L_1^c \\mid A)$):**  
The conditioning event is $A$ ($n(A) = 240$). We seek $P(L_1^c \\mid A)$. Since the language choice is binary (Python vs. R), $L_1^c = L_2$.
Applying the complement rule within the conditioned space:
$$P(L_1^c \\mid A) = 1 - P(L_1 \\mid A) = 1 - \\frac{n(L_1 \\cap A)}{n(A)} = 1 - \\frac{180}{240} = 1 - \\frac{3}{4} = \\frac{1}{4} = 0.25$$
Direct verification from the table: $n(L_2 \\cap A) / n(A) = 60 / 240 = 0.25$.

**Answer.**  
- (a) $P(A \\mid L_2) = 0.50$ (50.0%).
- (b) $P(L_1 \\mid A^c) = 0.625$ (62.5%).
- (c) $P(L_1^c \\mid A) = 0.25$ (25.0%).

---

### Problem Type PT-02: Multi-Stage Sequential Intersection via the General Multiplication / Chain Rule

**Question reference:** [Study-Notes.md: Problem Type PT-02](Study-Notes.md#problem-type-pt-02-multi-stage-sequential-intersection-via-the-general-multiplication--chain-rule)

**Worked solution.**  
The bin contains $N = 15$ circuits: $4$ defective ($D$) and $11$ non-defective ($G$). Sampling is performed sequentially *without replacement*.

**(a) Probability all 3 circuits are defective ($P(D_1 \\cap D_2 \\cap D_3)$):**  
Applying the Chain Rule:
$$P(D_1 \\cap D_2 \\cap D_3) = P(D_1) \\cdot P(D_2 \\mid D_1) \\cdot P(D_3 \\mid D_1 \\cap D_2)$$
- Draw 1: $15$ circuits remain, $4$ defective $\\implies P(D_1) = \\frac{4}{15}$.
- Draw 2: $14$ circuits remain, $3$ defective $\\implies P(D_2 \\mid D_1) = \\frac{3}{14}$.
- Draw 3: $13$ circuits remain, $2$ defective $\\implies P(D_3 \\mid D_1 \\cap D_2) = \\frac{2}{13}$.
$$P(D_1 \\cap D_2 \\cap D_3) = \\frac{4}{15} \\times \\frac{3}{14} \\times \\frac{2}{13} = \\frac{24}{2730} = \\frac{4}{455} \\approx 0.008791$$

**(b) Probability first two non-defective and third defective ($P(G_1 \\cap G_2 \\cap D_3)$):**  
- Draw 1: $P(G_1) = \\frac{11}{15}$.
- Draw 2: $10$ non-defective remain out of $14$ $\\implies P(G_2 \\mid G_1) = \\frac{10}{14}$.
- Draw 3: $4$ defective remain out of $13$ $\\implies P(D_3 \\mid G_1 \\cap G_2) = \\frac{4}{13}$.
$$P(G_1 \\cap G_2 \\cap D_3) = \\frac{11}{15} \\times \\frac{10}{14} \\times \\frac{4}{13} = \\frac{440}{2730} = \\frac{44}{273} \\approx 0.161172$$

**(c) Probability exactly 1 defective circuit across 3 draws:**  
The event of obtaining exactly 1 defective circuit can occur via three mutually exclusive sequential orderings:
1. Path 1 ($D_1 \\cap G_2 \\cap G_3$): $\\frac{4}{15} \\times \\frac{11}{14} \\times \\frac{10}{13} = \\frac{440}{2730}$.
2. Path 2 ($G_1 \\cap D_2 \\cap G_3$): $\\frac{11}{15} \\times \\frac{4}{14} \\times \\frac{10}{13} = \\frac{440}{2730}$.
3. Path 3 ($G_1 \\cap G_2 \\cap D_3$): $\\frac{11}{15} \\times \\frac{10}{14} \\times \\frac{4}{13} = \\frac{440}{2730}$.

By symmetry of unordered hypergeometric sampling, each ordering has identical probability. Summing the three disjoint paths:
$$P(\\text{Exactly 1 Defective}) = 3 \\times \\frac{440}{2730} = \\frac{1320}{2730} = \\frac{44}{91} \\approx 0.483516$$
*Hypergeometric Verification:*
$$\\frac{\\binom{4}{1} \\binom{11}{2}}{\\binom{15}{3}} = \\frac{4 \\times 55}{455} = \\frac{220}{455} = \\frac{44}{91} \\approx 0.483516$$

**Answer.**  
- (a) $P(\\text{All 3 Defective}) = \\frac{4}{455} \\approx 0.00879$ (0.88%).
- (b) $P(G_1 \\cap G_2 \\cap D_3) = \\frac{44}{273} \\approx 0.16117$ (16.12%).
- (c) $P(\\text{Exactly 1 Defective}) = \\frac{44}{91} \\approx 0.48352$ (48.35%).

---

### Problem Type PT-03: Independence Verification and Independence vs. Disjointness Diagnostics

**Question reference:** [Study-Notes.md: Problem Type PT-03](Study-Notes.md#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics)

**Worked solution.**  
Given:
- $P(M) = 0.20$
- $P(E) = 0.15$
- $P(M \\cup E) = 0.29$

**(a) Are $M$ and $E$ mutually exclusive?**  
Applying the Addition Rule:
$$P(M \\cup E) = P(M) + P(E) - P(M \\cap E)$$
$$0.29 = 0.20 + 0.15 - P(M \\cap E) \\implies P(M \\cap E) = 0.35 - 0.29 = 0.06$$
Since $P(M \\cap E) = 0.06 > 0$, the intersection is non-empty ($M \\cap E \\neq \\emptyset$). Therefore, $M$ and $E$ are **not mutually exclusive**.

**(b) Are $M$ and $E$ statistically independent?**  
Events $M$ and $E$ are independent if and only if $P(M \\cap E) = P(M) \\cdot P(E)$.
- Actual joint probability: $P(M \\cap E) = 0.06$.
- Theoretical product: $P(M) \\cdot P(E) = 0.20 \\times 0.15 = 0.03$.
Since $0.06 \\neq 0.03$, the condition fails. Specifically, $P(M \\cap E) > P(M)P(E)$, indicating that delays on the morning and evening trains are positively correlated. Thus, $M$ and $E$ are **statistically dependent (not independent)**.

**(c) Conditional probability $P(M \\mid E)$ and interpretation:**  
$$P(M \\mid E) = \\frac{P(M \\cap E)}{P(E)} = \\frac{0.06}{0.15} = \\frac{6}{15} = 0.40$$
*Interpretation:* While the baseline unconditional probability of a morning delay is only $P(M) = 0.20$, knowing that the evening train was delayed doubles the probability that the morning train was also delayed to $P(M \\mid E) = 0.40$. Because $P(M \\mid E) \\neq P(M)$, the occurrence of $E$ conveys substantial informational value about $M$, confirming statistical dependence.

**Answer.**  
- (a) Not mutually exclusive ($P(M \\cap E) = 0.06 \\neq 0$).
- (b) Not independent ($P(M \\cap E) = 0.06 \\neq 0.03 = P(M)P(E)$).
- (c) $P(M \\mid E) = 0.40 \\neq P(M) = 0.20$; positive dependency doubles the probability of delay.

---

### Problem Type PT-04: System Reliability and Network Flow Modeling with Independent Components

**Question reference:** [Study-Notes.md: Problem Type PT-04](Study-Notes.md#problem-type-pt-04-system-reliability-and-network-flow-modeling-with-independent-components)

**Worked solution.**  
The network consists of Subsystem $\\alpha$ and Subsystem $\\beta$ in parallel. All components are statistically independent.

**(a) Probability Subsystem $\\alpha$ functions ($P(\\alpha)$):**  
Subsystem $\\alpha$ has transceivers $T_1$ and $T_2$ in parallel, with $p_1 = 0.85$ and $p_2 = 0.80$. Subsystem $\\alpha$ fails if and only if both transceivers fail.
$$P(\\alpha^c) = P(T_1^c \\cap T_2^c) = (1 - p_1)(1 - p_2) = (1 - 0.85)(1 - 0.80) = 0.15 \\times 0.20 = 0.030$$
$$P(\\alpha) = 1 - P(\\alpha^c) = 1 - 0.030 = 0.970$$

**(b) Probability Subsystem $\\beta$ functions ($P(\\beta)$):**  
Subsystem $\\beta$ has processors $C_1$ and $C_2$ in series, each with $p_c = 0.90$. Subsystem $\\beta$ functions if and only if both processors function.
$$P(\\beta) = P(C_1 \\cap C_2) = P(C_1) \\cdot P(C_2) = 0.90 \\times 0.90 = 0.810$$

**(c) Probability data transmission is blocked ($P(\\text{Blocked})$):**  
Because Subsystem $\\alpha$ and Subsystem $\\beta$ form parallel paths across the relay station, data is blocked if and only if **both** Subsystem $\\alpha$ fails and Subsystem $\\beta$ fails:
$$\\text{Blocked} = \\alpha^c \\cap \\beta^c$$
Because the components forming Subsystem $\\alpha$ are distinct from and independent of the components forming Subsystem $\\beta$, the events $\\alpha$ and $\\beta$ are statistically independent.
$$P(\\text{Blocked}) = P(\\alpha^c) \\cdot P(\\beta^c) = (1 - P(\\alpha))(1 - P(\\beta))$$
$$P(\\text{Blocked}) = 0.030 \\times (1 - 0.810) = 0.030 \\times 0.190 = 0.0057$$
*System Reliability:* $P(\\text{Works}) = 1 - 0.0057 = 0.9943$ (99.43%).

**Answer.**  
- (a) $P(\\text{Subsystem } \\alpha \\text{ Works}) = 0.970$ (97.0%).
- (b) $P(\\text{Subsystem } \\beta \\text{ Works}) = 0.810$ (81.0%).
- (c) $P(\\text{Data Blocked}) = 0.0057$ (0.57%).

---

### Problem Type PT-05: Total Probability Computation via Partition Decompositions and Tree Diagrams

**Question reference:** [Study-Notes.md: Problem Type PT-05](Study-Notes.md#problem-type-pt-05-total-probability-computation-via-partition-decompositions-and-tree-diagrams)

**Worked solution.**  
The battery cell suppliers partition the universal inventory $\\Omega$:
- $P(S_1) = 0.50$
- $P(S_2) = 0.30$
- $P(S_3) = 0.20$
Verification: $0.50 + 0.30 + 0.20 = 1.00$.

Let $D$ be the event that a battery cell has internal micro-defects. The conditional defect likelihoods are:
- $P(D \\mid S_1) = 0.015$
- $P(D \\mid S_2) = 0.020$
- $P(D \\mid S_3) = 0.040$

**(a) Unconditional defect probability ($P(D)$):**  
Applying the Law of Total Probability:
$$P(D) = P(D \\mid S_1)P(S_1) + P(D \\mid S_2)P(S_2) + P(D \\mid S_3)P(S_3)$$
$$P(D) = (0.015 \\times 0.50) + (0.020 \\times 0.30) + (0.040 \\times 0.20)$$
$$P(D) = 0.0075 + 0.0060 + 0.0080 = 0.0215$$
Thus, 2.15% of all installed cells have internal micro-defects.

**(b) Probability a cell is defect-free and originated from Supplier $S_2$ ($P(D^c \\cap S_2)$):**  
For Supplier $S_2$, the defect-free conditional probability is:
$$P(D^c \\mid S_2) = 1 - P(D \\mid S_2) = 1 - 0.020 = 0.980$$
Applying the multiplication rule:
$$P(D^c \\cap S_2) = P(D^c \\mid S_2) \\cdot P(S_2) = 0.980 \\times 0.30 = 0.2940$$

**Answer.**  
- (a) $P(D) = 0.0215$ (2.15%).
- (b) $P(D^c \\cap S_2) = 0.2940$ (29.40%).

---

### Problem Type PT-06: First-Step Analysis and Recursive Conditioning

**Question reference:** [Study-Notes.md: Problem Type PT-06](Study-Notes.md#problem-type-pt-06-first-step-analysis-and-recursive-conditioning)

**Worked solution.**  
Let $E$ be the event that an outcome of 6 appears before an outcome of 1. Let $p = P(E)$. Let $X_1 \\in \\{1, 2, 3, 4, 5, 6\\}$ denote the face showing on the very first roll.

**(a) First-step balance equation setup:**  
By the Law of Total Probability, condition on the 6 mutually exclusive outcomes of the first roll:
$$p = \\sum_{k=1}^6 P(E \\mid X_1 = k) \\cdot P(X_1 = k)$$
For a fair die, $P(X_1 = k) = \\frac{1}{6}$ for each $k$.
- If $X_1 = 6$: The target 6 has appeared immediately. Thus, $E$ occurs with certainty: $P(E \\mid X_1 = 6) = 1$.
- If $X_1 = 1$: The rival 1 has appeared immediately. Thus, $E$ can no longer occur: $P(E \\mid X_1 = 1) = 0$.
- If $X_1 \\in \\{2, 3, 4, 5\\}$: Neither 6 nor 1 appeared. The die has no memory, so the experiment completely resets to its initial state: $P(E \\mid X_1 = k) = p$ for $k \\in \\{2, 3, 4, 5\\}$.

Substituting into the LTP formula:
$$p = 1 \\cdot \\left(\\frac{1}{6}\\right) + 0 \\cdot \\left(\\frac{1}{6}\\right) + p \\cdot \\left(\\frac{4}{6}\\right) = \\frac{1}{6} + \\frac{2}{3}p$$

**(b) Solving for $p$:**  
$$p - \\frac{2}{3}p = \\frac{1}{6} \\implies \\frac{1}{3}p = \\frac{1}{6} \\implies p = \\frac{3}{6} = \\frac{1}{2} = 0.50$$
By symmetry, since 6 and 1 have equal probability on each roll, each is equally likely to appear first.

**(c) Biased die calculation:**  
Given $P(X_1 = 6) = 0.25$, $P(X_1 = 1) = 0.15$, and $P(X_1 \\in \\{2, 3, 4, 5\\}) = 4 \\times 0.15 = 0.60$.
The LTP balance equation becomes:
$$p = 1 \\cdot (0.25) + 0 \\cdot (0.15) + p \\cdot (0.60) = 0.25 + 0.60 p$$
$$0.40 p = 0.25 \\implies p = \\frac{0.25}{0.40} = \\frac{5}{8} = 0.625$$

**Answer.**  
- (a) Balance equation: $p = \\frac{1}{6} + \\frac{2}{3}p$.
- (b) Fair die: $P(E) = \\frac{1}{2} = 0.50$.
- (c) Biased die: $P(E) = \\frac{5}{8} = 0.625$.

---

### Problem Type PT-07: Posterior Probability Inversion via Bayes' Rule

**Question reference:** [Study-Notes.md: Problem Type PT-07](Study-Notes.md#problem-type-pt-07-posterior-probability-inversion-via-bayes-rule)

**Worked solution.**  
Let the traffic categories form partition $\\{H_1, H_2, H_3\\}$:
- Prior probabilities: $P(H_1) = 0.70$, $P(H_2) = 0.20$, $P(H_3) = 0.10$.
- Likelihood of anomaly flag $A$: $P(A \\mid H_1) = 0.01$, $P(A \\mid H_2) = 0.03$, $P(A \\mid H_3) = 0.15$.

**(a) Total probability of anomaly flag ($P(A)$):**  
$$P(A) = P(A \\mid H_1)P(H_1) + P(A \\mid H_2)P(H_2) + P(A \\mid H_3)P(H_3)$$
$$P(A) = (0.01 \\times 0.70) + (0.03 \\times 0.20) + (0.15 \\times 0.10)$$
$$P(A) = 0.0070 + 0.0060 + 0.0150 = 0.0280$$
Overall, 2.80% of all packets trigger an anomaly flag.

**(b) Posterior probability of External Query given flag ($P(H_3 \\mid A)$):**  
Applying Bayes' Rule:
$$P(H_3 \\mid A) = \\frac{P(A \\cap H_3)}{P(A)} = \\frac{P(A \\mid H_3)P(H_3)}{P(A)} = \\frac{0.0150}{0.0280} = \\frac{15}{28} \\approx 0.535714$$

**(c) Most likely traffic category responsible:**  
We evaluate the posteriors for the remaining categories:
- Routine ($H_1$): $P(H_1 \\mid A) = \\frac{P(A \\cap H_1)}{P(A)} = \\frac{0.0070}{0.0280} = \\frac{7}{28} = 0.250$ (25.0%).
- Bulk Backup ($H_2$): $P(H_2 \\mid A) = \\frac{P(A \\cap H_2)}{P(A)} = \\frac{0.0060}{0.0280} = \\frac{6}{28} \\approx 0.2143$ (21.43%).
- External Query ($H_3$): $P(H_3 \\mid A) = \\frac{15}{28} \\approx 0.5357$ (53.57%).
Sum check: $7/28 + 6/28 + 15/28 = 28/28 = 1.00$.
Therefore, **External Query ($H_3$)** is the most likely source of a flagged packet, accounting for over 53.5% of all alarms despite representing only 10% of total volume.

**Answer.**  
- (a) $P(A) = 0.0280$ (2.80%).
- (b) $P(H_3 \\mid A) = \\frac{15}{28} \\approx 0.5357$ (53.57%).
- (c) External Query ($H_3$) is most probable ($53.57\\% > 25.0\\% > 21.43\\%$).

---

### Problem Type PT-08: Diagnostic Screening Evaluation and Base-Rate Fallacy Analysis

**Question reference:** [Study-Notes.md: Problem Type PT-08](Study-Notes.md#problem-type-pt-08-diagnostic-screening-evaluation-and-base-rate-fallacy-analysis)

**Worked solution.**  
Let $F$ be the event that a passenger carries fraudulent documents, and $+$ be the event that the scanner raises an alarm.
- Prevalence: $P(F) = 0.002 \\implies P(F^c) = 0.998$.
- Sensitivity: $P(+ \\mid F) = 0.96$.
- Specificity: $P(- \\mid F^c) = 0.98 \\implies \\text{False Positive Rate } P(+ \\mid F^c) = 1 - 0.98 = 0.02$.

**(a) Positive Predictive Value ($P(F \\mid +)$):**  
First, compute the marginal probability of an alarm via LTP:
$$P(+) = P(+ \\mid F)P(F) + P(+ \\mid F^c)P(F^c) = (0.96 \\times 0.002) + (0.02 \\times 0.998)$$
$$P(+) = 0.00192 + 0.01996 = 0.02188$$
By Bayes' Rule:
$$P(F \\mid +) = \\frac{P(+ \\mid F)P(F)}{P(+)} = \\frac{0.00192}{0.02188} = \\frac{192}{2188} = \\frac{48}{547} \\approx 0.087751$$
Thus, there is only an $8.78\\%$ chance that a flagged passenger is truly carrying fraudulent documents!

**(b) False alarm proportion ($P(F^c \\mid +)$):**  
$$P(F^c \\mid +) = 1 - P(F \\mid +) = 1 - \\frac{48}{547} = \\frac{499}{547} \\approx 0.912249 \\quad (91.22\\%)$$
Over $91\\%$ of individuals stopped by the scanner are innocent travelers.

**(c) Specificity required for $P(F \\mid +) \\ge 0.50$:**  
Let $s$ be the specificity, so $P(+ \\mid F^c) = 1 - s$. We set:
$$P(F \\mid +) = \\frac{0.96 \\times 0.002}{(0.96 \\times 0.002) + (1 - s) \\times 0.998} \\ge 0.50$$
$$\\frac{0.00192}{0.00192 + 0.998(1 - s)} \\ge 0.50$$
$$0.00192 \\ge 0.50 [0.00192 + 0.998(1 - s)] = 0.00096 + 0.499(1 - s)$$
$$0.00096 \\ge 0.499(1 - s) \\implies 1 - s \\le \\frac{0.00096}{0.499} = \\frac{96}{49900} \\approx 0.0019238$$
$$s \\ge 1 - 0.0019238 = 0.998076$$
The scanner's specificity must exceed **$99.81\\%$** (false positive rate under $0.19\\%$) to ensure that at least half of flagged passengers are fraudulent.

**Answer.**  
- (a) $P(F \\mid +) = \\frac{48}{547} \\approx 0.0878$ (8.78%).
- (b) False alarms: $91.22\\%$.
- (c) Required specificity: $s \\ge 99.81\\%$.

---

### Problem Type PT-09: Random Variable Definition and Event-to-Variable Mapping

**Question reference:** [Study-Notes.md: Problem Type PT-09](Study-Notes.md#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping)

**Worked solution.**  
**(a) Define $N$ and its support $\\mathcal{N}$:**  
Let $N: \\Omega \\to \\mathbb{R}$ be the random variable representing the total count of failed user connection attempts observed during a 1-minute window. Since the server allows between 0 and 5 failed attempts before lockout:
$$\\mathcal{N} = \\{0, 1, 2, 3, 4, 5\\}$$
The variable is discrete with a finite support of size 6.

**(b) Express events as algebraic inequalities:**  
- $E_1$ ("at least 2"): $\\{N \\ge 2\\}$.
- $E_2$ ("fewer than 4"): $\\{N < 4\\}$, which for integer counts is equivalent to $\\{N \\le 3\\}$.
- $E_3$ ("between 1 and 3 inclusive"): $\\{1 \\le N \\le 3\\}$.

**(c) Description of compound events as sets of support values:**  
- (i) $E_1 \\cap E_2$: Both $N \\ge 2$ and $N \\le 3$ must hold.
  $$\\{N \\ge 2\\} \\cap \\{N \\le 3\\} = \\{2 \\le N \\le 3\\} = \\{2, 3\\}$$
- (ii) $E_1 \\cup E_2$: Either $N \\ge 2$ or $N \\le 3$ holds.
  $$\\{2, 3, 4, 5\\} \\cup \\{0, 1, 2, 3\\} = \\{0, 1, 2, 3, 4, 5\\} = \\mathcal{N}$$
  The union covers the entire support, making $E_1 \\cup E_2$ a certain event ($P(E_1 \\cup E_2) = 1$).
- (iii) $E_1^c$: Complement of $N \\ge 2$.
  $$\\{N \\ge 2\\}^c = \\{N < 2\\} = \\{N \\le 1\\} = \\{0, 1\\}$$

**Answer.**  
- (a) $N = \\text{failed attempts}$; $\\mathcal{N} = \\{0, 1, 2, 3, 4, 5\\}$.
- (b) $E_1 = \\{N \\ge 2\\}$, $E_2 = \\{N \\le 3\\}$, $E_3 = \\{1 \\le N \\le 3\\}$.
- (c) $E_1 \\cap E_2 = \\{2, 3\\}$; $E_1 \\cup E_2 = \\{0, 1, 2, 3, 4, 5\\}$; $E_1^c = \\{0, 1\\}$.

---

### Problem Type PT-10: PMF Normalization, Parameter Determination, and Validation

**Question reference:** [Study-Notes.md: Problem Type PT-10](Study-Notes.md#problem-type-pt-10-pmf-normalization-parameter-determination-and-validation)

**Worked solution.**  
Proposed PMF: $p_X(x) = c(5 - x)^2$ for $x \\in \\{1, 2, 3, 4\\}$.

**(a) Determine constant $c$:**  
Applying the total normalization axiom $\\sum_{x=1}^4 p_X(x) = 1$:
$$c \\sum_{x=1}^4 (5 - x)^2 = 1$$
Compute $(5 - x)^2$ for each support value:
- $x = 1$: $(5 - 1)^2 = 4^2 = 16$
- $x = 2$: $(5 - 2)^2 = 3^2 = 9$
- $x = 3$: $(5 - 3)^2 = 2^2 = 4$
- $x = 4$: $(5 - 4)^2 = 1^2 = 1$
Sum of terms: $16 + 9 + 4 + 1 = 30$.
$$30 c = 1 \\implies c = \\frac{1}{30}$$

**(b) Verification of PMF axioms:**  
- **Axiom 1 (Non-negativity):**
  $p_X(1) = \\frac{16}{30}$, $p_X(2) = \\frac{9}{30}$, $p_X(3) = \\frac{4}{30}$, $p_X(4) = \\frac{1}{30}$.
  Since each probability lies strictly in $[0, 1]$, non-negativity holds.
- **Axiom 2 (Total Sum):**
  $\\sum_{x=1}^4 p_X(x) = \\frac{16 + 9 + 4 + 1}{30} = \\frac{30}{30} = 1.00$.
Both axioms are strictly satisfied.

**(c) Calculate $P(X \\ge 2)$:**  
$$P(X \\ge 2) = p_X(2) + p_X(3) + p_X(4) = \\frac{9}{30} + \\frac{4}{30} + \\frac{1}{30} = \\frac{14}{30} = \\frac{7}{15} \\approx 0.466667$$
Alternatively, via complement: $1 - p_X(1) = 1 - \\frac{16}{30} = \\frac{14}{30}$.

**(d) Calculate $P(X \\text{ is odd} \\mid X \\ge 2)$:**  
The conditioning event is $\\{X \\ge 2\\}$, which has support values $\\{2, 3, 4\\}$ and probability $P(X \\ge 2) = 14/30$.
The intersection $\\{X \\text{ is odd}\\} \\cap \\{X \\ge 2\\}$ contains only the point $x = 3$.
$$P(X \\text{ is odd} \\mid X \\ge 2) = \\frac{P(X = 3)}{P(X \\ge 2)} = \\frac{4/30}{14/30} = \\frac{4}{14} = \\frac{2}{7} \\approx 0.285714$$

**Answer.**  
- (a) $c = \\frac{1}{30}$.
- (b) Validated: $p_X(x) \\ge 0$ for all $x$, and $\\sum p_X(x) = 1$.
- (c) $P(X \\ge 2) = \\frac{7}{15} \\approx 0.4667$.
- (d) $P(X \\text{ is odd} \\mid X \\ge 2) = \\frac{2}{7} \\approx 0.2857$.

---
"""

with open(OUTPUT_PATH, "a", encoding="utf-8") as f:
    f.write(section_a)
print("Section A appended.")
