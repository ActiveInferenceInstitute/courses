# Study Questions: Agents

1. What are the five matrices (A, B, C, D, E) in a `GenerativeModel`, and what does each one encode?

2. Why must the columns of the A-matrix sum to 1.0 rather than the rows? What probability does each column represent?

3. Write the Python code to create a `GenerativeModel` for a 3-state, 3-observation system with 2 actions (identity and cyclic permutation), uniform C, uniform D, and no E.

4. What validation error would you get if you passed a B-matrix with shape `(3, 2, 2)` when the A-matrix has shape `(2, 2)`? Why?

5. Explain the role of the precision parameter γ in `ActiveInferenceAgent`. What happens when γ → 0? When γ → ∞?

6. What is the difference between `agent.step(obs)` and calling `agent.infer_states(obs)`, `agent.infer_policies()`, `agent.select_action()` separately?

7. If `model.E = None`, what prior over policies does the agent use? How does this change the policy posterior equation?

8. Describe the relationship between `model.num_actions` and `len(agent.policies)`. Are they always equal?

9. How would you construct custom multi-step policies for a 2-action agent? Provide a Python example with 3-step policies.

10. What does `agent.reset()` do to the agent's beliefs and history? When would you call it during a simulation?

11. Explain why `GenerativeModel` raises a `ValueError` for a D-vector of `[0.5, 0.3]`. What is the validation rule?

12. How does the C-vector influence which actions the agent selects? Trace the path from C through EFE to the policy posterior.

13. If you set `C = np.zeros(num_obs)`, the agent becomes purely epistemic. Explain what "purely epistemic" means in terms of the risk component of EFE.

14. Construct a T-maze `GenerativeModel` with 4 states (center, left, right, cue), 3 observations (neutral, reward, no-reward), and 3 actions (stay, go-left, go-right). Define each matrix.

15. What does `model.predict_observation(q_s)` compute? Write the mathematical formula.

16. Why does `model.predict_state(q_s, action)` need both the belief vector and the action index? What matrix does it use?

17. Explain the output of `model.log_joint(obs=0, state=0)`. What two terms are summed?

18. How does `model.surprisal(obs, q_s)` relate to the log-model-evidence? Is lower surprisal better or worse for the agent?

19. What is the default policy structure when you create `ActiveInferenceAgent(model)` without specifying `policies`? How many policies does a 4-action model produce?

20. After running 10 steps of the perception-action loop, what data can you extract from `agent.history`? List all tracked quantities.
