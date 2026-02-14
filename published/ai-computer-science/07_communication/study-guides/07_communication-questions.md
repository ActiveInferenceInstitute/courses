# Study Questions: Communication

1. How does a single-agent Active Inference loop extend to a multi-agent setting? What changes and what stays the same?

2. In a signaling game, what is the sender's A-matrix and what is the receiver's A-matrix? Why are they different?

3. Define mutual information $I(X; Y)$ in terms of entropy. What does $I = 0$ mean for communication? What does $I = H(\text{state})$ mean?

4. Write the code to compute mutual information between a signal sequence and a state sequence using `mutual_information()`.

5. In the signaling game, what is the C-vector for the sender? For the receiver? Why do they share the same reward structure?

6. How does the receiver learn which signal corresponds to which world state? What Dirichlet update is involved?

7. If the sender always produces signal 0 regardless of the world state, what is the mutual information? Why is this suboptimal?

8. How would you construct a joint distribution matrix from observed (signal, state) pairs for MI computation?

9. What role does the B-matrix play in a multi-agent simulation? Does each agent need its own B, or can they share?

10. Explain the difference between "hardcoded communication" (pre-programmed signals) and "emergent communication" in Active Inference.

11. How would you add a third agent (eavesdropper) to the signaling game? What would its A-matrix look like?

12. What happens to mutual information if you run the signaling game without learning (fixed pA, pB)? Why?

13. Design a 3-signal, 3-state signaling game. Define the sender and receiver A-matrices and C-vectors.

14. How does the sender's precision γ affect the quality of communication? What if γ is very low?

15. Write code for a multi-agent loop where two agents alternate between sending and receiving over 50 steps.

16. What is "theory of mind" in computational terms? How could an agent model another agent's beliefs within its own generative model?

17. If agents have different C-vectors (conflicting preferences), communication may not emerge. Explain why using the EFE framework.

18. How would you use `plot_learning_progress()` in a multi-agent context to show both agents' learning curves?

19. What is the maximum mutual information between signal and state for a 2-state system? When is this achieved?

20. Describe a scenario where communication emerges not through explicit signals but through action observation — agents inferring intentions from behavior.
