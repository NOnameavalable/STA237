#!/usr/bin/env python3
"""
Writes Section B to Answers-and-Practice.md.
"""

OUTPUT_PATH = "/Users/stevenli/Documents/University of toronto/STA237/W3/Study-Notes-Markdown/Answers-and-Practice.md"

section_b = """
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
$$N = \\frac{n!}{n_1! \\, n_2! \\, n_3! \\, n_4!} = \\frac{7!}{1! \\, 1! \\, 2! \\, 3!} = \\frac{5040}{1 \\times 1 \\times 2 \\times 6} = \\frac{5040}{12} = 420$$

**(b) The number is smaller than 4,000,000:**  
A 7-digit number is strictly less than 4,000,000 if and only if its leading (millions) digit is strictly less than 4. The available choices for the first digit are $1, 2,$ or $3$. We partition into three mutually exclusive cases based on the first digit:
- **Case 1 (First digit is 1):** Remaining digits to permute are $\\{2, 3, 3, 4, 4, 4\\}$ (counts: one 2, two 3s, three 4s).
  $$N_1 = \\frac{6!}{1! \\, 2! \\, 3!} = \\frac{720}{12} = 60$$
- **Case 2 (First digit is 2):** Remaining digits to permute are $\\{1, 3, 3, 4, 4, 4\\}$ (counts: one 1, two 3s, three 4s).
  $$N_2 = \\frac{6!}{1! \\, 2! \\, 3!} = \\frac{720}{12} = 60$$
- **Case 3 (First digit is 3):** Remaining digits to permute are $\\{1, 2, 3, 4, 4, 4\\}$ (counts: one 1, one 2, one 3, three 4s).
  $$N_3 = \\frac{6!}{1! \\, 1! \\, 1! \\, 3!} = \\frac{720}{6} = 120$$

Summing the cases:
$$N_{<4M} = N_1 + N_2 + N_3 = 60 + 60 + 120 = 240$$
*Complement Verification:* The only alternative is that the leading digit is 4. Remaining digits $\\{1, 2, 3, 3, 4, 4\\}$ have counts (one 1, one 2, two 3s, two 4s), yielding $\\frac{6!}{1! 1! 2! 2!} = \\frac{720}{4} = 180$. Total $= 420 - 180 = 240$. Matches.

**(c) The number is smaller than 4,000,000 AND is even:**  
To be even, the last digit must be an even digit from the multiset: either $2$ or $4$. Simultaneously, to be smaller than 4,000,000, the first digit must be $1, 2,$ or $3$. We partition by the ending digit:
- **Subcase C1 (Last digit is 2):**  
  Digit 2 is fixed in position 7. The remaining digits for positions 1–6 are $\\{1, 3, 3, 4, 4, 4\\}$.  
  The first digit can be 1 or 3 (it cannot be 2 since only one 2 exists):
  - *First digit = 1:* Remaining digits for positions 2–6 are $\\{3, 3, 4, 4, 4\\}$.
    $$N_{C1, 1} = \\frac{5!}{2! \\, 3!} = \\frac{120}{12} = 10$$
  - *First digit = 3:* Remaining digits for positions 2–6 are $\\{1, 3, 4, 4, 4\\}$.
    $$N_{C1, 3} = \\frac{5!}{1! \\, 1! \\, 3!} = \\frac{120}{6} = 20$$
  Subtotal for ending in 2: $10 + 20 = 30$.

- **Subcase C2 (Last digit is 4):**  
  One 4 is fixed in position 7. The remaining digits for positions 1–6 are $\\{1, 2, 3, 3, 4, 4\\}$.  
  The first digit can be 1, 2, or 3:
  - *First digit = 1:* Remaining digits for positions 2–6 are $\\{2, 3, 3, 4, 4\\}$.
    $$N_{C2, 1} = \\frac{5!}{1! \\, 2! \\, 2!} = \\frac{120}{4} = 30$$
  - *First digit = 2:* Remaining digits for positions 2–6 are $\\{1, 3, 3, 4, 4\\}$.
    $$N_{C2, 2} = \\frac{5!}{1! \\, 2! \\, 2!} = \\frac{120}{4} = 30$$
  - *First digit = 3:* Remaining digits for positions 2–6 are $\\{1, 2, 3, 4, 4\\}$.
    $$N_{C2, 3} = \\frac{5!}{1! \\, 1! \\, 1! \\, 2!} = \\frac{120}{2} = 60$$
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

**(a) Probability that an individual is male and colourblind ($P(M \\cap C)$):**  
This is the joint probability evaluated over the entire population:
$$P(M \\cap C) = \\frac{n(M \\cap C)}{N} = \\frac{106}{2500} = 0.0424 \\quad (4.24\\%)$$

**(b) Conditional probabilities $P(C \\mid M)$ and $P(C \\mid M^c)$:**  
- **For a male individual ($P(C \\mid M)$):**  
  Restricting the sample space to the male row ($n(M) = 1281$):
  $$P(C \\mid M) = \\frac{n(M \\cap C)}{n(M)} = \\frac{106}{1281} \\approx 0.082748 \\quad (8.27\\%)$$
- **For a female individual ($P(C \\mid M^c)$):**  
  Restricting the sample space to the female row ($n(M^c) = 1219$):
  $$P(C \\mid M^c) = \\frac{n(M^c \\cap C)}{n(M^c)} = \\frac{7}{1219} \\approx 0.005742 \\quad (0.57\\%)$$

*Interpretation:* In this sample, males are approximately $14.4$ times more likely to be colourblind than females ($8.27\\%$ vs. $0.57\\%$), illustrating how conditional conditioning reveals sex-linked genetic traits that are obscured in the overall marginal rate $P(C) = 113/2500 = 4.52\\%$.

**Answer.**  
- (a) $P(M \\cap C) = 0.0424$ (4.24%).
- (b) $P(C \\mid M) \\approx 0.0827$ (8.27%); $P(C \\mid M^c) \\approx 0.0057$ (0.57%).

---

### Slide 8: Example 2 — Consulting Firm Bids (MMSA Ex. 58 Selection)

**Source identification:** `W3/Week 3.pdf`, Slide 8 ("Example 2 - MMSA Ex. 58").  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
A consulting firm presently has bids out on three projects. Let $A_i = \\{\\text{Awarded project } i\\}$ for $i = 1, 2, 3$, and suppose that:
- $P(A_1) = 0.22$, $P(A_2) = 0.25$, $P(A_3) = 0.28$
- $P(A_1 \\cap A_2) = 0.11$, $P(A_1 \\cap A_3) = 0.05$, $P(A_2 \\cap A_3) = 0.07$
- $P(A_1 \\cap A_2 \\cap A_3) = 0.01$

Compute the following probabilities and explain in words the meaning of each event:
- (a) $P(A_2 \\mid A_1)$
- (b) $P(A_2 \\cap A_3 \\mid A_1)$ *(from MMSA Ex. 58)*
- (c) $P(A_2 \\cup A_3 \\mid A_1)$
- (d) $P(A_1 \\cap A_2 \\cap A_3 \\mid A_1 \\cup A_2 \\cup A_3)$ *(from MMSA Ex. 58)*

**Complete working.**  
**(a) $P(A_2 \\mid A_1)$:**  
$$P(A_2 \\mid A_1) = \\frac{P(A_1 \\cap A_2)}{P(A_1)} = \\frac{0.11}{0.22} = 0.50$$
*Meaning:* Given that the firm is awarded Project 1, the probability that it is also awarded Project 2 is $0.50$ (50%).

**(b) $P(A_2 \\cap A_3 \\mid A_1)$:**  
$$P(A_2 \\cap A_3 \\mid A_1) = \\frac{P(A_1 \\cap (A_2 \\cap A_3))}{P(A_1)} = \\frac{P(A_1 \\cap A_2 \\cap A_3)}{P(A_1)} = \\frac{0.01}{0.22} = \\frac{1}{22} \\approx 0.045455$$
*Meaning:* Given that the firm is awarded Project 1, the probability that it is awarded both Project 2 and Project 3 (all three projects) is $1/22 \\approx 4.55\\%$.

**(c) $P(A_2 \\cup A_3 \\mid A_1)$:**  
By the distributive law of sets:
$$(A_2 \\cup A_3) \\cap A_1 = (A_1 \\cap A_2) \\cup (A_1 \\cap A_3)$$
By the addition rule for probabilities:
$$P((A_2 \\cup A_3) \\cap A_1) = P(A_1 \\cap A_2) + P(A_1 \\cap A_3) - P((A_1 \\cap A_2) \\cap (A_1 \\cap A_3))$$
$$= P(A_1 \\cap A_2) + P(A_1 \\cap A_3) - P(A_1 \\cap A_2 \\cap A_3) = 0.11 + 0.05 - 0.01 = 0.15$$
Applying conditional probability:
$$P(A_2 \\cup A_3 \\mid A_1) = \\frac{0.15}{P(A_1)} = \\frac{0.15}{0.22} = \\frac{15}{22} \\approx 0.681818$$
*Meaning:* Given that Project 1 is awarded, the probability that the firm is awarded at least one of Project 2 or Project 3 is $15/22 \\approx 68.18\\%$.

**(d) $P(A_1 \\cap A_2 \\cap A_3 \\mid A_1 \\cup A_2 \\cup A_3)$:**  
First, compute the probability of the union $P(A_1 \\cup A_2 \\cup A_3)$ by the Principle of Inclusion-Exclusion:
$$P(A_1 \\cup A_2 \\cup A_3) = [P(A_1) + P(A_2) + P(A_3)] - [P(A_1 \\cap A_2) + P(A_1 \\cap A_3) + P(A_2 \\cap A_3)] + P(A_1 \\cap A_2 \\cap A_3)$$
$$= [0.22 + 0.25 + 0.28] - [0.11 + 0.05 + 0.07] + 0.01 = 0.75 - 0.23 + 0.01 = 0.53$$
Because the intersection $(A_1 \\cap A_2 \\cap A_3)$ is a subset of the union $(A_1 \\cup A_2 \\cup A_3)$, their intersection is simply the three-way intersection itself.
$$P(A_1 \\cap A_2 \\cap A_3 \\mid A_1 \\cup A_2 \\cup A_3) = \\frac{P(A_1 \\cap A_2 \\cap A_3)}{P(A_1 \\cup A_2 \\cup A_3)} = \\frac{0.01}{0.53} = \\frac{1}{53} \\approx 0.018868$$
*Meaning:* Given that the firm is awarded at least one project, the probability that it is awarded all three projects is $1/53 \\approx 1.89\\%$.

**Answer.**  
- (a) $P(A_2 \\mid A_1) = 0.50$.
- (b) $P(A_2 \\cap A_3 \\mid A_1) = \\frac{1}{22} \\approx 0.0455$.
- (c) $P(A_2 \\cup A_3 \\mid A_1) = \\frac{15}{22} \\approx 0.6818$.
- (d) $P(A_1 \\cap A_2 \\cap A_3 \\mid A_1 \\cup A_2 \\cup A_3) = \\frac{1}{53} \\approx 0.0189$.

---

### Slide 9: Try It Yourself! — Standard Card Deck Conditional Probabilities

**Source identification:** `W3/Week 3.pdf`, Slide 9 ("Try it yourself!").  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
You pick a card at random from a standard 52-card deck (13 ranks, 4 suits: diamonds $\\diamondsuit$, hearts $\\heartsuit$, clubs $\\clubsuit$, spades $\\spadesuit$). Let $Q$ denote the event of drawing a Queen of Hearts, and $R$ denote the event of drawing a red card. Describe each event below and find its probability:
- (a) $P(Q \\mid R)$
- (b) $P(R \\mid Q)$
- (c) $P(Q^c \\mid R)$

**Complete working.**  
The sample space $\\Omega$ contains 52 equally likely outcomes.
- Event $Q$ = $\\{\\text{Queen of Hearts}\\}$ $\\implies |Q| = 1$, $P(Q) = 1/52$.
- Event $R$ = $\\{\\text{all hearts and diamonds}\\}$ $\\implies |R| = 26$, $P(R) = 26/52 = 1/2$.
- Note that the Queen of Hearts is a heart (red card), so $Q \\subseteq R$. Consequently, $Q \\cap R = Q$, and $P(Q \\cap R) = P(Q) = 1/52$.

**(a) $P(Q \\mid R)$:**  
*Description:* The probability of drawing the Queen of Hearts given that the drawn card is red.
$$P(Q \\mid R) = \\frac{P(Q \\cap R)}{P(R)} = \\frac{1/52}{26/52} = \\frac{1}{26} \\approx 0.038462$$

**(b) $P(R \\mid Q)$:**  
*Description:* The probability that the card is red given that it is the Queen of Hearts.
$$P(R \\mid Q) = \\frac{P(R \\cap Q)}{P(Q)} = \\frac{1/52}{1/52} = 1.00$$
Since every Queen of Hearts is guaranteed to be a red card, the condition establishes certainty.

**(c) $P(Q^c \\mid R)$:**  
*Description:* The probability that the card is *not* the Queen of Hearts given that it is a red card.  
By the complement rule on the conditioned space:
$$P(Q^c \\mid R) = 1 - P(Q \\mid R) = 1 - \\frac{1}{26} = \\frac{25}{26} \\approx 0.961538$$
Alternatively, among the 26 red cards, exactly 25 are not the Queen of Hearts: $25/26$.

**Answer.**  
- (a) $P(Q \\mid R) = \\frac{1}{26} \\approx 0.0385$.
- (b) $P(R \\mid Q) = 1.00$ (certain).
- (c) $P(Q^c \\mid R) = \\frac{25}{26} \\approx 0.9615$.

---

### Slide 13: Check Your Understanding! — Flight Delay Independence

**Source identification:** `W3/Week 3.pdf`, Slide 13 ("Check your understanding!").  
**Relevant PT ID(s):** [PT-03](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics).

**Complete question statement.**  
Consider two events:
- $A = \\{\\text{Arriving flight is delayed by at least 15 minutes}\\}$ with $P(A) = 0.20$.
- $D = \\{\\text{Departing flight is delayed by at least 15 minutes}\\}$ with $P(D) = 0.25$.
- $P(A \\cap D) = 0.16$.

Determine numerically whether events $A$ and $D$ are independent. Explain using conditional probabilities whether they are independent.

**Complete working.**  
- **Numerical Test via Product Rule:**  
  Two events are independent if and only if $P(A \\cap D) = P(A) \\cdot P(D)$.
  - Observed joint probability: $P(A \\cap D) = 0.16$.
  - Product of marginals: $P(A) \\cdot P(D) = 0.20 \\times 0.25 = 0.05$.
  Since $0.16 \\neq 0.05$, events $A$ and $D$ are **not statistically independent (they are dependent)**.

- **Explanation via Conditional Probabilities:**  
  Compute the conditional probability of an arrival delay given a departure delay:
  $$P(A \\mid D) = \\frac{P(A \\cap D)}{P(D)} = \\frac{0.16}{0.25} = 0.64$$
  Compare this to the baseline unconditional probability:
  $$P(A) = 0.20$$
  Since $P(A \\mid D) = 0.64 > 0.20 = P(A)$, knowing that the departing flight is delayed dramatically increases the probability of an arrival delay (more than tripling it). Symmetrically:
  $$P(D \\mid A) = \\frac{P(A \\cap D)}{P(A)} = \\frac{0.16}{0.20} = 0.80 > 0.25 = P(D)$$
  Because the occurrence of one event significantly alters the probability of the other, they are strongly dependent.

**Answer.**  
$A$ and $D$ are **not independent** because $P(A \\cap D) = 0.16 \\neq 0.05 = P(A)P(D)$. In conditional terms, $P(A \\mid D) = 0.64 \\neq P(A) = 0.20$.

---

### Slide 15: Example 3 — System Reliability via Indirect (Complement) Approach

**Source identification:** `W3/Week 3.pdf`, Slide 15 ("Example 3 - Indirect Approach").  
**Relevant PT ID(s):** [PT-04](#problem-type-pt-04-system-reliability-and-network-flow-modeling-with-independent-components).

**Complete question statement.**  
The system below is comprised of independent components. The probability that each numbered component will work is $0.90, 0.95,$ and $0.99$, respectively. An electrical signal will travel from left to right if there is a path of functioning components. Component 1 and Component 2 are connected in parallel; this parallel block is connected in series with Component 3. Find the probability that the signal is blocked.

**Complete working.**  
Let $C_1, C_2, C_3$ be the events that Components 1, 2, and 3 work, with:
- $P(C_1) = 0.90 \\implies P(C_1^c) = 0.10$
- $P(C_2) = 0.95 \\implies P(C_2^c) = 0.05$
- $P(C_3) = 0.99 \\implies P(C_3^c) = 0.01$

- **Step 1: Operational probability of the parallel block ($C_1 \\cup C_2$):**  
  The parallel block fails if and only if both components fail. Since components operate independently:
  $$P(\\text{Parallel Fails}) = P(C_1^c \\cap C_2^c) = P(C_1^c) \\cdot P(C_2^c) = 0.10 \\times 0.05 = 0.005$$
  $$P(\\text{Parallel Works}) = 1 - P(C_1^c \\cap C_2^c) = 1 - 0.005 = 0.995$$

- **Step 2: Operational probability of the overall system:**  
  The system functions if and only if the parallel block works **and** Component 3 works:
  $$\\text{System Works} = (C_1 \\cup C_2) \\cap C_3$$
  Because Component 3 is independent of Components 1 and 2:
  $$P(\\text{System Works}) = P(C_1 \\cup C_2) \\cdot P(C_3) = 0.995 \\times 0.99 = 0.98505$$

- **Step 3: Indirect evaluation of signal blockage:**  
  The signal is blocked if and only if the system fails to transmit:
  $$P(\\text{Signal Blocked}) = 1 - P(\\text{System Works}) = 1 - 0.98505 = 0.01495$$

*Direct Cut-Set Verification:*  
A signal is blocked if Component 3 fails ($C_3^c$) OR both parallel components fail ($C_1^c \\cap C_2^c$):
$$P(\\text{Blocked}) = P(C_3^c \\cup (C_1^c \\cap C_2^c)) = P(C_3^c) + P(C_1^c \\cap C_2^c) - P(C_3^c \\cap C_1^c \\cap C_2^c)$$
$$= 0.01 + 0.005 - (0.01 \\times 0.005) = 0.015 - 0.00005 = 0.01495$$
The direct and indirect approaches agree exactly.

**Answer.**  
$P(\\text{Signal is Blocked}) = 0.01495$ (1.495%).

---

### Slide 19: Handedness Translation Question

**Source identification:** `W3/Week 3.pdf`, Slide 19 ("Law of Total Probability" introductory translation).  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction), [PT-02](#problem-type-pt-02-multi-stage-sequential-intersection-via-the-general-multiplication--chain-rule).

**Complete question statement.**  
In a group of 100 people, 40 write left-handed. Half of left-handed people are also left-handed in sports. How many people are left-handed in both writing and sports?

**Complete working.**  
Let the population size be $N = 100$.
- Let $W$ be the event that a person writes left-handed. $n(W) = 40 \\implies P(W) = 40/100 = 0.40$.
- Let $S$ be the event that a person is left-handed in sports.
- The phrase *"Half of left-handed people also left-handed in sports"* defines the conditional probability:
  $$P(S \\mid W) = 0.50$$
Applying the multiplication rule for conditional probability:
$$P(W \\cap S) = P(S \\mid W) \\cdot P(W) = 0.50 \\times 0.40 = 0.20$$
The number of people who are left-handed in both writing and sports is:
$$n(W \\cap S) = N \\times P(W \\cap S) = 100 \\times 0.20 = 20 \\text{ people}$$
Equivalently: $n(W \\cap S) = 0.50 \\times n(W) = 0.50 \\times 40 = 20$.

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

**(a) Probability red ball drawn on both draws ($P(R_1 \\cap R_2)$):**  
Applying the multiplication rule:
$$P(R_1 \\cap R_2) = P(R_2 \\mid R_1) \\cdot P(R_1)$$
Given $R_1$, the urn contains 3 red balls out of 4 total $\\implies P(R_2 \\mid R_1) = 3/4$.
$$P(R_1 \\cap R_2) = \\frac{3}{4} \\times \\frac{1}{2} = \\frac{3}{8} = 0.375$$

**(b) Probability that the second ball drawn is red ($P(R_2)$):**  
The outcomes of the first draw $\\{R_1, W_1\\}$ partition the sample space. By the Law of Total Probability:
$$P(R_2) = P(R_2 \\mid R_1)P(R_1) + P(R_2 \\mid W_1)P(W_1)$$
Given $W_1$, the urn contains 1 red ball out of 2 total $\\implies P(R_2 \\mid W_1) = 1/2$.
$$P(R_2) = \\left(\\frac{3}{4} \\times \\frac{1}{2}\\right) + \\left(\\frac{1}{2} \\times \\frac{1}{2}\\right) = \\frac{3}{8} + \\frac{1}{4} = \\frac{3}{8} + \\frac{2}{8} = \\frac{5}{8} = 0.625$$

**(c) Probability the first ball was red given the second ball is red ($P(R_1 \\mid R_2)$):**  
Applying Bayes' Rule:
$$P(R_1 \\mid R_2) = \\frac{P(R_1 \\cap R_2)}{P(R_2)} = \\frac{3/8}{5/8} = \\frac{3}{5} = 0.60$$

**Answer.**  
- (a) $P(R_1 \\cap R_2) = \\frac{3}{8} = 0.375$.
- (b) $P(R_2) = \\frac{5}{8} = 0.625$.
- (c) $P(R_1 \\mid R_2) = \\frac{3}{5} = 0.60$.

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
- Prevalence: $P(D^c) = 0.98 \\implies P(D) = 1 - 0.98 = 0.02$ (2% baseline infection rate).
- Sensitivity: $P(+ \\mid D) = 0.95$.
- False positive rate: $P(+ \\mid D^c) = 0.01$.

We seek the Positive Predictive Value $P(D \\mid +)$.
- **Step 1: Total probability of testing positive ($P(+)$):**  
  Applying the Law of Total Probability:
  $$P(+) = P(+ \\mid D)P(D) + P(+ \\mid D^c)P(D^c)$$
  $$P(+) = (0.95 \\times 0.02) + (0.01 \\times 0.98) = 0.0190 + 0.0098 = 0.0288$$

- **Step 2: Inverting via Bayes' Rule:**  
  $$P(D \\mid +) = \\frac{P(+ \\mid D)P(D)}{P(+)} = \\frac{0.0190}{0.0288} = \\frac{190}{288} = \\frac{95}{144} \\approx 0.659722$$

*Clinical Interpretation:* Even with a 95% sensitive test and a very low 1% false positive rate, approximately $34\\%$ of positive tests are false alarms. This occurs because the healthy population ($98\\%$) is 49 times larger than the infected population ($2\\%$), generating a substantial volume of false positives.

**Answer.**  
$P(D \\mid +) = \\frac{95}{144} \\approx 0.6597$ (65.97%).

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
- $P(L \\mid E_1) = 0.02$
- $P(L \\mid E_2) = 0.01$
- $P(L \\mid E_3) = 0.05$

**(a) Overall probability parcel arrived late ($P(L)$):**  
Applying the Law of Total Probability:
$$P(L) = P(L \\mid E_1)P(E_1) + P(L \\mid E_2)P(E_2) + P(L \\mid E_3)P(E_3)$$
$$P(L) = (0.02 \\times 0.40) + (0.01 \\times 0.50) + (0.05 \\times 0.10)$$
$$P(L) = 0.0080 + 0.0050 + 0.0050 = 0.0180$$
Overall, 1.80% of overnight parcels arrive late.

**(b) Probability parcel was sent by $E_1$ given it arrived late ($P(E_1 \\mid L)$):**  
Applying Bayes' Rule:
$$P(E_1 \\mid L) = \\frac{P(L \\mid E_1)P(E_1)}{P(L)} = \\frac{0.0080}{0.0180} = \\frac{8}{18} = \\frac{4}{9} \\approx 0.444444$$

**Answer.**  
- (a) $P(L) = 0.0180$ (1.80%).
- (b) $P(E_1 \\mid L) = \\frac{4}{9} \\approx 0.4444$ (44.44%).

---

### Slide 28: Monty Hall Problem — Bayesian Formulation

**Source identification:** `W3/Week 3.pdf`, Slide 28 ("Monty Hall Problem").  
**Relevant PT ID(s):** [PT-07](#problem-type-pt-07-posterior-probability-inversion-via-bayes-rule).

**Complete question statement.**  
In the classic Monty Hall game show setup, a contestant faces three closed doors: behind one door is a car, and behind the other two are goats. The contestant initially chooses Door 1. Host Monty Hall, who knows the location of the car, opens one of the remaining doors (say, Door 3) to reveal a goat. Monty then offers the contestant the option to switch to Door 2. Using Bayes' Rule, determine whether the contestant should switch.

**Complete working.**  
Let $C_i$ be the event that the car is behind Door $i$ for $i \\in \\{1, 2, 3\\}$.
- Prior distribution: $P(C_1) = P(C_2) = P(C_3) = \\frac{1}{3}$.

Assume without loss of generality that the contestant picks Door 1. Let $M_3$ be the event that Monty Hall opens Door 3. Monty operates under the strict rules:
1. Monty never opens Door 1 (the contestant's choice).
2. Monty never opens the door hiding the car.
3. If Monty has a choice between two goat doors (which happens when the car is behind Door 1), he chooses either door with equal probability $1/2$.

The conditional likelihoods of Monty opening Door 3 are:
- If car is behind Door 1 ($C_1$): Monty chooses between Door 2 and Door 3 at random $\\implies P(M_3 \\mid C_1) = 1/2$.
- If car is behind Door 2 ($C_2$): Door 1 is picked by contestant, Door 2 has car; Monty is forced to open Door 3 $\\implies P(M_3 \\mid C_2) = 1$.
- If car is behind Door 3 ($C_3$): Monty cannot reveal the car $\\implies P(M_3 \\mid C_3) = 0$.

Applying the Law of Total Probability to find $P(M_3)$:
$$P(M_3) = P(M_3 \\mid C_1)P(C_1) + P(M_3 \\mid C_2)P(C_2) + P(M_3 \\mid C_3)P(C_3)$$
$$P(M_3) = \\left(\\frac{1}{2} \\times \\frac{1}{3}\\right) + \\left(1 \\times \\frac{1}{3}\\right) + \\left(0 \\times \\frac{1}{3}\\right) = \\frac{1}{6} + \\frac{1}{3} = \\frac{1}{2}$$

Now apply Bayes' Rule to compare staying (Door 1) versus switching (Door 2):
- **Posterior probability for staying with Door 1:**
  $$P(C_1 \\mid M_3) = \\frac{P(M_3 \\mid C_1)P(C_1)}{P(M_3)} = \\frac{1/6}{1/2} = \\frac{1}{3}$$
- **Posterior probability for switching to Door 2:**
  $$P(C_2 \\mid M_3) = \\frac{P(M_3 \\mid C_2)P(C_2)}{P(M_3)} = \\frac{1/3}{1/2} = \\frac{2}{3}$$

*Conclusion:* Switching doors doubles the contestant's probability of winning the car from $1/3$ to $2/3$.

**Answer.**  
The contestant should **switch**, as $P(\\text{Win} \\mid \\text{Switch}) = \\frac{2}{3}$, whereas $P(\\text{Win} \\mid \\text{Stay}) = \\frac{1}{3}$.

---

### Slide 32: Random Variable Definition — Coin Toss Outcome Mappings

**Source identification:** `W3/Week 3.pdf`, Slide 32 ("Random Variable").  
**Relevant PT ID(s):** [PT-09](#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping).

**Complete question statement.**  
Fill in the formal definitions and mappings for the qualitative coin tossing sample spaces presented in lecture:
- (a) For a single coin toss with $\\Omega = \\{H, T\\}$, define a standard indicator random variable $X$ and state its mapping.
- (b) For an experiment consisting of 3 coin tosses with $\\Omega = \\{HHH, HHT, HTH, THH, HTT, THT, TTH, TTT\\}$, define the random variable $X$ representing the number of heads that landed, list its value for each elementary outcome $\\omega \\in \\Omega$, and state its support $\\mathcal{X}$.

**Complete working.**  
**(a) Single Coin Toss:**  
The sample space is $\\Omega = \\{H, T\\}$. The standard numerical indicator variable $X: \\Omega \\to \\mathbb{R}$ is defined by:
$$X(\\omega) = \\begin{cases} 1 & \\text{if } \\omega = H \\\\ 0 & \\text{if } \\omega = T \\end{cases}$$
Support: $\\mathcal{X} = \\{0, 1\\}$. (This is the canonical Bernoulli random variable).

**(b) Three Coin Tosses:**  
Let $X: \\Omega \\to \\mathbb{R}$ denote the number of heads obtained in the 3 tosses.
Evaluating $X(\\omega)$ for each of the 8 outcomes:
- $X(TTT) = 0$
- $X(HTT) = X(THT) = X(TTH) = 1$
- $X(HHT) = X(HTH) = X(THH) = 2$
- $X(HHH) = 3$

The support of $X$ is:
$$\\mathcal{X} = \\{0, 1, 2, 3\\}$$
Pre-image event cardinalities and probabilities (assuming fair coins):
- $\\{X = 0\\} = \\{TTT\\} \\implies P(X = 0) = 1/8$
- $\\{X = 1\\} = \\{HTT, THT, TTH\\} \\implies P(X = 1) = 3/8$
- $\\{X = 2\\} = \\{HHT, HTH, THH\\} \\implies P(X = 2) = 3/8$
- $\\{X = 3\\} = \\{HHH\\} \\implies P(X = 3) = 1/8$

**Answer.**  
- (a) $X(H) = 1, X(T) = 0$; $\\mathcal{X} = \\{0, 1\\}$.
- (b) $X \\in \\{0, 1, 2, 3\\}$; mapping counts heads per sequence; probabilities are $1/8, 3/8, 3/8, 1/8$.

---

### Slide 35: Example 6 — Quadratic PMF Normalization Constant

**Source identification:** `W3/Week 3.pdf`, Slide 35 ("Example 6").  
**Relevant PT ID(s):** [PT-10](#problem-type-pt-10-pmf-normalization-parameter-determination-and-validation).

**Complete question statement.**  
Determine the value of $k$ such that:
$$P(X = x) = \\frac{k x^2 - x + 2}{4}$$
will be a valid probability mass function for the discrete support $\\mathcal{X} = \\{0, 1, 2, 3, 4\\}$.

**Complete working.**  
A valid PMF must satisfy two axioms:
1. Normalization: $\\sum_{x \\in \\mathcal{X}} P(X = x) = 1$.
2. Non-negativity: $P(X = x) \\ge 0$ for all $x \\in \\mathcal{X}$.

- **Step 1: Normalization Summation:**  
  $$\\sum_{x=0}^4 \\frac{k x^2 - x + 2}{4} = 1 \\implies \\sum_{x=0}^4 (k x^2 - x + 2) = 4$$
  Expand the sum term by term for $x = 0, 1, 2, 3, 4$:
  - $x = 0$: $k(0)^2 - 0 + 2 = 2$
  - $x = 1$: $k(1)^2 - 1 + 2 = k + 1$
  - $x = 2$: $k(2)^2 - 2 + 2 = 4k$
  - $x = 3$: $k(3)^2 - 3 + 2 = 9k - 1$
  - $x = 4$: $k(4)^2 - 4 + 2 = 16k - 2$

  Summing these five expressions:
  $$\\sum_{x=0}^4 (k x^2 - x + 2) = (k + 4k + 9k + 16k) + (2 + 1 + 0 - 1 - 2) = 30k + 0 = 30k$$
  Set the sum equal to 4:
  $$30k = 4 \\implies k = \\frac{4}{30} = \\frac{2}{15} \\approx 0.133333$$

- **Step 2: Non-Negativity Verification (Axiom 1):**  
  Substitute $k = \\frac{2}{15}$ back into the numerator $g(x) = \\frac{2}{15}x^2 - x + 2$ for each $x$:
  - For $x = 0$: $P(X = 0) = \\frac{2}{4} = \\frac{1}{2} = \\frac{30}{60} > 0$
  - For $x = 1$: $P(X = 1) = \\frac{2/15 + 1}{4} = \\frac{17/15}{4} = \\frac{17}{60} > 0$
  - For $x = 2$: $P(X = 2) = \\frac{4(2/15)}{4} = \\frac{2}{15} = \\frac{8}{60} > 0$
  - For $x = 3$: $P(X = 3) = \\frac{9(2/15) - 1}{4} = \\frac{18/15 - 1}{4} = \\frac{3/15}{4} = \\frac{1}{20} = \\frac{3}{60} > 0$
  - For $x = 4$: $P(X = 4) = \\frac{16(2/15) - 2}{4} = \\frac{32/15 - 30/15}{4} = \\frac{2/15}{4} = \\frac{2}{60} = \\frac{1}{30} > 0$

  Check sum:
  $$\\sum_{x=0}^4 P(X = x) = \\frac{30 + 17 + 8 + 3 + 2}{60} = \\frac{60}{60} = 1.00$$
  Since all point probabilities are strictly positive and bounded by 1, $k = 2/15$ defines a valid PMF.

**Answer.**  
$k = \\frac{2}{15}$.

---
"""

with open(OUTPUT_PATH, "a", encoding="utf-8") as f:
    f.write(section_b)
print("Section B appended.")
