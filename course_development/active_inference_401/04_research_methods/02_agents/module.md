# Module 02: Agents — Computational Phenotyping and Individual Differences

> **Course**: Active Inference 401 | **Unit**: Research Methods | **Audience**: Graduate students / researchers

## Learning Objectives

1. Apply **computational phenotyping** — characterizing individuals by their generative model parameters.
2. Analyze how **parameter recovery** validates computational models.
3. Evaluate using Active Inference parameters as **biomarkers** for clinical conditions.

## Key Concepts

### 1. Computational Phenotyping

Computational phenotyping uses generative models to characterize individual differences not in terms of behavior (reaction times, accuracy) but in terms of the latent computational processes that produce behavior:

**The idea**: Two people may perform a task with identical accuracy but for different computational reasons. Person A might have high sensory precision but a weak prior. Person B might have a strong prior but low sensory precision. Both achieve 80% accuracy, but their computational profiles are different.

**Active Inference parameters as phenotypes**: Each individual's fitted model yields parameter estimates:

- **Precision parameters (ω, γ)**: Sensitivity to prediction errors, confidence in priors
- **Learning rates (α)**: How quickly beliefs update
- **Policy precision (β)**: How decisively actions are selected
- **Prior preferences (C)**: What outcomes are valued

These parameters define a **computational phenotype** — a point in a high-dimensional parameter space that characterizes the individual's inference style.

### 2. Model Fitting to Behavioral Data

Fitting Active Inference models to empirical behavioral data:

**Task design**: Design tasks that dissociate model parameters. Example: A probabilistic reversal learning task where the reward probability switches between options. This dissociates:

- Learning rate: How quickly the agent detects the reversal
- Prior volatility: How much the agent expects change
- Precision: How confident the agent is in its estimates

**Fitting procedure**:

1. Specify the generative model (POMDP or continuous)
2. For each participant, find parameters θ* that maximize p(behavior | θ, model)
3. Use variational Bayes, maximum likelihood, or MCMC
4. Obtain posterior distributions over parameters: p(θ | behavior, model)

**Hierarchical fitting**: Use Parametric Empirical Bayes (PEB) to fit all subjects simultaneously, sharing information across the group. This regularizes individual estimates and provides group-level statistics.

### 3. Parameter Recovery and Validation

Before trusting model-based conclusions, validate the model:

**Parameter recovery**:

1. Choose known "true" parameters θ_true
2. Simulate data from the model with θ_true
3. Fit the model to the simulated data to recover θ_recovered
4. Compare θ_true with θ_recovered

**Good recovery**: Strong correlation between true and recovered parameters, low bias, reasonable confidence intervals.

**Identifiability**: Can the parameters be uniquely determined? Check:

- No two parameter settings produce the same behavior (global identifiability)
- Posterior distributions are narrower than priors (local identifiability from data)
- Parameters are not highly correlated (separability)

**Model comparison on simulated data**: Generate data from Model A, fit both Model A and Model B, and verify that Model A wins. If Model B fits Model-A-generated data equally well, the models are confounded.

### 4. Clinical Applications

Computational phenotyping has transformative potential for psychiatry:

**Transdiagnostic approach**: Instead of clustering patients by DSM categories, cluster them by computational parameters. Two patients with "depression" may have very different computational profiles (one with low precision, another with excessive precision on negative outcomes).

**Treatment matching**: If a patient's computational phenotype indicates pathologically low learning rate, treatments that boost learning (e.g., cognitive remediation) may be more appropriate than pharmacotherapy targeting precision.

**Longitudinal monitoring**: Track computational parameters over time to assess treatment response. A decrease in volatility estimates after medication suggests the drug is stabilizing belief dynamics.

**Normative modeling**: Rather than comparing patients to a single "healthy" distribution, normative modeling maps each individual's deviation from the population distribution in parameter space. This enables personalized anomaly detection.

### 5. Practical Considerations

**Software tools**: SPM (Statistical Parametric Mapping), spm_MDP_VB (for POMDP models), custom MATLAB/Python implementations.

**Sample size**: Computational phenotyping requires sufficient data per individual (hundreds of trials) and sufficient individuals for group comparisons (N > 30 typical).

**Reporting**: Report parameter recovery results, model comparison metrics, posterior parameter distributions, and individual differences in parameters — not just group means.

## Summary

Computational phenotyping characterizes individuals by their Active Inference model parameters rather than raw behavior. Model fitting uses variational Bayes or hierarchical methods. Parameter recovery validates that the model can distinguish different computational profiles. Clinical applications include transdiagnostic classification, treatment matching, and longitudinal monitoring.

## Further Reading

- Adams, R. A. et al. (2016). Computational psychiatry: toward a mathematically informed understanding of mental illness. *JNNP*, 87(1), 53-63.
- Friston, K. J. et al. (2016). Active inference and learning. *Neuroscience & Biobehavioral Reviews*, 68, 862-879.
- Stephan, K. E. et al. (2016). Allostatic self-efficacy: A metacognitive theory of dyshomeostasis-induced fatigue and depression. *Frontiers in Human Neuroscience*, 10, 550.
