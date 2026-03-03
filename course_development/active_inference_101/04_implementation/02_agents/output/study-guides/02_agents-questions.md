# Implementation — Module 02: Agents — Study Questions

1. What are the main components of the ActiveInferenceAgent class?
2. What does the `__init__` method set up? Why does it copy D?
3. How does `infer_states` implement the Bayesian update?
4. Why is normalization needed after the likelihood × prior multiplication?
5. What does `_generate_policies` produce for a single-step agent?
6. How does `infer_policies` evaluate all policies? What does it return?
7. Explain each line of the `_compute_efe` method.
8. What is the role of `self.gamma` in policy selection?
9. Why does `select_action` use np.random.choice with probabilities?
10. What does the SimpleEnvironment class represent?
11. How does `env.step(action)` work? What are the two random events?
12. Why is the simulation loop called a "perception-action loop"?
13. What logging does the agent maintain? Why is this useful?
14. What would happen if the agent's A matrix differed from the environment's true A?
15. How would you extend this to multi-step policies?
16. What is the role of `eps=1e-16` in the EFE computation?
17. How does this code relate to the mathematical equations from the Math Frameworks unit?
18. What happens if gamma = 0? What about gamma = 100?
19. How would you test that the agent is working correctly?
20. What improvements would you make to this basic implementation?
