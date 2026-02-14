# Practice Quiz: Cognition

## Part A: Multiple Choice

1. The C-vector encodes:
A) Transition probabilities between states
B) Log-preferences over observations
C) Prior beliefs over initial states
D) The agent's learning rate

2. If `C = [0, 0, 0]`, the agent's behavior is driven entirely by:
A) Risk (pragmatic value)
B) Ambiguity (epistemic value)
C) Habits (E-vector)
D) Nothing — the agent is frozen

3. The D-vector is used in Active Inference as:
A) The posterior after the first observation
B) The initial prior for state inference
C) The reward signal
D) The transition dynamics prior

4. What role does the E-vector play in the policy posterior equation?
A) It replaces EFE entirely
B) It adds a log-prior bias to each policy's score
C) It scales the precision parameter
D) It modifies the A-matrix

5. When precision γ = 0.01, the agent's policy selection is:
A) Nearly deterministic
B) Nearly random (or dominated by habits if E is set)
C) Identical to maximum EFE selection
D) Always action 0

6. The risk component of EFE is $D_{KL}[q(o|\pi) \| \tilde{P}(o)]$. The target distribution $\tilde{P}(o)$ is:
A) The empirical observation frequency
B) $\sigma(C)$ — the softmax of the C-vector
C) The A-matrix likelihood
D) A uniform distribution

7. `plot_D_prior()` annotates the bar chart with:
A) The VFE value
B) The entropy of D
C) The number of states
D) The D-vector norm

## Part B: Short Answer

1. An agent has `C = [0, 5, -5]` for (neutral, food, predator). Its current beliefs are $q(s) = [0.5, 0.5]$. The A-matrix maps state 0 to observation 1 (food) and state 1 to observation 2 (predator). Describe qualitatively what policy the agent should prefer and why, in terms of the risk component.

2. Write code to create an `ActiveInferenceAgent` with a habit prior that strongly favors policy 1 (go-left) and a low precision γ = 0.1. Explain why this agent would almost always go left regardless of observations.

3. Design an experiment to determine the "critical γ" at which an agent transitions from exploratory to exploitative behavior. Describe the setup, the measurement, and what plot you would produce.
