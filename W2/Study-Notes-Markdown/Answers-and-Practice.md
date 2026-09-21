# STA237 Week 2: Answers, Worked Solutions, and Practice Exercises

---

### Table of Contents
- [Section A: Problem Type Teaching-Example Solutions](#section-a-problem-type-teaching-example-solutions)
  - [Problem Type PT-01: Multi-Stage Sequential Selection via FPC](#problem-type-pt-01-multi-stage-sequential-selection-via-fpc)
  - [Problem Type PT-02: Ordered Permutations of Distinct Objects under Positional Constraints](#problem-type-pt-02-ordered-permutations-of-distinct-objects-under-positional-constraints)
  - [Problem Type PT-03: Permutations with Indistinguishable Objects and Digit Formation](#problem-type-pt-03-permutations-with-indistinguishable-objects-and-digit-formation)
  - [Problem Type PT-04: Unordered Combinations and Combinatorial Identity Proofs](#problem-type-pt-04-unordered-combinations-and-combinatorial-identity-proofs)
  - [Problem Type PT-05: Multi-Category Hypergeometric Sampling](#problem-type-pt-05-multi-category-hypergeometric-sampling)
  - [Problem Type PT-06: Symmetry, Subgroup Partitioning, and Card Hand Derivations](#problem-type-pt-06-symmetry-subgroup-partitioning-and-card-hand-derivations)
  - [Problem Type PT-07: Complementary Counting and Collision Problems (Birthday Paradox)](#problem-type-pt-07-complementary-counting-and-collision-problems-birthday-paradox)
  - [Problem Type PT-08: Generalized Principle of Inclusion-Exclusion ($n \ge 3$ Events)](#problem-type-pt-08-generalized-principle-of-inclusion-exclusion-n-ge-3-events)
  - [Problem Type PT-09: Empirical Relative Frequency and Monte Carlo Estimation in R](#problem-type-pt-09-empirical-relative-frequency-and-monte-carlo-estimation-in-r)
- [Section B: Actual Weekly Questions and Solutions](#section-b-actual-weekly-questions-and-solutions)
  - [Lecture Example 1: Inclusion-Exclusion on Project Bids (MMSA Ch. 2 Ex. 15)](#lecture-example-1-inclusion-exclusion-on-project-bids-mmsa-ch-2-ex-15)
  - [Lecture Example 2: Bank PIN Code Configurations](#lecture-example-2-bank-pin-code-configurations)
  - [Lecture Try For Yourself 1, Part 1: Rolling Six Fair Dice](#lecture-try-for-yourself-1-part-1-rolling-six-fair-dice)
  - [Lecture Try For Yourself 1, Part 2: Distinct Divisors of 24,500](#lecture-try-for-yourself-1-part-2-distinct-divisors-of-24500)
  - [Lecture Example 3: Lotto 6/49 Permutations vs. Combinations](#lecture-example-3-lotto-649-permutations-vs-combinations)
  - [Lecture Example 4: The Birthday Problem ($k = 10$)](#lecture-example-4-the-birthday-problem-k-10)
  - [Lecture Example 5: Arrangements of Colored Balls (Indistinguishable Objects)](#lecture-example-5-arrangements-of-colored-balls-indistinguishable-objects)
  - [Lecture Try For Yourself 2: Permutations of Digits $\{1, 2, 3, 3, 4, 4, 4\}$](#lecture-try-for-yourself-2-permutations-of-digits-1-2-3-3-4-4-4)
  - [Lecture Example 6: Lunch with Friends (University vs. High School)](#lecture-example-6-lunch-with-friends-university-vs-high-school)
  - [Lecture Example 7: Poker Hand Subsets — Face Cards and Two Pair](#lecture-example-7-poker-hand-subsets-face-cards-and-two-pair)
  - [Lecture Case Study: A Tale of Common Miscounts — Full House Analysis](#lecture-case-study-a-tale-of-common-miscounts-full-house-analysis)
- [Section C: Textbook Exercises and Solutions](#section-c-textbook-exercises-and-solutions)
  - [MMSA — Basic Practice](#mmsa-basic-practice)
    - [MMSA Section 2.3, Exercise 31 (p. 72)](#mmsa-section-23-exercise-31-p-72)
    - [MMSA Section 2.3, Exercise 33 (p. 72)](#mmsa-section-23-exercise-33-p-72)
    - [MMSA Section 2.3, Exercise 34 (pp. 72–73)](#mmsa-section-23-exercise-34-pp-7273)
  - [MMSA — Medium Practice](#mmsa-medium-practice)
    - [MMSA Section 2.3, Exercise 35 (p. 73)](#mmsa-section-23-exercise-35-p-73)
    - [MMSA Section 2.3, Exercise 37 (p. 73)](#mmsa-section-23-exercise-37-p-73)
    - [MMSA Section 2.3, Exercise 39 (p. 73)](#mmsa-section-23-exercise-39-p-73)
    - [MMSA Section 2.3, Exercise 40 (pp. 73–74)](#mmsa-section-23-exercise-40-pp-7374)
    - [MMSA Section 2.3, Exercise 44 (p. 74)](#mmsa-section-23-exercise-44-p-74)
  - [MMSA — Test Level](#mmsa-test-level)
    - [MMSA Section 2.3, Exercise 38 (p. 73)](#mmsa-section-23-exercise-38-p-73)
    - [MMSA Section 2.3, Exercise 43 (p. 74)](#mmsa-section-23-exercise-43-p-74)
    - [MMSA Section 2.3, Exercise 45 (p. 74)](#mmsa-section-23-exercise-45-p-74)
    - [MMSA Section 2.3, Exercise 47 (p. 75)](#mmsa-section-23-exercise-47-p-75)
  - [PAR — Basic Practice](#par-basic-practice)
    - [PAR Chapter 1, Exercise 16 (p. 38)](#par-chapter-1-exercise-16-p-38)
    - [PAR Chapter 1, Exercise 17 (p. 38)](#par-chapter-1-exercise-17-p-38)
    - [PAR Chapter 1, Exercise 21 (p. 38)](#par-chapter-1-exercise-21-p-38)
  - [PAR — Medium Practice](#par-medium-practice)
    - [PAR Chapter 1, Exercise 19 (p. 38)](#par-chapter-1-exercise-19-p-38)
    - [PAR Chapter 1, Exercise 20 (p. 38)](#par-chapter-1-exercise-20-p-38)
    - [PAR Chapter 1, Exercise 41 (p. 42)](#par-chapter-1-exercise-41-p-42)
    - [PAR Chapter 1, Exercise 49 (p. 43)](#par-chapter-1-exercise-49-p-43)
  - [PAR — Test Level](#par-test-level)
    - [PAR Chapter 1, Exercise 18 (p. 38) — Multi-Length License Plates](#par-chapter-1-exercise-18-p-38-multi-length-license-plates)
    - [PAR Chapter 1, Exercise 22 (p. 39) — Shoe Pair Selection](#par-chapter-1-exercise-22-p-39-shoe-pair-selection)
    - [PAR Chapter 1, Exercise 23 (p. 39) — Bridge Hand Distributional Symmetries](#par-chapter-1-exercise-23-p-39-bridge-hand-distributional-symmetries)
    - [PAR Chapter 1, Exercise 24 (p. 39) — Bridge Hands with a Nine-Card Suit](#par-chapter-1-exercise-24-p-39-bridge-hands-with-a-nine-card-suit)
    - [PAR Chapter 1, Exercise 25 (p. 39) — Non-Attacking Rooks / Independent Placements on a Chessboard](#par-chapter-1-exercise-25-p-39-non-attacking-rooks-independent-placements-on-a-chessboard)
    - [PAR Chapter 1, Exercise 26 (pp. 39–40) — Exhaustive Hierarchy of 5-Card Poker Hands](#par-chapter-1-exercise-26-pp-3940-exhaustive-hierarchy-of-5-card-poker-hands)
    - [PAR Chapter 1, Exercise 29 (p. 40) — Combinatorial Proof of Subset Symmetry](#par-chapter-1-exercise-29-p-40-combinatorial-proof-of-subset-symmetry)
- [Section D: Original Self-Test Questions](#section-d-original-self-test-questions)
- [Section E: Self-Test Answers](#section-e-self-test-answers)
- [Section F: Compact Coverage and Unresolved-Items Appendix](#section-f-compact-coverage-and-unresolved-items-appendix)

---

## Section A: Problem Type Teaching-Example Solutions

---

### Problem Type PT-01: Multi-Stage Sequential Selection via FPC

**Question reference:** [Study-Notes.md: Problem Type PT-01](Study-Notes.md#problem-type-pt-01-multi-stage-sequential-selection-via-fpc)

**Worked solution.**
- **Part (a):** We are forming a 6-character token $(c_1, c_2, c_3, c_4, c_5, c_6)$ from an alphabet of 26 letters and 10 digits (total 36 symbols).
  - Slot 1 ($c_1$): Must be a letter $\implies 26$ choices.
  - Slot 6 ($c_6$): Must be an even digit from $\{0, 2, 4, 6, 8\} \implies 5$ choices.
  - Slots 2, 3, 4, 5 ($c_2, c_3, c_4, c_5$): Unrestricted alphanumeric symbols with repetition allowed $\implies 36$ choices each.
  By the Fundamental Principle of Counting (FPC):
  $$N_a = 26 \times 36 \times 36 \times 36 \times 36 \times 5 = 26 \times 5 \times 36^4 = 130 \times 1,679,616 = 218,350,080$$

- **Part (b):** The token structure is fixed as (Letter, Digit, Letter, Digit, Letter, Digit) with **no repetition**:
  - Slot 1 (Vowel): 5 choices ($\text{A, E, I, O, U}$).
  - Slot 2 (Digit): 10 choices ($0\text{--}9$).
  - Slot 3 (Letter): Any letter remaining in the 26-letter alphabet except the vowel chosen in Slot 1 $\implies 26 - 1 = 25$ choices.
  - Slot 4 (Digit): Any digit remaining except the one chosen in Slot 2 $\implies 10 - 1 = 9$ choices.
  - Slot 5 (Letter): Any letter remaining except the two already used $\implies 26 - 2 = 24$ choices.
  - Slot 6 (Digit): Any digit remaining except the two already used $\implies 10 - 2 = 8$ choices.
  Applying FPC:
  $$N_b = 5 \times 10 \times 25 \times 9 \times 24 \times 8 = (5 \times 25 \times 24) \times (10 \times 9 \times 8) = 3,000 \times 720 = 2,160,000$$

- **Part (c):**
  - The sample space $\Omega$ consists of all 6-character strings formed from the 36 alphanumeric characters with repetition allowed:
    $$|\Omega| = 36^6 = 2,176,782,336$$
  - The favorable event $E$ is that the token consists of 6 **distinct digits**. This corresponds to an ordered selection of 6 digits from the 10 available digits without replacement:
    $$|E| = P(10, 6) = \frac{10!}{(10-6)!} = 10 \times 9 \times 8 \times 7 \times 6 \times 5 = 151,200$$
  - Since all strings in $\Omega$ are equally likely:
    $$P(E) = \frac{|E|}{|\Omega|} = \frac{151,200}{2,176,782,336} = \frac{175}{2,519,424} \approx 6.9460 \times 10^{-5}$$

**Answer.**
- (a) $218,350,080$ valid tokens.
- (b) $2,160,000$ valid tokens.
- (c) Exact: $\frac{175}{2,519,424} \approx 6.9460 \times 10^{-5}$ ($0.00695\%$).

---

### Problem Type PT-02: Ordered Permutations of Distinct Objects under Positional Constraints

**Question reference:** [Study-Notes.md: Problem Type PT-02](Study-Notes.md#problem-type-pt-02-ordered-permutations-of-distinct-objects-under-positional-constraints)

**Worked solution.**
- Total unrestricted arrangements of the 7 distinct students is $|\Omega| = 7! = 5,040$.
- **Part (a): All 3 graduate students must sit together in a block.**
  - Regard the 3 graduate students $\{G_1, G_2, G_3\}$ as a single super-object $[G]$.
  - We now arrange 5 entities: $[G], U_1, U_2, U_3, U_4$.
  - These 5 entities can be arranged in $5!$ ways.
  - Inside the block, the 3 graduate students can be permuted in $3!$ ways.
  - Total arrangements $= 5! \times 3! = 120 \times 6 = 720$.

- **Part (b): No two graduate students may sit adjacent to each other.**
  - Use the gap/insertion method.
  - First, arrange the 4 undergraduates in the row: $4! = 24$ ways.
  - This creates $4 + 1 = 5$ possible insertion slots (one before each undergraduate, between them, and after the last):
    $$\_ \ U_1 \ \_ \ U_2 \ \_ \ U_3 \ \_ \ U_4 \ \_$$
  - To ensure no two graduate students are adjacent, we must place at most one graduate student into each slot.
  - We select and arrange 3 distinct graduate students into these 5 available slots:
    $$P(5, 3) = 5 \times 4 \times 3 = 60$$
  - Total arrangements $= 4! \times P(5, 3) = 24 \times 60 = 1,440$.

- **Part (c): Probability $G_1$ is seated at an end and $G_2, G_3$ sit adjacent to each other:**
  - Total unrestricted sample space: $|\Omega| = 7! = 5,040$.
  - Let $E$ be the event of interest.
  - **Step 1:** Graduate student $G_1$ must sit at one of the ends of the row: Seat 1 or Seat 7 (2 choices).
  - **Step 2:** The remaining 6 seats must be occupied by $\{G_2, G_3, U_1, U_2, U_3, U_4\}$ such that $G_2$ and $G_3$ sit adjacent to each other.
  - Treat $\{G_2, G_3\}$ as a single composite block $[G_{23}]$.
  - We arrange 5 distinct units: the block $[G_{23}]$ and the 4 undergraduates $U_1, U_2, U_3, U_4$.
  - These 5 units can be arranged in the 5 available unit positions in $5! = 120$ ways.
  - Within the block, $G_2$ and $G_3$ can be permuted in $2! = 2$ ways ($G_2 G_3$ or $G_3 G_2$).
  - Number of favorable arrangements for the remaining 6 seats $= 5! \times 2! = 120 \times 2 = 240$ ways.
  - **Total favorable arrangements:**
    $$|E| = 2 \times 240 = 480$$
  - **Probability:**
    $$P(E) = \frac{|E|}{|\Omega|} = \frac{480}{5,040} = \frac{2}{21} \approx 0.095238 \quad (9.52\%)$$

**Answer.**
- (a) $720$ seating arrangements.
- (b) $1,440$ seating arrangements.
- (c) $P = \frac{2}{21} \approx 0.0952$ ($9.52\%$).

---

### Problem Type PT-03: Permutations with Indistinguishable Objects and Digit Formation

**Question reference:** [Study-Notes.md: Problem Type PT-03](Study-Notes.md#problem-type-pt-03-permutations-with-indistinguishable-objects-and-digit-formation)

**Worked solution.**
- Digits available: three 2s, two 4s, one 5, one 7, one 9. Total $n = 3 + 2 + 1 + 1 + 1 = 8$.
- **Part (a): Unconstrained 8-digit integers:**
  Using the multinomial permutation formula:
  $$N_{\text{total}} = \frac{8!}{3! \, 2! \, 1! \, 1! \, 1!} = \frac{40,320}{6 \times 2} = \frac{40,320}{12} = 3,360$$

- **Part (b): Strictly greater than $40,000,000$:**
  - An 8-digit number formed from these digits is $> 40,000,000$ if and only if its leading digit is in $\{4, 5, 7, 9\}$ (since no digit is 0, any leading 4 produces a number $\ge 42,224,579 > 40,000,000$).
  - **Case 1: Leading digit is 4.**
    Remaining multiset has seven digits: three 2s, one 4, one 5, one 7, one 9.
    $$N_4 = \frac{7!}{3! \, 1! \, 1! \, 1! \, 1!} = \frac{5,040}{6} = 840$$
  - **Case 2: Leading digit is 5.**
    Remaining multiset: three 2s, two 4s, one 7, one 9.
    $$N_5 = \frac{7!}{3! \, 2! \, 1! \, 1!} = \frac{5,040}{6 \times 2} = 420$$
  - **Case 3: Leading digit is 7.**
    Remaining multiset: three 2s, two 4s, one 5, one 9.
    $$N_7 = \frac{7!}{3! \, 2! \, 1! \, 1!} = 420$$
  - **Case 4: Leading digit is 9.**
    Remaining multiset: three 2s, two 4s, one 5, one 7.
    $$N_9 = \frac{7!}{3! \, 2! \, 1! \, 1!} = 420$$
  - By the Addition Principle:
    $$N(> 40,000,000) = 840 + 420 + 420 + 420 = 2,100$$
  *(Alternative check via complement: Numbers starting with 2 have remaining digits $\{2, 2, 4, 4, 5, 7, 9\}$, which gives $\frac{7!}{2! 2! 1! 1! 1!} = \frac{5040}{4} = 1260$. Then $3360 - 1260 = 2100$. Verified!)*

- **Part (c): Strictly greater than $40,000,000$ AND divisible by 2 (even):**
  - To be even, the last digit must be 2 or 4.
  - To be $> 40,000,000$, the first digit must be in $\{4, 5, 7, 9\}$.
  - We partition by the joint pair $(\text{first digit}, \text{last digit})$:
    - **Subcase (First = 4, Last = 2):** Remaining 6 digits are two 2s, one 4, one 5, one 7, one 9.
      $$N_{4, 2} = \frac{6!}{2! \, 1! \, 1! \, 1! \, 1!} = \frac{720}{2} = 360$$
    - **Subcase (First = 4, Last = 4):** Both 4s are used. Remaining 6 digits are three 2s, one 5, one 7, one 9.
      $$N_{4, 4} = \frac{6!}{3! \, 1! \, 1! \, 1!} = \frac{720}{6} = 120$$
    - **Subcase (First $\in \{5, 7, 9\}$, Last = 2):** There are 3 choices for the first digit. For each, the remaining 6 digits have two 2s, two 4s, and two others:
      $$N_{\text{odd}, 2} = 3 \times \frac{6!}{2! \, 2! \, 1! \, 1!} = 3 \times \frac{720}{4} = 3 \times 180 = 540$$
    - **Subcase (First $\in \{5, 7, 9\}$, Last = 4):** There are 3 choices for the first digit. For each, the remaining 6 digits have three 2s, one 4, and two others:
      $$N_{\text{odd}, 4} = 3 \times \frac{6!}{3! \, 1! \, 1! \, 1!} = 3 \times \frac{720}{6} = 3 \times 120 = 360$$
  - Summing all mutually exclusive subcases:
    $$N = 360 + 120 + 540 + 360 = 1,380$$

**Answer.**
- (a) $3,360$ distinct 8-digit integers.
- (b) $2,100$ integers.
- (c) $1,380$ integers.

---

### Problem Type PT-04: Unordered Combinations and Combinatorial Identity Proofs

**Question reference:** [Study-Notes.md: Problem Type PT-04](Study-Notes.md#problem-type-pt-04-unordered-combinations-and-combinatorial-identity-proofs)

**Worked solution.**
- **Part (a):** Number of ways to choose a 4-member committee from 12 developers:
  $$\binom{12}{4} = \frac{12 \times 11 \times 10 \times 9}{4 \times 3 \times 2 \times 1} = \frac{11,880}{24} = 495$$

- **Part (b): Algebraic Proof:**
  Using the definition of the binomial coefficient $\binom{n}{r} = \frac{n!}{r!(n-r)!}$:
  $$\text{LHS} = k \binom{n}{k} = k \cdot \frac{n!}{k!(n-k)!} = k \cdot \frac{n!}{k \cdot (k-1)! (n-k)!} = \frac{n!}{(k-1)!(n-k)!}$$
  Now evaluate the RHS:
  $$\text{RHS} = n \binom{n-1}{k-1} = n \cdot \frac{(n-1)!}{(k-1)!((n-1)-(k-1))!} = \frac{n \cdot (n-1)!}{(k-1)!(n-k)!} = \frac{n!}{(k-1)!(n-k)!}$$
  Since $\text{LHS} = \text{RHS} = \frac{n!}{(k-1)!(n-k)!}$, the identity is established algebraically. $\blacksquare$

- **Part (c): Combinatorial Proof:**
  - **Question:** Consider a pool of $n$ people. In how many ways can we choose a committee of $k$ people and designate one member of this committee as the committee chair?
  - **Perspective 1 (Form Committee First, then Elect Chair):**
    1. First, select the $k$-person committee from the $n$ candidates: $\binom{n}{k}$ ways.
    2. Second, from the $k$ chosen members, select one person to serve as chair: $\binom{k}{1} = k$ ways.
    By FPC, the total number of ways is $k \binom{n}{k}$.
  - **Perspective 2 (Elect Chair First, then Fill Remaining Committee Seats):**
    1. First, select the chair directly from the entire pool of $n$ candidates: $\binom{n}{1} = n$ ways.
    2. Second, to complete the $k$-person committee, select the remaining $k-1$ members from the remaining $n-1$ candidates: $\binom{n-1}{k-1}$ ways.
    By FPC, the total number of ways is $n \binom{n-1}{k-1}$.
  - **Conclusion:** Both procedures count the exact same set of structured committees (a $k$-element subset with one distinguished element). Therefore, the two expressions must be equal:
    $$k \binom{n}{k} = n \binom{n-1}{k-1} \quad \blacksquare$$

**Answer.**
- (a) $\binom{12}{4} = 495$ committees.
- (b) Algebraic proof complete ($\text{LHS} = \text{RHS} = \frac{n!}{(k-1)!(n-k)!}$).
- (c) Combinatorial proof complete via double counting of a chaired committee.

---

### Problem Type PT-05: Multi-Category Hypergeometric Sampling

**Question reference:** [Study-Notes.md: Problem Type PT-05](Study-Notes.md#problem-type-pt-05-multi-category-hypergeometric-sampling)

**Worked solution.**
- Population: $N = 30$ microchips ($M_1 = 15$ Class-A, $M_2 = 10$ Class-B, $M_3 = 5$ Class-C).
- Sample size: $n = 6$ drawn without replacement.
- **Part (a): Total distinct 6-chip samples:**
  $$|\Omega| = \binom{30}{6} = \frac{30 \times 29 \times 28 \times 27 \times 26 \times 25}{6 \times 5 \times 4 \times 3 \times 2 \times 1} = 593,775$$

- **Part (b): Exactly 3 Class-A, 2 Class-B, and 1 Class-C:**
  Using the multivariate hypergeometric formula:
  $$|A| = \binom{15}{3} \binom{10}{2} \binom{5}{1} = 455 \times 45 \times 5 = 102,375$$
  $$P(A) = \frac{102,375}{593,775} = \frac{455}{2,639} \approx 0.17241379 \quad (17.24\%)$$

- **Part (c): No Class-C chips:**
  All 6 chips must come from the $15 + 10 = 25$ non-C chips (Class-A or Class-B):
  $$|C^c| = \binom{25}{6} = 177,100$$
  $$P(C^c) = \frac{177,100}{593,775} = \frac{1,012}{3,393} \approx 0.2982611 \quad (29.83\%)$$

- **Part (d): At least two of the three chip classes are represented:**
  - The complement of "at least two classes represented" is "exactly ONE class represented" (all 6 chips are of the same class).
  - We can have all 6 Class-A, or all 6 Class-B. (Class-C has only 5 chips, so it is impossible to have 6 Class-C chips).
  - Favorable to complement:
    $$N(\text{1 class}) = \binom{15}{6} + \binom{10}{6} + \binom{5}{6} = 5,005 + 210 + 0 = 5,215$$
  - Probability of complement:
    $$P(\text{1 class}) = \frac{5,215}{593,775} = \frac{149}{16,965} \approx 0.00878278$$
  - Probability of at least two classes:
    $$P(\ge 2 \text{ classes}) = 1 - P(\text{1 class}) = 1 - \frac{5,215}{593,775} = \frac{588,560}{593,775} = \frac{16,816}{16,965} \approx 0.9912172 \quad (99.12\%)$$

**Answer.**
- (a) $\binom{30}{6} = 593,775$ samples.
- (b) $P = \frac{455}{2,639} \approx 0.1724$.
- (c) $P = \frac{1,012}{3,393} \approx 0.2983$.
- (d) $P = \frac{16,816}{16,965} \approx 0.9912$.

---

### Problem Type PT-06: Symmetry, Subgroup Partitioning, and Card Hand Derivations

**Question reference:** [Study-Notes.md: Problem Type PT-06](Study-Notes.md#problem-type-pt-06-symmetry-subgroup-partitioning-and-card-hand-derivations)

**Worked solution.**
- Sample space size: $|\Omega| = \binom{52}{5} = 2,598,960$.
- **Part (a): Number of "Three of a Kind" hands:**
  A three-of-a-kind hand has the rank profile $(3, 1, 1)$, meaning 3 cards of rank $R_1$, 1 card of rank $R_2$, and 1 card of rank $R_3$, where $R_1, R_2, R_3$ are distinct.
  1. Select the rank of the triple: $\binom{13}{1} = 13$ choices.
  2. Select the 3 suits for the triple: $\binom{4}{3} = 4$ choices.
  3. Select the 2 distinct ranks for the kickers from the remaining 12 ranks: $\binom{12}{2} = 66$ choices.
  4. Select the suit for each kicker: $\binom{4}{1} \times \binom{4}{1} = 4 \times 4 = 16$ choices.
  $$\text{Total Three of a Kind} = 13 \times 4 \times 66 \times 16 = 54,912$$

- **Part (b): Why $\binom{13}{1}\binom{4}{3} \times \binom{49}{2}$ is an overcount:**
  - The expression evaluates to $13 \times 4 \times 1,176 = 61,152$ hands, which exceeds the true count of Three of a Kind ($54,912$) by $6,240$ hands.
  - The remaining 49 cards consist of 1 card of the triple's rank, plus 48 cards belonging to the other 12 ranks (4 cards per rank).
  - When choosing 2 cards from these 49 without restriction ($\binom{49}{2} = 1,176$ pairs), three mutually exclusive outcomes occur:
    1. **Genuine Three of a Kind kickers:** The 2 cards have distinct ranks different from the triple rank: $\binom{12}{2} \times \binom{4}{1} \times \binom{4}{1} = 66 \times 16 = 1,056$ pairs per triple rank. This gives $13 \times 4 \times 1,056 = 54,912$ genuine Three of a Kind hands (each counted exactly once).
    2. **Full House contamination:** The 2 cards share a rank from the other 12 ranks: $\binom{12}{1} \times \binom{4}{2} = 12 \times 6 = 72$ pairs per triple rank. This contributes $13 \times 4 \times 72 = 3,744$ hands (the complete set of Full Houses, which do not qualify as Three of a Kind).
    3. **Four of a Kind contamination and overcounting:** One card is the 4th card of the triple's rank and the other card is any of the remaining 48 cards: $1 \times 48 = 48$ pairs per triple rank. This contributes $13 \times 4 \times 48 = 2,496$ representations. Since there are only $\binom{13}{1}\binom{4}{4}\binom{48}{1} = 624$ distinct Four of a Kind hands, each Four of a Kind hand is counted $\binom{4}{3} = 4$ times (any 3 of the 4 cards could have been chosen as the initial triple).
  - Summing the partitions: $54,912 + 3,744 + 2,496 = 61,152$.
  - Thus, the overcount of $6,240$ hands consists of $3,744$ Full Houses and $2,496$ Four of a Kind representations (counting each Four of a Kind hand 4 times).

- **Part (c): Two Pair vs. Full House Comparison:**
  - **Two Pair:** Rank profile $(2, 2, 1)$. The two pairs have the **same size** (2 cards each). Choosing rank $K$ then rank $7$ gives the identical set of pairs as choosing rank $7$ then rank $K$. Thus, the 2 ranks must be chosen **unordered**:
    $$N(\text{Two Pair}) = \binom{13}{2} \times \binom{4}{2} \times \binom{4}{2} \times \binom{11}{1} \times \binom{4}{1} = 78 \times 6 \times 6 \times 11 \times 4 = 123,552$$
    $$P(\text{Two Pair}) = \frac{123,552}{2,598,960} = \frac{198}{4,165} \approx 0.047539 \quad (4.75\%)$$
  - **Full House:** Rank profile $(3, 2)$. The two groups have **different sizes** (3 cards vs. 2 cards). A hand with three Aces and two Kings is not the same as a hand with three Kings and two Aces. The roles are asymmetric; therefore, we must choose which rank is the triple and which is the pair, requiring an ordered selection ($13 \times 12$):
    $$N(\text{Full House}) = 13 \times 12 \times \binom{4}{3} \times \binom{4}{2} = 156 \times 4 \times 6 = 3,744$$
    $$P(\text{Full House}) = \frac{3,744}{2,598,960} = \frac{6}{4,165} \approx 0.001441 \quad (0.144\%)$$

**Answer.**
- (a) $54,912$ hands.
- (b) See detailed diagnostic above.
- (c) $P(\text{Two Pair}) = \frac{198}{4,165} \approx 0.0475$; $P(\text{Full House}) = \frac{6}{4,165} \approx 0.00144$. Two Pair uses $\binom{13}{2}$ due to symmetry between the two pairs, while Full House uses $13 \times 12$ due to asymmetry between the triple and the pair.

---

### Problem Type PT-07: Complementary Counting and Collision Problems (Birthday Paradox)

**Question reference:** [Study-Notes.md: Problem Type PT-07](Study-Notes.md#problem-type-pt-07-complementary-counting-and-collision-problems-birthday-paradox)

**Worked solution.**
- $N = 128$ server slots, $k = 8$ incoming requests.
- Total possible assignment configurations: $|\Omega| = 128^8$.
- **Part (a): Exact probability of all 8 requests assigned to distinct slots:**
  $$P(A^c) = \frac{P(128, 8)}{128^8} = \frac{128 \times 127 \times 126 \times 125 \times 124 \times 123 \times 122 \times 121}{128^8}$$
  Numerator:
  $$P(128, 8) = 57,645,610,944,768,000$$
  Denominator:
  $$128^8 = 72,057,594,037,927,936$$
  Simplifying the fraction:
  $$P(A^c) = \frac{57,645,610,944,768,000}{72,057,594,037,927,936} = \frac{28,147,270,969,125}{35,184,372,088,832} \approx \mathbf{0.7999936} \quad (79.9994\%)$$
  Alternatively, evaluating via the sequential product:
  $$\prod_{j=0}^7 \left(1 - \frac{j}{128}\right) = 1 \times 0.9921875 \times 0.984375 \times 0.9765625 \times 0.96875 \times 0.9609375 \times 0.953125 \times 0.9453125 \approx \mathbf{0.7999936}$$

- **Part (b): Exact probability of at least one collision:**
  $$P(\text{collision}) = 1 - P(A^c) = 1 - \frac{28,147,270,969,125}{35,184,372,088,832} = \frac{7,037,101,119,707}{35,184,372,088,832} \approx \mathbf{0.2000064} \quad (20.00\%)$$

- **Part (c): Exponential approximation:**
  $$P(\text{collision}) \approx 1 - e^{-\frac{k(k-1)}{2N}} = 1 - e^{-\frac{8 \times 7}{2 \times 128}} = 1 - e^{-\frac{56}{256}} = 1 - e^{-0.21875} \approx 1 - 0.803522 = \mathbf{0.196478} \quad (19.65\%)$$
  Relative difference is:
  $$\frac{|0.2000064 - 0.196478|}{0.2000064} \approx 1.76\%$$
  confirming the fidelity of the exponential approximation.

- **Part (d): Threshold $k^*$ for $P \ge 0.50$:**
  Set $1 - e^{-\frac{k(k-1)}{2N}} \ge 0.50 \iff e^{-\frac{k(k-1)}{256}} \le 0.50 \iff \frac{k(k-1)}{256} \ge \ln(2) \approx 0.693147$.
  $$k(k-1) \ge 256 \times \ln(2) \approx 177.446$$
  Testing integer values:
  - For $k = 13$: $13 \times 12 = 156 < 177.45$. (Exact $P(\text{collision}) = 1 - \frac{P(128, 13)}{128^{13}} \approx 0.4675$).
  - For $k = 14$: $14 \times 13 = 182 > 177.45$. (Exact $P(\text{collision}) = 1 - \frac{P(128, 14)}{128^{14}} \approx 0.5216$).
  Thus, $k^* = 14$ requests.

**Answer.**
- (a) $P(\text{all distinct}) = \frac{28,147,270,969,125}{35,184,372,088,832} \approx 0.8000$.
- (b) $P(\text{at least one collision}) \approx 0.2000$.
- (c) Approximation $\approx 0.1965$ (relative error $\approx 1.76\%$).
- (d) $k^* = 14$ requests.

---

### Problem Type PT-08: Generalized Principle of Inclusion-Exclusion ($n \ge 3$ Events)

**Question reference:** [Study-Notes.md: Problem Type PT-08](Study-Notes.md#problem-type-pt-08-generalized-principle-of-inclusion-exclusion-n-ge-3-events)

**Worked solution.**
- Universe $\mathcal{S} = \{1, 2, \dots, 3000\}$, so $|\mathcal{S}| = 3000$.
- **Part (a): Individual, pairwise, and triple intersection counts:**
  - $|A| = \lfloor 3000 / 6 \rfloor = 500$.
  - $|B| = \lfloor 3000 / 10 \rfloor = 300$.
  - $|C| = \lfloor 3000 / 15 \rfloor = 200$.
  - $\text{lcm}(6, 10) = 30 \implies |A \cap B| = \lfloor 3000 / 30 \rfloor = 100$.
  - $\text{lcm}(6, 15) = 30 \implies |A \cap C| = \lfloor 3000 / 30 \rfloor = 100$.
  - $\text{lcm}(10, 15) = 30 \implies |B \cap C| = \lfloor 3000 / 30 \rfloor = 100$.
  - $\text{lcm}(6, 10, 15) = 30 \implies |A \cap B \cap C| = \lfloor 3000 / 30 \rfloor = 100$.

- **Part (b): Divisible by at least one (Inclusion-Exclusion):**
  $$|A \cup B \cup C| = (|A| + |B| + |C|) - (|A \cap B| + |A \cap C| + |B \cap C|) + |A \cap B \cap C|$$
  $$= (500 + 300 + 200) - (100 + 100 + 100) + 100 = 1000 - 300 + 100 = 800$$
  $$P(A \cup B \cup C) = \frac{800}{3000} = \frac{4}{15} \approx 0.266667 \quad (26.67\%)$$

- **Part (c): Divisible by exactly one:**
  Notice that all three pairwise intersections and the triple intersection are identical ($|A \cap B| = |A \cap C| = |B \cap C| = |A \cap B \cap C| = 100$).
  This means whenever an integer is divisible by two of the numbers, it is automatically divisible by all three! There are no numbers in $(A \cap B \cap C^c)$, $(A \cap C \cap B^c)$, or $(B \cap C \cap A^c)$.
  - Integers in $A$ only $= |A| - |A \cap B \cap C| = 500 - 100 = 400$.
  - Integers in $B$ only $= |B| - |A \cap B \cap C| = 300 - 100 = 200$.
  - Integers in $C$ only $= |C| - |A \cap B \cap C| = 200 - 100 = 100$.
  - Total divisible by exactly one $= 400 + 200 + 100 = 700$.
  $$P(\text{exactly one}) = \frac{700}{3000} = \frac{7}{30} \approx 0.233333 \quad (23.33\%)$$

- **Part (d): Divisible by none:**
  By the Complement Rule:
  $$P(\text{none}) = 1 - P(A \cup B \cup C) = 1 - \frac{4}{15} = \frac{11}{15} \approx 0.733333 \quad (73.33\%)$$

**Answer.**
- (a) $|A|=500, |B|=300, |C|=200$; $|A \cap B|=|A \cap C|=|B \cap C|=|A \cap B \cap C|=100$.
- (b) $P(\text{at least one}) = \frac{4}{15} \approx 0.2667$.
- (c) $P(\text{exactly one}) = \frac{7}{30} \approx 0.2333$.
- (d) $P(\text{none}) = \frac{11}{15} \approx 0.7333$.

---

### Problem Type PT-09: Empirical Relative Frequency and Monte Carlo Estimation in R

**Question reference:** [Study-Notes.md: Problem Type PT-09](Study-Notes.md#problem-type-pt-09-empirical-relative-frequency-and-monte-carlo-estimation-in-r)

**Worked solution.**
- **Part (a): R Simulation Script:**
  ```r
  # Set random seed for reproducibility
  set.seed(237)

  # Simulation parameters
  N <- 50000
  carton <- c(rep("D", 5), rep("N", 20)) # 5 Defective, 20 Non-defective

  # Monte Carlo trial replication
  sim_results <- replicate(N, {
    drawn_sample <- sample(carton, size = 5, replace = FALSE)
    sum(drawn_sample == "D") >= 2
  })

  # Empirical probability estimate
  p_hat <- mean(sim_results)
  cat("Estimated Probability:", p_hat, "\n")
  ```

- **Part (b): Standard Error and 95% Confidence Interval:**
  Given $\hat{p} = 0.2525$ and $N = 50,000$:
  $$\widehat{\text{SE}}(\hat{p}) = \sqrt{\frac{\hat{p}(1 - \hat{p})}{N}} = \sqrt{\frac{0.2525 \times 0.7475}{50,000}} = \sqrt{\frac{0.18874375}{50,000}} \approx 0.0019429$$
  The approximate 95% confidence interval is:
  $$\hat{p} \pm 1.96 \times \widehat{\text{SE}} = 0.2525 \pm 1.96(0.001943) = [0.2487, 0.2563]$$

- **Part (c): Sample Size Determination for Margin of Error $\pm 0.002$:**
  $$N \ge \frac{1.96^2 \times 0.25}{(0.002)^2} = \frac{0.9604}{0.000004} = 240,100 \text{ trials}$$

- **Part (d): Exact Theoretical Probability (Hypergeometric):**
  $$P(X \ge 2) = 1 - P(X = 0) - P(X = 1)$$
  Total ways to choose 5 bulbs from 25: $\binom{25}{5} = 53,130$.
  - $P(X = 0) = \frac{\binom{5}{0}\binom{20}{5}}{\binom{25}{5}} = \frac{1 \times 15,504}{53,130} = \frac{15,504}{53,130} \approx 0.2918125$
  - $P(X = 1) = \frac{\binom{5}{1}\binom{20}{4}}{\binom{25}{5}} = \frac{5 \times 4,845}{53,130} = \frac{24,225}{53,130} \approx 0.4559571$
  - $P(X \le 1) = \frac{15,504 + 24,225}{53,130} = \frac{39,729}{53,130} \approx 0.7477696$
  - $$P(X \ge 2) = 1 - \frac{39,729}{53,130} = \frac{13,401}{53,130} = \frac{4,467}{17,710} \approx \mathbf{0.2522304} \quad (25.22\%)$$
  The simulation estimate of $0.2525$ matches the theoretical $0.2522$ to within $0.0003$.

**Answer.**
- (a) See R code above.
- (b) $\widehat{\text{SE}} \approx 0.00194$; 95% CI is $[0.2487, 0.2563]$.
- (c) $N = 240,100$ trials.
- (d) Exact $P(X \ge 2) = \frac{4,467}{17,710} \approx 0.25223$.

---

## Section B: Actual Weekly Questions and Solutions

---

### Lecture Example 1: Inclusion-Exclusion on Project Bids (MMSA Ch. 2 Ex. 15)

**Source:** `W2/Week2-L0401-annotated(1).pdf`, Slide 6; MMSA Chapter 2, Exercise 15.  
**Relevant method:** [Problem Type PT-08](Study-Notes.md#problem-type-pt-08-generalized-principle-of-inclusion-exclusion-n-ge-3-events)

**Question.**  
A consulting firm presently has bids out on three projects. Let $A_i = \{\text{Awarded project } i\}$ for $i \in \{1, 2, 3\}$, and suppose that:
$$P(A_1) = 0.22, \quad P(A_2) = 0.25, \quad P(A_3) = 0.28$$
$$P(A_1 \cap A_2) = 0.11, \quad P(A_1 \cap A_3) = 0.05, \quad P(A_2 \cap A_3) = 0.07$$
$$P(A_1 \cap A_2 \cap A_3) = 0.01$$
- **Part (a):** Describe what the event $A_1^c \cap A_2^c$ represents and find its probability.
- **Part (b):** Describe what the event $A_1^c \cap A_2^c \cap A_3$ represents and find its probability.
- **Part (c):** Express the event that the firm is awarded **at least two projects** and calculate its probability.

**Necessary work.**  
- **Part (a):** The event $A_1^c \cap A_2^c$ represents the firm NOT being awarded Project 1 AND NOT being awarded Project 2. By De Morgan’s Law, $A_1^c \cap A_2^c = (A_1 \cup A_2)^c$.
  By the Complement Rule:
  $$P(A_1^c \cap A_2^c) = 1 - P(A_1 \cup A_2)$$
  By 2-event addition rule:
  $$P(A_1 \cup A_2) = P(A_1) + P(A_2) - P(A_1 \cap A_2) = 0.22 + 0.25 - 0.11 = 0.36$$
  $$P(A_1^c \cap A_2^c) = 1 - 0.36 = 0.64$$
- **Part (b):** The event $A_1^c \cap A_2^c \cap A_3$ represents the event that the firm is awarded **only Project 3** (and neither Project 1 nor Project 2).
  Decompose $A_3$ into disjoint components:
  $$A_3 = [A_3 \cap (A_1 \cup A_2)] \cup [A_3 \cap (A_1 \cup A_2)^c]$$
  Since these two components are mutually exclusive, by Kolmogorov Axiom 3:
  $$P(A_3) = P(A_3 \cap (A_1 \cup A_2)) + P(A_3 \cap (A_1 \cup A_2)^c)$$
  $$P(A_1^c \cap A_2^c \cap A_3) = P(A_3) - P((A_1 \cap A_3) \cup (A_2 \cap A_3))$$
  Expanding the union via the addition rule:
  $$P((A_1 \cap A_3) \cup (A_2 \cap A_3)) = P(A_1 \cap A_3) + P(A_2 \cap A_3) - P(A_1 \cap A_2 \cap A_3)$$
  $$= 0.05 + 0.07 - 0.01 = 0.11$$
  Therefore:
  $$P(A_1^c \cap A_2^c \cap A_3) = 0.28 - 0.11 = 0.17$$
- **Part (c):** The event that the firm is awarded at least two projects is $(A_1 \cap A_2) \cup (A_1 \cap A_3) \cup (A_2 \cap A_3)$.
  Let $E_1 = A_1 \cap A_2$, $E_2 = A_1 \cap A_3$, $E_3 = A_2 \cap A_3$. Note that the intersection of any two of these events (as well as all three) is the common triple intersection $A_1 \cap A_2 \cap A_3$.
  Applying 3-event Inclusion-Exclusion:
  $$P(\text{at least two}) = P(E_1) + P(E_2) + P(E_3) - [P(E_1 \cap E_2) + P(E_1 \cap E_3) + P(E_2 \cap E_3)] + P(E_1 \cap E_2 \cap E_3)$$
  $$= (0.11 + 0.05 + 0.07) - (0.01 + 0.01 + 0.01) + 0.01 = 0.23 - 0.03 + 0.01 = 0.21$$

**Answer.**  
- (a) $P(A_1^c \cap A_2^c) = 0.64$ (awarded neither Project 1 nor Project 2).
- (b) $P(A_1^c \cap A_2^c \cap A_3) = 0.17$ (awarded only Project 3).
- (c) $P(\text{at least two}) = 0.21$.

---

### Lecture Example 2: Bank PIN Code Configurations

**Source:** `W2/Week2-L0401-annotated(1).pdf`, Slide 15.  
**Relevant method:** [Problem Type PT-01](Study-Notes.md#problem-type-pt-01-multi-stage-sequential-selection-via-fpc), [Problem Type PT-02](Study-Notes.md#problem-type-pt-02-ordered-permutations-of-distinct-objects-under-positional-constraints)

**Question.**  
When opening an account with a bank, you are required to set a 4 to 6 digit numeric personal identification number (PIN) using the digits $\{0, 1, 2, \dots, 9\}$.
- **Part (a):** How many different PIN codes can be generated if all digits are numeric (repetition allowed)?
- **Part (b):** How many PIN codes can be generated if all digits are numeric and each digit is used at most once (no repetition)?
- **Part (c):** What is the probability that a randomly chosen 4-to-6 digit PIN has no repeated digits?

**Necessary work.**  
The possible lengths of PINs are 4, 5, or 6. These form three mutually exclusive categories. By the Addition Principle:
- **Part (a): Repetition allowed:**
  - 4-digit PIN: $10^4 = 10,000$.
  - 5-digit PIN: $10^5 = 100,000$.
  - 6-digit PIN: $10^6 = 1,000,000$.
  Total $= 10,000 + 100,000 + 1,000,000 = 1,110,000$.
- **Part (b): No repetition (Permutations):**
  - 4-digit PIN: $P(10, 4) = 10 \times 9 \times 8 \times 7 = 5,040$.
  - 5-digit PIN: $P(10, 5) = 10 \times 9 \times 8 \times 7 \times 6 = 30,240$.
  - 6-digit PIN: $P(10, 6) = 10 \times 9 \times 8 \times 7 \times 6 \times 5 = 151,200$.
  Total $= 5,040 + 30,240 + 151,200 = 186,480$.
- **Part (c): Probability:**
  Assuming all $1,110,000$ PINs are equally likely:
  $$P(\text{no repeated digits}) = \frac{186,480}{1,110,000} = \frac{1,554}{9,250} = \frac{777}{4,625} \approx 0.1680 \quad (16.80\%)$$

**Answer.**  
- (a) $1,110,000$ PINs.
- (b) $186,480$ PINs.
- (c) $P = \frac{777}{4,625} \approx 0.1680$ ($16.8\%$).

---

### Lecture Try For Yourself 1, Part 1: Rolling Six Fair Dice

**Source:** `W2/Week2-L0401-annotated(1).pdf`, Slide 16.  
**Relevant method:** [Problem Type PT-01](Study-Notes.md#problem-type-pt-01-multi-stage-sequential-selection-via-fpc), [Problem Type PT-02](Study-Notes.md#problem-type-pt-02-ordered-permutations-of-distinct-objects-under-positional-constraints)

**Question.**  
Suppose you roll a fair 6-sided die 6 times. What is the probability that all 6 rolls result in different values? Explain why the order of rolls matters.

**Necessary work.**  
- **Order Considerations:** If we do not distinguish the order of rolls, outcomes are unordered multisets. An outcome with 6 identical faces (e.g., all 1s) occurs in only 1 sequence, whereas an outcome with 6 distinct faces (e.g., $\{1, 2, 3, 4, 5, 6\}$) occurs in $6! = 720$ sequences. Thus, unordered outcomes are **not equally likely**. To use $P(A) = n(A)/n(\Omega)$, we must track order.
- **Sample Space:** $|\Omega| = 6^6 = 46,656$.
- **Favorable Outcomes:** Selecting 6 distinct faces in order without replacement:
  $$n(\text{all different}) = 6! = 720$$
- **Probability:**
  $$P(\text{all different}) = \frac{6!}{6^6} = \frac{720}{46,656} = \frac{5}{324} \approx 0.015432 \quad (1.54\%)$$

**Answer.**  
$P = \frac{5}{324} \approx 0.0154$ ($1.54\%$). Order matters to ensure that all elementary outcomes in the sample space have equal probability ($1/6^6$).

---

### Lecture Try For Yourself 1, Part 2: Distinct Divisors of 24,500

**Source:** `W2/Week2-L0401-annotated(1).pdf`, Slide 16.  
**Relevant method:** [Problem Type PT-01](Study-Notes.md#problem-type-pt-01-multi-stage-sequential-selection-via-fpc)

**Question.**  
How many different positive divisors are there for the number $24,500$?

**Necessary work.**  
1. Find the prime factorization of $24,500$:
   $$24,500 = 245 \times 100 = (5 \times 49) \times (4 \times 25) = (5 \times 7^2) \times (2^2 \times 5^2) = 2^2 \times 5^3 \times 7^2$$
2. Any positive divisor $d$ of $24,500$ must have the form $d = 2^a \times 5^b \times 7^c$, where:
   - $a \in \{0, 1, 2\}$ ($2 + 1 = 3$ choices)
   - $b \in \{0, 1, 2, 3\}$ ($3 + 1 = 4$ choices)
   - $c \in \{0, 1, 2\}$ ($2 + 1 = 3$ choices)
3. By the Fundamental Principle of Counting, the total number of distinct divisors is:
   $$N = 3 \times 4 \times 3 = 36$$

**Answer.**  
$36$ distinct positive divisors.

---

### Lecture Example 3: Lotto 6/49 Permutations vs. Combinations

**Source:** `W2/Week2-L0401-annotated(1).pdf`, Slide 22.  
**Relevant method:** [Problem Type PT-02](Study-Notes.md#problem-type-pt-02-ordered-permutations-of-distinct-objects-under-positional-constraints), [Problem Type PT-04](Study-Notes.md#problem-type-pt-04-unordered-combinations-and-combinatorial-identity-proofs)

**Question.**  
In the Lotto 6/49 game, 6 winning numbers are drawn without replacement from the set $\{1, 2, \dots, 49\}$.
- **Part (a):** What is the probability of matching all 6 numbers if the order of the draw must also be matched exactly?
- **Part (b):** What is the probability of winning the jackpot if the 6 numbers can be matched in any order?

**Necessary work.**  
- **Part (a): Ordered Draw:**
  - Total ordered sequences: $n(\Omega_{\text{ord}}) = P(49, 6) = 49 \times 48 \times 47 \times 46 \times 45 \times 44 = 10,068,347,520$.
  - Exactly 1 specific sequence matches: $n(\text{win}) = 1$.
  - $$P(\text{ordered win}) = \frac{1}{10,068,347,520} \approx 9.932 \times 10^{-11} \quad (9.932 \times 10^{-9}\%)$$
- **Part (b): Unordered Draw:**
  - *Method 1 (Combinations):* Total unordered subsets: $\binom{49}{6} = \frac{10,068,347,520}{6!} = 13,983,816$. A single ticket matches 1 subset.
    $$P(\text{win}) = \frac{1}{13,983,816} \approx 7.1511 \times 10^{-8} \quad (0.00000715\%)$$
  - *Method 2 (Permutations):* Favorable ordered outcomes $= 6! = 720$.
    $$P(\text{win}) = \frac{6!}{P(49, 6)} = \frac{720}{10,068,347,520} = \frac{1}{13,983,816} \approx 7.1511 \times 10^{-8}$$

**Answer.**  
- (a) $P = \frac{1}{10,068,347,520} \approx 9.932 \times 10^{-11}$.
- (b) $P = \frac{1}{13,983,816} \approx 7.151 \times 10^{-8}$.

---

### Lecture Example 4: The Birthday Problem ($k = 10$)

**Source:** `W2/Week2-L0401-annotated(1).pdf`, Slide 23.  
**Relevant method:** [Problem Type PT-07](Study-Notes.md#problem-type-pt-07-complementary-counting-and-collision-problems-birthday-paradox)

**Question.**  
In a room of $k = 10$ randomly chosen individuals, what is the probability that at least two people share a birthday? (Assume 365 equally likely days in a year and independent birthdays).

**Necessary work.**  
- Total possible assignment of birthdays to 10 people:
  $$n(\Omega) = 365^{10} \approx 4.1958 \times 10^{25}$$
- Complement event $A^c$: "All 10 individuals have distinct birthdays."
  $$n(A^c) = P(365, 10) = 365 \times 364 \times 363 \times 362 \times 361 \times 360 \times 359 \times 358 \times 357 \times 356 \approx 3.7052 \times 10^{25}$$
- Ratio:
  $$P(A^c) = \frac{P(365, 10)}{365^{10}} \approx 0.88305$$
- Complement rule:
  $$P(A) = 1 - P(A^c) = 1 - 0.88305 = 0.11695 \approx 11.69\%$$

**Answer.**  
$P(\text{at least two share a birthday}) \approx 0.1169$ ($11.69\%$).

---

### Lecture Example 5: Arrangements of Colored Balls (Indistinguishable Objects)

**Source:** `W2/Week2-L0401-annotated(1).pdf`, Slides 24–25.  
**Relevant method:** [Problem Type PT-03](Study-Notes.md#problem-type-pt-03-permutations-with-indistinguishable-objects-and-digit-formation)

**Question.**  
An urn contains 6 balls: 2 identical red balls, 1 yellow ball, and 3 identical green balls. In how many distinct ways can all 6 balls be arranged in a line?

**Necessary work.**  
- If all 6 balls were distinct, there would be $6! = 720$ linear arrangements.
- However, the 2 red balls are indistinguishable, so any permutation of the red balls among their positions produces the same appearance ($2! = 2$ ways).
- The 3 green balls are indistinguishable, contributing $3! = 6$ identical arrangements.
- The 1 yellow ball has $1! = 1$ arrangement.
- By the Multinomial Permutation Formula:
  $$N = \frac{6!}{2! \, 1! \, 3!} = \frac{720}{2 \times 1 \times 6} = \frac{720}{12} = 60$$

**Answer.**  
$60$ distinct linear arrangements.

---

### Lecture Try For Yourself 2: Permutations of Digits $\{1, 2, 3, 3, 4, 4, 4\}$

**Source:** `W2/Week2-L0401-annotated(1).pdf`, Slide 26.  
**Relevant method:** [Problem Type PT-03](Study-Notes.md#problem-type-pt-03-permutations-with-indistinguishable-objects-and-digit-formation)

**Question.**  
Using all seven digits from the multiset $\{1, 2, 3, 3, 4, 4, 4\}$, how many distinct 7-digit natural numbers can be formed:
- **Part (a):** With no restrictions?
- **Part (b):** That are strictly less than $4,000,000$?
- **Part (c):** That are strictly less than $4,000,000$ and are even?

**Necessary work.**  
Total digits: $n = 7$ (one 1, one 2, two 3s, three 4s).
- **Part (a): No restrictions:**
  $$N_a = \frac{7!}{1! \, 1! \, 2! \, 3!} = \frac{5,040}{1 \times 1 \times 2 \times 6} = \frac{5,040}{12} = 420$$
- **Part (b): Less than $4,000,000$:**
  The first digit must be strictly less than 4, so the first digit must be 1, 2, or 3.
  - *Case 1: First digit is 1.* Remaining digits $\{2, 3, 3, 4, 4, 4\}$:
    $$N_1 = \frac{6!}{1! \, 2! \, 3!} = \frac{720}{12} = 60$$
  - *Case 2: First digit is 2.* Remaining digits $\{1, 3, 3, 4, 4, 4\}$:
    $$N_2 = \frac{6!}{1! \, 2! \, 3!} = \frac{720}{12} = 60$$
  - *Case 3: First digit is 3.* Remaining digits $\{1, 2, 3, 4, 4, 4\}$:
    $$N_3 = \frac{6!}{1! \, 1! \, 1! \, 3!} = \frac{720}{6} = 120$$
  Total $= 60 + 60 + 120 = 240$.
- **Part (c): Less than $4,000,000$ and even:**
  - First digit $\in \{1, 2, 3\}$, Last digit $\in \{2, 4\}$.
  - *Subcase 1: Last digit is 2.*
    First digit can be 1 or 3 (2 is unavailable since there is only one '2').
    - First = 1: remaining $\{3, 3, 4, 4, 4\} \implies \frac{5!}{2! 3!} = \frac{120}{12} = 10$.
    - First = 3: remaining $\{1, 3, 4, 4, 4\} \implies \frac{5!}{1! 1! 3!} = \frac{120}{6} = 20$.
    Subtotal for last digit 2 $= 10 + 20 = 30$.
  - *Subcase 2: Last digit is 4.*
    Remaining set of 4s has size $3 - 1 = 2$.
    - First = 1: remaining $\{2, 3, 3, 4, 4\} \implies \frac{5!}{1! 2! 2!} = \frac{120}{4} = 30$.
    - First = 2: remaining $\{1, 3, 3, 4, 4\} \implies \frac{5!}{1! 2! 2!} = 30$.
    - First = 3: remaining $\{1, 2, 3, 4, 4\} \implies \frac{5!}{1! 1! 1! 2!} = \frac{120}{2} = 60$.
    Subtotal for last digit 4 $= 30 + 30 + 60 = 120$.
  - Total $= 30 + 120 = 150$.

**Answer.**  
- (a) $420$ numbers.
- (b) $240$ numbers.
- (c) $150$ numbers.

---

### Lecture Example 6: Lunch with Friends (University vs. High School)

**Source:** `W2/Week2-L0401-annotated(1).pdf`, Slide 31.  
**Relevant method:** [Problem Type PT-04](Study-Notes.md#problem-type-pt-04-unordered-combinations-and-combinatorial-identity-proofs), [Problem Type PT-05](Study-Notes.md#problem-type-pt-05-multi-category-hypergeometric-sampling)

**Question.**  
You have 12 friends, consisting of 5 university friends and 7 high school friends. You decide to invite 5 friends to lunch.
- **Part (a):** How many different groups of 5 friends can you invite?
- **Part (b):** If the 5 friends are selected completely at random, what is the probability that all 5 invited friends are from high school?

**Necessary work.**  
- **Part (a):** Unordered selection of 5 from 12 distinct individuals without replacement:
  $$N = \binom{12}{5} = \frac{12 \times 11 \times 10 \times 9 \times 8}{5 \times 4 \times 3 \times 2 \times 1} = 792$$
- **Part (b):** Favorable outcomes: choosing 5 friends from the 7 high school friends:
  $$n(\text{all high school}) = \binom{7}{5} = \binom{7}{2} = \frac{7 \times 6}{2} = 21$$
  $$P(\text{all high school}) = \frac{\binom{7}{5}}{\binom{12}{5}} = \frac{21}{792} = \frac{7}{264} \approx 0.026515 \quad (2.65\%)$$

**Answer.**  
- (a) $792$ groups.
- (b) $P = \frac{7}{264} \approx 0.0265$ ($2.65\%$).

---

### Lecture Example 7: Poker Hand Subsets — Face Cards and Two Pair

**Source:** `W2/Week2-L0401-annotated(1).pdf`, Slides 32–33.  
**Relevant method:** [Problem Type PT-05](Study-Notes.md#problem-type-pt-05-multi-category-hypergeometric-sampling), [Problem Type PT-06](Study-Notes.md#problem-type-pt-06-symmetry-subgroup-partitioning-and-card-hand-derivations)

**Question.**  
A standard deck contains 52 cards: 12 face cards (J, Q, K), 36 numeric cards (2 through 10), and 4 Aces. A hand of 5 cards is dealt at random.
- **Part (a):** What is the probability that a 5-card hand contains exactly 4 face cards and 1 numeric card?
- **Part (b):** How many distinct Two Pair hands can be formed?

**Necessary work.**  
Total hands: $|\Omega| = \binom{52}{5} = 2,598,960$.
- **Part (a):**
  - Choose 4 face cards from 12: $\binom{12}{4} = 495$.
  - Choose 1 numeric card from 36: $\binom{36}{1} = 36$.
  - Number of favorable hands $= 495 \times 36 = 17,820$.
  - $$P(A) = \frac{17,820}{2,598,960} = \frac{297}{43,316} \approx 0.0068566 \quad (0.69\%)$$
- **Part (b):**
  - Select 2 ranks for the pairs from 13: $\binom{13}{2} = 78$.
  - Select 2 suits for the lower rank: $\binom{4}{2} = 6$.
  - Select 2 suits for the higher rank: $\binom{4}{2} = 6$.
  - Select 1 rank for the kicker from the remaining 11: $\binom{11}{1} = 11$.
  - Select 1 suit for the kicker: $\binom{4}{1} = 4$.
  - Total Two Pair hands $= 78 \times 6 \times 6 \times 11 \times 4 = 123,552$.

**Answer.**  
- (a) $P = \frac{297}{43,316} \approx 0.006857$ ($0.69\%$).
- (b) $123,552$ hands.

---

### Lecture Case Study: A Tale of Common Miscounts — Full House Analysis

**Source:** `W2/Week2-L0401-annotated(1).pdf`, Slide 34.  
**Relevant method:** [Problem Type PT-06](Study-Notes.md#problem-type-pt-06-symmetry-subgroup-partitioning-and-card-hand-derivations)

**Question.**  
Explain why each of the following two common student attempts to count the number of Full House hands ($3,744$) is incorrect, and show how to fix them:
- **Method 1 Attempt:** $52 \times 3 \times 2 \times 48 \times 3 = 44,928$.
- **Method 2 Attempt:** $\binom{13}{2} \times \binom{4}{3} \times \binom{4}{2} = 1,872$.

**Necessary work.**  
- **Analysis of Method 1:**
  - The student sequentially picks cards: 52 choices for card 1, 3 choices for card 2 of same rank, 2 choices for card 3 of same rank; then 48 choices for card 4 (new rank), 3 choices for card 5 of that second rank.
  - *Error:* This procedure generates the 3 cards in the triple in a specific temporal order ($3! = 6$ ways) and the 2 cards in the pair in a specific temporal order ($2! = 2$ ways). Because a poker hand is an unordered set, each unique Full House hand has been counted $3! \times 2! = 12$ times.
  - *Correction:* Divide by $12$:
    $$\frac{44,928}{3! \times 2!} = \frac{44,928}{12} = 3,744$$
- **Analysis of Method 2:**
  - The student selects 2 ranks using $\binom{13}{2} = 78$, then chooses 3 suits from the first rank and 2 suits from the second rank.
  - *Error:* The roles of the two ranks are asymmetric. One rank must supply 3 cards, while the other supplies 2 cards. Selecting an unordered pair of ranks $\{R_1, R_2\}$ fails to specify which rank is the triple and which is the pair ($R_1 R_1 R_1 R_2 R_2 \neq R_2 R_2 R_2 R_1 R_1$). This undercounts by a factor of 2.
  - *Correction:* Select ranks as an ordered pair (${}_{13}P_2 = 13 \times 12 = 156$):
    $${}_{13} P_2 \times \binom{4}{3} \times \binom{4}{2} = 156 \times 4 \times 6 = 3,744$$

**Answer.**  
Method 1 overcounts by $3! \times 2! = 12$ because it treats cards within the triple and pair as ordered. Method 2 undercounts by a factor of 2 because it treats the two rank roles as symmetric when they are asymmetric. Both corrections yield $3,744$.

---

## Section C: Textbook Exercises and Solutions

---

### MMSA — Basic Practice

#### MMSA Section 2.3, Exercise 31 (p. 72)
**Source:** MMSA Chapter 2, Section 2.3, Exercise 31 (Printed p. 72, PDF p. 85).  
**Difficulty:** Basic Practice.  
**Relevant method:** [Problem Type PT-01](Study-Notes.md#problem-type-pt-01-multi-stage-sequential-selection-via-fpc), [Problem Type PT-02](Study-Notes.md#problem-type-pt-02-ordered-permutations-of-distinct-objects-under-positional-constraints), [Problem Type PT-04](Study-Notes.md#problem-type-pt-04-unordered-combinations-and-combinatorial-identity-proofs).

**Question.**  
The College of Science Student Council has one representative from each of the five science departments (biology, chemistry, statistics, mathematics, physics). In how many ways can:
- **Part (a):** Both a council president and a vice president be selected?
- **Part (b):** A president, a vice president, and a secretary be selected?
- **Part (c):** Two members be selected for the Dean’s Council?

**Necessary work.**  
- **Part (a):** The positions of president and vice president are distinct roles. We select 2 individuals out of 5 in order without replacement:
  $$P(5, 2) = 5 \times 4 = 20$$
- **Part (b):** Selecting 3 individuals for 3 distinct roles (president, vice president, secretary) without replacement:
  $$P(5, 3) = 5 \times 4 \times 3 = 60$$
- **Part (c):** Two members are chosen for the Dean's Council with equal status; order does not matter:
  $$\binom{5}{2} = \frac{5 \times 4}{2 \times 1} = 10$$

**Answer.**  
- (a) $20$ ways.
- (b) $60$ ways.
- (c) $10$ ways.

---

#### MMSA Section 2.3, Exercise 33 (p. 72)
**Source:** MMSA Chapter 2, Section 2.3, Exercise 33 (Printed p. 72, PDF p. 85).  
**Difficulty:** Basic Practice.  
**Relevant method:** [Problem Type PT-01](Study-Notes.md#problem-type-pt-01-multi-stage-sequential-selection-via-fpc).

**Question.**  
- **Part (a):** Beethoven wrote 9 symphonies and Mozart wrote 27 piano concertos. If a university radio station announcer wishes to play first a Beethoven symphony and then a Mozart concerto, in how many ways can this be done?
- **Part (b):** The station manager decides that on each successive night (7 days per week), a Beethoven symphony will be played, followed by a Mozart piano concerto, followed by a Schubert string quartet (of which there are 15). For roughly how many years could this policy be continued before exactly the same program would have to be repeated?

**Necessary work.**  
- **Part (a):** Stage 1: Select 1 of 9 Beethoven symphonies ($n_1 = 9$). Stage 2: Select 1 of 27 Mozart concertos ($n_2 = 27$).
  By FPC:
  $$N_a = 9 \times 27 = 243$$
- **Part (b):** A nightly program consists of 1 Beethoven symphony ($n_1 = 9$), 1 Mozart concerto ($n_2 = 27$), and 1 Schubert string quartet ($n_3 = 15$).
  Total distinct programs:
  $$N_b = 9 \times 27 \times 15 = 3,645$$
  The station broadcasts 365 programs per year (or $365.25$ accounting for leap years).
  $$\text{Years} = \frac{3,645}{365} \approx 9.986 \text{ years} \quad \left(\text{or } \frac{3,645}{365.25} \approx 9.979 \text{ years}\right)$$

**Answer.**  
- (a) $243$ ways.
- (b) $3,645$ distinct programs; roughly $10$ years ($9.99$ years).

---

#### MMSA Section 2.3, Exercise 34 (pp. 72–73)
**Source:** MMSA Chapter 2, Section 2.3, Exercise 34 (Printed pp. 72–73, PDF pp. 85–86).  
**Difficulty:** Basic Practice.  
**Relevant method:** [Problem Type PT-01](Study-Notes.md#problem-type-pt-01-multi-stage-sequential-selection-via-fpc), [Problem Type PT-07](Study-Notes.md#problem-type-pt-07-complementary-counting-and-collision-problems-birthday-paradox).

**Question.**  
A chain of home electronics stores offers a special price on a complete set of components (receiver, CD/MP3 player, speakers). The manufacturers are:
- **Receiver:** Kenwood, Onkyo, Pioneer, Sony, Yamaha ($5$ choices; Sony is 1 of 5).
- **CD/MP3 player:** Onkyo, Pioneer, Sony, Panasonic ($4$ choices; Sony is 1 of 4).
- **Speakers:** Boston, Infinity, Polk ($3$ choices; no Sony model available).
- **Part (a):** In how many ways can one component of each type be selected?
- **Part (b):** In how many ways can components be selected if both the receiver and the CD/MP3 player are to be Sony?
- **Part (c):** In how many ways can components be selected if none is to be Sony?
- **Part (d):** In how many ways can a selection be made if at least one Sony component is to be included?
- **Part (e):** If someone flips switches on the selection in a completely random fashion, what is the probability that the system selected contains at least one Sony component? Exactly one Sony component?

**Necessary work.**  
- **Part (a):** Total selections $= 5 \times 4 \times 3 = 60$.
- **Part (b):** Receiver is Sony ($1$ choice), CD is Sony ($1$ choice), speakers ($3$ choices):
  $$N_b = 1 \times 1 \times 3 = 3$$
- **Part (c):** Non-Sony choices: Receiver has $5 - 1 = 4$ non-Sony; CD has $4 - 1 = 3$ non-Sony; speakers have $3$ non-Sony.
  $$N_c = 4 \times 3 \times 3 = 36$$
- **Part (d):** Using the complement rule:
  $$N(\ge 1 \text{ Sony}) = N_{\text{total}} - N(\text{no Sony}) = 60 - 36 = 24$$
- **Part (e):**
  - $$P(\ge 1 \text{ Sony}) = \frac{24}{60} = \frac{2}{5} = 0.40$$
  - Exactly one Sony component can happen in two disjoint ways (since speakers cannot be Sony):
    1. Receiver is Sony, CD is not Sony, speakers any: $1 \times 3 \times 3 = 9$.
    2. Receiver is not Sony, CD is Sony, speakers any: $4 \times 1 \times 3 = 12$.
    Total $= 9 + 12 = 21$.
    $$P(\text{exactly 1 Sony}) = \frac{21}{60} = \frac{7}{20} = 0.35$$

**Answer.**  
- (a) $60$ ways.
- (b) $3$ ways.
- (c) $36$ ways.
- (d) $24$ ways.
- (e) $P(\ge 1 \text{ Sony}) = 0.40$; $P(\text{exactly 1 Sony}) = 0.35$.

---

### MMSA — Medium Practice

#### MMSA Section 2.3, Exercise 35 (p. 73)
**Source:** MMSA Chapter 2, Section 2.3, Exercise 35 (Printed p. 73, PDF p. 86).  
**Difficulty:** Medium Practice.  
**Relevant method:** [Problem Type PT-01](Study-Notes.md#problem-type-pt-01-multi-stage-sequential-selection-via-fpc), [Problem Type PT-02](Study-Notes.md#problem-type-pt-02-ordered-permutations-of-distinct-objects-under-positional-constraints).

**Question.**  
A particular iPod playlist contains 100 songs, of which 10 are by the Beatles. Suppose the shuffle feature is used to play the songs in random order (each permutation of the 100 songs is equally likely). What is the probability that the first Beatles song heard is the fifth song played?

**Necessary work.**  
- For the first Beatles song to be the fifth song played, songs 1, 2, 3, and 4 must all be non-Beatles songs ($90$ non-Beatles available), and song 5 must be a Beatles song ($10$ Beatles available).
- **Method 1: Conditional probability / Sequential stages:**
  $$P = \frac{90}{100} \times \frac{89}{99} \times \frac{88}{98} \times \frac{87}{97} \times \frac{10}{96}$$
  $$\frac{90 \times 89 \times 88 \times 87 \times 10}{100 \times 99 \times 98 \times 97 \times 96} = \frac{613,245,600}{9,034,502,400} = \frac{2,581}{38,024} \approx 0.06787818$$
- **Method 2: Combinations of positions:**
  Alternatively, consider the 10 positions occupied by the Beatles songs out of the 100 possible play slots. There are $\binom{100}{10}$ equally likely choices of positions.
  For the first Beatles song to appear at slot 5, slot 5 must be chosen, no slots in $\{1, 2, 3, 4\}$ are chosen, and the remaining 9 Beatles songs must occupy 9 of the remaining 95 slots $\{6, 7, \dots, 100\}$:
  $$P = \frac{\binom{1}{1}\binom{95}{9}}{\binom{100}{10}} = \frac{\frac{95!}{9!86!}}{\frac{100!}{10!90!}} = \frac{10}{100} \times \frac{90 \times 89 \times 88 \times 87}{99 \times 98 \times 97 \times 96} = \frac{2,581}{38,024} \approx 0.06788$$

**Answer.**  
$P = \frac{2,581}{38,024} \approx 0.06788$ ($6.79\%$).

---

#### MMSA Section 2.3, Exercise 37 (p. 73)
**Source:** MMSA Chapter 2, Section 2.3, Exercise 37 (Printed p. 73, PDF p. 86).  
**Difficulty:** Medium Practice.  
**Relevant method:** [Problem Type PT-04](Study-Notes.md#problem-type-pt-04-unordered-combinations-and-combinatorial-identity-proofs), [Problem Type PT-05](Study-Notes.md#problem-type-pt-05-multi-category-hypergeometric-sampling).

**Question.**  
The statistics department faculty consists of 5 women and 11 men (16 total). A 6-person volleyball team is to be chosen.
- **Part (a):** How many different six-person rosters could be generated?
- **Part (b):** How many rosters comprised of exactly 2 women and 4 men can be generated?
- **Part (c):** The tournament requires at least two women. How many valid teams could be generated?
- **Part (d):** If the 6 team members are selected at random, what is the probability that the team has exactly two women? At least two women?

**Necessary work.**  
- **Part (a):** Total teams:
  $$\binom{16}{6} = \frac{16 \times 15 \times 14 \times 13 \times 12 \times 11}{6 \times 5 \times 4 \times 3 \times 2 \times 1} = 8,008$$
- **Part (b):** Choose 2 women from 5 and 4 men from 11:
  $$\binom{5}{2} \binom{11}{4} = 10 \times 330 = 3,300$$
- **Part (c):** "At least two women" can be found using the complement:
  - Total teams: $8,008$.
  - 0 women: $\binom{5}{0}\binom{11}{6} = 1 \times 462 = 462$.
  - 1 woman: $\binom{5}{1}\binom{11}{5} = 5 \times 462 = 2,310$.
  - Number with $\ge 2$ women $= 8,008 - (462 + 2,310) = 8,008 - 2,772 = 5,236$.
- **Part (d):**
  - $$P(\text{exactly 2 women}) = \frac{3,300}{8,008} = \frac{75}{182} \approx 0.4120879 \quad (41.21\%)$$
  - $$P(\ge 2 \text{ women}) = \frac{5,236}{8,008} = \frac{17}{26} \approx 0.6538462 \quad (65.38\%)$$

**Answer.**  
- (a) $8,008$ rosters.
- (b) $3,300$ rosters.
- (c) $5,236$ valid rosters.
- (d) $P(\text{exactly 2}) = \frac{75}{182} \approx 0.4121$; $P(\ge 2) = \frac{17}{26} \approx 0.6538$.

---

#### MMSA Section 2.3, Exercise 39 (p. 73)
**Source:** MMSA Chapter 2, Section 2.3, Exercise 39 (Printed p. 73, PDF p. 86).  
**Difficulty:** Medium Practice.  
**Relevant method:** [Problem Type PT-03](Study-Notes.md#problem-type-pt-03-permutations-with-indistinguishable-objects-and-digit-formation), [Problem Type PT-06](Study-Notes.md#problem-type-pt-06-symmetry-subgroup-partitioning-and-card-hand-derivations).

**Question.**  
In an election for department chair, there are two candidates, A and B. When the five faculty votes are tallied, candidate A receives 3 votes and candidate B receives 2 votes. If the vote slips are selected and tallied in random order, what is the probability that candidate A remains strictly ahead of candidate B throughout the entire vote count?

**Necessary work.**  
- Total possible tally sequences consisting of 3 A's and 2 B's:
  $$N(S) = \frac{5!}{3! \, 2!} = \binom{5}{2} = 10$$
- An outcome satisfies the condition if at every step $k \in \{1, 2, 3, 4, 5\}$, the cumulative votes for A exceed those for B: $N_A(k) > N_B(k)$.
  Let us examine all 10 sequences:
  1. $A A A B B$: Counts: $1-0, 2-0, 3-0, 3-1, 3-2$. (Valid)
  2. $A A B A B$: Counts: $1-0, 2-0, 2-1, 3-1, 3-2$. (Valid)
  3. $A A B B A$: Counts: $1-0, 2-0, 2-1, 2-2$ (Tied at step 4! Invalid)
  4. $A B A A B$: Counts: $1-0, 1-1$ (Tied at step 2! Invalid)
  5. $A B A B A$: Tied at step 2. (Invalid)
  6. $A B B A A$: Tied at step 2. (Invalid)
  7. $B A A A B$: First vote B. (Invalid)
  8. $B A A B A$: First vote B. (Invalid)
  9. $B A B A A$: First vote B. (Invalid)
  10. $B B A A A$: First vote B. (Invalid)
- Exactly 2 sequences ($A A A B B$ and $A A B A B$) keep A strictly ahead.
- General verification via **Bertrand’s Ballot Theorem**: If candidate A receives $a$ votes and candidate B receives $b$ votes ($a > b$), the probability that A is strictly ahead throughout is $\frac{a - b}{a + b}$. Here, $a=3, b=2 \implies \frac{3 - 2}{3 + 2} = \frac{1}{5} = 0.20$.
- Both methods yield:
  $$P(\text{A strictly ahead}) = \frac{2}{10} = \frac{1}{5} = 0.20$$

**Answer.**  
$P = \frac{1}{5} = 0.20$ ($20\%$).

---

#### MMSA Section 2.3, Exercise 40 (pp. 73–74)
**Source:** MMSA Chapter 2, Section 2.3, Exercise 40 (Printed pp. 73–74, PDF pp. 86–87).  
**Difficulty:** Medium Practice.  
**Relevant method:** [Problem Type PT-01](Study-Notes.md#problem-type-pt-01-multi-stage-sequential-selection-via-fpc).

**Question.**  
An experiment investigates the effects of 3 temperatures, 4 pressures, and 5 catalysts on the yield of a chemical reaction.
- **Part (a):** How many experimental runs are possible if each run uses 1 temperature, 1 pressure, and 1 catalyst?
- **Part (b):** How many runs involve the lowest temperature and one of the two lowest pressures?

**Necessary work.**  
- **Part (a):** By FPC across the three factors:
  $$N_a = 3 \times 4 \times 5 = 60$$
- **Part (b):**
  - Temperature: lowest temperature only $\implies 1$ choice.
  - Pressure: two lowest pressures $\implies 2$ choices.
  - Catalyst: any catalyst $\implies 5$ choices.
  $$N_b = 1 \times 2 \times 5 = 10$$

**Answer.**  
- (a) $60$ experimental runs.
- (b) $10$ experimental runs.

---

#### MMSA Section 2.3, Exercise 44 (p. 74)
**Source:** MMSA Chapter 2, Section 2.3, Exercise 44 (Printed p. 74, PDF p. 87).  
**Difficulty:** Medium Practice.  
**Relevant method:** [Problem Type PT-02](Study-Notes.md#problem-type-pt-02-ordered-permutations-of-distinct-objects-under-positional-constraints), [Problem Type PT-03](Study-Notes.md#problem-type-pt-03-permutations-with-indistinguishable-objects-and-digit-formation).

**Question.**  
A polymer molecule consists of a chain of 12 monomers: 3 of type A, 3 of type B, 3 of type C, and 3 of type D.
- **Part (a):** How many distinct chain molecules can be formed?
- **Part (b):** If the monomers assemble in random order, what is the probability that all 3 molecules of each type end up next to each other (i.e., all A's together, all B's together, all C's together, and all D's together)?

**Necessary work.**  
- **Part (a):** We are arranging a multiset of size $n = 12$ with repetition counts $n_A = 3, n_B = 3, n_C = 3, n_D = 3$.
  Using the multinomial coefficient:
  $$N = \frac{12!}{3! \, 3! \, 3! \, 3!} = \frac{479,001,600}{6 \times 6 \times 6 \times 6} = \frac{479,001,600}{1,296} = 369,600$$
- **Part (b):** To have all monomers of each type adjacent, we treat each identical triplet as a single block:
  $$[AAA], \quad [BBB], \quad [CCC], \quad [DDD]$$
  There are 4 blocks. Since the items inside each block are identical, there is only 1 way to order within each block.
  The number of ways to arrange the 4 distinct blocks is:
  $$4! = 24$$
  The probability under uniform random assembly is:
  $$P = \frac{24}{369,600} = \frac{1}{15,400} \approx 6.4935 \times 10^{-5}$$

**Answer.**  
- (a) $369,600$ distinct chains.
- (b) $P = \frac{1}{15,400} \approx 6.4935 \times 10^{-5}$ ($0.00649\%$).

---

### MMSA — Test Level

#### MMSA Section 2.3, Exercise 38 (p. 73)
**Source:** MMSA Chapter 2, Section 2.3, Exercise 38 (Printed p. 73, PDF p. 86).  
**Difficulty:** Test Level.  
**Relevant method:** [Problem Type PT-05](Study-Notes.md#problem-type-pt-05-multi-category-hypergeometric-sampling), [Problem Type PT-08](Study-Notes.md#problem-type-pt-08-generalized-principle-of-inclusion-exclusion-n-ge-3-events).

**Question.**  
A manufacturing plant has 45 employees: 20 on the Day shift ($D$), 15 on the Swing shift ($S$), and 10 on the Graveyard shift ($G$). A safety committee of 6 workers is selected at random without replacement.
- **Part (a):** How many selections result in all 6 workers coming from the day shift? What is the probability of this event?
- **Part (b):** What is the probability that all 6 selected workers will be from the same shift?
- **Part (c):** What is the probability that at least two different shifts will be represented?
- **Part (d):** What is the probability that at least one shift will be unrepresented?

**Necessary work.**  
Total sample space:
$$|\Omega| = \binom{45}{6} = \frac{45 \times 44 \times 43 \times 42 \times 41 \times 40}{6!} = 8,145,060$$
- **Part (a): All 6 from Day shift:**
  - Favorable ways: $\binom{20}{6} = 38,760$.
  - $$P(\text{all Day}) = \frac{38,760}{8,145,060} = \frac{646}{135,751} \approx 0.0047587 \quad (0.476\%)$$
- **Part (b): All 6 from the same shift:**
  Since the shifts are mutually exclusive:
  $$N(\text{same shift}) = \binom{20}{6} + \binom{15}{6} + \binom{10}{6} = 38,760 + 5,005 + 210 = 43,975$$
  $$P(\text{same shift}) = \frac{43,975}{8,145,060} = \frac{8,795}{1,629,012} \approx 0.00539898 \quad (0.540\%)$$
- **Part (c): At least two shifts represented:**
  This is the complement of "all 6 workers from the same shift":
  $$P(\ge 2 \text{ shifts}) = 1 - P(\text{same shift}) = 1 - \frac{43,975}{8,145,060} = \frac{8,101,085}{8,145,060} = \frac{1,620,217}{1,629,012} \approx 0.994601 \quad (99.46\%)$$
- **Part (d): At least one shift unrepresented:**
  Let $A_1$ = Day unrepresented, $A_2$ = Swing unrepresented, $A_3$ = Graveyard unrepresented.
  We want $P(A_1 \cup A_2 \cup A_3)$.
  Using the Principle of Inclusion-Exclusion:
  - $|A_1| = \binom{45 - 20}{6} = \binom{25}{6} = 177,100$ (all 6 from Swing + Graveyard).
  - $|A_2| = \binom{45 - 15}{6} = \binom{30}{6} = 593,775$ (all 6 from Day + Graveyard).
  - $|A_3| = \binom{45 - 10}{6} = \binom{35}{6} = 1,623,160$ (all 6 from Day + Swing).
  - $|A_1 \cap A_2| = \binom{10}{6} = 210$ (all 6 from Graveyard).
  - $|A_1 \cap A_3| = \binom{15}{6} = 5,005$ (all 6 from Swing).
  - $|A_2 \cap A_3| = \binom{20}{6} = 38,760$ (all 6 from Day).
  - $|A_1 \cap A_2 \cap A_3| = \binom{0}{6} = 0$ (cannot select 6 from 0 workers).
  Summing:
  $$|A_1 \cup A_2 \cup A_3| = (177,100 + 593,775 + 1,623,160) - (210 + 5,005 + 38,760) + 0$$
  $$= 2,394,035 - 43,975 = 2,350,060$$
  $$P(\ge 1 \text{ unrepresented}) = \frac{2,350,060}{8,145,060} = \frac{117,503}{407,253} \approx 0.2885258 \quad (28.85\%)$$

**Answer.**  
- (a) $\binom{20}{6} = 38,760$; $P \approx 0.004759$.
- (b) $P = \frac{43,975}{8,145,060} \approx 0.005399$.
- (c) $P = 1 - 0.005399 \approx 0.9946$.
- (d) $P = \frac{2,350,060}{8,145,060} \approx 0.2885$.

---

#### MMSA Section 2.3, Exercise 43 (p. 74)
**Source:** MMSA Chapter 2, Section 2.3, Exercise 43 (Printed p. 74, PDF p. 87).  
**Difficulty:** Test Level.  
**Relevant method:** [Problem Type PT-05](Study-Notes.md#problem-type-pt-05-multi-category-hypergeometric-sampling), [Problem Type PT-06](Study-Notes.md#problem-type-pt-06-symmetry-subgroup-partitioning-and-card-hand-derivations).

**Question.**  
A service facility has 15 telephones awaiting repair: 5 cellular, 5 cordless, and 5 corded phones. The order of servicing is randomly assigned.
- **Part (a):** What is the probability that all 5 cordless phones are among the first 10 serviced?
- **Part (b):** What is the probability that after servicing 10 phones, phones of only two of the three types remain to be serviced?
- **Part (c):** What is the probability that two phones of each type are among the first six serviced?

**Necessary work.**  
- **Part (a):** Focus on the set of the first 10 phones serviced. This is an unordered sample of size 10 from 15 phones.
  - Total ways to choose 10 phones: $\binom{15}{10} = 3,003$.
  - Favorable ways (all 5 cordless phones are included, and remaining 5 phones are chosen from the 10 other phones):
    $$\binom{5}{5} \binom{10}{5} = 1 \times 252 = 252$$
  - $$P = \frac{252}{3,003} = \frac{12}{143} \approx 0.083916 \quad (8.39\%)$$
- **Part (b):** "Phones of only two of the three types remain to be serviced."
  - After 10 phones are serviced, exactly $15 - 10 = 5$ phones remain in the shop.
  - The remaining 5 phones must contain representatives from **exactly two types**. This means exactly one phone type was completely exhausted (all 5 serviced in the first 10), and the other two types have at least 1 remaining.
  - Choose the 1 type that is completely exhausted: $\binom{3}{1} = 3$ ways.
  - From the other two types (10 phones), the remaining 5 unserviced phones must be chosen such that NOT all 5 are of the same type:
    $$\binom{10}{5} - \binom{5}{5} - \binom{5}{5} = 252 - 1 - 1 = 250 \text{ ways}$$
  - Total favorable sets of 5 remaining phones $= 3 \times 250 = 750$.
  - $$P = \frac{750}{\binom{15}{5}} = \frac{750}{3,003} = \frac{250}{1,001} \approx 0.249750 \quad (24.98\%)$$
  *(Note on interpretation: If "only two types remain" is loosely interpreted as "at most two types remain", we add the 3 cases where all 5 remaining phones are of a single type, giving $\frac{753}{3003} = \frac{251}{1001} \approx 0.2507$. The standard rigorous interpretation is "exactly two", yielding $250/1001$).*
- **Part (c): Two of each type in the first 6:**
  - Sample size is 6 from 15.
  - Total ways: $\binom{15}{6} = 5,005$.
  - Favorable ways (2 cellular, 2 cordless, 2 corded):
    $$\binom{5}{2} \binom{5}{2} \binom{5}{2} = 10 \times 10 \times 10 = 1,000$$
  - $$P = \frac{1,000}{5,005} = \frac{200}{1,001} \approx 0.1998002 \quad (19.98\%)$$

**Answer.**  
- (a) $P = \frac{12}{143} \approx 0.0839$.
- (b) $P = \frac{250}{1,001} \approx 0.2498$ (or $\frac{251}{1,001} \approx 0.2507$ if inclusive).
- (c) $P = \frac{200}{1,001} \approx 0.1998$.

---

#### MMSA Section 2.3, Exercise 45 (p. 74)
**Source:** MMSA Chapter 2, Section 2.3, Exercise 45 (Printed p. 74, PDF p. 87).  
**Difficulty:** Test Level.  
**Relevant method:** [Problem Type PT-02](Study-Notes.md#problem-type-pt-02-ordered-permutations-of-distinct-objects-under-positional-constraints), [Problem Type PT-08](Study-Notes.md#problem-type-pt-08-generalized-principle-of-inclusion-exclusion-n-ge-3-events).

**Question.**  
Three married couples are seated in a row of 6 seats at random. Total possible seatings $= 6! = 720$.
- **Part (a):** What is the probability that Jim and Paula (one of the couples) sit in the two seats on the far left?
- **Part (b):** What is the probability that Jim and Paula sit next to one another?
- **Part (c):** What is the probability that at least one of the wives sits next to her husband?

**Necessary work.**  
- **Part (a):** Jim and Paula occupy seats 1 and 2:
  - Internal arrangement of Jim and Paula: $2! = 2$ ways.
  - Remaining 4 people seated in seats 3, 4, 5, 6: $4! = 24$ ways.
  - Favorable $= 2 \times 24 = 48$.
  - $$P = \frac{48}{720} = \frac{1}{15} \approx 0.066667 \quad (6.67\%)$$
- **Part (b):** Jim and Paula sit adjacent anywhere:
  - Treat $\{J, P\}$ as 1 block.
  - Arrange 5 entities ($[JP]$ and the other 4 people): $5! = 120$ ways.
  - Internal arrangement of the couple: $2! = 2$ ways.
  - Favorable $= 5! \times 2! = 240$.
  - $$P = \frac{240}{720} = \frac{1}{3} \approx 0.333333 \quad (33.33\%)$$
- **Part (c): At least one couple sits together:**
  Let $E_1, E_2, E_3$ be the events that Couple 1, Couple 2, Couple 3 sit together, respectively.
  We want $P(E_1 \cup E_2 \cup E_3)$.
  By the Principle of Inclusion-Exclusion:
  - Single event $|E_i|$: Couple $i$ forms 1 block $\implies 5$ units arranged in $5! \times 2^1 = 240$ ways.
    $$\sum_{i=1}^3 |E_i| = 3 \times 240 = 720$$
  - Pairwise intersection $|E_i \cap E_j|$ ($i \neq j$): Two couples form two separate blocks.
    Remaining units: 2 blocks + 2 single people $= 4$ units.
    Arranged in $4! \times 2^2 = 24 \times 4 = 96$ ways.
    Number of pairs of couples: $\binom{3}{2} = 3$.
    $$\sum_{1 \le i < j \le 3} |E_i \cap E_j| = 3 \times 96 = 288$$
  - Triple intersection $|E_1 \cap E_2 \cap E_3|$: All three couples form blocks.
    Remaining units: 3 blocks $= 3$ units.
    Arranged in $3! \times 2^3 = 6 \times 8 = 48$ ways.
  - Total favorable arrangements by PIE:
    $$|E_1 \cup E_2 \cup E_3| = 720 - 288 + 48 = 480$$
  - Probability:
    $$P(E_1 \cup E_2 \cup E_3) = \frac{480}{720} = \frac{2}{3} \approx 0.666667 \quad (66.67\%)$$

**Answer.**  
- (a) $P = \frac{1}{15} \approx 0.0667$.
- (b) $P = \frac{1}{3} \approx 0.3333$.
- (c) $P = \frac{2}{3} \approx 0.6667$.

---

#### MMSA Section 2.3, Exercise 47 (p. 75)
**Source:** MMSA Chapter 2, Section 2.3, Exercise 47 (Printed p. 75, PDF p. 88).  
**Difficulty:** Test Level.  
**Relevant method:** [Problem Type PT-04](Study-Notes.md#problem-type-pt-04-unordered-combinations-and-combinatorial-identity-proofs).

**Question.**  
Show that for any positive integers $n$ and $k$ with $k \le n$, $\binom{n}{k} = \binom{n}{n-k}$. Give an interpretation of this result in terms of selecting subsets.

**Necessary work.**  
- **Algebraic Verification:**
  By definition:
  $$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$
  Replacing $k$ with $n-k$:
  $$\binom{n}{n-k} = \frac{n!}{(n-k)!(n - (n-k))!} = \frac{n!}{(n-k)!k!} = \frac{n!}{k!(n-k)!} = \binom{n}{k}$$
- **Subset Interpretation (Bijective Argument):**
  Consider a master set $S$ with $|S| = n$. Every time we choose an unordered subset $A \subseteq S$ of size $k$, we simultaneously and uniquely determine a complement subset $A^c = S \setminus A$ of size $n - k$ consisting of all elements that were *not* chosen.
  Because every $k$-element subset corresponds to exactly one $(n-k)$-element subset and vice versa, the mapping $A \mapsto S \setminus A$ is a one-to-one correspondence (bijection). Hence, the number of distinct ways to choose $k$ elements to include equals the number of distinct ways to choose $n-k$ elements to exclude:
  $$\binom{n}{k} = \binom{n}{n-k}$$

**Answer.**  
Both the algebraic identity and the bijective subset-complement interpretation rigorously verify that $\binom{n}{k} = \binom{n}{n-k}$.

---

### PAR — Basic Practice

#### PAR Chapter 1, Exercise 16 (p. 38)
**Source:** PAR Chapter 1, Exercise 16 (Printed p. 38, PDF p. 58).  
**Difficulty:** Basic Practice.  
**Relevant method:** [Problem Type PT-01](Study-Notes.md#problem-type-pt-01-multi-stage-sequential-selection-via-fpc), [Problem Type PT-02](Study-Notes.md#problem-type-pt-02-ordered-permutations-of-distinct-objects-under-positional-constraints).

**Question.**  
A club has 10 members, including Nasir, Rose, and Devin. An election is held to fill three distinct officer positions: President, Vice President, and Treasurer. Each position must be held by a different person.
- **Part (a):** What is the probability that Nasir is elected President?
- **Part (b):** What is the probability that Rose is President and Devin is Treasurer?
- **Part (c):** What is the probability that neither Nasir, Rose, nor Devin obtain an officer position?

**Necessary work.**  
Total possible slates of officers: $|\Omega| = P(10, 3) = 10 \times 9 \times 8 = 720$.
- **Part (a):** Nasir is fixed as President ($1$ choice). VP can be any of the remaining 9 members, and Treasurer can be any of the remaining 8 members:
  $$N_a = 1 \times 9 \times 8 = 72 \implies P = \frac{72}{720} = \frac{1}{10} = 0.10$$
- **Part (b):** Rose is President ($1$ choice), Devin is Treasurer ($1$ choice). VP can be any of the remaining $10 - 2 = 8$ members:
  $$N_b = 1 \times 8 \times 1 = 8 \implies P = \frac{8}{720} = \frac{1}{90} \approx 0.011111 \quad (1.11\%)$$
- **Part (c):** None of the 3 specified individuals receive any position. All 3 positions must be filled from the other $10 - 3 = 7$ members:
  $$N_c = P(7, 3) = 7 \times 6 \times 5 = 210 \implies P = \frac{210}{720} = \frac{7}{24} \approx 0.291667 \quad (29.17\%)$$

**Answer.**  
- (a) $P = \frac{1}{10} = 0.10$.
- (b) $P = \frac{1}{90} \approx 0.0111$.
- (c) $P = \frac{7}{24} \approx 0.2917$.

---

#### PAR Chapter 1, Exercise 17 (p. 38)
**Source:** PAR Chapter 1, Exercise 17 (Printed p. 38, PDF p. 58).  
**Difficulty:** Basic Practice.  
**Relevant method:** [Problem Type PT-01](Study-Notes.md#problem-type-pt-01-multi-stage-sequential-selection-via-fpc).

**Question.**  
A fair coin is flipped 6 times. What is the probability that the first two flips are heads and the last two flips are tails? Answer the question using the Multiplication Principle.

**Necessary work.**  
- Total possible sequences of 6 coin flips: $|\Omega| = 2^6 = 64$.
- The favorable event requires the sequence $(H, H, *, *, T, T)$ where $*$ denotes any outcome ($\{H, T\}$).
- By the Multiplication Principle, the number of favorable sequences is:
  $$N = 1 \times 1 \times 2 \times 2 \times 1 \times 1 = 4$$
- Since all 64 sequences are equally likely:
  $$P = \frac{4}{64} = \frac{1}{16} = 0.0625 \quad (6.25\%)$$
- *(Direct product of probabilities check: $\frac{1}{2} \times \frac{1}{2} \times 1 \times 1 \times \frac{1}{2} \times \frac{1}{2} = \frac{1}{16}$.)*

**Answer.**  
$P = \frac{1}{16} = 0.0625$ ($6.25\%$).

---

#### PAR Chapter 1, Exercise 21 (p. 38)
**Source:** PAR Chapter 1, Exercise 21 (Printed p. 38, PDF p. 58).  
**Difficulty:** Basic Practice.  
**Relevant method:** [Problem Type PT-02](Study-Notes.md#problem-type-pt-02-ordered-permutations-of-distinct-objects-under-positional-constraints), [Problem Type PT-04](Study-Notes.md#problem-type-pt-04-unordered-combinations-and-combinatorial-identity-proofs).

**Question.**  
Suppose $k$ numbers are chosen without replacement from the set $\{1, 2, \dots, n\}$, where $k \le n$. What is the probability that the numbers are chosen in strictly increasing order?

**Necessary work.**  
- **Sample Space:** The experiment specifies choosing $k$ numbers sequentially without replacement. The total number of ordered samples is:
  $$|\Omega| = P(n, k) = \frac{n!}{(n-k)!}$$
- **Favorable Outcomes:** Any subset of $k$ distinct numbers $\{x_1, x_2, \dots, x_k\}$ can be ordered in $k!$ different ways, but **exactly one** of these orderings is strictly increasing ($x_{(1)} < x_{(2)} < \dots < x_{(k)}$).
  Therefore, each unordered subset of size $k$ produces exactly one favorable sequence:
  $$N(\text{increasing}) = \binom{n}{k} = \frac{n!}{k!(n-k)!}$$
- **Probability:**
  $$P(\text{increasing}) = \frac{\binom{n}{k}}{P(n, k)} = \frac{\frac{n!}{k!(n-k)!}}{\frac{n!}{(n-k)!}} = \frac{1}{k!}$$
- **Symmetry / Exchangeability Argument:** For any chosen set of $k$ distinct values, all $k!$ permutations are equally likely to appear. Exactly 1 permutation is sorted in increasing order. Hence, $P = \frac{1}{k!}$, independent of $n$!

**Answer.**  
$P = \frac{1}{k!}$.

---

### PAR — Medium Practice

#### PAR Chapter 1, Exercise 19 (p. 38)
**Source:** PAR Chapter 1, Exercise 19 (Printed p. 38, PDF p. 58).  
**Difficulty:** Medium Practice.  
**Relevant method:** [Problem Type PT-01](Study-Notes.md#problem-type-pt-01-multi-stage-sequential-selection-via-fpc), [Problem Type PT-07](Study-Notes.md#problem-type-pt-07-complementary-counting-and-collision-problems-birthday-paradox).

**Question.**  
Throw 5 fair dice.
- **Part (a):** What is the probability that all 5 dice show the same number (a Yahtzee)?
- **Part (b):** What is the probability of getting at least one 4?
- **Part (c):** What is the probability that all 5 dice show different numbers?

**Necessary work.**  
Total possible outcomes (ordered sequences): $|\Omega| = 6^5 = 7,776$.
- **Part (a):** There are 6 possible outcomes where all dice match: $(1,1,1,1,1), \dots, (6,6,6,6,6)$.
  $$P(\text{all same}) = \frac{6}{7,776} = \frac{1}{1,296} \approx 0.00077160 \quad (0.0772\%)$$
- **Part (b):** Complement is "no die shows a 4". Each die has 5 non-4 faces:
  $$N(\text{no 4}) = 5^5 = 3,125$$
  $$P(\ge 1 \text{ four}) = 1 - \frac{5^5}{6^5} = 1 - \frac{3,125}{7,776} = \frac{4,651}{7,776} \approx 0.598122 \quad (59.81\%)$$
- **Part (c):** All 5 dice show distinct faces $\implies$ ordered selection of 5 distinct faces from 6 without replacement:
  $$N(\text{all different}) = P(6, 5) = 6 \times 5 \times 4 \times 3 \times 2 = 720$$
  $$P(\text{all different}) = \frac{720}{7,776} = \frac{5}{54} \approx 0.0925926 \quad (9.26\%)$$

**Answer.**  
- (a) $P = \frac{1}{1,296} \approx 0.000772$.
- (b) $P = \frac{4,651}{7,776} \approx 0.5981$.
- (c) $P = \frac{5}{54} \approx 0.0926$.

---

#### PAR Chapter 1, Exercise 20 (p. 38)
**Source:** PAR Chapter 1, Exercise 20 (Printed p. 38, PDF p. 58).  
**Difficulty:** Medium Practice.  
**Relevant method:** [Problem Type PT-04](Study-Notes.md#problem-type-pt-04-unordered-combinations-and-combinatorial-identity-proofs), [Problem Type PT-05](Study-Notes.md#problem-type-pt-05-multi-category-hypergeometric-sampling).

**Question.**  
A college offers 20 courses, three of which are Probability 101, 102, and 103. Suppose a student picks 3 courses completely at random.
- **Part (a):** What is the probability of getting Probability 101?
- **Part (b):** What is the probability of getting both Probability 101 and 102?
- **Part (c):** What is the probability of getting all three Probability courses?

**Necessary work.**  
Total combinations of 3 courses: $|\Omega| = \binom{20}{3} = \frac{20 \times 19 \times 18}{6} = 1,140$.
- **Part (a):** Probability 101 is selected (1 course); remaining 2 courses are selected from the other 19 courses:
  $$N_a = \binom{1}{1} \binom{19}{2} = 1 \times \frac{19 \times 18}{2} = 171$$
  $$P(\text{Prob 101}) = \frac{171}{1,140} = \frac{3}{20} = 0.15 \quad (15\%)$$
- **Part (b):** Probability 101 and 102 are both selected (2 courses); remaining 1 course is selected from the other 18:
  $$N_b = \binom{2}{2} \binom{18}{1} = 1 \times 18 = 18$$
  $$P(\text{Prob 101 and 102}) = \frac{18}{1,140} = \frac{3}{190} \approx 0.0157895 \quad (1.58\%)$$
- **Part (c):** All 3 Probability courses are selected:
  $$N_c = \binom{3}{3} = 1$$
  $$P(\text{all 3}) = \frac{1}{1,140} \approx 0.00087719 \quad (0.0877\%)$$

**Answer.**  
- (a) $P = \frac{3}{20} = 0.15$.
- (b) $P = \frac{3}{190} \approx 0.0158$.
- (c) $P = \frac{1}{1,140} \approx 0.000877$.

---

#### PAR Chapter 1, Exercise 41 (p. 42)
**Source:** PAR Chapter 1, Exercise 41 (Printed p. 42, PDF p. 62).  
**Difficulty:** Medium Practice.  
**Relevant method:** [Problem Type PT-01](Study-Notes.md#problem-type-pt-01-multi-stage-sequential-selection-via-fpc), [Problem Type PT-06](Study-Notes.md#problem-type-pt-06-symmetry-subgroup-partitioning-and-card-hand-derivations).

**Question.**  
Judith and Kory each independently pick 1 coin from a collection containing a penny (1¢), a nickel (5¢), a dime (10¢), and a quarter (25¢). Let $J$ be the value of Judith's coin and $K$ be the value of Kory's coin. Define $X = \max(J, K)$.
- **Part (a):** List all outcomes in the sample space and write out the event $\{X = k\}$ for each possible value of $k \in \{1, 5, 10, 25\}$.
- **Part (b):** Compute $P(X = k)$ for each $k$.
- **Part (c):** What is the probability that Judith's coin is worth strictly more than Kory's? Explain why this is not $1/2$.

**Necessary work.**  
- The coin values are $C = \{1, 5, 10, 25\}$.
  Since selections are independent with replacement (each picks from their own complete set), the sample space consists of 16 equally likely ordered pairs $(J, K) \in C \times C$:
  $$|\Omega| = 4 \times 4 = 16$$
- **Part (a) and Part (b):**
  - For $X = 1$: $\max(J, K) = 1 \implies \{(1, 1)\}$.
    $$P(X = 1) = \frac{1}{16} = 0.0625$$
  - For $X = 5$: $\max(J, K) = 5 \implies \{(1, 5), (5, 1), (5, 5)\}$.
    $$P(X = 5) = \frac{3}{16} = 0.1875$$
  - For $X = 10$: $\max(J, K) = 10 \implies \{(1, 10), (5, 10), (10, 1), (10, 5), (10, 10)\}$.
    $$P(X = 10) = \frac{5}{16} = 0.3125$$
  - For $X = 25$: $\max(J, K) = 25 \implies$ any pair where at least one coin is 25:
    $$\{(1, 25), (5, 25), (10, 25), (25, 1), (25, 5), (25, 10), (25, 25)\} \quad (7 \text{ pairs})$$
    $$P(X = 25) = \frac{7}{16} = 0.4375$$
  *(Check: $1/16 + 3/16 + 5/16 + 7/16 = 16/16 = 1$.)*
- **Part (c): Probability Judith's coin is worth strictly more ($J > K$):**
  - By symmetry, $P(J > K) = P(K > J)$.
  - The sample space is partitioned into three disjoint events: $\{J > K\}$, $\{K > J\}$, and $\{J = K\}$ (ties).
  - Number of tie outcomes: $(1, 1), (5, 5), (10, 10), (25, 25) \implies 4$ outcomes.
  - Thus, $P(J = K) = \frac{4}{16} = \frac{1}{4}$.
  - The remaining $16 - 4 = 12$ outcomes are split equally between $J > K$ and $K > J$:
    $$P(J > K) = \frac{1 - P(J = K)}{2} = \frac{1 - 1/4}{2} = \frac{3}{8} = 0.375$$
  - It is not $1/2$ because ties have non-zero probability ($25\%$).

**Answer.**  
- (a) Listed above.
- (b) $P(X=1) = \frac{1}{16}$, $P(X=5) = \frac{3}{16}$, $P(X=10) = \frac{5}{16}$, $P(X=25) = \frac{7}{16}$.
- (c) $P(J > K) = \frac{3}{8} = 0.375$. It is strictly less than $1/2$ because ties occur with probability $1/4$.

---

#### PAR Chapter 1, Exercise 49 (p. 43)
**Source:** PAR Chapter 1, Exercise 49 (Printed p. 43, PDF p. 63).  
**Difficulty:** Medium Practice.  
**Relevant method:** [Problem Type PT-08](Study-Notes.md#problem-type-pt-08-generalized-principle-of-inclusion-exclusion-n-ge-3-events).

**Question.**  
An integer is selected uniformly at random from the set $\{1, 2, \dots, 5000\}$. Find the probability that the selected number is divisible by 4, 7, or 10.

**Necessary work.**  
Let $S = \{1, 2, \dots, 5000\}$, so $|S| = 5000$.  
Let $A_4, A_7, A_{10}$ be the events that the integer is divisible by 4, 7, and 10, respectively.
1. **Single event counts:**
   - $|A_4| = \lfloor 5000 / 4 \rfloor = 1250$.
   - $|A_7| = \lfloor 5000 / 7 \rfloor = 714$.
   - $|A_{10}| = \lfloor 5000 / 10 \rfloor = 500$.
   - $S_1 = 1250 + 714 + 500 = 2464$.
2. **Pairwise intersections (using LCM):**
   - $\text{lcm}(4, 7) = 28 \implies |A_4 \cap A_7| = \lfloor 5000 / 28 \rfloor = 178$.
   - $\text{lcm}(4, 10) = 20 \implies |A_4 \cap A_{10}| = \lfloor 5000 / 20 \rfloor = 250$.
   - $\text{lcm}(7, 10) = 70 \implies |A_7 \cap A_{10}| = \lfloor 5000 / 70 \rfloor = 71$.
   - $S_2 = 178 + 250 + 71 = 499$.
3. **Triple intersection:**
   - $\text{lcm}(4, 7, 10) = \text{lcm}(20, 7) = 140$.
   - $|A_4 \cap A_7 \cap A_{10}| = \lfloor 5000 / 140 \rfloor = 35$.
   - $S_3 = 35$.
4. **Apply Principle of Inclusion-Exclusion:**
   $$|A_4 \cup A_7 \cup A_{10}| = S_1 - S_2 + S_3 = 2464 - 499 + 35 = 2000$$
5. **Probability:**
   $$P(A_4 \cup A_7 \cup A_{10}) = \frac{2000}{5000} = \frac{2}{5} = 0.40$$

**Answer.**  
$P = \frac{2}{5} = 0.40$ ($40\%$).

---

### PAR — Test Level

#### PAR Chapter 1, Exercise 18 (p. 38) — Multi-Length License Plates
**Source:** PAR Chapter 1, Exercise 18 (Printed p. 38, PDF p. 58).  
**Difficulty:** Test Level.  
*(Designated by course instructors as high-level practice synthesizing multiple core counting principles).*  
**Relevant method:** [Problem Type PT-01](Study-Notes.md#problem-type-pt-01-multi-stage-sequential-selection-via-fpc), [Problem Type PT-07](Study-Notes.md#problem-type-pt-07-complementary-counting-and-collision-problems-birthday-paradox).

**Question.**  
A jurisdiction issues vanity license plates that can be 2, 3, 4, or 5 letters long, chosen from the 26 letters of the English alphabet ($\text{A–Z}$). Repetitions of letters are permitted. Suppose all valid license plates across all allowable lengths are equally likely to be assigned.
- **Part (a):** What is the probability that a randomly issued license plate is exactly “A-R-R”?
- **Part (b):** What is the probability that a randomly issued license plate is 4 letters long?
- **Part (c):** What is the probability that a randomly issued license plate is a palindrome (reads the same forwards and backwards)?
- **Part (d):** What is the probability that a randomly issued license plate has at least one “R”?

**Synthesized Counting Analysis & Necessary Work:**  
This problem requires synthesizing three distinct principles:
1. **The Addition Principle:** Partitioning the universe of all plates into disjoint sets defined by word length $L \in \{2, 3, 4, 5\}$.
2. **Structural Degrees of Freedom (Palindromes):** Recognizing that a palindrome of length $L$ is uniquely determined by its first $\lceil L/2 \rceil$ characters.
3. **Partitioned Complementary Counting:** Applying $n(\ge 1 \text{ R}) = n(\text{Total}) - n(\text{No R})$ across disparate lengths.

- **Total Sample Space Cardinality ($n(\Omega)$):**
  - Length 2: $26^2 = 676$
  - Length 3: $26^3 = 17,576$
  - Length 4: $26^4 = 456,976$
  - Length 5: $26^5 = 11,881,376$
  $$n(\Omega) = 676 + 17,576 + 456,976 + 11,881,376 = 12,356,604$$

- **Part (a): Plate is "A-R-R":**
  "A-R-R" is a single specific outcome in the 3-letter subspace.
  $$P(\text{"A-R-R"}) = \frac{1}{12,356,604} \approx 8.092838 \times 10^{-8}$$

- **Part (b): Plate is 4 letters long:**
  $$P(L = 4) = \frac{456,976}{12,356,604} = \frac{676}{18,279} \approx 0.03698233 \quad (3.70\%)$$

- **Part (c): Palindromes across all lengths:**
  - Length 2: Shape $a a$. 1 independent choice $\implies 26^1 = 26$.
  - Length 3: Shape $a b a$. 2 independent choices $\implies 26^2 = 676$.
  - Length 4: Shape $a b b a$. 2 independent choices $\implies 26^2 = 676$.
  - Length 5: Shape $a b c b a$. 3 independent choices $\implies 26^3 = 17,576$.
  Total palindromes:
  $$N_{\text{pal}} = 26 + 676 + 676 + 17,576 = 18,954$$
  $$P(\text{palindrome}) = \frac{18,954}{12,356,604} = \frac{27}{17,602} \approx 0.00153392 \quad (0.153\%)$$

- **Part (d): At least one "R":**
  Counting the complement: "Plates with NO 'R'". For each position, there are $26 - 1 = 25$ choices:
  - Length 2 without R: $25^2 = 625$
  - Length 3 without R: $25^3 = 15,625$
  - Length 4 without R: $25^4 = 390,625$
  - Length 5 without R: $25^5 = 9,765,625$
  Total without R:
  $$N(\text{no R}) = 625 + 15,625 + 390,625 + 9,765,625 = 10,172,500$$
  Favorable plates containing at least one R:
  $$N(\ge 1 \text{ R}) = 12,356,604 - 10,172,500 = 2,184,104$$
  $$P(\ge 1 \text{ R}) = \frac{2,184,104}{12,356,604} = \frac{42,002}{237,627} \approx 0.17675601 \quad (17.68\%)$$

**Answer.**  
- (a) $P = \frac{1}{12,356,604} \approx 8.093 \times 10^{-8}$.
- (b) $P = \frac{676}{18,279} \approx 0.03698$.
- (c) $P = \frac{27}{17,602} \approx 0.001534$.
- (d) $P = \frac{42,002}{237,627} \approx 0.1768$.

---

#### PAR Chapter 1, Exercise 22 (p. 39) — Shoe Pair Selection
**Source:** PAR Chapter 1, Exercise 22 (Printed p. 39, PDF p. 59).  
**Difficulty:** Test Level.  
**Relevant method:** [Problem Type PT-04](Study-Notes.md#problem-type-pt-04-unordered-combinations-and-combinatorial-identity-proofs), [Problem Type PT-05](Study-Notes.md#problem-type-pt-05-multi-category-hypergeometric-sampling).

**Question.**  
A closet contains 40 pairs of shoes (80 individual shoes total). Suppose 20 shoes are randomly chosen from the closet.
- **Part (a):** What is the chance that Bill’s favorite sneakers will be in the group?
- **Part (b):** What is the chance that at most one shoe from each of the 40 pairs will be picked?

**Necessary work.**  
Total possible selections of 20 shoes from 80:
$$|\Omega| = \binom{80}{20} = 3,535,316,142,212,174,320$$
- **Part (a): "Bill’s favorite sneakers"**:
  - *Standard Mathematical Interpretation (The Complete Pair):* "Sneakers" is plural, referring to the matching pair of 2 shoes.
    The sample must contain both the left and right sneaker of this specific pair ($\binom{2}{2} = 1$ way).
    The remaining $20 - 2 = 18$ shoes are chosen from the other $80 - 2 = 78$ shoes:
    $$N_{\text{pair}} = \binom{2}{2} \binom{78}{18} = \binom{78}{18}$$
    $$P(\text{both sneakers}) = \frac{\binom{78}{18}}{\binom{80}{20}} = \frac{\frac{78!}{18!60!}}{\frac{80!}{20!60!}} = \frac{20 \times 19}{80 \times 79} = \frac{380}{6,320} = \frac{19}{316} \approx 0.06012658 \quad (6.01\%)$$
  - *Alternative Interpretations (for complete clarity):*
    - If interpreted as "at least one of Bill's favorite sneakers":
      $$P(\ge 1) = 1 - \frac{\binom{78}{20}}{\binom{80}{20}} = 1 - \frac{60 \times 59}{80 \times 79} = 1 - \frac{3,540}{6,320} = \frac{2,780}{6,320} = \frac{139}{316} \approx 0.439873 \quad (43.99\%)$$
    - If interpreted as "exactly one sneaker":
      $$P(\text{exactly 1}) = \frac{\binom{2}{1}\binom{78}{19}}{\binom{80}{20}} = \frac{2 \times 20 \times 60}{80 \times 79} = \frac{2,400}{6,320} = \frac{30}{79} \approx 0.379747$$
- **Part (b): At most one shoe from each pair:**
  - Choosing 20 shoes such that no two belong to the same pair means we must select exactly 20 distinct pairs out of the 40 pairs ($\binom{40}{20}$ ways).
  - From each of the 20 chosen pairs, we must pick exactly 1 shoe (either the left or right shoe, $2^1 = 2$ choices per pair): $2^{20}$ ways.
  - Total favorable outcomes $= \binom{40}{20} \times 2^{20}$.
  - Probability:
    $$P(\text{no pairs}) = \frac{\binom{40}{20} 2^{20}}{\binom{80}{20}} = \frac{137,846,528,820 \times 1,048,576}{3,535,316,142,212,174,320} = \frac{68,419,584}{1,673,450,759} \approx 0.04088533 \quad (4.09\%)$$

**Answer.**  
- (a) $P(\text{both sneakers}) = \frac{19}{316} \approx 0.0601$ ($6.01\%$). (At least one sneaker: $\frac{139}{316} \approx 0.4399$).
- (b) $P = \frac{\binom{40}{20} 2^{20}}{\binom{80}{20}} = \frac{68,419,584}{1,673,450,759} \approx 0.04089$ ($4.09\%$).

---

#### PAR Chapter 1, Exercise 23 (p. 39) — Bridge Hand Distributional Symmetries
**Source:** PAR Chapter 1, Exercise 23 (Printed p. 39, PDF p. 59).  
**Difficulty:** Test Level.  
*(Designated by course instructors as high-level practice synthesizing multiple core counting principles).*  
**Relevant method:** [Problem Type PT-06](Study-Notes.md#problem-type-pt-06-symmetry-subgroup-partitioning-and-card-hand-derivations).

**Question.**  
A bridge hand consists of 13 cards dealt from a standard 52-card deck ($|\Omega| = \binom{52}{13} = 635,013,559,600$). The suit distribution describes the number of cards in each of the four suits, written in descending order (e.g., 4-3-3-3 means 4 cards of one suit, 3 of another, 3 of a third, and 3 of the fourth).
- **Part (a):** Show that a 4-4-3-2 distribution is more likely than a 4-3-3-3 distribution.
- **Part (b):** Find the other three suit distributions that are more likely than a 4-3-3-3 distribution.

**Synthesized Counting Analysis & Necessary Work:**  
This problem reveals a celebrated counter-intuitive property of combinatorial probability: **multi-set partition symmetry**.  
To count hands with suit shape $(s_1, s_2, s_3, s_4)$ with $\sum s_i = 13$:
1. We must assign the 4 suits ($\spadesuit, \heartsuit, \diamondsuit, \clubsuit$) to the four integer counts $s_1, s_2, s_3, s_4$.
2. The number of ways to assign suits depends on the **distinctness of the counts**:
   $$\text{Suit permutations} = \frac{4!}{m_1! \, m_2! \dots}$$
   where $m_i$ is the number of times a suit length is repeated in the pattern!
3. For each assigned suit, we choose the specific cards from the 13 available in that suit: $\prod_{i=1}^4 \binom{13}{s_i}$.

- **Evaluation of 4-3-3-3:**
  - Suit counts have one 4 and three 3s ($m_4 = 1, m_3 = 3$).
  - Permutations of suits $= \frac{4!}{1! \, 3!} = 4$.
  - Card selections $= \binom{13}{4} \binom{13}{3}^3 = 715 \times 286^3 = 715 \times 23,393,656 = 16,726,464,040$.
  - Total hands $= 4 \times 16,726,464,040 = 66,905,856,160$.
  - Probability:
    $$P(4\text{-}3\text{-}3\text{-}3) = \frac{66,905,856,160}{635,013,559,600} \approx 0.105361 \quad (10.54\%)$$

- **Part (a): Evaluation of 4-4-3-2:**
  - Suit counts have two 4s, one 3, one 2 ($m_4 = 2, m_3 = 1, m_2 = 1$).
  - Permutations of suits $= \frac{4!}{2! \, 1! \, 1!} = 12$.
  - Card selections $= \binom{13}{4}^2 \binom{13}{3} \binom{13}{2} = 715^2 \times 286 \times 78 = 511,225 \times 22,308 = 11,404,407,300$.
  - Total hands $= 12 \times 11,404,407,300 = 136,852,887,600$.
  - Probability:
    $$P(4\text{-}4\text{-}3\text{-}2) = \frac{136,852,887,600}{635,013,559,600} \approx 0.215512 \quad (21.55\%)$$
  - **Comparison:** $136,852,887,600 > 66,905,856,160$. In fact, 4-4-3-2 is more than **twice as likely** as 4-3-3-3! Even though the card combinations for 4-3-3-3 are slightly higher, 4-4-3-2 has **3 times as many suit permutations** ($12$ vs $4$).

- **Part (b): Three other distributions more likely than 4-3-3-3:**
  Let us compute the total hands for candidate partitions of 13:
  1. **5-3-3-2:**
     - Suit permutations: $\frac{4!}{1! \, 2! \, 1!} = 12$.
     - Card selections: $\binom{13}{5} \binom{13}{3}^2 \binom{13}{2} = 1,287 \times 286^2 \times 78 = 8,211,173,256$.
     - Total $= 12 \times 8,211,173,256 = \mathbf{98,534,079,072} \implies P \approx 15.52\%$.
     - Since $98.53\text{B} > 66.91\text{B}$, 5-3-3-2 is more likely.
  2. **5-4-3-1:**
     - All 4 suit lengths are distinct ($m_i = 1$ for all $i$).
     - Suit permutations: $4! = 24$.
     - Card selections: $\binom{13}{5} \binom{13}{4} \binom{13}{3} \binom{13}{1} = 1,287 \times 715 \times 286 \times 13 = 3,421,322,190$.
     - Total $= 24 \times 3,421,322,190 = \mathbf{82,111,732,560} \implies P \approx 12.93\%$.
     - Since $82.11\text{B} > 66.91\text{B}$, 5-4-3-1 is more likely.
  3. **5-4-2-2:**
     - Suit counts have two 2s: $\frac{4!}{1! \, 1! \, 2!} = 12$.
     - Card selections: $\binom{13}{5} \binom{13}{4} \binom{13}{2}^2 = 1,287 \times 715 \times 78^2 = 5,598,527,220$.
     - Total $= 12 \times 5,598,527,220 = \mathbf{67,182,326,640} \implies P \approx 10.58\%$.
     - Since $67.18\text{B} > 66.91\text{B}$, 5-4-2-2 is more likely.

- **Ranking of Top 5 Bridge Distributions:**
  1. **4-4-3-2**: $21.55\%$ ($136.85$ billion hands)
  2. **5-3-3-2**: $15.52\%$ ($98.53$ billion hands)
  3. **5-4-3-1**: $12.93\%$ ($82.11$ billion hands)
  4. **5-4-2-2**: $10.58\%$ ($67.18$ billion hands)
  5. **4-3-3-3**: $10.54\%$ ($66.91$ billion hands)

**Answer.**  
- (a) $P(4\text{-}4\text{-}3\text{-}2) \approx 21.55\%$ while $P(4\text{-}3\text{-}3\text{-}3) \approx 10.54\%$.
- (b) The three other patterns more likely than 4-3-3-3 are **5-3-3-2** ($15.52\%$), **5-4-3-1** ($12.93\%$), and **5-4-2-2** ($10.58\%$).

---

#### PAR Chapter 1, Exercise 24 (p. 39) — Bridge Hands with a Nine-Card Suit
**Source:** PAR Chapter 1, Exercise 24 (Printed p. 39, PDF p. 59).  
**Difficulty:** Test Level.  
**Relevant method:** [Problem Type PT-05](Study-Notes.md#problem-type-pt-05-multi-category-hypergeometric-sampling), [Problem Type PT-06](Study-Notes.md#problem-type-pt-06-symmetry-subgroup-partitioning-and-card-hand-derivations).

**Question.**  
Find the probability that a randomly dealt bridge hand (13 cards) contains a nine-card suit.

**Necessary work.**  
- Notice that a bridge hand can contain at most **one** suit with 9 or more cards, because $9 + 9 = 18 > 13$. Thus, the events $\{ \text{9-card suit is spades} \}$, $\{ \text{9-card suit is hearts} \}$, etc., are pairwise disjoint.
- To form a hand with a 9-card suit:
  1. Select which of the 4 suits contains exactly 9 cards: $\binom{4}{1} = 4$ ways.
  2. Select 9 cards from that chosen suit: $\binom{13}{9} = \binom{13}{4} = 715$ ways.
  3. The remaining $13 - 9 = 4$ cards must be selected from the other 3 suits ($52 - 13 = 39$ cards): $\binom{39}{4}$ ways.
  $$\binom{39}{4} = \frac{39 \times 38 \times 37 \times 36}{24} = 82,251$$
- Total favorable hands:
  $$N = 4 \times 715 \times 82,251 = 235,237,860$$
- Probability:
  $$P(\text{9-card suit}) = \frac{235,237,860}{\binom{52}{13}} = \frac{235,237,860}{635,013,559,600} = \frac{11,761,893}{31,750,677,980} \approx 0.0003704454$$
  This represents roughly 1 in every 2,699 hands ($0.037\%$).

**Answer.**  
$P = \frac{11,761,893}{31,750,677,980} \approx 0.0003704$ ($0.037\%$).

---

#### PAR Chapter 1, Exercise 25 (p. 39) — Non-Attacking Rooks / Independent Placements on a Chessboard
**Source:** PAR Chapter 1, Exercise 25 (Printed p. 39, PDF p. 59).  
**Difficulty:** Test Level.  
**Relevant method:** [Problem Type PT-01](Study-Notes.md#problem-type-pt-01-multi-stage-sequential-selection-via-fpc), [Problem Type PT-04](Study-Notes.md#problem-type-pt-04-unordered-combinations-and-combinatorial-identity-proofs).

**Question.**  
Suppose 8 identical chess pieces are placed at random on an $8 \times 8$ chessboard, with at most one piece per square. What is the probability that there is exactly one piece in each row and each column?

**Necessary work.**  
- **Total Configurations:** The chessboard has $8 \times 8 = 64$ squares. We choose 8 distinct squares out of 64 without replacement:
  $$|\Omega| = \binom{64}{8} = 4,426,165,368$$
- **Favorable Configurations:**
  - For the condition "exactly one piece in each row and each column" to hold, Row 1 must have 1 piece, Row 2 must have 1 piece, ..., Row 8 must have 1 piece.
  - In Row 1, the piece can be placed in any of the 8 columns ($8$ choices).
  - In Row 2, the piece can be placed in any column except the column used in Row 1 ($7$ choices).
  - In Row 3, $6$ choices.
  - Continuing down to Row 8:
    $$N_{\text{fav}} = 8 \times 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 8! = 40,320$$
- **Probability:**
  $$P = \frac{8!}{\binom{64}{8}} = \frac{40,320}{4,426,165,368} = \frac{560}{61,474,519} \approx 9.109465 \times 10^{-6}$$
  This is approximately 1 in 109,776.

**Answer.**  
$P = \frac{560}{61,474,519} \approx 9.109 \times 10^{-6}$ ($0.000911\%$).

---

#### PAR Chapter 1, Exercise 26 (pp. 39–40) — Exhaustive Hierarchy of 5-Card Poker Hands
**Source:** PAR Chapter 1, Exercise 26 (Printed pp. 39–40, PDF pp. 59–60).  
**Difficulty:** Test Level.  
*(Designated by course instructors as high-level practice synthesizing multiple core counting principles).*  
**Relevant method:** [Problem Type PT-05](Study-Notes.md#problem-type-pt-05-multi-category-hypergeometric-sampling), [Problem Type PT-06](Study-Notes.md#problem-type-pt-06-symmetry-subgroup-partitioning-and-card-hand-derivations).

**Question.**  
Consider a standard 5-card poker game dealt from a 52-card deck ($|\Omega| = \binom{52}{5} = 2,598,960$). Compute the exact number of hands and probabilities for each of the following hand types, ordered from rarest to most common:
- **Part (a):** Straight flush
- **Part (b):** Four of a kind
- **Part (c):** Full house
- **Part (d):** Flush (excluding straight flushes)
- **Part (e):** Straight (excluding straight flushes)
- **Part (f):** Three of a kind (excluding full house and four of a kind)
- **Part (g):** Two pair (excluding four of a kind and full house)
- **Part (h):** One pair (excluding all higher-ranking hands)

**Synthesized Counting Analysis & Necessary Work:**  
All 5-card poker hands partition into disjoint sets. Hand classifications must strictly exclude superior combinations:
- **(a) Straight Flush:**
  A straight can begin with Ace ($A\text{--}5$), $2, 3, \dots, 10$ ($10\text{--}A$). Total starting ranks $= 10$.
  All 5 cards must be of the same suit ($4$ suits).
  $$N_{\text{SF}} = 10 \times 4 = 40$$
  $$P(\text{SF}) = \frac{40}{2,598,960} = \frac{1}{64,974} \approx 1.539077 \times 10^{-5}$$

- **(b) Four of a Kind:**
  Select rank of quad: $\binom{13}{1} = 13$. All 4 suits: $\binom{4}{4} = 1$.
  Kicker chosen from remaining 48 cards: $\binom{48}{1} = 48$.
  $$N_{\text{4K}} = 13 \times 1 \times 48 = 624$$
  $$P(\text{4K}) = \frac{624}{2,598,960} = \frac{1}{4,165} \approx 0.000240096$$

- **(c) Full House:**
  Rank of triple ($13$ choices), suits of triple ($\binom{4}{3} = 4$).
  Rank of pair ($12$ choices), suits of pair ($\binom{4}{2} = 6$).
  $$N_{\text{FH}} = 13 \times 4 \times 12 \times 6 = 3,744$$
  $$P(\text{FH}) = \frac{3,744}{2,598,960} = \frac{6}{4,165} \approx 0.001440576$$

- **(d) Flush (Strictly excluding Straight Flush):**
  Choose suit: $\binom{4}{1} = 4$. Choose 5 ranks in that suit: $\binom{13}{5} = 1,287$.
  Unrestricted flushes $= 4 \times 1,287 = 5,148$.
  Subtract the 40 straight flushes:
  $$N_{\text{Flush}} = 5,148 - 40 = 5,108$$
  $$P(\text{Flush}) = \frac{5,108}{2,598,960} = \frac{1,277}{649,740} \approx 0.001965402$$

- **(e) Straight (Strictly excluding Straight Flush):**
  10 sequences of 5 consecutive ranks. Each card can be any of the 4 suits: $4^5 = 1,024$.
  Unrestricted straights $= 10 \times 1,024 = 10,240$.
  Subtract the 40 straight flushes:
  $$N_{\text{Straight}} = 10,240 - 40 = 10,200$$
  $$P(\text{Straight}) = \frac{10,200}{2,598,960} = \frac{5}{1,274} \approx 0.003924647$$

- **(f) Three of a Kind (Strictly excluding Full House and Four of a Kind):**
  Choose rank of triple: $\binom{13}{1} = 13$. Choose suits of triple: $\binom{4}{3} = 4$.
  Choose 2 distinct ranks for kickers: $\binom{12}{2} = 66$.
  Choose suit for each kicker: $4 \times 4 = 16$.
  $$N_{\text{3K}} = 13 \times 4 \times 66 \times 16 = 54,912$$
  $$P(\text{3K}) = \frac{54,912}{2,598,960} = \frac{88}{4,165} \approx 0.021128451$$

- **(g) Two Pair:**
  Choose 2 ranks for the pairs: $\binom{13}{2} = 78$.
  Choose suits for both pairs: $\binom{4}{2} \times \binom{4}{2} = 36$.
  Choose rank for kicker: $\binom{11}{1} = 11$. Choose suit for kicker: $\binom{4}{1} = 4$.
  $$N_{\text{2P}} = 78 \times 36 \times 11 \times 4 = 123,552$$
  $$P(\text{2P}) = \frac{123,552}{2,598,960} = \frac{198}{4,165} \approx 0.047539016$$

- **(h) One Pair (Strictly excluding higher hands):**
  Choose 1 rank for the pair: $\binom{13}{1} = 13$. Choose 2 suits: $\binom{4}{2} = 6$.
  Choose 3 distinct kicker ranks: $\binom{12}{3} = 220$.
  Choose suit for each of the 3 kickers: $4^3 = 64$.
  $$N_{\text{1P}} = 13 \times 6 \times 220 \times 64 = 1,098,240$$
  $$P(\text{1P}) = \frac{1,098,240}{2,598,960} = \frac{352}{833} \approx 0.422569028$$

- **Hierarchy Summary Table:**

| Hand Type | Count $n(A)$ | Exact Fraction $P(A)$ | Decimal Probability | Percentage |
| :--- | :---: | :---: | :---: | :---: |
| **Straight Flush** | $40$ | $\frac{1}{64,974}$ | $0.00001539$ | $0.0015\%$ |
| **Four of a Kind** | $624$ | $\frac{1}{4,165}$ | $0.00024010$ | $0.0240\%$ |
| **Full House** | $3,744$ | $\frac{6}{4,165}$ | $0.00144058$ | $0.1441\%$ |
| **Flush** | $5,108$ | $\frac{1,277}{649,740}$ | $0.00196540$ | $0.1965\%$ |
| **Straight** | $10,200$ | $\frac{5}{1,274}$ | $0.00392465$ | $0.3925\%$ |
| **Three of a Kind** | $54,912$ | $\frac{88}{4,165}$ | $0.02112845$ | $2.1128\%$ |
| **Two Pair** | $123,552$ | $\frac{198}{4,165}$ | $0.04753902$ | $4.7539\%$ |
| **One Pair** | $1,098,240$ | $\frac{352}{833}$ | $0.42256903$ | $42.2569\%$ |
| **High Card (Remaining)** | $1,302,540$ | $\frac{1,277}{2,548}$ | $0.50117739$ | $50.1177\%$ |
| **Total** | **2,598,960** | **1** | **1.00000000** | **100.00%** |

**Answer.**  
Exact counts and probabilities verified as shown in the table above.

---

#### PAR Chapter 1, Exercise 29 (p. 40) — Combinatorial Proof of Subset Symmetry
**Source:** PAR Chapter 1, Exercise 29 (Printed p. 40, PDF p. 60).  
**Difficulty:** Test Level.  
**Relevant method:** [Problem Type PT-04](Study-Notes.md#problem-type-pt-04-unordered-combinations-and-combinatorial-identity-proofs).

**Question.**  
Give a combinatorial argument (not an algebraic manipulation of factorials) explaining why $\binom{n}{k} = \binom{n}{n-k}$.

**Necessary work.**  
- **Definition of Terms:** $\binom{n}{k}$ denotes the number of distinct subsets of size $k$ that can be chosen from a set $S$ containing $n$ elements. $\binom{n}{n-k}$ denotes the number of distinct subsets of size $n-k$ that can be chosen from $S$.
- **Combinatorial Correspondence:**
  - Suppose you are selecting a team of $k$ players from a squad of $n$ available athletes.
  - Deciding which $k$ athletes are on the team is mathematically and operationally identical to deciding which $n-k$ athletes are left on the bench.
  - Formally, define a mapping $f: \mathcal{P}_k(S) \to \mathcal{P}_{n-k}(S)$ by $f(A) = S \setminus A$.
  - For every unique subset $A$ of size $k$, its complement $S \setminus A$ is a unique subset of size $n-k$.
  - This mapping is a bijection: it is one-to-one (distinct teams leave distinct sets of bench players) and onto (any set of $n-k$ bench players uniquely specifies a team of $k$ players).
  - Because a bijection preserves set size, the number of ways to choose $k$ items must equal the number of ways to choose $n-k$ items:
    $$\binom{n}{k} = \binom{n}{n-k} \quad \blacksquare$$

**Answer.**  
Every selection of $k$ items to include creates an exact, unique complement of $n-k$ items to exclude, establishing a bijection between the collection of $k$-subsets and $(n-k)$-subsets.

---

## Section D: Original Self-Test Questions

---

### Question ST-01 (Focus: PT-01 — Multi-Stage FPC with Constraints)
An online banking portal generates temporary passwords of length 7. Each character must be chosen from the set of 26 lowercase English letters and the 10 decimal digits ($0\text{--}9$).
1. How many passwords can be formed if characters can be repeated, but the first character must be a consonant (non-vowel letter, where vowels are $a, e, i, o, u$), and the last character must be an odd digit?
2. How many passwords can be formed if **no characters can be repeated**, the password must contain exactly 4 letters followed by 3 digits, and the digits must form a strictly increasing sequence?

---

### Question ST-02 (Focus: PT-02 — Linear Permutations with Block and Gap Constraints)
Five computer science professors, four mathematics professors, and two statistics professors are to be seated in a row of 11 auditorium seats.
1. In how many ways can they be seated if all two statistics professors must sit together, and all four mathematics professors must sit together?
2. In how many ways can they be seated if the two statistics professors must NOT sit next to each other?
3. If the seating is assigned completely at random, what is the probability that the two statistics professors sit at the two outermost ends of the row?

---

### Question ST-03 (Focus: PT-03 — Multinomial Permutations of Digits with Numerical Thresholds)
Consider the multiset of digits $\mathcal{M} = \{1, 1, 3, 3, 3, 6, 8\}$.
1. How many distinct 7-digit numbers can be formed using all seven digits?
2. How many of these 7-digit numbers are strictly greater than $3,000,000$?
3. How many of these 7-digit numbers are both strictly greater than $3,000,000$ and divisible by 2?

---

### Question ST-04 (Focus: PT-04 — Combinatorial Identity by Double Counting)
Let $n \ge 2$.
1. Explain by a combinatorial argument (counting the same set in two ways) why:
   $$\sum_{k=1}^n k \binom{n}{k} = n 2^{n-1}$$
   *(Hint: Consider selecting a committee of any size $k \ge 1$ from $n$ people, with one designated president).*
2. Using the identity above, evaluate the sum $\sum_{k=1}^{10} k \binom{10}{k}$.

---

### Question ST-05 (Focus: PT-05 — Multivariate Hypergeometric Quality Inspection)
A pharmaceutical warehouse receives a batch of 40 vaccine vials: 24 are fully potent, 12 have minor degradation, and 4 are completely inactive. An inspector randomly selects 5 vials without replacement for destructive testing.
1. What is the total number of possible 5-vial inspection samples?
2. What is the probability that the sample contains exactly 3 fully potent vials, 1 degraded vial, and 1 inactive vial?
3. What is the probability that the sample contains at least one completely inactive vial?

---

### Question ST-06 (Focus: PT-06 — Symmetry in Poker / Dice Partitioning)
Suppose you roll five fair 6-sided dice simultaneously.
1. How many outcomes result in a "Full House" (three dice of one value and two dice of a different value)?
2. How many outcomes result in "Two Pair" (two dice of one value, two dice of a second value, and one die of a third value)?
3. Explain mathematically why the number of dice values chosen for the pairs in Two Pair uses $\binom{6}{2}$, whereas the dice values chosen for Full House uses $6 \times 5$.

---

### Question ST-07 (Focus: PT-07 — Hash Collisions and the Birthday Principle)
A network switch assigns incoming IP packets to one of $M = 365$ output queues uniformly at random.
1. What is the probability that among 15 packets, at least two are routed to the same queue?
2. What is the smallest number of packets $k$ such that the probability of at least one queue collision exceeds $90\%$? (Use the exponential approximation $1 - e^{-k(k-1)/(2M)} \ge 0.90$).

---

### Question ST-08 (Focus: PT-08 — Three-Event Inclusion-Exclusion)
In a class of 120 engineering students:
- 60 take Python ($P$)
- 50 take Calculus ($C$)
- 45 take Physics ($H$)
- 25 take both Python and Calculus
- 20 take both Python and Physics
- 15 take both Calculus and Physics
- 10 take all three courses.
1. What is the probability that a randomly chosen student takes at least one of the three courses?
2. What is the probability that a randomly chosen student takes **none** of these courses?
3. What is the probability that a randomly chosen student takes **exactly two** of these courses?

---

### Question ST-09 (Focus: PT-09 — R Monte Carlo Simulation and Sample Size Planning)
We want to estimate the probability of rolling a sum of 10 or greater when rolling three fair 6-sided dice.
1. Write an R script using `replicate()` and `sample()` to run $N = 100,000$ iterations and estimate this probability.
2. What is the exact theoretical probability of rolling a sum of at least 10?
3. How many simulation trials $N$ are needed so that the Monte Carlo margin of error is at most $\pm 0.001$ with 95% confidence?

---

## Section E: Self-Test Answers

---

### Answer to Question ST-01
**Reference:** [Problem Type PT-01](Study-Notes.md#problem-type-pt-01-multi-stage-sequential-selection-via-fpc)
1. Alphabet: 26 letters (5 vowels, 21 consonants) and 10 digits (5 odd: $1, 3, 5, 7, 9$).
   - Slot 1: 21 choices (consonant).
   - Slot 7: 5 choices (odd digit).
   - Slots 2, 3, 4, 5, 6: 36 choices each (any alphanumeric).
   $$N = 21 \times 36^5 \times 5 = 105 \times 60,466,176 = \mathbf{6,348,948,480}$$
2. 4 letters followed by 3 digits without repetition, where the digits must be in increasing order:
   - Selecting and arranging the 4 distinct letters: $P(26, 4) = 26 \times 25 \times 24 \times 23 = 358,800$.
   - For the 3 digits, any choice of 3 distinct digits from 10 has **exactly one** strictly increasing order:
     $$\binom{10}{3} \times 1 = \frac{10 \times 9 \times 8}{6} = 120$$
   - By FPC:
     $$N = 358,800 \times 120 = \mathbf{43,056,000}$$

---

### Answer to Question ST-02
**Reference:** [Problem Type PT-02](Study-Notes.md#problem-type-pt-02-ordered-permutations-of-distinct-objects-under-positional-constraints)
1. Two statistics professors form block $[S]$, four math professors form block $[M]$.
   - Entities to arrange: $[S]$, $[M]$, and 5 individual CS professors $\implies 1 + 1 + 5 = 7$ entities.
   - Total arrangements $= 7! \times 2! \times 4! = 5,040 \times 2 \times 24 = \mathbf{241,920}$.
2. Statistics professors must not sit together:
   - Arrange the other 9 professors (5 CS + 4 Math): $9! = 362,880$.
   - This creates 10 gaps ($\_ P_1 \_ P_2 \dots P_9 \_$).
   - Place 2 statistics professors into 10 gaps: $P(10, 2) = 10 \times 9 = 90$.
   - Total $= 9! \times 90 = 362,880 \times 90 = \mathbf{32,659,200}$.
3. Statistics professors at opposite ends:
   - Seat 1 and Seat 11 can be filled by the 2 statistics professors in $2! = 2$ ways.
   - The remaining 9 middle seats are filled by the other 9 professors in $9! = 362,880$ ways.
   - Favorable $= 2 \times 9!$. Total $= 11!$.
   - $$P = \frac{2 \times 9!}{11!} = \frac{2}{11 \times 10} = \frac{2}{110} = \frac{\mathbf{1}}{\mathbf{55}} \approx \mathbf{0.01818} \quad (1.82\%)$$

---

### Answer to Question ST-03
**Reference:** [Problem Type PT-03](Study-Notes.md#problem-type-pt-03-permutations-with-indistinguishable-objects-and-digit-formation)
1. Multiset: two 1s, three 3s, one 6, one 8 ($n=7$).
   $$N_{\text{total}} = \frac{7!}{2! \, 3! \, 1! \, 1!} = \frac{5,040}{2 \times 6} = \mathbf{420}$$
2. Strictly greater than $3,000,000$: First digit must be 3, 6, or 8.
   - First digit is 3: remaining digits $\{1, 1, 3, 3, 6, 8\} \implies \frac{6!}{2! \, 2! \, 1! \, 1!} = \frac{720}{4} = 180$.
   - First digit is 6: remaining digits $\{1, 1, 3, 3, 3, 8\} \implies \frac{6!}{2! \, 3! \, 1!} = \frac{720}{12} = 60$.
   - First digit is 8: remaining digits $\{1, 1, 3, 3, 3, 6\} \implies \frac{6!}{2! \, 3! \, 1!} = 60$.
   - Total $= 180 + 60 + 60 = \mathbf{300}$.
3. Greater than $3,000,000$ and even:
   - Must end in 6 or 8 (the only even digits in the multiset).
   - *Case 1: Ends in 6.*
     - First digit is 3: remaining $\{1, 1, 3, 3, 8\} \implies \frac{5!}{2! \, 2!} = 30$.
     - First digit is 8: remaining $\{1, 1, 3, 3, 3\} \implies \frac{5!}{2! \, 3!} = 10$.
     - Subtotal $= 30 + 10 = 40$.
   - *Case 2: Ends in 8.*
     - First digit is 3: remaining $\{1, 1, 3, 3, 6\} \implies \frac{5!}{2! \, 2!} = 30$.
     - First digit is 6: remaining $\{1, 1, 3, 3, 3\} \implies \frac{5!}{2! \, 3!} = 10$.
     - Subtotal $= 30 + 10 = 40$.
   - Total $= 40 + 40 = \mathbf{80}$.

---

### Answer to Question ST-04
**Reference:** [Problem Type PT-04](Study-Notes.md#problem-type-pt-04-unordered-combinations-and-combinatorial-identity-proofs)
1. **Combinatorial Proof:**
   - Consider choosing a committee of any size $k \in \{1, 2, \dots, n\}$ from $n$ individuals, with one member designated as president.
   - **Method A:** For a fixed committee size $k$, choose the committee in $\binom{n}{k}$ ways, then choose 1 of the $k$ members to be president in $k$ ways. Summing over all possible sizes $k=1, \dots, n$ gives:
     $$\sum_{k=1}^n k \binom{n}{k}$$
   - **Method B:** Choose the president first from the $n$ candidates in $n$ ways. For each of the remaining $n-1$ candidates, decide independently whether they are on the committee or not ($2^{n-1}$ choices). By FPC, this gives $n 2^{n-1}$ ways.
   - Since both methods count the identical set of chaired committees:
     $$\sum_{k=1}^n k \binom{n}{k} = n 2^{n-1} \quad \blacksquare$$
2. For $n = 10$:
   $$\sum_{k=1}^{10} k \binom{10}{k} = 10 \cdot 2^{10 - 1} = 10 \cdot 2^9 = 10 \times 512 = \mathbf{5,120}$$

---

### Answer to Question ST-05
**Reference:** [Problem Type PT-05](Study-Notes.md#problem-type-pt-05-multi-category-hypergeometric-sampling), [Problem Type PT-07](Study-Notes.md#problem-type-pt-07-complementary-counting-and-collision-problems-birthday-paradox)
1. Total samples:
   $$|\Omega| = \binom{40}{5} = \frac{40 \times 39 \times 38 \times 37 \times 36}{120} = \mathbf{658,008}$$
2. Exactly 3 potent, 1 degraded, 1 inactive:
   $$N = \binom{24}{3} \binom{12}{1} \binom{4}{1} = 2,024 \times 12 \times 4 = \mathbf{97,152}$$
   $$P = \frac{97,152}{658,008} = \frac{4,048}{27,417} \approx \mathbf{0.147644} \quad (14.76\%)$$
3. At least one inactive vial:
   - Complement: All 5 vials chosen from the $24 + 12 = 36$ active/degraded vials:
     $$N(\text{no inactive}) = \binom{36}{5} = 376,992$$
   - $$P(\ge 1 \text{ inactive}) = 1 - \frac{\binom{36}{5}}{\binom{40}{5}} = 1 - \frac{376,992}{658,008} = \frac{281,016}{658,008} = \frac{3,903}{9,139} \approx \mathbf{0.427071} \quad (42.71\%)$$

---

### Answer to Question ST-06
**Reference:** [Problem Type PT-06](Study-Notes.md#problem-type-pt-06-symmetry-subgroup-partitioning-and-card-hand-derivations)
Total outcomes in rolling 5 dice $= 6^5 = 7,776$.
1. **Full House (3 of one value, 2 of another):**
   - Choose value for triple: 6 choices.
   - Choose value for pair: 5 choices.
   - Choose which 3 of the 5 dice show the triple value: $\binom{5}{3} = 10$.
   - Total $= 6 \times 5 \times 10 = \mathbf{300}$.
2. **Two Pair (2 of value 1, 2 of value 2, 1 of value 3):**
   - Choose 2 values for the pairs from 6: $\binom{6}{2} = 15$.
   - Choose 1 value for the single die from the remaining 4: $\binom{4}{1} = 4$.
   - Assign the 5 dice to these values: $\frac{5!}{2! \, 2! \, 1!} = \frac{120}{4} = 30$.
   - Total $= 15 \times 4 \times 30 = \mathbf{1,800}$.
3. **Mathematical Explanation:**
   In Two Pair, both pairs have the identical size of 2 dice. Assigning values $\{2, 5\}$ results in two 2s and two 5s; ordering the values as $(2, 5)$ or $(5, 2)$ produces the exact same collection of dice values. Thus, an unordered choice $\binom{6}{2}$ is required. In contrast, Full House has asymmetric sizes (3 vs 2). Three 2s and two 5s is distinct from three 5s and two 2s; hence an ordered assignment $P(6, 2) = 6 \times 5 = 30$ is required.

---

### Answer to Question ST-07
**Reference:** [Problem Type PT-07](Study-Notes.md#problem-type-pt-07-complementary-counting-and-collision-problems-birthday-paradox)
1. Probability of no collision:
   $$P(\text{no collision}) = \frac{P(365, 15)}{365^{15}} = \prod_{j=0}^{14} \left(1 - \frac{j}{365}\right) \approx 0.7470876$$
   $$P(\text{at least one collision}) = 1 - 0.7470876 = \mathbf{0.252912} \quad (25.29\%)$$
2. Finding $k$ for $P(\text{collision}) \ge 0.90$:
   $$1 - e^{-\frac{k(k-1)}{2(365)}} \ge 0.90 \iff e^{-\frac{k(k-1)}{730}} \le 0.10 \iff \frac{k(k-1)}{730} \ge \ln(10) \approx 2.302585$$
   $$k(k-1) \ge 730 \times 2.302585 \approx 1680.89$$
   Solving $k^2 - k - 1680.89 \ge 0$:
   $$k \approx \frac{1 + \sqrt{1 + 4(1680.89)}}{2} = \frac{1 + \sqrt{6724.56}}{2} \approx \frac{1 + 82.003}{2} \approx 41.5$$
   Rounding up to the nearest integer gives $k = 42$ packets. (Exact calculation: $P(41) \approx 0.897$, $P(42) \approx 0.908$).
   Thus, $k^* = \mathbf{42}$ packets.

---

### Answer to Question ST-08
**Reference:** [Problem Type PT-08](Study-Notes.md#problem-type-pt-08-generalized-principle-of-inclusion-exclusion-n-ge-3-events)
1. By 3-event Inclusion-Exclusion:
   $$|P \cup C \cup H| = (60 + 50 + 45) - (25 + 20 + 15) + 10 = 155 - 60 + 10 = 105$$
   $$P(P \cup C \cup H) = \frac{105}{120} = \frac{7}{8} = \mathbf{0.875} \quad (87.5\%)$$
2. By the Complement Rule:
   $$P(\text{none}) = 1 - P(P \cup C \cup H) = 1 - \frac{7}{8} = \frac{\mathbf{1}}{\mathbf{8}} = \mathbf{0.125} \quad (12.5\%)$$
3. Number of students taking **exactly two** courses:
   Each pairwise overlap includes the triple overlap of 10 students:
   - Exactly Python & Calculus $= |P \cap C| - |P \cap C \cap H| = 25 - 10 = 15$.
   - Exactly Python & Physics $= |P \cap H| - |P \cap C \cap H| = 20 - 10 = 10$.
   - Exactly Calculus & Physics $= |C \cap H| - |P \cap C \cap H| = 15 - 10 = 5$.
   - Total taking exactly two $= 15 + 10 + 5 = 30$.
   $$P(\text{exactly two}) = \frac{30}{120} = \frac{\mathbf{1}}{\mathbf{4}} = \mathbf{0.25} \quad (25\%)$$

---

### Answer to Question ST-09
**Reference:** [Problem Type PT-09](Study-Notes.md#problem-type-pt-09-empirical-relative-frequency-and-monte-carlo-estimation-in-r)
1. **Executable R Script:**
   ```r
   set.seed(237)
   N <- 100000
   sim_dice <- replicate(N, {
     sum(sample(1:6, size = 3, replace = TRUE)) >= 10
   })
   p_hat <- mean(sim_dice)
   cat("Estimated Probability P(Sum >= 10):", p_hat, "\n")
   ```
2. **Exact Theoretical Probability:**
   Total outcomes $= 6^3 = 216$.
   By symmetry of three 6-sided dice, the distribution of the sum is symmetric around $10.5$:
   $P(\text{Sum} \le 10) = P(\text{Sum} \ge 11) = 108/216 = 0.50$.
   The number of ways to roll a sum of 10 is 27.
   Thus, favorable outcomes for sum $\ge 10$ is $27 + 108 = 135$.
   $$P(\text{Sum} \ge 10) = \frac{135}{216} = \frac{5}{8} = \mathbf{0.625}$$
3. **Required Sample Size:**
   With $p = 5/8 = 0.625$, $p(1-p) = 0.625 \times 0.375 = 0.234375$.
   For a margin of error $E = 1.96 \sqrt{\frac{p(1-p)}{N}} \le 0.001$:
   $$N \ge \frac{1.96^2 \times 0.234375}{(0.001)^2} = \frac{3.8416 \times 0.234375}{0.000001} \approx \mathbf{900,375} \text{ trials}$$
   (Using the conservative upper bound $p=0.5$: $N \ge \frac{0.9604}{10^{-6}} = 960,400$).

---

## Section F: Compact Coverage and Unresolved-Items Appendix

### 1. Source Mapping Matrix

| Source File / Reading | Section & Pages | Topics Covered | Mapped Problem Type(s) | Exercises Solved |
| :--- | :--- | :--- | :--- | :--- |
| **Course Slides** (`Week2-L0401-annotated(1).pdf`) | Slides 1–6 | Inclusion-Exclusion ($n=3, 4$, general), Axiomatic justification | PT-08 | Ex. 1 (MMSA #15) |
| **Course Slides** (`Week2-L0401-annotated(1).pdf`) | Slides 8–12 | WLLN, empirical vs. theoretical probability, simulation | PT-09 | Rock-Paper-Scissors sim |
| **Course Slides** (`Week2-L0401-annotated(1).pdf`) | Slides 13–16 | FPC, tree diagrams, independent stages | PT-01 | Ex. 2 (PINs), Try 1 (Dice, 24500) |
| **Course Slides** (`Week2-L0401-annotated(1).pdf`) | Slides 18–21 | Permutations (${}_n P_k$), ordering without replacement | PT-02 | Ex. 3 (Lotto 649 ordered) |
| **Course Slides** (`Week2-L0401-annotated(1).pdf`) | Slides 22–23 | Unordered vs. ordered lotto, Birthday problem | PT-04, PT-07 | Ex. 3, Ex. 4 (Birthdays) |
| **Course Slides** (`Week2-L0401-annotated(1).pdf`) | Slides 24–26 | Permutations of repeated/indistinguishable objects | PT-03 | Ex. 5 (Balls), Try 2 (Digits) |
| **Course Slides** (`Week2-L0401-annotated(1).pdf`) | Slides 28–31 | Combinations ($\binom{n}{k}$), committee sampling | PT-04, PT-05 | Ex. 6 (Lunch with friends) |
| **Course Slides** (`Week2-L0401-annotated(1).pdf`) | Slides 32–34 | Poker hand card counting, symmetry vs. asymmetry miscounts | PT-05, PT-06 | Ex. 7 (Face cards, 2-pair), Full house case study |
| **MMSA (3rd ed.)** | Ch. 2.3, pp. 66–75 | Counting techniques, FPC, permutations, combinations | PT-01 through PT-08 | #31, #33, #34, #35, #37, #38, #39, #40, #43, #44, #45, #47 |
| **MMSA (3rd ed.)** | Ch. 2.6, pp. 94–103 | Simulation of random events, empirical frequency, SE | PT-09 | Theory & methodology synthesized |
| **PAR (Wagaman)** | Ch. 1.6–1.7, pp. 12–26 | Counting I & II (FPC, permutations, combinations) | PT-01 through PT-08 | #16, #17, #18, #19, #20, #21, #22, #23, #24, #25, #26, #29 |
| **PAR (Wagaman)** | Ch. 1.9, pp. 29–34 | A First Look at Simulation (R `sample`, `replicate`) | PT-09 | Theory & methodology synthesized |
| **PAR (Wagaman)** | Ch. 1.11, pp. 42–43 | Inclusion-Exclusion and discrete probability models | PT-01, PT-08 | #41, #49 |

---

### 2. Canvas Learning Objectives Alignment Audit

- $\checkmark$ **State and describe the Weak Law of Large Numbers:** Fully developed in Section 8.1 of `Study-Notes.md`, visualized in `wlln-simulation.png`, and tested in PT-09 and Self-Test Question ST-09.
- $\checkmark$ **State and use the Fundamental Principle of Counting (FPC):** Developed in Section 2.1 of `Study-Notes.md`, structured in PT-01, and solved across MMSA #31, #33, #34, #40, and PAR #16, #17, #18.
- $\checkmark$ **Apply FPC to count ordered subsets of $k$ elements from $n$ distinct elements:** Thoroughly formulated in Section 3.2 of `Study-Notes.md`, structured in PT-02, and solved in MMSA #31, #45, and PAR #16, #21.
- $\checkmark$ **Apply FPC to count unordered subsets of $k$ elements from $n$ distinct elements:** Formulated in Section 3.3 and 5.1 of `Study-Notes.md`, structured in PT-04, and solved in MMSA #31, #37, #47, and PAR #20, #22, #29.
- $\checkmark$ **Identify and describe how counting with partially indistinguishable elements can lead to under/over counting:** Deep dive in Section 4.1, 4.2, and Section 6 of `Study-Notes.md`, structured in PT-03 and PT-06, and demonstrated in MMSA #39, #43, #44, and PAR #18, #23, #26.
- $\checkmark$ **Apply counting strategies to solve counting problems and compute event probabilities:** Illustrated across all 9 Problem Types, all 11 lecture examples, all 26 textbook exercises, and all 9 self-test problems.

---

### 3. Record of Ambiguities and Interpretations

1. **PAR Chapter 1, Exercise 22(a) ("Bill's favorite sneakers"):**
   - *Ambiguity:* Whether "sneakers" denotes both individual shoes of the pair or at least one shoe.
   - *Resolution:* Both interpretations are completely solved and documented: both shoes ($\frac{19}{316} \approx 6.01\%$) and at least one shoe ($\frac{139}{316} \approx 43.99\%$).
2. **MMSA Section 2.3, Exercise 43(b) ("only two of the three types remain"):**
   - *Ambiguity:* Whether "only two" means strictly/exactly two types or at most two types.
   - *Resolution:* Both interpretations are solved and distinguished: strictly two types ($\frac{250}{1,001} \approx 24.98\%$) and at most two types ($\frac{251}{1,001} \approx 25.07\%$).
3. **MMSA Section 2.3, Exercise 39 (Ballot Problem):**
   - *Ambiguity:* Whether "strictly ahead" applies to all counts including the initial vote.
   - *Resolution:* Consistent with Bertrand's Ballot Theorem, $N_A(k) > N_B(k)$ for all $k \ge 1$, verified by exhaustive 10-path enumeration and theorem formula $(3-2)/(3+2) = 0.20$.
