# Script to generate and append Sections D, E, and F to Answers-and-Practice.md
import os

target_path = "/Users/stevenli/Documents/University of toronto/STA237/W3/Study-Notes-Markdown/Answers-and-Practice.md"

sec_d_e_f = r'''
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
'''

with open(target_path, "a", encoding="utf-8") as f:
    f.write(sec_d_e_f)

print("Sections D, E, F appended successfully.")
