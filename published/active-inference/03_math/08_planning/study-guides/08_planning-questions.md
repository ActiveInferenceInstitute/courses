# Study Questions: Planning

1. Write the Expected Free Energy G(π) for a multi-step policy. How does each timestep contribute?
2. How does the number of policies scale with the planning horizon T and the number of actions K?
3. What strategies can reduce the combinatorial explosion of policies? (Consider pruning, habit formation.)
4. How are future states predicted under a policy? Write the prediction equation using the B matrix.
5. How are future observations predicted? Write the prediction equation using the A matrix.
6. Define sophisticated inference. How does it extend basic EFE evaluation?
7. How does sophisticated inference incorporate future belief updates into policy evaluation?
8. Why is sophisticated inference considered a form of "meta-cognition" or "thinking about thinking"?
9. What is the computational cost of sophisticated inference? How does the recursion depth affect this?
10. Compare sophisticated inference with Monte Carlo tree search (MCTS). What are the similarities and differences?
11. What is a hierarchical POMDP? How does it differ from a flat POMDP?
12. How do higher levels of the hierarchy set context (prior preferences) for lower levels?
13. What determines the temporal scale of each level in a hierarchical POMDP?
14. Write the total free energy for a two-level hierarchical POMDP.
15. How do top-down and bottom-up messages propagate between levels in the planning hierarchy?
16. What is the relationship between hierarchical POMDPs and options (temporally extended actions) in reinforcement learning?
17. How does the concept of habits (crystallized policies) reduce computational load?
18. What is the mathematical relationship between planning depth and temporal discounting?
19. How does Active Inference planning differ from classical dynamic programming (Bellman equation)?
20. Derive the EFE for a three-step, two-action POMDP with full policy enumeration. How many policies exist?
