# Study Questions: Action

1. Write the formula for Expected Free Energy $G(\pi)$ and identify the two component terms.

2. Explain the difference between risk and ambiguity in EFE. Which drives goal-directed behavior and which drives information-seeking?

3. How does `compute_efe(q_s, A, B, C, action)` compute the predicted next-state distribution $q(s' \mid \pi)$?

4. What happens to EFE when the C-vector is all zeros? Which component vanishes and which remains?

5. Write the policy posterior equation $q(\pi)$. What role does the negative sign in front of γ play?

6. Why is softmax used to convert EFE values to policy probabilities instead of simply picking the minimum $G$?

7. Compute $G(\pi)$ by hand for a 2-state system with $q(s) = [1, 0]$, $A = I$, $B_{a=0} = I$, $C = [1, -1]$. Show both risk and ambiguity components.

8. In `run_policy_inference()`, what does the return value `G_values` contain? What is its shape?

9. How does the agent select a specific action from $q(\pi)$? Is it deterministic or stochastic?

10. Explain why an agent in the T-maze visits the cue location before choosing an arm. Which EFE component is responsible?

11. If the A-matrix is the identity (fully observable), what is the ambiguity for every policy? What behavior results?

12. Write code to compute and print the EFE for all 3 actions in a T-maze model, then determine which action has the lowest G.

13. How would you modify the C-vector to create an agent that explores without any particular preference? What would its behavior look like?

14. What is `result["selected_action"]` from `run_policy_inference()`? How is it computed from `q(π)`?

15. If γ is very large, the policy with the lowest $G$ gets nearly all the probability mass. What is the computational danger for multi-step policies?

16. Describe how multi-step policies are evaluated. If a policy is $[a_0, a_1, a_2]$, how does EFE aggregate across the three steps?

17. Use `plot_policy_values()` to visualize EFE over time. What should the plot look like when the agent has fully located the reward?

18. Use `plot_efe_decomposition()` to visualize risk and ambiguity components. When does ambiguity dominate risk in the T-maze?

19. Compare two agents on the T-maze: one with γ = 1 and one with γ = 16. Which one reaches the reward arm more consistently? Which explores more?

20. What is the computational complexity of evaluating $G(\pi)$ for $K$ policies, each of length $T$, in a system with $N_s$ states and $N_o$ observations? How does it scale?
