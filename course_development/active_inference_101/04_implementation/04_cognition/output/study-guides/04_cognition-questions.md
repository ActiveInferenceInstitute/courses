# Implementation — Module 04: Cognition — Study Questions

1. What is the T-Maze and why is it the canonical Active Inference benchmark?
2. How many hidden states does the T-Maze have? What do they represent?
3. Why does the T-Maze have 3 observation modalities? What is each?
4. What is the structure of the A matrix for location observations?
5. How does cue reliability affect the A_cue matrix?
6. How does the reward A matrix encode reward contingencies?
7. What do the 4 actions in the T-Maze represent?
8. How does the B matrix encode movement between locations?
9. Why does the reward condition stay constant across transitions?
10. What does the C vector encode? Why are there no location preferences?
11. What does the D vector represent in the T-Maze?
12. What is the expected behavior of a well-performing agent? (cue first, then reward arm)
13. Why does the agent visit the cue location first? What drives this behavior?
14. How does EFE decomposition explain the cue-seeking behavior?
15. What happens if cue reliability is 0.5 (useless cue)?
16. What happens if C_reward = [0, 0, 0] (no reward preferences)?
17. How would you extend the T-Maze to test multi-step planning?
18. What is the difference between this implementation and the pymdp T-Maze?
19. How does the T-Maze demonstrate the exploration-exploitation balance?
20. What other benchmarks could test Active Inference agents?
