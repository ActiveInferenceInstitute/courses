# Lab: Derivation Exercise — Coupled Inference and Multi-Agent Free Energy

## Objective

Derive the mathematics of communication between Active Inference agents, from coupled generative models to generalized synchrony conditions.

## Part 1: Two-Agent Generative Models

**Goal**: Formalize how two agents model each other.

**Setup**: Agent A and Agent B, each with 2 states. Agent A's generative model:

- p_A(o_A | s_A, s_B) — likelihood depends on both agents' states
- p_A(s_A) = N(s_A; 0, 1) — prior over own states
- p_A(s_B) = N(s_B; 0, σ²_B) — prior over B's states (higher uncertainty)

Agent B's generative model is symmetric.

**Task**:

1. Write A's free energy F_A as a function of q_A(s_A) and q_A(s_B)
2. Derive the update equations for A's beliefs about s_A and s_B
3. Show that A's beliefs about B depend on A's observations (which are influenced by B's actions)


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Joint Free Energy Decomposition

**Goal**: Derive the relationship between individual and joint free energy.

**Task**:

1. Write the joint free energy: F_joint = F_A + F_B - I(s_A; s_B)
2. Show that the mutual information I(s_A; s_B) = E[ln q(s_A, s_B) / (q(s_A)q(s_B))] captures the coupling
3. Explain why minimizing F_joint simultaneously minimizes individual free energies and maximizes mutual predictability
4. Interpret: when I(s_A; s_B) is high, the agents are in tight communication; when it is low, they are operating independently


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Generalized Synchrony Conditions

**Goal**: Derive the conditions for synchronization.

**Setup**: Two coupled dynamical systems:

- dx₁/dt = f₁(x₁) + κ · (x₂ - x₁)
- dx₂/dt = f₂(x₂) + κ · (x₁ - x₂)

where κ is the coupling strength.

**Task**:

1. Define the synchronization error e = x₁ - x₂
2. Derive the dynamics of e: de/dt = f₁(x₁) - f₂(x₂) - 2κ · e
3. Show that for identical systems (f₁ = f₂ = f), e → 0 is stable if κ > λ_max/2, where λ_max is the maximum Lyapunov exponent of f
4. Interpret: coupling must be strong enough relative to the internal dynamics for synchronization to occur


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Theory of Mind as Hierarchical Modeling

**Goal**: Formalize Theory of Mind mathematically.

**Setup**: Agent A's hierarchical model:

- Level 1: p_A(o_A | s_A) — how A's states generate A's observations
- Level 2: p_A(s_A | s_B model) — how B's model of the world influences A's states
- Level 3: p_A(s_B model | s_B meta-model) — A's model of B's model of A

**Task**:

1. Write the free energy for this three-level hierarchy
2. Show how increasing hierarchical depth enables more sophisticated social inference
3. Compute the additional cost (complexity) of each added level
4. Discuss: what is the optimal depth of Theory of Mind modeling?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Synthesis

In 200 words, explain how the mathematics of coupled inference, joint free energy, and generalized synchrony provide a unified account of communication — from simple biological coordination to human language.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Lab Summary

| Part | Skill Developed | Mathematical Result |
|------|----------------|-------------------|
| 1 | Multi-agent modeling | Two-agent free energy formulation |
| 2 | Information theory | Joint free energy decomposition |
| 3 | Dynamical systems | Synchronization stability conditions |
| 4 | Hierarchical modeling | Theory of Mind as recursive generative models |
| 5 | Conceptual integration | Connecting mathematical communication to natural language |
