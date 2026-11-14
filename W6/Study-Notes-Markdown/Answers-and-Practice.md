# STA237 Week 6 Answers and Practice

Use this file with the [Study Notes](Study-Notes.md). All question statements are **faithful paraphrases** preserving their data, conditions, subparts, and tasks; teaching-example statements are in the Study Notes. Basic / Medium / Test Level labels come from the user's screenshot; no new difficulty labels are assigned to lecture questions. Numerical values are generally rounded to six decimal places; exact expressions take priority.

## Contents

- [A. Problem Type Teaching-Example Solutions](#teaching-solutions)
- [B. Lecture Source Questions and Solutions](#lecture-solutions)
- [C. Requested Textbook Exercises and Solutions](#textbook-solutions)
- [D. Source-Based Self-Test Index](#self-test)
- [E. Coverage and Unresolved-Items Appendix](#coverage)

<a id="teaching-solutions"></a>

## A. Problem Type Teaching-Example Solutions

<a id="a01"></a>

### Problem Type PT-01: Fixed-Trial Success Counts

**Question reference:** [PT-01 source question](Study-Notes.md#pt01), slides 5–6, PDF pp6–7, telephone warranties.

**Worked solution.** Let $R$ count the telephones, among 10, that must be replaced. A telephone must first be submitted for service and then classified as requiring replacement:

$$
p=P(\text{service})P(\text{replacement}\mid\text{service})=0.2(0.4)=0.08.
$$

Under the independent, identically distributed model used in class, $R\sim\operatorname{Bin}(10,0.08)$.

$$
P(R=2)=\binom{10}{2}(0.08)^2(0.92)^8=0.1478070355.
$$

$$
P(R\le2)=\sum_{j=0}^{2}\binom{10}{j}(0.08)^j(0.92)^{10-j}
=0.9599245803.
$$

$$
P(R\ge3)=1-P(R\le2)=0.0400754197,\qquad E(R)=10(0.08)=0.8.
$$

**Answer.** Exactly 2: **0.147807**; at most 2: **0.959925**; at least 3: **0.040075**; long-run average replacements per batch of 10: **0.8 telephones**. An expected value need not equal an integer observed in a particular batch.

**Check.** The final two probabilities are complements and sum to 1. R commands: `dbinom(2,10,.08)`, `pbinom(2,10,.08)`, and `1-pbinom(2,10,.08)`.

<a id="a02"></a>

### Problem Type PT-02: Minimum Trials for At Least One Success

**Question reference:** [PT-02 source question](Study-Notes.md#pt02), slide 7, PDF p8, hospital backup generators.

**Worked solution.** There are $n$ independent generators, each failing with probability $0.3$. The system fails if and only if every generator fails:

$$
1-0.3^n\ge0.995
\iff 0.3^n\le0.005
\iff n\ge\frac{\log(0.005)}{\log(0.3)}\approx4.4007.
$$

The last step divides by a negative number, reversing the inequality. The smallest integer is $n=5$.

**Answer.** Install at least **5 generators**. Check: with 4, reliability is $1-0.3^4=0.9919<0.995$; with 5, it is $1-0.3^5=0.99757\ge0.995$.

<a id="a03"></a>

### Problem Type PT-03: Derive Stated Means and Variances

**Question reference:** [PT-03 source question](Study-Notes.md#pt03), slide 3's Bernoulli "show" task.

**Worked solution.** $P(I=0)=1-p$ and $P(I=1)=p$. By the definition of discrete expectation,

$$
E(I)=0(1-p)+1p=p,\qquad
E(I^2)=0^2(1-p)+1^2p=p.
$$

Therefore,

$$
\operatorname{Var}(I)=E(I^2)-[E(I)]^2=p-p^2=p(1-p).
$$

**Answer.** $E(I)=p$ and $\operatorname{Var}(I)=p(1-p)$. At $p=0,1$, the variable is constant with variance 0, consistent with the formulas.

<a id="a04"></a>

### Problem Type PT-04: First-Success Waiting and Counting Conventions

**Question reference:** [PT-04 source question](Study-Notes.md#pt04), PAR Basic #5.4(a–c), printed p218, PDF p237.

**Worked solution.** The textbook's $X$ counts total trials, $X=1,2,\ldots$, with PMF $0.7^{x-1}0.3$. R's variable $F=X-1$ counts failures.

| Part | Mathematical calculation and event conversion | Suitable R command | Result |
| --- | --- | --- | --- |
| (a) | $P(X=3)=0.7^2(0.3)$ | `dgeom(2,.3)` | $0.147$ |
| (b) | $2\le X<9\iff1\le F\le7$; probability $0.7-0.7^8$ | `pgeom(7,.3)-pgeom(0,.3)` | $0.64235199$ |
| (c) | $X\ge4\iff F\ge3$; probability $0.7^3$ | `1-pgeom(2,.3)` | $0.343$ |

**Answer.** (a) **0.147000**;(b) **0.642352**;(c) **0.343000**.

**Check.** Part (b) includes seven integers, $X=2,3,\ldots,8$. `pgeom(7)` corresponds to $F\le7$, not $X\le7$. The R counting conversion needed for this requested exercise is **Supplementary — not explicitly covered in Week 6 slides**.

<a id="a05"></a>

### Problem Type PT-05: Sum Even First-Success Waiting Times

**Classification:** Supplementary — not explicitly covered in Week 6 slides. Based on the specified Basic source exercise PAR #5.2.

**Question reference:** [PT-05 source question](Study-Notes.md#pt05), PAR Basic #5.2, printed p218, PDF p237.

**Worked solution.** Let $T$ be the total rolls until the first 4, with $p=1/6$ and $q=5/6$. For $T=2j$, the first $2j-1$ rolls must fail, followed by success. Thus

$$
P(T\text{ even})=\sum_{j=1}^{\infty}q^{2j-1}p
=pq\sum_{j=0}^{\infty}(q^2)^j
=\frac{pq}{1-q^2}
=\frac{q}{1+q}=\frac5{11}.
$$

**Supplementary — not explicitly covered in Week 6 slides:** The final summation uses the geometric series from PAR §5.1. Here $q^2=25/36<1$, so it converges.

**Answer.** $\boxed{5/11\approx0.454545}$. The probability of an odd time is $6/11$; they sum to 1 and are not automatically equal.

<a id="a06"></a>

### Problem Type PT-06: Waiting for the rth Success

**Question reference:** [PT-06 source question](Study-Notes.md#pt06), PAR Basic #5.20(a–c), actual printed p220, PDF p239.

**Worked solution.** The textbook's $X$ is total trials through the third success. R uses failures $F=X-3$, with parameters `size=3, prob=.4`.

$$
P(X=x)=\binom{x-1}{2}(0.4)^3(0.6)^{x-3},\quad x=3,4,\ldots.
$$

| Part | Mathematical calculation and event conversion | R command | Result |
| --- | --- | --- | --- |
| (a) | $X=6\iff F=3$;$\binom52(.4)^3(.6)^3$ | `dnbinom(3,3,.4)` | $0.13824$ |
| (b) | $5\le X<11\iff2\le F\le7$; sum over $x=5,\ldots,10$ | `pnbinom(7,3,.4)-pnbinom(1,3,.4)` | $0.6535102464$ |
| (c) | $X\ge8\iff F\ge5$;$1-\sum_{x=3}^{7}P(X=x)$ | `1-pnbinom(4,3,.4)` | $0.419904$ |

**Answer.** (a) **0.138240**; (b) **0.653510**; (c) **0.419904**. The specific R NB functions and counting conversions needed for this exercise are **Supplementary — not explicitly covered in Week 6 slides**.

**Check.** Total trials start at 3, while R's failure count starts at 0. Every shift is by 3, not 1.

<a id="a07"></a>

### Problem Type PT-07: Without-Replacement Sample Counts

**Question reference:** [PT-07 source question](Study-Notes.md#pt07), PAR Basic #5.34(a–c), actual printed p223, PDF p242.

**Worked solution.** The population has 23 plants, including 8 marigolds. Six are selected without replacement. Therefore,

$$
P(X=x)=\frac{\binom8x\binom{15}{6-x}}{\binom{23}{6}},\quad x=0,1,\ldots,6.
$$

$$
\text{(a)}\quad P(X=3)=\frac{\binom83\binom{15}{3}}{\binom{23}{6}}
=0.2524096803.
$$

$$
\text{(b)}\quad P(X\le2)=\frac{\binom80\binom{15}{6}+\binom81\binom{15}{5}+\binom82\binom{15}{4}}{\binom{23}{6}}
=0.6661812634.
$$

$$
\text{(c)}\quad E(X)=6\frac8{23}=\frac{48}{23}=2.0869565217.
$$

**Answer.** (a) **0.252410**; (b) **0.666181**; (c) **48/23, approximately 2.086957 plants**. Check: the support is 0–6, the PMF sums to 1 over that support, and the mean lies within it.

<a id="a08"></a>

### Problem Type PT-08: Compare Exact Sampling with a Binomial Approximation

**Question reference:** [PT-08 source question](Study-Notes.md#pt08), slides 16–17 Case 2, PDF pp17–18.

**Worked solution.** $N=5000,K=500,n=10$. Let $D$ count sampled defectives. The exact model is Hypergeometric:

$$
P(D\ge3)=1-\sum_{j=0}^{2}
\frac{\binom{500}{j}\binom{4500}{10-j}}{\binom{5000}{10}}
=0.0700011561.
$$

Removing 10 products barely changes the population proportions, so use $B\sim\operatorname{Bin}(10,0.1)$ as an approximation:

$$
P(D\ge3)\approx P(B\ge3)
=1-\sum_{j=0}^{2}\binom{10}{j}(0.1)^j(0.9)^{10-j}
=0.0701908264.
$$

**Answer.** Exact: **0.070001**; approximate: **0.070191**. The approximation is about **0.000190** higher. Actual sampling remains without replacement; the exact model has not changed.

<a id="a09"></a>

### Problem Type PT-09: Poisson Interval Count Probabilities

**Question reference:** [PT-09 source question](Study-Notes.md#pt09), MMSA Basic #91(a–d), actual printed p162, PDF p174.

**Worked solution.** $X\sim\operatorname{Pois}(20)$ and $\sigma=\sqrt{20}$. Write $F(k)=\sum_{j=0}^{k}e^{-20}20^j/j!$.

| Part | Event and calculation | Result |
| --- | --- | --- |
| (a) At most 10 | $F(10)$ | $0.0108117188$ |
| (b) More than 20 | $1-F(20)$ | $0.4409074158$ |
| (c) Including endpoints | $F(20)-F(9)$ | $0.5540971719$ |
| (c) Excluding endpoints | $F(19)-F(10)$ | $0.4594455480$ |
| (d) Within 2 standard deviations | $F(28)-F(11)$ | $0.9442796565$ |

For part (d),

$$
20-2\sqrt{20}\le X\le20+2\sqrt{20}
\iff11.0557\ldots\le X\le28.9443\ldots
\iff12\le X\le28.
$$

**Answer.** In order: **0.010812, 0.440907, 0.554097, 0.459446, 0.944280**.

**Check.** The inclusive and exclusive probabilities differ by $P(X=10)+P(X=20)$. The standard-deviation interval includes integers 12–28; do not extend it outward to 11–29.

<a id="a10"></a>

### Problem Type PT-10: Assess a Poisson Count Model

**Question reference:** [PT-10 source question](Study-Notes.md#pt10), slide 26(a), PDF p27.

**Worked solution.** The variable is the total trees in a fixed area. A Poisson model can be a simplification if average density is approximately stable across the region, counts in disjoint small regions are approximately independent, and trees do not coincide at exactly the same location.

However, seed dispersal may cause clustering, competition for light and water may cause repulsion, and soil or terrain may change density. An average of 6 trees per 100 square metres alone does not establish these conditions.

**Answer.** **It may be a useful model under suitable assumptions, but the mean alone does not establish applicability.** Discuss stable density and independence across regions. The slide's no-coincidence condition does not mean the whole region can contain at most one tree.

<a id="a11"></a>

### Problem Type PT-11: Obtain the Poisson PMF from a Binomial Limit

**Question reference:** [PT-11 source question](Study-Notes.md#pt11), slides 21–23, PDF pp22–24.

**Worked solution.** Let $I_i$ indicate a sighting in subinterval $i$, so $P(I_i=1)=p$ and $P(I_i=0)=1-p$. Each subinterval is 0/1 in the lecture construction. The daily count is $D_n=\sum_{i=1}^{n}I_i\sim\operatorname{Bin}(n,p)$, giving $E(D_n)=np$.

The daily mean is fixed at $\lambda$, so $np=\lambda$ and $p=\lambda/n$. As $n\to\infty$, $p\to0$, while their product stays fixed. For fixed $d\in\mathbb Z_{\ge0}$ and sufficiently large integers $n>\lambda$ and $n\ge d$,

$$
\begin{aligned}
P(D_n=d)
&=\binom nd\left(\frac\lambda n\right)^d\left(1-\frac\lambda n\right)^{n-d}\\
&=\frac{\lambda^d}{d!}
\left[\prod_{j=0}^{d-1}\left(1-\frac jn\right)\right]
\left(1-\frac\lambda n\right)^n
\left(1-\frac\lambda n\right)^{-d}.
\end{aligned}
$$

For the second line, expand $n!/(n-d)!$ into $n(n-1)\cdots(n-d+1)$ and divide each factor by $n$ using the denominator $n^d$. Also split the power $n-d$ into powers $n$ and $-d$. See [C-05's step-by-step derivation](Study-Notes.md#poisson-limit) for the factorial cancellation and product notation.

Because $d$ is fixed, the bracket is a finite product of factors tending to 1, and the final power $-d$ also tends to 1. Apply slide 23's limit $\lim_{n\to\infty}(1+c/n)^n=e^c$ with $c=-\lambda$ to obtain $e^{-\lambda}$ for the middle factor. A base tending to 1 does not mean its $n$th power tends to 1.

**Answer.**

$$
\lim_{n\to\infty}P(D_n=d)=e^{-\lambda}\frac{\lambda^d}{d!},
\quad d=0,1,2,\ldots.
$$

**Check.** When $d=0$, the Binomial zero-success probability gives $(1-\lambda/n)^n\to e^{-\lambda}$, agreeing with the resulting PMF's $d=0$ term. The empty product and $0!$ both equal 1. Where the slides use $D$ for both a subinterval and the full day, separate symbols $I_i,D_n$ avoid ambiguity.

<a id="lecture-solutions"></a>

## B. Lecture Source Questions and Solutions

The following **13 lecture-task groups** combine complete activities/tasks across pages without counting the same question twice. All available subparts are retained; teaching examples link to their unique complete solutions.

<a id="l01"></a>

### L01 — Bernoulli moments

**Source:** slide 3, PDF p3, handwritten "Show that" task; **PT-03**.

**Question, faithful paraphrase:** Prove the mean and variance of a Bernoulli success indicator. See [A03](#a03) for the full derivation.

<a id="l02"></a>

### L02 — Binomial mean from indicators and from the definition

**Source:** slide 4, PDF p4, and the immediately following handwritten insert at PDF p5; **PT-03**.

**Question, faithful paraphrase:** Express $X\sim\operatorname{Bin}(n,p)$ as a sum of Bernoulli variables. The handwritten insert specifically asks for $E(X)$ from its definition. Verify the variance relationship also stated in the lecture.

**Worked solution.** If $X=\sum_{i=1}^{n}I_i$, with independent Bernoulli$(p)$ variables $I_i$, then

$$
E(X)=\sum_iE(I_i)=np,\qquad
\operatorname{Var}(X)=\sum_i\operatorname{Var}(I_i)=np(1-p).
$$

Starting from the definition, for $n\ge1$, use $x\binom nx=n\binom{n-1}{x-1}$:

$$
\begin{aligned}
E(X)&=\sum_{x=1}^{n}x\binom nx p^xq^{n-x}\\
&=np\sum_{x=1}^{n}\binom{n-1}{x-1}p^{x-1}q^{n-x}\\
&=np\sum_{y=0}^{n-1}\binom{n-1}{y}p^yq^{(n-1)-y}=np.
\end{aligned}
$$

The final sum is the sum of a Binomial$(n-1,p)$ PMF, hence 1. Recognizing that PMF is the handwritten insert's main strategy. When $n=0$, $X=0$ and the result still holds.

<a id="l03"></a>

### L03 — Example 1: warranty replacements

**Source:** slides 5–6, PDF pp6–7, identified as MMSA #71; **PT-01**.

**Question and all parts:** Of telephones purchased, 20% need service and 40% of those need replacement. For 10 telephones, find the probabilities of exactly 2, at most 2, and at least 3 replacements, plus the expected replacement count. The statement and unique complete solution are in [PT-01](Study-Notes.md#pt01) and [A01](#a01). This is a lecture question, outside the screenshot's 25 requested textbook exercises.

<a id="l04"></a>

### L04 — Example 2: backup generators

**Source:** slide 7, PDF p8; **PT-02**. The handwritten "Test level" label is retained from the slide.

**Question:** Identical independent generators each fail with probability 0.3. Find the minimum number giving at least a 0.995 probability that one or more work. See [PT-02](Study-Notes.md#pt02) and [A02](#a02) for the statement and unique solution: **5 generators**.

<a id="l05"></a>

### L05 — Activity: First Holy Grail Labubu

**Source:** slides 8–9, PDF p9–10; **PT-04**.

**Question, faithful paraphrase:** Each box contains the target HG with probability 5%; stop at the first HG. (a) Identify whether HG count and box count are fixed or random, and whether boxes can be modeled as independent Bernoulli trials. (b) If the first HG is in box 10, draw the success/failure sequence and give its probability. (e) Generalize to the PMF of $X$, the boxes opened before success, and state its smallest and largest possible values. Unavailable parts (c–d) are recorded under [source gaps](#source-gaps); their wording is not reconstructed.

**Worked solution and answers.**

- (a)(i) The HG count is fixed at 1; (ii) the box count is random; (iii) under the lecture model, boxes are independent Bernoulli trials with fixed success probability.
- (b) The sequence is `FFFFFFFFFS`: nine failures followed by success on trial 10. If $T$ counts total boxes and $X=T-1$ counts failures, then $P(T=10)=P(X=9)=0.95^9(0.05)=\boxed{0.0315124705}$.
- (e) $P(X=x)=0.95^x(0.05)$ for $x=0,1,\ldots$. The minimum is 0; there is no finite maximum. For total trials $T$, support starts at 1 and the PMF is $0.95^{t-1}(0.05)$.

**Check.** "Before" excludes the successful box; using $X=10$ shifts the event by one. Independence is a model assumption, not a consequence of equal marginal probabilities.

<a id="l06"></a>

### L06 — Geometric PMF, moments, and alternative variable

**Source:** slide 10, PDF p11, PMF/variable blanks and explicit "show this" task; **PT-03, PT-04**.

**Question, faithful paraphrase:** For independent, identically distributed Bernoulli trials, define failures before the first success, state the PMF, and prove its mean and variance. Identify which trial/success/failure counts are fixed, then convert to a total-trials variable.

**Worked solution.** $F=f$ means exactly $f$ initial failures followed by success, so $P(F=f)=q^fp$, $f\ge0$. Total trials and failures are random; successes are fixed at 1.

**Supplementary — not explicitly covered in Week 6 slides:** The following differentiated-series steps from PAR §5.1 provide a calculation tool for the lecture's "show this" task, without establishing another PT. For $0\le q<1$, start from $G(q)=\sum_{f=0}^{\infty}q^f=(1-q)^{-1}$ to obtain

$$
\sum f q^f=qG'(q)=\frac{q}{(1-q)^2},\qquad
\sum f^2q^f=q\frac{d}{dq}[qG'(q)]=\frac{q(1+q)}{(1-q)^3}.
$$

Differentiating $q^f$ gives $fq^{f-1}$; multiplying by $q$ restores $fq^f$, the term needed for expectation. Differentiating that result and multiplying by $q$ gives $f^2q^f$, needed for the second moment. Both sums run from $f=0$ to infinity, with zero contribution at $f=0$. These power series can be differentiated term by term for $|q|<1$; $q=0$ can also be checked directly using certain success on the first trial.

Since $P(F=f)=pq^f$, multiply the two sums by $p=1-q$ to obtain $E(F)$ and $E(F^2)$:

$$
E(F)=\frac qp,\quad E(F^2)=\frac{q(1+q)}{p^2},\quad
\operatorname{Var}(F)=\frac{q(1+q)-q^2}{p^2}=\frac q{p^2}.
$$

**Answer.** $T=F+1$, so $P(T=t)=q^{t-1}p$, $E(T)=1/p$, and $\operatorname{Var}(T)=q/p^2$. At $p=1$, $F=0,T=1$, consistent with the formulas.

<a id="l07"></a>

### L07 — Activity: Three More Holy Grail Labubus

**Source:** slides 11–13, PDF pp12–14, including the extra handwritten question on slide 13; **PT-01, PT-06**.

**Question, faithful paraphrase:** You already own an HG and want three more. Each independent box still has success probability 0.05. (a) Buy exactly 10 boxes; let $Y$ count HGs and give its model and parameters. (b) Write the probability of $A=\{\text{2 HGs among 10 boxes}\}$. (c) Give three possible sequences for $B=\{\text{10 boxes opened before finding the third HG}\}$; identify total boxes, the last outcome, the earlier HG count, and whether the earlier order is fixed. (d) Compare $A,B$, write $P(B)$, and identify fixed/random quantities under the stopping rule. Extra handwritten question: what is the probability of finding the fifth HG in 15 boxes?

**Worked solution.**

- (a) $Y\sim\operatorname{Bin}(10,0.05)$ because exactly 10 boxes are bought.
- (b) $P(A)=\binom{10}{2}(0.05)^2(0.95)^8=\boxed{0.0746347985}$.
- (c) Three possible sequences for $B$ are `SSFFFFFFFFS`, `SFSFFFFFFFS`, and `FFSSFFFFFFS`. Each has 11 boxes, exactly two successes among the first 10, and a final success. Answers: (i) 11 boxes; (ii) True; (iii) two earlier HGs; (iv) No, success positions among the first 10 are not fixed.
- (d) Event $B$ is event $A$ in the first 10 boxes followed by success, so $P(B)=P(A)(0.05)=\binom{10}{2}(0.05)^3(0.95)^8=\boxed{0.0037317399}$. Across the full experiment that stops at three successes, the success count is fixed at 3, total boxes are random, Bernoulli trials are independent, and the final box must contain the third success. This is consistent with the particular event $B$ specifying 11 total boxes.

**Extra handwritten question: solution.** Trial 15 is the fifth success, so the first 14 trials must contain four successes:

$$
P(T_5=15)=\binom{14}{4}(0.05)^5(0.95)^{10}
=\boxed{0.0001872924}.
$$

Multiply the probability for the first 14 boxes by the final success factor $0.05$. The source-formula check is recorded under [source corrections](#source-corrections).

<a id="l08"></a>

### L08 — Negative binomial PMF, moments, and alternative variable

**Source:** slide 14, PDF p15, including "show this" and the handwritten geometric-sum relationship; **PT-03, PT-06**.

**Question, faithful paraphrase:** Define total trials through the $r$th success; state its PMF and support; prove its mean and variance; identify fixed counts; and convert to failures.

**Worked solution.** If $T_r=t$, the first $t-1$ trials contain exactly $r-1$ successes and the final trial succeeds. Hence

$$
P(T_r=t)=\binom{t-1}{r-1}p^rq^{t-r},\quad t=r,r+1,\ldots.
$$

In an independent Bernoulli sequence, let $G_1,\ldots,G_r$ be successive waiting times between successes, counting total trials. They are independent geometric variables, and $T_r=\sum_iG_i$ (slide 14 annotation). Therefore,

$$
E(T_r)=r/p,\qquad \operatorname{Var}(T_r)=rq/p^2.
$$

**Answer.** Total trials are random, successes are fixed at $r$, and failures are random. If $F_r=T_r-r$, then

$$
P(F_r=f)=\binom{f+r-1}{r-1}p^rq^f,\quad f=0,1,\ldots,
\qquad E(F_r)=rq/p,\quad\operatorname{Var}(F_r)=rq/p^2.
$$

Check $r=1$ to recover both geometric conventions; with $p=1$, total trials are fixed at $r$.

<a id="l09"></a>

### L09 — Hypergeometric formula and support blanks

**Source:** slides 15 and 18, PDF pp16 and 19. **Concept:** C-04. These formula blanks do not establish a separate PT.

**Question, faithful paraphrase:** In a finite population of size $N$ with $K$ target objects, draw $n$ without replacement. Complete the count PMF, support, mean, and variance, and give an approximation for a large population. Slide 18's annotated diagram uses $N=20,K=8,n=15$ to illustrate support.

**Answer and reasoning.** Choose $x$ target objects and $n-x$ nontarget objects separately:

$$
P(X=x)=\frac{\binom Kx\binom{N-K}{n-x}}{\binom Nn},
\quad\max(0,n-(N-K))\le x\le\min(n,K).
$$

The lecture moments are $E(X)=nK/N$ and $\operatorname{Var}(X)=n(K/N)(1-K/N)(N-n)/(N-1)$. The diagram gives $3\le X\le8$: a sample of 15 can contain at most 12 nontarget objects. When the population is sufficiently large relative to the sample, approximate using $\operatorname{Bin}(n,K/N)$, while noting that actual sampling remains without replacement.

<a id="l10"></a>

### L10 — Warehouse Case 1 and Case 2

**Source:** slides 16–17, PDF p17–18; **PT-07, PT-08**.

**Question, faithful paraphrase:** In (1) a population of $N=50$ and (2) a population of $N=5000$, 10% are defective. Randomly draw 10 without replacement. Find the probability of at least three defectives, and consider the fixed-success-probability approximation for Case 2.

**Case 1.** $K=5$, so $D$ can take only values 0–5:

$$
P(D\ge3)=\frac{\binom53\binom{45}{7}+\binom54\binom{45}{6}+\binom55\binom{45}{5}}{\binom{50}{10}}
=\boxed{0.0482603032}.
$$

Equivalently, use $1-\sum_{j=0}^{2}\binom5j\binom{45}{10-j}/\binom{50}{10}$; both calculations agree.

**Case 2.** See [A08](#a08): exact probability **0.0700011561**, Binomial approximation **0.0701908264**. The cases have the same target proportion but different sampling fractions, giving different exact tail probabilities.

<a id="l11"></a>

### L11 — Shiba modeling and small-interval construction

**Source:** slides 20–22, PDF p21–23; **PT-10, PT-11**.

**Question, faithful paraphrase:** How does counting Shibas seen in one day differ from a Binomial setting? Divide the day into $n$ independent 0/1 subintervals, complete their probabilities and the daily model/expectation, and describe changes to $p$ and $n$ when the daily mean stays fixed.

**Worked solution.** Counting sightings in one day does not begin with a specified finite number of Bernoulli trials or a fixed upper bound. The question "Was any Shiba seen that day?" defines a different Bernoulli indicator, which cannot replace the count.

The subinterval indicator $I_i$ has probabilities $p,1-p$ for 1/0; the lecture construction sets $P(I_i>1)=0$. The daily count satisfies $D_n\sim\operatorname{Bin}(n,p)$ and $E(D_n)=np=\lambda$, hence $p=\lambda/n$. Increasing $n$ decreases $p$ while keeping $np$ fixed. Slide 22 illustrates $\lambda=10$ per day: 24 one-hour intervals use $p=10/24$, and 48 half-hour intervals use $p=10/48$. These illustrate finer subdivisions; they do not verify independence of real sightings.

<a id="l12"></a>

### L12 — Derive the Poisson PMF

**Source:** slide 23, PDF p24; **PT-11**.

**Question:** In this construction, let $n\to\infty,p\to0,np=\lambda$ and find the limiting count PMF for fixed $d$. See [A11](#a11) for the factor-by-factor derivation, giving $e^{-\lambda}\lambda^d/d!$ for $d\ge0$.

<a id="l13"></a>

### L13 — Example 3: trees in a forest

**Source:** slide 26, PDF p27; **PT-10, PT-09**.

**Question, faithful paraphrase:** There are on average 6 trees per $100\,\mathrm{m}^2$. (a) Discuss the Poisson assumptions. (b) Find the probability of at least one tree in $100\,\mathrm{m}^2$. (c) Find the probability of exactly 10 trees in $300\,\mathrm{m}^2$.

**(a)** See [A10](#a10) for the full discussion. The following calculations assume this model.

**(b)** $T_1\sim\operatorname{Pois}(6)$:

$$
P(T_1\ge1)=1-e^{-6}=\boxed{0.9975212478}.
$$

**(c)** Tripling the area gives $T_2\sim\operatorname{Pois}(18)$:

$$
P(T_2=10)=e^{-18}\frac{18^{10}}{10!}=\boxed{0.0149851586}.
$$

**Check.** $\mu$ is the mean for the selected area, not a parameter that stays unchanged as the area changes.

<a id="textbook-solutions"></a>

## C. Requested Textbook Exercises and Solutions

Exercise identities follow the screenshot; actual locations were checked in the PDFs. MMSA uses chapter-wide numbers such as `#91`; PAR uses full numbers such as `#3.26`. The five textbook exercises selected as teaching examples retain their locators and subpart lists here and link to unique solutions. The sixth Basic exercise, PAR #3.26, is solved fully in this section.

### MMSA #91 — Basic Practice

**Source:** §3.6, actual printed p162, PDF p174 (screenshot: p163); **PT-09**.

**Question:** $X\sim\operatorname{Pois}(20)$ counts drivers. Find (a) at most 10; (b) more than 20; (c) 10–20 inclusive and strictly between them; (d) within two standard deviations of the mean. See [PT-09](Study-Notes.md#pt09) and [A09](#a09) for the full paraphrase and all solutions.

<a id="m93"></a>

### MMSA #93 — Medium Practice

**Source:** §3.6, actual printed p162, PDF p174 (screenshot: p163). Calculation components use **PT-01, PT-09**; the numerical approximation comparison itself has **No matching Basic/slide PT — retained as a requested exercise**. No PT is added.

**Question, faithful paraphrase:** Metal-on-plastic implants have a five-year failure rate of 1.7%. For 200 randomly selected implants, use both an exact Binomial calculation and a Poisson approximation to find (a) exactly three failures and (b) at most three failures. Use independent outcomes with the same failure probability.

**Worked solution.** $X\sim\operatorname{Bin}(200,0.017)$; approximate with $Z\sim\operatorname{Pois}(200\cdot0.017)=\operatorname{Pois}(3.4)$.

$$
\text{(a)}\quad P(X=3)=\binom{200}{3}(.017)^3(.983)^{197}=\boxed{0.2201845232},
$$

$$
P(X=3)\approx P(Z=3)=e^{-3.4}\frac{3.4^3}{3!}=\boxed{0.2186171671}.
$$

$$
\text{(b)}\quad P(X\le3)=\sum_{j=0}^{3}\binom{200}{j}(.017)^j(.983)^{200-j}=\boxed{0.5576091436},
$$

$$
P(X\le3)\approx e^{-3.4}\sum_{j=0}^{3}\frac{3.4^j}{j!}=\boxed{0.5583570553}.
$$

**Check.** Both models have the same mean; the approximation does not change the actual experiment into continuous-interval counting. The approximation is explicitly covered on slide 24 and is Core.

<a id="m94"></a>

### MMSA #94 — Medium Practice

**Source:** §3.6, actual printed p162, PDF p174 (screenshot: p163); calculation components use **PT-01, PT-09**. The comparison does not expand the PT inventory.

**Question, faithful paraphrase:** Of a particular type of computer, 0.10% experience CPU failure under warranty. Consider 10000 computers. Find (a) the expected failure count and its standard deviation; (b) the approximate probability of more than 10 failures; (c) the approximate probability of no failures.

**Worked solution.** $X\sim\operatorname{Bin}(10000,0.001)$. Note that 0.10% equals 0.001, not 0.10.

$$
\text{(a)}\quad E(X)=10,\quad\operatorname{SD}(X)=\sqrt{10000(.001)(.999)}=\sqrt{9.99}=\boxed{3.1606961259}.
$$

Approximate with $Z\sim\operatorname{Pois}(10)$ (slide 24, Core):

$$
\text{(b)}\quad P(X>10)\approx1-e^{-10}\sum_{j=0}^{10}\frac{10^j}{j!}=\boxed{0.4169602498};
$$

$$
\text{(c)}\quad P(X=0)\approx e^{-10}=\boxed{0.00004539993}.
$$

**Check.** Part (a) uses the exact Binomial standard deviation; do not present the approximate $\sqrt{10}$ as exact. In (b), "more than" starts at 11.

<a id="m101"></a>

### MMSA #101 — Test Level

**Source:** §3.6, printed p163, PDF p175. Count probabilities use **PT-09**; part (c), solving for continuous time, has **No matching Basic/slide PT — retained as a requested exercise**. It does not broaden PT-02's integer-trial task.

**Question, faithful paraphrase:** Structural-load occurrences follow a Poisson process with mean time 0.5 year between loads. The question supplies mean time $=1/\lambda$, where $\lambda$ is the annual rate. (a) How many loads are expected in two years? (b) What is the probability of more than five in two years? (c) How long must an interval be to make the probability of no loads at most 0.1?

**Supplementary — not explicitly covered in Week 6 slides:** Obtaining the rate from the reciprocal mean interarrival time uses the relationship supplied in this exercise. The interarrival-time distribution is not developed here.

**Worked solution.** Annual intensity is $\lambda=1/0.5=2$, so the two-year mean is 4.

$$
\text{(a)}\quad E(N_2)=\boxed{4};\qquad
\text{(b)}\quad P(N_2>5)=1-e^{-4}\sum_{j=0}^{5}\frac{4^j}{j!}=\boxed{0.2148696130}.
$$

$$
\text{(c)}\quad P(N_t=0)=e^{-2t}\le0.1
\iff t\ge\frac{\log10}{2}=\boxed{1.1512925465\text{ years}}.
$$

**Check.** At the threshold, $e^{-2t}=0.1$; longer times give a smaller probability of no loads.

<a id="m114"></a>

### MMSA #114 — Test Level

**Source:** §3.7, printed p172, PDF p184; **PT-07, PT-08**. Moment formulas are Core in C-04.

**Question, faithful paraphrase:** Of 50 industrial firms in an area, 15 violate at least one regulation. An inspector randomly visits 10. (a) Give the PMF of the number of visited firms in violation. (b) With 500 firms including 150 violators, approximate the PMF for a sample of 10 using a simpler model. (c) Calculate means and variances for the exact and approximate models in (b).

**Worked solution.**

$$
\text{(a)}\quad P(X=x)=\frac{\binom{15}{x}\binom{35}{10-x}}{\binom{50}{10}},\quad x=0,\ldots,10.
$$

**(b)** The new exact PMF is $\binom{150}{x}\binom{350}{10-x}/\binom{500}{10}$. Since the sample is a small fraction of the population, approximate by

$$
P(X=x)\approx\binom{10}{x}(0.3)^x(0.7)^{10-x},\quad x=0,\ldots,10.
$$

$$
\text{(c), exact in (b):}\quad E(X)=3,\quad
\operatorname{Var}(X)=10(.3)(.7)\frac{490}{499}=\boxed{2.0621242485}.
$$

$$
\text{(c), approximation in (b):}\quad E(X)=\boxed{3},\quad\operatorname{Var}(X)=\boxed{2.1}.
$$

**Check.** The means agree; exact variance is slightly smaller. To distinguish the original setting, part (a)'s variance is $2.1(40/49)=1.7142857143$, not the variance of the 500-firm setting requested in (c).

<a id="m118"></a>

### MMSA #118 — Test Level

**Source:** §3.7, printed p172, PDF p184; the waiting structure uses **PT-06**. Scaling paired rounds into individual rolls is local to this exercise, not another PT.

**Question, faithful paraphrase:** A rolls a fair red die and B a fair green die once each per round until five doubles (11, 22, …, 66) occur. Let $X$ be the total individual die rolls. Find its PMF, $E(X)$, and SD$(X)$.

**Worked solution.** A double has probability $6/36=1/6$ per round. Let $T$ count rounds: it is a total-trials NB variable with target 5 and probability $1/6$. Two dice are rolled per round, so $X=2T$.

$$
P(X=2t)=\binom{t-1}{4}\left(\frac16\right)^5\left(\frac56\right)^{t-5},\quad t=5,6,\ldots;
$$

All other $x$ have probability 0; odd totals are impossible.

$$
E(X)=2\frac5{1/6}=\boxed{60},\qquad
\operatorname{SD}(X)=2\sqrt{\frac{5(5/6)}{(1/6)^2}}
=\sqrt{600}=\boxed{24.4948974278}.
$$

**Supplementary — not explicitly covered in Week 6 slides:** For $X=2T$, use $\operatorname{Var}(2T)=4\operatorname{Var}(T)$ to convert counting units. Slides 10 and 14 explicitly show only shifts by constants.

**Check.** At least five rounds, or ten individual rolls, are needed. Mistaking $X$ for rounds halves both its mean and standard deviation.

<a id="m121"></a>

### MMSA #121 — Test Level

**Source:** §3.7, actual printed p173, PDF p185 (screenshot: p172); waiting model **PT-06**. Converting an interval to integer bounds uses event handling already present in PT-09.

**Question, faithful paraphrase:** A professor randomly approaches students one by one from a large population until finding 40 volunteers. Each independently volunteers with probability 25%. Find (a) the expected number approached and its standard deviation; (b) the probability this count is within one standard deviation of its mean.

**Worked solution.** Let $T$ count all students approached. Then $r=40,p=.25$ and $T\ge40$.

$$
\text{(a)}\quad E(T)=\frac{40}{.25}=\boxed{160},\quad
\operatorname{SD}(T)=\sqrt{\frac{40(.75)}{.25^2}}=\sqrt{480}=\boxed{21.9089023002}.
$$

**(b)** The interval is $160-\sqrt{480}\le T\le160+\sqrt{480}$, with integer bounds $139\le T\le181$. Thus

$$
\sum_{t=139}^{181}\binom{t-1}{39}(.25)^{40}(.75)^{t-40}
=\boxed{0.6755661232}.
$$

**Supplementary — not explicitly covered in Week 6 slides:** R check: `pnbinom(141,40,.25)-pnbinom(98,40,.25)`. The first term is $T\le181$; the subtracted term is $T\le138$. Both inputs first subtract 40 successes.

### PAR #3.23 — Medium Practice

**Source:** §3.5 exercises, printed p121, PDF p140. **No matching Basic/slide PT — retained as a requested exercise:** Inferring an unknown Poisson parameter from a probability ratio is not an established PT.

**Question, faithful paraphrase:** $X$ is Poisson with $P(X=2)=2P(X=1)$. Find $P(X=3)$.

**Supplementary — not explicitly covered in Week 6 slides:** Inferring the parameter from a probability ratio is specific to requested #3.23; it does not establish a parameter-identification PT.

**Worked solution.** For a nondegenerate parameter $\lambda>0$,

$$
\frac{P(X=2)}{P(X=1)}=\frac{\lambda}{2}=2\quad\Rightarrow\quad\lambda=4.
$$

**Answer.** $P(X=3)=e^{-4}4^3/3!=\boxed{0.1953668148}$.

**Boundary check.** If degenerate Poisson$(0)$ is allowed, the given equality also holds as $0=2\cdot0$, and the answer is 0. The textbook exercise uses the usual positive-parameter convention. Without excluding 0, the equality alone does not determine a unique answer. The convention is stated rather than silently dividing by zero.

### PAR #3.25 — Medium Practice

**Source:** §3.5 exercises, actual printed p122, PDF p141 (screenshot: p121). **No matching Basic/slide PT — retained as a requested exercise:** The parameter is inferred from a zero-count probability; the subsequent tail calculation uses PT-09.

**Question, faithful paraphrase:** The number of eggs a chicken hatches is Poisson. The probability of hatching none is 0.10. Find the probability of hatching at least two.

**Supplementary — not explicitly covered in Week 6 slides:** Solving for an unknown mean is an additional task in this exercise.

**Worked solution.** $e^{-\lambda}=0.1$, so $\lambda=\log10$;

$$
P(X\ge2)=1-P(X=0)-P(X=1)
=1-0.1(1+\log10)=\boxed{0.6697414907}.
$$

**Check.** $P(X=0)=0.1$ and $P(X=1)=0.2302585093$. Together with the tail, these three mutually exclusive probabilities sum to 1.

<a id="p326"></a>

### PAR #3.26 — Basic Practice

**Source:** §3.5 exercises, actual printed p122, PDF p141 (screenshot: p121); the second Basic source for **PT-09**.

**Question, faithful paraphrase:** A hemocytometer has 160 small squares, averaging 4.375 red blood cells per square. Find the probability that one square contains between 3 and 6 cells.

**Worked solution.** Use the homogeneous Poisson count model from this exercise's section: $X\sim\operatorname{Pois}(4.375)$. The 160 squares are not the parameter of this single-square count. Interpret "between 3 and 6" inclusively:

$$
P(3\le X\le6)=e^{-4.375}\sum_{j=3}^{6}\frac{4.375^j}{j!}=\boxed{0.6585906793}.
$$

**Check.** The target is one square, so do not multiply the mean by 160. The calculation assumes the Poisson model; a mean alone does not establish it.

### PAR #3.27 — Test Level

**Source:** §3.5 exercises, printed p122, PDF p141; the screenshot supplies no page; **PT-09**.

**Question, faithful paraphrase:** Cars pass an intersection at approximately 16 per minute. Find the probability that at least 1000 pass in the next hour. Hint: first convert to an hourly mean.

**Worked solution.** Under the Poisson model, the hourly mean is $\mu=16(60)=960$.

$$
P(X\ge1000)=1-e^{-960}\sum_{j=0}^{999}\frac{960^j}{j!}
=\boxed{0.1017568202}.
$$

**Check.** The complement is $X\le999$. Evaluate numerically using log-PMF summation or a stable survival function: do not first let $e^{-960}$ underflow to floating-point zero and then multiply by enormous powers. No Normal approximation or additional approximation topic is used.

<a id="p328"></a>

### PAR #3.28 — Test Level

**Source:** §3.5 exercises and Table 3.6, printed p122, PDF p141. **No matching Basic/slide PT — retained as a requested exercise:** Choosing a mean from frequency data and comparing observed/expected counts is not a task established by Basic/slide questions.

**Question, faithful paraphrase:** The data cover 104 baseball seasons, 1901–2004. Model the number of no-hitters per season and tabulate observed versus model-expected season counts. The complete source table gives 0–7 no-hitters with frequencies 18, 30, 21, 21, 6, 3, 3, and 2 seasons, respectively.

**Supplementary — not explicitly covered in Week 6 slides:** Choosing the Poisson parameter using a sample mean and computing expected frequencies as total seasons times model probability are modeling steps required by #3.28. No goodness-of-fit test is introduced.

**Worked solution.** Total events are $\sum kf_k=206$ across 104 seasons. Use

$$
\widehat\lambda=\frac{206}{104}=\frac{103}{52}\approx1.9807692308,
\quad X\sim\operatorname{Pois}(\widehat\lambda).
$$

For each $k$, the expected season count is $104e^{-\widehat\lambda}\widehat\lambda^k/k!$. Add an $8+$ category to account for all probability; its observed frequency is 0.

| No-hitters per season | Observed seasons | Expected seasons |
| --- | --- | --- |
| 0 | 18 | 14.348159 |
| 1 | 30 | 28.420393 |
| 2 | 21 | 28.147120 |
| 3 | 21 | 18.584316 |
| 4 | 6 | 9.202810 |
| 5 | 3 | 3.645729 |
| 6 | 3 | 1.203558 |
| 7 | 2 | 0.340567 |
| 8+ | 0 | 0.107348 |
| Total | 104 | 104.000000 |

**Answer and interpretation.** The model mean is approximately **1.980769 no-hitters per season**. It does not reproduce the observed frequencies exactly; high-count seasons are more common in the observations. This table provides a comparison, not proof of the model or a significant formal test. Differences across eras and players may also affect the stable-intensity assumption.

### PAR #3.30 — Test Level

**Source:** §3.5 exercises, printed p122, PDF p141; the screenshot supplies no page. **No matching Basic/slide PT — retained as a requested exercise:** The mixture/posterior-probability task does not establish a new PT.

**Question, faithful paraphrase:** A red pill gives a Poisson$(1)$ count of colds next winter; a blue pill gives Poisson$(4)$. Each pill is equally likely beforehand. Given three colds, find the probability that the blue pill was taken.

**Supplementary — not explicitly covered in Week 6 slides:** Bayes updating is included for this requested exercise, not as new Week 6 Core material.

**Worked solution.** Let $B,R$ denote pill colors. By total probability and Bayes' rule,

$$
P(B\mid X=3)=\frac{\tfrac12e^{-4}4^3/3!}{\tfrac12e^{-4}4^3/3!+\tfrac12e^{-1}1^3/3!}
=\frac{64e^{-3}}{1+64e^{-3}}=\boxed{0.7611297060}.
$$

**Check.** The pill probabilities need not remain equal after conditioning. Observing three colds favors the blue pill with mean 4.

### PAR #3.31 — Medium Practice

**Source:** §3.5 exercises, actual printed p122, PDF p141 (screenshot: p121). Calculation components use **PT-01, PT-09**; the numerical comparison establishes no new PT.

**Question, faithful paraphrase:** A US nickel has an estimated probability $1/6000$ of landing on its edge. Flip it independently 10000 times, and let $X$ count edge landings. Find the probability of 1–3 inclusive using (a) its exact distribution and (b) an approximate distribution.

**Worked solution.**

$$
\text{(a)}\quad X\sim\operatorname{Bin}(10000,1/6000),\quad
P(1\le X\le3)=\sum_{j=1}^{3}\binom{10000}{j}(1/6000)^j(5999/6000)^{10000-j}
=\boxed{0.7228996744}.
$$

$$
\text{(b)}\quad Z\sim\operatorname{Pois}(5/3),\quad
P(1\le X\le3)\approx e^{-5/3}\sum_{j=1}^{3}\frac{(5/3)^j}{j!}
=\boxed{0.7228572454}.
$$

**Check.** The approximation differs from the exact result by about $0.000042429$. It uses the Core relationship on slide 24.

### PAR #3.32 — Medium Practice

**Source:** §3.5 exercises, actual printed pp122–123, PDF pp141–142 (screenshot: p121). Calculation components use **PT-01, PT-09**; the comparison adds no PT.

**Question, faithful paraphrase:** A chessboard is hung as a dartboard. Throw 100 darts, each equally likely to hit any of the 64 squares, using independent throws. (a) Find the exact probability that the top-left square receives exactly two darts. (b) Approximate it with an appropriate distribution.

**Worked solution.** The success probability for one specified square is $1/64$, not $1/8$.

$$
\text{(a)}\quad P(X=2)=\binom{100}{2}(1/64)^2(63/64)^{98}
=\boxed{0.2582151068}.
$$

$$
\text{(b)}\quad \mu=100/64=1.5625,\quad
P(X=2)\approx e^{-1.5625}\frac{1.5625^2}{2!}=\boxed{0.2558732753}.
$$

**Check.** Multiple darts may hit the same square; no finite stock is being depleted, so this is not Hypergeometric.

### PAR #5.2 — Basic Practice

**Source:** §5.1 exercises, printed p218, PDF p237; **PT-05**.

**Question:** Find the probability that an even number of rolls of a fair die is needed for the first 4. See [PT-05](Study-Notes.md#pt05) and [A05](#a05) for the full statement and series solution: $\boxed{5/11}$.

### PAR #5.4 — Basic Practice

**Source:** §5.1 exercises, printed p218, PDF p237; **PT-04**.

**Question:** The textbook's total-trials variable is $X\sim\operatorname{Geom}(.3)$. Use R to find (a) $P(X=3)$, (b) $P(2\le X<9)$, and (c) $P(X\ge4)$. See [PT-04](Study-Notes.md#pt04) and [A04](#a04) for the full statement, conversions, commands, and values.

### PAR #5.5 — Medium Practice

**Source:** §5.1 exercises, printed pp218–219, PDF pp237–238; **PT-04**. Expectation uses Core material in C-02.

**Question, faithful paraphrase:** Loki independently metal-detects small beach sites on weekends; each site has hit probability 15%. Find (a) the probability of the first hit on site 5; (b) the probability of a hit within five sites; (c) the expected sites searched until the first hit.

**Worked solution.** Let $T$ count total sites. Then $P(T=t)=.85^{t-1}(.15)$.

$$
\text{(a)}\quad P(T=5)=.85^4(.15)=\boxed{0.0783009375};
$$

$$
\text{(b)}\quad P(T\le5)=1-.85^5=\boxed{0.5562946875};\qquad
\text{(c)}\quad E(T)=1/.15=\boxed{20/3\approx6.666667}.
$$

**Check.** First success on trial 5 requires four initial failures. Within five also includes success on trials 1–4.

### PAR #5.7 — Test Level

**Source:** §5.1 exercises, printed p219, PDF p238; **PT-02**.

**Question, faithful paraphrase:** Each of Dominic's college applications succeeds with probability 25%. Under independent, constant-probability outcomes, how many applications are needed for at least a 95% probability of one or more acceptances?

**Worked solution.**

$$
1-.75^n\ge.95\iff n\ge\frac{\log .05}{\log .75}=10.4133436193\ldots.
$$

**Answer.** At least **11 applications**. With 10, the probability is $0.9436864853$; with 11, it is $0.9577648640$, first meeting the target. Actual applications may be dependent; independence is the calculation's model assumption.

### PAR #5.10 — Test Level

**Source:** §5.1 exercises, printed p219, PDF p238. **No matching Basic/slide PT — retained as a requested exercise:** First-success waiting without replacement is not independent geometric waiting. PT-07's fixed-sample count is not expanded into a stopping-time task.

**Question, faithful paraphrase:** A bag contains $r$ red and $b$ blue balls. Draw randomly without replacement. Let $X$ be total draws through the first red ball. (a) Explain why it is not geometric. (b) Prove

$$
P(X=k)=\frac{\binom{r+b-k}{r-1}}{\binom{r+b}{r}},\quad k=1,2,\ldots,b+1.
$$

**Worked solution.** Take integers $r\ge1,b\ge0$. (a) Drawing blue changes the red proportion: initially $r/(r+b)$, then $r/(r+b-1)$ after a blue draw. Trials are dependent with changing success probability. Waiting is at most $b+1$, unlike the usual unbounded geometric support. The degenerate case $b=0$ gives immediate success, consistent with geometric$(1)$.

**Supplementary — not explicitly covered in Week 6 slides:** Part (b)'s first-red-position count is specific to this exercise. Randomly order all $N=r+b$ balls. The $r$ red positions have $\binom Nr$ equally likely choices. First red at position $k$ requires blue in the first $k-1$ positions, red at $k$, and the other $r-1$ red positions chosen from the remaining $N-k$:

$$
P(X=k)=\frac{\binom{N-k}{r-1}}{\binom Nr}.
$$

**Answer and check.** Support is $1\le k\le b+1$; red must appear by draw $b+1$. Every set of red positions belongs to exactly one group according to its minimum position, so these probabilities sum to 1. If $r=0$, there is no first red, and this finite waiting model does not apply.

### PAR #5.11 — Medium Practice

**Source:** §5.1 exercises, actual printed p219, PDF p238 (screenshot: p218). **No matching Basic/slide PT — retained as a requested exercise:** $E(2^X)$ and its existence conditions differ from the first/second-moment tasks specified in class.

**Question, faithful paraphrase:** For $X\sim\operatorname{Geom}(p)$, find $E(2^X)$ and the values of $p$ for which it exists. The textbook's $X$ counts total trials.

**Supplementary — not explicitly covered in Week 6 slides:** The expectation of a nonlinear function and its series-convergence condition are included only for this exercise, without introducing generating functions.

**Worked solution.** For $0<p\le1$,

$$
E(2^X)=\sum_{x=1}^{\infty}2^x p(1-p)^{x-1}
=2p\sum_{j=0}^{\infty}[2(1-p)]^j.
$$

The series converges when $2(1-p)<1$, equivalently $p>1/2$.

**Answer.**

$$
E(2^X)=\frac{2p}{2p-1},\quad \frac12<p\le1;
\qquad E(2^X)=+\infty,\quad0<p\le\frac12.
$$

**Check.** With $p=1$, $X=1$ and the answer is 2. At $p=1/2$, the terms do not approach 0, so the closed form cannot give a finite expectation. Do not replace the expectation with $2^{E(X)}$.

### PAR #5.20 — Basic Practice

**Source:** §5.3 exercises, actual printed p220, PDF p239 (screenshot: p218); **PT-06**.

**Question:** The textbook's total-trials variable is $X\sim\operatorname{NegBin}(3,.4)$. Give R commands and find (a) $P(X=6)$, (b) $P(5\le X<11)$, and (c) $P(X\ge8)$. See [PT-06](Study-Notes.md#pt06) and [A06](#a06) for the statement and solutions.

### PAR #5.21 — Test Level

**Source:** §5.3 exercises, actual printed p220, PDF p239 (screenshot: p219); **PT-06**.

**Question, faithful paraphrase:** Independently toss a fair coin until the fourth head. Find (a) the probability of exactly 10 tosses; (b) the probability of at least 10; (c) the PMF of $Y$, the total tails.

**Worked solution.** Let $T$ count total tosses, with success target 4 and success probability $1/2$.

$$
\text{(a)}\quad P(T=10)=\binom93\left(\frac12\right)^{10}
=\boxed{0.08203125}.
$$

$$
\text{(b)}\quad P(T\ge10)=1-\sum_{t=4}^{9}\binom{t-1}{3}2^{-t}
=\boxed{0.25390625}.
$$

**Supplementary — not explicitly covered in Week 6 slides:** Independently check (b) using PAR §5.3's equivalent event: at most three heads in the first nine tosses, with probability $\sum_{j=0}^{3}\binom9j2^{-9}=130/512=0.25390625$.

$$
\text{(c)}\quad Y=T-4,\qquad
P(Y=y)=\binom{y+3}{3}\left(\frac12\right)^{y+4},\quad y=0,1,\ldots.
$$

**Check.** Part (b) includes the fourth head occurring exactly on toss 10. Examine the first nine tosses, not fewer than four successes in the first ten.

### PAR #5.25 — Test Level

**Source:** §5.3 exercises, actual printed p221, PDF p240 (screenshot: p219); cumulative waiting calculations from **PT-06**.

**Question, faithful paraphrase:** O-negative blood occurs in 7.2% of the US population. A clinic wants 10 such donors. Treat successive screenings as independent with fixed success probability. Find the probability of finding the required 10 among the first 100 people screened.

**Worked solution.** "Finding 10" means the tenth success has occurred by screening 100: at least 10, not exactly 10. Let $T_{10}$ count total people screened. Then

$$
P(T_{10}\le100)=\sum_{t=10}^{100}\binom{t-1}{9}(.072)^{10}(.928)^{t-10}
=\boxed{0.1830090887}.
$$

**Supplementary — not explicitly covered in Week 6 slides:** Check using PAR §5.3's NB/Binomial event equivalence. If $B\sim\operatorname{Bin}(100,.072)$, then

$$
P(T_{10}\le100)=P(B\ge10)=1-\sum_{j=0}^{9}\binom{100}{j}(.072)^j(.928)^{100-j}.
$$

R checks are `pnbinom(90,10,.072)` or `1-pbinom(9,100,.072)`. The specific R functions are Supplementary; both produce the same answer.

### PAR #5.34 — Basic Practice

**Source:** §5.4 exercises, actual printed p223, PDF p242 (screenshot: p218); **PT-07**.

**Question:** Randomly select six plants from eight marigolds and 15 impatiens; $X$ counts marigolds. Find (a) $P(X=3)$, (b) $P(X\le2)$, and (c) $E(X)$. See [PT-07](Study-Notes.md#pt07) and [A07](#a07) for the full statement and solution.

<a id="self-test"></a>

## D. Source-Based Self-Test Index

This section indexes existing slide/Basic questions without changing data, adding subparts, or inventing exercises. Open each statement and answer its original task independently before checking the solution. The relevant Concept appears above the corresponding PT if you need to review the method. Supplementary PTs remain labelled separately.

| PT / source task | Source | Question statement | Unique complete solution |
| --- | --- | --- | --- |
| PT-01 Fixed-trial success counts | Slides 5–6: telephone warranties | [Question](Study-Notes.md#pt01) | [A01](#a01) |
| PT-02 Minimum quantity for at least one success | Slide 7: backup generators | [Question](Study-Notes.md#pt02) | [A02](#a02) |
| PT-03 Derive stated means and variances | Slide 3: Bernoulli show task | [Question](Study-Notes.md#pt03) | [A03](#a03) |
| PT-04 First-success waiting and counting conventions | PAR Basic #5.4(a–c) | [Question](Study-Notes.md#pt04) | [A04](#a04) |
| PT-05 Even first-success times — **Supplementary** | PAR Basic #5.2 | [Question](Study-Notes.md#pt05) | [A05](#a05) |
| PT-06 Waiting for the rth success | PAR Basic #5.20(a–c) | [Question](Study-Notes.md#pt06) | [A06](#a06) |
| PT-07 Sample counts without replacement | PAR Basic #5.34(a–c) | [Question](Study-Notes.md#pt07) | [A07](#a07) |
| PT-08 Exact sampling versus Binomial approximation | Slides 16–17: warehouse Case 2 | [Question](Study-Notes.md#pt08) | [A08](#a08) |
| PT-09 Poisson count probabilities | MMSA Basic #91(a–d) | [Question](Study-Notes.md#pt09) | [A09](#a09) |
| PT-10 Assess Poisson assumptions | Slide 26(a): forest trees | [Question](Study-Notes.md#pt10) | [A10](#a10) |
| PT-11 Obtain Poisson PMF from a Binomial limit | Slides 21–23: Shiba construction | [Question](Study-Notes.md#pt11) | [A11](#a11) |

**The sixth Basic question:** [PAR #3.26: red blood cell counts](#p326) also uses PT-09; its statement and solution are in that entry. All six Basic exercises therefore have an entry point in this review index.

**Further lecture review:** [L01–L13](#lecture-solutions) preserve all available questions in lecture order. [L06](#l06) proves geometric moments; [L08](#l08) proves NB moments. Both remain within PT-03 rather than creating another PT for a different distribution. The missing Labubu (c–d) remain a source gap.

<a id="coverage"></a>

## E. Coverage and Unresolved-Items Appendix

### Sources, concepts, and learning outcomes

| Reviewed material | Role / reading status | Coverage |
| --- | --- | --- |
| Week6-L0401-annotated.pdf, PDF pp1–28 | Primary; all 28 pages visually checked, including the handwritten insert | C-01–C-05; L01–L13 |
| Week-relevant content in MMSA §3.6, printed pp156–164 | Relevant/supporting reading; Poisson model, approximation, specified exercises | C-05; #91, #93, #94, #101 |
| Week-relevant content in MMSA §3.7, printed pp164–173 | Relevant/supporting reading; Hypergeometric, NB, counting conventions, specified exercises | C-02–C-04; #114, #118, #121 |
| PAR §3.5 and specified chapter exercises, pp121–123 | Relevant/supporting reading; Poisson and specified exercises | C-05; 8 textbook exercises |
| Actual PAR §§5.1, 5.3, 5.4 and specified exercises, pp218–223 | Relevant/supporting reading; only needed geometric, NB, Hypergeometric material | C-02–C-04; 10 textbook exercises |
| User's Week 6 exercise-table screenshot | Authority for Relevant Chapters / Suggested Problems list | Original Basic / Medium / Test Level labels retained |

**Section-number discrepancy:** The screenshot labels PAR NB and Hypergeometric as §§5.2 and 5.3. The supplied second edition's contents and text instead use §§5.3 and 5.4; §5.2 is MGFs. Topics are matched by their identities, without including MGFs in this week's scope.

Mandatory assigned reading has not been verified from these sources. No additional course-platform assignments or assessment scope have been queried or inferred. Adjacent PAR topics such as MGFs, memorylessness, coupon collection, and multinomial distributions are excluded.

| slide 2 learning outcome | Concepts / tasks |
| --- | --- |
| Define geometric, NB, Hypergeometric variables, PMFs, and features | C-02–C-04; L05–L10 |
| Use their properties to calculate probabilities | PT-04–PT-08; corresponding Basic and requested exercises |
| Poisson/Binomial relationship and approximation | C-05, PT-11; L11–L12; MMSA #93, #94; PAR #3.31, #3.32 |
| Assess Poisson modeling contexts | PT-10; L11, L13(a) |
| Poisson probabilities | PT-09; MMSA #91, #101; PAR #3.26, #3.27; L13(b–c) |
| Select and justify discrete models | Scope comparison table and PT conditions; actual L03–L13 source questions, without an invented comprehensive PT |

### PT evidence audit

| PT | Single owner | At least one actual eligible source task |
| --- | --- | --- |
| PT-01 | C-01 | Full slides 5–6 question; slide 11(a–b) |
| PT-02 | C-01 | Slide 7 source question |
| PT-03 | C-01 | Slide 3 handwritten task; PDF p5 derivation; slides 10 and 14 "show this" |
| PT-04 | C-02 | slides 8–9; PAR Basic #5.4(a–c) |
| PT-05 — Supplementary | C-02 | PAR Basic #5.2; no even-waiting task appears in the slides |
| PT-06 | C-03 | slides 12–14; PAR Basic #5.20(a–c) |
| PT-07 | C-04 | slide 16 Case 1; PAR Basic #5.34(a–c) |
| PT-08 | C-04 | Slides 16–17 Case 2 source question and approximation annotations |
| PT-09 | C-05 | MMSA Basic #91(a–d); PAR Basic #3.26; slide 26(b–c) |
| PT-10 | C-05 | Slide 20 question; slide 26(a) |
| PT-11 | C-05 | Slides 21–23 blanks and explicit limiting-PMF task |

No PT is established from Medium/Test Level or invented questions. Each of the 11 PTs has one owner, one source teaching question, and one matching teaching solution.

### Exact textbook exercise accounting and verified locators

| Source / level | Requested exercises | Actual printed page(s) / PDF page(s) | Count |
| --- | --- | --- | --- |
| MMSA Basic | #91 | 162 / 174 | 1 |
| MMSA Medium | #93, 94 | 162 / 174 | 2 |
| MMSA Test Level | #101; #114, 118; #121 | 163 / 175; 172 / 184; 173 / 185 | 4 |
| PAR Ch3 Basic | #3.26 | 122 / 141 | 1 |
| PAR Ch3 Medium | #3.23; #3.25, 31; #3.32 | 121 / 140; 122 / 141; 122–123 / 141–142 | 4 |
| PAR Ch3 Test Level | #3.27, 28, 30 | 122 / 141 | 3 |
| PAR Ch5 Basic | #5.2, 4; #5.20; #5.34 | 218 / 237; 220 / 239; 223 / 242 | 4 |
| PAR Ch5 Medium | #5.5; #5.11 | 218–219 / 237–238; 219 / 238 | 2 |
| PAR Ch5 Test Level | #5.7, 10; #5.21; #5.25 | 219 / 238; 220 / 239; 221 / 240 | 4 |
| Total | 7 MMSA + 18 PAR | All source subparts and continuations included | **25** |

Exercise identities are retained when pages differ. MMSA #91, #93, #94 are on p162 rather than screenshot p163; #121 is on p173 rather than p172. Many PAR Chapter 3 items listed at p121 continue onto pp122–123. Chapter 5 locations for #5.20, #5.34, #5.11, #5.21, and #5.25 are listed above. All three PAR Chapter 3 Test Level exercises, for which the screenshot gives no page, were located on p122.

### Supplementary and no-matching-PT register

| Material | Reason for inclusion / location |
| --- | --- |
| Geometric/NB R functions and failures conversion | Explicitly requested by Basic #5.4 and #5.20; A04, A06, notes R table |
| PT-05 even-waiting task, geometric series and differentiation | Basic #5.2 and slide 10 moment proof; notes PT-05, A05, L06 |
| NB/Binomial cumulative-event equivalence | Independent checks for #5.21 and #5.25; notes C-03 and corresponding solutions |
| Small-interval clarification, tied Poisson modes, relative variation | Clarify slides 21–25; notes C-05 |
| Reciprocal of mean interarrival time | Supplied directly in MMSA #101; used only there |
| Variance-scaling rule | MMSA #118's conversion from paired rounds to individual rolls; used only there |
| Parameter inference | PAR #3.23 and #3.25; no complete matching Basic/slide PT |
| Sample-mean modeling and expected frequencies | PAR #3.28; no matching PT |
| Bayes / mixture model | PAR #3.30; no matching PT |
| First-red waiting PMF without replacement | PAR #5.10; no matching PT |
| Nonlinear expectation and convergence | PAR #5.11; no matching PT |

The numerical Binomial–Poisson approximation is Core on slide 24, but no eligible numerical source question establishes a separate PT. MMSA #93, #94 and PAR #3.31, #3.32 retain their original exact/approximate comparisons; calculation components link to PT-01 and PT-09. PT-11's limit derivation is not broadened into another task. The continuous-time threshold in MMSA #101(c) is handled locally.

<a id="source-corrections"></a>

### Verified source clarifications and corrections

- **MMSA third edition §3.7:** From printed p167, the main NB variable counts total trials; failures are an alternative definition. R counts failures, so subtract the success target $r$ before using R with total-trials questions. The notes and quick-reference table follow this edition.

- **Slide 13 extra handwritten question, PDF p14:** The stopping rule requires the first 14 boxes to contain four successes and ten failures when box 15 is the fifth success. The initial factor is $\binom{14}{4}(.05)^4(.95)^{10}$, followed by a factor $.05$ for the last success. The solution is reconstructed from the event, independently of the handwritten exponent's appearance.
- **Slide 16 Case 2, PDF p17:** The handwritten complement's layout could make all three numerator terms look positive. The correct form is $1-(a+b+c)/\binom{5000}{10}$. Slide 17's typed expansion explicitly subtracts each probability; the numerical results agree.
- **Slides 24–25:** "Unimodal" must allow adjacent tied maxima at a positive integer mean. The adjacent-PMF ratio verifies this Supplementary clarification without adding a modes PT.
- **PAR #3.23:** A positive parameter gives 4; allowing 0 leaves a degenerate possibility that the stated equality does not exclude. The solution explicitly records that boundary.
- **PAR #5.25:** "Find 10 among the first 100" is interpreted as finding the required number, hence at least 10 rather than exactly 10. The textbook total-trials variable and R failures conversion are explicit.

<a id="source-gaps"></a>

### Unresolved source gaps

**Only unrecoverable subparts:** Slide 9, PDF p10, begins at (e) and refers to (c) and (d), but the preceding slide 8 contains only (a) and (b). The available (a), (b), and (e) are solved. Missing statements are not guessed and establish no PT.

The Progress Check pages contain no readable additional question statements; slide 19's QR code is not expanded into another problem set. All 25 specified textbook exercises have been located, include necessary tables/continuations, and are solved; there are no missing textbook sources.

### Verification and artifact checks

- PDF extraction used the Docling native pipeline for searching; formulas, handwriting, cross-page statements, and Table 3.6 were checked against page images.
- [verify_week6.py](scripts/verify_week6.py) uses explicit finite PMF sums in the standard library to recompute textbook and slide values. It checks normalization, NB/Binomial event equivalence, integer thresholds, inverse-time substitution, and the first-red PMF. Run with `python3 scripts/verify_week6.py`.
- Numerical values were independently checked with SciPy Binomial, Poisson, Negative Binomial, and Hypergeometric PMF/CDF/survival functions rather than relying on handwritten answers or answer keys.
- Structural checks cover PT names/counts, single ownership, question/solution pairs, the 25-exercise inventory, relative links, figure paths, headings, table columns, mathematical delimiters, and unfinished markers. The retained Poisson figure was visually inspected.
- Both revised Markdown files pass Pandoc's MathML conversion without warnings, with links, anchors, tables, mathematical delimiters, and source-question preservation checked. The expanded Poisson factorial identity was also checked numerically. Earlier browser spot checks are not presented as complete visual verification of this version.
- Final deliverables are the two Markdown files, `figures/poisson-pmf.png`, and `scripts/verify_week6.py`. Source PDFs and the existing prompt are preserved. Temporary extraction, rendering, and QA artifacts are outside the deliverable directory.
