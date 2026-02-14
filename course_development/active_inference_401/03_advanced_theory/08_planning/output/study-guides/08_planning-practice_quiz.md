# Practice Quiz: Planning / Grand Unification (Advanced Theory)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** Active Inference unifies perception, action, learning, and planning because:
A) They are unrelated processes
B) All four are aspects of variational free energy minimization operating on different variables at different timescales
C) They are all reward-based
D) They are all deterministic

**2.** Active Inference subsumes PID control because:
A) PID is more general
B) The proportional, integral, and derivative terms correspond to prediction error, accumulated PE (learning), and PE rate of change (hierarchical prediction) — which emerge as special cases of free energy minimization
C) PID and Active Inference are unrelated
D) PID handles uncertainty better

**3.** The key advantage of Active Inference over Reinforcement Learning for exploration is:
A) Active Inference avoids exploration
B) Epistemic value (information gain) is built into the expected free energy — exploration emerges naturally without ad-hoc bonuses
C) Active Inference uses more data
D) Active Inference is simpler

**4.** The formal analogy between Helmholtz free energy and variational free energy shows:
A) They are coincidental
B) Both balance energy against entropy — F = U - TS in thermodynamics, F = Energy - Entropy in Active Inference
C) Only one is real
D) Temperature is irrelevant

**5.** The second law analogue in Active Inference is:
A) Free energy always increases
B) An agent's free energy cannot systematically increase over time — dynamics are approximately gradient descent on F
C) Entropy must decrease
D) Information is always lost

**6.** The biggest open problem for Active Inference is arguably:
A) It's well-understood
B) Scalability and falsifiability — can the framework handle brain-scale systems, and can it be empirically tested in a way that could fail?
C) It's too simple
D) It conflicts with physics

**7.** Rate-distortion theory connects to Active Inference by:
A) Being unrelated
B) The complexity cost D_KL[q || p] measures the "rate" — how many bits the posterior uses beyond the prior — formalizing information processing costs
C) Distortion maximization
D) Rate always equals zero

## Part B: Capstone Essay Questions

**1.** Write a comprehensive comparison of Active Inference and deep reinforcement learning for a complex task (autonomous driving, robotic manipulation, or game playing). Address: (a) how each handles state estimation, (b) exploration-exploitation, (c) model learning, (d) safety constraints, (e) multi-agent scenarios. Which approach is more promising, and under what conditions? (600 words)

**2.** Write a critical appraisal of the Free Energy Principle's claim to be a universal theory of adaptive systems. Consider: (a) What does "universal" mean? (b) How does this compare to other universal principles (e.g., conservation of energy, principle of least action, natural selection)? (c) What is the relationship between mathematical generality and explanatory power? (d) Is the FEP more like a law, a principle, a framework, a language, or a tautology? Defend your position. (500 words)

**3.** **Track capstone**: Synthesize the entire Advanced Theory track. For each module (01-08), state the key mathematical tool introduced, how it contributes to the overall framework, and what it explains that no other module explains. Then identify the three most important open questions that the framework, as currently developed, cannot answer. Propose a research program to address one of them. (600 words)
