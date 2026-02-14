# Section 03: The Mathematics of Active Inference

## Learning Objectives

1. Derive the core equations of Active Inference — including the variational free energy bound, the KL divergence decomposition, and the expected free energy — from first principles using probability theory and information theory.
2. Formalize the dynamics of self-organizing systems using stochastic differential equations, the Langevin equation, and the Fokker-Planck equation.
3. Construct precision-weighted message passing equations for hierarchical generative models and apply Bayesian Model Reduction to compare nested models analytically.
4. Derive the sophisticated inference update equations that support multi-step planning through recursive belief updating and tree search over policies.

## Introduction

Mathematics is the language in which Active Inference achieves its full precision. The philosophical intuitions about boundaries, beliefs, and surprise become exact when expressed as Markov Blanket conditions, posterior distributions, and variational free energy bounds. The neural mechanisms described by cognitive science become quantitative when formulated as precision-weighted prediction errors flowing through a hierarchical generative model. This section develops the complete mathematical foundation.

The section begins with two prerequisite modules covering the mathematical tools required for the rest of the curriculum: matrix operations, probability theory, Bayes' theorem, information theory (entropy, KL divergence, mutual information), graphical models, stochastic processes, the Langevin equation, and the Fokker-Planck equation. From Module 3 onward, we derive the core results of Active Inference step by step, with worked examples at each stage.

## Key Concepts

### 1. The Variational Free Energy Bound

The central mathematical object of Active Inference is the variational free energy F, an upper bound on surprise (negative log-evidence). Its derivation from the KL divergence between the recognition density and the true posterior reveals the fundamental trade-off between complexity (how far beliefs deviate from priors) and accuracy (how well beliefs explain observations). Minimizing F with respect to beliefs yields perception; minimizing F with respect to actions yields behavior.

### 2. Stochastic Dynamics and Nonequilibrium Steady States

Living systems are far-from-equilibrium systems described by stochastic differential equations. The Langevin equation governs their dynamics, and the Fokker-Planck equation describes the evolution of probability density over time. At nonequilibrium steady state, any system with a Markov Blanket partition can be shown to behave as if it is minimizing free energy — connecting the physics of self-organization to the mathematics of inference.

### 3. Expected Free Energy and Policy Selection

The expected free energy G decomposes into two components: pragmatic value (risk — the divergence between predicted and preferred outcomes) and epistemic value (ambiguity resolution — the expected information gain from acting). This decomposition elegantly captures the exploration-exploitation tradeoff: agents choose policies that both approach their goals and reduce their uncertainty.

### 4. Hierarchical Message Passing and Bayesian Model Reduction

In hierarchical generative models, belief updating is implemented through precision-weighted message passing between levels. Bayesian Model Reduction provides an analytical method for comparing nested models without refitting, enabling efficient structure learning. Together, these tools formalize how agents build, maintain, and prune their models of the world.

## Applications

* **Deriving the ELBO**: The Evidence Lower Bound (ELBO) used throughout machine learning is identical to the negative variational free energy. Deriving this equivalence from first principles connects Active Inference to the variational autoencoder (VAE) framework and reveals that modern generative AI and biological inference share the same mathematical foundation.

* **Computing Expected Free Energy for the T-Maze**: The T-maze task provides a concrete worked example where the expected free energy can be computed analytically for each policy. One arm of the maze contains a reward, and a cue indicates which arm. Computing G for the "go to cue" policy versus the "go directly to arm" policy reveals the epistemic value of information seeking — the mathematics of curiosity.

## Conclusion

The Mathematics section provides the formal rigor that transforms Active Inference from a conceptual framework into a precise, falsifiable theory. Every equation derived here has a philosophical interpretation (Section 01), a neural correlate (Section 02), and a computational implementation (Section 04). Students who complete this section will be able to derive the core results of Active Inference from first principles and apply them to novel problems.
