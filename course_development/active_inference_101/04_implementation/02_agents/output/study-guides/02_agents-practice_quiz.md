# Practice Quiz: Agents (Implementation)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** The ActiveInferenceAgent class stores beliefs in:
A) self.A
B) self.qs — the posterior distribution over hidden states
C) self.C
D) self.gamma

**2.** The infer_states method implements:
A) Policy evaluation
B) Bayesian updating: posterior = normalize(likelihood × prior)
C) Action selection
D) Environment simulation

**3.** The _compute_efe method calculates:
A) The observation likelihood
B) Expected Free Energy by summing pragmatic and epistemic terms over predicted futures
C) The transition probability
D) The number of policies

**4.** The SimpleEnvironment generates observations by:
A) Always returning the same value
B) Sampling from P(o | s) using the true A matrix and current state
C) Reading from a file
D) Copying the agent's beliefs

**5.** The simulation loop connects agent and environment through:
A) Shared memory
B) Observe → Infer → Select → Act → Repeat
C) A single function call
D) Random steps

**6.** Setting gamma = 0 would cause the agent to:
A) Always select the best policy
B) Select policies nearly uniformly (random behavior) regardless of EFE
C) Crash the program
D) Move faster

**7.** The agent logs belief_history, action_history, and obs_history for:
A) Entertainment
B) Analysis and debugging — understanding the agent's decision-making over time
C) Sending to another agent
D) Reducing computation

## Part B: Short Answer

**1.** Write the key lines of the `infer_states` method and explain what each line does.

**2.** Explain what happens in the simulation loop when the agent's model (A matrix) is slightly wrong — different from the environment's true A matrix. How does this affect behavior?

**3.** Design a test to verify that the agent's policy selection is working correctly. What should happen when C strongly favors one observation? When C is uniform?
