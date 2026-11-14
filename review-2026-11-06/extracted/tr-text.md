## Question 1

A group of researchers conducted a study to examine the relationship between smoking history and the incidence of cardiovascular (heart) disease.

At the beginning of the study, 45% of the participants reported having a smoking history, while the remaining 55% reported no smoking history. After a five-year follow-up, the incidence rates of cardiovascular disease among individuals with and without a smoking history were 35% and 15%, respectively.

Let T denote the event that a participant has a history of smoking, and let R denote the event where a participant developed cardiovascular disease.

We are given:

- P ( T ) = 0 . 45
- P ( T c ) = 0 . 55
- P ( R | T ) = 0 . 35
- P ( R | T c ) = 0 . 15
- (a) (5 pts) Represent the following events using appropriate notation in terms of T and R , and calculate their corresponding probabilities:
- (i) A randomly selected individual reported having a smoking history but did not develop cardiovascular disease.
- (ii) A randomly selected individual developed cardiovascular disease.
- (b) (3 pts) Are smoking history ( T ) and the development of cardiovascular disease ( R ) independent? Justify your reasoning based on the context and show numerically.
- (c) (5 pts) Suppose we take a random sample of 10 participants who developed cardiovascular disease and want to find the probability that the majority of these individuals had a smoking history. You may assume that the number of participants is su ! ciently large that the proportions are relatively unchanged with a random sample of size 10.
- (i) Define an appropriate random variable.
- (ii) What probability distribution would be an appropriate model in this situation? Include any parameter(s) and justify your answer.
- (iii) Write down, but do not calculate, the expression used to calculate the probability of interest.

## TR Midterm

Questions Only

October 24, 2025

## Question 2

The format of standard Ontario passenger vehicle license plates is an alphanumeric sequence of four letters, followed by three numbers (e.g., ABCD 012). All letters (A-Z) and numbers (0-9) are possible and there can be repeated letters and/or numbers.

Suppose an alphanumeric sequence is generated at random in the format of standard Ontario passenger vehicle license plates. Define events A and B as follows:

- A = no repeated letters nor numbers
- B = letters and numbers both show in strictly increasing order (e.g., ABCD 123, but not ABBD 111 nor DBBA 321)
- (a) (2 pts) How many alphanumeric sequences are possible for a standard Ontario license plate?
- (b) (3 pts) Compute P ( A ).
- (c) (4 pts) Use probability axioms (not probability calculations) to show that P ( B ) &lt; P ( A ). Be sure to state which axiom(s) you use.

## Question 3

The time (in weeks) a certain variety of apple takes to spoil at room temperature follows the following probability density function (PDF):

<!-- formula-not-decoded -->

- (a) (i) Briefly describe (in words) what the 90th percentile represents in this context.
- (ii) The following plot displays this PDF. Sketch the 90th percentile on this plot and briefly justify your reasoning.

[公式或图像请见原页面]

x

## Question 2

The format of standard Ontario passenger vehicle license plates is an alphanumeric sequence of four letters, followed by three numbers (e.g., ABCD 012). All letters (A–Z) and numbers (0–9) are possible and there can be repeated letters and/or numbers.

Suppose an alphanumeric sequence is generated at random in the format of standard Ontario passenger vehicle license plates. Define events A and B as follows:

- A = no repeated letters nor numbers
- B = letters and numbers both show instrictly increasing order (e.g., ABCD 123, but not ABBD 111 nor DBBA 321)
- (a) (2 pts) How many alphanumeric sequences are possible for a standard Ontario license plate?
- (b) (3 pts) Compute P(A).
- (c) (4 pts) Use probability axioms (not probability calculations) to show that P(B) &lt; P(A). B sure to state which axiom(s) you use.
- (b) (2 pts) Determine the average time it takes this variety of apple to spoil at room temperature as a function of k .
- (c) (2 pts) What value of k makes f ( x ) a valid PDF?
- (d) (7 pts) Suppose the variance of X is 0 . 4294.
- (i) Find a bound on the probability P (1 . 55 → X → 2 . 8) using Chebyshev's inequality.
- (ii) Find the actual probability P (1 . 55 → X → 2 . 8) using the information given in this question.
- (iii) Compare the values in (i) and (ii). Which one is more accurate? Briefly explain in 2-3 sentences.

[公式或图像请见原页面]

[公式或图像请见原页面]

## Question 4

Consider the following experiment: we first toss a fair coin.

- If the coin lands tails, X takes the value of 0.
- If the coin lands heads, we roll a fair, six-sided die and X is the result of the die roll. The die is numbered 1 through 6.
- (a) (3 pts) Derive the probability mass function (PMF) of X .
- (b) (2 pts) Let F ( x ) denote the cumulative distribution function (CDF) of X . Find F (2 . 5). You do not need to derive the complete CDF F ( x ) here.
- (c) (3 pts) The expected value of X is 1.75. Calculate the variance of X .

## Question 5

The code snippet below is meant to simulate the random experiment of rolling three fair dice and observing the product of the result of each die. The prod function takes the product of all elements in a vector (e.g., prod(c(1, 2, 3)) returns 3 · 2 · 1 = 6):

```
product <- c() for (i in 1:100){ x <- sample(1:10, 3, replace = T) product[i] <- prod(x) }
```

- (a) (1 pt) How many simulations are being implemented? 100

.

- (b) (1 pt) What are the smallest and largest possible outcomes from this random experiment?

<!-- formula-not-decoded -->

- (c) (2 pts) Following this simulation, how would you produce the estimated probability of getting a result of 504 in R? Describe in words and reference any object names in the code snippet, or write using R syntax. co/ 1 ( s == tpud) s
- (d) (2 pts) What would happen to the estimate you described in (c) if the simulation size was 10 times larger? Explain how you know.

[公式或图像请见原页面]