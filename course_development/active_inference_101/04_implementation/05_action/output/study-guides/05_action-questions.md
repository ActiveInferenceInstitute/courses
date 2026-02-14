# Implementation — Module 05: Action — Study Questions

1. How does `generate_policies` create multi-step policies? What is its computational complexity?
2. How many policies are generated for 3 actions and 3 time steps?
3. Explain each step of the `compute_efe_decomposed` function.
4. What does the pragmatic term compute? What inputs does it need?
5. What does the epistemic term compute? Why does it involve mutual information?
6. How does softmax convert EFE values into policy probabilities?
7. What role does gamma play in action selection?
8. Walk through the `active_inference_loop` step by step for one time step.
9. Why is belief transition (`qs = B @ qs`) done after action execution?
10. What does the log dictionary record? Why is each entry useful?
11. How does policy length affect the quality of decisions?
12. What is the computational cost of evaluating all policies? When does this become prohibitive?
13. How could you reduce computation for large action/time spaces?
14. What happens if pragmatic value and epistemic value conflict?
15. How does this code relate to the math in the Mathematical Frameworks unit?
16. What is the difference between `select_action` returning the first action vs. the full policy?
17. How would you visualize the EFE decomposition to understand agent behavior?
18. What tests would you write to validate the EFE computation?
19. How does the agent handle a change in preferences (C vector) mid-simulation?
20. Compare this implementation to how pymdp handles action selection.
