# Practice Quiz: Learning (Implementation)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** Dirichlet concentration parameters encode:
A) The exact probability values
B) Pseudo-counts that represent accumulated experience — more counts = more confidence
C) The number of states
D) The temperature of the system

**2.** The Dirichlet mean E[θ_i] = α_i / Σα gives:
A) The mode of the distribution
B) The expected probability for each outcome, computed from concentration parameters
C) The variance
D) A random sample

**3.** The `update_A` method increments concentration parameters by:
A) A fixed learning rate
B) The outer product of the observation vector and state beliefs
C) One everywhere
D) A random amount

**4.** Learning rate decreases because:
A) We manually reduce it
B) Each new observation contributes 1/N to the total, where N grows with experience
C) The agent gets tired
D) Python slows down

**5.** A strong Dirichlet prior (large α):
A) Learns from every observation equally
B) Changes slowly because each new observation is a small fraction of total experience
C) Is always better
D) Cannot be overridden

**6.** To implement "forgetting," you would:
A) Delete the agent
B) Reset concentration parameters to smaller values, reducing accumulated experience
C) Increase gamma
D) Clear the observation log

**7.** `update_B` needs both previous and current beliefs because:
A) B has 3 dimensions
B) It's learning P(s_t | s_{t-1}, a) — the transition from previous to current state
C) It updates faster that way
D) NumPy requires two arrays

## Part B: Short Answer

**1.** Start with A_prior = [[2, 2], [2, 2]]. After observing state 0 produce observation 0 five times and observation 1 twice, compute the updated A_prior and the new A matrix (Dirichlet mean).

**2.** Explain why a "weak prior" agent learns faster but is initially less accurate, while a "strong prior" agent learns slower but may be initially more accurate. When would you prefer each?

**3.** Design a test to verify your learning implementation: what properties should the learned A matrix have after sufficient observations from a known environment?
