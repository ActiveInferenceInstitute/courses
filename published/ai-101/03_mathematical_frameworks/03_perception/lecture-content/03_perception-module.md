# Module 03: Perception — Free Energy Minimization

> **Course**: Active Inference 101 | **Unit**: Mathematical Frameworks | **Audience**: First-semester undergraduates

## Learning Objectives

1. Derive free energy minimization as the mathematical basis of **perceptual inference**.
2. Show how **prediction error minimization** emerges from the free energy objective.
3. Connect the math to **precision weighting** and attention.

## Introduction

Modules 01-02 established probability, generative models, and variational inference. Now we apply these tools to perception: how does the brain infer what's out there? The answer: by minimizing variational free energy.

## Key Concepts

### 1. Free Energy Recap

Variational free energy is:

**F = E_q[log q(s) - log P(o, s)]**

This can be decomposed as:
**F = D_KL[q(s) || P(s)] - E_q[log P(o | s)]**
**F = Complexity - Accuracy**

Minimizing F means finding beliefs q(s) that explain observations well (high accuracy) while staying close to prior expectations (low complexity).

### 2. Gradient Descent on Free Energy

What does "minimizing F" look like in practice? **Gradient descent**:

1. Start with current beliefs q(s) = q₀(s) (the prior)
2. Observe data o
3. Compute the gradient: ∂F/∂q — which direction to adjust beliefs?
4. Update beliefs: q → q - η × ∂F/∂q (where η is the learning rate)
5. Repeat until F stops decreasing

Each step reduces F by adjusting beliefs toward the posterior. This is the mathematical description of "belief updating."

### 3. Prediction Error Minimization

For a Gaussian generative model, minimizing F reduces to minimizing **precision-weighted prediction error**:

**F ∝ ½ π(o - g(s))²**

Where:

- **o**: The observation
- **g(s)**: The predicted observation (generated from beliefs about state s)
- **π**: The precision (inverse variance) — how reliable the observation is
- **(o - g(s))**: The prediction error — mismatch between predicted and actual

This is the mathematical version of predictive coding from the Computational Neuroscience unit!

### 4. Precision as a Weight

Precision π determines how much a prediction error matters:

- **High precision (π large)**: This sensory channel is reliable → errors are weighted heavily → beliefs update strongly
- **Low precision (π small)**: This channel is unreliable → errors are down-weighted → beliefs change little

**Mathematical attention**: Minimizing F with respect to precision is equivalent to optimizing the gain on sensory channels — exactly what attention does.

### 5. Hierarchical Free Energy

In a hierarchical model with multiple levels, each level minimizes its own free energy:

- Level 1: Minimizes F₁ by predicting raw sensory data
- Level 2: Minimizes F₂ by predicting Level 1's activity
- Level 3: Minimizes F₃ by predicting Level 2's activity

Total free energy: **F = F₁ + F₂ + F₃ + ...**

Each level passes prediction errors upward and predictions downward — this is the mathematical formulation of the canonical microcircuit from Computational Neuroscience Module 03.

## Summary

Perception is free energy minimization. For Gaussian models, this reduces to precision-weighted prediction error minimization. Precision controls how much each error contributes, implementing attention. In hierarchical models, free energy is minimized at each level, with predictions flowing down and errors flowing up — the mathematical basis of predictive coding.

## Further Reading

- Friston, K. J. (2005). A theory of cortical responses. *Phil. Trans. R. Soc. B*, 360(1456), 815-836.
- Bogacz, R. (2017). A tutorial on the free-energy framework for modelling perception and learning. *Journal of Mathematical Psychology*, 76, 198-211.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*. MIT Press. (Chapter 4)
