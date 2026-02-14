# Module 07: Communication — Multi-Agent Active Inference

> **Course**: Active Inference 101 | **Unit**: Mathematical Frameworks | **Audience**: First-semester undergraduates

## Learning Objectives

1. Formalize communication as **coupled inference** between multiple agents with shared generative models.
2. Define **generalized synchrony** mathematically — when agents' beliefs converge.
3. Introduce the mathematics of **shared narratives** and cultural norms as shared priors.

## Introduction

Everything so far has described a single agent. But communication involves *multiple* agents whose models interact. This module formalizes multi-agent Active Inference.

## Key Concepts

### 1. Two Agents, Two Generative Models

Each agent i has its own generative model: P_i(o, s) = P_i(o | s) × P_i(s)

In communication, one agent's actions become another agent's observations:

- Agent A's speech → Agent B's auditory observations
- Agent B's facial expression → Agent A's visual observations

Mathematically: **o_B = f(a_A)** — Agent B's observations are a function of Agent A's actions.

### 2. Coupled Free Energy Minimization

When agents communicate, they jointly minimize a coupled free energy:

**F_total = F_A + F_B + F_coupling**

The coupling term ensures both agents' models converge — they form **shared beliefs**. This happens because:

- Agent A generates predictions about what Agent B believes
- Agent B generates predictions about what Agent A believes
- Both minimize their respective free energies, which includes modeling the other agent

### 3. Generalized Synchrony

**Generalized synchrony** occurs when two agents' internal states become statistically dependent:

**I(s_A; s_B) > 0** (mutual information between internal states is positive)

This is the mathematical definition of "being on the same page." In successful communication:

- Agent A's beliefs about hidden state s converge with Agent B's beliefs
- The prediction error between agents' models approaches zero
- Both agents' posteriors become aligned

### 4. Language as Compressed Generative Models

Language can be formalized as an efficient encoding of generative models:

- **Words** are compressed representations of hidden states or observation categories
- **Grammar** encodes the transition structure (B matrix) — how states relate temporally
- **Pragmatics** encodes shared preferences (C vector) — what matters in context

A sentence like "The cat sat on the mat" transmits:

- State information (cat, mat)
- Relational structure (sat on)
- The speaker's generative model compressed into a few words

### 5. Cultural Norms as Shared Priors

Cultural norms are **shared D vectors** — common priors that a population of agents agrees on:

- "Shake hands when greeting" = shared prior about appropriate action in greeting contexts
- "Stop at red lights" = shared prior about traffic behavior

These shared priors reduce the mutual free energy of social interaction — when everyone expects the same things, prediction errors are minimized.

## Summary

Communication is coupled inference between agents whose actions are each other's observations. Generalized synchrony measures the alignment of beliefs. Language compresses generative models for efficient transmission, and cultural norms are shared priors that minimize collective prediction error.

## Further Reading

- Friston, K. J. & Frith, C. D. (2015). A duet for one. *Consciousness and Cognition*, 36, 390-405.
- Vasil, J. et al. (2020). A world unto itself: Human communication as active inference. *Frontiers in Psychology*, 11, 417.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*. MIT Press. (Chapter 9)
