# FAQ: Active Inference 401: Advanced PhD Seminar

> Frequently asked questions for PhD students and researchers.

## What is Active Inference?

Active Inference is a normative framework derived from the Free Energy Principle (Friston, 2010) in which agents — systems possessing a Markov blanket and a particular partition — are modeled as minimizing variational free energy (for perception and learning) and expected free energy (for action and planning). It unifies perception, action, learning, and planning under a single variational objective, formalized through partially observable Markov decision processes (POMDPs) in discrete time and stochastic differential equations in continuous time.

## How does Active Inference differ from reinforcement learning?

Active Inference subsumes reward-maximizing frameworks by replacing the reward function with prior preferences $\mathbf{C}$ encoded in the generative model. Policies are selected by minimizing expected free energy $G(\pi)$, which naturally decomposes into pragmatic value (exploitation — fulfilling preferences) and epistemic value (exploration — reducing uncertainty). This eliminates the need for separate exploration bonuses or epsilon-greedy strategies. See Sajid et al. (2021) for a formal comparison.

## What is the Free Energy Principle?

The FEP is the conjecture that any system that maintains a non-equilibrium steady state (NESS) with a particular partition can be described as minimizing variational free energy. It is a principle about the dynamics of self-organizing systems, not a specific theory of brain function. Active Inference is the application of the FEP to agents. The principle is contested: critics argue it may be unfalsifiable (Colombo & Wright, 2021) or trivially true (Bruineberg et al., 2022); proponents argue it provides a unifying formal language for the life sciences (Ramstead et al., 2018).

## Who is this curriculum for?

PhD students and researchers with strong backgrounds in probability theory, differential geometry, dynamical systems, and at least one domain (neuroscience, philosophy, or computational modeling). See the Prerequisites section in [AGENTS.md](../AGENTS.md) for the full list.

## Why are there four courses on the same 8 topics?

Each course examines the same topics through a different disciplinary lens: philosophical (What does it mean?), neuroscientific (What is the evidence?), mathematical (Can we prove it?), and methodological (How do we test it?). This spiral pedagogy ensures that PhD students develop a multi-perspectival understanding — the kind required for original research that bridges disciplines.

## What are the 8 modules about?

1. **Systems** — Non-equilibrium steady states, random dynamical systems, and the conditions for self-organization
2. **Agents** — The particular partition, Markov blankets, and the formal conditions that distinguish agents from mere systems
3. **Perception** — Generative model inversion, predictive coding, and variational inference as perceptual inference
4. **Cognition** — Variational methods (mean-field, Bethe, message passing), belief updating, and the structure of generative models
5. **Action** — Expected free energy minimization, path integral control, and the action-perception cycle
6. **Learning** — Parameter estimation, structure learning, Bayesian model reduction, and model evidence
7. **Communication** — Multi-agent inference, shared Markov blankets, cultural affordances, and social cognition
8. **Planning** — Temporal depth, sophisticated inference, deep temporal models, and counterfactual reasoning

## What software tools are used?

SPM (MATLAB), PyMDP (Python), RxInfer.jl (Julia), and deep-active-inference (PyTorch). See the Computational Tools section in [AGENTS.md](../AGENTS.md).

## Navigation

- [Glossary](./glossary.md)
- [Learning Pathways](./learning_pathways.md)
- [Home](../README.md)
