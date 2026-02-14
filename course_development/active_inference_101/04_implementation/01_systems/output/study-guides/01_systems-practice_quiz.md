# Practice Quiz: Systems (Implementation)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** In the Active Inference implementation, the A matrix has shape:
A) (num_states, num_observations)
B) (num_observations, num_states) — rows are observations, columns are states
C) (num_actions, num_states)
D) (1, num_states)

**2.** The B matrix has 3 dimensions because:
A) It represents 3D space
B) It stores a separate state-to-state transition matrix for each action
C) Python requires 3D arrays
D) There are always exactly 3 states

**3.** The softmax function converts:
A) Probabilities to log-probabilities
B) Log-scores to normalized probabilities where higher scores get higher probability
C) States to observations
D) Integers to floats

**4.** Numerically stable log uses log(x + ε) because:
A) It makes computations faster
B) It prevents log(0) = -infinity which would crash the program
C) Python requires it
D) It's more accurate

**5.** The normalize function ensures:
A) All values are between -1 and 1
B) The array sums to 1, making it a valid probability distribution
C) All values are positive integers
D) The array is sorted

**6.** To validate a generative model, you should check that:
A) All matrices contain positive integers
B) Columns of A and B sum to 1, and D sums to 1
C) All values are greater than 0.5
D) The matrices are square

**7.** KL divergence D_KL(q || p) = 0 when:
A) q and p are very different
B) q and p are identical distributions
C) q is uniform
D) p is uniform

## Part B: Short Answer

**1.** Write Python code to create an A matrix for a 3-state, 2-observation system where observation is 85% reliable. Include the validation check.

**2.** Implement a Bayesian update function that takes A, prior, and observation_index as inputs and returns the normalized posterior. Show a test case.

**3.** Explain why implementing Active Inference in code is valuable for understanding the theory. Give a specific example of something that becomes clearer through implementation.
