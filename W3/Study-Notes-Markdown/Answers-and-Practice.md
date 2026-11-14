# STA237 Week 3 Answers and Practice: Worked Solutions, Lecture Exercises, Reference Problems, and Self-Tests

## Contents

- [Section A: Problem Type Teaching-Example Solutions](#section-a-problem-type-teaching-example-solutions)
  - [Problem Type PT-01: Direct Conditional Probability Computation and Sample Space Restriction](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction)
  - [Problem Type PT-02: Multi-Stage Sequential Intersection via the General Multiplication / Chain Rule](#problem-type-pt-02-multi-stage-sequential-intersection-via-the-general-multiplication--chain-rule)
  - [Problem Type PT-03: Independence Verification and Independence vs. Disjointness Diagnostics](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics)
  - [Problem Type PT-04: System Reliability and Network Flow Modeling with Independent Components](#problem-type-pt-04-system-reliability-and-network-flow-modeling-with-independent-components)
  - [Problem Type PT-05: Total Probability Computation via Partition Decompositions and Tree Diagrams](#problem-type-pt-05-total-probability-computation-via-partition-decompositions-and-tree-diagrams)
  - [Problem Type PT-06: First-Step Analysis and Recursive Conditioning](#problem-type-pt-06-first-step-analysis-and-recursive-conditioning)
  - [Problem Type PT-07: Posterior Probability Inversion via Bayes' Rule](#problem-type-pt-07-posterior-probability-inversion-via-bayes-rule)
  - [Problem Type PT-08: Diagnostic Screening Evaluation and Base-Rate Fallacy Analysis](#problem-type-pt-08-diagnostic-screening-evaluation-and-base-rate-fallacy-analysis)
  - [Problem Type PT-09: Random Variable Definition and Event-to-Variable Mapping](#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping)
  - [Problem Type PT-10: PMF Normalization, Parameter Determination, and Validation](#problem-type-pt-10-pmf-normalization-parameter-determination-and-validation)
- [Section B: Source Questions and Solutions (Lecture Deck)](#section-b-source-questions-and-solutions-lecture-deck)
  - [Slide 2: Prerequisite Recap — Digit Permutations with Repetition](#slide-2-prerequisite-recap--digit-permutations-with-repetition)
  - [Slide 7: Example 1 — Colourblindness and Sex Contingency Table](#slide-7-example-1--colourblindness-and-sex-contingency-table)
  - [Slide 8: Example 2 — Consulting Firm Bids (MMSA Ex. 58 Selection)](#slide-8-example-2--consulting-firm-bids-mmsa-ex-58-selection)
  - [Slide 9: Try It Yourself! — Standard Card Deck Conditional Probabilities](#slide-9-try-it-yourself--standard-card-deck-conditional-probabilities)
  - [Slide 13: Check Your Understanding! — Flight Delay Independence](#slide-13-check-your-understanding--flight-delay-independence)
  - [Slide 15: Example 3 — System Reliability via Indirect (Complement) Approach](#slide-15-example-3--system-reliability-via-indirect-complement-approach)
  - [Slide 19: Handedness Translation Question](#slide-19-handedness-translation-question)
  - [Slides 22–24: Example 4 — Sequential Urn Model with Ball Addition](#slides-2224-example-4--sequential-urn-model-with-ball-addition)
  - [Slide 26: Example 5 — Clinical HIV Diagnostic Screening](#slide-26-example-5--clinical-hiv-diagnostic-screening)
  - [Slide 27: Try It! — Express Mail Late Deliveries (MMSA Ex. 125/126)](#slide-27-try-it--express-mail-late-deliveries-mmsa-ex-125126)
  - [Slide 28: Monty Hall Problem — Bayesian Formulation](#slide-28-monty-hall-problem--bayesian-formulation)
  - [Slide 32: Random Variable Definition — Coin Toss Outcome Mappings](#slide-32-random-variable-definition--coin-toss-outcome-mappings)
  - [Slide 35: Example 6 — Quadratic PMF Normalization Constant](#slide-35-example-6--quadratic-pmf-normalization-constant)
- [Section C: Requested Textbook / Reference Exercises and Solutions](#section-c-requested-textbook--reference-exercises-and-solutions)
  - [Subsection C.1: Modern Mathematical Statistics with Applications (MMSA)](#subsection-c1-modern-mathematical-statistics-with-applications-mmsa)
    - [MMSA Basic Exercises](#mmsa-basic-exercises)
      - [Exercise MMSA 2.49 (p. 83)](#exercise-mmsa-249-p-83)
      - [Exercise MMSA 2.50 (p. 83)](#exercise-mmsa-250-p-83)
      - [Exercise MMSA 2.75 (p. 91)](#exercise-mmsa-275-p-91)
      - [Exercise MMSA 3.3 (p. 114)](#exercise-mmsa-33-p-114)
      - [Exercise MMSA 3.6 (p. 114)](#exercise-mmsa-36-p-114)
      - [Exercise MMSA 3.7 (p. 114)](#exercise-mmsa-37-p-114)
      - [Exercise MMSA 3.11 (p. 114)](#exercise-mmsa-311-p-114)
    - [MMSA Medium Exercises](#mmsa-medium-exercises)
      - [Exercise MMSA 2.57 (p. 84)](#exercise-mmsa-257-p-84)
      - [Exercise MMSA 2.58 (p. 84)](#exercise-mmsa-258-p-84)
      - [Exercise MMSA 2.60 (p. 84)](#exercise-mmsa-260-p-84)
      - [Exercise MMSA 2.64 (p. 84)](#exercise-mmsa-264-p-84)
      - [Exercise MMSA 2.79 (p. 92)](#exercise-mmsa-279-p-92)
      - [Exercise MMSA 2.83 (p. 92)](#exercise-mmsa-283-p-92)
    - [MMSA Test Exercises](#mmsa-test-exercises)
      - [Exercise MMSA 2.55 (p. 84)](#exercise-mmsa-255-p-84)
      - [Exercise MMSA 2.67 (p. 84)](#exercise-mmsa-267-p-84)
      - [Exercise MMSA 2.71 (p. 84)](#exercise-mmsa-271-p-84)
      - [Exercise MMSA 2.77 (p. 92)](#exercise-mmsa-277-p-92)
      - [Exercise MMSA 2.88 (p. 92)](#exercise-mmsa-288-p-92)
  - [Subsection C.2: Probability with Applications and R (PAR)](#subsection-c2-probability-with-applications-and-r-par)
    - [PAR Basic Exercises](#par-basic-exercises)
      - [Exercise PAR 2.4 (Ch. 2, p. 84)](#exercise-par-24-ch-2-p-84)
      - [Exercise PAR 2.9 (Ch. 2, p. 84)](#exercise-par-29-ch-2-p-84)
      - [Exercise PAR 2.34 (Ch. 2, p. 84)](#exercise-par-234-ch-2-p-84)
      - [Exercise PAR 3.1 (Ch. 3, p. 118)](#exercise-par-31-ch-3-p-118)
      - [Shared Italicized Instructions for PAR 3.2–3.5](#shared-italicized-instructions-for-par-3235)
      - [Exercise PAR 3.2 (Ch. 3, p. 118)](#exercise-par-32-ch-3-p-118)
      - [Exercise PAR 3.3 (Ch. 3, p. 118)](#exercise-par-33-ch-3-p-118)
      - [Exercise PAR 3.4 (Ch. 3, p. 118)](#exercise-par-34-ch-3-p-118)
      - [Exercise PAR 3.5 (Ch. 3, p. 118)](#exercise-par-35-ch-3-p-118)
      - [Exercise PAR 3.6 (Ch. 3, p. 118)](#exercise-par-36-ch-3-p-118)
      - [Exercise PAR 3.7 (Ch. 3, p. 118)](#exercise-par-37-ch-3-p-118)
    - [PAR Medium Exercises](#par-medium-exercises)
      - [Exercise PAR 2.5 (Ch. 2, p. 84)](#exercise-par-25-ch-2-p-84)
      - [Exercise PAR 2.7 (Ch. 2, p. 84)](#exercise-par-27-ch-2-p-84)
      - [Exercise PAR 2.11 (Ch. 2, p. 84)](#exercise-par-211-ch-2-p-84)
      - [Exercise PAR 2.16 (Ch. 2, p. 84)](#exercise-par-216-ch-2-p-84)
      - [Exercise PAR 2.21 (Ch. 2, p. 84)](#exercise-par-221-ch-2-p-84)
      - [Exercise PAR 2.27 (Ch. 2, p. 84)](#exercise-par-227-ch-2-p-84)
      - [Exercise PAR 2.28 (Ch. 2, p. 84)](#exercise-par-228-ch-2-p-84)
      - [Exercise PAR 2.30 (Ch. 2, p. 84)](#exercise-par-230-ch-2-p-84)
      - [Exercise PAR 2.35 (Ch. 2, p. 84)](#exercise-par-235-ch-2-p-84)
      - [Exercise PAR 2.38 (Ch. 2, p. 84)](#exercise-par-238-ch-2-p-84)
      - [Exercise PAR 2.39 (Ch. 2, p. 84)](#exercise-par-239-ch-2-p-84)
    - [PAR Test Exercises](#par-test-exercises)
      - [Exercise PAR 2.17 (Ch. 2, p. 84)](#exercise-par-217-ch-2-p-84)
      - [Exercise PAR 2.23 (Ch. 2, p. 84)](#exercise-par-223-ch-2-p-84)
      - [Exercise PAR 2.26 (Ch. 2, p. 84)](#exercise-par-226-ch-2-p-84)
      - [Exercise PAR 2.29 (Ch. 2, p. 84)](#exercise-par-229-ch-2-p-84)
      - [Exercise PAR 2.31 (Ch. 2, p. 84)](#exercise-par-231-ch-2-p-84)
      - [Exercise PAR 2.33 (Ch. 2, p. 84)](#exercise-par-233-ch-2-p-84)
      - [Exercise PAR 2.32 (Ch. 2, p. 84)](#exercise-par-232-ch-2-p-84)
      - [Exercise PAR 2.36 (Ch. 2, p. 84)](#exercise-par-236-ch-2-p-84)
- [Section D: Original Self-Test Questions](#section-d-original-self-test-questions)
- [Section E: Self-Test Answers](#section-e-self-test-answers)
- [Section F: Coverage and Unresolved-Items Appendix](#section-f-coverage-and-unresolved-items-appendix)

---

## Section A: Problem Type Teaching-Example Solutions

### Problem Type PT-01: Direct Conditional Probability Computation and Sample Space Restriction

**Question reference:** [Study-Notes.md: Problem Type PT-01](Study-Notes.md#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction)

**Worked solution.**  
Let the total surveyed population be $N = 400$. We define the relevant events:
- $A$: Student has completed linear algebra ($n(A) = 240$, $P(A) = 240/400 = 0.60$).
- $A^c$: Student has not completed linear algebra ($n(A^c) = 160$, $P(A^c) = 160/400 = 0.40$).
- $L_1$: Student's primary programming language is Python ($n(L_1) = 280$, $P(L_1) = 280/400 = 0.70$).
- $L_2$: Student's primary programming language is R ($n(L_2) = 120$, $P(L_2) = 120/400 = 0.30$).

**(a) Probability student has completed linear algebra given primary language is R ($P(A \mid L_2)$):**  
The conditioning event is $L_2$. The sample space is restricted from the entire student body ($400$) to the column of R users ($n(L_2) = 120$). Within this restricted sub-population, the count of students who completed linear algebra is $n(A \cap L_2) = 60$.
$$P(A \mid L_2) = \frac{n(A \cap L_2)}{n(L_2)} = \frac{60}{120} = \frac{1}{2} = 0.50$$
Alternatively, via probability definitions:
$$P(A \mid L_2) = \frac{P(A \cap L_2)}{P(L_2)} = \frac{60/400}{120/400} = \frac{0.15}{0.30} = 0.50$$

**(b) Probability primary language is Python given no linear algebra ($P(L_1 \mid A^c)$):**  
The conditioning event is $A^c$. The sample space is restricted to the row of students who have not completed linear algebra ($n(A^c) = 160$). Among these $160$ students, the count who use Python is $n(L_1 \cap A^c) = 100$.
$$P(L_1 \mid A^c) = \frac{n(L_1 \cap A^c)}{n(A^c)} = \frac{100}{160} = \frac{5}{8} = 0.625$$

**(c) Probability a student who completed linear algebra does not use Python ($P(L_1^c \mid A)$):**  
The conditioning event is $A$ ($n(A) = 240$). We seek $P(L_1^c \mid A)$. Since the language choice is binary (Python vs. R), $L_1^c = L_2$.
Applying the complement rule within the conditioned space:
$$P(L_1^c \mid A) = 1 - P(L_1 \mid A) = 1 - \frac{n(L_1 \cap A)}{n(A)} = 1 - \frac{180}{240} = 1 - \frac{3}{4} = \frac{1}{4} = 0.25$$
Direct verification from the table: $n(L_2 \cap A) / n(A) = 60 / 240 = 0.25$.

**Answer.**  
- (a) $P(A \mid L_2) = 0.50$ (50.0%).
- (b) $P(L_1 \mid A^c) = 0.625$ (62.5%).
- (c) $P(L_1^c \mid A) = 0.25$ (25.0%).

---

### Problem Type PT-02: Multi-Stage Sequential Intersection via the General Multiplication / Chain Rule

**Question reference:** [Study-Notes.md: Problem Type PT-02](Study-Notes.md#problem-type-pt-02-multi-stage-sequential-intersection-via-the-general-multiplication--chain-rule)

**Worked solution.**  
The bin contains $N = 15$ circuits: $4$ defective ($D$) and $11$ non-defective ($G$). Sampling is performed sequentially *without replacement*.

**(a) Probability all 3 circuits are defective ($P(D_1 \cap D_2 \cap D_3)$):**  
Applying the Chain Rule:
$$P(D_1 \cap D_2 \cap D_3) = P(D_1) \cdot P(D_2 \mid D_1) \cdot P(D_3 \mid D_1 \cap D_2)$$
- Draw 1: $15$ circuits remain, $4$ defective $\implies P(D_1) = \frac{4}{15}$.
- Draw 2: $14$ circuits remain, $3$ defective $\implies P(D_2 \mid D_1) = \frac{3}{14}$.
- Draw 3: $13$ circuits remain, $2$ defective $\implies P(D_3 \mid D_1 \cap D_2) = \frac{2}{13}$.
$$P(D_1 \cap D_2 \cap D_3) = \frac{4}{15} \times \frac{3}{14} \times \frac{2}{13} = \frac{24}{2730} = \frac{4}{455} \approx 0.008791$$

**(b) Probability first two non-defective and third defective ($P(G_1 \cap G_2 \cap D_3)$):**  
- Draw 1: $P(G_1) = \frac{11}{15}$.
- Draw 2: $10$ non-defective remain out of $14$ $\implies P(G_2 \mid G_1) = \frac{10}{14}$.
- Draw 3: $4$ defective remain out of $13$ $\implies P(D_3 \mid G_1 \cap G_2) = \frac{4}{13}$.
$$P(G_1 \cap G_2 \cap D_3) = \frac{11}{15} \times \frac{10}{14} \times \frac{4}{13} = \frac{440}{2730} = \frac{44}{273} \approx 0.161172$$

**(c) Probability exactly 1 defective circuit across 3 draws:**  
The event of obtaining exactly 1 defective circuit can occur via three mutually exclusive sequential orderings:
1. Path 1 ($D_1 \cap G_2 \cap G_3$): $\frac{4}{15} \times \frac{11}{14} \times \frac{10}{13} = \frac{440}{2730}$.
2. Path 2 ($G_1 \cap D_2 \cap G_3$): $\frac{11}{15} \times \frac{4}{14} \times \frac{10}{13} = \frac{440}{2730}$.
3. Path 3 ($G_1 \cap G_2 \cap D_3$): $\frac{11}{15} \times \frac{10}{14} \times \frac{4}{13} = \frac{440}{2730}$.

By symmetry of unordered hypergeometric sampling, each ordering has identical probability. Summing the three disjoint paths:
$$P(\text{Exactly 1 Defective}) = 3 \times \frac{440}{2730} = \frac{1320}{2730} = \frac{44}{91} \approx 0.483516$$
*Hypergeometric Verification:*
$$\frac{\binom{4}{1} \binom{11}{2}}{\binom{15}{3}} = \frac{4 \times 55}{455} = \frac{220}{455} = \frac{44}{91} \approx 0.483516$$

**Answer.**  
- (a) $P(\text{All 3 Defective}) = \frac{4}{455} \approx 0.00879$ (0.88%).
- (b) $P(G_1 \cap G_2 \cap D_3) = \frac{44}{273} \approx 0.16117$ (16.12%).
- (c) $P(\text{Exactly 1 Defective}) = \frac{44}{91} \approx 0.48352$ (48.35%).

---

### Problem Type PT-03: Independence Verification and Independence vs. Disjointness Diagnostics

**Question reference:** [Study-Notes.md: Problem Type PT-03](Study-Notes.md#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics)

**Worked solution.**  
Given:
- $P(M) = 0.20$
- $P(E) = 0.15$
- $P(M \cup E) = 0.29$

**(a) Are $M$ and $E$ mutually exclusive?**  
Applying the Addition Rule:
$$P(M \cup E) = P(M) + P(E) - P(M \cap E)$$
$$0.29 = 0.20 + 0.15 - P(M \cap E) \implies P(M \cap E) = 0.35 - 0.29 = 0.06$$
Since $P(M \cap E) = 0.06 > 0$, the intersection is non-empty ($M \cap E \neq \emptyset$). Therefore, $M$ and $E$ are **not mutually exclusive**.

**(b) Are $M$ and $E$ statistically independent?**  
Events $M$ and $E$ are independent if and only if $P(M \cap E) = P(M) \cdot P(E)$.
- Actual joint probability: $P(M \cap E) = 0.06$.
- Theoretical product: $P(M) \cdot P(E) = 0.20 \times 0.15 = 0.03$.
Since $0.06 \neq 0.03$, the condition fails. Specifically, $P(M \cap E) > P(M)P(E)$, indicating that delays on the morning and evening trains are positively correlated. Thus, $M$ and $E$ are **statistically dependent (not independent)**.

**(c) Conditional probability $P(M \mid E)$ and interpretation:**  
$$P(M \mid E) = \frac{P(M \cap E)}{P(E)} = \frac{0.06}{0.15} = \frac{6}{15} = 0.40$$
*Interpretation:* While the baseline unconditional probability of a morning delay is only $P(M) = 0.20$, knowing that the evening train was delayed doubles the probability that the morning train was also delayed to $P(M \mid E) = 0.40$. Because $P(M \mid E) \neq P(M)$, the occurrence of $E$ conveys substantial informational value about $M$, confirming statistical dependence.

**Answer.**  
- (a) Not mutually exclusive ($P(M \cap E) = 0.06 \neq 0$).
- (b) Not independent ($P(M \cap E) = 0.06 \neq 0.03 = P(M)P(E)$).
- (c) $P(M \mid E) = 0.40 \neq P(M) = 0.20$; positive dependency doubles the probability of delay.

---

### Problem Type PT-04: System Reliability and Network Flow Modeling with Independent Components

**Question reference:** [Study-Notes.md: Problem Type PT-04](Study-Notes.md#problem-type-pt-04-system-reliability-and-network-flow-modeling-with-independent-components)

**Worked solution.**  
The network consists of Subsystem $\alpha$ and Subsystem $\beta$ in parallel. All components are statistically independent.

**(a) Probability Subsystem $\alpha$ functions ($P(\alpha)$):**  
Subsystem $\alpha$ has transceivers $T_1$ and $T_2$ in parallel, with $p_1 = 0.85$ and $p_2 = 0.80$. Subsystem $\alpha$ fails if and only if both transceivers fail.
$$P(\alpha^c) = P(T_1^c \cap T_2^c) = (1 - p_1)(1 - p_2) = (1 - 0.85)(1 - 0.80) = 0.15 \times 0.20 = 0.030$$
$$P(\alpha) = 1 - P(\alpha^c) = 1 - 0.030 = 0.970$$

**(b) Probability Subsystem $\beta$ functions ($P(\beta)$):**  
Subsystem $\beta$ has processors $C_1$ and $C_2$ in series, each with $p_c = 0.90$. Subsystem $\beta$ functions if and only if both processors function.
$$P(\beta) = P(C_1 \cap C_2) = P(C_1) \cdot P(C_2) = 0.90 \times 0.90 = 0.810$$

**(c) Probability data transmission is blocked ($P(\text{Blocked})$):**  
Because Subsystem $\alpha$ and Subsystem $\beta$ form parallel paths across the relay station, data is blocked if and only if **both** Subsystem $\alpha$ fails and Subsystem $\beta$ fails:
$$\text{Blocked} = \alpha^c \cap \beta^c$$
Because the components forming Subsystem $\alpha$ are distinct from and independent of the components forming Subsystem $\beta$, the events $\alpha$ and $\beta$ are statistically independent.
$$P(\text{Blocked}) = P(\alpha^c) \cdot P(\beta^c) = (1 - P(\alpha))(1 - P(\beta))$$
$$P(\text{Blocked}) = 0.030 \times (1 - 0.810) = 0.030 \times 0.190 = 0.0057$$
*System Reliability:* $P(\text{Works}) = 1 - 0.0057 = 0.9943$ (99.43%).

**Answer.**  
- (a) $P(\text{Subsystem } \alpha \text{ Works}) = 0.970$ (97.0%).
- (b) $P(\text{Subsystem } \beta \text{ Works}) = 0.810$ (81.0%).
- (c) $P(\text{Data Blocked}) = 0.0057$ (0.57%).

---

### Problem Type PT-05: Total Probability Computation via Partition Decompositions and Tree Diagrams

**Question reference:** [Study-Notes.md: Problem Type PT-05](Study-Notes.md#problem-type-pt-05-total-probability-computation-via-partition-decompositions-and-tree-diagrams)

**Worked solution.**  
The battery cell suppliers partition the universal inventory $\Omega$:
- $P(S_1) = 0.50$
- $P(S_2) = 0.30$
- $P(S_3) = 0.20$
Verification: $0.50 + 0.30 + 0.20 = 1.00$.

Let $D$ be the event that a battery cell has internal micro-defects. The conditional defect likelihoods are:
- $P(D \mid S_1) = 0.015$
- $P(D \mid S_2) = 0.020$
- $P(D \mid S_3) = 0.040$

**(a) Unconditional defect probability ($P(D)$):**  
Applying the Law of Total Probability:
$$P(D) = P(D \mid S_1)P(S_1) + P(D \mid S_2)P(S_2) + P(D \mid S_3)P(S_3)$$
$$P(D) = (0.015 \times 0.50) + (0.020 \times 0.30) + (0.040 \times 0.20)$$
$$P(D) = 0.0075 + 0.0060 + 0.0080 = 0.0215$$
Thus, 2.15% of all installed cells have internal micro-defects.

**(b) Probability a cell is defect-free and originated from Supplier $S_2$ ($P(D^c \cap S_2)$):**  
For Supplier $S_2$, the defect-free conditional probability is:
$$P(D^c \mid S_2) = 1 - P(D \mid S_2) = 1 - 0.020 = 0.980$$
Applying the multiplication rule:
$$P(D^c \cap S_2) = P(D^c \mid S_2) \cdot P(S_2) = 0.980 \times 0.30 = 0.2940$$

**Answer.**  
- (a) $P(D) = 0.0215$ (2.15%).
- (b) $P(D^c \cap S_2) = 0.2940$ (29.40%).

---

### Problem Type PT-06: First-Step Analysis and Recursive Conditioning

**Question reference:** [Study-Notes.md: Problem Type PT-06](Study-Notes.md#problem-type-pt-06-first-step-analysis-and-recursive-conditioning)

**Worked solution.**  
Let $E$ be the event that an outcome of 6 appears before an outcome of 1. Let $p = P(E)$. Let $X_1 \in \{1, 2, 3, 4, 5, 6\}$ denote the face showing on the very first roll.

**(a) First-step balance equation setup:**  
By the Law of Total Probability, condition on the 6 mutually exclusive outcomes of the first roll:
$$p = \sum_{k=1}^6 P(E \mid X_1 = k) \cdot P(X_1 = k)$$
For a fair die, $P(X_1 = k) = \frac{1}{6}$ for each $k$.
- If $X_1 = 6$: The target 6 has appeared immediately. Thus, $E$ occurs with certainty: $P(E \mid X_1 = 6) = 1$.
- If $X_1 = 1$: The rival 1 has appeared immediately. Thus, $E$ can no longer occur: $P(E \mid X_1 = 1) = 0$.
- If $X_1 \in \{2, 3, 4, 5\}$: Neither 6 nor 1 appeared. The die has no memory, so the experiment completely resets to its initial state: $P(E \mid X_1 = k) = p$ for $k \in \{2, 3, 4, 5\}$.

Substituting into the LTP formula:
$$p = 1 \cdot \left(\frac{1}{6}\right) + 0 \cdot \left(\frac{1}{6}\right) + p \cdot \left(\frac{4}{6}\right) = \frac{1}{6} + \frac{2}{3}p$$

**(b) Solving for $p$:**  
$$p - \frac{2}{3}p = \frac{1}{6} \implies \frac{1}{3}p = \frac{1}{6} \implies p = \frac{3}{6} = \frac{1}{2} = 0.50$$
By symmetry, since 6 and 1 have equal probability on each roll, each is equally likely to appear first.

**(c) Biased die calculation:**  
Given $P(X_1 = 6) = 0.25$, $P(X_1 = 1) = 0.15$, and $P(X_1 \in \{2, 3, 4, 5\}) = 4 \times 0.15 = 0.60$.
The LTP balance equation becomes:
$$p = 1 \cdot (0.25) + 0 \cdot (0.15) + p \cdot (0.60) = 0.25 + 0.60 p$$
$$0.40 p = 0.25 \implies p = \frac{0.25}{0.40} = \frac{5}{8} = 0.625$$

**Answer.**  
- (a) Balance equation: $p = \frac{1}{6} + \frac{2}{3}p$.
- (b) Fair die: $P(E) = \frac{1}{2} = 0.50$.
- (c) Biased die: $P(E) = \frac{5}{8} = 0.625$.

---

### Problem Type PT-07: Posterior Probability Inversion via Bayes' Rule

**Question reference:** [Study-Notes.md: Problem Type PT-07](Study-Notes.md#problem-type-pt-07-posterior-probability-inversion-via-bayes-rule)

**Worked solution.**  
Let the traffic categories form partition $\{H_1, H_2, H_3\}$:
- Prior probabilities: $P(H_1) = 0.70$, $P(H_2) = 0.20$, $P(H_3) = 0.10$.
- Likelihood of anomaly flag $A$: $P(A \mid H_1) = 0.01$, $P(A \mid H_2) = 0.03$, $P(A \mid H_3) = 0.15$.

**(a) Total probability of anomaly flag ($P(A)$):**  
$$P(A) = P(A \mid H_1)P(H_1) + P(A \mid H_2)P(H_2) + P(A \mid H_3)P(H_3)$$
$$P(A) = (0.01 \times 0.70) + (0.03 \times 0.20) + (0.15 \times 0.10)$$
$$P(A) = 0.0070 + 0.0060 + 0.0150 = 0.0280$$
Overall, 2.80% of all packets trigger an anomaly flag.

**(b) Posterior probability of External Query given flag ($P(H_3 \mid A)$):**  
Applying Bayes' Rule:
$$P(H_3 \mid A) = \frac{P(A \cap H_3)}{P(A)} = \frac{P(A \mid H_3)P(H_3)}{P(A)} = \frac{0.0150}{0.0280} = \frac{15}{28} \approx 0.535714$$

**(c) Most likely traffic category responsible:**  
We evaluate the posteriors for the remaining categories:
- Routine ($H_1$): $P(H_1 \mid A) = \frac{P(A \cap H_1)}{P(A)} = \frac{0.0070}{0.0280} = \frac{7}{28} = 0.250$ (25.0%).
- Bulk Backup ($H_2$): $P(H_2 \mid A) = \frac{P(A \cap H_2)}{P(A)} = \frac{0.0060}{0.0280} = \frac{6}{28} \approx 0.2143$ (21.43%).
- External Query ($H_3$): $P(H_3 \mid A) = \frac{15}{28} \approx 0.5357$ (53.57%).
Sum check: $7/28 + 6/28 + 15/28 = 28/28 = 1.00$.
Therefore, **External Query ($H_3$)** is the most likely source of a flagged packet, accounting for over 53.5% of all alarms despite representing only 10% of total volume.

**Answer.**  
- (a) $P(A) = 0.0280$ (2.80%).
- (b) $P(H_3 \mid A) = \frac{15}{28} \approx 0.5357$ (53.57%).
- (c) External Query ($H_3$) is most probable ($53.57\% > 25.0\% > 21.43\%$).

---

### Problem Type PT-08: Diagnostic Screening Evaluation and Base-Rate Fallacy Analysis

**Question reference:** [Study-Notes.md: Problem Type PT-08](Study-Notes.md#problem-type-pt-08-diagnostic-screening-evaluation-and-base-rate-fallacy-analysis)

**Worked solution.**  
Let $F$ be the event that a passenger carries fraudulent documents, and $+$ be the event that the scanner raises an alarm.
- Prevalence: $P(F) = 0.002 \implies P(F^c) = 0.998$.
- Sensitivity: $P(+ \mid F) = 0.96$.
- Specificity: $P(- \mid F^c) = 0.98 \implies \text{False Positive Rate } P(+ \mid F^c) = 1 - 0.98 = 0.02$.

**(a) Positive Predictive Value ($P(F \mid +)$):**  
First, compute the marginal probability of an alarm via LTP:
$$P(+) = P(+ \mid F)P(F) + P(+ \mid F^c)P(F^c) = (0.96 \times 0.002) + (0.02 \times 0.998)$$
$$P(+) = 0.00192 + 0.01996 = 0.02188$$
By Bayes' Rule:
$$P(F \mid +) = \frac{P(+ \mid F)P(F)}{P(+)} = \frac{0.00192}{0.02188} = \frac{192}{2188} = \frac{48}{547} \approx 0.087751$$
Thus, there is only an $8.78\%$ chance that a flagged passenger is truly carrying fraudulent documents!

**(b) False alarm proportion ($P(F^c \mid +)$):**  
$$P(F^c \mid +) = 1 - P(F \mid +) = 1 - \frac{48}{547} = \frac{499}{547} \approx 0.912249 \quad (91.22\%)$$
Over $91\%$ of individuals stopped by the scanner are innocent travelers.

**(c) Specificity required for $P(F \mid +) \ge 0.50$:**  
Let $s$ be the specificity, so $P(+ \mid F^c) = 1 - s$. We set:
$$P(F \mid +) = \frac{0.96 \times 0.002}{(0.96 \times 0.002) + (1 - s) \times 0.998} \ge 0.50$$
$$\frac{0.00192}{0.00192 + 0.998(1 - s)} \ge 0.50$$
$$0.00192 \ge 0.50 [0.00192 + 0.998(1 - s)] = 0.00096 + 0.499(1 - s)$$
$$0.00096 \ge 0.499(1 - s) \implies 1 - s \le \frac{0.00096}{0.499} = \frac{96}{49900} \approx 0.0019238$$
$$s \ge 1 - 0.0019238 = 0.998076$$
The scanner's specificity must exceed **$99.81\%$** (false positive rate under $0.19\%$) to ensure that at least half of flagged passengers are fraudulent.

**Answer.**  
- (a) $P(F \mid +) = \frac{48}{547} \approx 0.0878$ (8.78%).
- (b) False alarms: $91.22\%$.
- (c) Required specificity: $s \ge 99.81\%$.

---

### Problem Type PT-09: Random Variable Definition and Event-to-Variable Mapping

**Question reference:** [Study-Notes.md: Problem Type PT-09](Study-Notes.md#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping)

**Worked solution.**  
**(a) Define $N$ and its support $\mathcal{N}$:**  
Let $N: \Omega \to \mathbb{R}$ be the random variable representing the total count of failed user connection attempts observed during a 1-minute window. Since the server allows between 0 and 5 failed attempts before lockout:
$$\mathcal{N} = \{0, 1, 2, 3, 4, 5\}$$
The variable is discrete with a finite support of size 6.

**(b) Express events as algebraic inequalities:**  
- $E_1$ ("at least 2"): $\{N \ge 2\}$.
- $E_2$ ("fewer than 4"): $\{N < 4\}$, which for integer counts is equivalent to $\{N \le 3\}$.
- $E_3$ ("between 1 and 3 inclusive"): $\{1 \le N \le 3\}$.

**(c) Description of compound events as sets of support values:**  
- (i) $E_1 \cap E_2$: Both $N \ge 2$ and $N \le 3$ must hold.
  $$\{N \ge 2\} \cap \{N \le 3\} = \{2 \le N \le 3\} = \{2, 3\}$$
- (ii) $E_1 \cup E_2$: Either $N \ge 2$ or $N \le 3$ holds.
  $$\{2, 3, 4, 5\} \cup \{0, 1, 2, 3\} = \{0, 1, 2, 3, 4, 5\} = \mathcal{N}$$
  The union covers the entire support, making $E_1 \cup E_2$ a certain event ($P(E_1 \cup E_2) = 1$).
- (iii) $E_1^c$: Complement of $N \ge 2$.
  $$\{N \ge 2\}^c = \{N < 2\} = \{N \le 1\} = \{0, 1\}$$

**Answer.**  
- (a) $N = \text{failed attempts}$; $\mathcal{N} = \{0, 1, 2, 3, 4, 5\}$.
- (b) $E_1 = \{N \ge 2\}$, $E_2 = \{N \le 3\}$, $E_3 = \{1 \le N \le 3\}$.
- (c) $E_1 \cap E_2 = \{2, 3\}$; $E_1 \cup E_2 = \{0, 1, 2, 3, 4, 5\}$; $E_1^c = \{0, 1\}$.

---

### Problem Type PT-10: PMF Normalization, Parameter Determination, and Validation

**Question reference:** [Study-Notes.md: Problem Type PT-10](Study-Notes.md#problem-type-pt-10-pmf-normalization-parameter-determination-and-validation)

**Worked solution.**  
Proposed PMF: $p_X(x) = c(5 - x)^2$ for $x \in \{1, 2, 3, 4\}$.

**(a) Determine constant $c$:**  
Applying the total normalization axiom $\sum_{x=1}^4 p_X(x) = 1$:
$$c \sum_{x=1}^4 (5 - x)^2 = 1$$
Compute $(5 - x)^2$ for each support value:
- $x = 1$: $(5 - 1)^2 = 4^2 = 16$
- $x = 2$: $(5 - 2)^2 = 3^2 = 9$
- $x = 3$: $(5 - 3)^2 = 2^2 = 4$
- $x = 4$: $(5 - 4)^2 = 1^2 = 1$
Sum of terms: $16 + 9 + 4 + 1 = 30$.
$$30 c = 1 \implies c = \frac{1}{30}$$

**(b) Verification of PMF axioms:**  
- **Axiom 1 (Non-negativity):**
  $p_X(1) = \frac{16}{30}$, $p_X(2) = \frac{9}{30}$, $p_X(3) = \frac{4}{30}$, $p_X(4) = \frac{1}{30}$.
  Since each probability lies strictly in $[0, 1]$, non-negativity holds.
- **Axiom 2 (Total Sum):**
  $\sum_{x=1}^4 p_X(x) = \frac{16 + 9 + 4 + 1}{30} = \frac{30}{30} = 1.00$.
Both axioms are strictly satisfied.

**(c) Calculate $P(X \ge 2)$:**  
$$P(X \ge 2) = p_X(2) + p_X(3) + p_X(4) = \frac{9}{30} + \frac{4}{30} + \frac{1}{30} = \frac{14}{30} = \frac{7}{15} \approx 0.466667$$
Alternatively, via complement: $1 - p_X(1) = 1 - \frac{16}{30} = \frac{14}{30}$.

**(d) Calculate $P(X \text{ is odd} \mid X \ge 2)$:**  
The conditioning event is $\{X \ge 2\}$, which has support values $\{2, 3, 4\}$ and probability $P(X \ge 2) = 14/30$.
The intersection $\{X \text{ is odd}\} \cap \{X \ge 2\}$ contains only the point $x = 3$.
$$P(X \text{ is odd} \mid X \ge 2) = \frac{P(X = 3)}{P(X \ge 2)} = \frac{4/30}{14/30} = \frac{4}{14} = \frac{2}{7} \approx 0.285714$$

**Answer.**  
- (a) $c = \frac{1}{30}$.
- (b) Validated: $p_X(x) \ge 0$ for all $x$, and $\sum p_X(x) = 1$.
- (c) $P(X \ge 2) = \frac{7}{15} \approx 0.4667$.
- (d) $P(X \text{ is odd} \mid X \ge 2) = \frac{2}{7} \approx 0.2857$.

---

## Section B: Source Questions and Solutions (Lecture Deck)

### Slide 2: Prerequisite Recap — Digit Permutations with Repetition

**Source identification:** `W3/Week 3.pdf`, Slide 2 ("From Last Week: Try for yourself!").  
**Relevant PT ID(s):** Prerequisite Counting / Combinatorial Foundations.

**Complete question statement.**  
How many 7-digit natural numbers can be formed using each of the following digits once: $1, 2, 3, 3, 4, 4, 4$ if:
- (a) There are no conditions on the number?
- (b) The number is smaller than 4,000,000?
- (c) The number is smaller than 4,000,000 and is even?

**Complete working.**  
The multiset of 7 digits consists of:
- One 1 ($n_1 = 1$)
- One 2 ($n_2 = 1$)
- Two 3s ($n_3 = 2$)
- Three 4s ($n_4 = 3$)
Total digits: $n = 1 + 1 + 2 + 3 = 7$.

**(a) No conditions:**  
The total number of distinct 7-digit numbers is given by the formula for permutations of indistinguishable objects:
$$N = \frac{n!}{n_1! \, n_2! \, n_3! \, n_4!} = \frac{7!}{1! \, 1! \, 2! \, 3!} = \frac{5040}{1 \times 1 \times 2 \times 6} = \frac{5040}{12} = 420$$

**(b) The number is smaller than 4,000,000:**  
A 7-digit number is strictly less than 4,000,000 if and only if its leading (millions) digit is strictly less than 4. The available choices for the first digit are $1, 2,$ or $3$. We partition into three mutually exclusive cases based on the first digit:
- **Case 1 (First digit is 1):** Remaining digits to permute are $\{2, 3, 3, 4, 4, 4\}$ (counts: one 2, two 3s, three 4s).
  $$N_1 = \frac{6!}{1! \, 2! \, 3!} = \frac{720}{12} = 60$$
- **Case 2 (First digit is 2):** Remaining digits to permute are $\{1, 3, 3, 4, 4, 4\}$ (counts: one 1, two 3s, three 4s).
  $$N_2 = \frac{6!}{1! \, 2! \, 3!} = \frac{720}{12} = 60$$
- **Case 3 (First digit is 3):** Remaining digits to permute are $\{1, 2, 3, 4, 4, 4\}$ (counts: one 1, one 2, one 3, three 4s).
  $$N_3 = \frac{6!}{1! \, 1! \, 1! \, 3!} = \frac{720}{6} = 120$$

Summing the cases:
$$N_{<4M} = N_1 + N_2 + N_3 = 60 + 60 + 120 = 240$$
*Complement Verification:* The only alternative is that the leading digit is 4. Remaining digits $\{1, 2, 3, 3, 4, 4\}$ have counts (one 1, one 2, two 3s, two 4s), yielding $\frac{6!}{1! 1! 2! 2!} = \frac{720}{4} = 180$. Total $= 420 - 180 = 240$. Matches.

**(c) The number is smaller than 4,000,000 AND is even:**  
To be even, the last digit must be an even digit from the multiset: either $2$ or $4$. Simultaneously, to be smaller than 4,000,000, the first digit must be $1, 2,$ or $3$. We partition by the ending digit:
- **Subcase C1 (Last digit is 2):**  
  Digit 2 is fixed in position 7. The remaining digits for positions 1–6 are $\{1, 3, 3, 4, 4, 4\}$.  
  The first digit can be 1 or 3 (it cannot be 2 since only one 2 exists):
  - *First digit = 1:* Remaining digits for positions 2–6 are $\{3, 3, 4, 4, 4\}$.
    $$N_{C1, 1} = \frac{5!}{2! \, 3!} = \frac{120}{12} = 10$$
  - *First digit = 3:* Remaining digits for positions 2–6 are $\{1, 3, 4, 4, 4\}$.
    $$N_{C1, 3} = \frac{5!}{1! \, 1! \, 3!} = \frac{120}{6} = 20$$
  Subtotal for ending in 2: $10 + 20 = 30$.

- **Subcase C2 (Last digit is 4):**  
  One 4 is fixed in position 7. The remaining digits for positions 1–6 are $\{1, 2, 3, 3, 4, 4\}$.  
  The first digit can be 1, 2, or 3:
  - *First digit = 1:* Remaining digits for positions 2–6 are $\{2, 3, 3, 4, 4\}$.
    $$N_{C2, 1} = \frac{5!}{1! \, 2! \, 2!} = \frac{120}{4} = 30$$
  - *First digit = 2:* Remaining digits for positions 2–6 are $\{1, 3, 3, 4, 4\}$.
    $$N_{C2, 2} = \frac{5!}{1! \, 2! \, 2!} = \frac{120}{4} = 30$$
  - *First digit = 3:* Remaining digits for positions 2–6 are $\{1, 2, 3, 4, 4\}$.
    $$N_{C2, 3} = \frac{5!}{1! \, 1! \, 1! \, 2!} = \frac{120}{2} = 60$$
  Subtotal for ending in 4: $30 + 30 + 60 = 120$.

Total even numbers smaller than 4,000,000:
$$N = 30 + 120 = 150$$

**Answer.**  
- (a) $420$ numbers.
- (b) $240$ numbers.
- (c) $150$ numbers.

---

### Slide 7: Example 1 — Colourblindness and Sex Contingency Table

**Source identification:** `W3/Week 3.pdf`, Slide 7 ("Example 1 - Contingency Table").  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
Below is a contingency table containing counts from a fictional study on colourblindness and sex involving 2500 randomly selected adults. Let $C$ denote the event that a surveyed individual is colourblind, and $M$ denote the event that a surveyed individual is male ($M^c$ denotes female).

| Sex | Colourblind ($C$) | Not Colourblind ($C^c$) | Row Total |
| :--- | :---: | :---: | :---: |
| Male ($M$) | 106 | 1175 | 1281 |
| Female ($M^c$) | 7 | 1212 | 1219 |
| **Column Total** | **113** | **2387** | **2500** |

Based on the data:
- (a) What would you estimate to be the probability that an individual is male and colourblind?
- (b) What is the estimated probability that a male individual is colourblind? That a female individual is colourblind?

**Complete working.**  
Total sample size $N = 2500$.

**(a) Probability that an individual is male and colourblind ($P(M \cap C)$):**  
This is the joint probability evaluated over the entire population:
$$P(M \cap C) = \frac{n(M \cap C)}{N} = \frac{106}{2500} = 0.0424 \quad (4.24\%)$$

**(b) Conditional probabilities $P(C \mid M)$ and $P(C \mid M^c)$:**  
- **For a male individual ($P(C \mid M)$):**  
  Restricting the sample space to the male row ($n(M) = 1281$):
  $$P(C \mid M) = \frac{n(M \cap C)}{n(M)} = \frac{106}{1281} \approx 0.082748 \quad (8.27\%)$$
- **For a female individual ($P(C \mid M^c)$):**  
  Restricting the sample space to the female row ($n(M^c) = 1219$):
  $$P(C \mid M^c) = \frac{n(M^c \cap C)}{n(M^c)} = \frac{7}{1219} \approx 0.005742 \quad (0.57\%)$$

*Interpretation:* In this sample, males are approximately $14.4$ times more likely to be colourblind than females ($8.27\%$ vs. $0.57\%$), illustrating how conditional conditioning reveals sex-linked genetic traits that are obscured in the overall marginal rate $P(C) = 113/2500 = 4.52\%$.

**Answer.**  
- (a) $P(M \cap C) = 0.0424$ (4.24%).
- (b) $P(C \mid M) \approx 0.0827$ (8.27%); $P(C \mid M^c) \approx 0.0057$ (0.57%).

---

### Slide 8: Example 2 — Consulting Firm Bids (MMSA Ex. 58 Selection)

**Source identification:** `W3/Week 3.pdf`, Slide 8 ("Example 2 - MMSA Ex. 58").  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
A consulting firm presently has bids out on three projects. Let $A_i = \{\text{Awarded project } i\}$ for $i = 1, 2, 3$, and suppose that:
- $P(A_1) = 0.22$, $P(A_2) = 0.25$, $P(A_3) = 0.28$
- $P(A_1 \cap A_2) = 0.11$, $P(A_1 \cap A_3) = 0.05$, $P(A_2 \cap A_3) = 0.07$
- $P(A_1 \cap A_2 \cap A_3) = 0.01$

Compute the following probabilities and explain in words the meaning of each event:
- (a) $P(A_2 \mid A_1)$
- (b) $P(A_2 \cap A_3 \mid A_1)$ *(from MMSA Ex. 58)*
- (c) $P(A_2 \cup A_3 \mid A_1)$
- (d) $P(A_1 \cap A_2 \cap A_3 \mid A_1 \cup A_2 \cup A_3)$ *(from MMSA Ex. 58)*

**Complete working.**  
**(a) $P(A_2 \mid A_1)$:**  
$$P(A_2 \mid A_1) = \frac{P(A_1 \cap A_2)}{P(A_1)} = \frac{0.11}{0.22} = 0.50$$
*Meaning:* Given that the firm is awarded Project 1, the probability that it is also awarded Project 2 is $0.50$ (50%).

**(b) $P(A_2 \cap A_3 \mid A_1)$:**  
$$P(A_2 \cap A_3 \mid A_1) = \frac{P(A_1 \cap (A_2 \cap A_3))}{P(A_1)} = \frac{P(A_1 \cap A_2 \cap A_3)}{P(A_1)} = \frac{0.01}{0.22} = \frac{1}{22} \approx 0.045455$$
*Meaning:* Given that the firm is awarded Project 1, the probability that it is awarded both Project 2 and Project 3 (all three projects) is $1/22 \approx 4.55\%$.

**(c) $P(A_2 \cup A_3 \mid A_1)$:**  
By the distributive law of sets:
$$(A_2 \cup A_3) \cap A_1 = (A_1 \cap A_2) \cup (A_1 \cap A_3)$$
By the addition rule for probabilities:
$$P((A_2 \cup A_3) \cap A_1) = P(A_1 \cap A_2) + P(A_1 \cap A_3) - P((A_1 \cap A_2) \cap (A_1 \cap A_3))$$
$$= P(A_1 \cap A_2) + P(A_1 \cap A_3) - P(A_1 \cap A_2 \cap A_3) = 0.11 + 0.05 - 0.01 = 0.15$$
Applying conditional probability:
$$P(A_2 \cup A_3 \mid A_1) = \frac{0.15}{P(A_1)} = \frac{0.15}{0.22} = \frac{15}{22} \approx 0.681818$$
*Meaning:* Given that Project 1 is awarded, the probability that the firm is awarded at least one of Project 2 or Project 3 is $15/22 \approx 68.18\%$.

**(d) $P(A_1 \cap A_2 \cap A_3 \mid A_1 \cup A_2 \cup A_3)$:**  
First, compute the probability of the union $P(A_1 \cup A_2 \cup A_3)$ by the Principle of Inclusion-Exclusion:
$$P(A_1 \cup A_2 \cup A_3) = [P(A_1) + P(A_2) + P(A_3)] - [P(A_1 \cap A_2) + P(A_1 \cap A_3) + P(A_2 \cap A_3)] + P(A_1 \cap A_2 \cap A_3)$$
$$= [0.22 + 0.25 + 0.28] - [0.11 + 0.05 + 0.07] + 0.01 = 0.75 - 0.23 + 0.01 = 0.53$$
Because the intersection $(A_1 \cap A_2 \cap A_3)$ is a subset of the union $(A_1 \cup A_2 \cup A_3)$, their intersection is simply the three-way intersection itself.
$$P(A_1 \cap A_2 \cap A_3 \mid A_1 \cup A_2 \cup A_3) = \frac{P(A_1 \cap A_2 \cap A_3)}{P(A_1 \cup A_2 \cup A_3)} = \frac{0.01}{0.53} = \frac{1}{53} \approx 0.018868$$
*Meaning:* Given that the firm is awarded at least one project, the probability that it is awarded all three projects is $1/53 \approx 1.89\%$.

**Answer.**  
- (a) $P(A_2 \mid A_1) = 0.50$.
- (b) $P(A_2 \cap A_3 \mid A_1) = \frac{1}{22} \approx 0.0455$.
- (c) $P(A_2 \cup A_3 \mid A_1) = \frac{15}{22} \approx 0.6818$.
- (d) $P(A_1 \cap A_2 \cap A_3 \mid A_1 \cup A_2 \cup A_3) = \frac{1}{53} \approx 0.0189$.

---

### Slide 9: Try It Yourself! — Standard Card Deck Conditional Probabilities

**Source identification:** `W3/Week 3.pdf`, Slide 9 ("Try it yourself!").  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
You pick a card at random from a standard 52-card deck (13 ranks, 4 suits: diamonds $\diamondsuit$, hearts $\heartsuit$, clubs $\clubsuit$, spades $\spadesuit$). Let $Q$ denote the event of drawing a Queen of Hearts, and $R$ denote the event of drawing a red card. Describe each event below and find its probability:
- (a) $P(Q \mid R)$
- (b) $P(R \mid Q)$
- (c) $P(Q^c \mid R)$

**Complete working.**  
The sample space $\Omega$ contains 52 equally likely outcomes.
- Event $Q$ = $\{\text{Queen of Hearts}\}$ $\implies |Q| = 1$, $P(Q) = 1/52$.
- Event $R$ = $\{\text{all hearts and diamonds}\}$ $\implies |R| = 26$, $P(R) = 26/52 = 1/2$.
- Note that the Queen of Hearts is a heart (red card), so $Q \subseteq R$. Consequently, $Q \cap R = Q$, and $P(Q \cap R) = P(Q) = 1/52$.

**(a) $P(Q \mid R)$:**  
*Description:* The probability of drawing the Queen of Hearts given that the drawn card is red.
$$P(Q \mid R) = \frac{P(Q \cap R)}{P(R)} = \frac{1/52}{26/52} = \frac{1}{26} \approx 0.038462$$

**(b) $P(R \mid Q)$:**  
*Description:* The probability that the card is red given that it is the Queen of Hearts.
$$P(R \mid Q) = \frac{P(R \cap Q)}{P(Q)} = \frac{1/52}{1/52} = 1.00$$
Since every Queen of Hearts is guaranteed to be a red card, the condition establishes certainty.

**(c) $P(Q^c \mid R)$:**  
*Description:* The probability that the card is *not* the Queen of Hearts given that it is a red card.  
By the complement rule on the conditioned space:
$$P(Q^c \mid R) = 1 - P(Q \mid R) = 1 - \frac{1}{26} = \frac{25}{26} \approx 0.961538$$
Alternatively, among the 26 red cards, exactly 25 are not the Queen of Hearts: $25/26$.

**Answer.**  
- (a) $P(Q \mid R) = \frac{1}{26} \approx 0.0385$.
- (b) $P(R \mid Q) = 1.00$ (certain).
- (c) $P(Q^c \mid R) = \frac{25}{26} \approx 0.9615$.

---

### Slide 13: Check Your Understanding! — Flight Delay Independence

**Source identification:** `W3/Week 3.pdf`, Slide 13 ("Check your understanding!").  
**Relevant PT ID(s):** [PT-03](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics).

**Complete question statement.**  
Consider two events:
- $A = \{\text{Arriving flight is delayed by at least 15 minutes}\}$ with $P(A) = 0.20$.
- $D = \{\text{Departing flight is delayed by at least 15 minutes}\}$ with $P(D) = 0.25$.
- $P(A \cap D) = 0.16$.

Determine numerically whether events $A$ and $D$ are independent. Explain using conditional probabilities whether they are independent.

**Complete working.**  
- **Numerical Test via Product Rule:**  
  Two events are independent if and only if $P(A \cap D) = P(A) \cdot P(D)$.
  - Observed joint probability: $P(A \cap D) = 0.16$.
  - Product of marginals: $P(A) \cdot P(D) = 0.20 \times 0.25 = 0.05$.
  Since $0.16 \neq 0.05$, events $A$ and $D$ are **not statistically independent (they are dependent)**.

- **Explanation via Conditional Probabilities:**  
  Compute the conditional probability of an arrival delay given a departure delay:
  $$P(A \mid D) = \frac{P(A \cap D)}{P(D)} = \frac{0.16}{0.25} = 0.64$$
  Compare this to the baseline unconditional probability:
  $$P(A) = 0.20$$
  Since $P(A \mid D) = 0.64 > 0.20 = P(A)$, knowing that the departing flight is delayed dramatically increases the probability of an arrival delay (more than tripling it). Symmetrically:
  $$P(D \mid A) = \frac{P(A \cap D)}{P(A)} = \frac{0.16}{0.20} = 0.80 > 0.25 = P(D)$$
  Because the occurrence of one event significantly alters the probability of the other, they are strongly dependent.

**Answer.**  
$A$ and $D$ are **not independent** because $P(A \cap D) = 0.16 \neq 0.05 = P(A)P(D)$. In conditional terms, $P(A \mid D) = 0.64 \neq P(A) = 0.20$.

---

### Slide 15: Example 3 — System Reliability via Indirect (Complement) Approach

**Source identification:** `W3/Week 3.pdf`, Slide 15 ("Example 3 - Indirect Approach").  
**Relevant PT ID(s):** [PT-04](#problem-type-pt-04-system-reliability-and-network-flow-modeling-with-independent-components).

**Complete question statement.**  
The system below is comprised of independent components. The probability that each numbered component will work is $0.90, 0.95,$ and $0.99$, respectively. An electrical signal will travel from left to right if there is a path of functioning components. Component 1 and Component 2 are connected in parallel; this parallel block is connected in series with Component 3. Find the probability that the signal is blocked.

**Complete working.**  
Let $C_1, C_2, C_3$ be the events that Components 1, 2, and 3 work, with:
- $P(C_1) = 0.90 \implies P(C_1^c) = 0.10$
- $P(C_2) = 0.95 \implies P(C_2^c) = 0.05$
- $P(C_3) = 0.99 \implies P(C_3^c) = 0.01$

- **Step 1: Operational probability of the parallel block ($C_1 \cup C_2$):**  
  The parallel block fails if and only if both components fail. Since components operate independently:
  $$P(\text{Parallel Fails}) = P(C_1^c \cap C_2^c) = P(C_1^c) \cdot P(C_2^c) = 0.10 \times 0.05 = 0.005$$
  $$P(\text{Parallel Works}) = 1 - P(C_1^c \cap C_2^c) = 1 - 0.005 = 0.995$$

- **Step 2: Operational probability of the overall system:**  
  The system functions if and only if the parallel block works **and** Component 3 works:
  $$\text{System Works} = (C_1 \cup C_2) \cap C_3$$
  Because Component 3 is independent of Components 1 and 2:
  $$P(\text{System Works}) = P(C_1 \cup C_2) \cdot P(C_3) = 0.995 \times 0.99 = 0.98505$$

- **Step 3: Indirect evaluation of signal blockage:**  
  The signal is blocked if and only if the system fails to transmit:
  $$P(\text{Signal Blocked}) = 1 - P(\text{System Works}) = 1 - 0.98505 = 0.01495$$

*Direct Cut-Set Verification:*  
A signal is blocked if Component 3 fails ($C_3^c$) OR both parallel components fail ($C_1^c \cap C_2^c$):
$$P(\text{Blocked}) = P(C_3^c \cup (C_1^c \cap C_2^c)) = P(C_3^c) + P(C_1^c \cap C_2^c) - P(C_3^c \cap C_1^c \cap C_2^c)$$
$$= 0.01 + 0.005 - (0.01 \times 0.005) = 0.015 - 0.00005 = 0.01495$$
The direct and indirect approaches agree exactly.

**Answer.**  
$P(\text{Signal is Blocked}) = 0.01495$ (1.495%).

---

### Slide 19: Handedness Translation Question

**Source identification:** `W3/Week 3.pdf`, Slide 19 ("Law of Total Probability" introductory translation).  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction), [PT-02](#problem-type-pt-02-multi-stage-sequential-intersection-via-the-general-multiplication--chain-rule).

**Complete question statement.**  
In a group of 100 people, 40 write left-handed. Half of left-handed people are also left-handed in sports. How many people are left-handed in both writing and sports?

**Complete working.**  
Let the population size be $N = 100$.
- Let $W$ be the event that a person writes left-handed. $n(W) = 40 \implies P(W) = 40/100 = 0.40$.
- Let $S$ be the event that a person is left-handed in sports.
- The phrase *"Half of left-handed people also left-handed in sports"* defines the conditional probability:
  $$P(S \mid W) = 0.50$$
Applying the multiplication rule for conditional probability:
$$P(W \cap S) = P(S \mid W) \cdot P(W) = 0.50 \times 0.40 = 0.20$$
The number of people who are left-handed in both writing and sports is:
$$n(W \cap S) = N \times P(W \cap S) = 100 \times 0.20 = 20 \text{ people}$$
Equivalently: $n(W \cap S) = 0.50 \times n(W) = 0.50 \times 40 = 20$.

**Answer.**  
$20$ people are left-handed in both writing and sports.

---

### Slides 22–24: Example 4 — Sequential Urn Model with Ball Addition

**Source identification:** `W3/Week 3.pdf`, Slides 22–24 ("Example 4" and "Example 4 - Continued").  
**Relevant PT ID(s):** [PT-02](#problem-type-pt-02-multi-stage-sequential-intersection-via-the-general-multiplication--chain-rule), [PT-05](#problem-type-pt-05-total-probability-computation-via-partition-decompositions-and-tree-diagrams), [PT-07](#problem-type-pt-07-posterior-probability-inversion-via-bayes-rule).

**Complete question statement.**  
A ball is drawn at random from an urn containing one red and one white ball. If the white ball is drawn, it is put back in the urn. If the red ball is drawn, it is returned to the urn together with two more red balls. Then a second draw is made. Let $R_i$ be the event that the $i$-th ball drawn is red.
- (a) What is the probability a red ball was drawn on both the first and second draws?
- (b) What is the probability that the second ball drawn is red?
- (c) What is the probability the first ball drawn was red given that the second ball is red?

**Complete working.**  
Initial composition: 1 Red ($R$), 1 White ($W$). Total $= 2$ balls.
First draw:
- Draw White ($W_1$): probability $P(W_1) = 1/2$. The white ball is replaced. Urn composition for draw 2 remains 1 Red, 1 White (total 2).
- Draw Red ($R_1$): probability $P(R_1) = 1/2$. The red ball is returned along with 2 extra red balls. Urn composition for draw 2 becomes $1 + 2 = 3$ Red, 1 White (total 4).

**(a) Probability red ball drawn on both draws ($P(R_1 \cap R_2)$):**  
Applying the multiplication rule:
$$P(R_1 \cap R_2) = P(R_2 \mid R_1) \cdot P(R_1)$$
Given $R_1$, the urn contains 3 red balls out of 4 total $\implies P(R_2 \mid R_1) = 3/4$.
$$P(R_1 \cap R_2) = \frac{3}{4} \times \frac{1}{2} = \frac{3}{8} = 0.375$$

**(b) Probability that the second ball drawn is red ($P(R_2)$):**  
The outcomes of the first draw $\{R_1, W_1\}$ partition the sample space. By the Law of Total Probability:
$$P(R_2) = P(R_2 \mid R_1)P(R_1) + P(R_2 \mid W_1)P(W_1)$$
Given $W_1$, the urn contains 1 red ball out of 2 total $\implies P(R_2 \mid W_1) = 1/2$.
$$P(R_2) = \left(\frac{3}{4} \times \frac{1}{2}\right) + \left(\frac{1}{2} \times \frac{1}{2}\right) = \frac{3}{8} + \frac{1}{4} = \frac{3}{8} + \frac{2}{8} = \frac{5}{8} = 0.625$$

**(c) Probability the first ball was red given the second ball is red ($P(R_1 \mid R_2)$):**  
Applying Bayes' Rule:
$$P(R_1 \mid R_2) = \frac{P(R_1 \cap R_2)}{P(R_2)} = \frac{3/8}{5/8} = \frac{3}{5} = 0.60$$

**Answer.**  
- (a) $P(R_1 \cap R_2) = \frac{3}{8} = 0.375$.
- (b) $P(R_2) = \frac{5}{8} = 0.625$.
- (c) $P(R_1 \mid R_2) = \frac{3}{5} = 0.60$.

---

### Slide 26: Example 5 — Clinical HIV Diagnostic Screening

**Source identification:** `W3/Week 3.pdf`, Slide 26 ("Example 5").  
**Relevant PT ID(s):** [PT-08](#problem-type-pt-08-diagnostic-screening-evaluation-and-base-rate-fallacy-analysis).

**Complete question statement.**  
Consider the context of disease testing (specifically, HIV testing).
- An HIV test will correctly test positive 95% of the time (test sensitivity).
- The test also incorrectly tests positive 1% of the time (false positive rate).
- Based on recent data, 98% of the population is HIV-free.
Under these conditions, how likely is it that a positive HIV test is from an individual with HIV?

**Complete working.**  
Define events:
- $D$: Individual has HIV.
- $D^c$: Individual is HIV-free.
- $+$: Test result is positive.

From the problem statement:
- Prevalence: $P(D^c) = 0.98 \implies P(D) = 1 - 0.98 = 0.02$ (2% baseline infection rate).
- Sensitivity: $P(+ \mid D) = 0.95$.
- False positive rate: $P(+ \mid D^c) = 0.01$.

We seek the Positive Predictive Value $P(D \mid +)$.
- **Step 1: Total probability of testing positive ($P(+)$):**  
  Applying the Law of Total Probability:
  $$P(+) = P(+ \mid D)P(D) + P(+ \mid D^c)P(D^c)$$
  $$P(+) = (0.95 \times 0.02) + (0.01 \times 0.98) = 0.0190 + 0.0098 = 0.0288$$

- **Step 2: Inverting via Bayes' Rule:**  
  $$P(D \mid +) = \frac{P(+ \mid D)P(D)}{P(+)} = \frac{0.0190}{0.0288} = \frac{190}{288} = \frac{95}{144} \approx 0.659722$$

*Clinical Interpretation:* Even with a 95% sensitive test and a very low 1% false positive rate, approximately $34\%$ of positive tests are false alarms. This occurs because the healthy population ($98\%$) is 49 times larger than the infected population ($2\%$), generating a substantial volume of false positives.

**Answer.**  
$P(D \mid +) = \frac{95}{144} \approx 0.6597$ (65.97%).

---

### Slide 27: Try It! — Express Mail Late Deliveries (MMSA Ex. 125/126)

**Source identification:** `W3/Week 3.pdf`, Slide 27 ("Try it! MMSA Ex. 125/126").  
**Relevant PT ID(s):** [PT-05](#problem-type-pt-05-total-probability-computation-via-partition-decompositions-and-tree-diagrams), [PT-07](#problem-type-pt-07-posterior-probability-inversion-via-bayes-rule).

**Complete question statement.**  
A certain company sends 40% of its overnight mail parcels via express mail service $E_1$. Of these parcels, 2% arrive after the guaranteed delivery time (denoted by $L$ for event of late delivery). 50% are sent via express mail service $E_2$ and the remaining 10% are sent via $E_3$. Of those sent via $E_2$, only 1% arrive late, whereas 5% of the parcels sent by $E_3$ arrive late.
- (a) What is the probability that a randomly selected parcel arrived late?
- (b) If a randomly selected parcel has arrived late, what is the probability it was sent by $E_1$?

**Complete working.**  
The delivery services partition the overnight shipments:
- $P(E_1) = 0.40$, $P(E_2) = 0.50$, $P(E_3) = 0.10$. (Sum $= 1.00$).
The conditional late probabilities are:
- $P(L \mid E_1) = 0.02$
- $P(L \mid E_2) = 0.01$
- $P(L \mid E_3) = 0.05$

**(a) Overall probability parcel arrived late ($P(L)$):**  
Applying the Law of Total Probability:
$$P(L) = P(L \mid E_1)P(E_1) + P(L \mid E_2)P(E_2) + P(L \mid E_3)P(E_3)$$
$$P(L) = (0.02 \times 0.40) + (0.01 \times 0.50) + (0.05 \times 0.10)$$
$$P(L) = 0.0080 + 0.0050 + 0.0050 = 0.0180$$
Overall, 1.80% of overnight parcels arrive late.

**(b) Probability parcel was sent by $E_1$ given it arrived late ($P(E_1 \mid L)$):**  
Applying Bayes' Rule:
$$P(E_1 \mid L) = \frac{P(L \mid E_1)P(E_1)}{P(L)} = \frac{0.0080}{0.0180} = \frac{8}{18} = \frac{4}{9} \approx 0.444444$$

**Answer.**  
- (a) $P(L) = 0.0180$ (1.80%).
- (b) $P(E_1 \mid L) = \frac{4}{9} \approx 0.4444$ (44.44%).

---

### Slide 28: Monty Hall Problem — Bayesian Formulation

**Source identification:** `W3/Week 3.pdf`, Slide 28 ("Monty Hall Problem").  
**Relevant PT ID(s):** [PT-07](#problem-type-pt-07-posterior-probability-inversion-via-bayes-rule).

**Complete question statement.**  
In the classic Monty Hall game show setup, a contestant faces three closed doors: behind one door is a car, and behind the other two are goats. The contestant initially chooses Door 1. Host Monty Hall, who knows the location of the car, opens one of the remaining doors (say, Door 3) to reveal a goat. Monty then offers the contestant the option to switch to Door 2. Using Bayes' Rule, determine whether the contestant should switch.

**Complete working.**  
Let $C_i$ be the event that the car is behind Door $i$ for $i \in \{1, 2, 3\}$.
- Prior distribution: $P(C_1) = P(C_2) = P(C_3) = \frac{1}{3}$.

Assume without loss of generality that the contestant picks Door 1. Let $M_3$ be the event that Monty Hall opens Door 3. Monty operates under the strict rules:
1. Monty never opens Door 1 (the contestant's choice).
2. Monty never opens the door hiding the car.
3. If Monty has a choice between two goat doors (which happens when the car is behind Door 1), he chooses either door with equal probability $1/2$.

The conditional likelihoods of Monty opening Door 3 are:
- If car is behind Door 1 ($C_1$): Monty chooses between Door 2 and Door 3 at random $\implies P(M_3 \mid C_1) = 1/2$.
- If car is behind Door 2 ($C_2$): Door 1 is picked by contestant, Door 2 has car; Monty is forced to open Door 3 $\implies P(M_3 \mid C_2) = 1$.
- If car is behind Door 3 ($C_3$): Monty cannot reveal the car $\implies P(M_3 \mid C_3) = 0$.

Applying the Law of Total Probability to find $P(M_3)$:
$$P(M_3) = P(M_3 \mid C_1)P(C_1) + P(M_3 \mid C_2)P(C_2) + P(M_3 \mid C_3)P(C_3)$$
$$P(M_3) = \left(\frac{1}{2} \times \frac{1}{3}\right) + \left(1 \times \frac{1}{3}\right) + \left(0 \times \frac{1}{3}\right) = \frac{1}{6} + \frac{1}{3} = \frac{1}{2}$$

Now apply Bayes' Rule to compare staying (Door 1) versus switching (Door 2):
- **Posterior probability for staying with Door 1:**
  $$P(C_1 \mid M_3) = \frac{P(M_3 \mid C_1)P(C_1)}{P(M_3)} = \frac{1/6}{1/2} = \frac{1}{3}$$
- **Posterior probability for switching to Door 2:**
  $$P(C_2 \mid M_3) = \frac{P(M_3 \mid C_2)P(C_2)}{P(M_3)} = \frac{1/3}{1/2} = \frac{2}{3}$$

*Conclusion:* Switching doors doubles the contestant's probability of winning the car from $1/3$ to $2/3$.

**Answer.**  
The contestant should **switch**, as $P(\text{Win} \mid \text{Switch}) = \frac{2}{3}$, whereas $P(\text{Win} \mid \text{Stay}) = \frac{1}{3}$.

---

### Slide 32: Random Variable Definition — Coin Toss Outcome Mappings

**Source identification:** `W3/Week 3.pdf`, Slide 32 ("Random Variable").  
**Relevant PT ID(s):** [PT-09](#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping).

**Complete question statement.**  
Fill in the formal definitions and mappings for the qualitative coin tossing sample spaces presented in lecture:
- (a) For a single coin toss with $\Omega = \{H, T\}$, define a standard indicator random variable $X$ and state its mapping.
- (b) For an experiment consisting of 3 coin tosses with $\Omega = \{HHH, HHT, HTH, THH, HTT, THT, TTH, TTT\}$, define the random variable $X$ representing the number of heads that landed, list its value for each elementary outcome $\omega \in \Omega$, and state its support $\mathcal{X}$.

**Complete working.**  
**(a) Single Coin Toss:**  
The sample space is $\Omega = \{H, T\}$. The standard numerical indicator variable $X: \Omega \to \mathbb{R}$ is defined by:
$$X(\omega) = \begin{cases} 1 & \text{if } \omega = H \\ 0 & \text{if } \omega = T \end{cases}$$
Support: $\mathcal{X} = \{0, 1\}$. (This is the canonical Bernoulli random variable).

**(b) Three Coin Tosses:**  
Let $X: \Omega \to \mathbb{R}$ denote the number of heads obtained in the 3 tosses.
Evaluating $X(\omega)$ for each of the 8 outcomes:
- $X(TTT) = 0$
- $X(HTT) = X(THT) = X(TTH) = 1$
- $X(HHT) = X(HTH) = X(THH) = 2$
- $X(HHH) = 3$

The support of $X$ is:
$$\mathcal{X} = \{0, 1, 2, 3\}$$
Pre-image event cardinalities and probabilities (assuming fair coins):
- $\{X = 0\} = \{TTT\} \implies P(X = 0) = 1/8$
- $\{X = 1\} = \{HTT, THT, TTH\} \implies P(X = 1) = 3/8$
- $\{X = 2\} = \{HHT, HTH, THH\} \implies P(X = 2) = 3/8$
- $\{X = 3\} = \{HHH\} \implies P(X = 3) = 1/8$

**Answer.**  
- (a) $X(H) = 1, X(T) = 0$; $\mathcal{X} = \{0, 1\}$.
- (b) $X \in \{0, 1, 2, 3\}$; mapping counts heads per sequence; probabilities are $1/8, 3/8, 3/8, 1/8$.

---

### Slide 35: Example 6 — Quadratic PMF Normalization Constant

**Source identification:** `W3/Week 3.pdf`, Slide 35 ("Example 6").  
**Relevant PT ID(s):** [PT-10](#problem-type-pt-10-pmf-normalization-parameter-determination-and-validation).

**Complete question statement.**  
Determine the value of $k$ such that:
$$P(X = x) = \frac{k x^2 - x + 2}{4}$$
will be a valid probability mass function for the discrete support $\mathcal{X} = \{0, 1, 2, 3, 4\}$.

**Complete working.**  
A valid PMF must satisfy two axioms:
1. Normalization: $\sum_{x \in \mathcal{X}} P(X = x) = 1$.
2. Non-negativity: $P(X = x) \ge 0$ for all $x \in \mathcal{X}$.

- **Step 1: Normalization Summation:**  
  $$\sum_{x=0}^4 \frac{k x^2 - x + 2}{4} = 1 \implies \sum_{x=0}^4 (k x^2 - x + 2) = 4$$
  Expand the sum term by term for $x = 0, 1, 2, 3, 4$:
  - $x = 0$: $k(0)^2 - 0 + 2 = 2$
  - $x = 1$: $k(1)^2 - 1 + 2 = k + 1$
  - $x = 2$: $k(2)^2 - 2 + 2 = 4k$
  - $x = 3$: $k(3)^2 - 3 + 2 = 9k - 1$
  - $x = 4$: $k(4)^2 - 4 + 2 = 16k - 2$

  Summing these five expressions:
  $$\sum_{x=0}^4 (k x^2 - x + 2) = (k + 4k + 9k + 16k) + (2 + 1 + 0 - 1 - 2) = 30k + 0 = 30k$$
  Set the sum equal to 4:
  $$30k = 4 \implies k = \frac{4}{30} = \frac{2}{15} \approx 0.133333$$

- **Step 2: Non-Negativity Verification (Axiom 1):**  
  Substitute $k = \frac{2}{15}$ back into the numerator $g(x) = \frac{2}{15}x^2 - x + 2$ for each $x$:
  - For $x = 0$: $P(X = 0) = \frac{2}{4} = \frac{1}{2} = \frac{30}{60} > 0$
  - For $x = 1$: $P(X = 1) = \frac{2/15 + 1}{4} = \frac{17/15}{4} = \frac{17}{60} > 0$
  - For $x = 2$: $P(X = 2) = \frac{4(2/15)}{4} = \frac{2}{15} = \frac{8}{60} > 0$
  - For $x = 3$: $P(X = 3) = \frac{9(2/15) - 1}{4} = \frac{18/15 - 1}{4} = \frac{3/15}{4} = \frac{1}{20} = \frac{3}{60} > 0$
  - For $x = 4$: $P(X = 4) = \frac{16(2/15) - 2}{4} = \frac{32/15 - 30/15}{4} = \frac{2/15}{4} = \frac{2}{60} = \frac{1}{30} > 0$

  Check sum:
  $$\sum_{x=0}^4 P(X = x) = \frac{30 + 17 + 8 + 3 + 2}{60} = \frac{60}{60} = 1.00$$
  Since all point probabilities are strictly positive and bounded by 1, $k = 2/15$ defines a valid PMF.

**Answer.**  
$k = \frac{2}{15}$.

---

## Section C: Requested Textbook / Reference Exercises and Solutions

### Subsection C.1: Modern Mathematical Statistics with Applications (MMSA)

#### MMSA Basic Exercises

##### Exercise MMSA 2.49 (p. 83)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.4, p. 83, Exercise 49.  
**Classification:** MMSA — Basic.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
The population of a particular country consists of three ethnic groups. Each individual belongs to one of the four major blood groups. The accompanying joint probability table gives the proportions of individuals in the various ethnic group – blood group combinations:

| Ethnic Group | Blood O | Blood A | Blood B | Blood AB | Row Total |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 0.082 | 0.106 | 0.008 | 0.004 | 0.200 |
| **2** | 0.135 | 0.141 | 0.018 | 0.006 | 0.300 |
| **3** | 0.215 | 0.200 | 0.065 | 0.020 | 0.500 |
| **Column Total** | **0.432** | **0.447** | **0.091** | **0.030** | **1.000** |

Suppose that an individual is randomly selected from the population, and define events by:
- $A = \{\text{type A selected}\}$
- $B = \{\text{type B selected}\}$
- $C = \{\text{ethnic group 3 selected}\}$
- (a) Calculate $P(A)$, $P(C)$, and $P(A \cap C)$.
- (b) Calculate both $P(A \mid C)$ and $P(C \mid A)$ and explain in context what each of these probabilities represents.
- (c) If the selected individual does not have type B blood, what is the probability that he or she is from ethnic group 1?

**Complete working.**  
- **(a) Calculate $P(A)$, $P(C)$, and $P(A \cap C)$:**  
  Summing column A: $P(A) = 0.106 + 0.141 + 0.200 = 0.447$.  
  Summing row 3: $P(C) = 0.215 + 0.200 + 0.065 + 0.020 = 0.500$.  
  Intersection cell (Row 3, Col A): $P(A \cap C) = 0.200$.

- **(b) Calculate $P(A \mid C)$ and $P(C \mid A)$ and interpret:**  
  $$P(A \mid C) = \frac{P(A \cap C)}{P(C)} = \frac{0.200}{0.500} = 0.400$$
  *Meaning:* Given that a selected individual belongs to ethnic group 3, the probability that they have type A blood is $0.400$ (40.0%).
  $$P(C \mid A) = \frac{P(A \cap C)}{P(A)} = \frac{0.200}{0.447} = \frac{200}{447} \approx 0.447427$$
  *Meaning:* Given that a selected individual is observed to have type A blood, the probability that they belong to ethnic group 3 is approximately $0.4474$ (44.74%).

- **(c) Probability of ethnic group 1 given NOT type B blood ($P(E_1 \mid B^c)$):**  
  Let $E_1$ denote ethnic group 1.
  The conditioning event is $B^c$ (does not have type B blood).
  $$P(B^c) = 1 - P(B) = 1 - 0.091 = 0.909$$
  The joint event $E_1 \cap B^c$ consists of ethnic group 1 individuals with blood groups O, A, or AB:
  $$P(E_1 \cap B^c) = 0.082 + 0.106 + 0.004 = 0.192 \quad \text{(or } 0.200 - 0.008 = 0.192\text{)}$$
  Applying conditional probability:
  $$P(E_1 \mid B^c) = \frac{P(E_1 \cap B^c)}{P(B^c)} = \frac{0.192}{0.909} = \frac{192}{909} = \frac{64}{303} \approx 0.211221$$

**Answer.**  
- (a) $P(A) = 0.447$, $P(C) = 0.500$, $P(A \cap C) = 0.200$.
- (b) $P(A \mid C) = 0.400$; $P(C \mid A) \approx 0.4474$.
- (c) $P(E_1 \mid B^c) = \frac{64}{303} \approx 0.2112$.

---

##### Exercise MMSA 2.50 (p. 83)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.4, p. 83, Exercise 50.  
**Classification:** MMSA — Basic.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction), [PT-07](#problem-type-pt-07-posterior-probability-inversion-via-bayes-rule).

**Complete question statement.**  
Suppose an individual is randomly selected from the population of all adult males living in the United States. Let $A$ be the event that the selected individual is over 6 ft in height, and let $B$ be the event that the selected individual is a professional basketball player. Which do you think is larger, $P(A \mid B)$ or $P(B \mid A)$? Why?

**Complete working.**  
*(Note on Textbook Design: This is an intentionally qualitative, conceptual exercise from Section 2.4. The textbook problem statement provides no numerical parameters because the comparison is designed to be deduced directly from base-rate reasoning and conditional definitions).*

1. **Official Textbook Solutions Manual Qualitative Reasoning:**
   - **$P(A \mid B)$:** The probability that a randomly chosen person is over 6 ft tall, **given that he is a professional basketball player**. Because extreme height is an essential requirement in professional basketball, the vast majority of professional basketball players are over 6 ft tall. Therefore:
     $$P(A \mid B) pprox 1 \quad (	ext{or very close to } 100\%)$$
   - **$P(B \mid A)$:** The probability that a randomly chosen person is a professional basketball player, **given that he is over 6 ft tall**. In the general population, tens of millions of adult males exceed 6 ft in height, but top professional basketball leagues have roster spots for only a few hundred players. Out of all tall adult males, only a tiny fraction are professional athletes. Therefore:
     $$P(B \mid A) pprox 0 \quad (	ext{an infinitesimal fraction close to zero})$$

2. **Mathematical Formalization via Bayes' Ratio & Real-World Data:**  
   Using the definition of conditional probability:
   $$P(A \mid B) = rac{P(A \cap B)}{P(B)}, \quad P(B \mid A) = rac{P(A \cap B)}{P(A)}$$
   Dividing the two equations eliminates the common intersection $P(A \cap B)$:
   $$rac{P(A \mid B)}{P(B \mid A)} = rac{P(A)}{P(B)}$$
   In the US adult male population:
   - $P(A) pprox 0.15$ (roughly $15\%$ of adult males are over 6 ft tall).
   - $P(B) pprox rac{500}{130,000,000} pprox 3.8 	imes 10^{-6}$ (roughly 500 active pro players out of 130 million adult males).
   Because $P(A) \gg P(B)$ (by a factor of $pprox 40,000$), the ratio confirms:
   $$rac{P(A \mid B)}{P(B \mid A)} pprox 40,000 \gg 1 \implies P(A \mid B) \gg P(B \mid A)$$

**Answer.**  
**Textbook Answer:** $P(A \mid B)$ is **much larger** than $P(B \mid A)$.  
Almost all professional basketball players are over 6 ft tall ($P(A \mid B) pprox 1$), whereas out of all adult males over 6 ft tall, only an infinitesimal fraction play professional basketball ($P(B \mid A) pprox 0$).

---

##### Exercise MMSA 2.75 (p. 91)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.5, p. 91, Exercise 75.  
**Classification:** MMSA — Basic.  
**Relevant PT ID(s):** [PT-03](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics).

**Complete question statement.**  
An oil exploration company currently has two active projects, one in Asia and the other in Europe. Let $A$ be the event that the Asian project is successful and $B$ be the event that the European project is successful. Suppose that $A$ and $B$ are independent events with $P(A) = 0.4$ and $P(B) = 0.7$.
- (a) If the Asian project is not successful, what is the probability that the European project is also not successful? Explain your reasoning.
- (b) What is the probability that at least one of the two projects will be successful?
- (c) Given that at least one of the two projects is successful, what is the probability that only the Asian project is successful?

**Complete working.**  
Given $A \perp B$, $P(A) = 0.4$, $P(B) = 0.7$.

- **(a) Probability European project fails given Asian project fails ($P(B^c \mid A^c)$):**  
  By the Independence of Complements Theorem, if $A$ and $B$ are independent, then their complements $A^c$ and $B^c$ are also independent ($A^c \perp B^c$).  
  Therefore, the conditioning on $A^c$ provides zero informational influence on $B^c$:
  $$P(B^c \mid A^c) = P(B^c) = 1 - P(B) = 1 - 0.7 = 0.3$$

- **(b) Probability at least one project is successful ($P(A \cup B)$):**  
  Using the complement rule with independent complements:
  $$P(A \cup B) = 1 - P(A^c \cap B^c) = 1 - [P(A^c) \cdot P(B^c)] = 1 - [(1 - 0.4)(1 - 0.7)] = 1 - (0.6 \times 0.3) = 1 - 0.18 = 0.82$$
  *Alternative Check:* $P(A) + P(B) - P(A \cap B) = 0.4 + 0.7 - (0.4 \times 0.7) = 1.1 - 0.28 = 0.82$.

- **(c) Probability only Asian is successful given at least one is successful ($P(A \cap B^c \mid A \cup B)$):**  
  The event "only Asian is successful" is $A \cap B^c$.
  Because $(A \cap B^c) \subseteq (A \cup B)$, the intersection $(A \cap B^c) \cap (A \cup B) = A \cap B^c$.
  By independence of $A$ and $B^c$:
  $$P(A \cap B^c) = P(A) \cdot P(B^c) = 0.4 \times (1 - 0.7) = 0.4 \times 0.3 = 0.12$$
  Applying conditional probability:
  $$P(A \cap B^c \mid A \cup B) = \frac{P(A \cap B^c)}{P(A \cup B)} = \frac{0.12}{0.82} = \frac{12}{82} = \frac{6}{41} \approx 0.146341$$

**Answer.**  
- (a) $P(B^c \mid A^c) = 0.30$.
- (b) $P(A \cup B) = 0.82$.
- (c) $P(A \cap B^c \mid A \cup B) = \frac{6}{41} \approx 0.1463$.

---

##### Exercise MMSA 3.3 (p. 114)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 3.1, p. 114, Exercise 3.  
**Classification:** MMSA — Basic.  
**Relevant PT ID(s):** [PT-09](#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping).

**Complete question statement.**  
Using the experiment in Example 3.3 (which references Example 2.3, observing the number of pumps in use at two gas stations, each having 6 pumps, where outcomes are ordered pairs $(s_1, s_2)$ with $s_1, s_2 \in \{0, 1, 2, 3, 4, 5, 6\}$), define two more random variables and list the possible values of each.

**Complete working.**  
The sample space $\Omega$ consists of all $7 	imes 7 = 49$ ordered pairs $(s_1, s_2)$, where $s_1$ is the number of pumps in use at Station 1 and $s_2$ is the number of pumps in use at Station 2. Example 3.3 already defined $X = s_1 + s_2$, $Y = s_1 - s_2$, and $U = \max(s_1, s_2)$.

We define two valid additional random variables mapping $\Omega 	o \mathbb{R}$ matching the textbook solution manual:
1. **Random Variable 1 (Textbook Solutions Manual Definition):**  
   Let $M$ be the absolute value of the difference between the outcomes:
   $$M(s_1, s_2) = |s_1 - s_2|$$
   - Minimum value: Occurs when $s_1 = s_2$ (e.g., $(0, 0)$), giving $|s_1 - s_2| = 0$.
   - Maximum value: Occurs when one station has 6 pumps in use and the other has 0 (e.g., $(6, 0)$ or $(0, 6)$), giving $|6 - 0| = 6$.
   - Possible values: $\mathcal{M} = \{0, 1, 2, 3, 4, 5, 6\}$.

2. **Random Variable 2 (Textbook Solutions Manual Definition):**  
   Let $W = 1$ if the sum of the two resulting numbers is even and $W = 0$ otherwise (a Bernoulli random variable):
   $$W(s_1, s_2) = egin{cases} 1 & 	ext{if } s_1 + s_2 	ext{ is even} \ 0 & 	ext{if } s_1 + s_2 	ext{ is odd} \end{cases}$$
   - Possible values: $\mathcal{W} = \{0, 1\}$.

*(Alternative valid RV: $Z = \min(s_1, s_2)$ with possible values $\{0, 1, 2, 3, 4, 5, 6\}$.)*

**Answer.**  
**Textbook Answer:**  
- $M = 	ext{the absolute value of the difference between the outcomes } |s_1 - s_2|$; possible values $\{0, 1, 2, 3, 4, 5, 6\}$.
- $W = 1 	ext{ if the sum of the two resulting numbers is even and } W = 0 	ext{ otherwise}$ (a Bernoulli random variable); possible values $\{0, 1\}$.

---

##### Exercise MMSA 3.6 (p. 114)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 3.1, p. 114, Exercise 6.  
**Classification:** MMSA — Basic.  
**Relevant PT ID(s):** [PT-09](#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping).

**Complete question statement.**  
Starting at a fixed time, each car entering an intersection is observed to see whether it turns left ($L$), right ($R$), or goes straight ahead ($A$). The experiment terminates as soon as a car is observed to turn left. Let $X = \text{the number of cars observed}$. What are possible $X$ values? List five outcomes and their associated $X$ values.

**Complete working.**  
- **Possible values of $X$:**  
  The experiment terminates upon observing the first left-turning car ($L$).
  The shortest possible sequence is that the very first car turns left ($L$), giving $X = 1$.
  The first left turn could theoretically occur on the 2nd car, 3rd car, or after any arbitrarily long sequence of non-left turns ($R$ or $A$).
  Therefore, the possible values of $X$ are the set of all positive integers:
  $$\mathcal{X} = \{1, 2, 3, 4, 5, \dots\} = \mathbb{Z}^+$$
  This support is countably infinite.

- **Five specific outcomes and associated $X$ values:**  
  1. Outcome: $\omega_1 = L \implies X(\omega_1) = 1$.
  2. Outcome: $\omega_2 = RL \implies X(\omega_2) = 2$.
  3. Outcome: $\omega_3 = AL \implies X(\omega_3) = 2$.
  4. Outcome: $\omega_4 = ARL \implies X(\omega_4) = 3$.
  5. Outcome: $\omega_5 = RAAL \implies X(\omega_5) = 4$.

**Answer.**  
Possible $X$ values: $\{1, 2, 3, 4, \dots\}$ (all positive integers). Five outcomes: $L$ ($X=1$), $RL$ ($X=2$), $AL$ ($X=2$), $ARL$ ($X=3$), $RAAL$ ($X=4$).

---

##### Exercise MMSA 3.7 (p. 114)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 3.1, p. 114, Exercise 7.  
**Classification:** MMSA — Basic.  
**Relevant PT ID(s):** [PT-09](#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping).

**Complete question statement.**  
For each random variable defined here, describe the set of possible values for the variable, and state whether the variable is discrete:
- (a) $X =$ the number of unbroken eggs in a randomly chosen standard egg carton
- (b) $Y =$ the number of students on a class list for a particular course who are absent on the first day of classes
- (c) $U =$ the number of times a duffer has to swing at a golf ball before hitting it
- (d) $X =$ the length of a randomly selected rattlesnake
- (e) $Z =$ the amount of royalties earned from the sale of a first edition of 10,000 textbooks
- (f) $Y =$ the pH of a randomly chosen soil sample
- (g) $X =$ the tension (psi) at which a randomly selected tennis racket has been strung
- (h) $X =$ the total number of coin tosses required for three individuals to obtain a match ($HHH$ or $TTT$)

**Complete working.**  
- **(a) $X =$ number of unbroken eggs in standard egg carton:**  
  A standard carton holds 12 eggs. The number unbroken can be any integer from 0 to 12.  
  Set of possible values: $\{0, 1, 2, \dots, 12\}$.  
  **Discrete** (finite support).

- **(b) $Y =$ number of absent students on first day out of class list of size $n$:**  
  Set of possible values: $\{0, 1, 2, \dots, n\}$, where $n$ is the fixed course enrollment.  
  **Discrete** (finite support).

- **(c) $U =$ number of swings before hitting golf ball:**  
  The golfer must swing at least once ($U=1$), and could theoretically miss indefinitely ($U=2, 3, \dots$).  
  Set of possible values: $\{1, 2, 3, \dots\} = \mathbb{Z}^+$.  
  **Discrete** (countably infinite support).

- **(d) $X =$ length of a randomly selected rattlesnake:**  
  Length is a physical spatial dimension measured along a continuum.  
  Set of possible values: $\{x : 0 < x < \infty\}$ assuming a rattlesnake can be arbitrarily short or long.  
  **Continuous (not discrete)**.

- **(e) $Z =$ royalties earned from sale of 10,000 textbooks:**  
  With $c$ denoting the amount of royalty earned per book sold, possible values are $0, c, 2c, 3c, \dots, 10000c$.  
  Set of possible values: $\{0, c, 2c, \dots, 10000c\}$.  
  **Discrete** (finite support).

- **(f) $Y =$ pH of a randomly chosen soil sample:**  
  Chemical pH is a continuous chemical concentration measurement ($-\log_{10}[	ext{H}^+]$), where 0 is the smallest possible pH and 14 is the largest possible pH.  
  Set of possible values: $\{y : 0 < y < 14\}$.  
  **Continuous (not discrete)**.

- **(g) $X =$ tension (psi) of a tennis racket:**  
  With $m$ and $M$ denoting the minimum and maximum possible string tensions, respectively, possible values are $\{x : m < x < M\}$.  
  **Continuous (not discrete)**.

- **(h) $X =$ total coin tosses for three individuals until a match ($HHH$ or $TTT$):**  
  In each round, all three individuals toss their coins simultaneously, meaning each trial requires **3 tosses** (one per person). If a match is obtained on round 1, exactly 3 tosses occurred; on round 2, $3 	imes 2 = 6$ tosses occurred; on round $k$, $3k$ tosses occurred.  
  Set of possible values: $\{3, 6, 9, 12, 15, \dots\} = \{3k : k \in \mathbb{Z}^+\}$.  
  **Discrete** (countably infinite support).

**Answer.**  
**Textbook Answer:**  
- (a) Possible values are $0, 1, 2, \dots, 12$; **discrete**.
- (b) With $N =$ number on the list, values are $0, 1, 2, \dots, N$; **discrete**.
- (c) Possible values are $1, 2, 3, 4, \dots$; **discrete**.
- (d) $\{x : 0 < x < \infty\}$; **not discrete**.
- (e) With $c =$ amount earned per book sold, possible values are $0, c, 2c, \dots, 10,000c$; **discrete**.
- (f) $\{y : 0 < y < 14\}$; **not discrete**.
- (g) With $m$ and $M$ denoting min and max possible tensions, $\{x : m < x < M\}$; **not discrete**.
- (h) Possible values are $3, 6, 9, 12, 15, \dots$ (i.e., $3(1), 3(2), 3(3), \dots$); **discrete**.

---

##### Exercise MMSA 3.11 (p. 114)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 3.1, p. 114, Exercise 11.  
**Classification:** MMSA — Basic.  
**Relevant PT ID(s):** [PT-10](#problem-type-pt-10-pmf-normalization-parameter-determination-and-validation).

**Complete question statement.**  
Let $X$ be the number of students who show up at a professor's office hours on a particular day. Suppose that the only possible values of $X$ are $0, 1, 2, 3,$ and $4$, and that $p(0) = 0.30$, $p(1) = 0.25$, $p(2) = 0.20$, and $p(3) = 0.15$.
- (a) What is $p(4)$?
- (b) Draw both a line graph and a probability histogram for the pmf of $X$.
- (c) What is the probability that at least two students come to the office hour? What is the probability that more than two students come to the office hour?
- (d) What is the probability that the professor shows up for his office hour?

**Complete working.**  
Support: $\mathcal{X} = \{0, 1, 2, 3, 4\}$.

- **(a) What is $p(4)$?**  
  By the normalization axiom of a PMF, $\sum_{x=0}^4 p(x) = 1$:
  $$p(0) + p(1) + p(2) + p(3) + p(4) = 1$$
  $$0.30 + 0.25 + 0.20 + 0.15 + p(4) = 1 \implies 0.90 + p(4) = 1 \implies p(4) = 0.10$$

- **(b) Visual Representations (Line Graph and Probability Histogram):**  
  *(See graphical render in [Study-Notes.md: PMF Visual Representations](Study-Notes.md#3-probability-mass-function-pmf) and figure `graphs/pmf-distribution-visualization.png`)*
  - **Probability Histogram:** Centered at integers $x \in \{0, 1, 2, 3, 4\}$ with bin width $1.0$ (spanning $[x - 0.5, x + 0.5]$). Heights equal $p(x)$: heights $0.30, 0.25, 0.20, 0.15, 0.10$. Total area $= 1.0 \times 1.00 = 1.00$.
  - **Line Graph (Spike Plot):** Vertical line segments erected from $(x, 0)$ to $(x, p(x))$ with a circular point mass marker at the top.

- **(c) Evaluate $P(X \ge 2)$ and $P(X > 2)$:**  
  - *At least two students ($P(X \ge 2)$):*
    $$P(X \ge 2) = p(2) + p(3) + p(4) = 0.20 + 0.15 + 0.10 = 0.45$$
    *(Or via complement: $1 - [p(0) + p(1)] = 1 - 0.55 = 0.45$)*
  - *More than two students ($P(X > 2)$):*
    $$P(X > 2) = p(3) + p(4) = 0.15 + 0.10 = 0.25$$

- **(d) Probability professor shows up:**  
  The definition of the random variable $X$ ("number of students who show up at a professor's office hours on a particular day") is predicated on the office hour taking place. In the context of probability modeling, this parameter is outside the domain of the random variable $X$ itself; given that the model specifies office hour attendance, the professor is presumed present with probability $1.0$ (or the condition is defined on the event that the office hour was held).

**Answer.**  
- (a) $p(4) = 0.10$.
- (b) Histogram and spike plot constructed; see `graphs/pmf-distribution-visualization.png`.
- (c) $P(X \ge 2) = 0.45$; $P(X > 2) = 0.25$.
- (d) $1.0$ (under the foundational premise that the scheduled office hour occurs).

---

#### MMSA Medium Exercises

##### Exercise MMSA 2.57 (p. 84)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.4, p. 84, Exercise 57.  
**Classification:** MMSA — Medium.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
A certain shop repairs both audio and video components. Let $A$ denote the event that the next component brought in for repair is an audio component, and let $B$ be the event that the next component is an MP3 player (so the event $B$ is contained in $A$). Suppose that $P(A) = 0.6$ and $P(B) = 0.05$. What is $P(B \mid A)$?

**Complete working.**  
We are given that $B \subseteq A$ (every MP3 player is an audio component).
By set theory, whenever $B \subseteq A$, the intersection is simply $B$:
$$A \cap B = B$$
Applying the definition of conditional probability:
$$P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{P(B)}{P(A)}$$
Substitute the given values $P(B) = 0.05$ and $P(A) = 0.60$:
$$P(B \mid A) = \frac{0.05}{0.60} = \frac{5}{60} = \frac{1}{12} \approx 0.083333$$

**Answer.**  
$P(B \mid A) = \frac{1}{12} \approx 0.0833$ (8.33%).

---

##### Exercise MMSA 2.58 (p. 84)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.4, p. 84, Exercise 58.  
**Classification:** MMSA — Medium.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
In Exercise 15, $A_i = \{\text{awarded project } i\}$, for $i = 1, 2, 3$. Use the probabilities given there:
- $P(A_1) = 0.22$, $P(A_2) = 0.25$, $P(A_3) = 0.28$
- $P(A_1 \cap A_2) = 0.11$, $P(A_1 \cap A_3) = 0.05$, $P(A_2 \cap A_3) = 0.07$
- $P(A_1 \cap A_2 \cap A_3) = 0.01$
to compute the following probabilities, and explain in words the meaning of each one:
- (a) $P(A_2 \mid A_1)$
- (b) $P(A_2 \cap A_3 \mid A_1)$
- (c) $P(A_2 \cup A_3 \mid A_1)$
- (d) $P(A_1 \cap A_2 \cap A_3 \mid A_1 \cup A_2 \cup A_3)$

**Complete working.**  
*(This problem matches Lecture Example 2 exactly, with subparts (b) and (d) fully integrated).*

- **(a) $P(A_2 \mid A_1)$:**  
  $$P(A_2 \mid A_1) = \frac{P(A_1 \cap A_2)}{P(A_1)} = \frac{0.11}{0.22} = 0.50$$
  *Meaning:* Given that Project 1 is awarded, the probability that Project 2 is also awarded is $0.50$ (50.0%).

- **(b) $P(A_2 \cap A_3 \mid A_1)$:**  
  $$P(A_2 \cap A_3 \mid A_1) = \frac{P(A_1 \cap A_2 \cap A_3)}{P(A_1)} = \frac{0.01}{0.22} = \frac{1}{22} \approx 0.045455$$
  *Meaning:* Given that Project 1 is awarded, the probability that both Projects 2 and 3 are also awarded (all three projects won) is $1/22 \approx 4.55\%$.

- **(c) $P(A_2 \cup A_3 \mid A_1)$:**  
  By distributive expansion: $(A_2 \cup A_3) \cap A_1 = (A_1 \cap A_2) \cup (A_1 \cap A_3)$.
  $$P((A_1 \cap A_2) \cup (A_1 \cap A_3)) = P(A_1 \cap A_2) + P(A_1 \cap A_3) - P(A_1 \cap A_2 \cap A_3) = 0.11 + 0.05 - 0.01 = 0.15$$
  $$P(A_2 \cup A_3 \mid A_1) = \frac{0.15}{0.22} = \frac{15}{22} \approx 0.681818$$
  *Meaning:* Given that Project 1 is awarded, the probability that at least one of Project 2 or Project 3 is also awarded is $15/22 \approx 68.18\%$.

- **(d) $P(A_1 \cap A_2 \cap A_3 \mid A_1 \cup A_2 \cup A_3)$:**  
  By PIE:
  $$P(A_1 \cup A_2 \cup A_3) = (0.22 + 0.25 + 0.28) - (0.11 + 0.05 + 0.07) + 0.01 = 0.75 - 0.23 + 0.01 = 0.53$$
  $$P(A_1 \cap A_2 \cap A_3 \mid A_1 \cup A_2 \cup A_3) = \frac{0.01}{0.53} = \frac{1}{53} \approx 0.018868$$
  *Meaning:* Given that at least one project is awarded to the firm, the probability that all three projects are awarded is $1/53 \approx 1.89\%$.

**Answer.**  
- (a) $P(A_2 \mid A_1) = 0.50$.
- (b) $P(A_2 \cap A_3 \mid A_1) = \frac{1}{22} \approx 0.0455$.
- (c) $P(A_2 \cup A_3 \mid A_1) = \frac{15}{22} \approx 0.6818$.
- (d) $P(A_1 \cap A_2 \cap A_3 \mid A_1 \cup A_2 \cup A_3) = \frac{1}{53} \approx 0.0189$.

---

##### Exercise MMSA 2.60 (p. 84)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.4, p. 84, Exercise 60.  
**Classification:** MMSA — Medium.  
**Relevant PT ID(s):** [PT-05](#problem-type-pt-05-total-probability-computation-via-partition-decompositions-and-tree-diagrams), [PT-07](#problem-type-pt-07-posterior-probability-inversion-via-bayes-rule).

**Complete question statement.**  
Three plants manufacture hard drives and ship them to a warehouse for distribution. Plant I produces 54% of the warehouse's inventory with a 4% defect rate. Plant II produces 35% of the warehouse's inventory with an 8% defect rate. Plant III produces the remainder of the warehouse's inventory with a 12% defect rate.
- (a) Draw a tree diagram to represent this information.
- (b) A warehouse inspector selects one hard drive at random. What is the probability that it is a defective hard drive and from Plant II?
- (c) What is the probability that a randomly selected hard drive is defective?
- (d) Suppose a hard drive is defective. What is the probability that it came from Plant II?

**Complete working.**  
Let $B_1, B_2, B_3$ denote the plants, and $D$ denote a defective hard drive.
- Priors: $P(B_1) = 0.54$, $P(B_2) = 0.35$.
  Remainder: $P(B_3) = 1 - 0.54 - 0.35 = 0.11$.
- Conditional defect rates:
  $P(D \mid B_1) = 0.04$, $P(D \mid B_2) = 0.08$, $P(D \mid B_3) = 0.12$.

- **(a) Tree Diagram Structure:**  
  - Root branches into Plant I ($0.54$), Plant II ($0.35$), Plant III ($0.11$).
  - From Plant I: Defective ($0.04$), Good ($0.96$). Joint $P(B_1 \cap D) = 0.54 \times 0.04 = 0.0216$.
  - From Plant II: Defective ($0.08$), Good ($0.92$). Joint $P(B_2 \cap D) = 0.35 \times 0.08 = 0.0280$.
  - From Plant III: Defective ($0.12$), Good ($0.88$). Joint $P(B_3 \cap D) = 0.11 \times 0.12 = 0.0132$.

- **(b) Probability defective and from Plant II ($P(B_2 \cap D)$):**  
  $$P(B_2 \cap D) = P(D \mid B_2) \cdot P(B_2) = 0.08 \times 0.35 = 0.0280 \quad (2.80\%)$$

- **(c) Overall probability of a defective hard drive ($P(D)$):**  
  Applying the Law of Total Probability:
  $$P(D) = P(B_1 \cap D) + P(B_2 \cap D) + P(B_3 \cap D) = 0.0216 + 0.0280 + 0.0132 = 0.0628 \quad (6.28\%)$$

- **(d) Probability defective came from Plant II ($P(B_2 \mid D)$):**  
  Applying Bayes' Rule:
  $$P(B_2 \mid D) = \frac{P(B_2 \cap D)}{P(D)} = \frac{0.0280}{0.0628} = \frac{280}{628} = \frac{70}{157} \approx 0.445860 \quad (44.59\%)$$

**Answer.**  
- (a) Tree diagram described above.
- (b) $P(B_2 \cap D) = 0.0280$ (2.80%).
- (c) $P(D) = 0.0628$ (6.28%).
- (d) $P(B_2 \mid D) = \frac{70}{157} \approx 0.4459$ (44.59%).

---

##### Exercise MMSA 2.64 (p. 84)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.4, p. 84, Exercise 64.  
**Classification:** MMSA — Medium.  
**Relevant PT ID(s):** [PT-05](#problem-type-pt-05-total-probability-computation-via-partition-decompositions-and-tree-diagrams), [PT-07](#problem-type-pt-07-posterior-probability-inversion-via-bayes-rule).

**Complete question statement.**  
At a gas station, 40% of the customers use regular gas ($A_1$), 35% use midgrade gas ($A_2$), and 25% use premium gas ($A_3$). Of those customers using regular gas, only 30% fill their tanks (event $B$). Of those customers using midgrade gas, 60% fill their tanks, whereas of those using premium, 50% fill their tanks.
- (a) What is the probability that the next customer will request midgrade gas and fill the tank ($A_2 \cap B$)?
- (b) What is the probability that the next customer fills the tank?
- (c) If the next customer fills the tank, what is the probability that regular gas is requested? Midgrade gas? Premium gas?

**Complete working.**  
Priors: $P(A_1) = 0.40, P(A_2) = 0.35, P(A_3) = 0.25$.
Conditional fill rates: $P(B \mid A_1) = 0.30, P(B \mid A_2) = 0.60, P(B \mid A_3) = 0.50$.

- **(a) $P(A_2 \cap B)$:**  
  $$P(A_2 \cap B) = P(B \mid A_2) \cdot P(A_2) = 0.60 \times 0.35 = 0.210$$

- **(b) Total probability customer fills tank ($P(B)$):**  
  Applying the Law of Total Probability:
  $$P(B) = P(B \mid A_1)P(A_1) + P(B \mid A_2)P(A_2) + P(B \mid A_3)P(A_3)$$
  $$P(B) = (0.30 \times 0.40) + (0.60 \times 0.35) + (0.50 \times 0.25)$$
  $$P(B) = 0.120 + 0.210 + 0.125 = 0.455$$

- **(c) Posterior probabilities given customer fills tank ($B$):**  
  - *Regular ($A_1$):*
    $$P(A_1 \mid B) = \frac{P(A_1 \cap B)}{P(B)} = \frac{0.120}{0.455} = \frac{120}{455} = \frac{24}{91} \approx 0.263736 \quad (26.37\%)$$
  - *Midgrade ($A_2$):*
    $$P(A_2 \mid B) = \frac{P(A_2 \cap B)}{P(B)} = \frac{0.210}{0.455} = \frac{210}{455} = \frac{42}{91} = \frac{6}{13} \approx 0.461538 \quad (46.15\%)$$
  - *Premium ($A_3$):*
    $$P(A_3 \mid B) = \frac{P(A_3 \cap B)}{P(B)} = \frac{0.125}{0.455} = \frac{125}{455} = \frac{25}{91} \approx 0.274725 \quad (27.47\%)$$
  Sum check: $\frac{24 + 42 + 25}{91} = \frac{91}{91} = 1.00$.

**Answer.**  
- (a) $P(A_2 \cap B) = 0.210$ (21.0%).
- (b) $P(B) = 0.455$ (45.5%).
- (c) $P(A_1 \mid B) = \frac{24}{91} \approx 0.2637$; $P(A_2 \mid B) = \frac{6}{13} \approx 0.4615$; $P(A_3 \mid B) = \frac{25}{91} \approx 0.2747$.

---

##### Exercise MMSA 2.79 (p. 92)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.5, p. 92, Exercise 79.  
**Classification:** MMSA — Medium.  
**Relevant PT ID(s):** [PT-03](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics).

**Complete question statement.**  
The probability that a grader will make a marking error on any particular question of a multiple-choice exam is $0.1$. If there are ten questions and questions are marked independently:
- What is the probability that no errors are made?
- That at least one error is made?
- If there are $n$ questions and the probability of a marking error is $p$ rather than $0.1$, give expressions for these two probabilities.

**Complete working.**  
Let $E_i$ be the event that a marking error is made on question $i$.
We are given that $E_1, \dots, E_n$ are mutually independent events with $P(E_i) = p$.
The probability of marking question $i$ correctly is $P(E_i^c) = 1 - p$.

- **No errors made on $n=10$ questions ($p=0.1$):**  
  No errors means that all 10 questions are marked correctly ($E_1^c \cap E_2^c \cap \cdots \cap E_{10}^c$).
  By mutual independence:
  $$P(\text{No Errors}) = \prod_{i=1}^{10} P(E_i^c) = (1 - 0.1)^{10} = (0.9)^{10} \approx 0.348678$$

- **At least one error made on $n=10$ questions:**  
  Applying the complement rule:
  $$P(\ge 1 \text{ Error}) = 1 - P(\text{No Errors}) = 1 - (0.9)^{10} \approx 1 - 0.348678 = 0.651322$$

- **General expressions for $n$ questions with error rate $p$:**  
  - $P(\text{No Errors}) = (1 - p)^n$.
  - $P(\text{At Least One Error}) = 1 - (1 - p)^n$.

**Answer.**  
- $P(\text{No Errors, } 10) = (0.9)^{10} \approx 0.3487$ (34.87%).
- $P(\ge 1 \text{ Error, } 10) = 1 - (0.9)^{10} \approx 0.6513$ (65.13%).
- General: No errors $= (1 - p)^n$; At least one error $= 1 - (1 - p)^n$.

---

##### Exercise MMSA 2.83 (p. 92)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.5, p. 92, Exercise 83.  
**Classification:** MMSA — Medium.  
**Relevant PT ID(s):** [PT-04](#problem-type-pt-04-system-reliability-and-network-flow-modeling-with-independent-components).

**Complete question statement.**  
Consider the system of components connected as in the accompanying picture. Components 1 and 2 are connected in parallel, so that subsystem works if and only if either 1 or 2 works; since 3 and 4 are connected in series, that subsystem works if and only if both 3 and 4 work. The parallel subsystem (1, 2) and the series subsystem (3, 4) are themselves connected in parallel across the main system terminals. If components work independently of one another and $P(\text{component works}) = 0.9$, calculate $P(\text{system works})$.

**Complete working.**  
Let $C_i$ denote the event that component $i$ functions, with $P(C_i) = p = 0.90$ for $i = 1, 2, 3, 4$. All components operate independently.

- **Step 1: Evaluate Subsystem A (Components 1 and 2 in parallel):**  
  Subsystem A works if at least one of 1 or 2 works:
  $$P(A) = 1 - P(C_1^c \cap C_2^c) = 1 - (1 - p)^2 = 1 - (0.10)^2 = 1 - 0.01 = 0.99$$
  $$P(A^c) = 0.01$$

- **Step 2: Evaluate Subsystem B (Components 3 and 4 in series):**  
  Subsystem B works if both 3 and 4 work:
  $$P(B) = P(C_3 \cap C_4) = P(C_3) \cdot P(C_4) = (0.90)^2 = 0.81$$
  $$P(B^c) = 1 - 0.81 = 0.19$$

- **Step 3: Evaluate Overall System (Subsystem A and Subsystem B in parallel):**  
  The overall system transmits if **either** Subsystem A works **or** Subsystem B works (parallel top-level architecture).  
  The system fails if and only if **both** Subsystem A fails and Subsystem B fails:
  $$P(\text{System Fails}) = P(A^c \cap B^c) = P(A^c) \cdot P(B^c) = 0.01 \times 0.19 = 0.0019$$
  $$P(\text{System Works}) = 1 - P(\text{System Fails}) = 1 - 0.0019 = 0.9981$$

*Direct Union Verification:*  
$$P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.99 + 0.81 - (0.99 \times 0.81) = 1.80 - 0.8019 = 0.9981$$

**Answer.**  
$P(\text{System Works}) = 0.9981$ (99.81%).

---

#### MMSA Test Exercises

##### Exercise MMSA 2.55 (p. 84)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.4, p. 84, Exercise 55.  
**Classification:** MMSA — Test.  
**Relevant PT ID(s):** [PT-02](#problem-type-pt-02-multi-stage-sequential-intersection-via-the-general-multiplication--chain-rule), [PT-05](#problem-type-pt-05-total-probability-computation-via-partition-decompositions-and-tree-diagrams).

**Complete question statement.**  
One box contains six red balls and four green balls, and a second box contains seven red balls and three green balls. A ball is randomly chosen from the first box and placed in the second box. Then a ball is randomly selected from the second box and placed in the first box.
- (a) What is the probability that a red ball is selected from the first box and a red ball is selected from the second box?
- (b) At the conclusion of the selection process, what is the probability that the numbers of red and green balls in the first box are identical to the numbers at the beginning?

**Complete working.**  
Initial box compositions:
- Box 1: 6 Red ($R_1$), 4 Green ($G_1$). Total $= 10$.
- Box 2: 7 Red, 3 Green. Total $= 10$.

- **(a) Probability a red ball is selected from Box 1 and a red ball is selected from Box 2 ($P(R_1 \cap R_2)$):**  
  Applying the multiplication rule:
  $$P(R_1 \cap R_2) = P(R_2 \mid R_1) \cdot P(R_1)$$
  From Box 1: $P(R_1) = \frac{6}{10}$.
  If a red ball is placed into Box 2, Box 2 now contains $7 + 1 = 8$ red balls and 3 green balls (total 11).
  $$P(R_2 \mid R_1) = \frac{8}{11}$$
  $$P(R_1 \cap R_2) = \frac{6}{10} \times \frac{8}{11} = \frac{48}{110} = \frac{24}{55} \approx 0.436364$$

- **(b) Probability Box 1 ends with its original composition:**  
  Box 1 initially has 6 red and 4 green balls. Its composition remains identical at the end if and only if the ball transferred from Box 2 back to Box 1 has the **exact same colour** as the ball originally transferred from Box 1 to Box 2. This can occur via two mutually exclusive cases:
  1. *Case 1 (Red transferred 1 to 2, Red returned 2 to 1):* $R_1 \cap R_2$.
     From part (a): $P(R_1 \cap R_2) = \frac{48}{110}$.
  2. *Case 2 (Green transferred 1 to 2, Green returned 2 to 1):* $G_1 \cap G_2$.
     From Box 1: $P(G_1) = \frac{4}{10}$.
     If a green ball is transferred, Box 2 now contains 7 red balls and $3 + 1 = 4$ green balls (total 11).
     $$P(G_2 \mid G_1) = \frac{4}{11}$$
     $$P(G_1 \cap G_2) = \frac{4}{10} \times \frac{4}{11} = \frac{16}{110}$$

  Summing the two disjoint cases:
  $$P(\text{Identical Composition}) = P(R_1 \cap R_2) + P(G_1 \cap G_2) = \frac{48}{110} + \frac{16}{110} = \frac{64}{110} = \frac{32}{55} \approx 0.581818$$

**Answer.**  
- (a) $P(R_1 \cap R_2) = \frac{24}{55} \approx 0.4364$ (43.64%).
- (b) $P(\text{Identical}) = \frac{32}{55} \approx 0.5818$ (58.18%).

---

##### Exercise MMSA 2.67 (p. 84)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.4, p. 84, Exercise 67.  
**Classification:** MMSA — Test.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction), [PT-02](#problem-type-pt-02-multi-stage-sequential-intersection-via-the-general-multiplication--chain-rule).

**Complete question statement.**  
Verify the multiplication rule for conditional probabilities:
$$P(A \cap B \mid C) = P(A \mid B \cap C) \cdot P(B \mid C)$$

**Complete working.**  
Assume $P(B \cap C) > 0$, which also implies $P(C) \ge P(B \cap C) > 0$.
- **Left-Hand Side (LHS):**  
  By the definition of conditional probability:
  $$P(A \cap B \mid C) = \frac{P((A \cap B) \cap C)}{P(C)} = \frac{P(A \cap B \cap C)}{P(C)}$$

- **Right-Hand Side (RHS):**  
  Express each factor on the right-hand side using the definition of conditional probability:
  $$P(A \mid B \cap C) = \frac{P(A \cap (B \cap C))}{P(B \cap C)} = \frac{P(A \cap B \cap C)}{P(B \cap C)}$$
  $$P(B \mid C) = \frac{P(B \cap C)}{P(C)}$$
  Multiplying the two terms:
  $$P(A \mid B \cap C) \cdot P(B \mid C) = \frac{P(A \cap B \cap C)}{P(B \cap C)} \times \frac{P(B \cap C)}{P(C)}$$
  The non-zero scalar term $P(B \cap C)$ cancels algebraically from the numerator and denominator:
  $$= \frac{P(A \cap B \cap C)}{P(C)}$$
  This is identical to the LHS.
  If $P(B \cap C) = 0$, both sides are defined to be 0. Thus, the identity holds universally. $\blacksquare$

**Answer.**  
Proof established algebraically by expanding definitions: $\frac{P(A \cap B \cap C)}{P(B \cap C)} \times \frac{P(B \cap C)}{P(C)} = \frac{P(A \cap B \cap C)}{P(C)} = P(A \cap B \mid C)$.

---

##### Exercise MMSA 2.71 (p. 84)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.4, p. 84, Exercise 71.  
**Classification:** MMSA — Test.  
**Relevant PT ID(s):** [PT-07](#problem-type-pt-07-posterior-probability-inversion-via-bayes-rule).

**Complete question statement.**  
A friend who lives in Los Angeles makes frequent consulting trips to Washington, D.C.; 50% of the time she travels on airline #1, 30% of the time on airline #2, and the remaining 20% of the time on airline #3. For airline #1, flights are late into D.C. 30% of the time and late into L.A. 10% of the time. For airline #2, these percentages are 25% and 20%, whereas for airline #3 the percentages are 40% and 25%. 

If we learn that on a particular trip she arrived late at **exactly one** of the two destinations, what are the posterior probabilities of having flown on airlines #1, #2, and #3? Assume that the chance of a late arrival in L.A. is unaffected by what happens on the flight to D.C. [Hint: From the tip of each first-generation branch on a tree diagram, draw three second-generation branches labeled, respectively, 0 late, 1 late, and 2 late.]

**Complete working.**  
Let $A_1, A_2, A_3$ be the airlines, with priors:
- $P(A_1) = 0.50$
- $P(A_2) = 0.30$
- $P(A_3) = 0.20$

Let $D$ be late into D.C. and $L$ be late into L.A. Conditional on airline $A_i$, $D$ and $L$ are independent.
For airline $i$, let $p_i = P(D \mid A_i)$ and $q_i = P(L \mid A_i)$:
- Airline 1: $p_1 = 0.30, q_1 = 0.10$
- Airline 2: $p_2 = 0.25, q_2 = 0.20$
- Airline 3: $p_3 = 0.40, q_3 = 0.25$

Let $E$ be the event of arriving late at **exactly one** destination:
$$E = (D \cap L^c) \cup (D^c \cap L)$$
By conditional independence for each airline:
$$P(E \mid A_i) = p_i(1 - q_i) + (1 - p_i)q_i$$

- **Compute conditional likelihoods $P(E \mid A_i)$:**  
  - For $A_1$: $P(E \mid A_1) = (0.30)(0.90) + (0.70)(0.10) = 0.27 + 0.07 = 0.34$.
  - For $A_2$: $P(E \mid A_2) = (0.25)(0.80) + (0.75)(0.20) = 0.20 + 0.15 = 0.35$.
  - For $A_3$: $P(E \mid A_3) = (0.40)(0.75) + (0.60)(0.25) = 0.30 + 0.15 = 0.45$.

- **Compute joint probabilities $P(A_i \cap E) = P(E \mid A_i)P(A_i)$:**  
  - $P(A_1 \cap E) = 0.34 \times 0.50 = 0.170$.
  - $P(A_2 \cap E) = 0.35 \times 0.30 = 0.105$.
  - $P(A_3 \cap E) = 0.45 \times 0.20 = 0.090$.

- **Compute total evidence probability $P(E)$ via LTP:**  
  $$P(E) = 0.170 + 0.105 + 0.090 = 0.365$$

- **Compute posterior probabilities via Bayes' Rule:**  
  - **Airline 1:**
    $$P(A_1 \mid E) = \frac{P(A_1 \cap E)}{P(E)} = \frac{0.170}{0.365} = \frac{170}{365} = \frac{34}{73} \approx 0.465753$$
  - **Airline 2:**
    $$P(A_2 \mid E) = \frac{P(A_2 \cap E)}{P(E)} = \frac{0.105}{0.365} = \frac{105}{365} = \frac{21}{73} \approx 0.287671$$
  - **Airline 3:**
    $$P(A_3 \mid E) = \frac{P(A_3 \cap E)}{P(E)} = \frac{0.090}{0.365} = \frac{90}{365} = \frac{18}{73} \approx 0.246575$$
  Sum check: $\frac{34 + 21 + 18}{73} = \frac{73}{73} = 1.00$.

**Answer.**  
- $P(A_1 \mid E) = \frac{34}{73} \approx 0.4658$ (46.58%).
- $P(A_2 \mid E) = \frac{21}{73} \approx 0.2877$ (28.77%).
- $P(A_3 \mid E) = \frac{18}{73} \approx 0.2466$ (24.66%).

---

##### Exercise MMSA 2.77 (p. 92)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.5, p. 92, Exercise 77.  
**Classification:** MMSA — Test.  
**Relevant PT ID(s):** [PT-03](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics).

**Complete question statement.**  
If $A$ and $B$ are independent events, show that $A'$ ($A^c$) and $B$ are also independent. [Hint: First establish a relationship among $P(A' \cap B), P(B),$ and $P(A \cap B)$.]

**Complete working.**  
Let events $A$ and $B$ be independent, meaning $P(A \cap B) = P(A) \cdot P(B)$.
- **Step 1: Partition event $B$:**  
  Event $B$ can be decomposed into two mutually exclusive subsets depending on whether $A$ occurs:
  $$B = (A \cap B) \cup (A^c \cap B)$$
  Because $A$ and $A^c$ are disjoint, $(A \cap B) \cap (A^c \cap B) = \emptyset$.

- **Step 2: Apply additivity axiom:**  
  By Axiom 3 (finite additivity):
  $$P(B) = P(A \cap B) + P(A^c \cap B)$$
  Subtracting $P(A \cap B)$ from both sides gives the difference identity:
  $$P(A^c \cap B) = P(B) - P(A \cap B)$$

- **Step 3: Substitute the independence condition:**  
  Since $A$ and $B$ are independent, substitute $P(A \cap B) = P(A)P(B)$:
  $$P(A^c \cap B) = P(B) - P(A)P(B)$$
  Factor out $P(B)$:
  $$P(A^c \cap B) = P(B)[1 - P(A)]$$
  By the complement rule, $1 - P(A) = P(A^c)$:
  $$P(A^c \cap B) = P(B) \cdot P(A^c) = P(A^c) \cdot P(B)$$

Because the joint probability of $A^c$ and $B$ factors into the product of their individual probabilities, $A^c$ and $B$ are statistically independent. $\blacksquare$

**Answer.**  
Proof established: $P(A^c \cap B) = P(B) - P(A)P(B) = P(B)(1 - P(A)) = P(A^c)P(B)$.

---

##### Exercise MMSA 2.88 (p. 92)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.5, p. 92, Exercise 88.  
**Classification:** MMSA — Test.  
**Relevant PT ID(s):** [PT-02](#problem-type-pt-02-multi-stage-sequential-intersection-via-the-general-multiplication--chain-rule), [PT-03](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics).

**Complete question statement.**  
- (a) A lumber company has just taken delivery on a lot of 10,000 $2 \times 4$ boards. Suppose that 20% of these boards (2000) are actually too green to be used in first-quality construction. Two boards are selected at random, one after the other. Let $A = \{\text{the first board is green}\}$ and $B = \{\text{the second board is green}\}$. Compute $P(A)$, $P(B)$, and $P(A \cap B)$ (a tree diagram might help). Are $A$ and $B$ independent?
- (b) With $A$ and $B$ independent and $P(A) = P(B) = 0.2$, what is $P(A \cap B)$? How much difference is there between this answer and $P(A \cap B)$ in part (a)? For purposes of calculating $P(A \cap B)$, can we assume that $A$ and $B$ of part (a) are independent to obtain essentially the correct probability?
- (c) Suppose the lot consists of ten boards, of which two are green. Does the assumption of independence now yield approximately the correct answer for $P(A \cap B)$? What is the critical difference between the situation here and that of part (a)? When do you think that an independence assumption would be valid in obtaining an approximately correct answer to $P(A \cap B)$?

**Complete working.**  
**(a) Lot of $N = 10,000$ boards with $2,000$ green ($G$) and $8,000$ non-green ($G^c$):**  
- First draw: $P(A) = \frac{2000}{10000} = 0.20$.
- Second draw probability $P(B)$ via Law of Total Probability:
  $$P(B) = P(B \mid A)P(A) + P(B \mid A^c)P(A^c)$$
  $$P(B \mid A) = \frac{1999}{9999}, \quad P(B \mid A^c) = \frac{2000}{9999}$$
  $$P(B) = \left(\frac{1999}{9999}\right)(0.20) + \left(\frac{2000}{9999}\right)(0.80) = \frac{399.8 + 1600}{9999} = \frac{1999.8}{9999} = \frac{2000}{10000} = 0.20$$
- Joint probability:
  $$P(A \cap B) = P(B \mid A) \cdot P(A) = \frac{1999}{9999} \times 0.20 = \frac{399.8}{9999} \approx 0.039983998$$
- Independence check:
  $$P(A) \cdot P(B) = 0.20 \times 0.20 = 0.040000$$
  Since $P(A \cap B) \approx 0.039984 \neq 0.040000$, strictly speaking $A$ and $B$ are **dependent (not independent)**.

**(b) Independence approximation:**  
Under assumed independence: $P(A \cap B) = 0.040000$.
Difference:
$$0.040000 - 0.039984 = 0.000016 \quad (0.0016\%)$$
This discrepancy is infinitesimal (a relative error of $0.04\%$). For all practical engineering and statistical calculations, we **can safely assume independence** when sampling 2 boards from a lot of 10,000.

**(c) Lot of $N = 10$ boards with $2$ green:**  
- True joint probability without replacement:
  $$P(A \cap B) = P(B \mid A)P(A) = \frac{1}{9} \times \frac{2}{10} = \frac{2}{90} = \frac{1}{45} \approx 0.022222$$
- Under assumed independence:
  $$P(A)P(B) = \frac{2}{10} \times \frac{2}{10} = 0.040000$$
- Comparison:
  The independence assumption yields $0.0400$, which is **$80\%$ higher** than the true value $0.0222$! The assumption does **not** yield approximately the correct answer.
- **Critical Difference & Rule of Thumb:**  
  The critical difference is the **sampling fraction** $n / N$:
  - In part (a), $n/N = 2 / 10,000 = 0.0002$ ($0.02\%$), so removing one board barely alters the remaining population composition ($1999/9999 \approx 0.19992 \approx 0.20$).
  - In part (c), $n/N = 2 / 10 = 0.20$ ($20\%$), so removing one green board cuts the concentration of green boards nearly in half ($1/9 \approx 0.111$ vs. $0.20$).
  **Statistical Rule of Thumb:** An independence assumption for sampling without replacement is practically valid whenever the sample size $n$ represents **less than 5% of the population** ($n/N \le 0.05$).

**Answer.**  
- (a) $P(A) = 0.20, P(B) = 0.20, P(A \cap B) = \frac{1999}{49995} \approx 0.03998$; Not independent.
- (b) With independence, $P(A \cap B) = 0.0400$; difference is $0.000016$; assumption is practically valid.
- (c) For $N=10$, true $= 0.0222$ vs. independent $= 0.0400$ (invalid); valid only when $n/N \le 0.05$.

---

### Subsection C.2: Probability with Applications and R (PAR)

#### PAR Basic Exercises

##### Exercise PAR 2.4 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.4.  
**Classification:** PAR — Basic.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
Suppose $P(A) = P(B) = 0.3$ and $P(A \mid B) = 0.5$. Find $P(A \cup B)$.

**Complete working.**  
First, apply the multiplication rule to calculate the joint intersection probability $P(A \cap B)$:
$$P(A \cap B) = P(A \mid B) \cdot P(B) = 0.5 \times 0.3 = 0.15$$
Next, apply the general addition rule for the union of two events:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
$$P(A \cup B) = 0.3 + 0.3 - 0.15 = 0.45$$

**Answer.**  
$P(A \cup B) = 0.45$.

---

##### Exercise PAR 2.9 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.9.  
**Classification:** PAR — Basic.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
Find a simple expression for $P(A \mid B)$ under the following conditions:
- (a) $A$ and $B$ are disjoint.
- (b) $A = B$.
- (c) $A$ implies $B$.
- (d) $B$ implies $A$.

**Complete working.**  
By definition, $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ (for $P(B) > 0$).
- **(a) $A$ and $B$ are disjoint ($A \cap B = \emptyset$):**  
  Since $A \cap B = \emptyset$, $P(A \cap B) = 0$.
  $$P(A \mid B) = \frac{0}{P(B)} = 0$$

- **(b) $A = B$:**  
  Since $A$ and $B$ are identical sets, $A \cap B = B$.
  $$P(A \mid B) = \frac{P(B)}{P(B)} = 1$$

- **(c) $A$ implies $B$ ($A \subseteq B$):**  
  In set theory, "$A$ implies $B$" means that whenever $A$ occurs, $B$ must occur, so $A$ is a subset of $B$ ($A \subseteq B$). Consequently, $A \cap B = A$.
  $$P(A \mid B) = \frac{P(A)}{P(B)}$$

- **(d) $B$ implies $A$ ($B \subseteq A$):**  
  "$B$ implies $A$" means that whenever $B$ occurs, $A$ must occur, so $B$ is a subset of $A$ ($B \subseteq A$). Consequently, $A \cap B = B$.
  $$P(A \mid B) = \frac{P(B)}{P(B)} = 1$$

**Answer.**  
- (a) $P(A \mid B) = 0$.
- (b) $P(A \mid B) = 1$.
- (c) $P(A \mid B) = \frac{P(A)}{P(B)}$.
- (d) $P(A \mid B) = 1$.

---

##### Exercise PAR 2.34 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.34.  
**Classification:** PAR — Basic.  
**Relevant PT ID(s):** [PT-03](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics).

**Complete question statement.**  
Suppose $A, B,$ and $C$ are independent events with respective probabilities $1/3, 1/4,$ and $1/5$. Find:
- (a) $P(ABC)$
- (b) $P(A \text{ or } B \text{ or } C)$
- (c) $P(AB \mid C)$
- (d) $P(B \mid AC)$
- (e) $P(\text{At most one of the three events occurs})$

**Complete working.**  
Given: $P(A) = 1/3$, $P(B) = 1/4$, $P(C) = 1/5$. The events are mutually independent.

- **(a) $P(ABC) = P(A \cap B \cap C)$:**  
  By mutual independence:
  $$P(ABC) = P(A) \cdot P(B) \cdot P(C) = \frac{1}{3} \times \frac{1}{4} \times \frac{1}{5} = \frac{1}{60} \approx 0.016667$$

- **(b) $P(A \cup B \cup C)$:**  
  Applying the complement rule with independent complements ($A^c, B^c, C^c$ are mutually independent):
  $$P(A \cup B \cup C) = 1 - P(A^c B^c C^c) = 1 - [P(A^c)P(B^c)P(C^c)]$$
  $$P(A^c) = 1 - \frac{1}{3} = \frac{2}{3}, \quad P(B^c) = 1 - \frac{1}{4} = \frac{3}{4}, \quad P(C^c) = 1 - \frac{1}{5} = \frac{4}{5}$$
  $$P(A^c B^c C^c) = \frac{2}{3} \times \frac{3}{4} \times \frac{4}{5} = \frac{2}{5}$$
  $$P(A \cup B \cup C) = 1 - \frac{2}{5} = \frac{3}{5} = 0.60$$

- **(c) $P(AB \mid C)$:**  
  Because $A, B,$ and $C$ are mutually independent, the compound event $AB = A \cap B$ is statistically independent of event $C$.  
  $$P(AB \mid C) = P(AB) = P(A) \cdot P(B) = \frac{1}{3} \times \frac{1}{4} = \frac{1}{12} \approx 0.083333$$
  *(Formally: $\frac{P(A \cap B \cap C)}{P(C)} = \frac{1/60}{1/5} = \frac{5}{60} = \frac{1}{12}$)*

- **(d) $P(B \mid AC)$:**  
  By mutual independence, event $B$ is independent of the compound event $AC = A \cap C$:
  $$P(B \mid AC) = P(B) = \frac{1}{4} = 0.25$$
  *(Formally: $\frac{P(A \cap B \cap C)}{P(A \cap C)} = \frac{1/60}{(1/3)(1/5)} = \frac{1/60}{1/15} = \frac{15}{60} = \frac{1}{4}$)*

- **(e) $P(\text{At most one occurs})$:**  
  "At most one" means either zero events occur or exactly one event occurs.
  1. *Zero events occur:* $P(A^c B^c C^c) = \frac{2}{5} = \frac{24}{60}$.
  2. *Exactly one event occurs:* Partition into three disjoint outcomes:
     - $A$ only: $P(A B^c C^c) = \frac{1}{3} \times \frac{3}{4} \times \frac{4}{5} = \frac{12}{60}$.
     - $B$ only: $P(A^c B C^c) = \frac{2}{3} \times \frac{1}{4} \times \frac{4}{5} = \frac{8}{60}$.
     - $C$ only: $P(A^c B^c C) = \frac{2}{3} \times \frac{3}{4} \times \frac{1}{5} = \frac{6}{60}$.
     Sum for exactly one: $\frac{12 + 8 + 6}{60} = \frac{26}{60}$.
  Summing zero and exactly one:
  $$P(\text{At most one}) = \frac{24}{60} + \frac{26}{60} = \frac{50}{60} = \frac{5}{6} \approx 0.833333$$

**Answer.**  
- (a) $P(ABC) = \frac{1}{60} \approx 0.0167$.
- (b) $P(A \cup B \cup C) = \frac{3}{5} = 0.60$.
- (c) $P(AB \mid C) = \frac{1}{12} \approx 0.0833$.
- (d) $P(B \mid AC) = \frac{1}{4} = 0.25$.
- (e) $P(\text{At most one}) = \frac{5}{6} \approx 0.8333$.

---

##### Exercise PAR 3.1 (Ch. 3, p. 118)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 3, p. 118, Exercise 3.1.  
**Classification:** PAR — Basic.  
**Relevant PT ID(s):** [PT-09](#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping).

**Complete question statement.**  
Your friend missed probability class today. Explain to your friend, in simple language, what a random variable is.

**Complete working.**  
*Plain-Language Conceptual Explanation:*  
A random variable is not a single number, nor is it "random" in the sense of being unpredictable chaos. It is a **translator (or mathematical function)** that takes the real-world outcome of a chance experiment and turns it into a clear, usable number. 

Before we use random variables, experimental outcomes can be messy descriptions, words, or lists of physical events—like "coin landed heads", "patient recovered in 4 days", or "traffic light was red". A random variable creates a standard rule: it looks at what happened and assigns a specific numerical value. For example, if you toss three coins, the random variable $X$ might be defined as "the total number of heads." If the result is Tails-Heads-Heads, the random variable translates that qualitative outcome into the number $2$. 

Once outcomes are turned into numbers, we can use algebra and calculus to compute averages (expectations), quantify risk (variance), and graph probability distributions.

**Answer.**  
A random variable is a mathematical rule (function) that assigns a specific numerical value to each outcome of a random experiment, translating qualitative outcomes into real numbers for mathematical analysis.

---

##### Shared Italicized Instructions for PAR 3.2–3.5
> *Textbook Instruction (PAR p. 118):*  
> **"For the following problems 3.2–3.5, identify and define the random variable of interest. Then, express the probability in question in terms of the defined random variable, but do not compute the probability."**

---

##### Exercise PAR 3.2 (Ch. 3, p. 118)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 3, p. 118, Exercise 3.2.  
**Classification:** PAR — Basic.  
**Relevant PT ID(s):** [PT-09](#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping).

**Complete question statement.**  
*(Subject to shared instruction above)*  
Roll four dice. Consider the probability of getting all fives.

**Complete working.**  
- **Identification and definition of Random Variable:**  
  Let $X$ denote the number of dice that show the face value 5 among the four rolled dice.  
  The support of $X$ is $\mathcal{X} = \{0, 1, 2, 3, 4\}$.
- **Expressed probability in terms of $X$:**  
  Getting "all fives" means every one of the 4 dice lands on 5, which corresponds to the event:
  $$P(X = 4)$$

**Answer.**  
Random variable: Let $X =$ number of fives rolled. Expressed probability: $P(X = 4)$.

---

##### Exercise PAR 3.3 (Ch. 3, p. 118)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 3, p. 118, Exercise 3.3.  
**Classification:** PAR — Basic.  
**Relevant PT ID(s):** [PT-09](#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping).

**Complete question statement.**  
*(Subject to shared instruction above)*  
A pizza shop offers three toppings: pineapple, peppers, and pepperoni. A pizza can have 0, 1, 2, or 3 toppings. Consider the probability that a random customer asks for two toppings.

**Complete working.**  
- **Identification and definition of Random Variable:**  
  Let $T$ denote the number of toppings requested by a randomly selected customer.  
  The support of $T$ is $\mathcal{T} = \{0, 1, 2, 3\}$.
- **Expressed probability in terms of $T$:**  
  The event that a customer asks for two toppings corresponds to:
  $$P(T = 2)$$

**Answer.**  
Random variable: Let $X$ (or $T$) = number of toppings requested. Expressed probability: $P(X = 2)$ (matching Textbook Solutions: *'Let X be the number of toppings. P(X = 2)'*).

---

##### Exercise PAR 3.4 (Ch. 3, p. 118)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 3, p. 118, Exercise 3.4.  
**Classification:** PAR — Basic.  
**Relevant PT ID(s):** [PT-09](#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping).

**Complete question statement.**  
*(Subject to shared instruction above)*  
Bored one day, you decide to play the video game Angry Birds until you win. Every time you lose, you start over. Consider the probability that you win in less than 1000 tries.

**Complete working.**  
- **Identification and definition of Random Variable:**  
  Let $N$ denote the total number of tries (attempts) required to achieve the first win.  
  The support of $N$ is $\mathcal{N} = \{1, 2, 3, 4, \dots\} = \mathbb{Z}^+$. (This is a geometric random variable).
- **Expressed probability in terms of $N$:**  
  The event that the first win occurs in strictly less than 1000 tries is expressed as:
  $$P(N < 1000) \quad \text{or equivalently for discrete counts, } P(N \le 999)$$

**Answer.**  
Random variable: Let $N =$ number of tries until the first win. Expressed probability: $P(N < 1000)$ (or $P(N \le 999)$).

---

##### Exercise PAR 3.5 (Ch. 3, p. 118)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 3, p. 118, Exercise 3.5.  
**Classification:** PAR — Basic.  
**Relevant PT ID(s):** [PT-09](#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping).

**Complete question statement.**  
*(Subject to shared instruction above)*  
In Julia's garden, there is a 3% chance that a tomato will be bad. Julia harvests 100 tomatoes and wants to know the probability that at most five tomatoes are bad.

**Complete working.**  
- **Identification and definition of Random Variable:**  
  Let $B$ denote the total number of bad tomatoes among the 100 harvested tomatoes.  
  The support of $B$ is $\mathcal{B} = \{0, 1, 2, \dots, 100\}$. (This is a binomial random variable).
- **Expressed probability in terms of $B$:**  
  The event that "at most five tomatoes are bad" is expressed as:
  $$P(B \le 5)$$

**Answer.**  
Random variable: Let $B =$ number of bad tomatoes out of 100 harvested. Expressed probability: $P(B \le 5)$.

---

##### Exercise PAR 3.6 (Ch. 3, p. 118)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 3, p. 118, Exercise 3.6.  
**Classification:** PAR — Basic.  
**Relevant PT ID(s):** [PT-10](#problem-type-pt-10-pmf-normalization-parameter-determination-and-validation).

**Complete question statement.**  
Suppose $X$ is a random variable that takes values on $\{0, 0.01, 0.02, \dots, 0.99, 1\}$. If each outcome is equally likely, find:
- (a) $P(X \le 0.33)$
- (b) $P(0.55 \le X \le 0.66)$

**Complete working.**  
The support $\mathcal{X}$ contains the values $k / 100$ for integers $k \in \{0, 1, 2, \dots, 100\}$.
Total number of support points:
$$N = 100 - 0 + 1 = 101 \text{ points}$$
Since all outcomes are equally likely, the probability mass function is uniform:
$$P(X = x) = \frac{1}{101} \quad \forall x \in \mathcal{X}$$

- **(a) $P(X \le 0.33)$:**  
  The condition $X \le 0.33$ corresponds to integers $k \in \{0, 1, 2, \dots, 33\}$.  
  The number of favorable support points is $33 - 0 + 1 = 34$.
  $$P(X \le 0.33) = \frac{34}{101} \approx 0.336634$$

- **(b) $P(0.55 \le X \le 0.66)$:**  
  The condition $0.55 \le X \le 0.66$ corresponds to integers $k \in \{55, 56, \dots, 66\}$.  
  The number of favorable support points is $66 - 55 + 1 = 12$.
  $$P(0.55 \le X \le 0.66) = \frac{12}{101} \approx 0.118812$$

**Answer.**  
- (a) $P(X \le 0.33) = \frac{34}{101} \approx 0.3366$.
- (b) $P(0.55 \le X \le 0.66) = \frac{12}{101} \approx 0.1188$.

---

##### Exercise PAR 3.7 (Ch. 3, p. 118)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 3, p. 118, Exercise 3.7.  
**Classification:** PAR — Basic.  
**Relevant PT ID(s):** [PT-09](#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping).

**Complete question statement.**  
Suppose $X$ is a random variable that takes values on all positive integers ($\mathcal{X} = \{1, 2, 3, 4, \dots\} = \mathbb{Z}^+$). Let $A = \{2 \le X \le 4\}$ and $B = \{X \ge 4\}$. Describe the events:
- (i) $A^c$
- (ii) $B^c$
- (iii) $AB$ ($A \cap B$)
- (iv) $A \cup B$

**Complete working.**  
Given universe of values: $\mathcal{X} = \{1, 2, 3, 4, 5, \dots\}$.
- $A = \{2 \le X \le 4\} = \{2, 3, 4\}$.
- $B = \{X \ge 4\} = \{4, 5, 6, 7, \dots\}$.

- **(i) Event $A^c$:**  
  The complement consists of all positive integers strictly less than 2 or strictly greater than 4:
  $$A^c = \{X = 1\} \cup \{X \ge 5\} = \{1, 5, 6, 7, \dots\}$$

- **(ii) Event $B^c$:**  
  The complement consists of all positive integers strictly less than 4:
  $$B^c = \{X < 4\} = \{X \le 3\} = \{1, 2, 3\}$$

- **(iii) Event $AB = A \cap B$:**  
  The intersection contains support points common to both $\{2, 3, 4\}$ and $\{4, 5, 6, \dots\}$:
  $$A \cap B = \{X = 4\} = \{4\}$$

- **(iv) Event $A \cup B$:**  
  The union combines all support points present in at least one set:
  $$A \cup B = \{2, 3, 4\} \cup \{4, 5, 6, \dots\} = \{X \ge 2\} = \{2, 3, 4, 5, \dots\}$$

**Answer.**  
- (i) $A^c = \{1, 5, 6, 7, \dots\} = \{X = 1\} \cup \{X \ge 5\}$.
- (ii) $B^c = \{1, 2, 3\} = \{X \le 3\}$.
- (iii) $AB = \{4\} = \{X = 4\}$.
- (iv) $A \cup B = \{2, 3, 4, 5, \dots\} = \{X \ge 2\}$.

---

#### PAR Medium Exercises

##### Exercise PAR 2.5 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.5.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
Suppose $P(A) = P(B) = p_1$ and $P(A \cup B) = p_2$. Find $P(A \mid B)$.

**Complete working.**  
By the addition rule for the union of two events:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
Substitute the given algebraic quantities:
$$p_2 = p_1 + p_1 - P(A \cap B) = 2p_1 - P(A \cap B)$$
Isolating the joint intersection probability:
$$P(A \cap B) = 2p_1 - p_2$$
Now apply the definition of conditional probability:
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{2p_1 - p_2}{p_1} = 2 - \frac{p_2}{p_1} \quad (\text{provided } p_1 > 0)$$

*Boundary Check:* Since $A \cap B \subseteq B$, $2p_1 - p_2 \le p_1 \implies p_2 \ge p_1$. Furthermore, $P(A \cap B) \ge 0 \implies p_2 \le 2p_1$. These conditions guarantee $0 \le P(A \mid B) \le 1$.

**Answer.**  
$P(A \mid B) = \frac{2p_1 - p_2}{p_1} = 2 - \frac{p_2}{p_1}$.

---

##### Exercise PAR 2.7 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.7.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
A total of 108 students filled out a survey for a psychology class project. A total of 36 students indicated they were athletes. Of those students, 21 said they preferred to work out in the morning as opposed to the afternoon. For the nonathletes, 25 said they preferred to work out in the morning. Find the following probabilities for a randomly selected student who took the survey:
- (a) $P(\text{Athlete given prefer morning workout})$
- (b) $P(\text{Prefer morning workout given nonathlete})$
- (c) $P(\text{Nonathlete given prefer nonmorning workout})$

**Complete working.**  
Total students $N = 108$.
Let $A$ be Athlete ($n(A) = 36$), so Nonathletes $n(A^c) = 108 - 36 = 72$.
Let $M$ be Prefer Morning Workout:
- Among 36 athletes: $n(A \cap M) = 21$, so $n(A \cap M^c) = 36 - 21 = 15$.
- Among 72 nonathletes: $n(A^c \cap M) = 25$, so $n(A^c \cap M^c) = 72 - 25 = 47$.

Marginal workout preference totals:
- Total preferring morning ($M$): $n(M) = 21 + 25 = 46$.
- Total preferring non-morning ($M^c$): $n(M^c) = 15 + 47 = 62$.
Sum check: $46 + 62 = 108$.

- **(a) $P(\text{Athlete} \mid \text{Morning}) = P(A \mid M)$:**  
  Restricting to morning workout column ($n(M) = 46$):
  $$P(A \mid M) = \frac{n(A \cap M)}{n(M)} = \frac{21}{46} \approx 0.456522$$

- **(b) $P(\text{Morning} \mid \text{Nonathlete}) = P(M \mid A^c)$:**  
  Restricting to nonathlete row ($n(A^c) = 72$):
  $$P(M \mid A^c) = \frac{n(A^c \cap M)}{n(A^c)} = \frac{25}{72} \approx 0.347222$$

- **(c) $P(\text{Nonathlete} \mid \text{Nonmorning}) = P(A^c \mid M^c)$:**  
  Restricting to non-morning column ($n(M^c) = 62$):
  $$P(A^c \mid M^c) = \frac{n(A^c \cap M^c)}{n(M^c)} = \frac{47}{62} \approx 0.758065$$

**Answer.**  
- (a) $P(A \mid M) = \frac{21}{46} \approx 0.4565$ (45.65%).
- (b) $P(M \mid A^c) = \frac{25}{72} \approx 0.3472$ (34.72%).
- (c) $P(A^c \mid M^c) = \frac{47}{62} \approx 0.7581$ (75.81%).

---

##### Exercise PAR 2.11 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.11.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction), Conceptual Foundations.

**Complete question statement.**  
True or False. Either show the statement to be true for any event $A$ and $B$ (with $0 < P(B) < 1$) or exhibit a counterexample:
- (a) $P(A \mid B) + P(A \mid B^c) = 1$.
- (b) $P(A \mid B) + P(A^c \mid B) = 1$.

**Complete working.**  
- **(a) Analysis of $P(A \mid B) + P(A \mid B^c) = 1$:**  
  **FALSE.**  
  *Proof by Counterexample:*  
  Let the experiment be rolling a fair 6-sided die, $\Omega = \{1, 2, 3, 4, 5, 6\}$.  
  Let $A = \Omega$ (the certain event, $P(A) = 1$).  
  Let $B = \{1, 2\}$, so $B^c = \{3, 4, 5, 6\}$.  
  Then $P(A \mid B) = 1$ and $P(A \mid B^c) = 1$.  
  Sum $= 1 + 1 = 2 \neq 1$.  
  *Alternative Non-Trivial Counterexample:*  
  Let $A$ and $B$ be independent events with $P(A) = 0.20$ and $P(B) = 0.50$.  
  By independence, $P(A \mid B) = P(A) = 0.20$, and $P(A \mid B^c) = P(A) = 0.20$.  
  Sum $= 0.20 + 0.20 = 0.40 \neq 1$.

- **(b) Analysis of $P(A \mid B) + P(A^c \mid B) = 1$:**  
  **TRUE.**  
  *General Analytical Proof:*  
  By definition of conditional probability:
  $$P(A \mid B) + P(A^c \mid B) = \frac{P(A \cap B)}{P(B)} + \frac{P(A^c \cap B)}{P(B)} = \frac{P(A \cap B) + P(A^c \cap B)}{P(B)}$$
  Notice that $A \cap B$ and $A^c \cap B$ are disjoint sets because $A \cap A^c = \emptyset$.  
  Their union is:
  $$(A \cap B) \cup (A^c \cap B) = (A \cup A^c) \cap B = \Omega \cap B = B$$
  By Kolmogorov Axiom 3 (finite additivity):
  $$P(A \cap B) + P(A^c \cap B) = P((A \cap B) \cup (A^c \cap B)) = P(B)$$
  Substituting this into the numerator:
  $$\frac{P(B)}{P(B)} = 1$$
  Thus, the identity holds universally for any event $A$ and any event $B$ with $P(B) > 0$. $\blacksquare$

**Answer.**  
- (a) **False** (Counterexample: if $A$ and $B$ are independent with $P(A) = 0.2$, sum is $0.4 \neq 1$).
- (b) **True** (Proven: $(A \cap B) \cup (A^c \cap B) = B \implies \frac{P(B)}{P(B)} = 1$).

---

##### Exercise PAR 2.16 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.16.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** [PT-02](#problem-type-pt-02-multi-stage-sequential-intersection-via-the-general-multiplication--chain-rule).

**Complete question statement.**  
Suppose $P(A) = 1/2$, $P(B^c \mid AC) = 1/3$, and $P(C \mid A) = 1/4$. Find $P(ABC)$ ($P(A \cap B \cap C)$).

**Complete working.**  
First, apply the complement rule within the conditioned space $AC = A \cap C$:
$$P(B \mid AC) = 1 - P(B^c \mid AC) = 1 - \frac{1}{3} = \frac{2}{3}$$
Next, apply the Chain Rule for three events:
$$P(ABC) = P(A \cap B \cap C) = P(A) \cdot P(C \mid A) \cdot P(B \mid A \cap C)$$
Substitute the given and derived probabilities:
$$P(ABC) = \frac{1}{2} \times \frac{1}{4} \times \frac{2}{3} = \frac{2}{24} = \frac{1}{12} \approx 0.083333$$

**Answer.**  
$P(ABC) = \frac{1}{12} \approx 0.0833$.

---

##### Exercise PAR 2.21 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.21.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** [PT-05](#problem-type-pt-05-total-probability-computation-via-partition-decompositions-and-tree-diagrams).

**Complete question statement.**  
Maya has two bags of candy. The first bag contains two packs of M&Ms and three packs of Gummi Bears. The second bag contains four packs of M&Ms and two packs of Gummi Bears. Maya chooses a bag uniformly at random and then picks a pack of candy. What is the probability that the pack chosen is Gummi Bears? Solve (i) by using a tree diagram and (ii) by another method.

**Complete working.**  
Bag compositions:
- Bag 1 ($B_1$): 2 M&Ms, 3 Gummi Bears. Total $= 5$.
- Bag 2 ($B_2$): 4 M&Ms, 2 Gummi Bears. Total $= 6$.
Bag selection: Uniform at random $\implies P(B_1) = 1/2$, $P(B_2) = 1/2$.
Let $G$ be the event that Gummi Bears are selected.
- Conditional rates: $P(G \mid B_1) = 3/5$, $P(G \mid B_2) = 2/6 = 1/3$.

- **(i) Method 1: Tree Diagram:**  
  - Branch 1: Choose Bag 1 ($1/2$) $\to$ Choose Gummi Bears ($3/5$).  
    Joint path probability $= \frac{1}{2} \times \frac{3}{5} = \frac{3}{10} = \frac{9}{30}$.
  - Branch 2: Choose Bag 2 ($1/2$) $\to$ Choose Gummi Bears ($2/6 = 1/3$).  
    Joint path probability $= \frac{1}{2} \times \frac{1}{3} = \frac{1}{6} = \frac{5}{30}$.
  Summing the terminal Gummi Bear leaf nodes:
  $$P(G) = \frac{9}{30} + \frac{5}{30} = \frac{14}{30} = \frac{7}{15} \approx 0.466667$$

- **(ii) Method 2: Analytical Law of Total Probability:**  
  Using the binary partition $\{B_1, B_2\}$:
  $$P(G) = P(G \mid B_1)P(B_1) + P(G \mid B_2)P(B_2)$$
  $$P(G) = \left(\frac{3}{5}\right)\left(\frac{1}{2}\right) + \left(\frac{2}{6}\right)\left(\frac{1}{2}\right) = \frac{3}{10} + \frac{1}{6} = \frac{9 + 5}{30} = \frac{14}{30} = \frac{7}{15}$$

**Answer.**  
$P(\text{Gummi Bears}) = \frac{7}{15} \approx 0.4667$ (46.67%).

---

##### Exercise PAR 2.27 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.27.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** [PT-05](#problem-type-pt-05-total-probability-computation-via-partition-decompositions-and-tree-diagrams).

**Complete question statement.**  
In a certain population of youth, the probability of being a smoker is 20%. The probability that at least one parent is a smoker is 30%. And if at least one parent is a smoker, the probability of being a smoker is 35%. Find the probability of being a smoker if neither parent is a smoker.

**Complete working.**  
Define events:
- $S$: Youth is a smoker $\implies P(S) = 0.20$.
- $A$: At least one parent is a smoker $\implies P(A) = 0.30$.
- $A^c$: Neither parent is a smoker $\implies P(A^c) = 1 - 0.30 = 0.70$.
- Conditional probability: $P(S \mid A) = 0.35$.

We seek $P(S \mid A^c)$.
The events $\{A, A^c\}$ partition the parental smoking status. Applying the Law of Total Probability:
$$P(S) = P(S \mid A)P(A) + P(S \mid A^c)P(A^c)$$
Substitute the known values into the equation:
$$0.20 = (0.35 \times 0.30) + P(S \mid A^c) \times 0.70$$
$$0.20 = 0.105 + 0.70 \, P(S \mid A^c)$$
Isolate $P(S \mid A^c)$:
$$0.70 \, P(S \mid A^c) = 0.20 - 0.105 = 0.095$$
$$P(S \mid A^c) = \frac{0.095}{0.70} = \frac{95}{700} = \frac{19}{140} \approx 0.135714$$

**Answer.**  
$P(S \mid A^c) = \frac{19}{140} \approx 0.1357$ (13.57%).

---

##### Exercise PAR 2.28 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.28.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** [PT-08](#problem-type-pt-08-diagnostic-screening-evaluation-and-base-rate-fallacy-analysis).

**Complete question statement.**  
According to the National Cancer Institute, for women aged 50, there is a 2.38% risk (probability) of being diagnosed with breast cancer. Screening mammography has a sensitivity of about 85% for women aged 50, and a 95% specificity. That is, the false-negative rate is 15% and the false-positive rate is 5%. If a woman aged 50 has a mammogram, and it comes back positive for breast cancer, what is the probability that she has the disease?

**Complete working.**  
Define events:
- $C$: Woman has breast cancer.
- $C^c$: Woman does not have breast cancer.
- $+$: Mammogram result is positive.

Parameters:
- Prevalence: $P(C) = 0.0238 \implies P(C^c) = 1 - 0.0238 = 0.9762$.
- Sensitivity: $P(+ \mid C) = 0.85$.
- Specificity: $P(- \mid C^c) = 0.95 \implies \text{False Positive Rate } P(+ \mid C^c) = 0.05$.

We seek the Positive Predictive Value $P(C \mid +)$.
- **Step 1: Total probability of positive mammogram ($P(+)$):**  
  Applying the Law of Total Probability:
  $$P(+) = P(+ \mid C)P(C) + P(+ \mid C^c)P(C^c)$$
  $$P(+) = (0.85 \times 0.0238) + (0.05 \times 0.9762)$$
  $$P(+) = 0.02023 + 0.04881 = 0.06904$$

- **Step 2: Invert via Bayes' Rule:**  
  $$P(C \mid +) = \frac{P(+ \mid C)P(C)}{P(+)} = \frac{0.02023}{0.06904} = \frac{2023}{6904} \approx 0.293019$$

*Interpretation:* Despite high sensitivity (85%) and specificity (95%), a positive mammogram for a 50-year-old woman yields only a $29.30\%$ posterior probability of cancer, because false positives from the healthy 97.6% majority outnumber true positives by more than 2 to 1.

**Answer.**  
$P(C \mid +) = \frac{2023}{6904} \approx 0.2930$ (29.30%).

---

##### Exercise PAR 2.30 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.30.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** [PT-07](#problem-type-pt-07-posterior-probability-inversion-via-bayes-rule).

**Complete question statement.**  
An eyewitness observes a hit-and-run accident in New York City, where 95% of the cabs are yellow and 5% are blue. The witness asserts the cab was blue. Police experts believe that eyewitnesses are 80% reliable. That is, an eyewitness will correctly identify the color of a cab 80% of the time. What is the probability that the cab actually was blue?

**Complete working.**  
Define events:
- Cab colors: $B = \{\text{cab is Blue}\}$, $Y = \{\text{cab is Yellow}\}$.
  Priors: $P(B) = 0.05, P(Y) = 0.95$.
- Witness testimony: $W_B = \{\text{witness asserts cab is Blue}\}$.
- Witness reliability (80%):
  $P(W_B \mid B) = 0.80$ (correct identification)
  $P(W_B \mid Y) = 0.20$ (misidentifying a yellow cab as blue)

We seek $P(B \mid W_B)$.
- **Step 1: Total probability that witness reports blue ($P(W_B)$):**  
  Applying the Law of Total Probability:
  $$P(W_B) = P(W_B \mid B)P(B) + P(W_B \mid Y)P(Y)$$
  $$P(W_B) = (0.80 \times 0.05) + (0.20 \times 0.95) = 0.040 + 0.190 = 0.230$$

- **Step 2: Invert via Bayes' Rule:**  
  $$P(B \mid W_B) = \frac{P(W_B \mid B)P(B)}{P(W_B)} = \frac{0.040}{0.230} = \frac{4}{23} \approx 0.173913$$

*Interpretation:* Although the witness is 80% accurate, because yellow cabs are so dominant (95%), the witness is actually more than 4 times as likely to have mistakenly called a yellow cab blue ($0.19$) than to have correctly seen a blue cab ($0.04$). The probability the cab was blue is only $17.39\%$.

**Answer.**  
$P(B \mid W_B) = \frac{4}{23} \approx 0.1739$ (17.39%).

---

##### Exercise PAR 2.35 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.35.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** [PT-03](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics).

**Complete question statement.**  
There is a 70% chance that a tree is infected with either root rot or bark disease. The chance that it does not have bark disease is 0.4. Whether or not a tree has root rot is independent of whether it has bark disease. Find the probability that a tree has root rot.

**Complete working.**  
Let $R$ be the event that the tree has root rot, and $B$ be the event that the tree has bark disease.
Given:
- $P(R \cup B) = 0.70$
- $P(B^c) = 0.40 \implies P(B) = 1 - 0.40 = 0.60$
- $R$ and $B$ are statistically independent ($R \perp B$)

By the complement rule and De Morgan's Law:
$$P((R \cup B)^c) = P(R^c \cap B^c) = 1 - P(R \cup B) = 1 - 0.70 = 0.30$$
By the Independence of Complements Theorem, since $R \perp B$, their complements are also independent ($R^c \perp B^c$):
$$P(R^c \cap B^c) = P(R^c) \cdot P(B^c)$$
Substitute the known values:
$$0.30 = P(R^c) \times 0.40 \implies P(R^c) = \frac{0.30}{0.40} = 0.75$$
Applying the complement rule to find $P(R)$:
$$P(R) = 1 - P(R^c) = 1 - 0.75 = 0.25$$

*Verification via Addition Rule:*
$$P(R \cup B) = P(R) + P(B) - P(R \cap B) = 0.25 + 0.60 - (0.25 \times 0.60) = 0.85 - 0.15 = 0.70$$
Matches given information exactly.

**Answer.**  
$P(R) = 0.25$ (25.0%).

---

##### Exercise PAR 2.38 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.38.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** Classical Probability & Sample Space Partitioning.

**Complete question statement.**  
A lottery will be held. From 1000 numbers, one will be chosen as the winner. Each lottery ticket is a number between 1 and 1000. How many tickets do you need to buy in order for the probability of winning to be at least 50%?

**Complete working.**  
The sample space consists of $N = 1000$ equally likely winning numbers.
If a participant buys $k$ distinct tickets ($1 \le k \le 1000$), the event of winning $W$ is the union of the $k$ distinct ticket numbers. Since the ticket numbers are mutually exclusive single-number outcomes:
$$P(W) = \frac{k}{1000}$$
We require:
$$P(W) \ge 0.50 \implies \frac{k}{1000} \ge 0.50 \implies k \ge 500$$
To guarantee a probability of at least $50\%$, you must purchase at least 500 distinct tickets.

**Answer.**  
$500$ tickets.

---

##### Exercise PAR 2.39 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.39.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** Classical Probability & Sample Space Partitioning.

**Complete question statement.**  
A local church is holding a bake sale which includes a cake raffle. One cake will be raffled off based on raffle ticket numbers from 1 to 30. How many tickets do you need to buy in order for the probability of winning the cake to be at least 25%?

**Complete working.**  
There are two mathematical formulations for this problem depending on the underlying ticket model:

1. **Textbook Solutions Manual Model (Independent Bernoulli / Sampling with Replacement):**  
   If buying each ticket provides an independent $1/30$ chance of holding a winning draw (the standard textbook modeling assumption in Wagaman Chapter 2 Solutions, p. 511):
   The probability of not winning with a single ticket is $1 - 1/30 = 29/30$.  
   For $k$ tickets, the probability of winning at least once is:
   $$P(	ext{Win}) = 1 - \left(rac{29}{30}ight)^k$$
   We require $P(	ext{Win}) \ge 0.25$:
   $$1 - \left(rac{29}{30}ight)^k \ge 0.25 \implies \left(rac{29}{30}ight)^k \le 0.75$$
   Taking natural logarithms:
   $$k \ln\left(rac{29}{30}ight) \le \ln(0.75) \implies k(-0.033902) \le -0.287682$$
   $$k \ge rac{-0.287682}{-0.033902} pprox 8.485$$
   Since $k$ must be an integer:
   $$k = \lceil 8.485 ceil = 9$$

2. **Finite Fixed-Batch Model (Sampling without Replacement from 30 Unique Tickets):**  
   If the church sells exactly 30 unique physical tickets and draws 1 winner without replacement:
   $$P(	ext{Win}) = rac{k}{30} \ge 0.25 \implies k \ge 30 	imes 0.25 = 7.5 \implies k = 8$$

**Answer.**  
**Textbook Answer Key (p. 511):** **$9$ tickets** (derived from the textbook's independent model $1 - (29/30)^k \ge 0.25$).  
*(Alternative note: If buying $k$ unique tickets from a fixed pool of 30 without replacement, $k = \lceil 7.5 ceil = 8$ tickets).*

---

#### PAR Test Exercises
*(Note: Preserving exact course screenshot sequence: #17, 23, 26, 29, 31, 33, 32, 36 — specifically #33 before #32).*

##### Exercise PAR 2.17 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.17.  
**Classification:** PAR — Test.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction), Theoretical Proofs.

**Complete question statement.**  
Prove the addition rule for conditional probabilities. That is, show that for events $A, B,$ and $C$ (with $P(C) > 0$):
$$P(A \cup B \mid C) = P(A \mid C) + P(B \mid C) - P(AB \mid C)$$

**Complete working.**  
- **Step 1: Expand conditional definition:**  
  By definition of conditional probability:
  $$P(A \cup B \mid C) = \frac{P((A \cup B) \cap C)}{P(C)}$$

- **Step 2: Apply set distributive law:**  
  Distribute intersection with $C$ across the union:
  $$(A \cup B) \cap C = (A \cap C) \cup (B \cap C)$$

- **Step 3: Apply unconditional addition rule:**  
  Let $E_1 = A \cap C$ and $E_2 = B \cap C$. By the standard addition rule for unconditional probabilities:
  $$P(E_1 \cup E_2) = P(E_1) + P(E_2) - P(E_1 \cap E_2)$$
  Notice that:
  $$E_1 \cap E_2 = (A \cap C) \cap (B \cap C) = A \cap B \cap C = AB \cap C$$
  Therefore:
  $$P((A \cup B) \cap C) = P(A \cap C) + P(B \cap C) - P(AB \cap C)$$

- **Step 4: Divide by $P(C)$:**  
  $$P(A \cup B \mid C) = \frac{P(A \cap C) + P(B \cap C) - P(AB \cap C)}{P(C)} = \frac{P(A \cap C)}{P(C)} + \frac{P(B \cap C)}{P(C)} - \frac{P(AB \cap C)}{P(C)}$$
  By definition, these ratios are $P(A \mid C), P(B \mid C),$ and $P(AB \mid C)$:
  $$P(A \cup B \mid C) = P(A \mid C) + P(B \mid C) - P(AB \mid C)$$
  $\blacksquare$

**Answer.**  
Proof established algebraically by distributing $(A \cup B) \cap C = (A \cap C) \cup (B \cap C)$ and applying the unconditional addition rule divided by $P(C)$.

---

##### Exercise PAR 2.23 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.23.  
**Classification:** PAR — Test.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
Give a formula for $P(A \mid B^c)$ in terms of $P(A), P(B),$ and $P(AB)$ only.

**Complete working.**  
By the definition of conditional probability:
$$P(A \mid B^c) = \frac{P(A \cap B^c)}{P(B^c)}$$
1. Express the denominator using the complement rule:
   $$P(B^c) = 1 - P(B)$$
2. Express the numerator using the difference rule:
   Since $A = (A \cap B) \cup (A \cap B^c)$ where the sets are disjoint:
   $$P(A) = P(A \cap B) + P(A \cap B^c) \implies P(A \cap B^c) = P(A) - P(A \cap B) = P(A) - P(AB)$$
3. Substitute these two expressions:
   $$P(A \mid B^c) = \frac{P(A) - P(AB)}{1 - P(B)}$$

**Answer.**  
$P(A \mid B^c) = \frac{P(A) - P(AB)}{1 - P(B)}$.

---

##### Exercise PAR 2.26 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.26.  
**Classification:** PAR — Test.  
**Relevant PT ID(s):** [PT-06](#problem-type-pt-06-first-step-analysis-and-recursive-conditioning).

**Complete question statement.**  
Consider flipping coins until either two heads $HH$ or heads then tails $HT$ first occurs. By conditioning on the first coin toss, find the probability that $HT$ occurs before $HH$.

**Complete working.**  
Let $E$ be the event that sequence $HT$ occurs before sequence $HH$. Let $p = P(E)$.
Condition on the outcome of the very first coin toss $T_1 \in \{H, T\}$, where $P(T_1 = H) = 1/2$ and $P(T_1 = T) = 1/2$.
By the Law of Total Probability:
$$p = P(E \mid T_1 = H) \cdot P(T_1 = H) + P(E \mid T_1 = T) \cdot P(T_1 = T)$$

- **Case 1: First toss is Tails ($T_1 = T$):**  
  Both target patterns ($HT$ and $HH$) begin with an initial $H$. Any sequence of initial tails ($T, TT, TTT, \dots$) can never contribute to either pattern. The experiment simply resets until the first $H$ is flipped.
  $$P(E \mid T_1 = T) = p$$

- **Case 2: First toss is Heads ($T_1 = H$):**  
  Now look at the immediate second coin toss $T_2 \in \{H, T\}$:
  - If $T_2 = T$, the full sequence generated so far is $HT$. The target $HT$ has occurred before $HH$ can ever form!  
    Thus, $P(E \mid T_1 = H, T_2 = T) = 1$.
  - If $T_2 = H$, the full sequence generated so far is $HH$. The rival $HH$ has occurred, so $HT$ did *not* occur before $HH$!  
    Thus, $P(E \mid T_1 = H, T_2 = H) = 0$.

  Conditioning on $T_2$ given $T_1 = H$:
  $$P(E \mid T_1 = H) = 1 \cdot P(T_2 = T) + 0 \cdot P(T_2 = H) = 1 \cdot \left(\frac{1}{2}\right) + 0 \cdot \left(\frac{1}{2}\right) = \frac{1}{2}$$

- **Step 3: Solve the LTP linear equation:**  
  Substitute the conditional values into the total probability formula:
  $$p = \left(\frac{1}{2}\right)\left(\frac{1}{2}\right) + p\left(\frac{1}{2}\right) = \frac{1}{4} + \frac{1}{2}p$$
  $$p - \frac{1}{2}p = \frac{1}{4} \implies \frac{1}{2}p = \frac{1}{4} \implies p = \frac{2}{4} = \frac{1}{2}$$

**Answer.**  
$P(HT \text{ before } HH) = \frac{1}{2} = 0.50$.

---

##### Exercise PAR 2.29 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.29.  
**Classification:** PAR — Test.  
**Relevant PT ID(s):** [PT-08](#problem-type-pt-08-diagnostic-screening-evaluation-and-base-rate-fallacy-analysis).

**Complete question statement.**  
A polygraph (lie detector) is said to be 90% reliable in the following sense: There is a 90% chance that a person who is telling the truth will pass the polygraph test; and there is a 90% chance that a person telling a lie will fail the polygraph test.
- (a) Suppose a population consists of 5% liars. A random person takes a polygraph test, which concludes that they are lying (fails the test). What is the probability that they are actually lying?
- (b) Consider the probability that a person is actually lying given that the polygraph says that they are. Using the definition of reliability, how reliable must the polygraph test be in order that this probability is at least 80%?

**Complete working.**  
Define events:
- $L$: Person is lying $\implies P(L) = 0.05$.
- $T$: Person is telling the truth $\implies P(T) = 0.95$.
- $F$: Polygraph concludes lying (person fails test).

Reliability $r = 0.90$:
- $P(F \mid L) = r = 0.90$ (sensitivity)
- $P(F^c \mid T) = r = 0.90$ (specificity) $\implies P(F \mid T) = 1 - r = 0.10$ (false alarm rate).

- **(a) Evaluate $P(L \mid F)$ for $r = 0.90$:**  
  Marginal probability of failing the polygraph via LTP:
  $$P(F) = P(F \mid L)P(L) + P(F \mid T)P(T) = (0.90 \times 0.05) + (0.10 \times 0.95)$$
  $$P(F) = 0.045 + 0.095 = 0.140$$
  Applying Bayes' Rule:
  $$P(L \mid F) = \frac{P(F \mid L)P(L)}{P(F)} = \frac{0.045}{0.140} = \frac{45}{140} = \frac{9}{28} \approx 0.321429 \quad (32.14\%)$$
  Even with 90% reliability, approximately $68\%$ of those who fail the test are truthful!

- **(b) Find reliability $r$ such that $P(L \mid F) \ge 0.80$:**  
  Let reliability be $r$. Then $P(F \mid L) = r$ and $P(F \mid T) = 1 - r$.
  $$P(L \mid F) = \frac{0.05 r}{0.05 r + 0.95(1 - r)} \ge 0.80$$
  $$0.05 r \ge 0.80 [0.05 r + 0.95 - 0.95 r] = 0.80 [0.95 - 0.90 r] = 0.76 - 0.72 r$$
  $$0.05 r + 0.72 r \ge 0.76 \implies 0.77 r \ge 0.76$$
  $$r \ge \frac{0.76}{0.77} = \frac{76}{77} \approx 0.987013$$
  The polygraph must be at least **$98.70\%$ reliable**.

**Answer.**  
- (a) $P(L \mid F) = \frac{9}{28} \approx 0.3214$ (32.14%).
- (b) $r \ge \frac{76}{77} \approx 0.9870$ (98.70% reliability required).

---

##### Exercise PAR 2.31 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.31.  
**Classification:** PAR — Test.  
**Relevant PT ID(s):** [PT-07](#problem-type-pt-07-posterior-probability-inversion-via-bayes-rule).

**Complete question statement.**  
Your friend has three dice:
- One die is fair ($D_1$).
- One die has fives on all six sides ($D_2$).
- One die has fives on three sides and fours on three sides ($D_3$).
A die is chosen at random. It comes up five. Find the probability that the chosen die is the fair one.

**Complete working.**  
A die is chosen uniformly at random:
$$P(D_1) = P(D_2) = P(D_3) = \frac{1}{3}$$
Let $F_5$ be the event that the rolled die lands on 5.
Conditional likelihoods of rolling a 5 for each die:
- Fair die ($D_1$): 6 distinct faces $\{1, 2, 3, 4, 5, 6\} \implies P(F_5 \mid D_1) = 1/6$.
- All fives die ($D_2$): 6 fives $\{5, 5, 5, 5, 5, 5\} \implies P(F_5 \mid D_2) = 6/6 = 1$.
- Half fives die ($D_3$): 3 fives and 3 fours $\implies P(F_5 \mid D_3) = 3/6 = 1/2$.

Applying the Law of Total Probability to find $P(F_5)$:
$$P(F_5) = P(F_5 \mid D_1)P(D_1) + P(F_5 \mid D_2)P(D_2) + P(F_5 \mid D_3)P(D_3)$$
$$P(F_5) = \left(\frac{1}{6} \times \frac{1}{3}\right) + \left(1 \times \frac{1}{3}\right) + \left(\frac{1}{2} \times \frac{1}{3}\right) = \frac{1}{3} \left[\frac{1}{6} + \frac{6}{6} + \frac{3}{6}\right] = \frac{1}{3} \times \frac{10}{6} = \frac{10}{18} = \frac{5}{9}$$

Applying Bayes' Rule to find $P(D_1 \mid F_5)$:
$$P(D_1 \mid F_5) = \frac{P(F_5 \mid D_1)P(D_1)}{P(F_5)} = \frac{(1/6)(1/3)}{10/18} = \frac{1/18}{10/18} = \frac{1}{10} = 0.10$$

**Answer.**  
$P(D_1 \mid F_5) = \frac{1}{10} = 0.10$ (10.0%).

---

##### Exercise PAR 2.33 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.33.  
**Classification:** PAR — Test.  
*(Note: Ordered before #32 to preserve exact screenshot sequence).*  
**Relevant PT ID(s):** [PT-03](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics), Theoretical Proofs.

**Complete question statement.**  
Suppose $A$ and $B$ are independent events. Show that $A^c$ and $B^c$ are independent events.

**Complete working.**  
Given: $P(A \cap B) = P(A) \cdot P(B)$.
We must show that $P(A^c \cap B^c) = P(A^c) \cdot P(B^c)$.

- **Step 1: Apply De Morgan's Law:**  
  $$A^c \cap B^c = (A \cup B)^c$$
- **Step 2: Apply the complement rule:**  
  $$P(A^c \cap B^c) = P((A \cup B)^c) = 1 - P(A \cup B)$$
- **Step 3: Expand union by general addition rule:**  
  $$P(A^c \cap B^c) = 1 - [P(A) + P(B) - P(A \cap B)]$$
- **Step 4: Substitute the independence condition $P(A \cap B) = P(A)P(B)$:**  
  $$P(A^c \cap B^c) = 1 - P(A) - P(B) + P(A)P(B)$$
- **Step 5: Factor the algebraic expression:**  
  $$P(A^c \cap B^c) = [1 - P(A)] - P(B)[1 - P(A)] = [1 - P(A)][1 - P(B)]$$
  Since $1 - P(A) = P(A^c)$ and $1 - P(B) = P(B^c)$:
  $$P(A^c \cap B^c) = P(A^c) \cdot P(B^c)$$
This establishes that $A^c$ and $B^c$ are statistically independent. $\blacksquare$

**Answer.**  
Proof established: $P(A^c \cap B^c) = 1 - P(A \cup B) = 1 - P(A) - P(B) + P(A)P(B) = (1 - P(A))(1 - P(B)) = P(A^c)P(B^c)$.

---

##### Exercise PAR 2.32 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.32.  
**Classification:** PAR — Test.  
**Relevant PT ID(s):** [PT-03](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics), Conceptual Foundations.

**Complete question statement.**  
Your friend missed probability class today. Explain to your friend, in simple language, what the difference between disjoint and independent events is.

**Complete working.**  
*Plain-Language Conceptual Explanation:*  
Disjoint events and independent events are not only different—they are mathematical opposites!
1. **Disjoint (Mutually Exclusive) Events:**  
   Think of disjoint events as **incompatible physical realities**. They cannot happen at the same time. If one happens, the other is completely impossible.  
   *Example:* You roll a single die. Let $A$ be rolling an even number and $B$ be rolling an odd number. The die cannot be both even and odd simultaneously ($A \cap B = \emptyset$). If I tell you the roll is even, the probability that it is odd immediately drops to zero ($P(B \mid A) = 0$). Knowing $A$ occurred gives you *total information* about $B$.

2. **Independent Events:**  
   Think of independent events as **unrelated, uninformative occurrences**. They can easily happen together, and knowing that one happened gives you *zero new information* about whether the other happened.  
   *Example:* You roll a red die and a blue die. Let $A$ be the red die showing 6, and $B$ be the blue die showing 6. Can both occur? Yes, you can roll two sixes. Does seeing a 6 on the red die change the chance of getting a 6 on the blue die? Not at all; it remains $1/6$ ($P(B \mid A) = P(B)$).

3. **The Golden Rule to remember:**  
   If two events both have positive probabilities, **they can NEVER be both disjoint and independent**. Disjoint events are *maximally dependent*, because the occurrence of one prevents the other from occurring!

**Answer.**  
Disjoint events cannot happen together ($P(A \cap B) = 0$); if one occurs, the other is impossible. Independent events can happen together, and one happening gives zero information about the other ($P(A \mid B) = P(A)$).

---

##### Exercise PAR 2.36 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.36.  
**Classification:** PAR — Test.  
**Relevant PT ID(s):** [PT-03](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics).

**Complete question statement.**  
Toss two dice. Let $A$ be the event that the first die rolls 1, 2, or 3. Let $B$ be the event that the first die rolls 3, 4, or 5. Let $C$ be the event that the sum of the dice is 9. Show that $P(ABC) = P(A)P(B)P(C)$, but no pair of events is independent.

**Complete working.**  
The sample space $\Omega$ consists of all 36 equally likely ordered pairs $(d_1, d_2)$ where $d_1, d_2 \in \{1, 2, 3, 4, 5, 6\}$.
- Event $A = \{d_1 \in \{1, 2, 3\}\}$: $|A| = 3 \times 6 = 18 \implies P(A) = \frac{18}{36} = \frac{1}{2}$.
- Event $B = \{d_1 \in \{3, 4, 5\}\}$: $|B| = 3 \times 6 = 18 \implies P(B) = \frac{18}{36} = \frac{1}{2}$.
- Event $C = \{d_1 + d_2 = 9\}$: Pairs summing to 9 are $\{(3, 6), (4, 5), (5, 4), (6, 3)\} \implies |C| = 4 \implies P(C) = \frac{4}{36} = \frac{1}{9}$.

- **Step 1: Check the 3-Way Product Condition:**  
  $$P(A) \cdot P(B) \cdot P(C) = \left(\frac{1}{2}\right) \left(\frac{1}{2}\right) \left(\frac{1}{9}\right) = \frac{1}{36}$$
  Now examine the intersection $A \cap B \cap C$:
  - $A \cap B = \{d_1 = 3\}$.
  - For $d_1 + d_2 = 9$ with $d_1 = 3$, we must have $d_2 = 6$.
  Thus, $A \cap B \cap C$ contains exactly one elementary outcome:
  $$A \cap B \cap C = \{(3, 6)\} \implies P(ABC) = \frac{1}{36}$$
  Therefore:
  $$P(ABC) = P(A)P(B)P(C) = \frac{1}{36}$$
  The mutual product condition holds!

- **Step 2: Check Pairwise Independence for All Pairs:**  
  1. **Pair $(A, B)$:**  
     $A \cap B = \{d_1 = 3\} \implies |A \cap B| = 6 \implies P(A \cap B) = \frac{6}{36} = \frac{1}{6}$.  
     Product: $P(A)P(B) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$.  
     Since $\frac{1}{6} \neq \frac{1}{4}$, $A$ and $B$ are **dependent**.
  2. **Pair $(A, C)$:**  
     $A \cap C = \{(d_1, d_2) \in C : d_1 \in \{1, 2, 3\}\} = \{(3, 6)\} \implies P(A \cap C) = \frac{1}{36}$.  
     Product: $P(A)P(C) = \frac{1}{2} \times \frac{1}{9} = \frac{1}{18} = \frac{2}{36}$.  
     Since $\frac{1}{36} \neq \frac{1}{18}$, $A$ and $C$ are **dependent**.
  3. **Pair $(B, C)$:**  
     $B \cap C = \{(d_1, d_2) \in C : d_1 \in \{3, 4, 5\}\} = \{(3, 6), (4, 5), (5, 4)\} \implies P(B \cap C) = \frac{3}{36} = \frac{1}{12}$.  
     Product: $P(B)P(C) = \frac{1}{2} \times \frac{1}{9} = \frac{1}{18}$.  
     Since $\frac{1}{12} \neq \frac{1}{18}$, $B$ and $C$ are **dependent**.

*Theoretical Significance:* This classic counterexample proves that the 3-way product identity $P(ABC) = P(A)P(B)P(C)$ does **not** imply pairwise independence, reinforcing why mutual independence requires checking all sub-collection equations.

**Answer.**  
$P(ABC) = \frac{1}{36} = P(A)P(B)P(C)$, but $P(AB) = \frac{1}{6} \neq \frac{1}{4}$, $P(AC) = \frac{1}{36} \neq \frac{1}{18}$, and $P(BC) = \frac{1}{12} \neq \frac{1}{18}$. No pair is independent.

---

---

## Section D: Original Self-Test Questions

> **Instructions**: Attempt all questions before consulting the solutions in Section E. Each question corresponds directly to one Problem Type (PT-01 through PT-10) and is designed to test your ability to recognize structural cues, avoid common pitfalls, and execute rigorous probabilistic derivations.

---

### Question ST-01 (Mapping to PT-01: Conditional Probability from Joint / Marginal Probabilities and Two-Way Tables)

A cybersecurity firm audits $1,200$ connected IoT devices across three deployment tiers: Residential ($R$), Commercial ($C$), and Industrial ($I$). Devices are evaluated for high vulnerability risk ($V$) or standard security ($S = V^c$). The audit records the following joint counts:

| Deployment Tier | Vulnerable ($V$) | Standard ($V^c$) | Total |
| :--- | :---: | :---: | :---: |
| **Residential ($R$)** | $180$ | $420$ | $600$ |
| **Commercial ($C$)** | $100$ | $300$ | $400$ |
| **Industrial ($I$)** | $20$ | $180$ | $200$ |
| **Total** | $300$ | $900$ | $1,200$ |

1. A device is selected uniformly at random from the entire fleet. What is the probability that it is vulnerable, given that it is not deployed in an Industrial tier?
2. A device is selected uniformly at random and confirmed to be vulnerable. What is the conditional probability that it is deployed in either the Commercial or Industrial tier?
3. Define event $A = R \cup C$ (the device is Non-Industrial) and event $B = V$ (the device is Vulnerable). State whether $A$ and $B$ are independent. Provide mathematical justification using $P(B \mid A)$ and $P(B)$.

---

### Question ST-02 (Mapping to PT-02: Independence and Mutual Exclusivity Conceptual Diagnostics)

Let $(\Omega, \mathcal{F}, P)$ be a probability space, and let $E$ and $F$ be two events such that $0 < P(E) < 1$ and $0 < P(F) < 1$.

1. Suppose $E$ and $F$ are mutually exclusive (disjoint). Can $E$ and $F$ be independent? Explain rigorously by comparing $P(E \cap F)$ under both definitions.
2. Suppose $P(E) = 0.45$, $P(F) = 0.60$, and $P(E \cup F) = 0.78$.
   - (a) Determine $P(E \cap F)$.
   - (b) Are $E$ and $F$ mutually exclusive? Justify.
   - (c) Are $E$ and $F$ independent? Justify.
3. Let $G$ be an event such that $P(G) = 0$. Prove that $G$ is independent of *any* arbitrary event $H \in \mathcal{F}$. Does this imply that an impossible event can occur simultaneously with $H$? Explain the distinction between algebraic independence and physical causal relationship.

---

### Question ST-03 (Mapping to PT-03: Mutual Independence Verification for Three or More Events)

A high-availability computing cluster consists of three independent failover nodes: $N_1, N_2, N_3$. Let $A_i$ denote the event that node $N_i$ experiences a memory leak during a 24-hour cycle ($i \in \{1, 2, 3\}$). The probabilities are $P(A_1) = 0.20$, $P(A_2) = 0.25$, and $P(A_3) = 0.10$.

1. State the exact four mathematical conditions required for the collection $\{A_1, A_2, A_3\}$ to be mutually independent.
2. Assuming mutual independence holds:
   - (a) What is the probability that at least one node experiences a memory leak?
   - (b) What is the probability that exactly one node experiences a memory leak?
   - (c) What is the conditional probability that node $N_1$ experiences a leak, given that at least one of the three nodes experiences a leak?

---

### Question ST-04 (Mapping to PT-04: Network and System Reliability (Series-Parallel Systems))

Consider the telecommunication transmission network shown below between source node $S$ and destination node $T$:

```
                 +--- [ C1 ] ---+
                 |              |
         +--- [ B1 ] --- [ B2 ] ---+
         |                         |
S -------+                         +------- T
         |                         |
         +--- [ D1 ] --- [ D2 ] ---+
                 |              |
                 +--- [ D3 ] ---+
```

Specifically:
- Top branch consists of component $B_1$ in series with $B_2$, but $B_1$ is bypassed by a redundant sub-component $C_1$ in parallel with $B_1$. That is, the top branch functions if $(C_1 \cup B_1)$ functions AND $B_2$ functions.
- Bottom branch consists of a parallel bank of three sub-components: $D_1, D_2, D_3$. The bottom branch functions if at least one of $\{D_1, D_2, D_3\}$ functions.
- The overall system functions if **either** the top branch **or** the bottom branch (or both) functions.

All components operate independently. The operating probabilities are:
- $P(B_1) = 0.80$, $P(C_1) = 0.70$, $P(B_2) = 0.90$.
- $P(D_1) = 0.60$, $P(D_2) = 0.50$, $P(D_3) = 0.40$.

1. Calculate the reliability of the top branch, $R_{\text{top}}$.
2. Calculate the reliability of the bottom branch, $R_{\text{bottom}}$.
3. Calculate the overall system reliability, $R_{\text{system}} = P(\text{Message traverses from } S \text{ to } T)$.

---

### Question ST-05 (Mapping to PT-05: Law of Total Probability (LTP))

An e-commerce platform processes transactions through three third-party payment gateways:
- Gateway 1 ($G_1$) handles $50\%$ of all transactions, with a fraudulent transaction detection failure rate of $0.015$.
- Gateway 2 ($G_2$) handles $35\%$ of all transactions, with a failure rate of $0.020$.
- Gateway 3 ($G_3$) handles $15\%$ of all transactions, with a failure rate of $0.040$.

1. Verify that $\{G_1, G_2, G_3\}$ forms a valid partition of the transaction space.
2. Define event $F$: "A fraudulent transaction fails detection." State the Law of Total Probability expansion for $P(F)$.
3. Compute the overall proportion of fraudulent transactions that fail detection across the entire platform.

---

### Question ST-06 (Mapping to PT-06: Bayes' Rule with Rare Events and Base Rate Fallacy)

A rapid non-invasive screen for a rare pancreatic marker is evaluated in an asymptomatic adult population. The true population prevalence of the marker is $0.2\%$ ($0.002$). Clinical validation reveals:
- Sensitivity (True Positive Rate): $P(+ \mid D) = 0.98$
- False Positive Rate: $P(+ \mid D^c) = 0.01$ (i.e., Specificity $P(- \mid D^c) = 0.99$)

1. Set up the complete Bayes' theorem equation to evaluate the posterior probability $P(D \mid +)$ (Positive Predictive Value, PPV).
2. Calculate $P(D \mid +)$.
3. Explain mathematically why an individual who tests positive on a test with $98\%$ sensitivity and $99\%$ specificity still has a probability substantially below $50\%$ of actually carrying the marker. Identify the cognitive bias known as the "Base Rate Fallacy."
4. If a positive test is immediately followed by a second, fully independent confirmatory screen with the exact same operating characteristics ($98\%$ sensitivity, $1\%$ false positive rate), compute the updated posterior probability $P(D \mid +_1 \cap +_2)$.

---

### Question ST-07 (Mapping to PT-07: Random Variable Definition and Sample Space Mapping)

A quality control engineer inspects batches of microchips. From a large batch containing $10\%$ defective chips, chips are tested sequentially one by one until either a defective chip is found or a total of 4 chips have been inspected, whichever occurs first. Let $D$ denote a defective chip and $G$ denote a non-defective (good) chip. Assume successive chip outcomes are independent.

1. Write out the explicit sample space $\Omega$ listing all possible inspection sequences (sample points).
2. Assign the correct probability to each elementary outcome in $\Omega$. Verify that the sum of all probabilities equals 1.
3. Define the random variable $X$ as the total number of non-defective ($G$) chips observed during the inspection. For each outcome $\omega \in \Omega$, state the value $X(\omega)$.
4. Determine the support $\mathcal{S}_X$ of the random variable $X$.

---

### Question ST-08 (Mapping to PT-08: PMF Validity Verification and Unknown Constant Normalization)

A discrete random variable $Y$ has probability mass function (PMF) given by:
$$p_Y(y) = \begin{cases} c \cdot (y^2 + 1), & y \in \{-2, -1, 0, 1, 2\} \\ 0, & \text{otherwise} \end{cases}$$
where $c$ is a real constant.

1. State the two axiomatic conditions that $p_Y(y)$ must satisfy to be a legitimate probability mass function.
2. Determine the exact value of the normalizing constant $c$.
3. Compute the following probabilities:
   - (a) $P(Y > 0)$
   - (b) $P(Y^2 \le 1)$
   - (c) $P(Y \ge 0 \mid Y \le 1)$

---

### Question ST-09 (Mapping to PT-09: Probability Calculations from a PMF (Events, Intervals, and Tail Probabilities))

The number of emergency maintenance calls $K$ received by a municipal water utility on a weekend day follows the PMF:

| $k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $p_K(k)$ | $0.15$ | $0.30$ | $0.25$ | $0.15$ | $0.10$ | $0.05$ |

and $p_K(k) = 0$ for all other integers $k$.

1. Compute $P(1 < K \le 4)$. Show clearly which support points are included.
2. Compute $P(K \ge 2)$ using:
   - (a) Direct summation of relevant support points.
   - (b) The complement rule. Verify both yield identical numerical results.
3. Compute the conditional probability $P(K \ge 3 \mid K \ge 1)$.

---

### Question ST-10 (Mapping to PT-10: Deriving a PMF from an Experiment or Functional Transformation)

A fair six-sided die (with faces numbered $1, 2, 3, 4, 5, 6$) is rolled once. Let $U$ be the outcome of the roll, so $P(U = u) = \frac{1}{6}$ for $u \in \{1, 2, 3, 4, 5, 6\}$. A secondary random variable $W$ is defined by the transformation:
$$W = (U - 3)^2$$

1. Determine the set of possible values (support $\mathcal{S}_W$) taken by $W$.
2. For each distinct value $w \in \mathcal{S}_W$, determine the pre-image set $\{u \in \mathcal{S}_U : (u - 3)^2 = w\}$.
3. Derive the complete probability mass function $p_W(w)$, writing the final PMF in standard piecewise/tabular format.
4. Verify that $\sum_{w \in \mathcal{S}_W} p_W(w) = 1$.

---

## Section E: Solutions to Self-Test Questions

---

### Solution ST-01 (PT-01)

#### Part 1: $P(V \mid I^c)$
- The conditioning event is $I^c = R \cup C$ (Residential or Commercial).
- Total count in $I^c$: $n(I^c) = n(R) + n(C) = 600 + 400 = 1,000$.
- Count of vulnerable devices in $I^c$: $n(V \cap I^c) = n(V \cap R) + n(V \cap C) = 180 + 100 = 280$.
- By the conditional probability formula:
  $$P(V \mid I^c) = \frac{n(V \cap I^c)}{n(I^c)} = \frac{280}{1,000} = 0.280$$

#### Part 2: $P(C \cup I \mid V)$
- Conditioning on $V$ (total vulnerable devices = $300$).
- Favorable devices in $C \cup I$: $n((C \cup I) \cap V) = n(C \cap V) + n(I \cap V) = 100 + 20 = 120$.
- By conditional probability:
  $$P(C \cup I \mid V) = \frac{n((C \cup I) \cap V)}{n(V)} = \frac{120}{300} = \frac{2}{5} = 0.400$$

#### Part 3: Independence Check of $A = R \cup C$ and $B = V$
- $P(B) = P(V) = \frac{300}{1,200} = 0.250$.
- From Part 1, $P(B \mid A) = P(V \mid I^c) = 0.280$.
- Since $P(B \mid A) = 0.280 \ne 0.250 = P(B)$, the events $A$ and $B$ are **not independent** (they are dependent).
- *Alternative check*: $P(A \cap B) = \frac{280}{1,200} = \frac{7}{30} \approx 0.2333$. Meanwhile, $P(A)P(B) = \left(\frac{1,000}{1,200}\right) \times \left(\frac{300}{1,200}\right) = \frac{5}{6} \times \frac{1}{4} = \frac{5}{24} \approx 0.2083$. Since $\frac{7}{30} \ne \frac{5}{24}$, independence fails.

---

### Solution ST-02 (PT-02)

#### Part 1: Mutual Exclusivity vs. Independence
- If $E$ and $F$ are mutually exclusive, then by definition $E \cap F = \emptyset$, which implies $P(E \cap F) = 0$.
- If $E$ and $F$ were also independent, they must satisfy $P(E \cap F) = P(E) P(F)$.
- Combining these gives:
  $$P(E) P(F) = 0$$
- This requires either $P(E) = 0$ or $P(F) = 0$.
- However, the problem explicitly premises that $0 < P(E) < 1$ and $0 < P(F) < 1$. Thus, $P(E)P(F) > 0$.
- Therefore, $P(E \cap F) = 0 \ne P(E)P(F)$, so $E$ and $F$ **cannot** be independent.
- **Conclusion**: Two events with non-zero probability that are mutually exclusive are always strongly dependent (in fact, if one occurs, the other cannot occur: $P(E \mid F) = 0$).

#### Part 2: Calculations
- **(a) $P(E \cap F)$**:
  By the addition rule for probabilities:
  $$P(E \cup F) = P(E) + P(F) - P(E \cap F)$$
  $$0.78 = 0.45 + 0.60 - P(E \cap F) \implies P(E \cap F) = 1.05 - 0.78 = 0.27$$
- **(b) Mutual Exclusivity**:
  $P(E \cap F) = 0.27 \ne 0$. Since their intersection has positive probability, $E$ and $F$ are **not mutually exclusive**.
- **(c) Independence**:
  Check product rule:
  $$P(E) P(F) = 0.45 \times 0.60 = 0.270$$
  Since $P(E \cap F) = 0.27 = P(E) P(F)$, events $E$ and $F$ are **independent**.

#### Part 3: Independence with a Null Event
- Let $G$ have $P(G) = 0$.
- For any arbitrary event $H$, note that $G \cap H \subseteq G$. By monotonicity of probability:
  $$0 \le P(G \cap H) \le P(G) = 0 \implies P(G \cap H) = 0$$
- On the other hand:
  $$P(G) P(H) = 0 \times P(H) = 0$$
- Therefore, $P(G \cap H) = P(G) P(H)$ holds identically. Thus, $G$ is independent of $H$.
- **Conceptual distinction**: This demonstrates that mathematical independence is strictly an algebraic property of the probability measure ($P(A \cap B) = P(A)P(B)$), not a physical or causal statement. An impossible event does not "cause" or physically interact with $H$; rather, learning that $H$ occurred leaves the probability of $G$ unchanged at 0 ($P(G \mid H) = 0 = P(G)$).

---

### Solution ST-03 (PT-03)

#### Part 1: Four Conditions for Mutual Independence
For $\{A_1, A_2, A_3\}$ to be mutually independent, the following four conditions must hold simultaneously:
1. $P(A_1 \cap A_2) = P(A_1) P(A_2)$
2. $P(A_1 \cap A_3) = P(A_1) P(A_3)$
3. $P(A_2 \cap A_3) = P(A_2) P(A_3)$
4. $P(A_1 \cap A_2 \cap A_3) = P(A_1) P(A_2) P(A_3)$

#### Part 2(a): At least one leak
- Complement: No node experiences a leak, which is $A_1^c \cap A_2^c \cap A_3^c$.
- By mutual independence, the complements are also mutually independent:
  $$P(A_1^c) = 1 - 0.20 = 0.80$$
  $$P(A_2^c) = 1 - 0.25 = 0.75$$
  $$P(A_3^c) = 1 - 0.10 = 0.90$$
  $$P(A_1^c \cap A_2^c \cap A_3^c) = 0.80 \times 0.75 \times 0.90 = 0.540$$
- Therefore:
  $$P(\text{at least one leak}) = 1 - 0.540 = 0.460$$

#### Part 2(b): Exactly one leak
- "Exactly one leak" is the disjoint union of three mutually exclusive events:
  $$\text{Ex}_1 = (A_1 \cap A_2^c \cap A_3^c) \cup (A_1^c \cap A_2 \cap A_3^c) \cup (A_1^c \cap A_2^c \cap A_3)$$
- Compute each probability by independence:
  $$P(A_1 \cap A_2^c \cap A_3^c) = 0.20 \times 0.75 \times 0.90 = 0.135$$
  $$P(A_1^c \cap A_2 \cap A_3^c) = 0.80 \times 0.25 \times 0.90 = 0.180$$
  $$P(A_1^c \cap A_2^c \cap A_3) = 0.80 \times 0.75 \times 0.10 = 0.060$$
- Summing these:
  $$P(\text{exactly one leak}) = 0.135 + 0.180 + 0.060 = 0.375$$

#### Part 2(c): Conditional probability $P(A_1 \mid \text{at least one leak})$
- Let $E = A_1 \cup A_2 \cup A_3$. Note that $A_1 \subseteq E$, so $A_1 \cap E = A_1$.
- Thus:
  $$P(A_1 \mid E) = \frac{P(A_1 \cap E)}{P(E)} = \frac{P(A_1)}{P(E)} = \frac{0.20}{0.460} = \frac{20}{46} = \frac{10}{23} \approx 0.4348$$

---

### Solution ST-04 (PT-04)

#### Part 1: Top Branch Reliability $R_{\text{top}}$
- The top branch has sub-system $S_{\text{parallel}} = C_1 \cup B_1$ in series with $B_2$.
- Parallel sub-system reliability:
  $$R_{C_1 \cup B_1} = 1 - P(C_1^c \cap B_1^c) = 1 - (1 - 0.70)(1 - 0.80) = 1 - (0.30 \times 0.20) = 1 - 0.06 = 0.94$$
- Since this sub-system is in series with $B_2$:
  $$R_{\text{top}} = R_{C_1 \cup B_1} \times P(B_2) = 0.94 \times 0.90 = 0.846$$

#### Part 2: Bottom Branch Reliability $R_{\text{bottom}}$
- The bottom branch consists of $D_1, D_2, D_3$ in parallel.
- Fails only if all three fail simultaneously:
  $$P(\text{bottom fails}) = P(D_1^c) P(D_2^c) P(D_3^c) = (1 - 0.60)(1 - 0.50)(1 - 0.40) = 0.40 \times 0.50 \times 0.60 = 0.120$$
- Thus:
  $$R_{\text{bottom}} = 1 - 0.120 = 0.880$$

#### Part 3: Overall System Reliability $R_{\text{system}}$
- The top branch and bottom branch are in parallel.
- System fails if and only if both the top branch and bottom branch fail simultaneously.
- Since components in top and bottom branches are distinct and independent, the branches operate independently:
  $$P(\text{top fails}) = 1 - R_{\text{top}} = 1 - 0.846 = 0.154$$
  $$P(\text{bottom fails}) = 1 - R_{\text{bottom}} = 1 - 0.880 = 0.120$$
  $$P(\text{system fails}) = 0.154 \times 0.120 = 0.01848$$
- Overall system reliability:
  $$R_{\text{system}} = 1 - P(\text{system fails}) = 1 - 0.01848 = 0.98152$$

---

### Solution ST-05 (PT-05)

#### Part 1: Partition Verification
1. **Mutually Exclusive**: A transaction is routed through exactly one gateway, so $G_i \cap G_j = \emptyset$ for $i \ne j$.
2. **Exhaustive**: $P(G_1) + P(G_2) + P(G_3) = 0.50 + 0.35 + 0.15 = 1.00$, covering $\Omega$.
3. **Non-zero**: $P(G_i) > 0$ for all $i \in \{1, 2, 3\}$.
Hence, $\{G_1, G_2, G_3\}$ forms a valid partition.

#### Part 2: Law of Total Probability Formula
$$P(F) = \sum_{i=1}^3 P(F \mid G_i) P(G_i) = P(F \mid G_1) P(G_1) + P(F \mid G_2) P(G_2) + P(F \mid G_3) P(G_3)$$

#### Part 3: Computation
- Given:
  - $P(F \mid G_1) = 0.015$, $P(G_1) = 0.50$
  - $P(F \mid G_2) = 0.020$, $P(G_2) = 0.35$
  - $P(F \mid G_3) = 0.040$, $P(G_3) = 0.15$
- Calculating:
  $$P(F) = (0.015)(0.50) + (0.020)(0.35) + (0.040)(0.15)$$
  $$P(F) = 0.00750 + 0.00700 + 0.00600 = 0.0205$$
Across the entire platform, $2.05\%$ of fraudulent transactions fail detection.

---

### Solution ST-06 (PT-06)

#### Part 1: Bayes' Theorem Setup
$$P(D \mid +) = \frac{P(+ \mid D) P(D)}{P(+)} = \frac{P(+ \mid D) P(D)}{P(+ \mid D) P(D) + P(+ \mid D^c) P(D^c)}$$

#### Part 2: Calculation of $P(D \mid +)$
- $P(D) = 0.002 \implies P(D^c) = 0.998$
- $P(+ \mid D) = 0.98$
- $P(+ \mid D^c) = 0.01$
- Numerator (True Positives):
  $$P(+ \cap D) = 0.98 \times 0.002 = 0.00196$$
- Denominator component (False Positives):
  $$P(+ \cap D^c) = 0.01 \times 0.998 = 0.00998$$
- Total $P(+)$:
  $$P(+) = 0.00196 + 0.00998 = 0.01194$$
- Posterior:
  $$P(D \mid +) = \frac{0.00196}{0.01194} \approx 0.16415 \approx 16.42\%$$

#### Part 3: Base Rate Fallacy Explanation
Even though the test has high sensitivity ($98\%$) and specificity ($99\%$), the condition is very rare ($0.2\%$). In a cohort of $100,000$ individuals:
- $200$ individuals have the marker; $\approx 196$ test positive.
- $99,800$ individuals do not have the marker; $1\%$ of them ($998$ individuals) test false positive.
Out of $196 + 998 = 1,194$ total positive tests, the vast majority ($998$) are healthy people who received false positives. The **Base Rate Fallacy** occurs when human intuition focuses solely on the high accuracy rates of the test ($98\%$ and $99\%$) while neglecting the extremely low prior baseline prevalence ($0.2\%$).

#### Part 4: Second Independent Confirmatory Screen
Assuming the second screen $+_2$ is conditionally independent of $+_1$ given disease state:
$$P(+_1 \cap +_2 \mid D) = (0.98)^2 = 0.9604$$
$$P(+_1 \cap +_2 \mid D^c) = (0.01)^2 = 0.0001$$
Applying Bayes' rule:
$$P(D \mid +_1 \cap +_2) = \frac{P(+_1 \cap +_2 \mid D) P(D)}{P(+_1 \cap +_2 \mid D) P(D) + P(+_1 \cap +_2 \mid D^c) P(D^c)}$$
$$= \frac{0.9604 \times 0.002}{(0.9604 \times 0.002) + (0.0001 \times 0.998)}$$
$$= \frac{0.0019208}{0.0019208 + 0.0000998} = \frac{0.0019208}{0.0020206} \approx 0.9506 \approx 95.06\%$$
Two successive independent positive tests raise the confidence to over $95\%$.

---

### Solution ST-07 (PT-07)

#### Part 1: Explicit Sample Space $\Omega$
The inspection stops as soon as a defective chip ($D$) is encountered OR when 4 chips are inspected.
The possible outcome strings are:
$$\Omega = \{ D, GD, GGD, GGGD, GGGG \}$$

#### Part 2: Probability Assignment and Verification
Given $P(D) = 0.10$ and $P(G) = 0.90$, with independent draws:
- $P(D) = 0.10$
- $P(GD) = (0.90)(0.10) = 0.090$
- $P(GGD) = (0.90)^2(0.10) = 0.0810$
- $P(GGGD) = (0.90)^3(0.10) = 0.0729$
- $P(GGGG) = (0.90)^4 = 0.6561$

**Sum of probabilities**:
$$\sum_{\omega \in \Omega} P(\omega) = 0.10 + 0.090 + 0.0810 + 0.0729 + 0.6561 = 1.0000$$
Validates axiom 2.

#### Part 3: Mapping of Random Variable $X$
$X$ is the total number of good ($G$) chips observed:
- For $\omega = D$: $X(D) = 0$
- For $\omega = GD$: $X(GD) = 1$
- For $\omega = GGD$: $X(GGD) = 2$
- For $\omega = GGGD$: $X(GGGD) = 3$
- For $\omega = GGGG$: $X(GGGG) = 4$

#### Part 4: Support $\mathcal{S}_X$
$$\mathcal{S}_X = \{0, 1, 2, 3, 4\}$$

---

### Solution ST-08 (PT-08)

#### Part 1: PMF Axiomatic Conditions
1. **Non-negativity**: $p_Y(y) \ge 0$ for all $y \in \mathbb{R}$.
2. **Total Probability Normalization**: $\sum_{y \in \mathcal{S}_Y} p_Y(y) = 1$.

#### Part 2: Normalizing Constant $c$
Evaluate $y^2 + 1$ over $\mathcal{S}_Y = \{-2, -1, 0, 1, 2\}$:
- For $y = -2$: $(-2)^2 + 1 = 5$
- For $y = -1$: $(-1)^2 + 1 = 2$
- For $y = 0$: $0^2 + 1 = 1$
- For $y = 1$: $1^2 + 1 = 2$
- For $y = 2$: $2^2 + 1 = 5$

Sum of kernel values:
$$\sum_{y \in \mathcal{S}_Y} (y^2 + 1) = 5 + 2 + 1 + 2 + 5 = 15$$
Condition 2 requires:
$$c \sum (y^2 + 1) = 1 \implies 15c = 1 \implies c = \frac{1}{15}$$
Since $c = \frac{1}{15} > 0$, $p_Y(y) \ge 0$ holds for all $y$, satisfying Condition 1.
Thus:
$$p_Y(y) = \frac{y^2 + 1}{15}, \quad y \in \{-2, -1, 0, 1, 2\}$$

#### Part 3: Probability Calculations
- **(a) $P(Y > 0)$**:
  $$P(Y > 0) = p_Y(1) + p_Y(2) = \frac{2}{15} + \frac{5}{15} = \frac{7}{15}$$
- **(b) $P(Y^2 \le 1)$**:
  $Y^2 \le 1 \iff -1 \le Y \le 1$, which corresponds to $y \in \{-1, 0, 1\}$.
  $$P(Y^2 \le 1) = p_Y(-1) + p_Y(0) + p_Y(1) = \frac{2}{15} + \frac{1}{15} + \frac{2}{15} = \frac{5}{15} = \frac{1}{3}$$
- **(c) $P(Y \ge 0 \mid Y \le 1)$**:
  Conditioning event: $Y \le 1 \implies \mathcal{S}_{\text{cond}} = \{-2, -1, 0, 1\}$.
  $$P(Y \le 1) = p_Y(-2) + p_Y(-1) + p_Y(0) + p_Y(1) = \frac{5 + 2 + 1 + 2}{15} = \frac{10}{15} = \frac{2}{3}$$
  Intersection event: $\{Y \ge 0\} \cap \{Y \le 1\} = \{0, 1\}$.
  $$P(Y \in \{0, 1\}) = p_Y(0) + p_Y(1) = \frac{1 + 2}{15} = \frac{3}{15} = \frac{1}{5}$$
  Applying conditional probability:
  $$P(Y \ge 0 \mid Y \le 1) = \frac{3/15}{10/15} = \frac{3}{10} = 0.30$$

---

### Solution ST-09 (PT-09)

#### Part 1: $P(1 < K \le 4)$
The strict inequality $1 < K$ and non-strict $\le 4$ includes support points $k \in \{2, 3, 4\}$.
$$P(1 < K \le 4) = p_K(2) + p_K(3) + p_K(4) = 0.25 + 0.15 + 0.10 = 0.50$$

#### Part 2: $P(K \ge 2)$
- **(a) Direct summation**:
  Support points $\ge 2$ are $\{2, 3, 4, 5\}$.
  $$P(K \ge 2) = p_K(2) + p_K(3) + p_K(4) + p_K(5) = 0.25 + 0.15 + 0.10 + 0.05 = 0.55$$
- **(b) Complement rule**:
  The complement event is $\{K < 2\} = \{K \le 1\} = \{0, 1\}$.
  $$P(K < 2) = p_K(0) + p_K(1) = 0.15 + 0.30 = 0.45$$
  $$P(K \ge 2) = 1 - P(K < 2) = 1 - 0.45 = 0.55$$
Both methods match.

#### Part 3: Conditional Probability $P(K \ge 3 \mid K \ge 1)$
- Denominator:
  $$P(K \ge 1) = 1 - P(K = 0) = 1 - 0.15 = 0.85$$
- Numerator:
  Since $\{K \ge 3\} \subseteq \{K \ge 1\}$, their intersection is simply $\{K \ge 3\}$.
  $$P(\{K \ge 3\} \cap \{K \ge 1\}) = P(K \ge 3) = p_K(3) + p_K(4) + p_K(5) = 0.15 + 0.10 + 0.05 = 0.30$$
- Conditional probability:
  $$P(K \ge 3 \mid K \ge 1) = \frac{0.30}{0.85} = \frac{30}{85} = \frac{6}{17} \approx 0.3529$$

---

### Solution ST-10 (PT-10)

#### Part 1: Support $\mathcal{S}_W$
Evaluate $w = (u - 3)^2$ for each $u \in \{1, 2, 3, 4, 5, 6\}$:
- $u = 1 \implies w = (1 - 3)^2 = (-2)^2 = 4$
- $u = 2 \implies w = (2 - 3)^2 = (-1)^2 = 1$
- $u = 3 \implies w = (3 - 3)^2 = 0^2 = 0$
- $u = 4 \implies w = (4 - 3)^2 = 1^2 = 1$
- $u = 5 \implies w = (5 - 3)^2 = 2^2 = 4$
- $u = 6 \implies w = (6 - 3)^2 = 3^2 = 9$

Distinct values taken by $W$:
$$\mathcal{S}_W = \{0, 1, 4, 9\}$$

#### Part 2: Pre-image Sets
- For $w = 0$: $\{u : (u - 3)^2 = 0\} = \{3\}$
- For $w = 1$: $\{u : (u - 3)^2 = 1\} = \{2, 4\}$
- For $w = 4$: $\{u : (u - 3)^2 = 4\} = \{1, 5\}$
- For $w = 9$: $\{u : (u - 3)^2 = 9\} = \{6\}$

#### Part 3: Derivation of the PMF $p_W(w)$
Since each die roll is equally likely with $P(U = u) = \frac{1}{6}$:
- $p_W(0) = P(U = 3) = \frac{1}{6}$
- $p_W(1) = P(U = 2) + P(U = 4) = \frac{1}{6} + \frac{1}{6} = \frac{2}{6} = \frac{1}{3}$
- $p_W(4) = P(U = 1) + P(U = 5) = \frac{1}{6} + \frac{1}{6} = \frac{2}{6} = \frac{1}{3}$
- $p_W(9) = P(U = 6) = \frac{1}{6}$

In standard tabular format:

| $w$ | $0$ | $1$ | $4$ | $9$ |
| :---: | :---: | :---: | :---: | :---: |
| $p_W(w)$ | $\frac{1}{6}$ | $\frac{1}{3}$ | $\frac{1}{3}$ | $\frac{1}{6}$ |

or in piecewise specification:
$$p_W(w) = \begin{cases} \frac{1}{6}, & w \in \{0, 9\} \\ \frac{1}{3}, & w \in \{1, 4\} \\ 0, & \text{otherwise} \end{cases}$$

#### Part 4: Sum Verification
$$\sum_{w \in \mathcal{S}_W} p_W(w) = \frac{1}{6} + \frac{1}{3} + \frac{1}{3} + \frac{1}{6} = \frac{1 + 2 + 2 + 1}{6} = \frac{6}{6} = 1$$
Normalization verified.

---

## Section F: Coverage & Unresolved-Items Appendix

### 1. Comprehensive Coverage Mapping Matrix

| Week 3 Slide / Source | Core Topic / Learning Objective | Concept ID | Problem Type ID | MMSA Exercises | PAR Exercises | Self-Test Question |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| **Slides 1–5** | Conditional probability definition, sample space restriction, multiplication rule | **C-01** | **PT-01** | 2.4-1, 2.4-3, 2.4-7, 2.4-9 | 2.1, 2.3, 2.4, 2.6, 2.8, 2.11 | **ST-01** |
| **Slides 6–10** | Independence vs. mutual exclusivity, pairwise verification, zero-probability events | **C-02** | **PT-02** | 2.5-1, 2.5-3, 2.5-5, 2.5-7, 2.5-9 | 2.16, 2.17, 2.19, 2.21, 2.22, 2.24 | **ST-02** |
| **Slides 11–13** | Mutual independence of $\ge 3$ events, conditions product, pairwise vs. mutual counterexamples | **C-02** | **PT-03** | 2.5-11, 2.5-13, 2.5-15 | 2.26, 2.39 | **ST-03** |
| **Slides 14–16** | System reliability, series, parallel, bridge structures, independent components | **C-02** | **PT-04** | 2.5-17, 2.5-19, 2.5-21 | 2.29, 2.31, 2.32, 2.33, 2.36 | **ST-04** |
| **Slides 17–20** | Partition of sample space, Law of Total Probability (LTP), weighted average of conditional probabilities | **C-03** | **PT-05** | 2.4-11, 2.4-13 | 2.7, 2.10 | **ST-05** |
| **Slides 21–25** | Bayes' Rule, prior to posterior updating, diagnostic testing, Base Rate Fallacy | **C-03** | **PT-06** | 2.4-15, 2.4-17, 2.4-19 | 2.13, 2.14, 2.23 | **ST-06** |
| **Slides 26–29** | Random variables as functions from $\Omega \to \mathbb{R}$, support $\mathcal{S}_X$, event pre-images | **C-04** | **PT-07** | 3.1-1, 3.1-3 | 3.1, 3.2, 3.3, 3.4, 3.5 | **ST-07** |
| **Slides 30–31** | PMF axiomatic conditions ($p(x) \ge 0$, $\sum p(x) = 1$), normalizing constants | **C-05** | **PT-08** | 3.1-5, 3.1-7 | 3.6 | **ST-08** |
| **Slides 32–33** | Probability evaluation from PMF, intervals, complement tail tricks | **C-05** | **PT-09** | 3.1-9, 3.1-11 | 3.7 | **ST-09** |
| **Slides 34–36** | Deriving PMFs from physical random experiments and functional transformations $Y = g(X)$ | **C-05** | **PT-10** | 3.1-13, 3.1-15 | 3.1 | **ST-10** |

---

### 2. Reading Status and Textbook Chapter Alignment

| Reference Text | Sections Covered | Alignment Status | Role in Course Study Notes |
| :--- | :--- | :--- | :--- |
| **MMSA (Probability & Statistical Inference, 3rd ed.)** | §§ 2.4 (Conditional Probability, Total Prob, Bayes), 2.5 (Independent Events), 3.1 (Random Variables of the Discrete Type) | **Core Scope** | Primary source for formal mathematical definitions, textbook exercise sets, and canonical notation. |
| **PAR (Probability & Applications with R, 2nd ed.)** | §§ 2.1–2.6 (Conditional Probability, Independence, Bayes), 3.1 (Discrete Random Variables) | **Supporting / Applied Scope** | Provides engineering/reliability applications (circuit diagrams), clinical diagnostic problems, and applied modeling contexts. |

---

### 3. Recorded Course Platform Access Gaps

1. **Canvas Discussion Boards & Course Announcements Access Gap**:
   - *Nature of Gap*: Canvas LMS course shell `465634` was queried via MCP tools. Course announcements and assignment descriptions were accessible, but the Canvas discussion board / forum API endpoints are not supported by the MCP server, and raw file downloads of certain course-internal syllabus attachments returned 403 Forbidden.
   - *Resolution & Handling*: In strict adherence to academic honesty and factual accuracy standards, **no discussion board posts, student inquiries, or unconfirmed instructor clarifications have been simulated or fabricated**. All instructional cues, emphasis points, and pitfalls are grounded strictly in the verified lecture slides (`Week 3.pdf`), course syllabus learning outcomes, and established textbook problem structures.
2. **Textbook Reading Classification**:
   - The textbook sections MMSA 2.4–2.5, 3.1 and PAR 2.1–2.6, 3.1 are recorded as core supporting readings directly aligned with the Week 3 syllabus learning modules.
