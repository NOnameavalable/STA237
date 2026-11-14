#!/usr/bin/env python3
"""
Writes Section C.1 (MMSA Exercises) to Answers-and-Practice.md.
"""

OUTPUT_PATH = "/Users/stevenli/Documents/University of toronto/STA237/W3/Study-Notes-Markdown/Answers-and-Practice.md"

section_c1 = """
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
- $A = \\{\\text{type A selected}\\}$
- $B = \\{\\text{type B selected}\\}$
- $C = \\{\\text{ethnic group 3 selected}\\}$
- (a) Calculate $P(A)$, $P(C)$, and $P(A \\cap C)$.
- (b) Calculate both $P(A \\mid C)$ and $P(C \\mid A)$ and explain in context what each of these probabilities represents.
- (c) If the selected individual does not have type B blood, what is the probability that he or she is from ethnic group 1?

**Complete working.**  
- **(a) Calculate $P(A)$, $P(C)$, and $P(A \\cap C)$:**  
  Summing column A: $P(A) = 0.106 + 0.141 + 0.200 = 0.447$.  
  Summing row 3: $P(C) = 0.215 + 0.200 + 0.065 + 0.020 = 0.500$.  
  Intersection cell (Row 3, Col A): $P(A \\cap C) = 0.200$.

- **(b) Calculate $P(A \\mid C)$ and $P(C \\mid A)$ and interpret:**  
  $$P(A \\mid C) = \\frac{P(A \\cap C)}{P(C)} = \\frac{0.200}{0.500} = 0.400$$
  *Meaning:* Given that a selected individual belongs to ethnic group 3, the probability that they have type A blood is $0.400$ (40.0%).
  $$P(C \\mid A) = \\frac{P(A \\cap C)}{P(A)} = \\frac{0.200}{0.447} = \\frac{200}{447} \\approx 0.447427$$
  *Meaning:* Given that a selected individual is observed to have type A blood, the probability that they belong to ethnic group 3 is approximately $0.4474$ (44.74%).

- **(c) Probability of ethnic group 1 given NOT type B blood ($P(E_1 \\mid B^c)$):**  
  Let $E_1$ denote ethnic group 1.
  The conditioning event is $B^c$ (does not have type B blood).
  $$P(B^c) = 1 - P(B) = 1 - 0.091 = 0.909$$
  The joint event $E_1 \\cap B^c$ consists of ethnic group 1 individuals with blood groups O, A, or AB:
  $$P(E_1 \\cap B^c) = 0.082 + 0.106 + 0.004 = 0.192 \\quad \\text{(or } 0.200 - 0.008 = 0.192\\text{)}$$
  Applying conditional probability:
  $$P(E_1 \\mid B^c) = \\frac{P(E_1 \\cap B^c)}{P(B^c)} = \\frac{0.192}{0.909} = \\frac{192}{909} = \\frac{64}{303} \\approx 0.211221$$

**Answer.**  
- (a) $P(A) = 0.447$, $P(C) = 0.500$, $P(A \\cap C) = 0.200$.
- (b) $P(A \\mid C) = 0.400$; $P(C \\mid A) \\approx 0.4474$.
- (c) $P(E_1 \\mid B^c) = \\frac{64}{303} \\approx 0.2112$.

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
     $$P(A \mid B) \approx 1 \quad (\text{or very close to } 100\%)$$
   - **$P(B \mid A)$:** The probability that a randomly chosen person is a professional basketball player, **given that he is over 6 ft tall**. In the general population, tens of millions of adult males exceed 6 ft in height, but top professional basketball leagues have roster spots for only a few hundred players. Out of all tall adult males, only a tiny fraction are professional athletes. Therefore:
     $$P(B \mid A) \approx 0 \quad (\text{an infinitesimal fraction close to zero})$$

2. **Mathematical Formalization via Bayes' Ratio & Real-World Data:**  
   Using the definition of conditional probability:
   $$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B \mid A) = \frac{P(A \cap B)}{P(A)}$$
   Dividing the two equations eliminates the common intersection $P(A \cap B)$:
   $$\frac{P(A \mid B)}{P(B \mid A)} = \frac{P(A)}{P(B)}$$
   In the US adult male population:
   - $P(A) \approx 0.15$ (roughly $15\%$ of adult males are over 6 ft tall).
   - $P(B) \approx \frac{500}{130,000,000} \approx 3.8 \times 10^{-6}$ (roughly 500 active pro players out of 130 million adult males).
   Because $P(A) \gg P(B)$ (by a factor of $\approx 40,000$), the ratio confirms:
   $$\frac{P(A \mid B)}{P(B \mid A)} \approx 40,000 \gg 1 \implies P(A \mid B) \gg P(B \mid A)$$

**Answer.**  
**Textbook Answer:** $P(A \mid B)$ is **much larger** than $P(B \mid A)$.  
Almost all professional basketball players are over 6 ft tall ($P(A \mid B) \approx 1$), whereas out of all adult males over 6 ft tall, only an infinitesimal fraction play professional basketball ($P(B \mid A) \approx 0$).

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
Given $A \\perp B$, $P(A) = 0.4$, $P(B) = 0.7$.

- **(a) Probability European project fails given Asian project fails ($P(B^c \\mid A^c)$):**  
  By the Independence of Complements Theorem, if $A$ and $B$ are independent, then their complements $A^c$ and $B^c$ are also independent ($A^c \\perp B^c$).  
  Therefore, the conditioning on $A^c$ provides zero informational influence on $B^c$:
  $$P(B^c \\mid A^c) = P(B^c) = 1 - P(B) = 1 - 0.7 = 0.3$$

- **(b) Probability at least one project is successful ($P(A \\cup B)$):**  
  Using the complement rule with independent complements:
  $$P(A \\cup B) = 1 - P(A^c \\cap B^c) = 1 - [P(A^c) \\cdot P(B^c)] = 1 - [(1 - 0.4)(1 - 0.7)] = 1 - (0.6 \\times 0.3) = 1 - 0.18 = 0.82$$
  *Alternative Check:* $P(A) + P(B) - P(A \\cap B) = 0.4 + 0.7 - (0.4 \\times 0.7) = 1.1 - 0.28 = 0.82$.

- **(c) Probability only Asian is successful given at least one is successful ($P(A \\cap B^c \\mid A \\cup B)$):**  
  The event "only Asian is successful" is $A \\cap B^c$.
  Because $(A \\cap B^c) \\subseteq (A \\cup B)$, the intersection $(A \\cap B^c) \\cap (A \\cup B) = A \\cap B^c$.
  By independence of $A$ and $B^c$:
  $$P(A \\cap B^c) = P(A) \\cdot P(B^c) = 0.4 \\times (1 - 0.7) = 0.4 \\times 0.3 = 0.12$$
  Applying conditional probability:
  $$P(A \\cap B^c \\mid A \\cup B) = \\frac{P(A \\cap B^c)}{P(A \\cup B)} = \\frac{0.12}{0.82} = \\frac{12}{82} = \\frac{6}{41} \\approx 0.146341$$

**Answer.**  
- (a) $P(B^c \\mid A^c) = 0.30$.
- (b) $P(A \\cup B) = 0.82$.
- (c) $P(A \\cap B^c \\mid A \\cup B) = \\frac{6}{41} \\approx 0.1463$.

---

##### Exercise MMSA 3.3 (p. 114)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 3.1, p. 114, Exercise 3.  
**Classification:** MMSA — Basic.  
**Relevant PT ID(s):** [PT-09](#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping).

**Complete question statement.**  
Using the experiment in Example 3.3 (which references Example 2.3, observing the number of pumps in use at two gas stations, each having 6 pumps, where outcomes are ordered pairs $(s_1, s_2)$ with $s_1, s_2 \in \{0, 1, 2, 3, 4, 5, 6\}$), define two more random variables and list the possible values of each.

**Complete working.**  
The sample space $\Omega$ consists of all $7 \times 7 = 49$ ordered pairs $(s_1, s_2)$, where $s_1$ is the number of pumps in use at Station 1 and $s_2$ is the number of pumps in use at Station 2. Example 3.3 already defined $X = s_1 + s_2$, $Y = s_1 - s_2$, and $U = \max(s_1, s_2)$.

We define two valid additional random variables mapping $\Omega \to \mathbb{R}$ matching the textbook solution manual:
1. **Random Variable 1 (Textbook Solutions Manual Definition):**  
   Let $M$ be the absolute value of the difference between the outcomes:
   $$M(s_1, s_2) = |s_1 - s_2|$$
   - Minimum value: Occurs when $s_1 = s_2$ (e.g., $(0, 0)$), giving $|s_1 - s_2| = 0$.
   - Maximum value: Occurs when one station has 6 pumps in use and the other has 0 (e.g., $(6, 0)$ or $(0, 6)$), giving $|6 - 0| = 6$.
   - Possible values: $\mathcal{M} = \{0, 1, 2, 3, 4, 5, 6\}$.

2. **Random Variable 2 (Textbook Solutions Manual Definition):**  
   Let $W = 1$ if the sum of the two resulting numbers is even and $W = 0$ otherwise (a Bernoulli random variable):
   $$W(s_1, s_2) = \begin{cases} 1 & \text{if } s_1 + s_2 \text{ is even} \\ 0 & \text{if } s_1 + s_2 \text{ is odd} \end{cases}$$
   - Possible values: $\mathcal{W} = \{0, 1\}$.

*(Alternative valid RV: $Z = \min(s_1, s_2)$ with possible values $\{0, 1, 2, 3, 4, 5, 6\}$.)*

**Answer.**  
**Textbook Answer:**  
- $M = \text{the absolute value of the difference between the outcomes } |s_1 - s_2|$; possible values $\{0, 1, 2, 3, 4, 5, 6\}$.
- $W = 1 \text{ if the sum of the two resulting numbers is even and } W = 0 \text{ otherwise}$ (a Bernoulli random variable); possible values $\{0, 1\}$.

---

##### Exercise MMSA 3.6 (p. 114)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 3.1, p. 114, Exercise 6.  
**Classification:** MMSA — Basic.  
**Relevant PT ID(s):** [PT-09](#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping).

**Complete question statement.**  
Starting at a fixed time, each car entering an intersection is observed to see whether it turns left ($L$), right ($R$), or goes straight ahead ($A$). The experiment terminates as soon as a car is observed to turn left. Let $X = \\text{the number of cars observed}$. What are possible $X$ values? List five outcomes and their associated $X$ values.

**Complete working.**  
- **Possible values of $X$:**  
  The experiment terminates upon observing the first left-turning car ($L$).
  The shortest possible sequence is that the very first car turns left ($L$), giving $X = 1$.
  The first left turn could theoretically occur on the 2nd car, 3rd car, or after any arbitrarily long sequence of non-left turns ($R$ or $A$).
  Therefore, the possible values of $X$ are the set of all positive integers:
  $$\\mathcal{X} = \\{1, 2, 3, 4, 5, \\dots\\} = \\mathbb{Z}^+$$
  This support is countably infinite.

- **Five specific outcomes and associated $X$ values:**  
  1. Outcome: $\\omega_1 = L \\implies X(\\omega_1) = 1$.
  2. Outcome: $\\omega_2 = RL \\implies X(\\omega_2) = 2$.
  3. Outcome: $\\omega_3 = AL \\implies X(\\omega_3) = 2$.
  4. Outcome: $\\omega_4 = ARL \\implies X(\\omega_4) = 3$.
  5. Outcome: $\\omega_5 = RAAL \\implies X(\\omega_5) = 4$.

**Answer.**  
Possible $X$ values: $\\{1, 2, 3, 4, \\dots\\}$ (all positive integers). Five outcomes: $L$ ($X=1$), $RL$ ($X=2$), $AL$ ($X=2$), $ARL$ ($X=3$), $RAAL$ ($X=4$).

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
  Chemical pH is a continuous chemical concentration measurement ($-\log_{10}[\text{H}^+]$), where 0 is the smallest possible pH and 14 is the largest possible pH.  
  Set of possible values: $\{y : 0 < y < 14\}$.  
  **Continuous (not discrete)**.

- **(g) $X =$ tension (psi) of a tennis racket:**  
  With $m$ and $M$ denoting the minimum and maximum possible string tensions, respectively, possible values are $\{x : m < x < M\}$.  
  **Continuous (not discrete)**.

- **(h) $X =$ total coin tosses for three individuals until a match ($HHH$ or $TTT$):**  
  In each round, all three individuals toss their coins simultaneously, meaning each trial requires **3 tosses** (one per person). If a match is obtained on round 1, exactly 3 tosses occurred; on round 2, $3 \times 2 = 6$ tosses occurred; on round $k$, $3k$ tosses occurred.  
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
Support: $\\mathcal{X} = \\{0, 1, 2, 3, 4\\}$.

- **(a) What is $p(4)$?**  
  By the normalization axiom of a PMF, $\\sum_{x=0}^4 p(x) = 1$:
  $$p(0) + p(1) + p(2) + p(3) + p(4) = 1$$
  $$0.30 + 0.25 + 0.20 + 0.15 + p(4) = 1 \\implies 0.90 + p(4) = 1 \\implies p(4) = 0.10$$

- **(b) Visual Representations (Line Graph and Probability Histogram):**  
  *(See graphical render in [Study-Notes.md: PMF Visual Representations](Study-Notes.md#3-probability-mass-function-pmf) and figure `graphs/pmf-distribution-visualization.png`)*
  - **Probability Histogram:** Centered at integers $x \\in \\{0, 1, 2, 3, 4\\}$ with bin width $1.0$ (spanning $[x - 0.5, x + 0.5]$). Heights equal $p(x)$: heights $0.30, 0.25, 0.20, 0.15, 0.10$. Total area $= 1.0 \\times 1.00 = 1.00$.
  - **Line Graph (Spike Plot):** Vertical line segments erected from $(x, 0)$ to $(x, p(x))$ with a circular point mass marker at the top.

- **(c) Evaluate $P(X \\ge 2)$ and $P(X > 2)$:**  
  - *At least two students ($P(X \\ge 2)$):*
    $$P(X \\ge 2) = p(2) + p(3) + p(4) = 0.20 + 0.15 + 0.10 = 0.45$$
    *(Or via complement: $1 - [p(0) + p(1)] = 1 - 0.55 = 0.45$)*
  - *More than two students ($P(X > 2)$):*
    $$P(X > 2) = p(3) + p(4) = 0.15 + 0.10 = 0.25$$

- **(d) Probability professor shows up:**  
  The definition of the random variable $X$ ("number of students who show up at a professor's office hours on a particular day") is predicated on the office hour taking place. In the context of probability modeling, this parameter is outside the domain of the random variable $X$ itself; given that the model specifies office hour attendance, the professor is presumed present with probability $1.0$ (or the condition is defined on the event that the office hour was held).

**Answer.**  
- (a) $p(4) = 0.10$.
- (b) Histogram and spike plot constructed; see `graphs/pmf-distribution-visualization.png`.
- (c) $P(X \\ge 2) = 0.45$; $P(X > 2) = 0.25$.
- (d) $1.0$ (under the foundational premise that the scheduled office hour occurs).

---

#### MMSA Medium Exercises

##### Exercise MMSA 2.57 (p. 84)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.4, p. 84, Exercise 57.  
**Classification:** MMSA — Medium.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
A certain shop repairs both audio and video components. Let $A$ denote the event that the next component brought in for repair is an audio component, and let $B$ be the event that the next component is an MP3 player (so the event $B$ is contained in $A$). Suppose that $P(A) = 0.6$ and $P(B) = 0.05$. What is $P(B \\mid A)$?

**Complete working.**  
We are given that $B \\subseteq A$ (every MP3 player is an audio component).
By set theory, whenever $B \\subseteq A$, the intersection is simply $B$:
$$A \\cap B = B$$
Applying the definition of conditional probability:
$$P(B \\mid A) = \\frac{P(A \\cap B)}{P(A)} = \\frac{P(B)}{P(A)}$$
Substitute the given values $P(B) = 0.05$ and $P(A) = 0.60$:
$$P(B \\mid A) = \\frac{0.05}{0.60} = \\frac{5}{60} = \\frac{1}{12} \\approx 0.083333$$

**Answer.**  
$P(B \\mid A) = \\frac{1}{12} \\approx 0.0833$ (8.33%).

---

##### Exercise MMSA 2.58 (p. 84)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.4, p. 84, Exercise 58.  
**Classification:** MMSA — Medium.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
In Exercise 15, $A_i = \\{\\text{awarded project } i\\}$, for $i = 1, 2, 3$. Use the probabilities given there:
- $P(A_1) = 0.22$, $P(A_2) = 0.25$, $P(A_3) = 0.28$
- $P(A_1 \\cap A_2) = 0.11$, $P(A_1 \\cap A_3) = 0.05$, $P(A_2 \\cap A_3) = 0.07$
- $P(A_1 \\cap A_2 \\cap A_3) = 0.01$
to compute the following probabilities, and explain in words the meaning of each one:
- (a) $P(A_2 \\mid A_1)$
- (b) $P(A_2 \\cap A_3 \\mid A_1)$
- (c) $P(A_2 \\cup A_3 \\mid A_1)$
- (d) $P(A_1 \\cap A_2 \\cap A_3 \\mid A_1 \\cup A_2 \\cup A_3)$

**Complete working.**  
*(This problem matches Lecture Example 2 exactly, with subparts (b) and (d) fully integrated).*

- **(a) $P(A_2 \\mid A_1)$:**  
  $$P(A_2 \\mid A_1) = \\frac{P(A_1 \\cap A_2)}{P(A_1)} = \\frac{0.11}{0.22} = 0.50$$
  *Meaning:* Given that Project 1 is awarded, the probability that Project 2 is also awarded is $0.50$ (50.0%).

- **(b) $P(A_2 \\cap A_3 \\mid A_1)$:**  
  $$P(A_2 \\cap A_3 \\mid A_1) = \\frac{P(A_1 \\cap A_2 \\cap A_3)}{P(A_1)} = \\frac{0.01}{0.22} = \\frac{1}{22} \\approx 0.045455$$
  *Meaning:* Given that Project 1 is awarded, the probability that both Projects 2 and 3 are also awarded (all three projects won) is $1/22 \\approx 4.55\\%$.

- **(c) $P(A_2 \\cup A_3 \\mid A_1)$:**  
  By distributive expansion: $(A_2 \\cup A_3) \\cap A_1 = (A_1 \\cap A_2) \\cup (A_1 \\cap A_3)$.
  $$P((A_1 \\cap A_2) \\cup (A_1 \\cap A_3)) = P(A_1 \\cap A_2) + P(A_1 \\cap A_3) - P(A_1 \\cap A_2 \\cap A_3) = 0.11 + 0.05 - 0.01 = 0.15$$
  $$P(A_2 \\cup A_3 \\mid A_1) = \\frac{0.15}{0.22} = \\frac{15}{22} \\approx 0.681818$$
  *Meaning:* Given that Project 1 is awarded, the probability that at least one of Project 2 or Project 3 is also awarded is $15/22 \\approx 68.18\\%$.

- **(d) $P(A_1 \\cap A_2 \\cap A_3 \\mid A_1 \\cup A_2 \\cup A_3)$:**  
  By PIE:
  $$P(A_1 \\cup A_2 \\cup A_3) = (0.22 + 0.25 + 0.28) - (0.11 + 0.05 + 0.07) + 0.01 = 0.75 - 0.23 + 0.01 = 0.53$$
  $$P(A_1 \\cap A_2 \\cap A_3 \\mid A_1 \\cup A_2 \\cup A_3) = \\frac{0.01}{0.53} = \\frac{1}{53} \\approx 0.018868$$
  *Meaning:* Given that at least one project is awarded to the firm, the probability that all three projects are awarded is $1/53 \\approx 1.89\\%$.

**Answer.**  
- (a) $P(A_2 \\mid A_1) = 0.50$.
- (b) $P(A_2 \\cap A_3 \\mid A_1) = \\frac{1}{22} \\approx 0.0455$.
- (c) $P(A_2 \\cup A_3 \\mid A_1) = \\frac{15}{22} \\approx 0.6818$.
- (d) $P(A_1 \\cap A_2 \\cap A_3 \\mid A_1 \\cup A_2 \\cup A_3) = \\frac{1}{53} \\approx 0.0189$.

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
  $P(D \\mid B_1) = 0.04$, $P(D \\mid B_2) = 0.08$, $P(D \\mid B_3) = 0.12$.

- **(a) Tree Diagram Structure:**  
  - Root branches into Plant I ($0.54$), Plant II ($0.35$), Plant III ($0.11$).
  - From Plant I: Defective ($0.04$), Good ($0.96$). Joint $P(B_1 \\cap D) = 0.54 \\times 0.04 = 0.0216$.
  - From Plant II: Defective ($0.08$), Good ($0.92$). Joint $P(B_2 \\cap D) = 0.35 \\times 0.08 = 0.0280$.
  - From Plant III: Defective ($0.12$), Good ($0.88$). Joint $P(B_3 \\cap D) = 0.11 \\times 0.12 = 0.0132$.

- **(b) Probability defective and from Plant II ($P(B_2 \\cap D)$):**  
  $$P(B_2 \\cap D) = P(D \\mid B_2) \\cdot P(B_2) = 0.08 \\times 0.35 = 0.0280 \\quad (2.80\\%)$$

- **(c) Overall probability of a defective hard drive ($P(D)$):**  
  Applying the Law of Total Probability:
  $$P(D) = P(B_1 \\cap D) + P(B_2 \\cap D) + P(B_3 \\cap D) = 0.0216 + 0.0280 + 0.0132 = 0.0628 \\quad (6.28\\%)$$

- **(d) Probability defective came from Plant II ($P(B_2 \\mid D)$):**  
  Applying Bayes' Rule:
  $$P(B_2 \\mid D) = \\frac{P(B_2 \\cap D)}{P(D)} = \\frac{0.0280}{0.0628} = \\frac{280}{628} = \\frac{70}{157} \\approx 0.445860 \\quad (44.59\\%)$$

**Answer.**  
- (a) Tree diagram described above.
- (b) $P(B_2 \\cap D) = 0.0280$ (2.80%).
- (c) $P(D) = 0.0628$ (6.28%).
- (d) $P(B_2 \\mid D) = \\frac{70}{157} \\approx 0.4459$ (44.59%).

---

##### Exercise MMSA 2.64 (p. 84)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.4, p. 84, Exercise 64.  
**Classification:** MMSA — Medium.  
**Relevant PT ID(s):** [PT-05](#problem-type-pt-05-total-probability-computation-via-partition-decompositions-and-tree-diagrams), [PT-07](#problem-type-pt-07-posterior-probability-inversion-via-bayes-rule).

**Complete question statement.**  
At a gas station, 40% of the customers use regular gas ($A_1$), 35% use midgrade gas ($A_2$), and 25% use premium gas ($A_3$). Of those customers using regular gas, only 30% fill their tanks (event $B$). Of those customers using midgrade gas, 60% fill their tanks, whereas of those using premium, 50% fill their tanks.
- (a) What is the probability that the next customer will request midgrade gas and fill the tank ($A_2 \\cap B$)?
- (b) What is the probability that the next customer fills the tank?
- (c) If the next customer fills the tank, what is the probability that regular gas is requested? Midgrade gas? Premium gas?

**Complete working.**  
Priors: $P(A_1) = 0.40, P(A_2) = 0.35, P(A_3) = 0.25$.
Conditional fill rates: $P(B \\mid A_1) = 0.30, P(B \\mid A_2) = 0.60, P(B \\mid A_3) = 0.50$.

- **(a) $P(A_2 \\cap B)$:**  
  $$P(A_2 \\cap B) = P(B \\mid A_2) \\cdot P(A_2) = 0.60 \\times 0.35 = 0.210$$

- **(b) Total probability customer fills tank ($P(B)$):**  
  Applying the Law of Total Probability:
  $$P(B) = P(B \\mid A_1)P(A_1) + P(B \\mid A_2)P(A_2) + P(B \\mid A_3)P(A_3)$$
  $$P(B) = (0.30 \\times 0.40) + (0.60 \\times 0.35) + (0.50 \\times 0.25)$$
  $$P(B) = 0.120 + 0.210 + 0.125 = 0.455$$

- **(c) Posterior probabilities given customer fills tank ($B$):**  
  - *Regular ($A_1$):*
    $$P(A_1 \\mid B) = \\frac{P(A_1 \\cap B)}{P(B)} = \\frac{0.120}{0.455} = \\frac{120}{455} = \\frac{24}{91} \\approx 0.263736 \\quad (26.37\\%)$$
  - *Midgrade ($A_2$):*
    $$P(A_2 \\mid B) = \\frac{P(A_2 \\cap B)}{P(B)} = \\frac{0.210}{0.455} = \\frac{210}{455} = \\frac{42}{91} = \\frac{6}{13} \\approx 0.461538 \\quad (46.15\\%)$$
  - *Premium ($A_3$):*
    $$P(A_3 \\mid B) = \\frac{P(A_3 \\cap B)}{P(B)} = \\frac{0.125}{0.455} = \\frac{125}{455} = \\frac{25}{91} \\approx 0.274725 \\quad (27.47\\%)$$
  Sum check: $\\frac{24 + 42 + 25}{91} = \\frac{91}{91} = 1.00$.

**Answer.**  
- (a) $P(A_2 \\cap B) = 0.210$ (21.0%).
- (b) $P(B) = 0.455$ (45.5%).
- (c) $P(A_1 \\mid B) = \\frac{24}{91} \\approx 0.2637$; $P(A_2 \\mid B) = \\frac{6}{13} \\approx 0.4615$; $P(A_3 \\mid B) = \\frac{25}{91} \\approx 0.2747$.

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
We are given that $E_1, \\dots, E_n$ are mutually independent events with $P(E_i) = p$.
The probability of marking question $i$ correctly is $P(E_i^c) = 1 - p$.

- **No errors made on $n=10$ questions ($p=0.1$):**  
  No errors means that all 10 questions are marked correctly ($E_1^c \\cap E_2^c \\cap \\cdots \\cap E_{10}^c$).
  By mutual independence:
  $$P(\\text{No Errors}) = \\prod_{i=1}^{10} P(E_i^c) = (1 - 0.1)^{10} = (0.9)^{10} \\approx 0.348678$$

- **At least one error made on $n=10$ questions:**  
  Applying the complement rule:
  $$P(\\ge 1 \\text{ Error}) = 1 - P(\\text{No Errors}) = 1 - (0.9)^{10} \\approx 1 - 0.348678 = 0.651322$$

- **General expressions for $n$ questions with error rate $p$:**  
  - $P(\\text{No Errors}) = (1 - p)^n$.
  - $P(\\text{At Least One Error}) = 1 - (1 - p)^n$.

**Answer.**  
- $P(\\text{No Errors, } 10) = (0.9)^{10} \\approx 0.3487$ (34.87%).
- $P(\\ge 1 \\text{ Error, } 10) = 1 - (0.9)^{10} \\approx 0.6513$ (65.13%).
- General: No errors $= (1 - p)^n$; At least one error $= 1 - (1 - p)^n$.

---

##### Exercise MMSA 2.83 (p. 92)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.5, p. 92, Exercise 83.  
**Classification:** MMSA — Medium.  
**Relevant PT ID(s):** [PT-04](#problem-type-pt-04-system-reliability-and-network-flow-modeling-with-independent-components).

**Complete question statement.**  
Consider the system of components connected as in the accompanying picture. Components 1 and 2 are connected in parallel, so that subsystem works if and only if either 1 or 2 works; since 3 and 4 are connected in series, that subsystem works if and only if both 3 and 4 work. The parallel subsystem (1, 2) and the series subsystem (3, 4) are themselves connected in parallel across the main system terminals. If components work independently of one another and $P(\\text{component works}) = 0.9$, calculate $P(\\text{system works})$.

**Complete working.**  
Let $C_i$ denote the event that component $i$ functions, with $P(C_i) = p = 0.90$ for $i = 1, 2, 3, 4$. All components operate independently.

- **Step 1: Evaluate Subsystem A (Components 1 and 2 in parallel):**  
  Subsystem A works if at least one of 1 or 2 works:
  $$P(A) = 1 - P(C_1^c \\cap C_2^c) = 1 - (1 - p)^2 = 1 - (0.10)^2 = 1 - 0.01 = 0.99$$
  $$P(A^c) = 0.01$$

- **Step 2: Evaluate Subsystem B (Components 3 and 4 in series):**  
  Subsystem B works if both 3 and 4 work:
  $$P(B) = P(C_3 \\cap C_4) = P(C_3) \\cdot P(C_4) = (0.90)^2 = 0.81$$
  $$P(B^c) = 1 - 0.81 = 0.19$$

- **Step 3: Evaluate Overall System (Subsystem A and Subsystem B in parallel):**  
  The overall system transmits if **either** Subsystem A works **or** Subsystem B works (parallel top-level architecture).  
  The system fails if and only if **both** Subsystem A fails and Subsystem B fails:
  $$P(\\text{System Fails}) = P(A^c \\cap B^c) = P(A^c) \\cdot P(B^c) = 0.01 \\times 0.19 = 0.0019$$
  $$P(\\text{System Works}) = 1 - P(\\text{System Fails}) = 1 - 0.0019 = 0.9981$$

*Direct Union Verification:*  
$$P(A \\cup B) = P(A) + P(B) - P(A \\cap B) = 0.99 + 0.81 - (0.99 \\times 0.81) = 1.80 - 0.8019 = 0.9981$$

**Answer.**  
$P(\\text{System Works}) = 0.9981$ (99.81%).

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

- **(a) Probability a red ball is selected from Box 1 and a red ball is selected from Box 2 ($P(R_1 \\cap R_2)$):**  
  Applying the multiplication rule:
  $$P(R_1 \\cap R_2) = P(R_2 \\mid R_1) \\cdot P(R_1)$$
  From Box 1: $P(R_1) = \\frac{6}{10}$.
  If a red ball is placed into Box 2, Box 2 now contains $7 + 1 = 8$ red balls and 3 green balls (total 11).
  $$P(R_2 \\mid R_1) = \\frac{8}{11}$$
  $$P(R_1 \\cap R_2) = \\frac{6}{10} \\times \\frac{8}{11} = \\frac{48}{110} = \\frac{24}{55} \\approx 0.436364$$

- **(b) Probability Box 1 ends with its original composition:**  
  Box 1 initially has 6 red and 4 green balls. Its composition remains identical at the end if and only if the ball transferred from Box 2 back to Box 1 has the **exact same colour** as the ball originally transferred from Box 1 to Box 2. This can occur via two mutually exclusive cases:
  1. *Case 1 (Red transferred 1 to 2, Red returned 2 to 1):* $R_1 \\cap R_2$.
     From part (a): $P(R_1 \\cap R_2) = \\frac{48}{110}$.
  2. *Case 2 (Green transferred 1 to 2, Green returned 2 to 1):* $G_1 \\cap G_2$.
     From Box 1: $P(G_1) = \\frac{4}{10}$.
     If a green ball is transferred, Box 2 now contains 7 red balls and $3 + 1 = 4$ green balls (total 11).
     $$P(G_2 \\mid G_1) = \\frac{4}{11}$$
     $$P(G_1 \\cap G_2) = \\frac{4}{10} \\times \\frac{4}{11} = \\frac{16}{110}$$

  Summing the two disjoint cases:
  $$P(\\text{Identical Composition}) = P(R_1 \\cap R_2) + P(G_1 \\cap G_2) = \\frac{48}{110} + \\frac{16}{110} = \\frac{64}{110} = \\frac{32}{55} \\approx 0.581818$$

**Answer.**  
- (a) $P(R_1 \\cap R_2) = \\frac{24}{55} \\approx 0.4364$ (43.64%).
- (b) $P(\\text{Identical}) = \\frac{32}{55} \\approx 0.5818$ (58.18%).

---

##### Exercise MMSA 2.67 (p. 84)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.4, p. 84, Exercise 67.  
**Classification:** MMSA — Test.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction), [PT-02](#problem-type-pt-02-multi-stage-sequential-intersection-via-the-general-multiplication--chain-rule).

**Complete question statement.**  
Verify the multiplication rule for conditional probabilities:
$$P(A \\cap B \\mid C) = P(A \\mid B \\cap C) \\cdot P(B \\mid C)$$

**Complete working.**  
Assume $P(B \\cap C) > 0$, which also implies $P(C) \\ge P(B \\cap C) > 0$.
- **Left-Hand Side (LHS):**  
  By the definition of conditional probability:
  $$P(A \\cap B \\mid C) = \\frac{P((A \\cap B) \\cap C)}{P(C)} = \\frac{P(A \\cap B \\cap C)}{P(C)}$$

- **Right-Hand Side (RHS):**  
  Express each factor on the right-hand side using the definition of conditional probability:
  $$P(A \\mid B \\cap C) = \\frac{P(A \\cap (B \\cap C))}{P(B \\cap C)} = \\frac{P(A \\cap B \\cap C)}{P(B \\cap C)}$$
  $$P(B \\mid C) = \\frac{P(B \\cap C)}{P(C)}$$
  Multiplying the two terms:
  $$P(A \\mid B \\cap C) \\cdot P(B \\mid C) = \\frac{P(A \\cap B \\cap C)}{P(B \\cap C)} \\times \\frac{P(B \\cap C)}{P(C)}$$
  The non-zero scalar term $P(B \\cap C)$ cancels algebraically from the numerator and denominator:
  $$= \\frac{P(A \\cap B \\cap C)}{P(C)}$$
  This is identical to the LHS.
  If $P(B \\cap C) = 0$, both sides are defined to be 0. Thus, the identity holds universally. $\\blacksquare$

**Answer.**  
Proof established algebraically by expanding definitions: $\\frac{P(A \\cap B \\cap C)}{P(B \\cap C)} \\times \\frac{P(B \\cap C)}{P(C)} = \\frac{P(A \\cap B \\cap C)}{P(C)} = P(A \\cap B \\mid C)$.

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
For airline $i$, let $p_i = P(D \\mid A_i)$ and $q_i = P(L \\mid A_i)$:
- Airline 1: $p_1 = 0.30, q_1 = 0.10$
- Airline 2: $p_2 = 0.25, q_2 = 0.20$
- Airline 3: $p_3 = 0.40, q_3 = 0.25$

Let $E$ be the event of arriving late at **exactly one** destination:
$$E = (D \\cap L^c) \\cup (D^c \\cap L)$$
By conditional independence for each airline:
$$P(E \\mid A_i) = p_i(1 - q_i) + (1 - p_i)q_i$$

- **Compute conditional likelihoods $P(E \\mid A_i)$:**  
  - For $A_1$: $P(E \\mid A_1) = (0.30)(0.90) + (0.70)(0.10) = 0.27 + 0.07 = 0.34$.
  - For $A_2$: $P(E \\mid A_2) = (0.25)(0.80) + (0.75)(0.20) = 0.20 + 0.15 = 0.35$.
  - For $A_3$: $P(E \\mid A_3) = (0.40)(0.75) + (0.60)(0.25) = 0.30 + 0.15 = 0.45$.

- **Compute joint probabilities $P(A_i \\cap E) = P(E \\mid A_i)P(A_i)$:**  
  - $P(A_1 \\cap E) = 0.34 \\times 0.50 = 0.170$.
  - $P(A_2 \\cap E) = 0.35 \\times 0.30 = 0.105$.
  - $P(A_3 \\cap E) = 0.45 \\times 0.20 = 0.090$.

- **Compute total evidence probability $P(E)$ via LTP:**  
  $$P(E) = 0.170 + 0.105 + 0.090 = 0.365$$

- **Compute posterior probabilities via Bayes' Rule:**  
  - **Airline 1:**
    $$P(A_1 \\mid E) = \\frac{P(A_1 \\cap E)}{P(E)} = \\frac{0.170}{0.365} = \\frac{170}{365} = \\frac{34}{73} \\approx 0.465753$$
  - **Airline 2:**
    $$P(A_2 \\mid E) = \\frac{P(A_2 \\cap E)}{P(E)} = \\frac{0.105}{0.365} = \\frac{105}{365} = \\frac{21}{73} \\approx 0.287671$$
  - **Airline 3:**
    $$P(A_3 \\mid E) = \\frac{P(A_3 \\cap E)}{P(E)} = \\frac{0.090}{0.365} = \\frac{90}{365} = \\frac{18}{73} \\approx 0.246575$$
  Sum check: $\\frac{34 + 21 + 18}{73} = \\frac{73}{73} = 1.00$.

**Answer.**  
- $P(A_1 \\mid E) = \\frac{34}{73} \\approx 0.4658$ (46.58%).
- $P(A_2 \\mid E) = \\frac{21}{73} \\approx 0.2877$ (28.77%).
- $P(A_3 \\mid E) = \\frac{18}{73} \\approx 0.2466$ (24.66%).

---

##### Exercise MMSA 2.77 (p. 92)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.5, p. 92, Exercise 77.  
**Classification:** MMSA — Test.  
**Relevant PT ID(s):** [PT-03](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics).

**Complete question statement.**  
If $A$ and $B$ are independent events, show that $A'$ ($A^c$) and $B$ are also independent. [Hint: First establish a relationship among $P(A' \\cap B), P(B),$ and $P(A \\cap B)$.]

**Complete working.**  
Let events $A$ and $B$ be independent, meaning $P(A \\cap B) = P(A) \\cdot P(B)$.
- **Step 1: Partition event $B$:**  
  Event $B$ can be decomposed into two mutually exclusive subsets depending on whether $A$ occurs:
  $$B = (A \\cap B) \\cup (A^c \\cap B)$$
  Because $A$ and $A^c$ are disjoint, $(A \\cap B) \\cap (A^c \\cap B) = \\emptyset$.

- **Step 2: Apply additivity axiom:**  
  By Axiom 3 (finite additivity):
  $$P(B) = P(A \\cap B) + P(A^c \\cap B)$$
  Subtracting $P(A \\cap B)$ from both sides gives the difference identity:
  $$P(A^c \\cap B) = P(B) - P(A \\cap B)$$

- **Step 3: Substitute the independence condition:**  
  Since $A$ and $B$ are independent, substitute $P(A \\cap B) = P(A)P(B)$:
  $$P(A^c \\cap B) = P(B) - P(A)P(B)$$
  Factor out $P(B)$:
  $$P(A^c \\cap B) = P(B)[1 - P(A)]$$
  By the complement rule, $1 - P(A) = P(A^c)$:
  $$P(A^c \\cap B) = P(B) \\cdot P(A^c) = P(A^c) \\cdot P(B)$$

Because the joint probability of $A^c$ and $B$ factors into the product of their individual probabilities, $A^c$ and $B$ are statistically independent. $\\blacksquare$

**Answer.**  
Proof established: $P(A^c \\cap B) = P(B) - P(A)P(B) = P(B)(1 - P(A)) = P(A^c)P(B)$.

---

##### Exercise MMSA 2.88 (p. 92)
**Source:** Devore, Berk, & Carlton (3rd ed.), Chapter 2.5, p. 92, Exercise 88.  
**Classification:** MMSA — Test.  
**Relevant PT ID(s):** [PT-02](#problem-type-pt-02-multi-stage-sequential-intersection-via-the-general-multiplication--chain-rule), [PT-03](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics).

**Complete question statement.**  
- (a) A lumber company has just taken delivery on a lot of 10,000 $2 \\times 4$ boards. Suppose that 20% of these boards (2000) are actually too green to be used in first-quality construction. Two boards are selected at random, one after the other. Let $A = \\{\\text{the first board is green}\\}$ and $B = \\{\\text{the second board is green}\\}$. Compute $P(A)$, $P(B)$, and $P(A \\cap B)$ (a tree diagram might help). Are $A$ and $B$ independent?
- (b) With $A$ and $B$ independent and $P(A) = P(B) = 0.2$, what is $P(A \\cap B)$? How much difference is there between this answer and $P(A \\cap B)$ in part (a)? For purposes of calculating $P(A \\cap B)$, can we assume that $A$ and $B$ of part (a) are independent to obtain essentially the correct probability?
- (c) Suppose the lot consists of ten boards, of which two are green. Does the assumption of independence now yield approximately the correct answer for $P(A \\cap B)$? What is the critical difference between the situation here and that of part (a)? When do you think that an independence assumption would be valid in obtaining an approximately correct answer to $P(A \\cap B)$?

**Complete working.**  
**(a) Lot of $N = 10,000$ boards with $2,000$ green ($G$) and $8,000$ non-green ($G^c$):**  
- First draw: $P(A) = \\frac{2000}{10000} = 0.20$.
- Second draw probability $P(B)$ via Law of Total Probability:
  $$P(B) = P(B \\mid A)P(A) + P(B \\mid A^c)P(A^c)$$
  $$P(B \\mid A) = \\frac{1999}{9999}, \\quad P(B \\mid A^c) = \\frac{2000}{9999}$$
  $$P(B) = \\left(\\frac{1999}{9999}\\right)(0.20) + \\left(\\frac{2000}{9999}\\right)(0.80) = \\frac{399.8 + 1600}{9999} = \\frac{1999.8}{9999} = \\frac{2000}{10000} = 0.20$$
- Joint probability:
  $$P(A \\cap B) = P(B \\mid A) \\cdot P(A) = \\frac{1999}{9999} \\times 0.20 = \\frac{399.8}{9999} \\approx 0.039983998$$
- Independence check:
  $$P(A) \\cdot P(B) = 0.20 \\times 0.20 = 0.040000$$
  Since $P(A \\cap B) \\approx 0.039984 \\neq 0.040000$, strictly speaking $A$ and $B$ are **dependent (not independent)**.

**(b) Independence approximation:**  
Under assumed independence: $P(A \\cap B) = 0.040000$.
Difference:
$$0.040000 - 0.039984 = 0.000016 \\quad (0.0016\\%)$$
This discrepancy is infinitesimal (a relative error of $0.04\\%$). For all practical engineering and statistical calculations, we **can safely assume independence** when sampling 2 boards from a lot of 10,000.

**(c) Lot of $N = 10$ boards with $2$ green:**  
- True joint probability without replacement:
  $$P(A \\cap B) = P(B \\mid A)P(A) = \\frac{1}{9} \\times \\frac{2}{10} = \\frac{2}{90} = \\frac{1}{45} \\approx 0.022222$$
- Under assumed independence:
  $$P(A)P(B) = \\frac{2}{10} \\times \\frac{2}{10} = 0.040000$$
- Comparison:
  The independence assumption yields $0.0400$, which is **$80\\%$ higher** than the true value $0.0222$! The assumption does **not** yield approximately the correct answer.
- **Critical Difference & Rule of Thumb:**  
  The critical difference is the **sampling fraction** $n / N$:
  - In part (a), $n/N = 2 / 10,000 = 0.0002$ ($0.02\\%$), so removing one board barely alters the remaining population composition ($1999/9999 \\approx 0.19992 \\approx 0.20$).
  - In part (c), $n/N = 2 / 10 = 0.20$ ($20\\%$), so removing one green board cuts the concentration of green boards nearly in half ($1/9 \\approx 0.111$ vs. $0.20$).
  **Statistical Rule of Thumb:** An independence assumption for sampling without replacement is practically valid whenever the sample size $n$ represents **less than 5% of the population** ($n/N \\le 0.05$).

**Answer.**  
- (a) $P(A) = 0.20, P(B) = 0.20, P(A \\cap B) = \\frac{1999}{49995} \\approx 0.03998$; Not independent.
- (b) With independence, $P(A \\cap B) = 0.0400$; difference is $0.000016$; assumption is practically valid.
- (c) For $N=10$, true $= 0.0222$ vs. independent $= 0.0400$ (invalid); valid only when $n/N \\le 0.05$.

---
"""

with open(OUTPUT_PATH, "a", encoding="utf-8") as f:
    f.write(section_c1)
print("Section C.1 appended.")
