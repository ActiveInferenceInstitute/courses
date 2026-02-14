# Practice Quiz: Agents

## Part A: Multiple Choice

1. Which matrix in the `GenerativeModel` encodes $P(o \mid s)$?
A) B-matrix
B) C-vector
C) A-matrix
D) D-vector

2. What is the correct shape of a B-matrix for a system with 4 states and 3 actions?
A) `(3, 4, 4)`
B) `(4, 4, 3)`
C) `(4, 3)`
D) `(3, 3, 4)`

3. Setting `C = np.zeros(num_obs)` makes the agent:
A) Unable to act
B) Purely exploitative
C) Purely epistemic (information-seeking)
D) Random

4. If `model.E = np.array([0.99, 0.01])`, the agent:
A) Always selects action 0
B) Has a strong habit prior favoring policy 0
C) Ignores EFE entirely
D) Has a strong preference for observation 0

5. The precision parameter γ controls:
A) How noisy observations are
B) How sharply the agent commits to the best policy
C) The learning rate for Dirichlet updates
D) The number of hidden states

6. What line of code creates an agent with 3-step policies `[[0,0,0], [1,1,1]]`?
A) `ActiveInferenceAgent(model, policies=3)`
B) `ActiveInferenceAgent(model, policies=[[0,0,0], [1,1,1]])`
C) `ActiveInferenceAgent(model, num_policies=2)`
D) `ActiveInferenceAgent(model, depth=3)`

7. `model.predict_observation(q_s)` computes:
A) $\mathbf{B} \cdot q(s)$
B) $\mathbf{A} \cdot q(s)$
C) $\mathbf{C} \cdot q(s)$
D) $\mathbf{D} \cdot q(s)$

## Part B: Short Answer

1. Write the complete code to construct a `GenerativeModel` for a 2-state, 2-observation, 1-action system where the A-matrix is the identity and the B-matrix swaps states. Include C and D vectors.

2. Explain what `agent.step(obs)` does internally. List the three sub-methods it calls and what each one computes.

3. An agent has `C = [5, 0, -5]` for observations (food, neutral, predator). Describe in words what behavior this C-vector would produce and explain the mechanism through EFE.
