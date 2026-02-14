# Mathematical Frameworks — Module 04: Cognition — Study Questions

1. What does POMDP stand for? Why is "partially observable" important?
2. How does a POMDP differ from an HMM?
3. List the five components of the Active Inference POMDP (A, B, C, D, π).
4. What does the A matrix represent? Give an example.
5. What constraint must each column of the A matrix satisfy?
6. What does the B matrix represent? How does it differ for different actions?
7. What does the C vector encode? How does it replace traditional reward functions?
8. What does the D vector represent?
9. Write the belief update equation: q(s_t) ∝ ...
10. What is a policy π in this framework? How is it different from a single action?
11. Walk through one step of the perception-action loop using the five components.
12. Why is it called "partially observable"? What is hidden from the agent?
13. How does the A matrix implement the likelihood P(o | s)?
14. How does the B matrix implement dynamics with agency?
15. Can the C vector change over time? What would that mean?
16. What happens if the A matrix is the identity? What does this imply about observability?
17. What happens if the B matrix is the same for all actions? What is lost?
18. How does the POMDP relate to the generative model from Module 01?
19. Why does the agent need to evaluate multiple policies rather than just pick one?
20. How does the mathematical POMDP formulation connect to the cognitive science concept of "cognition as belief updating" (Unit 1, Module 04)?
