# Practice Quiz: Communication

## Part A: Multiple Choice

1. In the coupled inference framework, agent A models agent B's states as:
A) Known constants
B) Hidden causes within A's generative model that must be inferred
C) Irrelevant noise
D) Exact copies of A's own states

2. The joint free energy F_joint decomposes into:
A) Only individual free energies
B) Sum of individual free energies minus mutual information between agents
C) The product of individual free energies
D) Only the mutual information term

3. Generalized synchrony between two systems means:
A) The systems oscillate at the same frequency
B) There exists a smooth functional relationship between the states of the two systems
C) The systems are physically connected
D) The systems have identical parameters

4. The coupling strength κ must exceed what threshold for synchronization to be stable?
A) Zero
B) Half the maximum Lyapunov exponent of the uncoupled system: κ > λ_max/2
C) The number of state variables
D) The mutual information

5. Theory of Mind in Active Inference is modeled as:
A) A single-level inference about behavior
B) Hierarchical generative modeling — A models B's model, and potentially B's model of A
C) Direct mind-to-mind communication
D) Emotional resonance without inference

6. Communication success in the multi-agent framework corresponds to:
A) Maximum individual free energy
B) High mutual information between agents — aligned generative models
C) Zero coupling
D) Maximum entropy

7. Deception in Active Inference terms involves:
A) Not communicating at all
B) Acting to create specific prediction errors in the other agent's model (manipulating their beliefs)
C) Random behavior
D) Copying the other agent's actions exactly

## Part B: Short Answer

1. For two coupled linear systems dx₁/dt = -x₁ + κ(x₂ - x₁) and dx₂/dt = -x₂ + κ(x₁ - x₂), derive the error dynamics and find the critical coupling strength for synchronization.
2. Explain why hierarchical Theory of Mind (A models B models A models B...) has diminishing computational returns. What determines the optimal depth?
3. Two agents have misaligned generative models (different priors). Describe mathematically how communication (exchange of prediction errors) can lead to alignment. Under what conditions does alignment fail?
