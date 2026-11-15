Create two English study files for STA237 Week 9, “Named Continuous Distributions & Transformations.” I will use them as my main resource for learning the material for the first time. Teach me how to get from the wording of a question to the model, event, and calculation, so that I can close the solution and redo the original problem myself.

Write both files entirely in English, including headings, explanations, tables, figure labels, captions, questions, and solutions. Original filenames may remain unchanged.

## 1. Sources and deliverables

Workspace: /Users/stevenli/Documents/University of toronto/STA237

Primary source: W9/Week9-L0401-annotated.pdf (20 PDF pages).

Exercise source: the local third edition of Modern Mathematical Statistics with Applications (MMSA).

Structure reference: /Users/stevenli/Documents/University of toronto/Study-Notes-Agent-Prompt-Generic.md

Create:

- W9/Study-Notes-Markdown/Study-Notes.md
- W9/Study-Notes-Markdown/Answers-and-Practice.md

Use the generic template’s concept-first structure. This prompt overrides its instructions to invent examples and self-tests. Preserve existing output; use a versioned sibling directory if necessary. Keep temporary files outside the deliverable.

## 2. Three scope rules

A. MMSA only this week. The instructor’s highlighted exercise-list heading says “MMSA only this week.” Although a PAR row is visible, do not assign, solve, or use those exercises as PT evidence. You may explain the rate-versus-scale notation comparison explicitly made in the lecture. MMSA §§4.3, 4.4, and 4.7 are relevant sections, not a direction to cover entire chapters. In particular, no additional §4.4 textbook exercises are listed; the Gamma practice comes from the slides.

B. Use the course’s CDF/distribution method for transformations. The instructor explicitly excludes the textbook’s Transformation Theorem. Start with the support and F_Y(y) = P(g(X) ≤ y), rewrite the event in terms of X, evaluate it, and differentiate the CDF where appropriate. Explain inequality reversals and two-sided events from first principles. Do not introduce the excluded theorem, a Jacobian shortcut, or a general multiple-inverse-branch density formula, even as an alternative solution. Differentiating a CDF already derived from an event is part of the permitted method.

C. Slides define Core. Material actually taught or explicitly requested in the Week 9 deck is Core. Mark substantive additions absent from the slides as **Supplementary** where they are taught or used, including inside solutions. Separate the Core idea from the extra technique when only one step is supplementary. Keep ordinary explanations, modelling rationale, and necessary algebra: a scope restriction is not a reason to skip the step a beginner needs. Reassess scope for this week: Gamma formulas and the CDF method for transformed variables are explicitly present in Week 9.

## 3. Exact exercise list

Use the instructor’s difficulty labels and subpart restrictions:

| Level | Normal distribution — Use R | Transformations — use the course CDF method |
| --- | --- | --- |
| Basic | Instructor p. 225: #39(h,i,j) only; #40, #41, #42 | Instructor p. 262: #116 |
| Medium | Instructor p. 226: #46, #48, #59 | Instructor p. 262: #113, #114 |
| Test Level | Instructor p. 226: #61; #67(a) only | Instructor p. 262: #118, #121 |

Total: **14 exercise numbers: 5 Basic, 5 Medium, 4 Test Level.** Include every subpart for unrestricted exercises. Do not include #39(a–g) or #67(b).

The instructor’s pages are starting locators. In the supplied edition, #41 continues onto printed p. 226; #59, #61, and #67(a) are on pp. 228, 229, and 230 respectively. #113 continues from p. 262 to p. 263; #114, #116, #118, and #121 are on p. 263. Verify each question in the PDF and give the actual printed page and one-based PDF page. Restore necessary definitions and shared instructions, including the book’s convention for z_α. Use faithful, self-contained English paraphrases.

For each “Use R” group, write the probability statement or quantile equation first, then the appropriate R command, numerical result where applicable, and interpretation. Use named `mean=` and `sd=` arguments; explain `lower.tail=FALSE` when used. For #67(a), the original task explicitly asks for a proof by integration: give that proof, including the substitution and symmetry argument. R can check an example but cannot replace the proof. Distinguish commands actually run from commands supplied for reproduction.

## 4. Establish problem types from real questions only

First inventory all explicit Week 9 slide tasks and the **five eligible Basic MMSA exercises: #39(h–j), #40, #41, #42, and #116**. Only these sources may establish a problem type (PT). Do not start by inventing a taxonomy from chapter headings.

For each PT, give one owning concept, one stable ID, an exact source locator and subpart, and one actual eligible question or subpart as the representative. Keep its original numbers, assumptions, and task. Explain the recognition cue, why the method fits, the reusable steps, a common mistake, and how to check the result. Group questions when they use the same reasoning; there is no target PT count. A concept can be taught without having its own PT.

Solve all Medium and Test Level questions. Map a task to an existing PT only if the fit is genuine. Otherwise write “No matching PT established by the slide/Basic source set” and explain it locally. PT eligibility and Core/Supplementary status are separate decisions. Do not invent teaching questions, change source numbers to create variants, or add original self-tests.

## 5. Week 9 teaching and accuracy checks

Use one-based PDF pages below. Printed slide numbering diverges from PDF page numbering in this deck. Preserve actual example names; do not invent an “Example 4” to fill a numbering gap.

Gamma and exponential models — PDF pp. 3–10:

- Start with one interarrival time versus the sum of several independent, common-rate exponential waits. Explain when the Gamma shape represents a number of waits and why the general Gamma shape need not be an integer.
- Define shape α, scale β, and rate λ = 1/β before using them. Connect the PDF, support, mean, and variance across the two parameterizations. For R, specify `shape=` and either `scale=` or `rate=` explicitly. Do not rely on an ambiguous positional argument.
- Cover the Gamma function, recurrence, integer factorial identity, stated half-value, exponential special case, and the expectation setup on p. 6. Show how the expectation integral uses the Gamma function. Do not turn a stated fact into an unrequested advanced proof.
- Technician example: convert 10 completed requests per eight-hour day to consistent hourly units. Define the two durations, state the Poisson-process/intercompletion assumptions under which their sum has the proposed model, and connect the upper-tail integral to the R calculation. A count average alone does not establish independent exponential durations.
- Video-length example: distinguish a Chebyshev guarantee of at least 80% from the Gamma model’s actual probability for that same interval. Account for the nonnegative support and explain “approximately” without inventing a platform-specific duration limit.
- Two-car exercise: include all three parts. The distance unit is 1,000 km; convert the 70,000 km threshold. Explain the distinction between a combined distance and either individual distance. State the independence and parameter convention used. If the bare `Exp(3)` notation leaves rate versus mean ambiguous, identify your interpretation and its source rather than silently choosing one.

Normal models and R — PDF pp. 11–15:

- Teach location, spread, symmetry, standardization, and the inverse operation. Distinguish variance σ² from standard deviation σ: state the convention whenever moving between the slides, MMSA, and R. Distinguish the standard normal CDF Φ(z) from the general normal CDF evaluated at x.
- Explain when the unknown is a probability (`pnorm`) and when it is a cutoff (`qnorm`). Use the water-dispenser example to connect an interval within one SD to the empirical rule, then explain why 0.5% overflow means an upper-tail probability of 0.005. Show how to recover a capacity in ounces.
- In the textbook questions, distinguish one-sided, central, and two-tailed events; handle independence and unit conversions where the original asks for them. For #61, translate each integer event before applying its required continuity correction. Mark that technique Supplementary if absent from the slides.
- Qualify broad slide wording when needed: an affine transformation of one normal variable is normal; arbitrary linear combinations of variables with normal marginals alone are not guaranteed normal. Keep the relevant condition brief.

Transformations — PDF pp. 16–19:

- Cover all five parts of the returning 30 cm ruler/cube question. Distinguish side length X from surface area A = 6X². Track units for the mean and variance. For the specified area interval, distinguish what Chebyshev can guarantee from the exact probability obtained by mapping the event back to side length. If the bound is uninformative, say so. Follow the typed interval and flag any conflicting handwritten endpoint.
- On pp. 17–18, explain why the displayed inverse-inequality step works for an increasing transformation. For Basic #116, Y = −log X is decreasing on its support: show the reversed inequality and resulting tail probability explicitly. For #121, translate |X| ≤ y into a two-sided event. Do not apply the increasing-case formula mechanically to either problem.
- On p. 19, connect the particular probability P(Y ≤ 100) to the general CDF for Y = X² when X is exponential with mean 2. Explain why only the nonnegative root matters here. Give the complete piecewise CDF and a valid PDF; distinguish a possible density singularity near zero from a point mass at zero.
- Respect each textbook transformation’s actual direction: #113 asks for the square root, whereas the slide example squares the variable. Include the requested density verification in #114 and address the “any other solution?” question in #118.

## 6. Make the files usable for independent study

Study-Notes.md: Begin with linked contents and a short notation guide. Teach each concept in learning order: what is observed, what is random, its support and units, why the model fits, and how the event determines the calculation. Put the evidenced PTs and their representative questions after the parent concept, with direct solution links. Use source-based figures where they clarify a tail, an interval, or a mapped event.

Answers-and-Practice.md: Include (A) PT representative solutions, (B) all slide questions and explicit mathematical tasks, (C) all 14 MMSA exercises, (D) a revision route linking only to existing questions, and (E) a compact coverage and unresolved-items appendix. Keep one canonical full solution per source question or subpart and link to it from other inventories. Each solution should contain enough reasoning to reproduce it without guessing a missing parameter, inequality, integration limit, or R argument.

Before delivery, visually check handwritten symbols, numerical thresholds, diagrams, and any formula lost during PDF extraction. Verify the required subparts, all PT evidence, local Supplementary labels, units, tail directions, rate/scale choices, numerical results, and full CDF branches. Check links, English-only output, and math rendering. Finally, read both files as a first-time learner and repair genuine comprehension gaps. Deliver links to the two files and state any unresolved source ambiguity or verification that could not be completed.
