# STA237 Week 7 Answers and Practice

Use this file with [Study Notes](Study-Notes.md). Statements are **faithful paraphrases** preserving source data, conditions, and requested parts. Textbook difficulty labels come from the instructor's Week 7 list. Calculations use exact expressions where practical; displayed decimals are approximations. A source question selected as a representative has one canonical solution here, with links from its other inventory entries.

## Contents

- [A. PT Representative Solutions](#representatives)
- [B. All Slide Questions and Solutions](#slides)
- [C. All 27 Requested Textbook Exercises](#textbooks)
- [D. Source-Based Revision Index](#revision)
- [E. Coverage and Unresolved-Items Appendix](#coverage)

<a id="representatives"></a>

## A. PT Representative Solutions

<a id="a01"></a>

### Problem Type PT-01: Poisson Counts in a Specified Interval

**Question:** [PT-01](Study-Notes.md#pt01), slide 9 question 2.

**Worked solution.** Let $B$ count visits from noon to 6 PM. Under the lecture's stable-rate Poisson model, this is $6/24=1/4$ of a day, so $B\sim\operatorname{Pois}(12/4)=\operatorname{Pois}(3)$. “At least two” excludes zero and one:

$$
P(B\ge2)=1-P(B=0)-P(B=1)=1-e^{-3}-3e^{-3}.
$$

**Answer:** $\boxed{1-4e^{-3}\approx0.800852}$. The calculation assumes the full-day rate is reasonably constant across the specified six hours; seasonal average rate alone cannot establish this. The complement contains exactly the two omitted outcomes, and the result lies in $[0,1]$.

<a id="a02"></a>

### Problem Type PT-02: Fixed-Trial Success Counts

**Question:** [PT-02](Study-Notes.md#pt02), slide 10 question 3.

**Worked solution.** Let $W$ count winning cards among five. Under the independent-card model in the annotation, $W\sim\operatorname{Bin}(5,0.1)$, with support $0,\ldots,5$.

$$
P(W\ge1)=1-P(W=0)=1-(0.9)^5=\boxed{0.40951}.
$$

**Answer:** Binomial$(5,0.1)$; probability **0.409510**. This is a fixed-trial experiment; opening stops after five cards rather than after the first win. Independence is an assumption used by the model, not a consequence of each card having marginal probability 0.1.

<a id="a03"></a>

### Problem Type PT-03: First-Success Waiting and Counting Conventions

**Question:** [PT-03](Study-Notes.md#pt03), slide 10 question 4.

**Worked solution.** There are $4+2+3+1=10$ books, one of which is non-fiction. With uniformly random, independent selections and replacement, each try succeeds with $p=1/10$. The requested number of **tries** is $T$, including the successful try:

$$
P(T=t)=(0.9)^{t-1}(0.1),\quad t=1,2,\ldots.
$$

**Answer:** A total-trials geometric variable with success probability 0.1. The slide's annotation instead calls $F$ the number selected **before** the non-fiction book. That alternative variable satisfies $F=T-1$, has support $0,1,\ldots$, and PMF $0.9^f0.1$. The two variables describe the same experiment but are not numerically identical. This convention distinction resolves the wording/annotation difference.

<a id="a04"></a>

### Problem Type PT-04: Finite-Population Sample Counts

**Question:** [PT-04](Study-Notes.md#pt04), slide 10 question 5.

**Worked solution.** Following the question's handwritten **without-replacement** annotation, let $S$ count sci-fi books in a uniformly selected three-book sample. Then $N=10,K=3,n=3$, so

$$
P(S=s)=\frac{\binom3s\binom7{3-s}}{\binom{10}3},\quad s=0,1,2,3.
$$

Choose one of the three sci-fi books and two of the seven others:

$$
P(S=1)=\frac{\binom31\binom72}{\binom{10}3}
=\frac{63}{120}=\boxed{0.525}.
$$

**Answer:** Hypergeometric under the annotation's sampling rule; probability **0.525000**. The typed reference to question 4 is ambiguous because question 4 explicitly replaces books. If replacement were retained, the alternative would be Binomial$(3,0.3)$ and $P(S=1)=3(0.3)(0.7)^2=0.441$. These are different experiments, not interchangeable calculations. The annotation is the basis for the main answer.

<a id="a05"></a>

### Problem Type PT-05: A Best-of-Seven Series with Competing Stops

**Question:** [PT-05](Study-Notes.md#pt05), slide 9 question 1.

**Worked solution.** Let $L$ be series length, and $q=1-p$. The support is $4,5,6,7$. For $L=n$ and the Jays to win, the Jays must have three wins in the first $n-1$ games, then win game $n$. There are $\binom{n-1}3$ such sequences. For the opponent to win, interchange $p$ and $q$:

$$
P(L=n)=\binom{n-1}3\{p^4q^{n-4}+q^4p^{n-4}\},
\quad n=4,5,6,7.
$$

No earlier stop is possible in these counted sequences: the eventual winner has only three earlier wins and the other side has at most three.

**Answer:** The finite series-length model above, with

$$
P(L=5)=\boxed{4p^4q+4q^4p}.
$$

A single ordinary NB model for reaching four Jays wins would include experiments where the opponent has already won the series, as well as impossible lengths above seven. The two winner cases here partition all completed series, so their probabilities across $n=4,\ldots,7$ sum to one. As a check, $p=0$ or 1 gives $L=4$ with probability one.

<a id="a06"></a>

### Problem Type PT-06: Derive Poisson Mean and Variance

**Question:** [PT-06](Study-Notes.md#pt06), slide 6.

**Worked solution.** For $X\sim\operatorname{Pois}(\lambda)$, cancelling $x$ and putting $j=x-1$ gives

$$
E(X)=\lambda\sum_{j=0}^{\infty}e^{-\lambda}\frac{\lambda^j}{j!}=\lambda.
$$

The same method with $x(x-1)$, starting at $x=2$ and setting $j=x-2$, gives

$$
E[X(X-1)]=\lambda^2\sum_{j=0}^{\infty}e^{-\lambda}\frac{\lambda^j}{j!}=\lambda^2.
$$

Both remaining sums are complete Poisson PMF sums, equal to one. Therefore $E(X^2)=E[X(X-1)]+E(X)=\lambda^2+\lambda$, and

$$
\operatorname{Var}(X)=(\lambda^2+\lambda)-\lambda^2=\boxed{\lambda}.
$$

**Answer:** $E(X)=\operatorname{Var}(X)=\lambda$. The [concept derivation](Study-Notes.md#c02) shows the factorial cancellation explicitly. If the degenerate parameter zero is allowed, $X=0$ and both quantities are zero as well.

<a id="a07"></a>

### Problem Type PT-07: Derive Failure-Count Waiting Means

**Question:** [PT-07](Study-Notes.md#pt07), slide 8.

**Worked solution.** Let $F$ count failures before the first success. For $q=1-p$, $P(F=f)=pq^f$. With $S=q+2q^2+3q^3+\cdots$, subtracting its one-step shift gives

$$
(1-q)S=q+q^2+q^3+\cdots=\frac{q}{1-q},
\qquad E(F)=pS=p\frac{q}{(1-q)^2}=\frac qp.
$$

The geometric series converges for $0\le q<1$, equivalently $0<p\le1$. If $F_r$ counts failures before success $r$, divide the Bernoulli sequence into successive waiting blocks $F_1^{*},\ldots,F_r^{*}$. Each block has the first-success failures distribution, and $F_r=\sum_iF_i^{*}$.

**Answer:** $\boxed{E(F)=q/p}$ and $\boxed{E(F_r)=rq/p}$. For total trials, add the fixed successes to obtain $1/p$ and $r/p$. At $p=1$, both failure counts vanish, checking the formulas.

<a id="a08"></a>

### Problem Type PT-08: Revenue from a Count and Its Expected Value

**Question:** [PT-08](Study-Notes.md#pt08), slides 3(b), 4(c).

**(b) Worked solution.** For ten operating hours, $Y=85R^2-600$. The function increases over nonnegative repair counts. The count event from part (a) is $R\in\{18,19,20\}$, giving

| Repairs | Revenue from the given model |
| --- | --- |
| 18 | $85(18)^2-600=26940$ |
| 19 | $85(19)^2-600=30085$ |
| 20 | $85(20)^2-600=33400$ |

**Answer (b):** The corresponding revenues are **26940, 30085, or 33400 monetary units**. Writing $26940\le Y\le33400$ describes the range, but not every real number inside is attainable from this three-count event.

**(c) Worked solution.** In eight hours, $R\sim\operatorname{Pois}(16)$ and the fixed subtraction is $60(8)=480$. The second moment is $E(R^2)=16+16^2=272$.

$$
E(Y)=85E(R^2)-480=85(272)-480=\boxed{22640}.
$$

**Answer (c):** Expected eight-hour revenue is **22640 monetary units** under the source's worked interpretation. It is not $85[E(R)]^2-480$; the omitted contribution in that incorrect calculation would be $85\operatorname{Var}(R)$. The wording and rate discrepancies are [recorded explicitly](#discrepancies).

<a id="a09"></a>

### Problem Type PT-09: Repair-Count Intervals with at Least 75% Coverage

**Question:** [PT-09](Study-Notes.md#pt09), slides 4(d)–5.

**Worked solution.** For $R\sim\operatorname{Pois}(20)$, $\mu=20$ and $\sigma=\sqrt{20}$. Chebyshev with $k=2$ gives at least $1-1/4=0.75$ within two SDs. The real endpoints are

$$
20\pm2\sqrt{20}\approx[11.055728,28.944272].
$$

The integer observations inside are **12 through 28**, so the actual coverage is

$$
\sum_{r=12}^{28}e^{-20}\frac{20^r}{r!}
=F(28)-F(11)=\boxed{0.944279657}.
$$

The handwritten outward rounding to $[11,29]$ is a wider valid interval, with a different coverage, $F(29)-F(10)\approx0.967370064$. It must not be given the narrower interval's 0.944280 coverage.

**Quantile comparison.** The source's `qpois(.125,20)` and `qpois(.875,20)` give 15 and 25. Their inclusive count interval has actual coverage

$$
P(15\le R\le25)=F(25)-F(14)=\boxed{0.782950746}.
$$

**Answer:** Either interval satisfies “at least 75%,” but the derivations differ. The Chebyshev interval has a distribution-independent lower guarantee; $[15,25]$ uses the particular Poisson CDF. Discrete quantile rounding explains why its coverage is not exactly 0.75. Correct R coverage expressions are `ppois(28,20)-ppois(11,20)` and `ppois(25,20)-ppois(14,20)`.

<a id="a10"></a>

### Problem Type PT-10: Check and Normalize a Density

**Question:** [PT-10](Study-Notes.md#pt10), MMSA #5(a), printed p201 / PDF p213.

**Worked solution.** The full density is $kx^2$ on $[0,2]$, zero elsewhere. Nonnegativity requires $k\ge0$. Normalize over the entire support:

$$
1=\int_0^2kx^2\,dx=k\left[\frac{x^3}{3}\right]_0^2=\frac{8k}{3}.
$$

**Answer:** $\boxed{k=3/8}$. This is positive and gives total integral one, so both PDF requirements hold. Parts (b–d) are completed in [MMSA #5](#m05).

<a id="a11"></a>

### Problem Type PT-11: Compare and Compute Density Areas

**Question:** [PT-11](Study-Notes.md#pt11), slide 17(b).

**Worked solution.** The density decreases from left to right, so equal-width intervals near zero should be more likely. An antiderivative of $3(y-1)^2$ is $(y-1)^3$:

$$
P(0\le Y\le0.25)=[(y-1)^3]_0^{1/4}
=\left(-\frac34\right)^3-(-1)^3=\boxed{\frac{37}{64}=0.578125},
$$

$$
P(0.75\le Y\le1)=[(y-1)^3]_{3/4}^{1}
=0-\left(-\frac14\right)^3=\boxed{\frac1{64}=0.015625}.
$$

**Answer:** The first interval is much more likely, confirming the graph. Both integrals use only the support and fall between zero and one; the same interval width does not force the same probability.

<a id="a12"></a>

### Problem Type PT-12: Uniform Interval Probabilities

**Classification:** Supplementary — uniform model absent from the Week 7 slides. **Question:** [PT-12](Study-Notes.md#pt12), MMSA #7(b,d), printed p201 / PDF p213.

**Worked solution.** The support $[25,35]$ has length ten minutes, so density height is $1/10$ per minute.

- **(b)** $X>33$ overlaps the support from 33 to 35: $P(X>33)=(35-33)/10=\boxed{0.2}$.
- **(d)** Since the entire interval $[a,a+2]$ lies inside the support, its probability is its length divided by ten: $\boxed{2/10=0.2}$, independent of its location.

The equal-length result uses a constant density; it is not true for arbitrary continuous models. [MMSA #7](#m07) completes the PDF/sketch and median parts.

<a id="a13"></a>

### Problem Type PT-13: PDF–CDF Conversion and CDF Probabilities

**Question:** [PT-13](Study-Notes.md#pt13), slide 19(a–c).

**(a) Worked solution.** Before zero there is no area; beyond one all area is accumulated. For $0\le y\le1$,

$$
F_Y(y)=\int_0^y3(u-1)^2\,du=[(u-1)^3]_0^y=(y-1)^3+1.
$$

Thus the complete CDF is

$$
F_Y(y)=\begin{cases}
0,&y<0,\\
1+(y-1)^3,&0\le y\le1,\\
1,&y>1.
\end{cases}
$$

**(b)** $P(0.1\le Y\le0.4)=F_Y(0.4)-F_Y(0.1)=[1-.6^3]-[1-.9^3]=\boxed{0.513}$.

**(c)** $P(Y=0.6)=\boxed{0}$ because an isolated point has zero density area.

**Check:** $F_Y(0)=0,F_Y(1)=1$, and the interior derivative is the given nonnegative PDF. The CDF joins continuously to its outside branches.

<a id="a14"></a>

### Problem Type PT-14: Solve a Percentile Equation

**Question:** [PT-14](Study-Notes.md#pt14), slide 22 and its CDF annotation.

**Worked solution.** On $[0,1]$, $F_M(m)=\int_0^m3u^2du=m^3$, so

$$
F_M(m)=\begin{cases}0,&m<0,\\m^3,&0\le m<1,\\1,&m\ge1.\end{cases}
$$

A median $m_{0.5}$ must have cumulative probability one half. Therefore

$$
m_{0.5}^3=\frac12,
\qquad m_{0.5}=\boxed{2^{-1/3}\approx0.793701}.
$$

It lies in the support and substitution yields $F_M(m_{0.5})=1/2$. Its location above the support midpoint is sensible because the density increases toward one.

<a id="a15"></a>

### Problem Type PT-15: Moments and Expected Functions from a Density

**Question:** [PT-15](Study-Notes.md#pt15), MMSA #18(a–c), printed p210 / PDF p222; shared density from #1/#11.

**(a)** The duration is in hours. Its mean is

$$
E(X)=\int_0^2x\frac{x}{2}\,dx=\left[\frac{x^3}{6}\right]_0^2=\boxed{\frac43\text{ hours}}.
$$

**(b)** First compute the mean square:

$$
E(X^2)=\int_0^2x^2\frac{x}{2}\,dx
=\left[\frac{x^4}{8}\right]_0^2=2.
$$

Then

$$
\operatorname{Var}(X)=2-\left(\frac43\right)^2=\boxed{\frac29\text{ hours}^2},
\qquad \sigma_X=\boxed{\frac{\sqrt2}{3}\text{ hours}\approx0.471405\text{ hours}}.
$$

**(c)** The charge function is $h(x)=x^2$, so

$$
E[h(X)]=\int_0^2x^2\frac{x}{2}\,dx=\boxed{2\text{ charge units}}.
$$

The source does not specify a currency. It is $E(X^2)$, not $[E(X)]^2$. The mean lies between zero and two hours and the variance is positive, checking basic plausibility.

<a id="slides"></a>

## B. All Slide Questions and Solutions

The following **14 source-task groups** account for explicit examples, model-selection questions, formula blanks, and annotated mathematical tasks. Cross-page continuations are grouped together. Slide/page numbers are identical in this PDF.

<a id="l01"></a>

### L01 — Mechanic counts, revenue, and intervals: slides 3–5

**Question — faithful paraphrase:** The repair count is Poisson with mean $2t$ for $t$ operating hours. The specified revenue function is $Y=85R^2-60t$. Assuming the source's independent-arrival model and same-day repair interpretation: (a) find the probability of 18–20 repairs in ten hours; (b) give corresponding revenues; (c) find expected revenue for eight hours; (d) give a repair interval holding at least 75% of the time in ten hours and explain the R interval comparison.

**(a), PT-01:** $R\sim\operatorname{Pois}(20)$, and the lecture annotation interprets “between” inclusively:

$$
P(18\le R\le20)=e^{-20}\left(\frac{20^{18}}{18!}+\frac{20^{19}}{19!}+\frac{20^{20}}{20!}\right)
=\boxed{0.262064186}.
$$

**(b–c), PT-08:** Complete solutions are [A08](#a08), including all three revenue values and the expected revenue.

**(d), PT-09:** [A09](#a09) gives the real Chebyshev interval, its included integer values and actual coverage, the handwritten rounding variant, and the central-quantile comparison. The contradictory $3t$ printed on slide 5 is not silently substituted for the consistent model; see [discrepancies](#discrepancies).

<a id="l02"></a>

### L02 — Poisson moment derivations: slide 6

**Question:** Show that the Poisson parameter equals both the mean and variance. The annotation suggests first finding $E[X(X-1)]$ rather than summing $x^2p_X(x)$ directly. **PT-06; complete solution:** [A06](#a06).

<a id="l03"></a>

### L03 — Geometric PMF and support blanks: slide 7

**Question:** Define the failures-before-first-success geometric PMF and support, and distinguish support from an algebraic function's domain. **PT-03.**

**Solution:** For independent Bernoulli trials with fixed $0<p<1$, $P(F=f)=(1-p)^fp$ for integers $f\ge0$, and zero otherwise. The geometric PMF is not a real-input probability-density curve. Its support is $\{0,1,2,\ldots\}$; an extension such as $0.7^x0.3$ can be evaluated at real inputs without assigning probability mass to them. At the boundary $p=1$, only $F=0$ has positive mass. The handwritten annotation reads “support $\subseteq$ domain,” consistent with the typed distinction: the support contains only inputs assigned positive probability, whereas a function can also be defined at inputs outside that set.

<a id="l04"></a>

### L04 — Geometric and NB failure-count expectations: slide 8

**Question:** Derive the expectation for failures before the first success, then for failures before the $r$th success. **PT-07; complete solution:** [A07](#a07). The slide itself supplies geometric-series reasoning, so that reasoning is Core in Week 7.

<a id="l05"></a>

### L05 — Pick the model, all five questions: slides 9–10

| Source question | Complete statement / task | Canonical solution |
| --- | --- | --- |
| 1 | Independent Jays game wins have fixed probability $p$; a series ends when either side wins four games. Model series length and find the probability of five games. | [A05](#a05), PT-05 |
| 2 | Monarchs visit at 12/day; under the stated Poisson interpretation find at least two arrivals from noon to 6 PM. | [A01](#a01), PT-01 |
| 3 | Five scratch cards, each 10% chance of a win; under the annotation's independence assumption model winning-card count and find at least one winner. | [A02](#a02), PT-02 |
| 4 | Ten books: four romance, two textbooks, three sci-fi, one non-fiction. Randomly pick and replace until non-fiction; model total tries. | [A03](#a03), PT-03 |
| 5 | From that collection randomly pick three books; under the without-replacement annotation model sci-fi count and find exactly one. | [A04](#a04), PT-04; typed ambiguity explicitly retained |

<a id="l06"></a>

### L06 — PDF property blanks: slide 15

**Task:** Supply the PDF conditions, interval probability, and distinction between a density and point probability.

**Answer and reasoning:** A valid PDF is nonnegative and has integral one. For $a\le b$, $P(a\le X\le b)=\int_a^bf_X(x)dx$. Generally $f_X(x)\ne P(X=x)$; for these continuous models, $P(X=x)=0$. Density heights may exceed one, because the probability restriction applies to areas, not heights. See [C-03](Study-Notes.md#c03). These are definition blanks, not a separately invented PT.

<a id="l07"></a>

### L07 — Verify a density and compare its regions: slides 16–17

**Question:** For $f_Y(y)=3(y-1)^2$ on $0\le y\le1$, zero elsewhere, (a) verify a valid PDF; (b) compare and compute probabilities on $[0,0.25]$ and $[0.75,1]$. The graph annotation also asks where its mode, median, and mean are located.

**(a), PT-10:** The function is nonnegative because it is three times a square. Total area is

$$
\int_0^13(y-1)^2dy=[(y-1)^3]_0^1=0-(-1)=1.
$$

Both conditions hold. **(b), PT-11:** [A11](#a11) contains both complete calculations.

**Graph annotation:** The maximum density is at zero, so the mode is 0. For the median, the [CDF in A13](#a13) gives $1-(1-m)^3=1/2$, hence $m=1-2^{-1/3}\approx0.206299$. For the mean,

$$
E(Y)=\int_0^13y(y-1)^2dy
=3\left[\frac{y^4}{4}-\frac{2y^3}{3}+\frac{y^2}{2}\right]_0^1=\frac14.
$$

Thus mode $<$ median $<$ mean, consistent with a decreasing density whose tail extends rightward. This answers the actual annotation using concepts introduced later in the deck; it is not an extra invented exercise.

<a id="l08"></a>

### L08 — CDF property blanks: slide 18

**Task:** Complete the CDF definition, derivative relation, point/interval probabilities, and limiting values.

**Answer:** Every RV has $F_X(x)=P(X\le x)$. For the density models here, $F_X(x)=\int_{-\infty}^xf_X(u)du$ and $F_X'=f_X$ at differentiable points. A point has probability zero; interval probability is $F_X(b)-F_X(a)$; $F_X(-\infty)=0$ and $F_X(+\infty)=1$. The CDF is nondecreasing. The source wording “if it exists” does not restrict existence of the CDF; see [C-04](Study-Notes.md#c04).

<a id="l09"></a>

### L09 — CDF of the polynomial density: slide 19

**Question:** For $f_Y(y)=3(y-1)^2$ on $[0,1]$, derive the complete CDF; find $P(0.1\le Y\le0.4)$; find $P(Y=0.6)$. **PT-13; complete solution:** [A13](#a13).

<a id="l10"></a>

### L10 — Piecewise CDF, probability, and density: slide 20

**Question — faithful paraphrase:** The CDF is

$$
F_Y(y)=\begin{cases}
0,&y<0,\\y^3/2,&0\le y<1,\\y/2,&1\le y<2,\\1,&y\ge2.
\end{cases}
$$

(a) Find $P(0.5\le Y\le1.5)$. (b) Find the PDF. **PT-13.**

**Solution:** The CDF joins at 1 because both interior expressions give $1/2$, and it reaches 1 at 2, so the boundaries have no jumps.

$$
\text{(a)}\quad F_Y(1.5)-F_Y(0.5)=\frac{1.5}{2}-\frac{(0.5)^3}{2}
=\boxed{\frac{11}{16}=0.6875}.
$$

For (b), differentiate inside each branch:

$$
f_Y(y)=\begin{cases}3y^2/2,&0<y<1,\\1/2,&1\le y<2,\\0,&\text{otherwise}.\end{cases}
$$

A density value at 1 can be chosen arbitrarily without affecting probabilities; here it is set to $1/2$, matching the plotted convention. The left and right derivatives of the CDF at 1 differ, so this chosen density value is not claimed to be an ordinary derivative there. Check total density area: $\int_0^1(3y^2/2)dy+\int_1^2(1/2)dy=1/2+1/2=1$. The [source reconstruction](figures/lecture-density-cdf.png) shows this PDF/CDF pair.

<a id="l11"></a>

### L11 — Percentile definition and median task: slides 21–22

**Definition blanks:** The $100p$th percentile satisfies $F_X(x_p)=p$ when the relevant continuous CDF can be inverted. The median is the 50th percentile; quartiles are the 25th and 75th; IQR is $Q_3-Q_1$ and describes the width containing the central 50% for these models.

**Original task:** For $f_M(m)=3m^2$ on $[0,1)$ and zero elsewhere, find the complete CDF as requested in the annotation and compute the median. **PT-14; complete solution:** [A14](#a14).

<a id="l12"></a>

### L12 — Derive the variance shortcut: slide 26

**Question:** Complete the efficient variance formula and show it again using the definition. The page says “To finish in Week 8”; it remains an explicit task in the supplied deck.

**Worked solution:** With $\mu=E(X)$ and finite second moment,

$$
\begin{aligned}
\operatorname{Var}(X)
&=\int (x-\mu)^2f_X(x)dx\\
&=\int x^2f_X(x)dx-2\mu\int xf_X(x)dx+\mu^2\int f_X(x)dx\\
&=E(X^2)-2\mu^2+\mu^2=\boxed{E(X^2)-[E(X)]^2}.
\end{aligned}
$$

All integrals are over the full support (equivalently the real line with the full PDF). The last equality uses normalization and the definition of the mean. This is an identity check attached to C-06, not a new exercise-derived PT. Variance is nonnegative; SD is its square root and has the original units.

<a id="l13"></a>

### L13 — Expected functions and transformed distributions: slides 24–25

**Definition tasks / demonstration:** State $E(X)$ and $E[g(X)]$, and explain the distributions shown for $X$, $X^2$, $\sqrt X$, and $e^X$ when $f_X(x)=3(x-1)^2$ on $[0,1]$.

**Answer:** $E(X)=\int xf_X(x)dx$ and $E[g(X)]=\int g(x)f_X(x)dx$. The density in the weighting factor remains $f_X$, because the integral averages over original observations. For the three displayed transformations, the expectation setups are respectively

$$
\int_0^1x^2\,3(x-1)^2dx,\quad
\int_0^1\sqrt{x}\,3(x-1)^2dx,\quad
\int_0^1e^x\,3(x-1)^2dx.
$$

The slide does not request numerical values for these three demonstrations. Their possible-value ranges are $[0,1]$, $[0,1]$, and $[1,e]$ respectively, with different density shapes as illustrated by the [reconstruction](figures/lecture-transformations.png). Neither $E[g(X)]=g(E(X))$ nor $f_{g(X)}=f_X$ follows. The slide explicitly defers tools for deriving those transformed densities, so no such method is added here.

<a id="l14"></a>

### L14 — Gas-pump mean and variance with physical units: slides 27–28

**Question — faithful paraphrase:** A pump can supply at most 20,000 gallons per month. Its monthly amount $G$, in units of 10,000 gallons, has PDF

$$
f_G(g)=\begin{cases}g,&0<g<1,\\2-g,&1\le g<2,\\0,&\text{otherwise}.\end{cases}
$$

(a) Find expected actual gallons pumped. (b) Find the variance in actual gallons. **PT-15.**

**(a)** Split at the density's breakpoint, keeping the observation $g$ as a factor:

$$
E(G)=\int_0^1g^2dg+\int_1^2g(2-g)dg
=\frac13+\left[g^2-\frac{g^3}{3}\right]_1^2=1.
$$

The actual amount is $A=10000G$, so $\boxed{E(A)=10000\text{ gallons}}$.

**(b)** The second moment is

$$
E(G^2)=\int_0^1g^3dg+\int_1^2g^2(2-g)dg
=\frac14+\left[\frac{2g^3}{3}-\frac{g^4}{4}\right]_1^2
=\frac76.
$$

Thus $\operatorname{Var}(G)=7/6-1=1/6$, and

$$
\boxed{\operatorname{Var}(A)=10000^2/6
\approx16666666.666667\text{ gallons}^2}.
$$

For a units check, the corresponding SD is $10000/\sqrt6\approx4082.482905$ gallons. The [density graph](figures/gas-pump.png) is symmetric about one scaled unit, consistent with the mean. Reporting $1/6$ as gallons squared would omit the squared conversion factor.

<a id="textbooks"></a>

## C. All 27 Requested Textbook Exercises

The following locators distinguish actual printed pages from one-based PDF pages. Instructor page references identify where the exercise sets begin; many specific questions continue on later pages. Exercise numbers are preserved. All unqualified textbook statements below are faithful paraphrases.

**MMSA: §§4.1–4.2 — 18 exercises**

<a id="m03"></a>

### MMSA #3 — Basic Practice

**Source:** §4.1, printed p200 / PDF p212; instructor locator p200. **PT-11** for probabilities; C-03 for graph interpretation.

**Question:** Measurement error $X$ has PDF $f_X(x)=0.09375(4-x^2)=\frac3{32}(4-x^2)$ for $-2\le x\le2$, zero elsewhere. (a) Sketch it. (b) Find $P(X>0)$. (c) Find $P(-1<X<1)$. (d) Find $P(X<-0.5\text{ or }X>0.5)$.

**(a)** The [density gallery](figures/textbook-densities.png) shows a downward-opening parabola, zero at $\pm2$, symmetric about zero, with maximum $f_X(0)=3/8$; it is zero outside $[-2,2]$.

Use the antiderivative $H(x)=\frac3{32}(4x-x^3/3)$.

**(b)** Symmetry puts half the area to each side of zero: $\boxed{1/2}$.

**(c)**

$$
P(-1<X<1)=H(1)-H(-1)
=\frac3{32}\left(8-\frac23\right)=\boxed{\frac{11}{16}=0.6875}.
$$

**(d)** The two requested tails are the complement of the central interval:

$$
1-[H(1/2)-H(-1/2)]
=1-\frac{47}{128}=\boxed{\frac{81}{128}=0.6328125}.
$$

**Check:** The smaller central interval has less probability than the larger one; all endpoint equalities have zero probability.

<a id="m04"></a>

### MMSA #4 — Medium Practice

**Source:** §4.1, printed pp200–201 / PDF pp212–213. **Supplementary model:** the named Rayleigh family does not appear in the Week 7 slides. Normalization, area, and CDF calculations use **PT-10, PT-11, PT-13**; no new Rayleigh PT is established.

**Question:** Wind-turbine power $X$ in MW has candidate PDF

$$
f_X(x;\theta)=\frac{x}{\theta^2}e^{-x^2/(2\theta^2)},\quad x>0,
$$

zero otherwise, with $\theta>0$. (a) Verify a legitimate PDF. For $\theta=100$, (b) find the probability power is at most 200, less than 200, and at least 200; (c) find the probability it is between 100 and 200. (d) Give its CDF.

**(a)** All factors are nonnegative. Since the derivative of $e^{-x^2/(2\theta^2)}$ is $-(x/\theta^2)e^{-x^2/(2\theta^2)}$,

$$
\int_0^\infty f_X(x;\theta)dx
=[-e^{-x^2/(2\theta^2)}]_0^\infty=0-(-1)=1.
$$

The infinite endpoint is an improper-integral limit, an exercise-specific **Supplementary** step.

**(b)** For $\theta=100$, the exponent at 200 is $-2$. Thus

$$
P(X\le200)=P(X<200)=\boxed{1-e^{-2}\approx0.864665},
\quad P(X\ge200)=\boxed{e^{-2}\approx0.135335}.
$$

**(c)**

$$
P(100\le X\le200)=e^{-1/2}-e^{-2}=\boxed{0.471195\text{ approximately}}.
$$

**(d)**

$$
F_X(x)=\begin{cases}0,&x\le0,\\1-e^{-x^2/(2\theta^2)},&x>0.\end{cases}
$$

It starts at zero, increases, tends to one, and differentiates to the specified density. The [gallery](figures/textbook-densities.png) includes the $\theta=100$ shape.

<a id="m05"></a>

### MMSA #5 — Basic Practice

**Source:** §4.1, printed p201 / PDF p213; instructor locator p200. **PT-10, PT-11.**

**Question:** A professor always finishes within two minutes after the hour and never before it. Time $X$ in minutes has PDF $kx^2$ on $[0,2]$, zero otherwise. (a) Find $k$. (b) Find the probability the lecture ends within one minute after the hour. (c) Find the probability it continues for between 60 and 90 seconds after the hour. (d) Find the probability it continues at least 90 seconds after the hour.

**(a)** [A10](#a10) gives the complete normalization and $k=3/8$.

For the remaining parts, $\int_0^x(3/8)u^2du=x^3/8$ inside the support.

**(b)**

$$
P(X\le1)=\frac{1^3}{8}=\boxed{\frac18=0.125}.
$$

**(c)** Convert seconds to minutes before integrating: $60\text{ s}=1$ min, $90\text{ s}=1.5$ min.

$$
P(1\le X\le1.5)=\frac{(3/2)^3-1}{8}=\boxed{\frac{19}{64}=0.296875}.
$$

**(d)**

$$
P(X\ge1.5)=1-\frac{(3/2)^3}{8}=\boxed{\frac{37}{64}=0.578125}.
$$

**Check:** The regions in (b), (c), and (d) partition the support up to zero-probability endpoints; their probabilities sum to one. The actual density is drawn in the [gallery](figures/textbook-densities.png).

<a id="m06"></a>

### MMSA #6 — Medium Practice

**Source:** §4.1, printed p201 / PDF p213. **PT-10, PT-11.**

**Question:** Graduating seniors' GPA $X$ has candidate PDF $k[1-(x-3)^2]$ on $2\le x\le4$, zero elsewhere. (a) Sketch it. (b) Find $k$. (c) Find $P(X>3)$. (d) Find the probability GPA is within 0.25 of 3. (e) Find the probability GPA differs from 3 by more than 0.5.

**(a)** The [gallery](figures/textbook-densities.png) shows a symmetric downward parabola centered at 3, meeting zero at 2 and 4. **(b)** Put $u=x-3$:

$$
1=k\int_{-1}^1(1-u^2)du=k\left[u-\frac{u^3}{3}\right]_{-1}^1
=\frac{4k}{3},\quad\boxed{k=3/4}.
$$

**(c)** Symmetry gives $\boxed{P(X>3)=1/2}$.

**(d)** The event is $-1/4\le u\le1/4$:

$$
\frac34\int_{-1/4}^{1/4}(1-u^2)du
=\frac34\left(\frac12-\frac1{96}\right)
=\boxed{\frac{47}{128}=0.3671875}.
$$

**(e)** Use the complement of $|u|\le1/2$:

$$
1-\frac34\left[u-\frac{u^3}{3}\right]_{-1/2}^{1/2}
=1-\frac{11}{16}=\boxed{\frac5{16}=0.3125}.
$$

**Check:** The normalized density is nonnegative throughout its support; symmetry and probability bounds agree with the calculations.

<a id="m07"></a>

### MMSA #7 — Basic Practice

**Source:** §4.1, printed p201 / PDF p213; instructor locator p200. **Supplementary model:** Uniform$(25,35)$. **PT-12** for (b,d); **PT-14** supplies percentile reasoning for (c).

**Question:** Laboratory preparation time $X$ in minutes is uniform from 25 to 35. (a) Write and sketch its PDF. (b) Find $P(X>33)$. (c) Find the probability preparation time is within two minutes of the median, identifying that median from the graph. (d) For $25<a<a+2<35$, find $P(a<X<a+2)$ and interpret it.

**(a)** Constant height times ten-minute width must equal one:

$$
f_X(x)=\begin{cases}1/10,&25\le x\le35,\\0,&\text{otherwise}.\end{cases}
$$

See the flat rectangle in the [gallery](figures/textbook-densities.png).

**(b,d)** The full length-ratio solutions are [A12](#a12).

**(c)** Half the rectangular area lies on each side of 30, so the median is 30 minutes. Being within two minutes means $28\le X\le32$:

$$
P(28\le X\le32)=\frac{32-28}{35-25}=\boxed{0.4}.
$$

**Interpretation of (d):** Every complete two-minute interval strictly inside this support has the same probability; the exact location $a$ is irrelevant for a uniform density.

<a id="m08"></a>

### MMSA #8 — Medium Practice

**Source:** §4.1, printed p201 / PDF p213. **PT-10, PT-11.** The exercise supplies the total-wait density; no convolution technique is introduced.

**Question:** A commute requires two buses, each with waiting time uniform on $[0,5]$ minutes. The supplied PDF for total waiting time $Y$ is

$$
f_Y(y)=\begin{cases}y/25,&0\le y<5,\\(10-y)/25,&5\le y\le10,\\0,&\text{otherwise}.\end{cases}
$$

(a) Sketch the PDF. (b) Verify total area one. Find probabilities that waiting time is (c) at most 3; (d) at most 8; (e) between 3 and 8; (f) either less than 2 or more than 6 minutes.

**(a)** The triangle rises from $(0,0)$ to $(5,1/5)$, then falls to $(10,0)$; see the [gallery](figures/textbook-densities.png). **(b)**

$$
\int_0^5\frac{y}{25}dy+\int_5^{10}\frac{10-y}{25}dy
=\frac12+\frac12=1.
$$

The CDF within the support is $y^2/50$ up to 5 and $1-(10-y)^2/50$ afterward. Consequently:

| Part | Event and setup | Answer |
| --- | --- | --- |
| (c) | $P(Y\le3)=3^2/50$ | $\boxed{9/50=0.18}$ |
| (d) | $P(Y\le8)=1-(10-8)^2/50$ | $\boxed{23/25=0.92}$ |
| (e) | $P(3\le Y\le8)=0.92-0.18$ | $\boxed{37/50=0.74}$ |
| (f) | $P(Y<2)+P(Y>6)=2^2/50+(10-6)^2/50$ | $\boxed{2/5=0.4}$ |

The regions in (f) are disjoint, so they are added, not intersected. Strict endpoints do not change these density-model probabilities.

<a id="m09"></a>

### MMSA #9 — Basic Practice

**Source:** §4.1, printed p201 / PDF p213, referring to Example 4.5 on printed p193 / PDF p205. **PT-11.**

**Question with the referenced information restored:** Hazardous flood rate $X$, in $\mathrm{m}^3/\mathrm{s}$, has PDF

$$
f_X(x)=\begin{cases}0.04e^{-0.04(x-10)},&x\ge10,\\0,&x<10.\end{cases}
$$

Find the probability flood rate is (a) at most 40; (b) more than 40, and at least 40; (c) between 40 and 60.

**Supplementary — exercise-specific model:** This flood-rate PDF is supplied by the referenced textbook example, not introduced as a named family in the slides. Its probabilities follow the Core area method.

An antiderivative of the interior density is $-e^{-0.04(x-10)}$, so its accumulated area is $1-e^{-0.04(x-10)}$ for $x\ge10$.

$$
\text{(a)}\quad P(X\le40)=1-e^{-1.2}=\boxed{0.698805788}.
$$

$$
\text{(b)}\quad P(X>40)=P(X\ge40)=e^{-1.2}=\boxed{0.301194212}.
$$

$$
\text{(c)}\quad P(40\le X\le60)=e^{-1.2}-e^{-2}=\boxed{0.165858929}.
$$

The continuous model makes the two inequalities in (b) equivalent. The shift by 10 is essential; replacing the exponent by $-0.04x$ would change the model.

<a id="m10"></a>

### MMSA #10 — Test Level

**Source:** §4.1, printed pp201–202 / PDF pp213–214. **Supplementary model:** Pareto family, absent from the slides. **PT-10, PT-11, PT-13, PT-14** cover the existing normalization/area/CDF/percentile operations. The new family does not establish a new PT.

**Question:** For $k>0,\theta>0$, consider $f_X(x;k,\theta)=k\theta^k/x^{k+1}$ for $x\ge\theta$, zero elsewhere. (a) Sketch the PDF. (b) Verify total integral one. (c) For fixed $b>\theta$, find $P(X\le b)$. (d) For $\theta<a<b$, find $P(a\le X\le b)$. (e) Find the $(100p)$th percentile.

**(a)** At $\theta$ the height is $k/\theta$, and the density decreases toward zero on the infinite right tail. The [gallery](figures/textbook-densities.png) uses the scaled axis $x/\theta$ to show labelled members of this source family; it is a schematic family sketch, not an extra practice scenario.

**(b)** Nonnegativity is immediate. Using an improper-integral limit,

$$
\int_\theta^\infty k\theta^k x^{-k-1}dx
=[-\theta^kx^{-k}]_\theta^\infty=1,
$$

because $k>0$ makes the upper endpoint zero. The unbounded-tail limit is **Supplementary**.

**(c)** $\boxed{P(X\le b)=1-(\theta/b)^k}$.

**(d)** Subtract accumulated areas, or integrate directly:

$$
P(a\le X\le b)=\boxed{(\theta/a)^k-(\theta/b)^k}.
$$

**(e)** Solve $1-(\theta/x_p)^k=p$, with $0<p<1$:

$$
x_p=\boxed{\frac{\theta}{(1-p)^{1/k}}}.
$$

This lies above $\theta$, approaches $\theta$ as $p\downarrow0$, and grows without bound as $p\uparrow1$, checking the support and tail behaviour.

<a id="m11"></a>

### MMSA #11 — Basic Practice

**Source:** §4.1, printed p202 / PDF p214; instructor locator p200. **PT-13, PT-14.** Shared duration definition restored from #1: $X$ is checkout time in hours, with

$$
F_X(x)=\begin{cases}0,&x<0,\\x^2/4,&0\le x<2,\\1,&x\ge2.\end{cases}
$$

**Question:** Find (a) $P(X\le1)$; (b) $P(0.5\le X\le1)$; (c) $P(X>0.5)$; (d) median duration; (e) $F_X'(x)$ to obtain the PDF.

**(a)** $F_X(1)=\boxed{1/4}$.

**(b)** $F_X(1)-F_X(0.5)=1/4-1/16=\boxed{3/16}$.

**(c)** $1-F_X(0.5)=\boxed{15/16}$.

**(d)** The median is in $[0,2]$. Solve $m^2/4=1/2$ and retain the nonnegative root:

$$
\boxed{m=\sqrt2\text{ hours}\approx1.414214\text{ hours}}.
$$

**(e)** Differentiate the interior branch:

$$
f_X(x)=\begin{cases}x/2,&0<x<2,\\0,&\text{otherwise}.\end{cases}
$$

The endpoint density values may be assigned differently without changing probabilities. The PDF integrates to one and accumulates back to the given CDF, checking the conversion. This same duration distribution is used in #18.

<a id="m12"></a>

### MMSA #12 — Medium Practice

**Source:** §4.1, printed p202 / PDF p214. **PT-13, PT-14.**

**Question:** The measurement-error CDF from #3 is

$$
F_X(x)=\begin{cases}0,&x<-2,\\\frac12+\frac3{32}(4x-x^3/3),&-2\le x<2,\\1,&x\ge2.\end{cases}
$$

(a) Compute $P(X<0)$. (b) Compute $P(-1<X<1)$. (c) Compute $P(0.5<X)$. (d) Differentiate to verify the PDF in #3. (e) Verify the median is zero.

**(a)** $F_X(0)=\boxed{1/2}$.

**(b)** $F_X(1)-F_X(-1)=\boxed{11/16}$, agreeing with #3(c).

**(c)** $F_X(1/2)=1/2+3/16-1/256=175/256$, hence

$$
P(X>1/2)=\boxed{81/256=0.31640625}.
$$

**(d)** For $-2<x<2$, $F_X'(x)=\frac3{32}(4-x^2)$; outside the support it is zero, reproducing #3. **(e)** $F_X(0)=1/2$ and the CDF is strictly increasing inside the support, so the median is $\boxed{0}$.

**Check:** Twice the one-sided tail in (c) equals #3(d)'s two-sided probability, as symmetry requires.

<a id="m13"></a>

### MMSA #13 — Test Level

**Source:** §4.1, printed p202 / PDF p214. **PT-10, PT-11, PT-13.** **Supplementary:** unbounded power-tail model and its improper-integral limit; no new tail-model PT.

**Question:** Traffic time headway $X$ in seconds has candidate PDF $k/x^4$ for $x>1$, zero otherwise. (a) Determine $k$. (b) Obtain the CDF. (c) Use it to find headway exceeding two seconds and headway between two and three seconds.

**(a)**

$$
1=k\int_1^\infty x^{-4}dx
=k[-x^{-3}/3]_1^\infty=k/3,
\quad\boxed{k=3}.
$$

**(b)** Integrating from the support boundary gives

$$
F_X(x)=\begin{cases}0,&x\le1,\\1-x^{-3},&x>1.\end{cases}
$$

**(c)**

$$
P(X>2)=1-F_X(2)=\boxed{1/8},
$$

$$
P(2<X<3)=F_X(3)-F_X(2)
=\frac18-\frac1{27}=\boxed{\frac{19}{216}\approx0.087963}.
$$

The CDF tends to one and differentiates to $3x^{-4}$, checking both normalization and conversion.

<a id="m18"></a>

### MMSA #18 — Basic Practice

**Source:** §4.2, printed p210 / PDF p222, referring to #1 and #11. **PT-15.**

**Complete question:** For checkout duration $X$ in hours, PDF $x/2$ on $[0,2]$ and zero elsewhere, find (a) $E(X)$; (b) $V(X)$ and $\sigma_X$; (c) expected charge for $h(x)=x^2$.

**Canonical full solution:** [A15](#a15). It supplies every integral, variance/SD, expected charge, and units. No extra MGF task is inferred from the broader section title.

<a id="m20"></a>

### MMSA #20 — Medium Practice

**Source:** §4.2, printed p210 / PDF p222. **Supplementary model:** uniform fracture-risk index, absent from slides. **PT-12, PT-13, PT-15** supply the calculation methods.

**Question:** The dimensionless midpoint fracture risk index (mFRI) $X$ is uniform on $[0.55,1.45]$. (a) Find its mean and SD. (b) Determine its CDF. (c) Find the probability mFRI is less than 1, and between 0.75 and 1.25. (d) Find the probability it is within one SD of its mean and within two SDs.

**(a)** The constant density is $1/0.9$. Integrating gives

$$
E(X)=\frac1{0.9}\left[\frac{x^2}{2}\right]_{.55}^{1.45}=\boxed{1}.
$$

For the variance, center at 1, so $u=x-1\in[-.45,.45]$:

$$
V(X)=\frac1{.9}\int_{-.45}^{.45}u^2du
=\frac{.9^2}{12}=\frac{27}{400},
\quad\sigma=\boxed{\frac{3\sqrt3}{20}\approx0.259808}.
$$

**(b)**

$$
F_X(x)=\begin{cases}0,&x<.55,\\(x-.55)/.9,&.55\le x\le1.45,\\1,&x>1.45.\end{cases}
$$

Its [CDF graph](figures/textbook-cdfs.png) is a straight ramp, constant outside the support.

**(c)** Length ratios give $\boxed{P(X<1)=1/2}$ and $\boxed{P(.75\le X\le1.25)=.5/.9=5/9}$.

**(d)** One-SD endpoints stay inside the support, so coverage is

$$
\frac{2\sigma}{.9}=\boxed{1/\sqrt3\approx0.577350}.
$$

The two-SD interval is approximately $[0.480385,1.519615]$, containing the entire support. Its probability is therefore $\boxed{1}$, not an untruncated length ratio greater than one. This checks why event/support intersection matters.

<a id="m22"></a>

### MMSA #22 — Medium Practice

**Source:** §4.2, printed p210 / PDF p222, referring to the full GPA PDF in #6. **PT-13, PT-14, PT-15.**

**Question with shared information restored:** $X$ has PDF $\frac34[1-(x-3)^2]$ on $[2,4]$, zero elsewhere. (a) Obtain and graph its CDF. (b) Determine its median from the PDF graph. (c) Compute $E(X)$ and $V(X)$.

**(a)** Put $u=x-3$ and integrate from $u=-1$ to $u=x-3$:

$$
F_X(x)=\begin{cases}
0,&x<2,\\
\frac12+\frac34(x-3)-\frac14(x-3)^3,&2\le x\le4,\\
1,&x>4.
\end{cases}
$$

The [CDF graph](figures/textbook-cdfs.png) rises smoothly from $(2,0)$ to $(4,1)$, steepest near 3.

**(b)** The PDF is symmetric about 3, so each side has half the area: median $\boxed{3}$. Directly, $F_X(3)=1/2$.

**(c)** For $U=X-3$, the density is $\frac34(1-u^2)$ on $[-1,1]$. The mean integral for $U$ vanishes by odd symmetry, and

$$
E(U^2)=\frac34\int_{-1}^{1}(u^2-u^4)du
=\frac34\left(\frac23-\frac25\right)=\frac15.
$$

Thus $\boxed{E(X)=3}$ and $\boxed{V(X)=1/5}$. Equivalently $E(X^2)=9+1/5=46/5$, and subtracting $3^2$ gives the same variance. Median and mean coincide here because of the symmetric density; they do not coincide for every distribution.

<a id="m24"></a>

### MMSA #24 — Test Level

**Source:** §4.2, printed pp210–211 / PDF pp222–223, referring to #8. **PT-13, PT-14, PT-15.**

**Question with shared PDF restored:** For total bus waiting time $Y$ in minutes, PDF $y/25$ on $[0,5)$, $(10-y)/25$ on $[5,10]$, zero elsewhere: (a) compute and sketch the CDF; (b) obtain the $(100p)$th percentile, treating $p<1/2$ and $p\ge1/2$ separately; (c) compute $E(Y)$ and $V(Y)$ and compare with a single uniform $[0,5]$ waiting time.

**(a)** Below five, integrate the first branch. Above five, retain the already accumulated $1/2$:

$$
F_Y(y)=\begin{cases}
0,&y<0,\\y^2/50,&0\le y<5,\\1-(10-y)^2/50,&5\le y\le10,\\1,&y>10.
\end{cases}
$$

The [CDF graph](figures/textbook-cdfs.png) joins at $(5,1/2)$; its slope first increases, then decreases.

**(b)** For $0<p<1/2$, $y_p^2/50=p$; for $1/2\le p<1$, $(10-y_p)^2/50=1-p$. The supported roots are

$$
y_p=\boxed{\begin{cases}\sqrt{50p},&0<p<1/2,\\10-\sqrt{50(1-p)},&1/2\le p<1.\end{cases}}
$$

Both expressions agree at $p=1/2$, giving a median of five minutes.

**(c)** Split the moment integrals:

$$
E(Y)=\frac1{25}\left\{\int_0^5y^2dy+\int_5^{10}(10y-y^2)dy\right\}=\boxed{5},
$$

$$
E(Y^2)=\frac1{25}\left\{\int_0^5y^3dy+\int_5^{10}(10y^2-y^3)dy\right\}=\frac{175}{6}.
$$

Therefore $\boxed{V(Y)=175/6-25=25/6}$ minutes squared. For one uniform $[0,5]$ wait $W$, direct integration gives $E(W)=5/2$ and $V(W)=25/12$: total-wait mean and variance are each twice the single-wait values. The supplied total PDF is consistent with adding independent waits; no convolution derivation is required by this exercise. The single-wait uniform model is **Supplementary** as in #7.

<a id="m25"></a>

### MMSA #25 — Test Level

**Source:** §4.2, printed p211 / PDF p223. **PT-15.**

**Question:** A circular ecological sampling region was intended to have radius ten metres, but actual radius $R$ has PDF $\frac34[1-(10-r)^2]$ on $9\le r\le11$, zero elsewhere. Find the expected area of the resulting circle.

**Worked solution.** Area is $A=\pi R^2$; the function to average is $\pi r^2$, not merely the radius. Put $u=r-10$:

$$
E(A)=\frac{3\pi}{4}\int_{-1}^{1}(u+10)^2(1-u^2)du.
$$

Expand $(u+10)^2=u^2+20u+100$. The odd term integrates to zero; the remaining integrals are

$$
\frac34\int_{-1}^1(1-u^2)du=1,
\qquad\frac34\int_{-1}^1u^2(1-u^2)du=\frac15.
$$

**Answer:**

$$
E(A)=\pi\left(100+\frac15\right)
=\boxed{\frac{501\pi}{5}\text{ m}^2\approx314.787584\text{ m}^2}.
$$

Using $\pi[E(R)]^2=100\pi$ would lose the contribution from radius variability. This is an expectation-of-a-function question, not a request for the distribution of area.

<a id="m26"></a>

### MMSA #26 — Test Level

**Source:** §4.2, printed p211 / PDF p223. **PT-13, PT-14, PT-15** for the existing operations. Part (e)'s inventory-payoff construction has **No matching PT established by the slide/Basic source set**; it is handled locally rather than added to PT-15's evidenced tasks.

**Question:** Weekly propane demand $X$, measured in thousands of gallons, has PDF $2(1-x^{-2})$ on $1\le x\le2$, zero elsewhere. (a) Compute the CDF. (b) Obtain the $(100p)$th percentile and median. (c) Compute the mean and compare it with the median. (d) Compute variance and SD. (e) If 1.5 thousand gallons are initially available with no resupply, find the expected amount of that stock left at week's end.

**(a)** The antiderivative of $2-2x^{-2}$ is $2x+2/x$, and its value at 1 is 4:

$$
F_X(x)=\begin{cases}0,&x<1,\\2x+2/x-4,&1\le x\le2,\\1,&x>2.\end{cases}
$$

It gives zero at 1 and one at 2, checking normalization.

**(b)** Solve $2x+2/x-4=p$. Multiplying by positive $x$ gives $2x^2-(4+p)x+2=0$. For $0<p<1$, the minus root lies below 1; the supported root is

$$
x_p=\boxed{\frac{4+p+\sqrt{(4+p)^2-16}}{4}}.
$$

At $p=1/2$, median $\boxed{(9+\sqrt{17})/8\approx1.640388}$ thousand gallons.

**(c)**

$$
E(X)=\int_1^22(x-x^{-1})dx
=[x^2-2\log x]_1^2
=\boxed{3-2\log2\approx1.613706}.
$$

The mean is slightly below the median; both lie in $[1,2]$.

**(d)**

$$
E(X^2)=\int_1^22(x^2-1)dx
=[2x^3/3-2x]_1^2=\frac83.
$$

Therefore

$$
V(X)=\boxed{\frac83-(3-2\log2)^2\approx0.062620778},
\quad\sigma_X=\boxed{0.250241439\text{ approximately}}.
$$

Variance units are $(\text{thousand gallons})^2$; SD units are thousand gallons.

**(e) Supplementary — exercise-specific payoff:** Remaining stock cannot be negative. Its function is $h(x)=1.5-x$ for $1\le x\le1.5$, and zero for larger demand. Thus

$$
\begin{aligned}
E[h(X)]&=\int_1^{3/2}(3/2-x)2(1-x^{-2})dx\\
&=[3x-x^2+3/x+2\log x]_1^{3/2}\\
&=\boxed{2\log(3/2)-3/4\approx0.060930216\text{ thousand gallons}}.
\end{aligned}
$$

This is approximately **60.930216 gallons**. Simply computing $1.5-E(X)$ would give a negative result and describe an unbounded signed balance rather than stock actually left.

<a id="m28"></a>

### MMSA #28 — Test Level

**Source:** §4.2, printed p211 / PDF p223, referring to the Pareto PDF in #10. **Supplementary:** Pareto moments and convergence conditions. **No matching PT established by the slide/Basic source set** covers classifying finite versus divergent moments; the expectation integral is familiar, but the tail question is not used to expand the PT list.

**Question:** For $f_X(x)=k\theta^k/x^{k+1}$ on $x\ge\theta>0$: (a) compute $E(X)$ for $k>1$; (b) discuss $E(X)$ for $k=1$; (c) for $k>2$, show $V(X)=k\theta^2/[(k-1)^2(k-2)]$; (d) discuss variance for $k=2$; (e) determine conditions on $k$ for $E(X^n)$ to be finite, for positive integer $n$.

**General integral for these subparts:**

$$
E(X^n)=k\theta^k\int_\theta^\infty x^{n-k-1}dx.
$$

The tail integral converges exactly when $n-k-1<-1$, that is, $k>n$. In that case,

$$
E(X^n)=k\theta^k\left[\frac{x^{n-k}}{n-k}\right]_\theta^\infty
=\frac{k\theta^n}{k-n}.
$$

**(a)** Set $n=1$: $\boxed{E(X)=k\theta/(k-1)}$.

**(b)** If $k=1$, the mean integral becomes $\theta\int_\theta^\infty x^{-1}dx=+\infty$. Thus there is **no finite mean**; the positive expectation is infinite.

**(c)** If $k>2$, $E(X^2)=k\theta^2/(k-2)$, and

$$
V(X)=\frac{k\theta^2}{k-2}-\frac{k^2\theta^2}{(k-1)^2}
=\boxed{\frac{k\theta^2}{(k-1)^2(k-2)}}.
$$

To check the algebra, the combined numerator is $k[(k-1)^2-k(k-2)]=k$.

**(d)** At $k=2$, the mean is finite, $2\theta$, but $E(X^2)=+\infty$ by a logarithmically divergent tail. Variance is consequently **infinite**, not obtained by substituting zero into a denominator as if the formula remained finite.

**(e)** $\boxed{k>n}$ is necessary and sufficient for a finite $n$th moment. At $k=n$ the logarithmic integral diverges; for $k<n$ the power integral diverges. This explains why a normalized density need not have finite moments.

**PAR: §§6.1–6.3 — 9 exercises**

<a id="p601"></a>

### PAR #6.1(a–c) — Basic Practice

**Source:** §§6.1–6.3 exercise set, printed p266 / PDF p284. **PT-10, PT-11, PT-15.** Only the assigned parts (a–c) are included; the source's MGF part (d) is deliberately outside the requested set.

**Question:** $X$ has density $f_X(x)=cx$ on $0<x<1$, zero elsewhere. (a) Find $c$. (b) Find $P(X<0.5)$. (c) Find $E(X)$.

**(a)** Nonnegativity requires $c\ge0$, and

$$
1=\int_0^1cx\,dx=c/2,\quad\boxed{c=2}.
$$

**(b)** $P(X<0.5)=\int_0^{1/2}2x\,dx=[x^2]_0^{1/2}=\boxed{1/4}$.

**(c)**

$$
E(X)=\int_0^1x(2x)dx=\left[\frac{2x^3}{3}\right]_0^1=\boxed{2/3}.
$$

The mean lies inside the support and to the right of its midpoint, sensible for this increasing density.

<a id="p602"></a>

### PAR #6.2 — Medium Practice

**Source:** printed pp266–267 / PDF pp284–285; the two requested subparts continue onto p267. **PT-10, PT-15.** **Supplementary:** unbounded-support integrals and the integration-by-parts calculations needed here.

**Question:** $X$ has density $f_X(x)=cx e^{-x/2}$ for $0<x<\infty$, zero elsewhere. (a) Find $c$. (b) Find $E(X)$.

**(a) Supplementary — integration by parts and an improper limit.** Use the [formula and choice-of-factors guide](Study-Notes.md#integration-by-parts). Write $I_1(b)=\int_0^b xe^{-x/2}dx$ for a finite $b>0$. Choose $u=x$, $du=dx$, $dv=e^{-x/2}dx$, and $v=-2e^{-x/2}$. Then

$$
\begin{aligned}
I_1(b)
&=[-2xe^{-x/2}]_0^b+2\int_0^b e^{-x/2}dx\\
&=-2be^{-b/2}+2[-2e^{-x/2}]_0^b\\
&=-2be^{-b/2}+4(1-e^{-b/2}).
\end{aligned}
$$

The polynomial factor has disappeared from the remaining integral, which is why this choice helps. As $b\to\infty$, both $e^{-b/2}$ and $be^{-b/2}$ tend to zero: exponential decay dominates the polynomial. Therefore

$$
I_1=\int_0^\infty xe^{-x/2}dx=\lim_{b\to\infty}I_1(b)=4,
\qquad 1=cI_1=4c,
\qquad\boxed{c=1/4}.
$$

Since $c>0$ and $xe^{-x/2}>0$ on the support, the normalized density is nonnegative as required.

**(b)** Average $x$ against the normalized density:

$$
E(X)=\frac14\int_0^\infty x^2e^{-x/2}dx.
$$

**Supplementary calculation:** Now choose $u=x^2$, $du=2x\,dx$, and keep $dv=e^{-x/2}dx$, $v=-2e^{-x/2}$. For a finite upper bound,

$$
\begin{aligned}
I_2(b)=\int_0^b x^2e^{-x/2}dx
&=[-2x^2e^{-x/2}]_0^b+4\int_0^b xe^{-x/2}dx\\
&=-2b^2e^{-b/2}+4I_1(b).
\end{aligned}
$$

The factor 4 comes from multiplying $v=-2e^{-x/2}$ by $du=2x\,dx$ and applying the minus sign in the formula. The remaining integral is the one from part (a). Taking $b\to\infty$, the boundary term vanishes and $I_1(b)\to4$, so $I_2=4(4)=16$. Consequently,

$$
E(X)=\frac14(16)=\boxed{4}.
$$

Both the normalization and first-moment integrals converge; no Gamma-distribution theory or new named-model PT is needed.

<a id="p603"></a>

### PAR #6.3 — Test Level

**Source:** printed p267 / PDF p285. **PT-13** for (a–c). Part (d)'s conditional-CDF calculation has **No matching PT established by the slide/Basic source set**; its conditional-probability step is labelled Supplementary.

**Question:** A nonnegative continuous RV $X$ has CDF $F$. Give numbers or expressions in $F$ for (a) $F(-5)$; (b) $P(3<X<11)$; (c) the limit of $F(x)$ as $x\to\infty$; (d) $P(X>12\mid X>6)$.

**(a)** Nonnegativity excludes all observations below zero, so $\boxed{F(-5)=0}$.

**(b)** There is no point mass at either endpoint, so $\boxed{F(11)-F(3)}$.

**(c)** Every CDF approaches one at plus infinity: $\boxed{1}$.

**(d) Supplementary — conditional probability:** The event $\{X>12\}$ is contained in $\{X>6\}$, so their intersection is the former. Provided $1-F(6)>0$,

$$
P(X>12\mid X>6)
=\frac{P(X>12)}{P(X>6)}
=\boxed{\frac{1-F(12)}{1-F(6)}}.
$$

If the conditioning event has probability zero, the elementary conditional probability is undefined. Since $F(12)\ge F(6)$, the ratio, when defined, is between zero and one.

<a id="p604"></a>

### PAR #6.4 — Basic Practice

**Source:** printed p267 / PDF p285; instructor locator p266. **PT-13.**

**Question:** Months $X$ from diagnosis to death in a cancer-patient population have CDF $F_X(x)=1-\exp(-0.03x^{1.2})$ for $x>0$. (a) Find the probability of surviving at least 12 months. (b) Find the PDF.

**Full CDF for a nonnegative survival time:** $F_X(x)=0$ for $x\le0$, with the given expression for $x>0$. It joins continuously at zero and tends to one.

**(a)** “Survive at least 12 months” is a right-tail event:

$$
P(X\ge12)=1-F_X(12)
=\boxed{e^{-0.03(12)^{1.2}}\approx0.553357696}.
$$


**(b)** Apply the chain rule to the interior branch:

$$
f_X(x)=\boxed{\begin{cases}0.036x^{0.2}e^{-0.03x^{1.2}},&x>0,\\0,&x\le0.\end{cases}}
$$

It is nonnegative, and its integral is $F_X(\infty)-F_X(0)=1$. The derivative's $0.036x^{0.2}$ factor is essential; dropping it would not differentiate the CDF correctly. No additional named lifetime-family theory is introduced.

<a id="p605"></a>

### PAR #6.5 — Medium Practice

**Source:** printed p267 / PDF p285. **PT-10, PT-11, PT-15.**

**Question:** $X$ has PDF $ce^x$ for $-2<x<2$, zero elsewhere. (a) Find $c$. (b) Find $P(X<-1)$. (c) Find $E(X)$.

**(a)**

$$
1=c\int_{-2}^2e^xdx=c(e^2-e^{-2}),
\quad\boxed{c=\frac1{e^2-e^{-2}}\approx0.137860282}.
$$

The constant is positive. **(b)**

$$
P(X<-1)=c\int_{-2}^{-1}e^xdx
=\boxed{\frac{e^{-1}-e^{-2}}{e^2-e^{-2}}\approx0.032058603}.
$$

**(c) Supplementary — integration by parts.** The expectation setup is $E(X)=c\int_{-2}^2xe^xdx$. Using the [calculus guide](Study-Notes.md#integration-by-parts), choose $u=x$, $du=dx$, $dv=e^xdx$, and $v=e^x$:

$$
\begin{aligned}
\int_{-2}^2xe^xdx
&=[xe^x]_{-2}^2-\int_{-2}^2e^xdx\\
&=(2e^2+2e^{-2})-(e^2-e^{-2})\\
&=e^2+3e^{-2}.
\end{aligned}
$$

Multiplying by the normalization constant gives

$$
E(X)=\frac{[(x-1)e^x]_{-2}^2}{e^2-e^{-2}}
=\boxed{\frac{e^2+3e^{-2}}{e^2-e^{-2}}\approx1.074629441}.
$$

The mean is within the support and positive, agreeing with the higher density on the right. The expectation is not obtained by treating $e^x$ as a constant weight.

<a id="p606"></a>

### PAR #6.6 — Test Level

**Source:** printed p267 / PDF p285. **PT-10, PT-11, PT-13, PT-15** for the existing integral operations. **Supplementary:** this exercise's unbounded power tail and moment-convergence checks; no new PT is added.

**Question:** $X$ has density proportional to $x^{-5}$ for $x>1$. (a) Find the proportionality constant. (b) Find and graph the CDF. (c) Use it to find $P(2<X<3)$. (d) Find the mean and variance.

**(a)** If $f_X(x)=cx^{-5}$, then $1=c\int_1^\infty x^{-5}dx=c/4$, giving $\boxed{c=4}$.

**(b)**

$$
F_X(x)=\begin{cases}0,&x\le1,\\1-x^{-4},&x>1.\end{cases}
$$

The [CDF gallery](figures/textbook-cdfs.png) shows zero before 1 and an increasing, concave-down curve approaching one afterward. **(c)**

$$
P(2<X<3)=F_X(3)-F_X(2)
=\frac1{16}-\frac1{81}=\boxed{\frac{65}{1296}\approx0.050154321}.
$$

**(d)** Compute the first two moments directly:

$$
E(X)=4\int_1^\infty x^{-4}dx=\boxed{\frac43},
\qquad E(X^2)=4\int_1^\infty x^{-3}dx=2.
$$

$$
V(X)=2-\left(\frac43\right)^2=\boxed{\frac29}.
$$

Both moment integrals converge because their power exponents are below $-1$. The CDF derivative returns the normalized PDF, and variance is positive.

<a id="p607"></a>

### PAR #6.7 — Medium Practice

**Source:** printed p267 / PDF p285; instructor locator p266. **PT-13, PT-11, PT-15.**

**Question:** The CDF is

$$
F_X(x)=\begin{cases}0,&x\le0,\\\sin x,&0<x\le\pi/2,\\1,&x>\pi/2.\end{cases}
$$

(a) Give the density. (b) Find $P(0.1<X<0.2)$. (c) Find $E(X)$.

**(a)** Differentiate the interior and constant branches:

$$
f_X(x)=\begin{cases}\cos x,&0<x<\pi/2,\\0,&\text{otherwise}.\end{cases}
$$

**(b)** $\boxed{\sin(0.2)-\sin(0.1)\approx0.098835914}$, with angles in radians.

**(c) Supplementary — integration by parts.** First set up the mean using the density: $E(X)=\int_0^{\pi/2}x\cos x\,dx$. Following the [calculus guide](Study-Notes.md#integration-by-parts), choose $u=x$, $du=dx$, $dv=\cos x\,dx$, and $v=\sin x$. Then

$$
\begin{aligned}
E(X)
&=[x\sin x]_0^{\pi/2}-\int_0^{\pi/2}\sin x\,dx\\
&=\frac{\pi}{2}-[-\cos x]_0^{\pi/2}\\
&=\frac{\pi}{2}-(0-(-1)).
\end{aligned}
$$

Thus

$$
E(X)=[x\sin x+\cos x]_0^{\pi/2}
=\boxed{\pi/2-1\approx0.570796327}.
$$

Check: $\cos x$ is nonnegative on the support and integrates to one; the mean lies between zero and $\pi/2$.

<a id="p613"></a>

### PAR #6.13 — Test Level

**Source:** printed p268 / PDF p286; instructor locator p267. **Supplementary — combining densities with weights. No matching PT established by the slide/Basic source set** covers this general coefficient-condition task. It reinforces, but does not expand, PT-10's PDF conditions.

**Question:** Suppose $f$ and $g$ are PDFs. Under what conditions on constants $a,b$ is $h(x)=af(x)+bg(x)$ a PDF?

**Worked solution.** A PDF must normalize and be nonnegative. Since each given density integrates to one,

$$
\int h(x)dx=a\int f(x)dx+b\int g(x)dx=a+b.
$$

Thus $\boxed{a+b=1}$ is necessary. A standard condition that also guarantees nonnegativity for any pair of PDFs is

$$
\boxed{a\ge0,\quad b\ge0,\quad a+b=1}.
$$

**Important qualification:** For a particular fixed pair $f,g$, nonnegative individual coefficients are sufficient but not always necessary. The exact conditions are $a+b=1$ and $af(x)+bg(x)\ge0$ throughout the density. For example, if $f=g$, any coefficients summing to one give $h=f$, even if a coefficient is negative. If a guarantee is required for arbitrary PDFs, nonnegative weights are needed; disjoint-support densities demonstrate why a negative coefficient can otherwise create negative density.

**Answer:** Use nonnegative weights summing to one for the usual mixture construction, while retaining the distinction between a universal guarantee and the exact condition for particular densities. Merely checking the integral is insufficient.

<a id="p615"></a>

### PAR #6.15 — Medium Practice

**Source:** printed p268 / PDF p286; instructor locator p266. **Core property / clarification:** linearity is used on slide 4 and follows from slide 24's expectation rule. The general proof is not used to create an additional PT; PT-15 supplies the expectation setup.

**Question:** For continuous $X$ and constants $a,b$, prove $E(aX+b)=aE(X)+b$.

**Worked solution.** Assume $E(X)$ is finite so the stated finite-mean identity is well-defined. Using the density of $X$ to average the function $ax+b$,

$$
\begin{aligned}
E(aX+b)
&=\int_{-\infty}^{\infty}(ax+b)f_X(x)dx\\
&=a\int_{-\infty}^{\infty}xf_X(x)dx
+b\int_{-\infty}^{\infty}f_X(x)dx\\
&=\boxed{aE(X)+b}.
\end{aligned}
$$

The second integral equals one by normalization. No density for $aX+b$ needs to be derived. The result concerns an affine function; it does not justify $E(X^2)=[E(X)]^2$.

<a id="revision"></a>

## D. Source-Based Revision Index

Use these **existing source questions** in the order below. Attempt the original task first, then reveal its linked solution. No numbers or subparts have been changed.

| Stage | Questions to redo | What the actual questions test |
| --- | --- | --- |
| 1. Discrete model structure | [L05, all five source questions](#l05) | Count, waiting, replacement, and competing stopping rules |
| 2. Discrete reasoning | [Poisson derivation](Study-Notes.md#pt06), [waiting means](Study-Notes.md#pt07), [mechanic parts (a–d)](#l01) | Derivations, transformed revenue, and guaranteed versus actual interval coverage |
| 3. First density practice | [MMSA #3](#m03), [#5](#m05), [PAR #6.1(a–c)](#p601) | All three Basic PDF exercises, including sign, normalization, area, and mean |
| 4. Other Basic models | [MMSA #7](#m07), [#9](#m09) | Uniform lengths and the provided flood-rate density |
| 5. CDF and percentiles | [MMSA #11](#m11), [PAR #6.4](#p604), [slide 22 median](Study-Notes.md#pt14), [piecewise slide 20](#l10) | CDF use, branch handling, differentiation, and inversion |
| 6. Moments and functions | [MMSA #18](Study-Notes.md#pt15), [gas pump](#l14), [MMSA #25](#m25) | Density-weighted averages, square versus mean square, and units |
| 7. Requested combined exercises | [MMSA #24](#m24), [#26](#m26), [PAR #6.3](#p603), [#6.15](#p615) | Piecewise quantiles/moments, inventory function, conditional probability, and linearity |
| 8. Supplementary source tasks | [MMSA #28](#m28), [PAR #6.6](#p606), [#6.13](#p613) | Convergence and density-combination conditions, without inventing new PTs |

All eight Basic exercise numbers have entries here: MMSA #3,5,7,9,11,18 and PAR #6.1(a–c),6.4. The [textbook inventory](#textbooks) also retains every requested Medium and Test exercise, including those not singled out in this revision route.

<a id="coverage"></a>

## E. Coverage and Unresolved-Items Appendix

### Source review and reading status

| Source | Role and actual review | Used for |
| --- | --- | --- |
| Week7-L0401-annotated.pdf, PDF/slide pp1–29 | Primary; every page visually inspected, including annotations and graphs | Six concepts, 15 evidenced PTs, 14 slide-task groups |
| MMSA §§4.1–4.2 and specified exercises | Relevant/supporting; actual question pages and required shared definitions inspected | 18 requested exercises; no MGF exercises imported |
| MMSA Example 4.5, printed p193 / PDF p205 | Necessary supporting source explicitly referenced by Basic #9 | Complete flood-rate PDF and units |
| MMSA #1, printed p200 / PDF p212 | Shared definition only, not an extra assigned exercise | Checkout-duration definition needed by #11/#18 |
| PAR §§6.1–6.3 and specified exercises | Relevant/supporting; requested problems on printed pp266–268 inspected | Nine requested exercises; #6.1 limited to (a–c) |
| Instructor Week 7 list as transcribed in the authorized prompt | Exercise identities and difficulty labels | Eight Basic, ten Medium, nine Test Level exercise numbers |

Neither assigned-reading status nor additional platform assignments were inferred. Section headings elsewhere in a textbook do not authorize importing joint densities, MGF theory, or other neighboring topics.

### Learning outcomes and source tasks

| Outcome / source range | Concepts and coverage |
| --- | --- |
| Discrete learning outcomes, slides 2 and 11 | C-01–C-02; the five actual model-selection questions in L05 and the calculations/derivations in L01–L04 |
| Continuous RV versus discrete, slides 13–15 | C-03; L06 and the support comparison in L03 |
| PMF versus PDF | C-01/C-03; point probabilities and density-area examples in L06–L07 |
| PDF–CDF conversion, slides 18–20 | C-04/PT-13; L08–L10; textbook CDF questions |
| Probabilities and percentiles, slides 16–22 | C-03–C-05; PT-10–PT-14; L07–L11 |
| Expected values/functions, slides 24–25 | C-06/PT-15; L13 and the exact source transformations |
| Variance, SD, and units, slides 26–28 | C-06; L12's explicit proof and L14's complete pump calculation |

The discrete-outcome list already checks several prior-week items as completed. The notes review their models as needed for Week 7 source questions, rather than duplicating a full previous-week course. In particular, no standalone new Binomial–Poisson approximation PT is invented from that outcome list.

### PT evidence and ownership

| PT | One primary owner | Eligible establishing evidence |
| --- | --- | --- |
| PT-01 | C-01 | slide 3(a), slide 9 question 2 |
| PT-02 | C-01 | slide 10 question 3 |
| PT-03 | C-01 | slide 7 PMF/support task, slide 10 question 4 |
| PT-04 | C-01 | slide 10 question 5 with sampling annotation |
| PT-05 | C-01 | slide 9 question 1 |
| PT-06 | C-02 | slide 6 explicit Poisson derivation |
| PT-07 | C-02 | slide 8 explicit waiting-mean derivations |
| PT-08 | C-02 | slides 3(b), 4(c) |
| PT-09 | C-02 | slides 4(d)–5 |
| PT-10 | C-03 | slide 16(a); MMSA Basic #5(a); PAR Basic #6.1(a) |
| PT-11 | C-03 | slide 17(b); MMSA Basic #3(b–d), #5(b–d), #9; PAR Basic #6.1(b) |
| PT-12 — Supplementary | C-03 | MMSA Basic #7(b,d) and its stated uniform assumption |
| PT-13 | C-04 | slides 19–20; MMSA Basic #11(a–c,e); PAR Basic #6.4 |
| PT-14 | C-05 | slide 22, including its CDF annotation; MMSA Basic #11(d) |
| PT-15 | C-06 | MMSA Basic #18(a–c); PAR Basic #6.1(c); slides 27–28 |

Every representative in Study Notes has exactly one matching A-section heading and canonical solution. Medium/Test questions do not establish extra PTs. Formula-fill and identity tasks can link directly to a concept without manufacturing another reusable category.

### Exact exercise accounting and locators

| Book / level | Exercise(s) | Actual printed page(s) | PDF page(s) | Count |
| --- | --- | --- | --- | --- |
| MMSA Basic | #3; #5,7,9; #11; #18 | 200; 201; 202; 210 | 212; 213; 214; 222 | 6 |
| MMSA Medium | #4; #6,8; #12; #20,22 | 200–201; 201; 202; 210 | 212–213; 213; 214; 222 | 6 |
| MMSA Test Level | #10; #13; #24; #25,26,28 | 201–202; 202; 210–211; 211 | 213–214; 214; 222–223; 223 | 6 |
| PAR Basic | #6.1(a–c); #6.4 | 266; 267 | 284; 285 | 2 |
| PAR Medium | #6.2; #6.5,6.7; #6.15 | 266–267; 267; 268 | 284–285; 285; 286 | 4 |
| PAR Test Level | #6.3,6.6; #6.13 | 267; 268 | 285; 286 | 3 |
| Total | 18 MMSA + 9 PAR | All requested continuations included | All locators one-based | **27** |

The instructor list places many exercises at the page on which their set begins. Actual continuations are preserved above. In particular, MMSA #10(e), #4(c–d), and #24(a–c), as well as PAR #6.2(a–b), must not be lost by reading only the first cited page. PAR #6.1(d) is not part of the assignment.

### Supplementary content and unmatched extensions

| Additional material | Why retained / exact location |
| --- | --- |
| Uniform model and length-ratio PT | Required by Basic MMSA #7; C-03, PT-12/A12; also used in #20/#24 |
| Rayleigh and Pareto families; referenced flood-rate model | Required only by MMSA #4, #10/#28, and #9 respectively |
| Improper integrals and power-tail moment convergence | Needed for the specified unbounded-source exercises; C-06, MMSA #4/#10/#13/#28 and PAR #6.2/#6.6 |
| Integration by parts | [Supplementary calculus guide](Study-Notes.md#integration-by-parts) in C-06; explicit worked steps in PAR #6.2, #6.5(c), and #6.7(c) |
| Nonnegative stock-left function | Specific extension in MMSA #26(e); no new PT |
| Conditional probability expressed through CDF tails | PAR #6.3(d); no new PT |
| Weighted combinations of densities and exact nonnegativity qualification | PAR #6.13; no new PT |

The arithmetic/calculus bridges explaining Core formulas remain fully taught; Supplementary labels are not used as an excuse to omit necessary reasoning. Conversely, being a requested exercise does not automatically make a new named distribution lecture Core.

<a id="discrepancies"></a>

### Verified discrepancies and source limitations

1. **Mechanic rate, slide 5:** Slides 3–4 give $2t$, slide 5's R code uses `lambda <- 2*t`, and its output is consistent with a mean of 20 for ten hours. Slide 5's repeated typed statement instead says $3t$. Main solutions use the consistent intended $2t$ model, explicitly recording the conflicting text.
2. **Revenue wording, slides 3–5:** The typed text calls $Y=85R^2-60t$ “average revenue per repair,” while the questions and worked annotations treat $Y$ itself as the workday revenue. Solutions follow that worked interpretation and do not introduce an unsupported additional multiplication by $R$. A literal different economic interpretation would need clarification from the instructor.
3. **Best-of-seven, slide 9 question 1:** The annotation's NB descriptions refer to one-side waiting counts. They cannot alone describe the actual bounded series length with two competing stops. A05 counts both possible winners and enforces the stopping rule.
4. **Library conventions, slide 10:** Question 4 asks total tries but its annotation names failures before non-fiction. A03 distinguishes them. Question 5 references question 4 without restating replacement, but its annotation says without replacement. A04 uses that annotation for the main answer and supplies the replacement alternative so the ambiguity is visible.
5. **Chebyshev endpoints, slides 4–5:** The exact real interval contains integers 12–28. The handwritten outward-rounded 11–29 interval is larger and has different coverage. Both are valid “at least 75%” intervals; their coverages must not be conflated.
6. **CDF existence, slide 18:** Every RV has a CDF. The phrase “if it exists” is not repeated as a restriction. Differentiability of a CDF at every point is also not assumed; slide 20 has a corner.
7. **Variance completion, slide 26:** The annotation says “To finish in Week 8.” The requested proof and slide 28's variance question are solved here because the prompt expressly includes the deck's tasks; they are not represented as necessarily completed in that week's classroom session.

**Remaining limitations:** No requested textbook exercise or visible mathematical subpart is missing. The contradictory rate/revenue wording and library replacement wording are source ambiguities, resolved transparently as stated above, not missing calculations. No inaccessible platform questions have been inferred or invented.

### Verification and retained artifacts

The retained [verification script](scripts/verify_week7.py) checks symbolic normalization, moments, CDF relationships, quantile equations, the competing-stop PMF, interval coverages, and numerical results against direct calculations. Figures in [figures](figures/) reconstruct actual source distributions, graphs, and transformations; family sketches and simulations are labelled as such.

Verification completed: 123 symbolic/numerical checks passed; the exact 27-exercise set, 14 slide-task groups, 15 PT/solution pairs, English-only text, links, figures, headings, tables, and math delimiters were checked. Both files passed Pandoc MathML conversion. Temporary PDF previews were also compiled with LaTeX and representative pages visually inspected for equations, piecewise functions, tables, and figures; this was a representative rendering check, not a page-by-page claim. All six retained figures were visually inspected. Temporary source-extraction and QA files were removed after verification. The two primary content files are Study-Notes.md and Answers-and-Practice.md.
