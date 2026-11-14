# STA237 Quiz 1 Review: Practice Problems & Solutions (September 28)

## Exam Scope and Instructions

This review package covers the official examinable scope for **Quiz 1**: **Week 1 and Week 2** (Foundations of Probability, Set Theory, Kolmogorov Axioms, and Counting Principles).

- **Format & Rules**: Closed book, no aid sheet permitted, non-programmable calculators allowed. Total: 15 marks.
- **Standards**: Numerical answers should be rounded to four decimal places unless an exact fraction is more informative. Show all intermediate steps and necessary justifications.
- **Structure**: The 14 problems below represent core problem types and conceptual checkpoints from lectures, tutorials, and assigned textbook exercises. **They do not constitute a direct forecast of exam questions or length.**
- **Navigation**: Problems are presented first for timed self-testing; complete worked solutions and pedagogical notes follow in the second half.

---

## Part I: Review Problems

### 1. Student Election: Sample Spaces and Compound Events

Yolanda and Zach are running for president of the student association. Exactly 1,000 students vote, and each student casts a ballot for one of the two candidates (no abstentions or spoiled ballots). 

(a) Specify the sample space $S$ using the vote counts received by the candidates.  
(b) Specify the event $Y$ that Yolanda beats Zach by at least 100 votes.

*Source:* [Week 1 Lecture Slides, pp. 24–25](W1/Week1-L0401-annotated.pdf) (PAR Example 1.3).


### 2. Rolling a Pair of Dice: Event Enumeration and Outcome Order

A fair six-sided die is rolled twice, and the outcomes are recorded as an ordered pair $(\text{first roll}, \text{second roll})$.

(a) Enumerate the elements of event $D$: doubles are rolled.  
(b) Enumerate the elements of event $E$: the sum of the two faces equals 8.  
(c) Write out the union $D \cup E$.  
(d) Explain physically and mathematically why $(2, 6)$ and $(6, 2)$ are distinct outcomes, and why $(4, 4)$ appears only once in $D \cup E$.

*Source:* [Week 1 Lecture Slides, p. 29](W1/Week1-L0401-annotated.pdf).


### 3. Mutually Exclusive vs. Independent Events: Conceptual Classification

A single card is drawn at random from a standard, well-shuffled 52-card deck. Let $A$ be the event that the card is black, and let $B$ be the event that the card is the Ace of Spades.

(a) Are $A$ and $B$ mutually exclusive (disjoint)? Justify using set definitions.  
(b) Are $A$ and $B$ independent? Justify using probability and conditional probability definitions.

*Source:* [Week 1 Lecture Slides, p. 34](W1/Week1-L0401-annotated.pdf).


### 4. Venn Diagrams and Regional Student Decompositions

In a survey of 60 students, 28 can roll their tongue, 15 have attached earlobes, and 8 have both traits. Let $T$ denote the event that a randomly chosen student can roll their tongue, and $E$ denote the event that they have attached earlobes.

(a) Find the number of students who can roll their tongue but do not have attached earlobes.  
(b) Find the number of students who have attached earlobes but cannot roll their tongue.  
(c) Express the event that a student has neither trait in set notation, and determine how many students belong to this event.

*Source:* [Week 1 Lecture Slides, p. 41](W1/Week1-L0401-annotated.pdf).


### 5. Kolmogorov Axioms and Fundamental Probability Proofs

(a) State the three Kolmogorov Axioms of Probability for an arbitrary sample space $\Omega$ and event space $\mathcal{F}$.  
(b) Using only the axioms, prove that $P(\emptyset) = 0$ and $P(A^c) = 1 - P(A)$.  
(c) Using only the axioms and disjoint event decompositions, prove the two-event Addition Rule:
$$
P(A \cup B) = P(A) + P(B) - P(A \cap B).
$$

*Source:* [Week 1 Lecture Slides, pp. 37–40](W1/Week1-L0401-annotated.pdf).


### 6. Multiple Project Bids: Inclusion-Exclusion Principle

A consulting engineering firm has submitted competitive bids for three independent projects. Let $A_i$ denote the event that the firm is awarded project $i$ for $i \in \{1, 2, 3\}$. Suppose:
$$
P(A_1) = 0.22, \quad P(A_2) = 0.25, \quad P(A_3) = 0.28,
$$
$$
P(A_1 \cap A_2) = 0.11, \quad P(A_1 \cap A_3) = 0.05, \quad P(A_2 \cap A_3) = 0.07,
$$
$$
P(A_1 \cap A_2 \cap A_3) = 0.01.
$$

(a) Express the event that the firm is awarded **at least two projects** in set notation.  
(b) Calculate the probability that the firm is awarded at least two projects.  
(c) Explain why the triple intersection $A_1 \cap A_2 \cap A_3$ must be adjusted when evaluating this probability.  
(d) Calculate the probability that the firm is awarded **at least one project**.

*Source:* [Week 2 Lecture Slides, p. 6](W2/Week2-L0401-annotated(1).pdf) (MMSA Ch. 2, Ex. 15).


### 7. Weak Law of Large Numbers and Long-Run Relative Frequency

(a) State the Weak Law of Large Numbers (WLLN) in words and explain its significance for probability modeling.  
(b) If the occurrence of an event $A$ in trial $i$ is coded as an indicator $X_i = 1$ and non-occurrence as $X_i = 0$, what does the sample mean $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ represent? What does it converge to as $n \to \infty$?  
(c) In Rock-Paper-Scissors, an automated opponent plays Rock, Paper, or Scissors independently with equal probability $1/3$ on each round. The human player chooses their move before the opponent's move is revealed. What is the human player's long-run win rate? Explain what the WLLN guarantees (and does not guarantee) about this game.

*Source:* [Week 2 Lecture Slides, pp. 8–11](W2/Week2-L0401-annotated(1).pdf).


### 8. Bank PIN Codes: Fundamental Principle of Counting

A financial institution requires customers to set a 4-, 5-, or 6-digit numeric Personal Identification Number (PIN) chosen from the digits $\{0, 1, 2, \dots, 9\}$. Leading zeros are permitted.

(a) If digits may be repeated without restriction, how many distinct PINs can be formed?  
(b) If each digit may appear at most once (sampling without replacement), how many distinct PINs can be formed?  
(c) Assuming all allowable PINs across the three lengths are equally likely, what is the probability that a randomly chosen PIN has no repeated digits?

*Source:* [Week 2 Lecture Slides, p. 15](W2/Week2-L0401-annotated(1).pdf).


### 9. Lotto 6/49: Permutations vs. Combinations

In the Lotto 6/49 game, 6 winning numbers are drawn without replacement from the set $\{1, 2, \dots, 49\}$.

(a) If a ticket must match all 6 numbers in the exact sequence in which they were drawn, what is the probability of winning with a single ticket?  
(b) If the order in which the numbers are drawn does not matter, what is the probability of winning the jackpot with a single ticket?  
(c) Explain combinatorially why the unordered combinations formula divides the number of ordered permutations by $6!$.

*Source:* [Week 2 Lecture Slides, p. 22; pp. 28–30](W2/Week2-L0401-annotated(1).pdf).


### 10. The Birthday Problem: Complementary Probability

In a tutorial room with $k = 10$ randomly chosen students, assume each student's birthday is independently and uniformly distributed across 365 days of the year (ignoring leap years).

What is the probability that at least two students share the same birthday?

*Source:* [Week 2 Lecture Slides, p. 23](W2/Week2-L0401-annotated(1).pdf).


### 11. Permutations of Indistinguishable Digits under Positional Constraints

Using all seven digits from the multiset $\{1, 2, 3, 3, 4, 4, 4\}$, how many distinct 7-digit natural numbers can be formed:

(a) With no restrictions?  
(b) That are strictly less than $4,000,000$?  
(c) That are strictly less than $4,000,000$ and are even numbers?

*Source:* [Week 2 Lecture Slides, pp. 24–26](W2/Week2-L0401-annotated(1).pdf).


### 12. Inviting Friends: Hypergeometric Sampling

You have 12 close friends: 5 from university and 7 from high school. You decide to invite 5 friends at random to lunch.

(a) How many distinct groups of 5 friends can be invited?  
(b) What is the probability that all 5 invited friends are from high school?

*Source:* [Week 2 Lecture Slides, pp. 30–31](W2/Week2-L0401-annotated(1).pdf).


### 13. Five-Card Poker: Face Cards and Numeric Cards

A standard 52-card deck consists of 12 face cards (J, Q, K), 36 numeric cards (2 through 10), and 4 Aces. A 5-card poker hand is dealt at random without replacement.

What is the probability that the hand contains exactly 4 face cards and 1 numeric card?

*Source:* [Week 2 Lecture Slides, p. 32](W2/Week2-L0401-annotated(1).pdf).


### 14. Poker Hands: Symmetry, Rank Roles, and Common Miscounts

(a) A Two Pair hand consists of two cards of one rank, two cards of a second rank, and one kicker card of a third rank. Write down the counting formula and calculate the total number of Two Pair hands. Explain why selecting the two pair ranks requires $\binom{13}{2}$ rather than $13 \times 12$.  
(b) A student attempts to count the total number of Full House hands as:
$$
\binom{13}{2}\binom{4}{3}\binom{4}{2} = 1,872.
$$
Explain why this formula is incorrect, identify the source of the error, and state the correct total.  
(c) Another student attempts to count Full Houses via sequential card choices:
$$
52 \times 3 \times 2 \times 48 \times 3 = 44,928.
$$
Explain why this leads to an overcount, identify the exact overcount factor, and show how to correct it.

*Source:* [Week 2 Lecture Slides, pp. 33–34](W2/Week2-L0401-annotated(1).pdf).

---

## Part II: Complete Solutions and Step-by-Step Work

### 1. Student Election

**(a) Sample Space $S$:**  
Let $i$ denote the number of votes cast for Yolanda. Because all 1,000 votes are divided between Yolanda and Zach, Zach must receive $1,000 - i$ votes. The integer $i$ ranges from 0 to 1,000.
$$
S = \{(i, 1000 - i) \mid i \in \{0, 1, 2, \dots, 1000\}\}.
$$
The total number of outcomes is $|S| = 1,001$.

**(b) Event $Y$ (Yolanda leads by $\ge 100$):**  
Yolanda's margin of victory is:
$$
i - (1000 - i) = 2i - 1000 \ge 100 \implies 2i \ge 1100 \implies i \ge 550.
$$
Thus, the event is:
$$
Y = \{(i, 1000 - i) \mid i \in \{550, 551, \dots, 1000\}\}.
$$
The event contains $1000 - 550 + 1 = 451$ outcomes.


### 2. Rolling a Pair of Dice

**(a) Doubles ($D$):**
$$
D = \{(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)\}, \quad |D| = 6.
$$

**(b) Sum to 8 ($E$):**
$$
E = \{(2,6), (3,5), (4,4), (5,3), (6,2)\}, \quad |E| = 5.
$$

**(c) Union ($D \cup E$):**
$$
D \cup E = \{(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (2,6), (3,5), (5,3), (6,2)\}, \quad |D \cup E| = 10.
$$

**(d) Order and Duplication:**
- **Outcome Order**: The recording distinguishes the sequence of throws $(\text{Die}_1, \text{Die}_2)$. Getting 2 on the first roll and 6 on the second is physically distinguishable from getting 6 on the first roll and 2 on the second. Treating them as distinct ensures that all 36 outcomes in $\Omega$ have equal probability $1/36$.
- **No Duplication in Sets**: By mathematical set definition, sets contain distinct elements without order or duplication. The outcome $(4,4)$ satisfies both conditions ($(4,4) \in D \cap E$), but appears only once in $D \cup E$. By the Addition Rule:
$$
|D \cup E| = |D| + |E| - |D \cap E| = 6 + 5 - 1 = 10.
$$


### 3. Mutually Exclusive vs. Independent Events

**(a) Mutual Exclusivity:**  
Two events are mutually exclusive if and only if $A \cap B = \emptyset$.  
Here, $A = \{\text{Black card}\}$ (26 cards: Spades and Clubs) and $B = \{\text{Ace of Spades}\}$.  
Because the Ace of Spades is a spade, it is black, so $B \subset A$. Thus:
$$
A \cap B = B = \{\text{Ace of Spades}\} \neq \emptyset.
$$
Therefore, $A$ and $B$ are **not mutually exclusive**.

**(b) Independence:**  
Two events are independent if and only if $P(A \cap B) = P(A)P(B)$, or equivalently $P(B \mid A) = P(B)$.
- $P(B) = \frac{1}{52} \approx 0.0192$.
- $P(A) = \frac{26}{52} = \frac{1}{2}$.
- $P(A \cap B) = P(B) = \frac{1}{52}$.
- $P(A)P(B) = \frac{1}{2} \times \frac{1}{52} = \frac{1}{104} \neq \frac{1}{52}$.
Alternatively, conditioning on knowing the card is black:
$$
P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{1/52}{26/52} = \frac{1}{26} \neq \frac{1}{52} = P(B).
$$
Because learning that $A$ occurred doubles the probability of $B$, the events are **dependent** (not independent).


### 4. Venn Diagrams and Regional Student Decompositions

Given: $n(\Omega) = 60$, $n(T) = 28$, $n(E) = 15$, and $n(T \cap E) = 8$.

**(a) Tongue rolling only ($T \cap E^c$):**
$$
n(T \cap E^c) = n(T) - n(T \cap E) = 28 - 8 = 20.
$$

**(b) Attached earlobes only ($E \cap T^c$):**
$$
n(E \cap T^c) = n(E) - n(T \cap E) = 15 - 8 = 7.
$$

**(c) Neither trait ($(T \cup E)^c = T^c \cap E^c$):**  
First, find the total number of students who possess at least one of the two traits:
$$
n(T \cup E) = n(T) + n(E) - n(T \cap E) = 28 + 15 - 8 = 35.
$$
The number possessing neither trait is:
$$
n((T \cup E)^c) = n(\Omega) - n(T \cup E) = 60 - 35 = 25.
$$
*(Corresponding probability: $P(\text{neither}) = \frac{25}{60} = \frac{5}{12} \approx 0.4167$.)*


### 5. Kolmogorov Axioms and Fundamental Probability Proofs

**(a) The Three Kolmogorov Axioms:**
1. **Non-negativity**: For every event $A \in \mathcal{F}$, $P(A) \ge 0$.
2. **Total Probability (Normalization)**: $P(\Omega) = 1$.
3. **Countable Additivity**: If $\{A_1, A_2, \dots\}$ is a countable collection of pairwise disjoint events (i.e., $A_i \cap A_j = \emptyset$ for all $i \neq j$), then:
$$
P\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty P(A_i).
$$
*(For finite collections, $P(A \cup B) = P(A) + P(B)$ whenever $A \cap B = \emptyset$.)*

**(b) Proof that $P(\emptyset) = 0$ and $P(A^c) = 1 - P(A)$:**
- For $P(\emptyset)$: Note that $\Omega \cap \emptyset = \emptyset$ and $\Omega \cup \emptyset = \Omega$. By Axiom 3 (finite additivity):
$$
P(\Omega) = P(\Omega \cup \emptyset) = P(\Omega) + P(\emptyset).
$$
Subtracting $P(\Omega)$ (which equals 1 by Axiom 2) from both sides gives $P(\emptyset) = 0$.
- For $P(A^c)$: By definition of complement, $A \cap A^c = \emptyset$ and $A \cup A^c = \Omega$. By Axiom 3 and Axiom 2:
$$
1 = P(\Omega) = P(A \cup A^c) = P(A) + P(A^c).
$$
Rearranging yields $P(A^c) = 1 - P(A)$. $\blacksquare$

**(c) Proof of the Two-Event Addition Rule:**  
Decompose the union $A \cup B$ into two mutually exclusive events:
$$
A \cup B = A \cup (B \cap A^c), \quad \text{where } A \cap (B \cap A^c) = \emptyset.
$$
By Axiom 3:
$$
P(A \cup B) = P(A) + P(B \cap A^c). \tag{1}
$$
Next, decompose event $B$ into its intersections with $A$ and $A^c$:
$$
B = (A \cap B) \cup (A^c \cap B), \quad \text{where } (A \cap B) \cap (A^c \cap B) = \emptyset.
$$
By Axiom 3:
$$
P(B) = P(A \cap B) + P(A^c \cap B) \implies P(B \cap A^c) = P(B) - P(A \cap B). \tag{2}
$$
Substituting (2) into (1):
$$
P(A \cup B) = P(A) + P(B) - P(A \cap B). \quad \blacksquare
$$


### 6. Multiple Project Bids: Inclusion-Exclusion Principle

**(a) Event Expression:**  
The event of winning at least two projects is:
$$
E_{\ge 2} = (A_1 \cap A_2) \cup (A_1 \cap A_3) \cup (A_2 \cap A_3).
$$

**(b) Probability of At Least Two Projects:**  
Let $E_1 = A_1 \cap A_2$, $E_2 = A_1 \cap A_3$, and $E_3 = A_2 \cap A_3$. Note that the intersection of any two of these events (as well as all three) is the common triple intersection $A_1 \cap A_2 \cap A_3$:
$$
E_1 \cap E_2 = (A_1 \cap A_2) \cap (A_1 \cap A_3) = A_1 \cap A_2 \cap A_3.
$$
Applying the 3-event Inclusion-Exclusion formula:
$$
P(E_{\ge 2}) = \sum P(E_i) - \sum_{i < j} P(E_i \cap E_j) + P(E_1 \cap E_2 \cap E_3)
$$
$$
= (0.11 + 0.05 + 0.07) - (0.01 + 0.01 + 0.01) + 0.01 = 0.23 - 0.03 + 0.01 = 0.2100.
$$
**Answer:** $0.2100$.

**(c) Triple Intersection Adjustment:**  
The triple intersection represents winning all three projects, which is a sub-case of winning at least two. In the sum of pairwise intersections $P(A_1 \cap A_2) + P(A_1 \cap A_3) + P(A_2 \cap A_3)$, the outcome $A_1 \cap A_2 \cap A_3$ is counted three times. To include it exactly once in the union, it must be subtracted twice ($-3(0.01) + 0.01 = -2(0.01)$).

**(d) At Least One Project:**  
Using the standard 3-event Principle of Inclusion-Exclusion:
$$
P(A_1 \cup A_2 \cup A_3) = \sum P(A_i) - \sum_{i < j} P(A_i \cap A_j) + P(A_1 \cap A_2 \cap A_3)
$$
$$
= (0.22 + 0.25 + 0.28) - (0.11 + 0.05 + 0.07) + 0.01 = 0.75 - 0.23 + 0.01 = 0.5300.
$$
**Answer:** $0.5300$.


### 7. Weak Law of Large Numbers and Long-Run Relative Frequency

**(a) Statement and Meaning:**  
The Weak Law of Large Numbers states that as the number of independent, identically distributed (i.i.d.) trials $n$ grows arbitrarily large, the sample mean $\bar{X}_n$ converges in probability to the theoretical expected value $\mu = E(X)$. That is, for any $\varepsilon > 0$:
$$
\lim_{n \to \infty} P(|\bar{X}_n - \mu| \ge \varepsilon) = 0.
$$
This provides the theoretical bridge connecting classical abstract probability measures to empirical, observable long-run frequencies.

**(b) Indicator Coding and Empirical Frequency:**  
Let $X_i = 1$ if $A$ occurs, and $X_i = 0$ if $A^c$ occurs. Then $E(X_i) = 1 \cdot P(A) + 0 \cdot P(A^c) = P(A)$.  
The sample mean is:
$$
\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i = \frac{\text{Number of occurrences of } A}{n} = \text{Empirical relative frequency of } A.
$$
By WLLN, $\bar{X}_n$ converges in probability to $P(A)$.

**(c) Rock-Paper-Scissors Analysis:**  
Because the opponent chooses independently and uniformly at random from $\{\text{Rock}, \text{Paper}, \text{Scissors}\}$, any choice made by the player has exactly 1 winning response, 1 tying response, and 1 losing response among the 3 equally likely options.  
Therefore, for every round, $P(\text{Win}) = 1/3 \approx 0.3333$.  
By the WLLN, over a very large number of games $n$, the empirical proportion of wins will become arbitrarily close to $1/3 = 0.3333$.  
*Crucial distinction:* The WLLN does not imply that the player will win exactly 1 out of every 3 rounds (there is no "law of averages" or self-correcting streak compensation in short samples); it only guarantees long-run frequency convergence.


### 8. Bank PIN Codes: Fundamental Principle of Counting

PINs can have length 4, 5, or 6. These form three mutually disjoint cases.

**(a) Repetition Allowed:**  
Each position has 10 independent choices $\{0, 1, \dots, 9\}$:
- 4-digit PINs: $10^4 = 10,000$
- 5-digit PINs: $10^5 = 100,000$
- 6-digit PINs: $10^6 = 1,000,000$
$$
N_{\text{total}} = 10,000 + 100,000 + 1,000,000 = 1,110,000.
$$

**(b) No Repetition (Permutations without Replacement):**  
Choosing $k$ distinct digits in order from 10:
- 4-digit PINs: $P(10, 4) = 10 \times 9 \times 8 \times 7 = 5,040$
- 5-digit PINs: $P(10, 5) = 10 \times 9 \times 8 \times 7 \times 6 = 30,240$
- 6-digit PINs: $P(10, 6) = 10 \times 9 \times 8 \times 7 \times 6 \times 5 = 151,200$
$$
N_{\text{no rep}} = 5,040 + 30,240 + 151,200 = 186,480.
$$

**(c) Probability of No Repeated Digits:**  
Assuming all $1,110,000$ PINs are equally likely:
$$
P(\text{no repetition}) = \frac{186,480}{1,110,000} = \frac{777}{4,625} \approx 0.1680 \quad (16.80\%).
$$


### 9. Lotto 6/49: Permutations vs. Combinations

**(a) Matching All 6 Numbers in Exact Order:**  
Total ordered permutations of 6 distinct numbers from 49:
$$
P(49, 6) = \frac{49!}{(49-6)!} = 49 \times 48 \times 47 \times 46 \times 45 \times 44 = 10,068,347,520.
$$
Since only 1 ordered sequence matches the winning draw:
$$
P(\text{ordered win}) = \frac{1}{10,068,347,520} \approx 9.9321 \times 10^{-11} \approx 0.0000.
$$

**(b) Matching in Any Order (Unordered Subsets):**  
Total unordered combinations of 6 from 49:
$$
\binom{49}{6} = \frac{49!}{6! \, 43!} = \frac{10,068,347,520}{720} = 13,983,816.
$$
$$
P(\text{jackpot}) = \frac{1}{13,983,816} \approx 7.1511 \times 10^{-8} \approx 0.0000.
$$
*(While reported as 0.0000 to four decimal places, the exact fraction is $1/13,983,816$.)*

**(c) Why Divide by $6!$:**  
Any specific subset of 6 numbers can be arranged in $6! = 720$ distinct orderings. The permutation count $P(49, 6)$ counts every unique 6-number set 720 times (once for each order). To treat order as irrelevant, we partition the permutations into equivalence classes of size $6!$, yielding $\binom{49}{6} = P(49, 6) / 6!$.


### 10. The Birthday Problem: Complementary Probability

Total number of possible birthday assignments for $k = 10$ people:
$$
n(\Omega) = 365^{10} \approx 4.1958 \times 10^{25}.
$$
Let $A$ be the event that at least two people share a birthday. Its complement $A^c$ is the event that all 10 birthdays are distinct:
$$
n(A^c) = P(365, 10) = 365 \times 364 \times 363 \times \dots \times 356 \approx 3.7052 \times 10^{25}.
$$
The probability that all birthdays are distinct is:
$$
P(A^c) = \frac{P(365, 10)}{365^{10}} = \prod_{i=0}^9 \left(\frac{365 - i}{365}\right) \approx 0.8831.
$$
By the Complement Rule:
$$
P(A) = 1 - P(A^c) = 1 - 0.8831 = 0.1169 \quad (11.69\%).
$$


### 11. Permutations of Indistinguishable Digits under Positional Constraints

Multiset: $\{1, 2, 3, 3, 4, 4, 4\}$. Frequencies: $n_1 = 1$, $n_2 = 1$, $n_3 = 2$, $n_4 = 3$; total $n = 7$.

**(a) No Restrictions:**  
By the Multinomial Permutations Formula:
$$
N_a = \frac{7!}{1! \, 1! \, 2! \, 3!} = \frac{5,040}{1 \times 1 \times 2 \times 6} = \frac{5,040}{12} = 420.
$$

**(b) Strictly Less Than $4,000,000$:**  
A 7-digit number is less than 4,000,000 if and only if its leading digit is 1, 2, or 3.
- **Leading 1**: remaining multiset $\{2, 3, 3, 4, 4, 4\} \implies \frac{6!}{1! \, 2! \, 3!} = \frac{720}{12} = 60$.
- **Leading 2**: remaining multiset $\{1, 3, 3, 4, 4, 4\} \implies \frac{6!}{1! \, 2! \, 3!} = \frac{720}{12} = 60$.
- **Leading 3**: remaining multiset $\{1, 2, 3, 4, 4, 4\} \implies \frac{6!}{1! \, 1! \, 1! \, 3!} = \frac{720}{6} = 120$.
$$
N_b = 60 + 60 + 120 = 240.
$$

**(c) Strictly Less Than $4,000,000$ and Even:**  
Leading digit $\in \{1, 2, 3\}$ and last digit $\in \{2, 4\}$.
- **Last digit is 2**:
  - *First digit = 1*: remaining $\{3, 3, 4, 4, 4\} \implies \frac{5!}{2! \, 3!} = \frac{120}{12} = 10$.
  - *First digit = 2*: impossible (only one '2' in multiset).
  - *First digit = 3*: remaining $\{1, 3, 4, 4, 4\} \implies \frac{5!}{1! \, 1! \, 3!} = \frac{120}{6} = 20$.
  - Subtotal for last digit 2: $10 + 20 = 30$.
- **Last digit is 4**: (two '4's remaining)
  - *First digit = 1*: remaining $\{2, 3, 3, 4, 4\} \implies \frac{5!}{1! \, 2! \, 2!} = \frac{120}{4} = 30$.
  - *First digit = 2*: remaining $\{1, 3, 3, 4, 4\} \implies \frac{5!}{1! \, 2! \, 2!} = \frac{120}{4} = 30$.
  - *First digit = 3*: remaining $\{1, 2, 3, 4, 4\} \implies \frac{5!}{1! \, 1! \, 1! \, 2!} = \frac{120}{2} = 60$.
  - Subtotal for last digit 4: $30 + 30 + 60 = 120$.
$$
N_c = 30 + 120 = 150.
$$


### 12. Inviting Friends: Hypergeometric Sampling

**(a) Total Possible Groups:**  
Choosing 5 friends from 12 without replacement where order does not matter:
$$
\binom{12}{5} = \frac{12 \times 11 \times 10 \times 9 \times 8}{5 \times 4 \times 3 \times 2 \times 1} = 792.
$$

**(b) Probability All 5 are High School Friends:**  
Number of ways to choose 5 from the 7 high school friends (and 0 from the 5 university friends):
$$
\binom{7}{5}\binom{5}{0} = \binom{7}{2} \times 1 = \frac{7 \times 6}{2} = 21.
$$
$$
P(\text{all high school}) = \frac{\binom{7}{5}}{\binom{12}{5}} = \frac{21}{792} = \frac{7}{264} \approx 0.0265 \quad (2.65\%).
$$


### 13. Five-Card Poker: Face Cards and Numeric Cards

Total possible 5-card hands from a standard 52-card deck:
$$
|\Omega| = \binom{52}{5} = 2,598,960.
$$
We seek the number of hands with exactly 4 face cards (out of 12) and 1 numeric card (out of 36):
- Ways to choose 4 face cards: $\binom{12}{4} = \frac{12 \times 11 \times 10 \times 9}{4 \times 3 \times 2 \times 1} = 495$.
- Ways to choose 1 numeric card: $\binom{36}{1} = 36$.
$$
n(\text{favorable}) = \binom{12}{4}\binom{36}{1} = 495 \times 36 = 17,820.
$$
$$
P = \frac{17,820}{2,598,960} = \frac{297}{43,316} \approx 0.0069 \quad (0.69\%).
$$


### 14. Poker Hands: Symmetry, Rank Roles, and Common Miscounts

**(a) Two Pair Derivation and Rank Selection Symmetry:**  
To build a Two Pair hand:
1. Select the 2 ranks for the pairs from the 13 available ranks: $\binom{13}{2} = 78$.
2. Select 2 suits from 4 for the lower pair: $\binom{4}{2} = 6$.
3. Select 2 suits from 4 for the higher pair: $\binom{4}{2} = 6$.
4. Select 1 rank for the kicker from the remaining 11 ranks: $\binom{11}{1} = 11$.
5. Select 1 suit for the kicker: $\binom{4}{1} = 4$.
$$
N_{\text{Two Pair}} = \binom{13}{2} \binom{4}{2}^2 \binom{11}{1} \binom{4}{1} = 78 \times 36 \times 11 \times 4 = 123,552.
$$
*Why $\binom{13}{2}$ and not $13 \times 12$*:  
The two pairs have symmetric group size (2 cards each). A hand with a pair of Kings and a pair of Queens is identical to a hand with a pair of Queens and a pair of Kings. Using $13 \times 12$ imposes an artificial ordering (e.g., "first pair" and "second pair"), counting every pair combination twice. We must use an unordered combination $\binom{13}{2}$.

**(b) Full House Error Analysis: Asymmetric Roles:**  
The formula $\binom{13}{2}\binom{4}{3}\binom{4}{2} = 1,872$ is **incorrect**.  
*Source of Error*: The two ranks in a Full House play **asymmetric roles**: one rank provides 3 cards (the triple) and the other provides 2 cards (the pair). Selecting an unordered pair of ranks $\{R_1, R_2\}$ via $\binom{13}{2}$ fails to assign which rank is the triple and which is the pair. For instance, $\{K, Q\}$ can produce either $K K K Q Q$ or $Q Q Q K K$.  
*Correction*: Select the ranks as an ordered sequence ($13$ choices for the triple rank, then $12$ choices for the pair rank):
$$
N_{\text{Full House}} = 13 \times 12 \times \binom{4}{3}\binom{4}{2} = 156 \times 4 \times 6 = 3,744.
$$
The student's formula undercounted by a factor of 2.

**(c) Sequential Card Selection Error: Internal Permutation Overcounting:**  
The calculation $52 \times 3 \times 2 \times 48 \times 3 = 44,928$ is **incorrect**.  
*Source of Error*: This sequential method tracks the order in which the cards are dealt:
- The 3 cards of the triple are dealt in one of $3! = 6$ possible sequences.
- The 2 cards of the pair are dealt in one of $2! = 2$ possible sequences.  
Because a poker hand is an unordered set, every unique Full House hand is counted $3! \times 2! = 6 \times 2 = 12$ times.  
*Correction*: Divide by the overcount factor $3! \times 2! = 12$:
$$
\frac{52 \times 3 \times 2 \times 48 \times 3}{3! \times 2!} = \frac{44,928}{12} = 3,744.
$$
