# Study Questions: Perception

1. Write the VFE formula in terms of complexity and accuracy. Which term encourages the posterior to stay close to the prior, and which encourages it to explain the observation?

2. In `run_state_inference()`, what does the `convergence_threshold` parameter control? What happens if you set it to 0?

3. If the prior is $q(s) = [0.5, 0.5]$ and the A-matrix is the identity, what is the posterior after observing $o = 0$?

4. Explain why `result["delta_history"]` generally decreases over iterations. Under what conditions might it not decrease monotonically?

5. What is `model.log_likelihood(obs)` and how is it used during state inference? Write the formula.

6. If the A-matrix has uniform columns ($A[:, s] = 1/N_o$ for all $s$), what happens to beliefs after state inference? Why?

7. Write code that runs state inference for 3 sequential observations $[0, 0, 1]$, updating the prior with the posterior from each step.

8. How does `agent.infer_states(obs)` differ from calling `run_state_inference()` directly? What additional bookkeeping does the agent method perform?

9. Compute the prediction error $\varepsilon$ by hand for a 2-state system where $q(s) = [0.8, 0.2]$, $A = [[0.9, 0.1], [0.1, 0.9]]$, and the observation is $o = 0$.

10. What does `agent.prediction_error(obs).sum()` return, and why? Prove it algebraically.

11. How would you detect that an observation is "surprising" to an agent from the `run_state_inference()` result? Name two quantitative indicators.

12. Compare the posterior after observing $o = 0$ with a clear A-matrix ($A = [[0.95, 0.05], [0.05, 0.95]]$) versus a noisy one ($A = [[0.6, 0.4], [0.4, 0.6]]$). Which produces a more peaked posterior?

13. What is the maximum number of iterations `run_state_inference()` will perform by default? What happens if convergence is not reached?

14. How does the prior $q(s)$ influence the posterior when the observation is weakly informative? Give a concrete numerical example.

15. Write code to visualize the convergence of state inference using `plot_convergence()` and interpret the resulting plot.

16. Explain the connection between `model.surprisal(obs, q_s)` and VFE. How are they related mathematically?

17. If an agent receives the same observation 10 times in a row, describe qualitatively how $q(s)$ evolves. Does it converge, and to what?

18. What is the shape of `agent.get_predicted_observation()` and what does it represent? How is it computed from $q(s)$ and $A$?

19. In a 3-state system, state inference with $o = 1$ and a uniform prior yields $q(s) = [0.1, 0.8, 0.1]$. What can you infer about the second column of A?

20. Design a scenario where the agent's A-matrix significantly mismatches the environment's true A-matrix. What happens to the agent's beliefs over time? How would you detect this misspecification?
