# Practice Quiz: Learning (Mathematical Frameworks)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** Parameter learning in Active Inference updates:
A) The agent's beliefs about hidden states
B) The concentration parameters of the A and B matrices
C) The agent's physical body
D) The number of observations

**2.** Dirichlet distributions are used for parameters because:
A) They are the only distribution
B) They are conjugate to the categorical distribution — posterior stays in the same family
C) They are always uniform
D) They represent continuous data

**3.** As concentration parameters grow larger:
A) The agent becomes more uncertain
B) The agent becomes more confident and the effective learning rate decreases
C) The agent forgets everything
D) The model structure changes

**4.** Bayesian Model Reduction (BMR) selects:
A) The most complex model available
B) The simplest model that explains the data well — implementing Occam's razor
C) A random model
D) The model with the most parameters

**5.** The effective learning rate decreases because:
A) The brain gets tired
B) Each new observation has proportionally less influence as total experience grows
C) The agent stops observing
D) Synapses degrade

**6.** Structure learning differs from parameter learning because:
A) Structure learning changes what states and connections exist, not just their values
B) They are the same thing
C) Structure learning is faster
D) Parameter learning requires no data

**7.** BMR is computationally cheap because:
A) It uses quantum computing
B) It compares model evidence analytically without re-fitting from scratch
C) It ignores all data
D) It only considers two models

## Part B: Short Answer

**1.** An agent starts with α = [2, 2] (2 outcomes). After 8 observations of outcome 1 and 2 observations of outcome 2, compute: (a) α_posterior, (b) expected probabilities, (c) the effective learning rate for the next observation.

**2.** Explain why the natural learning rate decay (from Dirichlet updating) is generally optimal, but give one example where it could be harmful (e.g., in a suddenly changed environment).

**3.** Compare parameter learning and structure learning. Give a real-life example of each. When would the brain/agent choose to restructure its model rather than just updating parameters?
