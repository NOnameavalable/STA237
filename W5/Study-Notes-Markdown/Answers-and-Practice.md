# STA237 Week 5 Answers and Practice: Bounds, Counts, and Waiting Times

## Contents

- [A. Teaching-example solutions](#a-teaching-example-solutions)
- [B. Lecture questions and solutions](#b-lecture-questions-and-solutions)
- [C. Requested textbook exercises](#c-requested-textbook-exercises)
- [D. Original self-test questions](#d-original-self-test-questions)
- [E. Self-test answers](#e-self-test-answers)
- [F. Coverage and unresolved items](#f-coverage-and-unresolved-items)

All source question statements below are **faithful paraphrases**, retaining the data and requested subparts. Page numbers are printed textbook pages unless explicitly labelled PDF pages. Textbook difficulty labels come from the user's screenshot; lecture questions have no supplied difficulty labels. Probability decimals are rounded; displayed sums are the exact model answers.

## A. Teaching-example solutions

### Problem Type PT-01: Moments of a transformed variable

**Question reference:** [PT-01 teaching example](Study-Notes.md#problem-type-pt-01-moments-of-a-transformed-variable).

**Worked solution.** The masses sum to 1. Calculate $E(X)=0(0.2)+1(0.5)+2(0.3)=1.1$ and $E(X^2)=0+0.5+4(0.3)=1.7$, hence $V(X)=1.7-1.1^2=0.49$.

| $x$ | $p_X(x)$ | $C=5x^2+2$ | $C^2$ |
| --- | --- | --- | --- |
| 0 | 0.2 | 2 | 4 |
| 1 | 0.5 | 7 | 49 |
| 2 | 0.3 | 22 | 484 |

Thus $E(C)=2(0.2)+7(0.5)+22(0.3)=10.5$, $E(C^2)=4(0.2)+49(0.5)+484(0.3)=170.5$, and $V(C)=170.5-10.5^2=60.25$. Independently, $E(X^4)=0.5+16(0.3)=5.3$ and $25[5.3-1.7^2]=60.25$.

**Answer.** (a) Mean 1.1 and variance 0.49; (b) mean cost **10.50 dollars**, SD **$\sqrt{60.25}\approx7.7621$ dollars**; (c) $5E(X)^2+2=8.05$ is not the expected cost. The gap $5V(X)=2.45$ confirms the error.

### Problem Type PT-02: Bounding a nonnegative tail

**Question reference:** [PT-02 teaching example](Study-Notes.md#problem-type-pt-02-bounding-a-nonnegative-tail).

**Worked solution.** Nonnegativity and finite mean allow Markov at $a=40$:

$$
P(Y\ge40)\le\frac{12}{40}=0.3,\qquad P(Y<40)=1-P(Y\ge40)\ge0.7.
$$

For a signed measurement, $Y\ge40I_{\{Y\ge40\}}$ can fail on negative outcomes, so its mean alone does not justify this bound.

**Answer.** (a) At most 30%; (b) at least 70%; the same mean is insufficient for the signed variable.

### Problem Type PT-03: Chebyshev event bounds with support checks

**Question reference:** [PT-03 teaching example](Study-Notes.md#problem-type-pt-03-chebyshev-event-bounds-with-support-checks).

**Worked solution.** For integer $X$, the complement of $42\le X\le58$ is $X\le41$ or $X\ge59$, equivalently $|X-50|\ge9$. Hence

$$
P(42\le X\le58)\ge1-\frac{16}{81}=\frac{65}{81}\approx0.802469.
$$

Using the contained open interval $|X-50|<8$ would give only $1-16/64=0.75$. No PMF has been supplied, so there is no exact probability to sum.

**Answer.** At least **80.2469%**; 75% is a valid weaker bound. The exact probability is undetermined.

### Problem Type PT-04: Designing a guaranteed central interval

**Question reference:** [PT-04 teaching example](Study-Notes.md#problem-type-pt-04-designing-a-guaranteed-central-interval).

**Worked solution.** Solve $1-1/k^2\ge0.96$, obtaining $k\ge5$. Set $t=5(2)=10$:

$$
P(20<X<40)\ge0.96.
$$

The larger inclusive interval also has at least this probability.

**Answer.** $(20,40)$, or $[20,40]$, guarantees at least 96%. This gives a lower bound, not exact coverage or a uniquely shortest interval.

### Problem Type PT-05: Bernoulli moments and powers

**Question reference:** [PT-05 teaching example](Study-Notes.md#problem-type-pt-05-bernoulli-moments-and-powers).

**Worked solution.** $P(I=0)=0.85$, $P(I=1)=0.15$. Since $I^8=I$, $E(I^8)=E(I)=0.15$. $V(I)=0.15-0.15^2=0.1275$. For $D=12I+1$, $E(D)=12(0.15)+1=2.8$ and $V(D)=144(0.1275)=18.36$.

**Answer.** (a) The masses above; (b) $E(I)=E(I^8)=0.15$, $V(I)=0.1275$; (c) mean fee **2.80 dollars**, SD **$\sqrt{18.36}\approx4.2849$ dollars**.

### Problem Type PT-06: Expected counts using indicators

**Question reference:** [PT-06 teaching example](Study-Notes.md#problem-type-pt-06-expected-counts-using-indicators).

**Worked solution.** Let $J_i=I_{\{\text{trials }i,i+1\text{ both succeed}\}}$ for $i=1,\ldots,5$. Then $Z=\sum_{i=1}^5J_i$, and $E(J_i)=0.4^2=0.16$. Therefore $E(Z)=5(0.16)=0.8$.

Adjacent pair indicators share a trial. $P(J_i=J_{i+1}=1)=0.4^3=0.064$, whereas $P(J_i=1)P(J_{i+1}=1)=0.4^4=0.0256$. They are dependent. In fact $P(Z=5)=0.4^6$ differs from the probability $0.16^5$ under the proposed $\operatorname{Bin}(5,0.16)$ model.

**Answer.** Expected count **0.8**. Pair indicators are dependent; the proposed binomial model is invalid.

### Problem Type PT-07: Checking a binomial model

**Question reference:** [PT-07 teaching example](Study-Notes.md#problem-type-pt-07-checking-a-binomial-model).

**Worked solution and answer.**

| Part | Model diagnosis |
| --- | --- |
| (a) | Red/not-red is binary, $n=10$ is fixed, and spins are independent with common $p=0.3$: $X\sim\operatorname{Bin}(10,0.3)$. |
| (b) | Without replacement, draws are dependent: exact model $\operatorname{Hypergeo}(N=50,K=30,n=10)$. A sample fraction 20% is not small under MMSA's 5% rule. |
| (c) | Trial count is random because the experiment stops at a target: negative binomial trial count with $r=3,p=0.3$ if the same spins are used. |
| (d) | Common-$p$ condition fails. The count is a sum of independent $\operatorname{Bin}(6,1/4)$ and $\operatorname{Bin}(6,1/2)$ counts, not one binomial with averaged $p$. |

### Problem Type PT-08: Exact binomial event probabilities

**Question reference:** [PT-08 teaching example](Study-Notes.md#problem-type-pt-08-exact-binomial-event-probabilities).

**Worked solution.** Refund is possible only after return, so $p=0.25(0.80)=0.20$. Independence gives $X\sim\operatorname{Bin}(8,0.2)$.

$$
P(X=2)=\binom82(0.2)^2(0.8)^6=0.29360128,
$$

$$
P(2\le X\le4)=\sum_{x=2}^4\binom8x(0.2)^x(0.8)^{8-x}=0.48627712.
$$

**Answer.** (a) 0.2; (b) **0.29360128**; (c) **0.48627712**. R: `dbinom(2,8,.2)` and `pbinom(4,8,.2)-pbinom(1,8,.2)`.

### Problem Type PT-09: Binomial moments and standard-deviation events

**Question reference:** [PT-09 teaching example](Study-Notes.md#problem-type-pt-09-binomial-moments-and-standard-deviation-events).

**Worked solution.** $X\sim\operatorname{Bin}(12,0.3)$, so $\mu=3.6$, $\sigma^2=2.52$, $\sigma\approx1.587451$. The one-SD interval is $[2.012549,5.187451]$, containing integers **3, 4, 5**. Thus the probability is

$$
\sum_{x=3}^5\binom{12}{x}(0.3)^x(0.7)^{12-x}=B(5;12,.3)-B(2;12,.3)\approx0.6293359133.
$$

Revenue $R=2(12)+5X=24+5X$, so $E(R)=24+5(3.6)=42$.

**Answer.** (a) Mean **3.6**, SD **1.587451**; (b) the displayed probability; (c) **42 dollars**. The noninteger lower endpoint excludes 2.

### Problem Type PT-10: Capacity and probability-based decisions

**Question reference:** [PT-10 teaching example](Study-Notes.md#problem-type-pt-10-capacity-and-probability-based-decisions).

**Worked solution.** Let $X\sim\operatorname{Bin}(8,0.55)$ count A buyers. A inventory requires $X\le5$, while B inventory requires $8-X\le5$, or $X\ge3$. Together:

$$
P(3\le X\le5)=\sum_{x=3}^5\binom8x(.55)^x(.45)^{8-x}=0.691413842109375.
$$

**Answer.** **0.691414**. The event $X\le5$ alone includes excessive B demand.

### Problem Type PT-11: Mixture probabilities and model diagnosis

**Question reference:** [PT-11 teaching example](Study-Notes.md#problem-type-pt-11-mixture-probabilities-and-model-diagnosis).

**Worked solution.** Conditional counts are $\operatorname{Bin}(4,.1)$ and $\operatorname{Bin}(4,.5)$, each selected with weight $1/2$. Therefore

$$
P(X=2)=\frac12\binom42(.1)^2(.9)^2+\frac12\binom42(.5)^4=0.2118.
$$

The marginal failure probability is 0.3, so $E(X)=1.2$. But $V(P)=[(.1-.3)^2+(.5-.3)^2]/2=.04$, and $V(X)=4(.3)(.7)+4(3)(.04)=1.32$. A $\operatorname{Bin}(4,.3)$ has variance 0.84. With positive probabilities across the full support $0,\ldots,4$, any binomial representation would require $n=4$ and then $p=.3$, so the mismatch rules it out.

**Answer.** **0.2118**, and the unconditional count is not binomial.

### Problem Type PT-12: First-success waiting times and memorylessness

**Question reference:** [PT-12 teaching example](Study-Notes.md#problem-type-pt-12-first-success-waiting-times-and-memorylessness).

**Worked solution.** Use $T$ for inspections through detection, $p=.25$, $q=.75$. (a) Three nondetections then detection is $P(T=4)=q^3p=.10546875$. (b) $P(T\le4)=1-q^4=.68359375$. (c) $E(T)=1/p=4$. (d) Given $T>3$, more than two additional inspections means $T>5$:

$$
P(T>5\mid T>3)=\frac{q^5}{q^3}=q^2=.5625.
$$

**Answer.** (a) **0.10546875**; (b) **0.68359375**; (c) **4 inspections**; (d) **0.5625**. The conditioning event has positive probability.

### Problem Type PT-13: Waiting for a target number of successes

**Question reference:** [PT-13 teaching example](Study-Notes.md#problem-type-pt-13-waiting-for-a-target-number-of-successes).

**Worked solution.** $T_3$ counts interviews through the third qualified applicant. For $T_3=5$, interview 5 qualifies and two of the preceding four qualify:

$$
P(T_3=5)=\binom42(.4)^3(.6)^2=.13824.
$$

Finishing by 8 is equivalent to at least three qualified applicants in eight interviews:

$$
P(T_3\le8)=1-\sum_{x=0}^2\binom8x(.4)^x(.6)^{8-x}=.68460544.
$$

$E(T_3)=3/.4=7.5$, $V(T_3)=3(.6)/(.4)^2=11.25$. Failures $F_3=T_3-3$ have mean 4.5 and the same variance.

**Answer.** (a) **0.13824**; (b) **0.68460544**; (c) trials mean/variance **7.5, 11.25**, failures mean/variance **4.5, 11.25**.

### Problem Type PT-14: Sampling without replacement

**Question reference:** [PT-14 teaching example](Study-Notes.md#problem-type-pt-14-sampling-without-replacement).

**Worked solution.** $N=12,K=5,n=4$, with support $0,1,2,3,4$:

$$
P(X=x)=\frac{\binom5x\binom7{4-x}}{\binom{12}4},\qquad
P(X=2)=\frac{10(21)}{495}=\frac{14}{33}\approx.424242.
$$

$E(X)=4(5/12)=5/3$ and $V(X)=4(5/12)(7/12)(8/11)=70/99\approx.707071$, so $SD(X)\approx.840875$. With replacement, variance is $4(5/12)(7/12)=35/36\approx.972222$. The ratio $8/11$ is the finite-population correction. Numerators $35,175,210,70,5$ sum to 495, verifying the PMF.

**Answer.** The PMF/support above; $P(X=2)=14/33$; mean **$5/3$**, SD **0.840875**, with a smaller variance than independent with-replacement sampling.

## B. Lecture questions and solutions

The 10 groups below account for explicit examples, proof/completion tasks, and the conceptual prompt embedded in the deck. “Slide” means its printed label; for slides 1–21 it is also the PDF page.

### L-01: Complete expectation and variance properties

**Source:** slide 4. **PTs:** PT-01, PT-06. **Question paraphrase:** Complete $E(a),E(X+a),E(aX),E(aX+b),E(X+Y),E(XY)$ and $V(a),V(X+a),V(aX),V(aX+b),V(X+Y)$; justify the scale properties and identify any additional conditions.

**Worked solution.** For constant $a$, $E(a)=a$. By linearity, the next four expectation expressions are $E(X)+a$, $aE(X)$, $aE(X)+b$, and $E(X)+E(Y)$. For discrete $X$, $E(aX)=\sum_xaxp_X(x)=aE(X)$. If $X,Y$ are independent with integrable products, $E(XY)=E(X)E(Y)$; in general compute the joint expectation rather than multiplying marginal means.

Constants have zero variance. The variance expressions are $0,V(X),a^2V(X),a^2V(X)$, and $V(X)+V(Y)+2\operatorname{Cov}(X,Y)$. Since $(aX+b)-E(aX+b)=a(X-\mu)$, the scale factor is squared. Independence is sufficient for the last covariance to vanish. It is not required for the expectation of a sum.

**Answer and check.** These identities assume the relevant moments exist; equality of a product expectation or additivity of variance alone does not establish independence.

### L-02: Nonlinear appliance repair cost

**Source:** slide 5, adapted from MMSA #28. **PT:** PT-01. **Question paraphrase:** Defect count $X$ has the table below. Verify mean 2.06 and variance 0.9364, then find the mean and SD of repair cost $C=2X^2+3$ in cost units.

| $x$ | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| $p_X(x)$ | .08 | .15 | .45 | .27 | .05 |
| $C(x)$ | 3 | 5 | 11 | 21 | 35 |

**Worked solution.** The masses sum to 1. $E(X)=.15+.90+.81+.20=2.06$, $E(X^2)=.15+1.80+2.43+.80=5.18$. Thus $V(X)=5.18-2.06^2=.9364$ as stated. For cost,

$$
E(C)=2(5.18)+3=13.36.
$$

$E(X^4)=.15+16(.45)+81(.27)+256(.05)=42.02$. Therefore

$$
V(C)=4[42.02-5.18^2]=60.7504,\quad SD(C)=\sqrt{60.7504}\approx7.794254.
$$

Independent direct check: $E(C^2)=9(.08)+25(.15)+121(.45)+441(.27)+1225(.05)=239.24$, and $239.24-13.36^2=60.7504$.

**Answer.** Mean repair cost **13.36 units**, SD **7.7943 units**. The handwritten SD is corrected; the discrepancy is documented in F.

### L-03: Derive the variance shortcut

**Source:** slide 6. **PT:** PT-01. **Question paraphrase:** Expand $E[(X-\mu)^2]$ to obtain the alternative variance formula and explain why the second raw moment differs from the squared mean.

**Worked solution.**

$$
V(X)=E(X^2-2\mu X+\mu^2)=E(X^2)-2\mu E(X)+\mu^2=E(X^2)-\mu^2.
$$

**Answer.** $V(X)=E(X^2)-E(X)^2$. $E(X^2)$ weights squared support values; $E(X)^2$ squares their weighted average. They coincide exactly when $V(X)=0$.

### L-04: What can moments tell us without a distribution?

**Source:** slide 7, bottom conceptual question. **PTs:** PT-02–04. **Question paraphrase:** Can knowing the mean and variance help describe the likelihood of outcomes if the exact distribution is unknown?

**Worked solution and answer.** They give center/spread and distribution-free bounds: use Chebyshev for deviation events; if the variable is nonnegative, Markov can also use its mean. They do not recover a unique distribution or exact event probabilities. At least 75% lie strictly within two SDs when SD is positive; no corresponding universal positive guarantee follows for one SD. A heuristic about “most” values near the center needs this distinction from a proved bound.

### L-05: Prove Markov inequality

**Source:** slide 8. **PT:** PT-02. **Question paraphrase:** For nonnegative $X$ and $a>0$, prove $P(X\ge a)\le E(X)/a$.

**Worked solution.** For a discrete $X$, split the expectation into values below and above $a$:

$$
E(X)=\sum_{x<a}xp_X(x)+\sum_{x\ge a}xp_X(x)
\ge\sum_{x\ge a}xp_X(x)\ge a\sum_{x\ge a}p_X(x)=aP(X\ge a).
$$

**Answer.** Divide by positive $a$. The first inequality uses nonnegativity; equivalently use the pointwise indicator proof, which also handles nondiscrete variables.

### L-06: Prove and interpret Chebyshev inequality

**Source:** slide 9. **PTs:** PT-03–04. **Question paraphrase:** Derive the deviation bound using Markov and state its complementary central-interval interpretation and when it is useful.

**Worked solution.** For $\sigma>0,k>0$, $Y=(X-\mu)^2\ge0$ and $E(Y)=\sigma^2$:

$$
P(|X-\mu|\ge k\sigma)=P(Y\ge k^2\sigma^2)
\le\frac{\sigma^2}{k^2\sigma^2}=\frac1{k^2}.
$$

**Answer.** $P(|X-\mu|<k\sigma)\ge1-1/k^2$, with a positive informative central guarantee for $k>1$. Finite variance is required; use an exact model probability if the PMF is known. If $\sigma=0$, handle the constant variable directly using a positive distance.

### L-07: Tech-support calls

**Source:** slide 10, Example 2(a)–(b). **PTs:** PT-03–04. **Question paraphrase:** Daily call count has mean 115 and SD 10. (a) Bound the fraction of days with 100–130 calls, inclusive. (b) Give a range covering at least 90% of days without specifying a distribution.

**Worked solution.** (a) The basic radius 15 gives $1-100/225=5/9\approx.555556$. Because calls are integer-valued,

$$
\{100\le X\le130\}=\{|X-115|<16\},
$$

so the stronger support-aware bound is $1-100/256=39/64=.609375$.

(b) Set $1-1/k^2=.90$, giving $k=\sqrt{10}$. Therefore $P(115-10\sqrt{10}<X<115+10\sqrt{10})\ge.90$. The real endpoints are approximately 83.3772 and 146.6228; the integer event is $84\le X\le146$.

**Answer.** (a) At least **60.9375%** using integer support; (b) **84–146 calls** is a sufficient integer range. The slide's rounded range 83–147 is also sufficient but wider. These are bounds, not predicted exact fractions.

### L-08: Bernoulli variance practice

**Source:** slide 13, handwritten practice prompt. **PT:** PT-05. **Question paraphrase:** Show that a Bernoulli variable with success probability $p$ has variance $p(1-p)$.

**Worked solution.** $E(X)=0(1-p)+1p=p$ and $X^2=X$, so $E(X^2)=p$.

**Answer.** $V(X)=p-p^2=p(1-p)$, including zero variance at the deterministic endpoints.

### L-09: Four-question guessing quiz

**Source:** slide 15, repeated Bernoulli example. **PTs:** PT-07–08. **Question paraphrase:** Independently guess on four MCQs, each with four options and one correct answer. Find probabilities of (a) all correct, (b) all incorrect, (c) exactly two correct. Discuss whether the 16 binary correct/incorrect sequences are equally likely.

**Worked solution.** Define $C\sim\operatorname{Bin}(4,1/4)$. (a) $(1/4)^4=1/256=.00390625$. (b) $(3/4)^4=81/256=.31640625$. (c) $\binom42(1/4)^2(3/4)^2=54/256=.2109375$. One specified sequence with two correct answers has probability $9/256$; six arrangements contribute.

**Answer.** The probabilities above. Binary sequences are not equally likely; independent option selections give 256 equally likely option sequences instead.

### L-10: Warranty replacements and R tails

**Source:** slides 20–21, Example 3 (MMSA #71, included here solely because it is a lecture source question). **PTs:** PT-08–09. **Question paraphrase:** Of all phones, 20% are submitted for warranty service; of these, 60% can be repaired and 40% must be replaced. A company buys ten phones. Assuming independent outcomes, find (a) probability exactly two are replaced and the expected number replaced, (b) probability at most two, and (c) probability at least three. Express the probabilities in R.

**Worked solution.** A counted success is a replacement under warranty, with $p=.2(.4)=.08$, so $X\sim\operatorname{Bin}(10,.08)$.

$$
P(X=2)=\binom{10}{2}(.08)^2(.92)^8\approx.1478070355,\qquad E(X)=.8.
$$

$P(X\le2)=\sum_{x=0}^2\binom{10}{x}(.08)^x(.92)^{10-x}\approx.95992458$ and $P(X\ge3)=1-P(X\le2)\approx.04007542$.

**Answer and R check.** Use `dbinom(2,10,.08)`, `pbinom(2,10,.08)`, and `pbinom(2,10,.08,lower.tail=FALSE)`. The two tail probabilities add to 1; 0.8 is an expected count, not a replacement probability for an individual phone.

## C. Requested textbook exercises

Exactly **13 MMSA exercises** and **7 PAR exercises** are included. #112 is limited to **(a)–(c)** as confirmed by the user. Textbook examples illustrate concepts in the notes; unrequested end-of-section exercises are not added. MMSA #45's dependence on #13 is supplied as a data table, not counted as another requested exercise.

### MMSA #32 — Bernoulli powers

**Locator:** §3.3, p.135 (PDF p.147). **Difficulty:** Test Level. **PT:** PT-05.

**Question paraphrase:** For a Bernoulli variable with parameter $p$, (a) compute $E(X^2)$, (b) show $V(X)=p(1-p)$, (c) compute $E(X^{79})$.

**Worked solution.** Its support is $\{0,1\}$, so $X^m=X$ for every positive integer $m$. Hence (a) $E(X^2)=p$; (b) $V(X)=p-p^2$; (c) $E(X^{79})=p$.

**Answer and check.** **$p$, $p(1-p)$, $p$**, respectively. Endpoint parameters give deterministic variables and zero variance.

### MMSA #45 — Chebyshev bounds and sharpness

**Locator:** §3.3, p.137 (PDF p.149); dependent #13 data p.124 (PDF p.136). **Difficulty:** Basic Practice. **PT:** PT-03.

**Question paraphrase:** Chebyshev bounds $P(|X-\mu|\ge k\sigma)$ by $1/k^2$. (a) Give upper bounds for $k=2,3,4,5,10$. (b) For the telephone-lines distribution in #13, calculate mean/SD, then the exact deviation probabilities for those $k$ values and compare them with the bounds. (c) For $X=-1,0,1$ with probabilities $1/18,8/9,1/18$, calculate $P(|X-\mu|\ge3\sigma)$ and compare with the bound. (d) Give a distribution attaining $P(|X-\mu|\ge5\sigma)=.04$.

| #13 data: lines in use $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $p_X(x)$ | .10 | .15 | .20 | .25 | .20 | .06 | .04 |

**Worked solution.** (a) Upper bounds are $.25,1/9,.0625,.04,.01$.

(b) $E(X)=.15+.40+.75+.80+.30+.24=2.64$. $E(X^2)=.15+.80+2.25+3.20+1.50+1.44=9.34$. Thus $V(X)=9.34-2.64^2=2.3704$ and $\sigma\approx1.539610$.

| $k$ | $k\sigma$ | Tail support satisfying $\lvert x-2.64\rvert\ge k\sigma$ | Exact probability | Bound |
| --- | --- | --- | --- | --- |
| 2 | 3.079221 | $\{6\}$ | .04 | .25 |
| 3 | 4.618831 | Empty | 0 | $1/9$ |
| 4 | 6.158441 | Empty | 0 | .0625 |
| 5 | 7.698052 | Empty | 0 | .04 |
| 10 | 15.396103 | Empty | 0 | .01 |

The bound can be much larger than the actual probability. The maximum support deviation is $6-2.64=3.36$, which checks all empty-tail cases.

(c) Symmetry gives $\mu=0$, and $E(X^2)=2/18=1/9$, so $\sigma=1/3$. The event $|X|\ge1$ consists of $-1$ and 1 and has probability $1/9$, attaining the bound.

(d) Put mass .02 at each of $-1$ and 1 and .96 at 0. Then $\mu=0$, $\sigma^2=.04$, $\sigma=.2$, and $5\sigma=1$. The two endpoints give probability .04.

**Answer and check.** Chebyshev is often conservative, but can be sharp. The constructed distributions are normalized and place tail mass exactly at the inclusive boundary.

### MMSA #62 — Diagnose binomial variables

**Locator:** §3.5, pp.151–152 (PDF pp.163–164). **Difficulty:** Basic Practice. **PT:** PT-07.

**Question paraphrase:** Determine whether each variable is binomial; if so identify $n,p$ where possible: (a) number of 4s in ten fair-die rolls; (b) correct answers on a 40-question test when independently guessing among four options per question; (c) same as (b) with half the questions having four options and half three; (d) women in a random sample of eight from a class of 20 women and 15 men; (e) total weight of fifteen randomly selected apples; (f) number of those fifteen apples weighing more than 150 g.

**Worked solution and answer.**

| Part | Diagnosis and reason |
| --- | --- |
| (a) | Assuming independent rolls, $\operatorname{Bin}(10,1/6)$: “4” versus “not 4” is binary. |
| (b) | $\operatorname{Bin}(40,1/4)$ under independent guesses. |
| (c) | Not one binomial: success probabilities differ. Under independence, sum $\operatorname{Bin}(20,1/4)+\operatorname{Bin}(20,1/3)$. |
| (d) | Not binomial for ordinary sampling without replacement; $\operatorname{Hypergeo}(N=35,K=20,n=8)$. The sample fraction exceeds 5%. |
| (e) | Not binomial: it sums weights, not binary successes. |
| (f) | Plausible $\operatorname{Bin}(15,\pi)$ under independent, identically distributed apple selections, with $\pi=P(\text{weight}>150\text{ g})$ unspecified. A finite sample without replacement has a hypergeometric count instead. |

The same numerical threshold can turn a continuous measurement into a binary event, but this alone does not establish independence.

### MMSA #64 — Binomial PMFs and CDFs

**Locator:** §3.5, p.152 (PDF p.164). **Difficulty:** Basic Practice. **PT:** PT-08.

**Question paraphrase:** Use the binomial table or software to find (a) $B(4;10,.3)$, (b) $b(4;10,.3)$, (c) $b(6;10,.7)$, (d) $P(2\le X\le4)$ for $\operatorname{Bin}(10,.3)$, (e) $P(X\ge2)$ for that model, (f) $P(X\le1)$ for $\operatorname{Bin}(10,.7)$, (g) $P(2<X<6)$ for $\operatorname{Bin}(10,.3)$.

**Worked solution and answer.** Each CDF is a sum of its binomial PMF; the transformations below show the included integer values.

| Part | Exact model expression | Numerical answer |
| --- | --- | --- |
| (a) | $\sum_{x=0}^4\binom{10}x(.3)^x(.7)^{10-x}$ | .8497316674 |
| (b) | $\binom{10}4(.3)^4(.7)^6$ | .2001209490 |
| (c) | $\binom{10}6(.7)^6(.3)^4$ | .2001209490 |
| (d) | $B(4;10,.3)-B(1;10,.3)$ | .7004233215 |
| (e) | $1-B(1;10,.3)$ | .8506916541 |
| (f) | $B(1;10,.7)$ | .0001436859 |
| (g) | $B(5;10,.3)-B(2;10,.3)$ | .5698682262 |

**Check.** Parts (b) and (c) agree by success/failure reflection. The strict interval in (g) includes only 3, 4, 5.

### MMSA #66 — Crystal goblets and stopping

**Locator:** §3.5, p.152 (PDF p.164). **Difficulty:** Basic Practice. **PTs:** PT-08, PT-13.

**Question paraphrase:** Ten percent of goblets have cosmetic flaws and are sold as “seconds.” (a) In six random selections, find the probability exactly one is a second. (b) Find the probability at least two are seconds. (c) Examining goblets one at a time, find the probability that at most five are examined to find four that are not seconds. Use the independent-selection model.

**Worked solution.** For (a)–(b), $X\sim\operatorname{Bin}(6,.1)$. Thus (a) $\binom61(.1)(.9)^5=.354294$; (b) $1-(.9)^6-6(.1)(.9)^5=.114265$.

For (c), success means **not** a second, with probability .9. Let $T_4$ count examinations through the fourth success. Finish within five if the first five contain at least four successes:

$$
P(T_4\le5)=\binom54(.9)^4(.1)+(.9)^5=.91854.
$$

Independently, stop on 4 or 5: $.9^4+\binom43(.9)^4(.1)=.91854$.

**Answer.** (a) **.354294**; (b) **.114265**; (c) **.91854**. Fixed count and stopping-time descriptions agree.

### MMSA #67 — Drivers stopping

**Locator:** §3.5, p.152 (PDF p.164). **Difficulty:** Basic Practice. **PT:** PT-08.

**Question paraphrase:** With no other cars visible at a flashing-red intersection, 25% of drivers completely stop. Among twenty random drivers, find probabilities of (a) at most six, (b) exactly six, and (c) at least six stopping. Model driver decisions as independent with common $p=.25$.

**Worked solution.** Let $X\sim\operatorname{Bin}(20,.25)$.

$$
\text{(a) }\sum_{x=0}^6\binom{20}x(.25)^x(.75)^{20-x}\approx.7857819476,
$$

$$
\text{(b) }\binom{20}6(.25)^6(.75)^{14}\approx.1686092932,
\qquad
\text{(c) }1-\sum_{x=0}^5\binom{20}x(.25)^x(.75)^{20-x}\approx.3828273456.
$$

**Answer and check.** The probabilities above; (a)+(c)−(b)=1 because “six” belongs to both inclusive events.

### MMSA #68 — Driver moments and a two-SD tail

**Locator:** §3.5, p.152 (PDF p.164), continuing #67. **Difficulty:** Test Level. **PT:** PT-09.

**Question paraphrase:** In #67's setting, find (a) expected number of complete stops, (b) its SD, (c) probability that the count differs from its mean by **more than** two SDs.

**Worked solution.** $\mu=20(.25)=5$, $\sigma=\sqrt{20(.25)(.75)}=\sqrt{3.75}\approx1.936492$. The event is $|X-5|>3.872983$, so the integer tails are $X\le1$ or $X\ge9$:

$$
P(|X-5|>2\sigma)=B(1;20,.25)+1-B(8;20,.25)\approx.0652377926.
$$

**Answer.** (a) **5 drivers**; (b) **1.936492 drivers**; (c) **.0652377926**. This is an exact binomial-model probability, smaller than Chebyshev's .25 bound.

### MMSA #70 — Racket preferences and inventory

**Locator:** §3.5, pp.152–153 (PDF pp.164–165). **Difficulty:** Medium Practice. **PTs:** PT-08–10.

**Question paraphrase:** A racket is available midsize or oversize; 60% of customers want oversize. For ten independent customers: (a) probability at least six want oversize; (b) probability the oversize count is within one SD of its mean; (c) with seven rackets of each size in stock, probability all ten get their preferred size.

**Worked solution.** $X\sim\operatorname{Bin}(10,.6)$, $\mu=6$, $\sigma=\sqrt{2.4}\approx1.549193$.

(a) $P(X\ge6)=1-B(5;10,.6)=.6331032576$.

(b) $|X-6|\le1.549193$ gives $X\in\{5,6,7\}$, so $B(7;10,.6)-B(4;10,.6)=.6664716288$. Strict versus inclusive “within” does not change this integer set.

(c) Oversize demand requires $X\le7$, midsize demand requires $10-X\le7$. Thus $3\le X\le7$, with probability $B(7;10,.6)-B(2;10,.6)=.8204156928$.

**Answer.** (a) **.6331032576**; (b) **.6664716288**; (c) **.8204156928**, accounting for both inventories.

### MMSA #78 — Toll revenue

**Locator:** §3.5, p.154 (PDF p.166). **Difficulty:** Medium Practice. **PTs:** PT-01, PT-09.

**Question paraphrase:** Passenger cars pay a 1-dollar bridge toll; other vehicles pay 2.50 dollars. During daytime, 60% of vehicles are passenger cars. If 25 vehicles cross during a particular daytime period, find expected revenue, expressing total revenue as a function of the passenger-car count.

**Worked solution.** Let $X$ count passenger cars, so $E(X)=25(.6)=15$. Under independent identical vehicle selections, $X\sim\operatorname{Bin}(25,.6)$; its mean alone also follows from indicators without independence. Revenue is

$$
R=X+2.5(25-X)=62.5-1.5X,\qquad E(R)=62.5-1.5(15)=40.
$$

**Answer and check.** **40 dollars**. Directly, each vehicle's expected toll is $.6(1)+.4(2.5)=1.6$, and $25(1.6)=40$.

### MMSA #79 — Choosing a paper topic

**Locator:** §3.5, pp.154–155 (PDF pp.166–167). **Difficulty:** Test Level. **PT:** PT-10.

**Question paraphrase:** Topic A requires ordering two books; topic B requires four. A good paper needs at least half the ordered books to arrive in time. Books arrive independently with probability .9. Which topic maximizes the good-paper probability? Repeat when arrival probability is .5.

**Worked solution.** A succeeds if $\operatorname{Bin}(2,p)\ge1$, with probability $1-(1-p)^2$. B succeeds if $\operatorname{Bin}(4,p)\ge2$, with probability $1-(1-p)^4-4p(1-p)^3$.

| Arrival probability | Topic A probability | Topic B probability | Higher probability |
| --- | --- | --- | --- |
| .9 | .99 | .9963 | B |
| .5 | .75 | .6875 | A |

**Answer.** Choose **B** for .9 and **A** for .5. Both plans require a proportion of books, but the integer thresholds and trial counts differ; ordering more books is not always optimal.

### MMSA #85 — Exact binomial tails versus Chebyshev

**Locator:** §3.5, p.156 (PDF p.168), referring to #45. **Difficulty:** Medium Practice. **PTs:** PT-03, PT-09.

**Question paraphrase:** Find $P(|X-\mu|\ge k\sigma)$ for $k=2,3$ when $X\sim\operatorname{Bin}(20,.5)$; compare with Chebyshev. Repeat for $X\sim\operatorname{Bin}(20,.75)$.

**Worked solution.** For $p=.5$, $\mu=10,\sigma=\sqrt5$. For $p=.75$, $\mu=15,\sigma=\sqrt{3.75}$. Determine support values before summing:

| $p$ | $k$ | Tail event | Exact expression | Probability | Chebyshev upper bound |
| --- | --- | --- | --- | --- | --- |
| .5 | 2 | $X\le5$ or $X\ge15$ | $B(5;20,.5)+1-B(14;20,.5)$ | .0413894653 | .25 |
| .5 | 3 | $X\le3$ or $X\ge17$ | $B(3;20,.5)+1-B(16;20,.5)$ | .0025768280 | $1/9$ |
| .75 | 2 | $X\le11$ or $X\ge19$ | $B(11;20,.75)+1-B(18;20,.75)$ | .0652377926 | .25 |
| .75 | 3 | $X\le9$ | $B(9;20,.75)$ | .0039421417 | $1/9$ |

**Answer and check.** Every exact tail is below its bound. In the final row the putative upper tail begins above 20 and is impossible; do not invent a symmetric upper tail for the skewed model.

### MMSA #108 — Two-slot radios

**Locator:** §3.7, p.171 (PDF p.183). **Difficulty:** Basic Practice. **PT:** PT-14.

**Question paraphrase:** An electronics store receives twenty radios: twelve have two device slots and eight have one. Six radios are randomly selected to store under the display shelf; the remaining radios go to a storeroom. Let $X$ count two-slot radios among the six. (a) Identify the distribution and all parameters. (b) Find $P(X=2),P(X\le2),P(X\ge2)$. (c) Find mean and SD.

**Worked solution.** (a) The sample is without replacement: $\operatorname{Hypergeo}(N=20,K=12,n=6)$, support $0,\ldots,6$ and

$$
h(x)=\frac{\binom{12}x\binom8{6-x}}{\binom{20}6}.
$$

(b) $h(2)=\binom{12}2\binom84/\binom{20}6\approx.1191950464$; $\sum_{x=0}^2h(x)\approx.1372549020$; $1-h(0)-h(1)\approx.9819401445$.

(c) $E(X)=6(12/20)=3.6$; $V(X)=6(.6)(.4)(14/19)=1.061052632$; $SD(X)\approx1.030074$.

**Answer and check.** The model and quantities above. The two inclusive tails sum to $1+h(2)$, and the variance is smaller than the corresponding binomial variance 1.44.

### MMSA #112(a)–(c) — First adverse drug reaction

**Locator:** §3.7, pp.171–172 (PDF pp.183–184). **Difficulty:** Medium Practice. **PT:** PT-12.

**Question paraphrase:** Twenty percent of individuals react adversely to a drug. Administer the drug one individual at a time until the first adverse reaction. Define a suitable variable and find (a) probability that four individuals have had no adverse reaction when the experiment ends; (b) probability exactly five individuals receive the drug; (c) probability at most four individuals have had no adverse reaction when it ends. Model reactions as independent with common probability .2.

**Worked solution.** Define $F$ as the number of nonreacting individuals before the first reaction. $P(F=f)=(.8)^f(.2)$ on $f=0,1,\ldots$, and total administered is $T=F+1$.

(a) $P(F=4)=(.8)^4(.2)=.08192$.

(b) $P(T=5)=P(F=4)=.08192$.

(c) $P(F\le4)=\sum_{f=0}^4(.8)^f(.2)=1-(.8)^5=.67232$.

**Answer and check.** **.08192, .08192, .67232**. Parts (a) and (b) are the same event. Parts (d)–(e) are outside the confirmed requested range.

### PAR #3.14 — Cora's pop quiz

**Locator:** §3.4 exercises, p.119 (PDF p.138). **Difficulty:** Basic Practice. **PT:** PT-08.

**Question paraphrase:** Cora guesses on fifteen questions with four answers each, one correct answer, and no dependence between answers. Define a variable and give expressions and R calculations for (a) exactly four correct, (b) at most eight correct, (c) between three and ten correct, inclusive.

**Worked solution.** $X\sim\operatorname{Bin}(15,.25)$.

| Part | Exact expression | R calculation | Probability |
| --- | --- | --- | --- |
| (a) | $\binom{15}4(.25)^4(.75)^{11}$ | `dbinom(4,15,.25)` | .2251990652 |
| (b) | $\sum_{x=0}^8\binom{15}x(.25)^x(.75)^{15-x}$ | `pbinom(8,15,.25)` | .9958069855 |
| (c) | $\sum_{x=3}^{10}\binom{15}x(.25)^x(.75)^{15-x}$ | `pbinom(10,15,.25)-pbinom(2,15,.25)` | .7637968529 |

**Answer and check.** The table gives all three answers; “between” is inclusive and the lower cumulative subtraction ends at 2.

### PAR #3.15 — Virus infections

**Locator:** §3.4 exercises, p.119 (PDF p.138). **Difficulty:** Basic Practice. **PT:** PT-08.

**Question paraphrase:** Each of 1000 people independently has infection probability .01. Define a variable, expressions, and R calculations for (a) exactly ten infected, (b) at least sixteen infected, (c) twelve to fourteen infected inclusive, (d) at least one infected.

**Worked solution.** $X\sim\operatorname{Bin}(1000,.01)$. Use the exact binomial model, without importing a Poisson approximation.

| Part | Exact expression | R calculation | Probability |
| --- | --- | --- | --- |
| (a) | $\binom{1000}{10}(.01)^{10}(.99)^{990}$ | `dbinom(10,1000,.01)` | .1257402111 |
| (b) | $1-\sum_{x=0}^{15}\binom{1000}x(.01)^x(.99)^{1000-x}$ | `pbinom(15,1000,.01,lower.tail=FALSE)` | .0478705858 |
| (c) | $\sum_{x=12}^{14}\binom{1000}x(.01)^x(.99)^{1000-x}$ | `pbinom(14,1000,.01)-pbinom(11,1000,.01)` | .2202375943 |
| (d) | $1-(.99)^{1000}$ | `pbinom(0,1000,.01,lower.tail=FALSE)` | .9999568288 |

**Answer and check.** All four model probabilities are above; the complement in (d) is the event that all 1000 avoid infection.

### PAR #3.16 — Newton–Pepys dice problem

**Locator:** §3.4 exercises, p.119 (PDF p.138). **Difficulty:** Medium Practice. **PTs:** PT-08, PT-10.

**Question paraphrase:** Which event has the largest probability: (1) at least one 6 among six fair dice, (2) at least two 6s among twelve fair dice, or (3) at least three 6s among eighteen fair dice? Assume independent dice.

**Worked solution.** Counts $X_n\sim\operatorname{Bin}(n,1/6)$ give

$$
P(X_6\ge1)=1-(5/6)^6\approx.6651020233,
$$

$$
P(X_{12}\ge2)=1-\sum_{x=0}^1\binom{12}x(1/6)^x(5/6)^{12-x}\approx.6186673737,
$$

$$
P(X_{18}\ge3)=1-\sum_{x=0}^2\binom{18}x(1/6)^x(5/6)^{18-x}\approx.5973456859.
$$

**Answer.** Event **(1)** is most likely. R: `pbinom(0,6,1/6,lower.tail=FALSE)`, `pbinom(1,12,1/6,lower.tail=FALSE)`, `pbinom(2,18,1/6,lower.tail=FALSE)`. Equal relationships between thresholds and means do not imply equal probabilities.

### PAR #3.17 — Model selection

**Locator:** §3.4 exercises, p.120 (PDF p.139). **Difficulty:** Medium Practice. **PT:** PT-07.

**Question paraphrase:** Identify whether $X$ is binomial, and give $n,p$ if so: (a) George chooses pizza at lunch with probability .25 each day; $X$ counts pizza choices last week. (b) Brandi makes a free throw with probability .60; $X$ counts successful free throws in a game. (c) Ten candies are sampled from a bowl of 100 red and 150 blue; $X$ counts reds. (d) In a 600-page book, even pages have typo probability .01 and odd pages .02; $X$ counts typos. (e) Each page's typo count in a 600-page book is Bernoulli$(.01)$; $X$ counts all typos.

**Worked solution and answer.**

| Part | Model diagnosis |
| --- | --- |
| (a) | $\operatorname{Bin}(7,.25)$ if “every day last week” means seven days and lunch choices are independent. If only five lunch days are intended, use $n=5$. Independence is a necessary additional modelling assumption; daily marginal probabilities alone do not establish it. |
| (b) | No fixed trial count is given. Conditional on a fixed number $m$ of attempts and independent shots, it is $\operatorname{Bin}(m,.6)$. Unconditionally, a random number of attempts does not specify one binomial model. |
| (c) | Ordinary sampling is without replacement: exact $\operatorname{Hypergeo}(N=250,K=100,n=10)$. A binomial$(10,.4)$ approximation is plausible because $10/250=.04$, but it is not the exact distribution. |
| (d) | Different page probabilities violate the common-$p$ condition. Under independent at-most-one-typo page indicators, it is a sum of $\operatorname{Bin}(300,.01)$ and $\operatorname{Bin}(300,.02)$, not one binomial. If multiple typos per page are allowed, an indicator only counts pages with typos, not total individual typos. |
| (e) | $\operatorname{Bin}(600,.01)$ under independent page indicators; the stated Bernoulli marginal distributions alone are insufficient to prove independence. |

**Check.** The conditional and approximation qualifications identify assumptions needed by the textbook's informal narratives rather than silently asserting them.

### PAR #3.19 — Colored balls with and without replacement

**Locator:** §3.4 exercises, p.120 (PDF p.139). **Difficulty:** Test Level. **PTs:** PT-08, PT-14.

**Question paraphrase:** A bag has sixteen balls: one red, three yellow, five green, seven blue. Draw four with replacement. (a) Probability at least two are green; (b) probability all four have different colors. (c) Repeat both calculations without replacement.

**Worked solution.** With replacement, green count $G\sim\operatorname{Bin}(4,5/16)$.

$$
\text{(a) }P(G\ge2)=1-(11/16)^4-4(5/16)(11/16)^3
=\frac{24275}{65536}\approx.3704071045.
$$

(b) Four distinct colors require exactly one of each; $4!$ orders have the same probability:

$$
4!\frac1{16}\frac3{16}\frac5{16}\frac7{16}
=\frac{2520}{65536}\approx.0384521484.
$$

(c) Without replacement, $G\sim\operatorname{Hypergeo}(16,5,4)$:

$$
P(G\ge2)=\frac{\binom52\binom{11}2+\binom53\binom{11}1+\binom54\binom{11}0}{\binom{16}4}
=\frac{665}{1820}=\frac{19}{52}\approx.3653846154.
$$

For one of each color, unordered favorable samples number $1(3)(5)(7)=105$, so $105/\binom{16}4=3/52\approx.0576923077$.

**Answer and check.** The four probabilities above. Unordered sampling already counts each subset once; multiplying the last answer by $4!$ would overcount.

### PAR #3.22 — Randomly selected die

**Locator:** §3.4 exercises, p.121 (PDF p.140). **Difficulty:** Test Level. **PT:** PT-11.

**Question paraphrase:** One die is standard; another has three faces labelled 1 and three labelled 4. Flip a fair coin: heads selects the standard die for all five rolls, tails selects the second die for all five rolls. Let $X$ count 4s. Find $P(X=3)$ and determine whether $X$ is binomial.

**Worked solution.** $X\mid H\sim\operatorname{Bin}(5,1/6)$ and $X\mid T\sim\operatorname{Bin}(5,1/2)$. Therefore

$$
P(X=3)=\frac12\binom53(1/6)^3(5/6)^2
+\frac12\binom53(1/2)^5
=\frac{1675}{9720}\approx.1723251029.
$$

The marginal probability of a 4 is $\overline p=(1/6+1/2)/2=1/3$, so $E(X)=5/3$. The common-die success probability has variance $1/36$, giving $V(X)=5(1/3)(2/3)+5(4)(1/36)=5/3$. A $\operatorname{Bin}(5,1/3)$ would have variance $10/9$ instead. Since all counts 0 through 5 have positive probability, a putative binomial model would have to use $n=5$ and $p=1/3$.

**Answer.** **$1675/9720\approx.1723251029$**, and **not binomial**. Rolls are independent conditional on the die, but share dependence through the one die selected before all rolls.

### PAR #4.23 — Birth months with at least two students

**Locator:** Ch.4 exercise, p.179 (PDF p.198); supporting indicator method from C-04. **Difficulty:** Test Level. **PT:** PT-06.

**Question paraphrase:** In a class of 25 students, find the expected number of months in which at least two students are born. Assume birth months are equally likely. Hint: use indicators.

**Worked solution.** Use the conventional model that different students' birth months are independent, each uniform over the 12 months. For month $j$, let $N_j$ count students born in that month and let $I_j=1$ if $N_j\ge2$, otherwise 0. Then $N_j\sim\operatorname{Bin}(25,1/12)$, and the requested count is $M=\sum_{j=1}^{12}I_j$.

For a fixed month, exclude the cases of zero and exactly one birth:

$$
P(I_j=1)=1-P(N_j=0)-P(N_j=1)
=1-\left(\frac{11}{12}\right)^{25}
-25\left(\frac1{12}\right)\left(\frac{11}{12}\right)^{24}.
$$

By linearity of expectation,

$$
E(M)=12\left[1-\left(\frac{11}{12}\right)^{25}
-\frac{25}{12}\left(\frac{11}{12}\right)^{24}\right]
\approx7.539567.
$$

**Answer and check.** Approximately **7.539567 months**. R verifies the result with `12*pbinom(1,25,1/12,lower.tail=FALSE)`. The answer lies between 0 and 12. Each qualifying month is counted once, even if three or more students were born in it; this is not a count of student pairs. The month indicators are dependent, but linearity does not require their independence. The source explicitly assumes equal birth-month probabilities; independence across students is the additional conventional assumption used for the binomial count in each month.

## D. Original self-test questions

Complete all questions before consulting E. These are original transfer questions, not additional assigned textbook exercises.

### ST-01: A nonlinear shortcut — PT-01

$X$ is equally likely to be $-1$ or 1. A student writes $E(X^2)=E(X)^2$ and $V(X^2)=V(X)$. Diagnose both claims by computing the four quantities. Which transformation rule was misused?

### ST-02: Choosing a bound — PT-02

A nonnegative loss $L$ has mean 18 dollars. Bound $P(L\ge60)$ and construct a two-point distribution attaining the bound. Would the mean suffice if $L$ could be negative?

### ST-03: A vacuous central bound — PT-03

A variable has mean 0 and SD 1, without an assumed distribution. A student asserts that at least 68% lie in $(-1,1)$ and at least 75% lie in $[-2,2]$. Which is justified? Give a distribution disproving the first assertion.

### ST-04: Coverage and units — PT-04

A filling machine has mean volume 500 mL and variance 9 mL squared. Construct a centered interval guaranteed to contain at least 99% of fill volumes. Explain the error in using radius $10\times9$ mL.

### ST-05: A complemented indicator — PT-05

$P(A)=.35$ and $J=1-I_A$. Find its distribution, $E(J^{10})$, and $V(J)$. Explain why $E(J^{10})$ is not generally $E(J)^{10}$.

### ST-06: Dependent indicators — PT-06

Four passengers independently choose one of three floors uniformly. Let $S$ be the number of floors where an elevator stops. Use indicators to find $E(S)$ without a full PMF. Explain why stop indicators are dependent and why the expectation calculation remains valid.

### ST-07: Same marginals, different count — PT-07

One fair coin controls ten lights: heads turns all on, tails all off. Each light's marginal on-probability is .5. Diagnose a proposed binomial$(10,.5)$ model for the number on. Give the true distribution, mean, and variance.

### ST-08: A tail indexing mistake — PT-08

For $X\sim\operatorname{Bin}(9,.2)$, a student calculates $P(X\ge3)$ as `1-pbinom(3,9,.2)`. Correct it, calculate the probability, and identify the exact omitted probability mass.

### ST-09: One-SD support — PT-09

$X\sim\operatorname{Bin}(9,1/3)$. Find its mean, variance, and integer outcomes within one SD, inclusive. Give the event probability as a sum and a numerical value.

### ST-10: Unequal inventories — PT-10

Five independent customers choose A with probability .5 and B otherwise. A shop has two A and four B items. Find the probability every request is fulfilled. Why do symmetric preference probabilities not imply symmetric demand constraints?

### ST-11: Common versus refreshed environment — PT-11

A bag is chosen with probability $1/2$: bag A gives red with probability .2, bag B with probability .8. Draw twice with replacement. Compare choosing one bag for both draws with choosing a bag independently anew for each draw. Find the probability both draws are red and diagnose a binomial count for each protocol.

### ST-12: Waiting and collecting — PT-12

Independent draws give one of three equally likely sticker types, with replacement. (a) Find expected draws to collect all three by geometric stages. (b) Find expected distinct types after four draws using indicators. (c) After three failed attempts to get a particular type, what is the chance the next two also fail? Why is total collection time not a single constant-$p$ geometric variable?

### ST-13: Negative binomial convention — PT-13

Independent trials succeed with probability .5. Let $T$ count trials through the second success. Find $P(T=4)$ and $P(T\le4)$ by stopping-time and binomial-horizon calculations; give mean, variance, and equivalent R failure-count arguments.

### ST-14: Finite-population boundaries — PT-14

Eight items include three successes. Sample six without replacement. Find support, PMF, mean, and variance; explain why zero successes is impossible and binomial$(6,3/8)$ is unsuitable as an exact model. What happens if all eight are selected?

## E. Self-test answers

### ST-01 answer — PT-01

$E(X)=0$, $E(X^2)=1$, $V(X)=1$, but $X^2$ is the constant 1, so $V(X^2)=0$. Both claims fail. The formula $V(aX+b)=a^2V(X)$ applies to affine, not quadratic, transformations.

### ST-02 answer — PT-02

Markov gives $P(L\ge60)\le18/60=.3$. Mass .3 at 60 and .7 at 0 attains it. For signed loss, mass .9 at 60 and .1 at $-360$ has the same mean 18 but tail probability .9; nonnegativity matters.

### ST-03 answer — PT-03

Chebyshev guarantees at least 75% in $(-2,2)$ and therefore also $[-2,2]$. Its radius-1 lower bound is zero. Mass $1/2$ at each of $-1,1$ gives mean 0 and SD 1 but no mass in $(-1,1)$, disproving the 68% assertion.

### ST-04 answer — PT-04

$\sigma=\sqrt9=3$ mL. Solve $1-1/k^2=.99$ to get $k=10$ and radius 30 mL. The interval $(470,530)$, or the inclusive version, guarantees at least 99%. The proposed calculation treats variance (mL squared) as SD (mL).

### ST-05 answer — PT-05

$J\sim\operatorname{Bern}(.65)$ because $J=1$ on $A^c$. Since $J^{10}=J$, its expectation is .65, not $.65^{10}$. Its variance is $.65(.35)=.2275$, equal to the original indicator's variance by affine reflection.

### ST-06 answer — PT-06

For floor $j$, $I_j$ indicates at least one passenger chooses it. Then $P(I_j=1)=1-(2/3)^4=65/81$, so $E(S)=3(65/81)=65/27\approx2.407407$. For two floors, $P(I_1=I_2=0)=(1/3)^4$ differs from $(2/3)^8=P(I_1=0)P(I_2=0)$. Indicators are dependent, but linearity still applies.

### ST-07 answer — PT-07

The lights are perfectly dependent. $P(X=0)=P(X=10)=1/2$, giving mean 5 and variance $50-25=25$. A binomial$(10,.5)$ would have variance 2.5 and positive masses at all intermediate counts. Equal marginal probabilities do not establish independence.

### ST-08 answer — PT-08

Use `pbinom(2,9,.2,lower.tail=FALSE)`:

$$
P(X\ge3)=1-\sum_{x=0}^2\binom9x(.2)^x(.8)^{9-x}=.261802496.
$$

The proposed code gives $P(X\ge4)$ and omits $P(X=3)=\binom93(.2)^3(.8)^6=.176160768$.

### ST-09 answer — PT-09

$\mu=3$, $\sigma^2=2$, and $[3-\sqrt2,3+\sqrt2]$ contains only integers $2,3,4$. Thus

$$
P(2\le X\le4)=\sum_{x=2}^4\binom9x(1/3)^x(2/3)^{9-x}=\frac{14016}{19683}\approx.712087.
$$

R: `pbinom(4,9,1/3)-pbinom(1,9,1/3)`. Determine integer support before rounding the mean or SD.

### ST-10 answer — PT-10

For $X\sim\operatorname{Bin}(5,.5)$ counting A choices, constraints are $X\le2$ and $5-X\le4$, hence $1\le X\le2$. Probability is $[\binom51+\binom52]/2^5=15/32=.46875$. Constraints depend on stock counts, not PMF symmetry.

### ST-11 answer — PT-11

For one common bag, $P(RR)=\tfrac12(.2)^2+\tfrac12(.8)^2=.34$, whereas each marginal is .5. The count masses are $.34,.32,.34$, a mixture rather than binomial$(2,.5)$. Selecting a new bag independently each time yields independent Bernoulli$(.5)$ trials, binomial$(2,.5)$ count, and $P(RR)=.25$.

### ST-12 answer — PT-12

(a) The first new type takes one draw; subsequent new-type probabilities are $2/3$ and $1/3$. Expected total time is $1+1/(2/3)+1/(1/3)=11/2=5.5$. (b) Each type has appeared by four draws with probability $1-(2/3)^4$, so expected distinct types are $3[1-(2/3)^4]=65/27$. (c) For a specific type, fixed $p=1/3$ and memorylessness give two further failures with probability $(2/3)^2=4/9$. Collection stages have changing probabilities, so their total is not one geometric wait.

### ST-13 answer — PT-13

$P(T=4)=\binom31(.5)^4=3/16$: one success among the first three, then a success. Summing stops on 2,3,4 gives $1/4+1/4+3/16=11/16$. Equivalently $P(\operatorname{Bin}(4,.5)\ge2)=1-(1+4)/16=11/16$. Mean $2/.5=4$ and variance $2(.5)/(.5)^2=4$. Failures $F=T-2$ have mean 2 and variance 4. R: `dnbinom(2,2,.5)` for the exact stop and `pnbinom(2,2,.5)` for stopping by 4; `pbinom(1,4,.5,lower.tail=FALSE)` verifies the latter.

### ST-14 answer — PT-14

At most five failures are available, so support is $1,2,3$. The PMF is $\binom3x\binom5{6-x}/\binom86$, giving masses $3/28,15/28,10/28$ that sum to 1. Mean $6(3/8)=9/4$, variance $6(3/8)(5/8)(2/7)=45/112\approx.401786$. Sampling 75% of the population makes dependence substantial; the binomial model even permits impossible counts. Sampling all eight makes $X=3$ certain, with variance 0.

## F. Coverage and unresolved items

### Coverage by source and learning outcome

| Source / objective | Role and reading status | Concepts / PTs | Practice |
| --- | --- | --- | --- |
| W5 slides 3–7: relate moments to outcomes | Primary lecture core; concise prerequisite application | C-01, PT-01 | L-01–04 |
| Slides 8–11: Chebyshev applicability and interval guarantees | Primary lecture core | C-02–03, PT-02–04 | L-05–07; MMSA #45,85 |
| Slides 13–17: Bernoulli/indicator versus binomial; model plausibility | Primary lecture core | C-04–05, PT-05–07 | L-08–09; MMSA #32,62; PAR #3.17,4.23 |
| Slides 18–21: parameters, probability calculations and R | Primary lecture core | C-05–06, PT-07–11 | L-10; MMSA #64,66–68,70,78–79; PAR #3.14–16,3.22 |
| Outcome “derive and justify other named distributions” | Listed in slide 2 and marked complete in printed slide 23; deck derives Bernoulli/binomial, with no geometric/negative-binomial/hypergeometric lecture derivations | C-07–09, PT-12–14 use screenshot-defined textbook supplements | MMSA #108,112; PAR #3.19(c) |
| MMSA §3.3, pp.126–137 | Relevant/supporting reading from screenshot: LOTUS, moments, transformations, Chebyshev exercise | C-01,03–04, PT-01,03–05 | #32,45; dependent #13 table only |
| MMSA §3.5, pp.144–156 | Relevant/supporting reading: binomial, 5% approximation rule, inference cutoffs, proportion SE and binomial MGF | C-05, PT-07–10 | #62,64,66,67,68,70,78,79,85 |
| MMSA §3.7, selected geometric/hypergeometric formulas and pp.171–172 exercises | Necessary additional supporting reading for explicitly requested exercises, not inferred assigned reading | C-07–09, PT-12–14 | #108,112(a)–(c) |
| PAR §§3.3–3.4, pp.99–107; selected exercises pp.119–121 | Relevant/supporting reading: Bernoulli sequences, binomial, conditional mixtures | C-04–06, PT-05,07–11,14 | #3.14–17,3.19,3.22 |
| PAR §5.1, pp.185–193 before §5.2 | Relevant/supporting reading: geometric, conventions, memorylessness, coupon/tiger models | C-04,07, PT-06,12 | ST-06,ST-12; no additional textbook exercises requested |
| PAR §5.3, pp.196–202 before §5.4 | Relevant/supporting reading: negative binomial, geometric sums, binomial horizon, contests | C-08, PT-13 | MMSA #66(c); ST-13 |
| PAR §5.4, pp.202–207 before §5.5 | Relevant/supporting reading: hypergeometric, support, finite-population correction, estimation | C-09, PT-14 | MMSA #108; PAR #3.19(c); ST-14 |
| PAR Ch.4 #23, p.179 | Explicit requested exercise: expected number of birth months containing at least two of 25 students; indicator method | C-04, PT-06 | #4.23 |

### Exact requested exercise inventory

| Source and difficulty | Requested exercise numbers | Count |
| --- | --- | --- |
| MMSA Basic | #45; #62,64,66,67,108 | 6 |
| MMSA Medium | #70,78,85,112(a)–(c) | 4 |
| MMSA Test Level | #32,68,79 | 3 |
| PAR Basic | Ch.3 #14,15 | 2 |
| PAR Medium | Ch.3 #16,17 | 2 |
| PAR Test Level | Ch.3 #19,22; Ch.4 #23 | 3 |

Totals: **9 concepts**, **14 PTs**, **14 original teaching examples with matching solutions**, **10 lecture question groups**, **20 requested textbook exercises** (13 MMSA, 7 PAR), and **14 original self-tests with answers**. Question groups combine shared example/slide subparts; counts are not individual-subpart counts.

### Verified discrepancies and corrections

| Item | Verified treatment |
| --- | --- |
| Screenshot's MMSA “p.151” group | #62 starts p.151; #64,66–68,70 are p.152; #70 continues p.153; #78 p.154; #79 continues p.155; #85 p.156. #108 and #112 belong to §3.7 on pp.171–172, not §3.5 or supplementary exercises. All specified numbers are retained. |
| Screenshot's PAR Ch.3 “p.119” group | #14–16 p.119; #17,19 p.120; #22 p.121. Ch.4 #23 is p.179. |
| Printed versus PDF pages | In these ranges, MMSA PDF page = printed page + 12; PAR PDF page = printed page + 19. Offsets checked against rendered headers. |
| Cropped #112 | User confirmed ending at (c); all requested (a)–(c) subparts are included. |
| Deck page count | 22 PDF pages, printed labels 1–21 and 23. The label skip is recorded without inventing content. |
| Slide 5 handwritten repair-cost SD | $E(X^4)=42.02$ implies $V(X^2)=15.1876$, not 6.7468. Thus $V(C)=60.7504$ and SD 7.794254, not approximately 5.19. Direct transformed-PMF calculation independently confirms the correction; mean 13.36 is correct. |
| Slides 3 and 6 nonlinear expectation warning | The correct reading is “not equal in general.” A universal strict $\ne$ is false; particular nonlinear cases can have equality. |
| Slide 4 independence annotations | Independence is sufficient, not necessary in general, for the displayed product-expectation equality and variance additivity. Sum expectation needs no independence. |
| Slides 8–9 proofs and zero variance | Use weak inequalities: sharp equality cases exist. Standardized Chebyshev needs positive SD; constants use the positive-distance form. |
| Slide 10 interval rounding | 83–147 is a valid wider range; 84–146 represents the displayed real interval on integer support and also guarantees at least 90%. |
| Requested exercise data | MMSA #78 uses 25 vehicles and gives expected revenue 40 dollars. PAR #4.23 counts birth months with at least two students, with expectation approximately 7.539567 months under independent uniform birth months. Both statements were checked against the cited textbook pages. |
| Informal independence assumptions | Necessary assumptions are explicit, particularly PAR #3.17 and independence of different students' birth months in #4.23; equal marginal probabilities alone do not establish independence. |

### Unresolved source item

**Slide 7 QR warm-up:** its QR resolves to a [Microsoft Forms warm-up](https://forms.cloud.microsoft/r/cDVzc0x0Er?origin=QRCode&qrcodeorigin=presentation), but question content could not be retrieved. No unseen question or answer has been invented. All questions visible in the supplied deck and every requested textbook exercise are included; there is no unresolved textbook subpart.

“Relevant Chapters” was not relabelled mandatory assigned reading. No additional platform/discussion-board scope was inferred.

### Verification record

PDF text was converted with local Docling and checked against rendered pages for mathematical notation, tables, handwriting, and exercise continuations. Probability sums, moments, integer tails, support, normalization, units, and boundary cases were checked. Key binomial/hypergeometric calculations were independently compared in R and SciPy; the nonlinear cost variance was checked using two different moment calculations.

Markdown checks cover headings, links and images, math delimiters, PT ownership/name agreement, one teaching example and solution per PT, the exact 20-exercise inventory, and unfinished placeholders. The MMSA #45 table uses `\lvert` and `\rvert` in its mathematical header so Markdown does not interpret absolute-value bars as column separators. Its five-column structure was checked with a standard Markdown table parser. Rendered-preview status is reported with the delivered files only after that check is actually performed.
