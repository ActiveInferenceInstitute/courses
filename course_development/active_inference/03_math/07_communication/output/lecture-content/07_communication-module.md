# Module 07: Communication — Coupled Inference, Shared Generative Models, and Multi-Agent Free Energy

## Learning Objectives

1. Formalize communication as **coupled inference**: two agents mutually predicting each other's behavior.
2. Derive the **multi-agent free energy** and show how it decomposes into individual and interaction terms.
3. Develop the mathematics of **generalized synchrony** between coupled dynamical systems.
4. Connect multi-agent Active Inference to **information-theoretic** measures of communication.

## Introduction

When two Active Inference agents interact, each treats the other as part of its environment — a generative model that must be inferred. Communication arises when both agents are simultaneously inferring each other's hidden states, producing a coupled dynamical system. This module develops the mathematics of multi-agent Active Inference.

## Key Concepts

### 1. Coupled Inference Between Two Agents

Consider agents A and B. Agent A's generative model includes a model of agent B:

**p_A(o_A, s_A, s_B) = p_A(o_A | s_A, s_B) · p_A(s_A) · p_A(s_B)**

Agent A treats B's states s_B as hidden causes of its own observations o_A. Symmetrically, agent B models agent A. Each agent minimizes its own free energy:

**F_A = E_{q_A}[ln q_A(s_A, s_B) - ln p_A(o_A, s_A, s_B)]**
**F_B = E_{q_B}[ln q_B(s_A, s_B) - ln p_B(o_B, s_A, s_B)]**

The coupling arises because A's actions influence B's observations and vice versa, creating a feedback loop.

### 2. Multi-Agent (Joint) Free Energy

For a system of N agents, the **joint free energy** is:

**F_joint = ∑ᵢ F_i - I_mutual**

where F_i is agent i's individual free energy and I_mutual captures the mutual information between agents' states. Joint free energy minimization implies:

1. Each agent minimizes its own free energy (individual inference)
2. The agents' beliefs become mutually consistent (generalized synchrony)

The interaction term measures the degree to which the agents' generative models align — successful communication corresponds to low interaction free energy (high mutual predictability).

### 3. Generalized Synchrony

Two dynamical systems x₁ and x₂ are in **generalized synchrony** if there exists a smooth function h such that:

**x₂(t) = h(x₁(t)) for all t**

For coupled Active Inference agents, generalized synchrony means the agents' internal states (sufficient statistics) become functionally related — each agent's beliefs can be predicted from the other's. This is the mathematical formalization of "mutual understanding."

The synchronization manifold is stabilized when the coupling strength exceeds the Lyapunov exponent of the uncoupled systems — a condition analogous to "paying enough attention to each other."

### 4. Information-Theoretic Communication Measures

Communication between Active Inference agents can be quantified using information-theoretic measures:

- **Mutual information**: I(s_A; s_B | o) measures how much knowing one agent's states tells us about the other's states, given the shared observations. Successful communication maximizes this quantity.
- **Transfer entropy**: TE(A→B) = H(s_B_future | s_B_past) - H(s_B_future | s_B_past, s_A_past) measures the directed flow of information from A to B — how much A's past states reduce uncertainty about B's future states.
- **Channel capacity**: The maximum rate at which agents can communicate is bounded by the mutual information between their action and observation channels: C = max I(a_A; o_B), where the maximum is over the distribution of A's actions.

### 5. Worked Example: Two Coupled Gaussian Agents

Consider two agents with scalar states and linear coupling:

**Agent A**: ds_A/dt = -κ_A · s_A + c_AB · s_B + ξ_A (where ξ_A ~ N(0, σ_A²))
**Agent B**: ds_B/dt = -κ_B · s_B + c_BA · s_A + ξ_B (where ξ_B ~ N(0, σ_B²))

The joint free energy under mean-field approximation:

**F_joint = ½π_A · (o_A - μ_A)² + ½π_B · (o_B - μ_B)² + ½λ_A · (μ_A - c_AB · μ_B)² + ½λ_B · (μ_B - c_BA · μ_A)² + ...**

At steady state, the belief updates satisfy:

**μ_A* = (π_A · o_A + λ_A · c_AB · μ_B) / (π_A + λ_A)**
**μ_B* = (π_B · o_B + λ_B · c_BA · μ_A) / (π_B + λ_B)**

Each agent's belief is a precision-weighted combination of its own sensory evidence and its prediction of the other agent. The coupling precisions λ_A and λ_B control "how much each agent listens to the other."

### 6. Scaling to Multi-Agent Systems

For N > 2 agents, the mathematics generalizes through **mean field factorization**:

**q(s₁, ..., s_N) ≈ ∏ᵢ q_i(sᵢ)**

Each agent infers only its own states and a summary of the population. This yields tractable inference even in large groups and connects to **collective behavior**: flocking, herding, and social norms emerge as attracting solutions of coupled free energy minimization (Friston & Frith, 2015).

## Derivation Exercises

1. For two coupled Gaussian agents, derive the joint free energy F_joint and show how it separates into individual and interaction terms.
2. Derive the condition for generalized synchrony: when does the synchronization manifold become an attractor?
3. Show that communication minimizes joint free energy by aligning the agents' generative models.
4. Compute the transfer entropy TE(A→B) for the two coupled linear-Gaussian agents and show it depends on the coupling strength c_BA.

## Conclusion

Communication is coupled inference — two agents minimizing their joint free energy through reciprocal prediction. The mathematics of generalized synchrony and information theory provides the formal framework for understanding how mutual understanding emerges from the dynamics of interacting generative models. Module 08 completes the mathematical framework with planning and sophisticated inference.

## Further Reading

- Friston, K. & Frith, C. (2015). A duet for one. *Consciousness and Cognition*, 36, 390-405.
- Schreiber, T. (2000). Measuring information transfer. *Physical Review Letters*, 85(2), 461.
- Vasil, J. et al. (2020). A world unto itself: Human communication as active inference. *Frontiers in Psychology*, 11, 417.
