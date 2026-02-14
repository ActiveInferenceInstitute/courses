# Practice Quiz: Communication

## Part A: Multiple Choice

1. In a multi-agent Active Inference setting, one agent's actions become:
A) Another agent's hidden states
B) Another agent's observations
C) Another agent's C-vector
D) Another agent's precision

2. In the signaling game, mutual information between signals and world states measures:
A) The reward gained by the receiver
B) How much the sender's signals reduce uncertainty about the world state
C) The entropy of the A-matrix
D) The agent's VFE

3. If the sender always produces signal 0 regardless of the world state, MI is:
A) Maximum
B) $\ln 2$
C) Zero
D) Undefined

4. Communication in Active Inference multi-agent systems is:
A) Pre-programmed via the C-vector
B) Emergent through learning
C) Impossible without a shared B-matrix
D) Only possible with 2 agents

5. The receiver learns the signal-to-state mapping by updating:
A) Its C-vector
B) Its Dirichlet pA concentrations
C) Its precision γ
D) Its D-vector

6. Maximum mutual information between a binary signal and a binary state is:
A) 0
B) 0.5
C) $\ln 2$
D) 1.0

7. A "theory of mind" in computational terms means:
A) The agent has a separate model of its own mental states
B) The agent includes other agents' beliefs as hidden states in its own generative model
C) The agent communicates using language
D) The agent has higher precision than other agents

## Part B: Short Answer

1. Write code to compute the joint distribution of (signal, state) pairs from two lists `signals = [0, 1, 0, 1, 0]` and `states = [0, 1, 1, 1, 0]`, then compute MI.

2. Explain why agents with conflicting C-vectors (one prefers observation 0, the other prefers observation 1) may not develop effective communication. What would the equilibrium behavior look like?

3. Design an extension of the signaling game with 3 world states and 2 available signals. Can the sender communicate the world state perfectly? Why or why not? What is the maximum achievable MI?
