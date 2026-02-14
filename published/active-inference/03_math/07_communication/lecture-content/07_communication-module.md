# Module 07: Communication — Coupled Inference, Shared Generative Models, and Multi-Agent Free Energy

## Learning Objectives

1. Formalize communication as **coupled inference**: two agents mutually predicting each other's behavior.
2. Derive the **multi-agent free energy** and show how it decomposes into individual and interaction terms.
3. Develop the mathematics of **generalized synchrony** between coupled dynamical systems.

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

## Derivation Exercises

1. For two coupled Gaussian agents, derive the joint free energy F_joint and show how it separates into individual and interaction terms.
2. Derive the condition for generalized synchrony: when does the synchronization manifold become an attractor?
3. Show that communication minimizes joint free energy by aligning the agents' generative models.

## Conclusion

Communication is coupled inference — two agents minimizing their joint free energy through reciprocal prediction. The mathematics of generalized synchrony provides the formal framework for understanding how mutual understanding emerges from the dynamics of interacting generative models. Module 08 completes the mathematical framework with planning and sophisticated inference.
