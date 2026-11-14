## Question 1

The time it takes for an individual to complete a project can be modeled by the random variable T , which has the following probability density function:

<!-- formula-not-decoded -->

[公式或图像请见原页面]

- a) (6 pts) Compute the expected value and standard deviation of T . Briefly explain in 2-3 sentences how you would estimate the expected value from the graph the PDF below: e) (6 pta) Cempute tbe cwnoctod

[公式或图像请见原页面]

<!-- formula-not-decoded -->

## MW Make-Up Midterm

Grading Scheme b) (3 pts) Derive the complete cumulative distribution function of T .

<!-- formula-not-decoded -->

- c) (3 pts) What is the median completion time for this project? Interpret the value within the given context. ー

[公式或图像请见原页面]

## Question 2

[公式或图像请见原页面]

There are two groups of people waiting to get into a concert. Group A consist of 3 people: ( Aa ron, Ab ner, Ac e) while group B consist of 5 people ( Ba la, Be tty, Bi ck, Bo han, Bu lma). Numbers are randomly assigned to each person waiting which determines their entry order. Number 1 will be enter first, number 2 second and so on.

- a) (4 pts) What is the probability that every person in group A were given consecutive numbers?

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- b) (2 pts) Let C represent the event everyone in group A enters the concert before anyone in group B can enter. Find P ( C ) . \_

<!-- formula-not-decoded -->

- c) (2 pts) Similarly, let D represent the event that everyone in group B enters the concert before anyone in group A can enter. Without any calculations, determine whether P ( C ) + P ( D ) = 1 . Justify in 1-2 sentences. ー

<!-- formula-not-decoded -->

## Question 3

To train your Large Language Model (LLM) you need to compile data-points. You send your data to a remote computer and the data is randomly assigned to one of two servers with equal probability.

- Server 1 will process all the data-points in the dataset one by one until it finds a bug, after which the server stops. The bugged data-point is not processed. There is a probability p 1 = 0 . 05 that a data-point is bugged.
- Server 2 will process the all the data-points in the dataset one by one until it finds 3 bugs, after which the server stops. The 3 bugged data-points are not processed. There is a probability p 2 = 0 . 1 that a data-point is bugged.

Let A be the event that the data is sent to server 1, and S be the number of data-points that are processed before the server stops.

Use appropriate event, probability, and/or random variable notation in all parts of this question.

- a) (1 pt) Let S 1 be the number of data-points processed by server 1 before it stops. State the distribution of S 1 , including any parameters. 一

<!-- formula-not-decoded -->

- b) (1 pt) Let S 2 be the number of data-points processed by server 2 before it stops. State the distribution of S 2 , including any parameters.

<!-- formula-not-decoded -->

- c) (4 pts) What is the probability that exactly 10 data-points are processed before the program stops?

ー

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- d) (3 pts) You leave your code running and when you come back you see it processed 10 data-points. Which server is more likely to have received the data for processing? Justify numerically.

<!-- formula-not-decoded -->

## Question 4

Let A and B be two events in the sample space ! . Prove

<!-- formula-not-decoded -->

using probability axioms, principles, or event laws. State any probability axioms, principles, and/or laws that you use in your proof.

<!-- formula-not-decoded -->

## Question 5

The time T between two customer arrivals at the take-out window of a fast food chain is exponentially distributed with an average of 2.5 minutes. σ

- a) (1 pt) Find the mean and standard deviation in time between customer arrivals at the take-out window.

、

- b) (2 pts) Compute the probability that there is more than 5 minutes before the first customer arrives at the take-out window.
- c) (2 pts) Let W be the random variable representing the number of customer arrivals in a 5 minute window. State the distribution of W , including its parameter and parameter value.

- d) (2 pts) Without calculating, find the probability P ( W = 0) . Justify your answer in 1-2 sentences.
- e) (5 pts)
3. (i) Find the exact probability that the time until the next customer arrival is within 1.5 standard deviations of the mean time.
4. (ii) Find the bound on the probability of the event described in (i).
5. (iii) Which probability in (i) and (ii) is more accurate? Briefly explain why.

## Question 6

You are reading some code that your friend ran to practice some skills from estimating probabilities of a random variable X in R. Read the code snippet below and answer the questions by referring to names of R objects defined in the code snippet .

```
31 x <- seq(-1, 7, by = 2) 32 probs <-c(0.25, 0.1, 0.3, 0.15, 0.2) 33 34 more.than3 <- 0 35 is.7 <- 0 36 ntrials <- 0 37 38 while (more.than3 <= 100){ 39 draw <- sample(x, (1/ probs, replace = T) 40 ntrials = ntrials + 1 41 if (draw > 3){ 42 more.than3 = more.than3+1. 43 if (draw == 7){ 44 is.7 = is.7 + 1 45 46 } 47} 48 49 is.7/more.than3 113 , 5 , 7
```

- a) (1 pt) How would you find the number of simulations that were run? atrials .
- b) (1 pt) What is she trying to estimate in the last line of her code? Express in probability notation.

put Abe

c) (1

.

norethous

B

pt)

How would your friend compute is

.,

the probability

is

P

She

(

X

is

= 7)

using their simulation

?

- d) (2 pts) Which part of the code snippet would you change to improve her estimate? Briefly explain in 1-2 students how it will improve. 7/utrial

.

```
I would. fix the nowbor of trioels each time. we stop. when nore thon s. reach (wow, it is wove roudondro Study. the distribation of uvanber of. trials to achieve tht. 1 If we wat. to wodel the Prob for.X ve uurt to fix the triad eadh tine currently , ,
```

.