# Implementation — Module 01: Systems — Study Questions

1. Why is Python the standard language for scientific computing and Active Inference? What specific libraries make it suitable?
2. What does the A matrix represent in a POMDP? Why does each column sum to 1? What would happen if it didn't?
3. What does the B matrix represent? Why is it three-dimensional (states × states × actions)? How do you extract the transition matrix for a specific action?
4. What does the C vector represent? Why is it in log-probability space rather than regular probability space?
5. What does the D vector represent? What is the difference between a uniform D (equal prior) and an informative D (strong prior)? When would each be appropriate?
6. Write a `normalize()` function from scratch. Why is normalization necessary — what happens if you skip it?
7. What is the `log_stable()` function? Why can't you just use `np.log()` directly? What happens if you compute log(0)?
8. Implement the `softmax()` function. Why do you subtract the maximum before exponentiating? What numerical problem does this prevent?
9. What is entropy? Write the formula and compute H(p) for p = [0.5, 0.5] and p = [0.9, 0.1]. What does higher entropy mean about the distribution?
10. What is KL divergence? Compute D_KL(q || p) for q = [0.8, 0.2] and p = [0.5, 0.5]. Is KL divergence symmetric? Why does this matter?
11. Why does column-summing-to-1 matter for the A matrix? What physical constraint does this represent?
12. How does the `GenerativeModel` class encapsulate the POMDP components? Why is object-oriented design useful here?
13. What does the `validate_model()` function check? Design two additional validation checks that would catch common model definition errors.
14. Modify the code to add a 3-state model (3 hidden states, 3 observations, 2 actions). Define sensible A, B, C, D matrices and validate them.
15. Critically evaluate: The P(o|s) observation model assumes the agent KNOWS how states generate observations. Is this realistic? How might an agent learn its A matrix from experience? Sketch pseudocode for learning A.
16. What happens to the agent's behavior if the B matrix (transition model) is wrong — for example, if the agent believes action "left" moves it right? Describe the resulting behavior and how the agent might detect and correct this model mismatch.
17. Implement a simple simulation loop: the agent starts with a uniform belief D, takes an observation, updates its belief using the A matrix and Bayes' rule, selects an action, and transitions. Trace through 5 timesteps and show how beliefs evolve. What patterns do you notice?
18. What is the relationship between the temperature parameter in the softmax function and the explore-exploit trade-off? What happens behaviorally when temperature → 0 (greedy) versus temperature → ∞ (random)? What is a reasonable default and why?
19. How would you extend the basic POMDP implementation to handle multiple observation modalities (e.g., both visual and auditory observations)? What changes to the A matrix structure are needed, and how does inference combine evidence from multiple senses?
20. Design a simple debugging protocol for when an Active Inference agent behaves unexpectedly. What are the three most common bugs in POMDP implementations, and how would you systematically diagnose each one using visualization of beliefs, prediction errors, and policy evaluation?
