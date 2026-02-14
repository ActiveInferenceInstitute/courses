# Practice Quiz: Agents (Mathematical Frameworks)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** Exact Bayesian inference is intractable because:
A) Bayes' theorem is incorrect
B) Computing P(o) requires summing over every possible state, which grows exponentially
C) Probabilities can't be computed
D) The brain doesn't use probability

**2.** The recognition model q(s) is:
A) The exact posterior distribution
B) An approximate posterior — the agent's best guess about hidden states
C) The prior distribution
D) The likelihood function

**3.** KL divergence D_KL[q(s) || P(s | o)] equals zero when:
A) q is very different from P
B) q(s) perfectly matches the true posterior P(s | o)
C) The agent has no data
D) All states are equally likely

**4.** The ELBO decomposes into:
A) Prior + Posterior
B) Accuracy (how well q explains data) minus Complexity (how far q is from the prior)
C) Reward minus Cost
D) Input minus Output

**5.** Variational free energy F is:
A) Physical energy in the brain
B) The negative ELBO — minimizing F is equivalent to good inference
C) Always zero
D) The temperature of the system

**6.** The accuracy-complexity trade-off means:
A) Always prefer the most complex model
B) Balance fitting the data well with keeping the model simple
C) Accuracy and complexity are the same thing
D) Ignore complexity entirely

**7.** Variational inference turns inference into:
A) A search problem
B) An optimization problem — adjusting q(s) to minimize free energy
C) A random guess
D) Exact computation

## Part B: Short Answer

**1.** Explain in your own words why the brain must use approximate inference rather than exact Bayesian inference. Use a concrete example to illustrate the computational challenge.

**2.** Consider two approximate posteriors for the state "is it raining?":

- q₁: P(rain) = 0.7, P(no rain) = 0.3
- q₂: P(rain) = 0.9, P(no rain) = 0.1

If the true posterior is P(rain | data) = 0.8, which approximation has lower KL divergence? Why?

**3.** Explain the ELBO accuracy-complexity trade-off using a real-world analogy. For example, compare a weather forecast model that uses 3 variables vs. one that uses 100 variables.
