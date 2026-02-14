# Lab: Dynamic Causal Modelling and Model Inversion

> **Learning Goal:** Design, specify, and analyze DCM studies for neuroimaging data.

## Part 1: Model Specification

**Exercise**: Design a DCM for a visual attention study with 3 regions: V1 (primary visual cortex), V5 (motion area), and PFC (prefrontal cortex — attentional control).

Hypothesis: Attention modulates the connection from V1 to V5.

Specify the matrices:

**A matrix** (intrinsic connectivity):

```
        V1   V5   PFC
V1    [  -    0    0  ]
V5    [  1    -    1  ]
PFC   [  0    0    -  ]
```

(V1 drives V5; PFC drives V5; self-connections on diagonal)

**B matrix** (attention modulation):

```
        V1   V5   PFC
V1    [  0    0    0  ]
V5    [  1    0    0  ]    ← attention modulates V1→V5
PFC   [  0    0    0  ]
```

**C matrix** (driving input — visual stimulus enters V1):

```
V1    [  1  ]
V5    [  0  ]
PFC   [  0  ]
```

Now design a competing model where attention modulates PFC→V5 instead. Write both B matrices and explain what each model predicts differently.

{fill:textarea}

## Part 2: Model Inversion Walkthrough

> **Learning Goal:** Understand the variational Laplace algorithm.

**Exercise**: Trace through the variational Laplace algorithm for a simplified version:

1. **Initialize**: Set q(θ) = N(μ₀, Σ₀) with prior values
2. **E-step**: Compute expected log-likelihood E_q[ln p(y | θ)]
3. **Gradient**: Compute ∂F/∂μ and ∂²F/∂μ²
4. **Update**: μ_new = μ_old - (∂²F/∂μ²)⁻¹ · ∂F/∂μ (Newton step)
5. **Covariance update**: Σ_new = -( ∂²F/∂μ²)⁻¹
6. **Convergence check**: Has F changed less than threshold? If not, return to step 2

For a model with one parameter θ (a single connection strength), with:

- Prior: p(θ) = N(0, 1)
- Likelihood: p(y | θ) = N(θ, 0.5)
- Observed y = 2

Compute the analytical posterior p(θ | y) and verify it matches the VL estimate.

{fill:textarea}

## Part 3: Model Comparison Exercise

> **Learning Goal:** Compare competing DCM models using Bayesian Model Selection.

**Exercise**: After inverting 4 models of a language network, you obtain these free energies:

| Model | Connectivity Hypothesis | Free Energy (F) | Relative F |
|-------|------------------------|-----------------|-----------|
| M1 | Broca → Wernicke, feedforward only | -1250.3 | 0 (reference) |
| M2 | Broca ↔ Wernicke, reciprocal | -1242.1 | +8.2 |
| M3 | Wernicke → Broca, feedforward only | -1255.7 | -5.4 |
| M4 | Broca ↔ Wernicke + STS mediation | -1238.5 | +11.8 |

1. Which model wins? (M4 — lowest F, highest evidence)
2. Compute Bayes factors: BF₄₁ = exp(11.8) ≈ 133,000 — very strong evidence
3. Does model M4's added complexity (STS involvement) pay for itself? Yes — the BF is decisive.
4. What would you conclude about the language network?

{fill:textarea}

## Part 4: Study Design

> **Learning Goal:** Design a complete DCM study from hypothesis to interpretation.

**Exercise**: Design a DCM study investigating how medication (e.g., an SSRI) changes effective connectivity in a depression network:

1. **Hypothesis**: SSRIs restore PFC→amygdala inhibition (top-down control)
2. **Participants**: 30 patients scanned before and after 8 weeks of SSRI treatment + 30 controls
3. **Task** (for task-based DCM) or **Resting state** (for spectral DCM): Specify and justify
4. **Regions**: PFC (dlPFC), amygdala, ACC, insula — justify inclusion
5. **Models**: Specify at least 3 competing models with different hypothesized connectivity changes
6. **Analysis plan**: Individual DCM → PEB group analysis → BMS → parameter inference
7. **Expected results**: If hypothesis is correct, B matrix for "medication" should show strengthened PFC→amygdala

{fill:textarea}

## Part 5: Reflection

In 300 words, reflect: DCM is powerful but has significant limitations — it requires strong prior hypotheses about regions and connections, it is sensitive to ROI placement, and results can depend on the model space. How should researchers handle these limitations? Is DCM confirmatory (testing pre-specified hypotheses) or exploratory (discovering unexpected connectivity)?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Model specification | A, B, C matrices |
| 2 | Algorithm understanding | Variational Laplace |
| 3 | Model comparison | Bayesian Model Selection |
| 4 | Study design | Complete DCM research workflow |
| 5 | Critical evaluation | DCM limitations and best practices |
