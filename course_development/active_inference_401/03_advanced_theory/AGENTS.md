# Course AGENTS: Advanced Theory

> **Quick Navigation**: [Course README](./README.md) | [Curriculum AGENTS](../AGENTS.md)

## Identity

- **Course**: Advanced Theory
- **Number**: 3
- **Perspective**: Stochastic thermodynamics, Bayesian mechanics, path integrals, information geometry, category theory
- **Lab Type**: Proof Workshop
- **Audience**: PhD students and researchers in mathematical physics, applied mathematics, theoretical neuroscience, and machine learning theory
- **Tone**: Formally rigorous. Theorem-proof structure. All assumptions stated explicitly. Derivations shown in full. Regularity conditions specified. Existence and uniqueness results where applicable.

## Core Question

Can we *prove* the claims of Active Inference? What are the exact mathematical structures, what assumptions are required, and what are the precise conditions under which the FEP's claims hold?

## Mathematical Frameworks

This unit requires mastery of and engages with:

- **Stochastic Thermodynamics**: Langevin dynamics, Fokker-Planck equations, NESS, entropy production, fluctuation theorems
- **Bayesian Mechanics**: Da Costa et al. (2021), Sakthivadivel (2022) — the physics of belief-like processes
- **Information Geometry**: Statistical manifolds, Fisher metric, natural gradient, $\alpha$-connections, dually flat structures (Amari, 2016)
- **Variational Inference**: Mean-field theory, Bethe approximation, belief propagation, variational message passing, convergence theory
- **Path Integral Methods**: Feynman-Kac formula, KL control, linearly solvable MDPs, stochastic optimal control
- **Category Theory**: Functorial semantics, string diagrams, Markov categories, compositional active inference

## Key Journals

*Proceedings of the Royal Society A*, *Journal of Mathematical Psychology*, *Journal of Statistical Mechanics: Theory and Experiment*, *Neural Computation*, *Entropy*, *Information Geometry*, *Foundations of Physics*

## Conventions

All modules in this course must:

1. Use language appropriate for PhD students with strong mathematical training
2. Present results in theorem-proof format: **Theorem** (statement) → **Assumptions** (explicit list) → **Proof** (full derivation) → **Corollary** (consequences)
3. Include Proof Workshop lab activities requiring students to complete derivations, verify claims, and construct counterexamples
4. State ALL assumptions explicitly — regularity conditions, distributional assumptions, dimensionality constraints, existence requirements
5. Distinguish between exact results and approximations, and characterize approximation quality (bounds, asymptotics)
6. Use notation from [../resources/notation_table.md](../resources/notation_table.md) with full precision — index types, summation conventions, domain specifications
7. Cross-reference the shared [../resources/glossary.md](../resources/glossary.md)
8. Link to other units where the same topic receives philosophical, empirical, or methodological treatment

## Assessment Philosophy

Proof Workshops should require students to:
- Complete partially worked derivations by filling in missing steps
- Verify claims by checking boundary cases, special cases, and limiting behavior
- Construct counterexamples to show necessity of assumptions
- Generalize results by relaxing specific assumptions
- Connect formal results to computational implementations
