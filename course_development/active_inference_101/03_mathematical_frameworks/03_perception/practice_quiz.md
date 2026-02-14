# Practice Quiz: Perception (Mathematical Frameworks)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** Variational free energy F can be decomposed as:
A) F = Reward - Cost
B) F = Complexity - Accuracy = D_KL[q||prior] - E_q[log P(o|s)]
C) F = Input + Output
D) F = Prior × Likelihood

**2.** For Gaussian models, minimizing free energy reduces to minimizing:
A) The sum of all observations
B) Precision-weighted prediction error: ½ π(o - g(s))²
C) The number of neurons
D) The distance between neurons

**3.** Precision π in the prediction error equation represents:
A) How fast the brain processes information
B) The reliability/confidence of a sensory channel — inverse variance
C) The size of the prediction error
D) The location of the observation

**4.** When precision is high, a prediction error:
A) Is ignored
B) Has a large influence on belief updating
C) Becomes negative
D) Doesn't exist

**5.** In hierarchical free energy minimization, prediction errors flow:
A) Downward (from higher to lower levels)
B) Upward (from lower to higher levels)
C) Only sideways
D) In no particular direction

**6.** The accuracy-complexity trade-off means:
A) Maximize accuracy at all costs
B) Good models explain data well (accuracy) while remaining as simple as possible (complexity)
C) Complexity is always bad
D) Accuracy is impossible to achieve

**7.** Gradient descent on free energy is the mathematical description of:
A) Physical movement
B) Belief updating — iteratively adjusting beliefs to reduce prediction error
C) Muscle contraction
D) Memory storage

## Part B: Short Answer

**1.** You observe a temperature of 25°C. Your model predicts 20°C. The precision of the thermometer is π = 2. Compute the prediction error and the weighted prediction error (½ π(o - g(s))²). If precision drops to π = 0.5 (unreliable thermometer), recompute. What changes?

**2.** Explain how the equation F = Complexity - Accuracy unifies two desires: fitting the data and keeping the model simple. Give a perception example where the brain must balance these.

**3.** In a hierarchical model with 3 levels, explain what happens when a completely unexpected stimulus appears at the lowest level (e.g., a flying pig). How do prediction errors propagate up the hierarchy, and how might higher levels respond?
