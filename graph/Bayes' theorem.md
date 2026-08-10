---
broader: "[[Probability]]"
inferred:skos:ancestor: "[[probability]]"
inferred:skos:broader: "[[probability]]"
inferred:skos:narrower: "[[Bayesian inference]]"
---
Basis of bayesian statistics where we take prior knowledge into account before calculating new probabilities. 

Bayes' theorem (alternatively Bayes' law or Bayes' rule, after Thomas Bayes) gives a mathematical rule for inverting conditional probabilities, allowing one to find the probability of a cause given its effect. For example, if the risk of developing health problems is known to increase with age, Bayes' theorem allows the risk to someone of a known age to be assessed more accurately by conditioning it relative to their age, rather than assuming that the person is typical of the population as a whole. Based on Bayes' law, both the prevalence of a disease in a given population and the error rate of an infectious disease test must be taken into account to evaluate the meaning of a positive test result and avoid the base-rate fallacy.

One of Bayes' theorem's many applications is Bayesian inference, an approach to statistical inference, where it is used to invert the probability of observations given a model configuration (i.e., the likelihood function) to obtain the probability of the model configuration given the observations (i.e., the posterior probability).

## Statement of theorem



Bayes' theorem is stated mathematically as the following equation:[[17]](#cite_note-18)

![{\displaystyle P(A\vert B)={\frac {P(B\vert A)P(A)}{P(B)}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4211e3e7c3482573cdfbc0653d48a6279104c899)

where ![{\displaystyle A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7daff47fa58cdfd29dc333def748ff5fa4c923e3) and ![{\displaystyle B}](https://wikimedia.org/api/rest_v1/media/math/render/svg/47136aad860d145f75f3eed3022df827cee94d7a) are [events](https://en.wikipedia.org/wiki/Event_\(probability_theory\) "Event (probability theory)") and ![{\displaystyle P(B)\neq 0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4696c4543d63622a09c29cbb00c0fea4e0b8d7b7).

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Bayes_theorem_visual_proof.svg/170px-Bayes_theorem_visual_proof.svg.png)](https://en.wikipedia.org/wiki/File:Bayes_theorem_visual_proof.svg)

Visual proof of Bayes' theorem

Bayes' theorem may be derived from the definition of [conditional probability](https://en.wikipedia.org/wiki/Conditional_probability "Conditional probability"):

![{\displaystyle P(A\vert B)={\frac {P(A\cap B)}{P(B)}},{\text{ if }}P(B)\neq 0,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8933ae615029cbf453fd2908335dc816b7a66df9)

where ![{\displaystyle P(A\cap B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f22276bc48d131dadc7e4dacbf38cee3ed05d536) is the probability of both A and B being true. Similarly,

![{\displaystyle P(B\vert A)={\frac {P(A\cap B)}{P(A)}},{\text{ if }}P(A)\neq 0.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e46e9d1e9656e662594c1c41cc1d170ae5208f58)

Solving for ![{\displaystyle P(A\cap B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f22276bc48d131dadc7e4dacbf38cee3ed05d536) and substituting into the above expression for ![{\displaystyle P(A\vert B)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8114af1733b7f0ad6aa718629a01264569d689ee) yields Bayes' theorem:

![{\displaystyle P(A\vert B)={\frac {P(B\vert A)P(A)}{P(B)}},{\text{ if }}P(B)\neq 0.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6158075cb0aa165f426e663093f2a1351e447b3c)


## Recreational mathematics

Bayes' rule and computing [conditional probabilities](https://en.wikipedia.org/wiki/Conditional_probability "Conditional probability") provide a method to solve a number of popular puzzles, such as the [Three Prisoners problem](https://en.wikipedia.org/wiki/Three_Prisoners_problem "Three Prisoners problem"), the [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem "Monty Hall problem"), the [Two Child problem](https://en.wikipedia.org/wiki/Boy_or_Girl_paradox "Boy or Girl paradox"), and the [Two Envelopes problem](https://en.wikipedia.org/wiki/Two_envelopes_problem "Two envelopes problem").

Suppose, a particular test for whether someone has been using cannabis is 90% [sensitive](https://en.wikipedia.org/wiki/Sensitivity_\(tests\) "Sensitivity (tests)"), meaning the [true positive rate](https://en.wikipedia.org/wiki/True_positive_rate "True positive rate") (TPR) = 0.90. Therefore, it leads to 90% true positive results (correct identification of drug use) for cannabis users.

The test is also 80% [specific](https://en.wikipedia.org/wiki/Specificity_\(tests\) "Specificity (tests)"), meaning [true negative rate](https://en.wikipedia.org/wiki/True_negative_rate "True negative rate") (TNR) = 0.80. Therefore, the test correctly identifies 80% of non-use for non-users, but also generates 20% false positives, or [false positive rate](https://en.wikipedia.org/wiki/False_positive_rate "False positive rate") (FPR) = 0.20, for non-users.

Assuming 0.05 [prevalence](https://en.wikipedia.org/wiki/Prevalence "Prevalence"), meaning 5% of people use cannabis, what is the [probability](https://en.wikipedia.org/wiki/Probability "Probability") that a random person who tests positive is really a cannabis user?

The [Positive predictive value](https://en.wikipedia.org/wiki/Positive_predictive_value "Positive predictive value") (PPV) of a test is the proportion of persons who are actually positive out of all those testing positive, and can be calculated from a sample as:

PPV = True positive / Tested positive

If sensitivity, specificity, and prevalence are known, PPV can be calculated using Bayes' theorem. Let ![{\displaystyle P({\text{User}}\vert {\text{Positive}})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d138c95f551ed76cc90c8a0592cd42768ec972b7) mean "the probability that someone is a cannabis user given that they test positive", which is what PPV means. We can write:

![{\displaystyle {\begin{aligned}P({\text{User}}\vert {\text{Positive}})&={\frac {P({\text{Positive}}\vert {\text{User}})P({\text{User}})}{P({\text{Positive}})}}\\&={\frac {P({\text{Positive}}\vert {\text{User}})P({\text{User}})}{P({\text{Positive}}\vert {\text{User}})P({\text{User}})+P({\text{Positive}}\vert {\text{Non-user}})P({\text{Non-user}})}}\\[8pt]&={\frac {0.90\times 0.05}{0.90\times 0.05+0.20\times 0.95}}={\frac {0.045}{0.045+0.19}}\approx 19\%\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c26c47487bf7b0fc56304c7123c3890a2b3e0f15)


The denominator ![{\displaystyle P({\text{Positive}})=P({\text{Positive}}\vert {\text{User}})P({\text{User}})+P({\text{Positive}}\vert {\text{Non-user}})P({\text{Non-user}})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/bd7a281e27f176df4cbf947aa5d334e056b42392) is a direct application of the [Law of Total Probability](https://en.wikipedia.org/wiki/Law_of_Total_Probability "Law of Total Probability"). In this case, it says that the probability that someone tests positive is the probability that a user tests positive times the probability of being a user, plus the probability that a non-user tests positive, times the probability of being a non-user. This is true because the classifications user and non-user form a [partition of a set](https://en.wikipedia.org/wiki/Partition_of_a_set "Partition of a set"), namely the set of people who take the drug test. This combined with the definition of [conditional probability](https://en.wikipedia.org/wiki/Conditional_probability "Conditional probability") results in the above statement.

In other words, if someone tests positive, the probability that they are a cannabis user is only 19%—because in this group, only 5% of people are users, and most positives are false positives coming from the remaining 95%.

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Bayes-rule3.png/220px-Bayes-rule3.png)](https://en.wikipedia.org/wiki/File:Bayes-rule3.png)

Using a frequency box to show ![{\displaystyle P({\text{User}}\vert {\text{Positive}})}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d138c95f551ed76cc90c8a0592cd42768ec972b7) visually by comparison of shaded areas. Note how small the pink area of true positives is compared to the blue area of false positives.

If 1,000 people were tested:

- 950 are non-users and 190 of them give false positive (0.20 × 950)
- 50 of them are users and 45 of them give true positive (0.90 × 50)

The 1,000 people thus have 235 positive tests, of which only 45 are genuine, about 19%.

#### Sensitivity or specificity

[[edit](https://en.wikipedia.org/w/index.php?title=Bayes%27_theorem&action=edit&section=10 "Edit section: Sensitivity or specificity")]

The importance of [specificity](https://en.wikipedia.org/wiki/Specificity_\(tests\) "Specificity (tests)") can be seen by showing that even if sensitivity is raised to 100% and specificity remains at 80%, the probability that someone who tests positive is a cannabis user rises only from 19% to 21%, but if the sensitivity is held at 90% and the specificity is increased to 95%, the probability rises to 49%.

|Test<br><br>Actual|Positive|Negative||Total|
|---|---|---|---|---|
|User|**45**|5|50|
|Non-user|190|760|950|
||   |   |   |   |
|Total|**235**|765|1000|
|90% sensitive, 80% specific, PPV=45/235 ≈ 19%|   |   |   |   |

|Test<br><br>Actual|Positive|Negative||Total|
|---|---|---|---|---|
|User|**50**|0|50|
|Non-user|190|760|950|
||   |   |   |   |
|Total|**240**|760|1000|
|100% sensitive, 80% specific, PPV=50/240 ≈ 21%|   |   |   |   |

|Test<br><br>Actual|Positive|Negative||Total|
|---|---|---|---|---|
|User|**45**|5|50|
|Non-user|47|903|950|
||   |   |   |   |
|Total|**92**|908|1000|
|90% sensitive, 95% specific, PPV=45/92 ≈ 49%|   |   |   |   |

If all patients with pancreatic cancer have a certain symptom, it does not follow that anyone who has that symptom has a 100% chance of getting pancreatic cancer. Assuming the incidence rate of pancreatic cancer is 1/100000, while 10/99999 healthy individuals have the same symptoms worldwide, the probability of having pancreatic cancer given the symptoms is 9.1%, and the other 90.9% could be "false positives" (that is, falsely said to have cancer; "positive" is a confusing term when, as here, the test gives bad news).

Based on incidence rate, the following table presents the corresponding numbers per 100,000 people.

|Symptom<br><br>Cancer|Yes|No||Total|
|---|---|---|---|---|
|Yes|1|0|1|
|No|10|99989|99999|
||   |   |   |   |
|Total|11|99989|100000|

Which can then be used to calculate the probability of having cancer when you have the symptoms:

![{\displaystyle {\begin{aligned}P({\text{Cancer}}|{\text{Symptoms}})&={\frac {P({\text{Symptoms}}|{\text{Cancer}})P({\text{Cancer}})}{P({\text{Symptoms}})}}\\&={\frac {P({\text{Symptoms}}|{\text{Cancer}})P({\text{Cancer}})}{P({\text{Symptoms}}|{\text{Cancer}})P({\text{Cancer}})+P({\text{Symptoms}}|{\text{Non-Cancer}})P({\text{Non-Cancer}})}}\\[8pt]&={\frac {1\times 0.00001}{1\times 0.00001+(10/99999)\times 0.99999}}={\frac {1}{11}}\approx 9.1\%\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d78d8f2bcc4f4b701033a5b1f1c2bf6c050970f6)

### Defective item rate

[[edit](https://en.wikipedia.org/w/index.php?title=Bayes%27_theorem&action=edit&section=12 "Edit section: Defective item rate")]

|Condition<br><br>Machine|Defective|Flawless||Total|
|---|---|---|---|---|
|A|10|190|200|
|B|9|291|300|
|C|**5**|495|500|
||   |   |   |   |
|Total|**24**|976|1000|

A factory produces items using three machines—A, B, and C—which account for 20%, 30%, and 50% of its output, respectively. Of the items produced by machine A, 5% are defective, while 3% of B's items and 1% of C's are defective. If a randomly selected item is defective, what is the probability it was produced by machine C?

Once again, the answer can be reached without using the formula by applying the conditions to a hypothetical number of cases. For example, if the factory produces 1,000 items, 200 will be produced by A, 300 by B, and 500 by C. Machine A will produce 5% × 200 = 10 defective items, B 3% × 300 = 9, and C 1% × 500 = 5, for a total of 24. Thus 24/1000 (2.4%) of the total output will be defective and the likelihood that a randomly selected defective item was produced by machine C is 5/24 (~20.83%).

This problem can also be solved using Bayes' theorem: Let _Xi_ denote the event that a randomly chosen item was made by the _i_ th machine (for _i_ = A,B,C). Let _Y_ denote the event that a randomly chosen item is defective. Then, we are given the following information:

![{\displaystyle P(X_{A})=0.2,\quad P(X_{B})=0.3,\quad P(X_{C})=0.5.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e7b055f1700a12db75d72221ca43686e19b623f8)

If the item was made by the first machine, then the probability that it is defective is 0.05; that is, _P_(_Y_ | _X_A) = 0.05. Overall, we have

![{\displaystyle P(Y|X_{A})=0.05,\quad P(Y|X_{B})=0.03,\quad P(Y|X_{C})=0.01.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/42e390b71af825f5f34b8001e6f1e5a1cfc305c7)

To answer the original question, we first find _P_(Y). That can be done in the following way:

![{\displaystyle P(Y)=\sum _{i}P(Y|X_{i})P(X_{i})=(0.05)(0.2)+(0.03)(0.3)+(0.01)(0.5)=0.024.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2ba5ec579a63c77e821a4fa42dcc4be5519eac05)

Hence, 2.4% of the total output is defective.

We are given that _Y_ has occurred and we want to calculate the conditional probability of _X_C. By Bayes' theorem,

![{\displaystyle P(X_{C}|Y)={\frac {P(Y|X_{C})P(X_{C})}{P(Y)}}={\frac {0.01\cdot 0.50}{0.024}}={\frac {5}{24}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/04d3d5182f6344e07323113d18c47afb33b227c1)

Given that the item is defective, the probability that it was made by machine C is 5/24. C produces half of the total output but a much smaller fraction of the defective items. Hence the knowledge that the item selected was defective enables us to replace the prior probability _P_(_X_C) = 1/2 by the smaller posterior probability _P_(XC | _Y_) = 5/24.

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Bayes_theorem_assassin.svg/220px-Bayes_theorem_assassin.svg.png)](https://en.wikipedia.org/wiki/File:Bayes_theorem_assassin.svg)

A geometric visualization of Bayes' theorem using astronauts, from the online game _[Among Us](https://en.wikipedia.org/wiki/Among_Us "Among Us")_, who may be suspicious (with eyebrows) and may be assassins (with daggers)

The interpretation of Bayes' rule depends on the [interpretation of probability](https://en.wikipedia.org/wiki/Probability_interpretations "Probability interpretations") ascribed to the terms. The two predominant interpretations are described below.

### Bayesian interpretation

[[edit](https://en.wikipedia.org/w/index.php?title=Bayes%27_theorem&action=edit&section=14 "Edit section: Bayesian interpretation")]

In the [Bayesian (or epistemological) interpretation](https://en.wikipedia.org/wiki/Bayesian_probability "Bayesian probability"), probability measures a "degree of belief". Bayes' theorem links the degree of belief in a proposition before and after accounting for evidence. For example, suppose it is believed with 50% certainty that a coin is twice as likely to land heads than tails. If the coin is flipped a number of times and the outcomes observed, that degree of belief will probably rise or fall, but might remain the same, depending on the results. For proposition _A_ and evidence _B_,

- _P_ (_A_), the _prior_, is the initial degree of belief in _A_.
- _P_ (_A_ | _B_), the _posterior_, is the degree of belief after incorporating news that _B_ is true.
- the quotient ⁠_P_(_B_ | _A_)/_P_(_B_)⁠ represents the support _B_ provides for _A_.

For more on the application of Bayes' theorem under the Bayesian interpretation of probability, see [Bayesian inference](https://en.wikipedia.org/wiki/Bayesian_inference "Bayesian inference").

