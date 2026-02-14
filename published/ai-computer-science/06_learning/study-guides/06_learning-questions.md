# Study Questions: Learning

1. Why does Active Inference use Dirichlet distributions to represent uncertainty about the A and B matrices?

2. Write the formula for the expected A-matrix $\mathbb{E}[\mathbf{A}]$ given concentration parameters $\mathbf{p}_A$. What does `expected_A(pA)` compute?

3. If `pA = np.ones((3, 2))` (all concentrations = 1), what is the expected A-matrix? What does this represent in terms of prior beliefs?

4. Explain the update rule for `update_dirichlet_A()`. Which entries of pA increase after observing $o = 0$ with beliefs $q(s) = [0.7, 0.3]$?

5. How does the learning rate $\eta$ affect the pA update? What happens if $\eta = 0$? If $\eta = 10$?

6. Write the complete online learning loop (perception, action, pA update, pB update) for 50 timesteps.

7. After 100 learning updates, how would you measure whether the agent has accurately recovered the true A-matrix?

8. What is `expected_B(pB)` and how is it used after each pB update?

9. Compute `update_dirichlet_B()` by hand for $q(s) = [1, 0]$, $q(s') = [0, 1]$, $a = 0$, $\eta = 1$. Which entry of $\mathbf{p}_B$ changes?

10. What does `dirichlet_entropy(alpha)` measure? Is a low or high Dirichlet entropy desirable for a well-learned model?

11. How does the agent's learned A-matrix affect its state inference? Describe the feedback loop between learning and perception.

12. What is Bayesian Model Reduction and what problem does it solve?

13. When does `bayesian_model_reduction(pA_full, pA_reduced)` return a negative ΔF? What does this mean for model selection?

14. How would you visualize the convergence of pA toward the true A? Which visualization function would you use?

15. Design an experiment with 3 episodes of 50 steps each. Between episodes, reset the environment but keep the accumulated pA. Predict how performance changes across episodes.

16. What is `update_dirichlet_D()` and when would you use it? How does it differ from updating pA?

17. If the true A-matrix changes after 50 steps (non-stationary environment), how would you modify the learning to adapt? Consider the effect of learning rate.

18. What is the relationship between the concentration magnitudes in pA and the agent's confidence in its likelihood model?

19. Use `plot_dirichlet_concentration()` to compare the initial and learned pA. What does the visualization show?

20. Explain why Dirichlet learning is online (incremental) rather than batch. What are the computational advantages?
