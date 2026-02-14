# Practice Quiz: Systems

## Part A: Multiple Choice

1. What does the `true_A` matrix in a `DiscreteEnvironment` represent?
A) The agent's beliefs about observations
B) The true probability of observing $o$ given hidden state $s$
C) The transition dynamics between states
D) The agent's prior over initial states

2. If `true_A` has shape `(5, 3)`, the environment has:
A) 5 states and 3 observations
B) 3 states and 5 observations
C) 5 observations and 3 states
D) 15 state-observation pairs

3. When `env.step(action)` is called, what happens first?
A) An observation is generated from the current state
B) The hidden state transitions according to `true_B`
C) The agent updates its beliefs
D) Free energy is computed

4. A fully observable environment corresponds to:
A) `true_A` being all zeros
B) `true_A` being the identity matrix
C) `true_B` being the identity matrix
D) `true_A` having uniform columns

5. If `true_B` is passed as a 2-D matrix (shape `(N, N)`), the environment assumes:
A) There are N possible actions
B) There is exactly 1 action
C) The transitions are stochastic
D) The B matrix is invalid

6. After calling `env.reset(initial_state=0)` followed by 10 calls to `env.step()`, how many entries does `env.history["states"]` contain?
A) 10
B) 11
C) 9
D) 12

7. The key difference between `DiscreteEnvironment` and `GenerativeModel` is:
A) `DiscreteEnvironment` uses continuous states
B) `GenerativeModel` represents ground truth; `DiscreteEnvironment` is an approximation
C) `DiscreteEnvironment` represents ground truth; `GenerativeModel` is the agent's hypothesis
D) There is no difference; they use the same matrices

## Part B: Short Answer

1. Write Python code to create a `DiscreteEnvironment` for a 3-state system where observations are deterministic (identity A-matrix) and action 0 keeps the state while action 1 cycles through states. Show the `true_A` and `true_B` matrices.

2. Explain why columns (not rows) of the `true_A` matrix must sum to 1.0. What probability is each column encoding, and what would go wrong if the normalization were over rows instead?

3. You observe the sequence $[0, 0, 1, 0, 1]$ from a 2-state environment. Using Bayes' rule and the `true_A` matrix $\begin{bmatrix} 0.9 & 0.2 \\ 0.1 & 0.8 \end{bmatrix}$, compute $P(s_0 = 0 \mid o_0 = 0)$ assuming a uniform prior $P(s_0) = [0.5, 0.5]$.
