# Practice Quiz: Perception (Implementation)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** Variational message passing differs from simple Bayesian updating because:
A) It doesn't use Bayes' theorem
B) It iterates, combining messages from past, present, and future until convergence
C) It's slower and less accurate
D) It only works with continuous states

**2.** The three messages combined at each time step are:
A) Input, output, error
B) Observation likelihood, prior/transition from past, and message from future
C) Left, right, center
D) Fast, medium, slow

**3.** Prediction error in this implementation is computed as:
A) The sum of all observations
B) The difference between actual and predicted observations (or states)
C) A random number
D) The log of the A matrix

**4.** Precision weighting multiplies prediction errors by:
A) Zero
B) A scalar precision value — higher precision means more influence
C) The number of states
D) Negative one

**5.** Free energy F = Complexity - Accuracy means:
A) Simpler models are always better
B) Good inference balances explaining data (accuracy) and staying close to priors (complexity)
C) Complexity is always bad
D) Accuracy doesn't matter

**6.** Working in log space (log probabilities) is important because:
A) Logs are easier to type
B) It prevents numerical underflow from multiplying many small probabilities
C) Python requires it
D) It makes values negative

**7.** The convergence of message passing means:
A) The algorithm crashes
B) Beliefs stop changing significantly between iterations
C) All states become equally likely
D) Observations stop arriving

## Part B: Short Answer

**1.** Trace through one iteration of the message passing algorithm for t=1 in a 2-state model. Show the three messages being combined and the resulting belief update.

**2.** Explain how precision weighting implements attention in code. Give an example where you would set high precision for one observation channel and low for another.

**3.** Design a test to verify your free energy computation is correct. What properties should F have? (e.g., F should decrease when beliefs improve, F should decompose correctly into accuracy and complexity)
