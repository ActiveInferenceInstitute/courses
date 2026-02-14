# Study Questions: Planning

1. What is a multi-step policy and how does it differ from the single-step policies used in earlier modules?

2. Write the formula for total EFE of a multi-step policy $\pi = [a_0, a_1, \ldots, a_{T-1}]$.

3. How does the agent predict future state distributions? Write the recursive formula using the B-matrix.

4. What is Marginal Message Passing (MMP) and why is it needed for deep temporal models?

5. In `run_mmp()`, what does the `beliefs` return value contain? How many belief vectors are returned for a 3-step policy?

6. Explain the computational tradeoff of increasing temporal depth T. How does the number of possible policies scale with T?

7. For a 4-action system with T = 3, how many exhaustive policies exist? How could you reduce this number?

8. Write code to define multi-step policies for a T-maze agent that can plan 2 steps ahead (first go to cue, then go to arm).

9. Why does the T-maze require T ≥ 2 for the agent to reliably find the reward? What fails with T = 1?

10. How would you encode a 3×3 gridworld as a `DiscreteEnvironment`? What shape would the B-tensor have?

11. How are obstacles (walls) represented in the B-matrix of a gridworld? What transition does a wall create?

12. What does `plot_gridworld()` visualize? What arguments does it accept?

13. Write the full code for evaluating a multi-step policy's total EFE by unrolling predicted states across all timesteps.

14. How does MMP differ from simple forward inference? What additional information does backward message passing provide?

15. In a gridworld with a distant reward (10 steps away), what minimum temporal depth T is needed? What practical problem arises?

16. How does `plot_simulation_dashboard()` organize its 5 panels? What is shown in each panel?

17. Explain how hierarchical planning could reduce the policy space. What are "abstract policies" in this context?

18. Compare a T = 1 agent and a T = 5 agent on the same gridworld. What differences in behavior would you expect?

19. What is the relationship between planning depth T and the exploration–exploitation tradeoff? Does deeper planning favor exploitation?

20. Design a delayed-reward task where a T = 1 agent fails but a T = 3 agent succeeds. Specify the states, observations, actions, C-vector, and the necessary policy structures.
