# Practice Quiz: Action

## Part A: Multiple Choice

1. Expected Free Energy $G(\pi)$ is minimized by policies that:
A) Maximize reward
B) Lead to preferred and informative outcomes
C) Maintain the current state
D) Increase entropy

2. The risk component of EFE measures:
A) The KL divergence between predicted and preferred observations
B) The entropy of the posterior
C) The agent's model accuracy
D) The transition probability

3. The ambiguity component of EFE is the:
A) KL divergence between the posterior and prior
B) Expected conditional entropy of the A-matrix along the policy's predicted states
C) Entropy of the C-vector
D) Mutual information between states and observations

4. In the T-maze, the agent visits the cue location because:
A) The cue has the highest C-value
B) The cue reduces ambiguity — it resolves which arm has the reward
C) The agent always visits all states
D) The B-matrix forces the transition

5. `run_policy_inference()` returns `q_pi` which is:
A) A vector of EFE values
B) A probability distribution over policies
C) The selected action index
D) The prior over policies

6. If the A-matrix is the identity (fully observable), the ambiguity for all policies is:
A) Maximum
B) Equal to the risk
C) Zero
D) Undefined

7. The softmax function in policy selection converts:
A) Positive EFE values to probabilities
B) Negative-γ-scaled EFE values (plus log-E) to probabilities
C) Observation likelihoods to beliefs
D) C-vector to preferred distribution

## Part B: Short Answer

1. A 2-state agent has $q(s) = [1, 0]$, $A = I$, $B_{a=0} = I$, $C = [3, -3]$. Compute $G(a = 0)$ by hand, showing risk and ambiguity separately.

2. Explain why an agent with `C = np.zeros(num_obs)` and a noisy A-matrix still takes non-random actions. What drives its behavior and which EFE component is responsible?

3. Describe the full path from observation to action in a single `agent.step(obs)` call. List every function invoked, what it computes, and what data flows between them.
