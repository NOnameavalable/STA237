#!/usr/bin/env python3
"""
Writes Section C.2 (PAR Exercises) to Answers-and-Practice.md.
"""

OUTPUT_PATH = "/Users/stevenli/Documents/University of toronto/STA237/W3/Study-Notes-Markdown/Answers-and-Practice.md"

section_c2 = """
### Subsection C.2: Probability with Applications and R (PAR)

#### PAR Basic Exercises

##### Exercise PAR 2.4 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.4.  
**Classification:** PAR — Basic.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
Suppose $P(A) = P(B) = 0.3$ and $P(A \\mid B) = 0.5$. Find $P(A \\cup B)$.

**Complete working.**  
First, apply the multiplication rule to calculate the joint intersection probability $P(A \\cap B)$:
$$P(A \\cap B) = P(A \\mid B) \\cdot P(B) = 0.5 \\times 0.3 = 0.15$$
Next, apply the general addition rule for the union of two events:
$$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$$
$$P(A \\cup B) = 0.3 + 0.3 - 0.15 = 0.45$$

**Answer.**  
$P(A \\cup B) = 0.45$.

---

##### Exercise PAR 2.9 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.9.  
**Classification:** PAR — Basic.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
Find a simple expression for $P(A \\mid B)$ under the following conditions:
- (a) $A$ and $B$ are disjoint.
- (b) $A = B$.
- (c) $A$ implies $B$.
- (d) $B$ implies $A$.

**Complete working.**  
By definition, $P(A \\mid B) = \\frac{P(A \\cap B)}{P(B)}$ (for $P(B) > 0$).
- **(a) $A$ and $B$ are disjoint ($A \\cap B = \\emptyset$):**  
  Since $A \\cap B = \\emptyset$, $P(A \\cap B) = 0$.
  $$P(A \\mid B) = \\frac{0}{P(B)} = 0$$

- **(b) $A = B$:**  
  Since $A$ and $B$ are identical sets, $A \\cap B = B$.
  $$P(A \\mid B) = \\frac{P(B)}{P(B)} = 1$$

- **(c) $A$ implies $B$ ($A \\subseteq B$):**  
  In set theory, "$A$ implies $B$" means that whenever $A$ occurs, $B$ must occur, so $A$ is a subset of $B$ ($A \\subseteq B$). Consequently, $A \\cap B = A$.
  $$P(A \\mid B) = \\frac{P(A)}{P(B)}$$

- **(d) $B$ implies $A$ ($B \\subseteq A$):**  
  "$B$ implies $A$" means that whenever $B$ occurs, $A$ must occur, so $B$ is a subset of $A$ ($B \\subseteq A$). Consequently, $A \\cap B = B$.
  $$P(A \\mid B) = \\frac{P(B)}{P(B)} = 1$$

**Answer.**  
- (a) $P(A \\mid B) = 0$.
- (b) $P(A \\mid B) = 1$.
- (c) $P(A \\mid B) = \\frac{P(A)}{P(B)}$.
- (d) $P(A \\mid B) = 1$.

---

##### Exercise PAR 2.34 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.34.  
**Classification:** PAR — Basic.  
**Relevant PT ID(s):** [PT-03](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics).

**Complete question statement.**  
Suppose $A, B,$ and $C$ are independent events with respective probabilities $1/3, 1/4,$ and $1/5$. Find:
- (a) $P(ABC)$
- (b) $P(A \\text{ or } B \\text{ or } C)$
- (c) $P(AB \\mid C)$
- (d) $P(B \\mid AC)$
- (e) $P(\\text{At most one of the three events occurs})$

**Complete working.**  
Given: $P(A) = 1/3$, $P(B) = 1/4$, $P(C) = 1/5$. The events are mutually independent.

- **(a) $P(ABC) = P(A \\cap B \\cap C)$:**  
  By mutual independence:
  $$P(ABC) = P(A) \\cdot P(B) \\cdot P(C) = \\frac{1}{3} \\times \\frac{1}{4} \\times \\frac{1}{5} = \\frac{1}{60} \\approx 0.016667$$

- **(b) $P(A \\cup B \\cup C)$:**  
  Applying the complement rule with independent complements ($A^c, B^c, C^c$ are mutually independent):
  $$P(A \\cup B \\cup C) = 1 - P(A^c B^c C^c) = 1 - [P(A^c)P(B^c)P(C^c)]$$
  $$P(A^c) = 1 - \\frac{1}{3} = \\frac{2}{3}, \\quad P(B^c) = 1 - \\frac{1}{4} = \\frac{3}{4}, \\quad P(C^c) = 1 - \\frac{1}{5} = \\frac{4}{5}$$
  $$P(A^c B^c C^c) = \\frac{2}{3} \\times \\frac{3}{4} \\times \\frac{4}{5} = \\frac{2}{5}$$
  $$P(A \\cup B \\cup C) = 1 - \\frac{2}{5} = \\frac{3}{5} = 0.60$$

- **(c) $P(AB \\mid C)$:**  
  Because $A, B,$ and $C$ are mutually independent, the compound event $AB = A \\cap B$ is statistically independent of event $C$.  
  $$P(AB \\mid C) = P(AB) = P(A) \\cdot P(B) = \\frac{1}{3} \\times \\frac{1}{4} = \\frac{1}{12} \\approx 0.083333$$
  *(Formally: $\\frac{P(A \\cap B \\cap C)}{P(C)} = \\frac{1/60}{1/5} = \\frac{5}{60} = \\frac{1}{12}$)*

- **(d) $P(B \\mid AC)$:**  
  By mutual independence, event $B$ is independent of the compound event $AC = A \\cap C$:
  $$P(B \\mid AC) = P(B) = \\frac{1}{4} = 0.25$$
  *(Formally: $\\frac{P(A \\cap B \\cap C)}{P(A \\cap C)} = \\frac{1/60}{(1/3)(1/5)} = \\frac{1/60}{1/15} = \\frac{15}{60} = \\frac{1}{4}$)*

- **(e) $P(\\text{At most one occurs})$:**  
  "At most one" means either zero events occur or exactly one event occurs.
  1. *Zero events occur:* $P(A^c B^c C^c) = \\frac{2}{5} = \\frac{24}{60}$.
  2. *Exactly one event occurs:* Partition into three disjoint outcomes:
     - $A$ only: $P(A B^c C^c) = \\frac{1}{3} \\times \\frac{3}{4} \\times \\frac{4}{5} = \\frac{12}{60}$.
     - $B$ only: $P(A^c B C^c) = \\frac{2}{3} \\times \\frac{1}{4} \\times \\frac{4}{5} = \\frac{8}{60}$.
     - $C$ only: $P(A^c B^c C) = \\frac{2}{3} \\times \\frac{3}{4} \\times \\frac{1}{5} = \\frac{6}{60}$.
     Sum for exactly one: $\\frac{12 + 8 + 6}{60} = \\frac{26}{60}$.
  Summing zero and exactly one:
  $$P(\\text{At most one}) = \\frac{24}{60} + \\frac{26}{60} = \\frac{50}{60} = \\frac{5}{6} \\approx 0.833333$$

**Answer.**  
- (a) $P(ABC) = \\frac{1}{60} \\approx 0.0167$.
- (b) $P(A \\cup B \\cup C) = \\frac{3}{5} = 0.60$.
- (c) $P(AB \\mid C) = \\frac{1}{12} \\approx 0.0833$.
- (d) $P(B \\mid AC) = \\frac{1}{4} = 0.25$.
- (e) $P(\\text{At most one}) = \\frac{5}{6} \\approx 0.8333$.

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
  The support of $X$ is $\\mathcal{X} = \\{0, 1, 2, 3, 4\\}$.
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
  The support of $T$ is $\\mathcal{T} = \\{0, 1, 2, 3\\}$.
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
  The support of $N$ is $\\mathcal{N} = \\{1, 2, 3, 4, \\dots\\} = \\mathbb{Z}^+$. (This is a geometric random variable).
- **Expressed probability in terms of $N$:**  
  The event that the first win occurs in strictly less than 1000 tries is expressed as:
  $$P(N < 1000) \\quad \\text{or equivalently for discrete counts, } P(N \\le 999)$$

**Answer.**  
Random variable: Let $N =$ number of tries until the first win. Expressed probability: $P(N < 1000)$ (or $P(N \\le 999)$).

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
  The support of $B$ is $\\mathcal{B} = \\{0, 1, 2, \\dots, 100\\}$. (This is a binomial random variable).
- **Expressed probability in terms of $B$:**  
  The event that "at most five tomatoes are bad" is expressed as:
  $$P(B \\le 5)$$

**Answer.**  
Random variable: Let $B =$ number of bad tomatoes out of 100 harvested. Expressed probability: $P(B \\le 5)$.

---

##### Exercise PAR 3.6 (Ch. 3, p. 118)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 3, p. 118, Exercise 3.6.  
**Classification:** PAR — Basic.  
**Relevant PT ID(s):** [PT-10](#problem-type-pt-10-pmf-normalization-parameter-determination-and-validation).

**Complete question statement.**  
Suppose $X$ is a random variable that takes values on $\\{0, 0.01, 0.02, \\dots, 0.99, 1\\}$. If each outcome is equally likely, find:
- (a) $P(X \\le 0.33)$
- (b) $P(0.55 \\le X \\le 0.66)$

**Complete working.**  
The support $\\mathcal{X}$ contains the values $k / 100$ for integers $k \\in \\{0, 1, 2, \\dots, 100\\}$.
Total number of support points:
$$N = 100 - 0 + 1 = 101 \\text{ points}$$
Since all outcomes are equally likely, the probability mass function is uniform:
$$P(X = x) = \\frac{1}{101} \\quad \\forall x \\in \\mathcal{X}$$

- **(a) $P(X \\le 0.33)$:**  
  The condition $X \\le 0.33$ corresponds to integers $k \\in \\{0, 1, 2, \\dots, 33\\}$.  
  The number of favorable support points is $33 - 0 + 1 = 34$.
  $$P(X \\le 0.33) = \\frac{34}{101} \\approx 0.336634$$

- **(b) $P(0.55 \\le X \\le 0.66)$:**  
  The condition $0.55 \\le X \\le 0.66$ corresponds to integers $k \\in \\{55, 56, \\dots, 66\\}$.  
  The number of favorable support points is $66 - 55 + 1 = 12$.
  $$P(0.55 \\le X \\le 0.66) = \\frac{12}{101} \\approx 0.118812$$

**Answer.**  
- (a) $P(X \\le 0.33) = \\frac{34}{101} \\approx 0.3366$.
- (b) $P(0.55 \\le X \\le 0.66) = \\frac{12}{101} \\approx 0.1188$.

---

##### Exercise PAR 3.7 (Ch. 3, p. 118)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 3, p. 118, Exercise 3.7.  
**Classification:** PAR — Basic.  
**Relevant PT ID(s):** [PT-09](#problem-type-pt-09-random-variable-definition-and-event-to-variable-mapping).

**Complete question statement.**  
Suppose $X$ is a random variable that takes values on all positive integers ($\\mathcal{X} = \\{1, 2, 3, 4, \\dots\\} = \\mathbb{Z}^+$). Let $A = \\{2 \\le X \\le 4\\}$ and $B = \\{X \\ge 4\\}$. Describe the events:
- (i) $A^c$
- (ii) $B^c$
- (iii) $AB$ ($A \\cap B$)
- (iv) $A \\cup B$

**Complete working.**  
Given universe of values: $\\mathcal{X} = \\{1, 2, 3, 4, 5, \\dots\\}$.
- $A = \\{2 \\le X \\le 4\\} = \\{2, 3, 4\\}$.
- $B = \\{X \\ge 4\\} = \\{4, 5, 6, 7, \\dots\\}$.

- **(i) Event $A^c$:**  
  The complement consists of all positive integers strictly less than 2 or strictly greater than 4:
  $$A^c = \\{X = 1\\} \\cup \\{X \\ge 5\\} = \\{1, 5, 6, 7, \\dots\\}$$

- **(ii) Event $B^c$:**  
  The complement consists of all positive integers strictly less than 4:
  $$B^c = \\{X < 4\\} = \\{X \\le 3\\} = \\{1, 2, 3\\}$$

- **(iii) Event $AB = A \\cap B$:**  
  The intersection contains support points common to both $\\{2, 3, 4\\}$ and $\\{4, 5, 6, \\dots\\}$:
  $$A \\cap B = \\{X = 4\\} = \\{4\\}$$

- **(iv) Event $A \\cup B$:**  
  The union combines all support points present in at least one set:
  $$A \\cup B = \\{2, 3, 4\\} \\cup \\{4, 5, 6, \\dots\\} = \\{X \\ge 2\\} = \\{2, 3, 4, 5, \\dots\\}$$

**Answer.**  
- (i) $A^c = \\{1, 5, 6, 7, \\dots\\} = \\{X = 1\\} \\cup \\{X \\ge 5\\}$.
- (ii) $B^c = \\{1, 2, 3\\} = \\{X \\le 3\\}$.
- (iii) $AB = \\{4\\} = \\{X = 4\\}$.
- (iv) $A \\cup B = \\{2, 3, 4, 5, \\dots\\} = \\{X \\ge 2\\}$.

---

#### PAR Medium Exercises

##### Exercise PAR 2.5 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.5.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
Suppose $P(A) = P(B) = p_1$ and $P(A \\cup B) = p_2$. Find $P(A \\mid B)$.

**Complete working.**  
By the addition rule for the union of two events:
$$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$$
Substitute the given algebraic quantities:
$$p_2 = p_1 + p_1 - P(A \\cap B) = 2p_1 - P(A \\cap B)$$
Isolating the joint intersection probability:
$$P(A \\cap B) = 2p_1 - p_2$$
Now apply the definition of conditional probability:
$$P(A \\mid B) = \\frac{P(A \\cap B)}{P(B)} = \\frac{2p_1 - p_2}{p_1} = 2 - \\frac{p_2}{p_1} \\quad (\\text{provided } p_1 > 0)$$

*Boundary Check:* Since $A \\cap B \\subseteq B$, $2p_1 - p_2 \\le p_1 \\implies p_2 \\ge p_1$. Furthermore, $P(A \\cap B) \\ge 0 \\implies p_2 \\le 2p_1$. These conditions guarantee $0 \\le P(A \\mid B) \\le 1$.

**Answer.**  
$P(A \\mid B) = \\frac{2p_1 - p_2}{p_1} = 2 - \\frac{p_2}{p_1}$.

---

##### Exercise PAR 2.7 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.7.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
A total of 108 students filled out a survey for a psychology class project. A total of 36 students indicated they were athletes. Of those students, 21 said they preferred to work out in the morning as opposed to the afternoon. For the nonathletes, 25 said they preferred to work out in the morning. Find the following probabilities for a randomly selected student who took the survey:
- (a) $P(\\text{Athlete given prefer morning workout})$
- (b) $P(\\text{Prefer morning workout given nonathlete})$
- (c) $P(\\text{Nonathlete given prefer nonmorning workout})$

**Complete working.**  
Total students $N = 108$.
Let $A$ be Athlete ($n(A) = 36$), so Nonathletes $n(A^c) = 108 - 36 = 72$.
Let $M$ be Prefer Morning Workout:
- Among 36 athletes: $n(A \\cap M) = 21$, so $n(A \\cap M^c) = 36 - 21 = 15$.
- Among 72 nonathletes: $n(A^c \\cap M) = 25$, so $n(A^c \\cap M^c) = 72 - 25 = 47$.

Marginal workout preference totals:
- Total preferring morning ($M$): $n(M) = 21 + 25 = 46$.
- Total preferring non-morning ($M^c$): $n(M^c) = 15 + 47 = 62$.
Sum check: $46 + 62 = 108$.

- **(a) $P(\\text{Athlete} \\mid \\text{Morning}) = P(A \\mid M)$:**  
  Restricting to morning workout column ($n(M) = 46$):
  $$P(A \\mid M) = \\frac{n(A \\cap M)}{n(M)} = \\frac{21}{46} \\approx 0.456522$$

- **(b) $P(\\text{Morning} \\mid \\text{Nonathlete}) = P(M \\mid A^c)$:**  
  Restricting to nonathlete row ($n(A^c) = 72$):
  $$P(M \\mid A^c) = \\frac{n(A^c \\cap M)}{n(A^c)} = \\frac{25}{72} \\approx 0.347222$$

- **(c) $P(\\text{Nonathlete} \\mid \\text{Nonmorning}) = P(A^c \\mid M^c)$:**  
  Restricting to non-morning column ($n(M^c) = 62$):
  $$P(A^c \\mid M^c) = \\frac{n(A^c \\cap M^c)}{n(M^c)} = \\frac{47}{62} \\approx 0.758065$$

**Answer.**  
- (a) $P(A \\mid M) = \\frac{21}{46} \\approx 0.4565$ (45.65%).
- (b) $P(M \\mid A^c) = \\frac{25}{72} \\approx 0.3472$ (34.72%).
- (c) $P(A^c \\mid M^c) = \\frac{47}{62} \\approx 0.7581$ (75.81%).

---

##### Exercise PAR 2.11 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.11.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction), Conceptual Foundations.

**Complete question statement.**  
True or False. Either show the statement to be true for any event $A$ and $B$ (with $0 < P(B) < 1$) or exhibit a counterexample:
- (a) $P(A \\mid B) + P(A \\mid B^c) = 1$.
- (b) $P(A \\mid B) + P(A^c \\mid B) = 1$.

**Complete working.**  
- **(a) Analysis of $P(A \\mid B) + P(A \\mid B^c) = 1$:**  
  **FALSE.**  
  *Proof by Counterexample:*  
  Let the experiment be rolling a fair 6-sided die, $\\Omega = \\{1, 2, 3, 4, 5, 6\\}$.  
  Let $A = \\Omega$ (the certain event, $P(A) = 1$).  
  Let $B = \\{1, 2\\}$, so $B^c = \\{3, 4, 5, 6\\}$.  
  Then $P(A \\mid B) = 1$ and $P(A \\mid B^c) = 1$.  
  Sum $= 1 + 1 = 2 \\neq 1$.  
  *Alternative Non-Trivial Counterexample:*  
  Let $A$ and $B$ be independent events with $P(A) = 0.20$ and $P(B) = 0.50$.  
  By independence, $P(A \\mid B) = P(A) = 0.20$, and $P(A \\mid B^c) = P(A) = 0.20$.  
  Sum $= 0.20 + 0.20 = 0.40 \\neq 1$.

- **(b) Analysis of $P(A \\mid B) + P(A^c \\mid B) = 1$:**  
  **TRUE.**  
  *General Analytical Proof:*  
  By definition of conditional probability:
  $$P(A \\mid B) + P(A^c \\mid B) = \\frac{P(A \\cap B)}{P(B)} + \\frac{P(A^c \\cap B)}{P(B)} = \\frac{P(A \\cap B) + P(A^c \\cap B)}{P(B)}$$
  Notice that $A \\cap B$ and $A^c \\cap B$ are disjoint sets because $A \\cap A^c = \\emptyset$.  
  Their union is:
  $$(A \\cap B) \\cup (A^c \\cap B) = (A \\cup A^c) \\cap B = \\Omega \\cap B = B$$
  By Kolmogorov Axiom 3 (finite additivity):
  $$P(A \\cap B) + P(A^c \\cap B) = P((A \\cap B) \\cup (A^c \\cap B)) = P(B)$$
  Substituting this into the numerator:
  $$\\frac{P(B)}{P(B)} = 1$$
  Thus, the identity holds universally for any event $A$ and any event $B$ with $P(B) > 0$. $\\blacksquare$

**Answer.**  
- (a) **False** (Counterexample: if $A$ and $B$ are independent with $P(A) = 0.2$, sum is $0.4 \\neq 1$).
- (b) **True** (Proven: $(A \\cap B) \\cup (A^c \\cap B) = B \\implies \\frac{P(B)}{P(B)} = 1$).

---

##### Exercise PAR 2.16 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.16.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** [PT-02](#problem-type-pt-02-multi-stage-sequential-intersection-via-the-general-multiplication--chain-rule).

**Complete question statement.**  
Suppose $P(A) = 1/2$, $P(B^c \\mid AC) = 1/3$, and $P(C \\mid A) = 1/4$. Find $P(ABC)$ ($P(A \\cap B \\cap C)$).

**Complete working.**  
First, apply the complement rule within the conditioned space $AC = A \\cap C$:
$$P(B \\mid AC) = 1 - P(B^c \\mid AC) = 1 - \\frac{1}{3} = \\frac{2}{3}$$
Next, apply the Chain Rule for three events:
$$P(ABC) = P(A \\cap B \\cap C) = P(A) \\cdot P(C \\mid A) \\cdot P(B \\mid A \\cap C)$$
Substitute the given and derived probabilities:
$$P(ABC) = \\frac{1}{2} \\times \\frac{1}{4} \\times \\frac{2}{3} = \\frac{2}{24} = \\frac{1}{12} \\approx 0.083333$$

**Answer.**  
$P(ABC) = \\frac{1}{12} \\approx 0.0833$.

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
Bag selection: Uniform at random $\\implies P(B_1) = 1/2$, $P(B_2) = 1/2$.
Let $G$ be the event that Gummi Bears are selected.
- Conditional rates: $P(G \\mid B_1) = 3/5$, $P(G \\mid B_2) = 2/6 = 1/3$.

- **(i) Method 1: Tree Diagram:**  
  - Branch 1: Choose Bag 1 ($1/2$) $\\to$ Choose Gummi Bears ($3/5$).  
    Joint path probability $= \\frac{1}{2} \\times \\frac{3}{5} = \\frac{3}{10} = \\frac{9}{30}$.
  - Branch 2: Choose Bag 2 ($1/2$) $\\to$ Choose Gummi Bears ($2/6 = 1/3$).  
    Joint path probability $= \\frac{1}{2} \\times \\frac{1}{3} = \\frac{1}{6} = \\frac{5}{30}$.
  Summing the terminal Gummi Bear leaf nodes:
  $$P(G) = \\frac{9}{30} + \\frac{5}{30} = \\frac{14}{30} = \\frac{7}{15} \\approx 0.466667$$

- **(ii) Method 2: Analytical Law of Total Probability:**  
  Using the binary partition $\\{B_1, B_2\\}$:
  $$P(G) = P(G \\mid B_1)P(B_1) + P(G \\mid B_2)P(B_2)$$
  $$P(G) = \\left(\\frac{3}{5}\\right)\\left(\\frac{1}{2}\\right) + \\left(\\frac{2}{6}\\right)\\left(\\frac{1}{2}\\right) = \\frac{3}{10} + \\frac{1}{6} = \\frac{9 + 5}{30} = \\frac{14}{30} = \\frac{7}{15}$$

**Answer.**  
$P(\\text{Gummi Bears}) = \\frac{7}{15} \\approx 0.4667$ (46.67%).

---

##### Exercise PAR 2.27 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.27.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** [PT-05](#problem-type-pt-05-total-probability-computation-via-partition-decompositions-and-tree-diagrams).

**Complete question statement.**  
In a certain population of youth, the probability of being a smoker is 20%. The probability that at least one parent is a smoker is 30%. And if at least one parent is a smoker, the probability of being a smoker is 35%. Find the probability of being a smoker if neither parent is a smoker.

**Complete working.**  
Define events:
- $S$: Youth is a smoker $\\implies P(S) = 0.20$.
- $A$: At least one parent is a smoker $\\implies P(A) = 0.30$.
- $A^c$: Neither parent is a smoker $\\implies P(A^c) = 1 - 0.30 = 0.70$.
- Conditional probability: $P(S \\mid A) = 0.35$.

We seek $P(S \\mid A^c)$.
The events $\\{A, A^c\\}$ partition the parental smoking status. Applying the Law of Total Probability:
$$P(S) = P(S \\mid A)P(A) + P(S \\mid A^c)P(A^c)$$
Substitute the known values into the equation:
$$0.20 = (0.35 \\times 0.30) + P(S \\mid A^c) \\times 0.70$$
$$0.20 = 0.105 + 0.70 \\, P(S \\mid A^c)$$
Isolate $P(S \\mid A^c)$:
$$0.70 \\, P(S \\mid A^c) = 0.20 - 0.105 = 0.095$$
$$P(S \\mid A^c) = \\frac{0.095}{0.70} = \\frac{95}{700} = \\frac{19}{140} \\approx 0.135714$$

**Answer.**  
$P(S \\mid A^c) = \\frac{19}{140} \\approx 0.1357$ (13.57%).

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
- Prevalence: $P(C) = 0.0238 \\implies P(C^c) = 1 - 0.0238 = 0.9762$.
- Sensitivity: $P(+ \\mid C) = 0.85$.
- Specificity: $P(- \\mid C^c) = 0.95 \\implies \\text{False Positive Rate } P(+ \\mid C^c) = 0.05$.

We seek the Positive Predictive Value $P(C \\mid +)$.
- **Step 1: Total probability of positive mammogram ($P(+)$):**  
  Applying the Law of Total Probability:
  $$P(+) = P(+ \\mid C)P(C) + P(+ \\mid C^c)P(C^c)$$
  $$P(+) = (0.85 \\times 0.0238) + (0.05 \\times 0.9762)$$
  $$P(+) = 0.02023 + 0.04881 = 0.06904$$

- **Step 2: Invert via Bayes' Rule:**  
  $$P(C \\mid +) = \\frac{P(+ \\mid C)P(C)}{P(+)} = \\frac{0.02023}{0.06904} = \\frac{2023}{6904} \\approx 0.293019$$

*Interpretation:* Despite high sensitivity (85%) and specificity (95%), a positive mammogram for a 50-year-old woman yields only a $29.30\\%$ posterior probability of cancer, because false positives from the healthy 97.6% majority outnumber true positives by more than 2 to 1.

**Answer.**  
$P(C \\mid +) = \\frac{2023}{6904} \\approx 0.2930$ (29.30%).

---

##### Exercise PAR 2.30 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.30.  
**Classification:** PAR — Medium.  
**Relevant PT ID(s):** [PT-07](#problem-type-pt-07-posterior-probability-inversion-via-bayes-rule).

**Complete question statement.**  
An eyewitness observes a hit-and-run accident in New York City, where 95% of the cabs are yellow and 5% are blue. The witness asserts the cab was blue. Police experts believe that eyewitnesses are 80% reliable. That is, an eyewitness will correctly identify the color of a cab 80% of the time. What is the probability that the cab actually was blue?

**Complete working.**  
Define events:
- Cab colors: $B = \\{\\text{cab is Blue}\\}$, $Y = \\{\\text{cab is Yellow}\\}$.
  Priors: $P(B) = 0.05, P(Y) = 0.95$.
- Witness testimony: $W_B = \\{\\text{witness asserts cab is Blue}\\}$.
- Witness reliability (80%):
  $P(W_B \\mid B) = 0.80$ (correct identification)
  $P(W_B \\mid Y) = 0.20$ (misidentifying a yellow cab as blue)

We seek $P(B \\mid W_B)$.
- **Step 1: Total probability that witness reports blue ($P(W_B)$):**  
  Applying the Law of Total Probability:
  $$P(W_B) = P(W_B \\mid B)P(B) + P(W_B \\mid Y)P(Y)$$
  $$P(W_B) = (0.80 \\times 0.05) + (0.20 \\times 0.95) = 0.040 + 0.190 = 0.230$$

- **Step 2: Invert via Bayes' Rule:**  
  $$P(B \\mid W_B) = \\frac{P(W_B \\mid B)P(B)}{P(W_B)} = \\frac{0.040}{0.230} = \\frac{4}{23} \\approx 0.173913$$

*Interpretation:* Although the witness is 80% accurate, because yellow cabs are so dominant (95%), the witness is actually more than 4 times as likely to have mistakenly called a yellow cab blue ($0.19$) than to have correctly seen a blue cab ($0.04$). The probability the cab was blue is only $17.39\\%$.

**Answer.**  
$P(B \\mid W_B) = \\frac{4}{23} \\approx 0.1739$ (17.39%).

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
- $P(R \\cup B) = 0.70$
- $P(B^c) = 0.40 \\implies P(B) = 1 - 0.40 = 0.60$
- $R$ and $B$ are statistically independent ($R \\perp B$)

By the complement rule and De Morgan's Law:
$$P((R \\cup B)^c) = P(R^c \\cap B^c) = 1 - P(R \\cup B) = 1 - 0.70 = 0.30$$
By the Independence of Complements Theorem, since $R \\perp B$, their complements are also independent ($R^c \\perp B^c$):
$$P(R^c \\cap B^c) = P(R^c) \\cdot P(B^c)$$
Substitute the known values:
$$0.30 = P(R^c) \\times 0.40 \\implies P(R^c) = \\frac{0.30}{0.40} = 0.75$$
Applying the complement rule to find $P(R)$:
$$P(R) = 1 - P(R^c) = 1 - 0.75 = 0.25$$

*Verification via Addition Rule:*
$$P(R \\cup B) = P(R) + P(B) - P(R \\cap B) = 0.25 + 0.60 - (0.25 \\times 0.60) = 0.85 - 0.15 = 0.70$$
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
If a participant buys $k$ distinct tickets ($1 \\le k \\le 1000$), the event of winning $W$ is the union of the $k$ distinct ticket numbers. Since the ticket numbers are mutually exclusive single-number outcomes:
$$P(W) = \\frac{k}{1000}$$
We require:
$$P(W) \\ge 0.50 \\implies \\frac{k}{1000} \\ge 0.50 \\implies k \\ge 500$$
To guarantee a probability of at least $50\\%$, you must purchase at least 500 distinct tickets.

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
   $$P(\text{Win}) = 1 - \left(\frac{29}{30}\right)^k$$
   We require $P(\text{Win}) \ge 0.25$:
   $$1 - \left(\frac{29}{30}\right)^k \ge 0.25 \implies \left(\frac{29}{30}\right)^k \le 0.75$$
   Taking natural logarithms:
   $$k \ln\left(\frac{29}{30}\right) \le \ln(0.75) \implies k(-0.033902) \le -0.287682$$
   $$k \ge \frac{-0.287682}{-0.033902} \approx 8.485$$
   Since $k$ must be an integer:
   $$k = \lceil 8.485 \rceil = 9$$

2. **Finite Fixed-Batch Model (Sampling without Replacement from 30 Unique Tickets):**  
   If the church sells exactly 30 unique physical tickets and draws 1 winner without replacement:
   $$P(\text{Win}) = \frac{k}{30} \ge 0.25 \implies k \ge 30 \times 0.25 = 7.5 \implies k = 8$$

**Answer.**  
**Textbook Answer Key (p. 511):** **$9$ tickets** (derived from the textbook's independent model $1 - (29/30)^k \ge 0.25$).  
*(Alternative note: If buying $k$ unique tickets from a fixed pool of 30 without replacement, $k = \lceil 7.5 \rceil = 8$ tickets).*

---

#### PAR Test Exercises
*(Note: Preserving exact course screenshot sequence: #17, 23, 26, 29, 31, 33, 32, 36 — specifically #33 before #32).*

##### Exercise PAR 2.17 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.17.  
**Classification:** PAR — Test.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction), Theoretical Proofs.

**Complete question statement.**  
Prove the addition rule for conditional probabilities. That is, show that for events $A, B,$ and $C$ (with $P(C) > 0$):
$$P(A \\cup B \\mid C) = P(A \\mid C) + P(B \\mid C) - P(AB \\mid C)$$

**Complete working.**  
- **Step 1: Expand conditional definition:**  
  By definition of conditional probability:
  $$P(A \\cup B \\mid C) = \\frac{P((A \\cup B) \\cap C)}{P(C)}$$

- **Step 2: Apply set distributive law:**  
  Distribute intersection with $C$ across the union:
  $$(A \\cup B) \\cap C = (A \\cap C) \\cup (B \\cap C)$$

- **Step 3: Apply unconditional addition rule:**  
  Let $E_1 = A \\cap C$ and $E_2 = B \\cap C$. By the standard addition rule for unconditional probabilities:
  $$P(E_1 \\cup E_2) = P(E_1) + P(E_2) - P(E_1 \\cap E_2)$$
  Notice that:
  $$E_1 \\cap E_2 = (A \\cap C) \\cap (B \\cap C) = A \\cap B \\cap C = AB \\cap C$$
  Therefore:
  $$P((A \\cup B) \\cap C) = P(A \\cap C) + P(B \\cap C) - P(AB \\cap C)$$

- **Step 4: Divide by $P(C)$:**  
  $$P(A \\cup B \\mid C) = \\frac{P(A \\cap C) + P(B \\cap C) - P(AB \\cap C)}{P(C)} = \\frac{P(A \\cap C)}{P(C)} + \\frac{P(B \\cap C)}{P(C)} - \\frac{P(AB \\cap C)}{P(C)}$$
  By definition, these ratios are $P(A \\mid C), P(B \\mid C),$ and $P(AB \\mid C)$:
  $$P(A \\cup B \\mid C) = P(A \\mid C) + P(B \\mid C) - P(AB \\mid C)$$
  $\\blacksquare$

**Answer.**  
Proof established algebraically by distributing $(A \\cup B) \\cap C = (A \\cap C) \\cup (B \\cap C)$ and applying the unconditional addition rule divided by $P(C)$.

---

##### Exercise PAR 2.23 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.23.  
**Classification:** PAR — Test.  
**Relevant PT ID(s):** [PT-01](#problem-type-pt-01-direct-conditional-probability-computation-and-sample-space-restriction).

**Complete question statement.**  
Give a formula for $P(A \\mid B^c)$ in terms of $P(A), P(B),$ and $P(AB)$ only.

**Complete working.**  
By the definition of conditional probability:
$$P(A \\mid B^c) = \\frac{P(A \\cap B^c)}{P(B^c)}$$
1. Express the denominator using the complement rule:
   $$P(B^c) = 1 - P(B)$$
2. Express the numerator using the difference rule:
   Since $A = (A \\cap B) \\cup (A \\cap B^c)$ where the sets are disjoint:
   $$P(A) = P(A \\cap B) + P(A \\cap B^c) \\implies P(A \\cap B^c) = P(A) - P(A \\cap B) = P(A) - P(AB)$$
3. Substitute these two expressions:
   $$P(A \\mid B^c) = \\frac{P(A) - P(AB)}{1 - P(B)}$$

**Answer.**  
$P(A \\mid B^c) = \\frac{P(A) - P(AB)}{1 - P(B)}$.

---

##### Exercise PAR 2.26 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.26.  
**Classification:** PAR — Test.  
**Relevant PT ID(s):** [PT-06](#problem-type-pt-06-first-step-analysis-and-recursive-conditioning).

**Complete question statement.**  
Consider flipping coins until either two heads $HH$ or heads then tails $HT$ first occurs. By conditioning on the first coin toss, find the probability that $HT$ occurs before $HH$.

**Complete working.**  
Let $E$ be the event that sequence $HT$ occurs before sequence $HH$. Let $p = P(E)$.
Condition on the outcome of the very first coin toss $T_1 \\in \\{H, T\\}$, where $P(T_1 = H) = 1/2$ and $P(T_1 = T) = 1/2$.
By the Law of Total Probability:
$$p = P(E \\mid T_1 = H) \\cdot P(T_1 = H) + P(E \\mid T_1 = T) \\cdot P(T_1 = T)$$

- **Case 1: First toss is Tails ($T_1 = T$):**  
  Both target patterns ($HT$ and $HH$) begin with an initial $H$. Any sequence of initial tails ($T, TT, TTT, \\dots$) can never contribute to either pattern. The experiment simply resets until the first $H$ is flipped.
  $$P(E \\mid T_1 = T) = p$$

- **Case 2: First toss is Heads ($T_1 = H$):**  
  Now look at the immediate second coin toss $T_2 \\in \\{H, T\\}$:
  - If $T_2 = T$, the full sequence generated so far is $HT$. The target $HT$ has occurred before $HH$ can ever form!  
    Thus, $P(E \\mid T_1 = H, T_2 = T) = 1$.
  - If $T_2 = H$, the full sequence generated so far is $HH$. The rival $HH$ has occurred, so $HT$ did *not* occur before $HH$!  
    Thus, $P(E \\mid T_1 = H, T_2 = H) = 0$.

  Conditioning on $T_2$ given $T_1 = H$:
  $$P(E \\mid T_1 = H) = 1 \\cdot P(T_2 = T) + 0 \\cdot P(T_2 = H) = 1 \\cdot \\left(\\frac{1}{2}\\right) + 0 \\cdot \\left(\\frac{1}{2}\\right) = \\frac{1}{2}$$

- **Step 3: Solve the LTP linear equation:**  
  Substitute the conditional values into the total probability formula:
  $$p = \\left(\\frac{1}{2}\\right)\\left(\\frac{1}{2}\\right) + p\\left(\\frac{1}{2}\\right) = \\frac{1}{4} + \\frac{1}{2}p$$
  $$p - \\frac{1}{2}p = \\frac{1}{4} \\implies \\frac{1}{2}p = \\frac{1}{4} \\implies p = \\frac{2}{4} = \\frac{1}{2}$$

**Answer.**  
$P(HT \\text{ before } HH) = \\frac{1}{2} = 0.50$.

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
- $L$: Person is lying $\\implies P(L) = 0.05$.
- $T$: Person is telling the truth $\\implies P(T) = 0.95$.
- $F$: Polygraph concludes lying (person fails test).

Reliability $r = 0.90$:
- $P(F \\mid L) = r = 0.90$ (sensitivity)
- $P(F^c \\mid T) = r = 0.90$ (specificity) $\\implies P(F \\mid T) = 1 - r = 0.10$ (false alarm rate).

- **(a) Evaluate $P(L \\mid F)$ for $r = 0.90$:**  
  Marginal probability of failing the polygraph via LTP:
  $$P(F) = P(F \\mid L)P(L) + P(F \\mid T)P(T) = (0.90 \\times 0.05) + (0.10 \\times 0.95)$$
  $$P(F) = 0.045 + 0.095 = 0.140$$
  Applying Bayes' Rule:
  $$P(L \\mid F) = \\frac{P(F \\mid L)P(L)}{P(F)} = \\frac{0.045}{0.140} = \\frac{45}{140} = \\frac{9}{28} \\approx 0.321429 \\quad (32.14\\%)$$
  Even with 90% reliability, approximately $68\\%$ of those who fail the test are truthful!

- **(b) Find reliability $r$ such that $P(L \\mid F) \\ge 0.80$:**  
  Let reliability be $r$. Then $P(F \\mid L) = r$ and $P(F \\mid T) = 1 - r$.
  $$P(L \\mid F) = \\frac{0.05 r}{0.05 r + 0.95(1 - r)} \\ge 0.80$$
  $$0.05 r \\ge 0.80 [0.05 r + 0.95 - 0.95 r] = 0.80 [0.95 - 0.90 r] = 0.76 - 0.72 r$$
  $$0.05 r + 0.72 r \\ge 0.76 \\implies 0.77 r \\ge 0.76$$
  $$r \\ge \\frac{0.76}{0.77} = \\frac{76}{77} \\approx 0.987013$$
  The polygraph must be at least **$98.70\\%$ reliable**.

**Answer.**  
- (a) $P(L \\mid F) = \\frac{9}{28} \\approx 0.3214$ (32.14%).
- (b) $r \\ge \\frac{76}{77} \\approx 0.9870$ (98.70% reliability required).

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
$$P(D_1) = P(D_2) = P(D_3) = \\frac{1}{3}$$
Let $F_5$ be the event that the rolled die lands on 5.
Conditional likelihoods of rolling a 5 for each die:
- Fair die ($D_1$): 6 distinct faces $\\{1, 2, 3, 4, 5, 6\\} \\implies P(F_5 \\mid D_1) = 1/6$.
- All fives die ($D_2$): 6 fives $\\{5, 5, 5, 5, 5, 5\\} \\implies P(F_5 \\mid D_2) = 6/6 = 1$.
- Half fives die ($D_3$): 3 fives and 3 fours $\\implies P(F_5 \\mid D_3) = 3/6 = 1/2$.

Applying the Law of Total Probability to find $P(F_5)$:
$$P(F_5) = P(F_5 \\mid D_1)P(D_1) + P(F_5 \\mid D_2)P(D_2) + P(F_5 \\mid D_3)P(D_3)$$
$$P(F_5) = \\left(\\frac{1}{6} \\times \\frac{1}{3}\\right) + \\left(1 \\times \\frac{1}{3}\\right) + \\left(\\frac{1}{2} \\times \\frac{1}{3}\\right) = \\frac{1}{3} \\left[\\frac{1}{6} + \\frac{6}{6} + \\frac{3}{6}\\right] = \\frac{1}{3} \\times \\frac{10}{6} = \\frac{10}{18} = \\frac{5}{9}$$

Applying Bayes' Rule to find $P(D_1 \\mid F_5)$:
$$P(D_1 \\mid F_5) = \\frac{P(F_5 \\mid D_1)P(D_1)}{P(F_5)} = \\frac{(1/6)(1/3)}{10/18} = \\frac{1/18}{10/18} = \\frac{1}{10} = 0.10$$

**Answer.**  
$P(D_1 \\mid F_5) = \\frac{1}{10} = 0.10$ (10.0%).

---

##### Exercise PAR 2.33 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.33.  
**Classification:** PAR — Test.  
*(Note: Ordered before #32 to preserve exact screenshot sequence).*  
**Relevant PT ID(s):** [PT-03](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics), Theoretical Proofs.

**Complete question statement.**  
Suppose $A$ and $B$ are independent events. Show that $A^c$ and $B^c$ are independent events.

**Complete working.**  
Given: $P(A \\cap B) = P(A) \\cdot P(B)$.
We must show that $P(A^c \\cap B^c) = P(A^c) \\cdot P(B^c)$.

- **Step 1: Apply De Morgan's Law:**  
  $$A^c \\cap B^c = (A \\cup B)^c$$
- **Step 2: Apply the complement rule:**  
  $$P(A^c \\cap B^c) = P((A \\cup B)^c) = 1 - P(A \\cup B)$$
- **Step 3: Expand union by general addition rule:**  
  $$P(A^c \\cap B^c) = 1 - [P(A) + P(B) - P(A \\cap B)]$$
- **Step 4: Substitute the independence condition $P(A \\cap B) = P(A)P(B)$:**  
  $$P(A^c \\cap B^c) = 1 - P(A) - P(B) + P(A)P(B)$$
- **Step 5: Factor the algebraic expression:**  
  $$P(A^c \\cap B^c) = [1 - P(A)] - P(B)[1 - P(A)] = [1 - P(A)][1 - P(B)]$$
  Since $1 - P(A) = P(A^c)$ and $1 - P(B) = P(B^c)$:
  $$P(A^c \\cap B^c) = P(A^c) \\cdot P(B^c)$$
This establishes that $A^c$ and $B^c$ are statistically independent. $\\blacksquare$

**Answer.**  
Proof established: $P(A^c \\cap B^c) = 1 - P(A \\cup B) = 1 - P(A) - P(B) + P(A)P(B) = (1 - P(A))(1 - P(B)) = P(A^c)P(B^c)$.

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
   *Example:* You roll a single die. Let $A$ be rolling an even number and $B$ be rolling an odd number. The die cannot be both even and odd simultaneously ($A \\cap B = \\emptyset$). If I tell you the roll is even, the probability that it is odd immediately drops to zero ($P(B \\mid A) = 0$). Knowing $A$ occurred gives you *total information* about $B$.

2. **Independent Events:**  
   Think of independent events as **unrelated, uninformative occurrences**. They can easily happen together, and knowing that one happened gives you *zero new information* about whether the other happened.  
   *Example:* You roll a red die and a blue die. Let $A$ be the red die showing 6, and $B$ be the blue die showing 6. Can both occur? Yes, you can roll two sixes. Does seeing a 6 on the red die change the chance of getting a 6 on the blue die? Not at all; it remains $1/6$ ($P(B \\mid A) = P(B)$).

3. **The Golden Rule to remember:**  
   If two events both have positive probabilities, **they can NEVER be both disjoint and independent**. Disjoint events are *maximally dependent*, because the occurrence of one prevents the other from occurring!

**Answer.**  
Disjoint events cannot happen together ($P(A \\cap B) = 0$); if one occurs, the other is impossible. Independent events can happen together, and one happening gives zero information about the other ($P(A \\mid B) = P(A)$).

---

##### Exercise PAR 2.36 (Ch. 2, p. 84)
**Source:** Wagaman & Dobrow (2nd ed.), Chapter 2, p. 84, Exercise 2.36.  
**Classification:** PAR — Test.  
**Relevant PT ID(s):** [PT-03](#problem-type-pt-03-independence-verification-and-independence-vs-disjointness-diagnostics).

**Complete question statement.**  
Toss two dice. Let $A$ be the event that the first die rolls 1, 2, or 3. Let $B$ be the event that the first die rolls 3, 4, or 5. Let $C$ be the event that the sum of the dice is 9. Show that $P(ABC) = P(A)P(B)P(C)$, but no pair of events is independent.

**Complete working.**  
The sample space $\\Omega$ consists of all 36 equally likely ordered pairs $(d_1, d_2)$ where $d_1, d_2 \\in \\{1, 2, 3, 4, 5, 6\\}$.
- Event $A = \\{d_1 \\in \\{1, 2, 3\\}\\}$: $|A| = 3 \\times 6 = 18 \\implies P(A) = \\frac{18}{36} = \\frac{1}{2}$.
- Event $B = \\{d_1 \\in \\{3, 4, 5\\}\\}$: $|B| = 3 \\times 6 = 18 \\implies P(B) = \\frac{18}{36} = \\frac{1}{2}$.
- Event $C = \\{d_1 + d_2 = 9\\}$: Pairs summing to 9 are $\\{(3, 6), (4, 5), (5, 4), (6, 3)\\} \\implies |C| = 4 \\implies P(C) = \\frac{4}{36} = \\frac{1}{9}$.

- **Step 1: Check the 3-Way Product Condition:**  
  $$P(A) \\cdot P(B) \\cdot P(C) = \\left(\\frac{1}{2}\\right) \\left(\\frac{1}{2}\\right) \\left(\\frac{1}{9}\\right) = \\frac{1}{36}$$
  Now examine the intersection $A \\cap B \\cap C$:
  - $A \\cap B = \\{d_1 = 3\\}$.
  - For $d_1 + d_2 = 9$ with $d_1 = 3$, we must have $d_2 = 6$.
  Thus, $A \\cap B \\cap C$ contains exactly one elementary outcome:
  $$A \\cap B \\cap C = \\{(3, 6)\\} \\implies P(ABC) = \\frac{1}{36}$$
  Therefore:
  $$P(ABC) = P(A)P(B)P(C) = \\frac{1}{36}$$
  The mutual product condition holds!

- **Step 2: Check Pairwise Independence for All Pairs:**  
  1. **Pair $(A, B)$:**  
     $A \\cap B = \\{d_1 = 3\\} \\implies |A \\cap B| = 6 \\implies P(A \\cap B) = \\frac{6}{36} = \\frac{1}{6}$.  
     Product: $P(A)P(B) = \\frac{1}{2} \\times \\frac{1}{2} = \\frac{1}{4}$.  
     Since $\\frac{1}{6} \\neq \\frac{1}{4}$, $A$ and $B$ are **dependent**.
  2. **Pair $(A, C)$:**  
     $A \\cap C = \\{(d_1, d_2) \\in C : d_1 \\in \\{1, 2, 3\\}\\} = \\{(3, 6)\\} \\implies P(A \\cap C) = \\frac{1}{36}$.  
     Product: $P(A)P(C) = \\frac{1}{2} \\times \\frac{1}{9} = \\frac{1}{18} = \\frac{2}{36}$.  
     Since $\\frac{1}{36} \\neq \\frac{1}{18}$, $A$ and $C$ are **dependent**.
  3. **Pair $(B, C)$:**  
     $B \\cap C = \\{(d_1, d_2) \\in C : d_1 \\in \\{3, 4, 5\\}\\} = \\{(3, 6), (4, 5), (5, 4)\\} \\implies P(B \\cap C) = \\frac{3}{36} = \\frac{1}{12}$.  
     Product: $P(B)P(C) = \\frac{1}{2} \\times \\frac{1}{9} = \\frac{1}{18}$.  
     Since $\\frac{1}{12} \\neq \\frac{1}{18}$, $B$ and $C$ are **dependent**.

*Theoretical Significance:* This classic counterexample proves that the 3-way product identity $P(ABC) = P(A)P(B)P(C)$ does **not** imply pairwise independence, reinforcing why mutual independence requires checking all sub-collection equations.

**Answer.**  
$P(ABC) = \\frac{1}{36} = P(A)P(B)P(C)$, but $P(AB) = \\frac{1}{6} \\neq \\frac{1}{4}$, $P(AC) = \\frac{1}{36} \\neq \\frac{1}{18}$, and $P(BC) = \\frac{1}{12} \\neq \\frac{1}{18}$. No pair is independent.

---
"""

with open(OUTPUT_PATH, "a", encoding="utf-8") as f:
    f.write(section_c2)
print("Section C.2 appended.")
