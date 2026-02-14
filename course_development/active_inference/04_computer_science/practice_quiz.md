# Practice Quiz: Computational Active Inference

## Part A: Multiple Choice

1. In the `active_inference` library, the `DiscreteEnvironment` class represents:
A) The agent's generative model
B) The true causal structure of the environment (generative process)
C) The visualization configuration
D) The policy selection mechanism

2. Each column of the A matrix (likelihood matrix) must:
A) Sum to zero
B) Be a unit vector
C) Sum to one (each column is a probability distribution over observations given a state)
D) Be equal to every other column

3. When computing expected free energy G, the epistemic value (ambiguity resolution) term is high when:
A) The agent already knows the state with certainty
B) The action is expected to produce observations that significantly reduce uncertainty about hidden states
C) The preferred outcome probability is uniform
D) The transition matrix is an identity matrix

4. What does `update_dirichlet_A(pA, observation, state)` do?
A) Replaces the A matrix entirely with the observation
B) Increments the concentration parameter at position [observation, state] by one
C) Normalizes the A matrix columns
D) Resets the A matrix to uniform

5. In a multi-agent signaling game, emergent communication arises because:
A) The agents are programmed with a shared language
B) One agent's active states become another's sensory states, and both minimize free energy
C) The environment explicitly rewards communication
D) The agents share the same generative model

6. The precision parameter gamma in the softmax policy selection:
A) Has no effect on behavior
B) Controls the tradeoff between deterministic and stochastic policy selection
C) Only affects the A matrix
D) Is always set to 1.0

7. Sophisticated inference differs from simple expected free energy planning by:
A) Ignoring future consequences entirely
B) Recursively evaluating how beliefs would update at each future time step
C) Using reinforcement learning instead of free energy
D) Requiring continuous rather than discrete state spaces

## Part B: Short Answer

1. Given a 3-state, 2-observation system with A = [[0.9, 0.1, 0.5], [0.1, 0.9, 0.5]], prior beliefs D = [0.33, 0.33, 0.34], and observation o=0, compute the updated posterior beliefs using one step of variational inference. Show your work.

2. Explain why an Active Inference agent with a perfectly accurate generative model (A_model = A_true, B_model = B_true) would still act in the environment rather than remaining passive. What drives action when perception is already optimal?

3. Design a simple 2-state environment where an Active Inference agent with uniform C (no preferences) still exhibits structured behavior. Explain what drives this behavior in the absence of pragmatic value and why epistemic value alone is sufficient to produce non-random action.
