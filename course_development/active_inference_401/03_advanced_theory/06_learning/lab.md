# Lab: Bayesian Model Selection and Structure Learning

> **Learning Goal:** Apply BMS, BMR, and structure learning to model comparison and discovery problems.

## Part 1: Model Comparison

**Exercise**: Compare three models of a simple perceptual task (detecting a light flash):

| Model | Description | Parameters | Expected Fit | Expected Complexity |
|-------|-------------|-----------|-------------|-------------------|
| m₁: No detection | Light has no effect | 1 (baseline response) | Poor (ignores signal) | Low (1 param) |
| m₂: Linear detection | Response scales linearly with intensity | 2 (baseline + slope) | Moderate | Moderate |
| m₃: Nonlinear detection | Response follows a sigmoid with threshold | 4 (baseline, gain, threshold, steepness) | Best fit | High (4 params) |

1. Which model has the best fit to data? (m₃)
2. Which has the lowest complexity? (m₁)
3. Which would BMS select? It depends on the data — if the data clearly shows nonlinearity, m₃ wins despite higher complexity. If the effect is subtle, m₂ might win through Occam's Razor.
4. Compute the Bayes factor BF₃₂ needed for m₃ to beat m₂. What data pattern would produce this?

{fill:textarea}

## Part 2: Bayesian Model Reduction

> **Learning Goal:** Apply BMR to prune a generative model.

**Exercise**: You have a full model with 6 connections (parameters) representing a brain network: A→B, A→C, B→C, B→D, C→D, D→A.

After fitting the full model, BMR is applied to test whether each connection can be removed:

| Connection | Full Model Posterior (θ*) | BMR Evidence Change (Δln p(o|m)) | Keep or Remove? |
|-----------|--------------------------|----------------------------------|----------------|
| A→B | θ* = 0.8, tight posterior | -15.2 (removing this greatly hurts evidence) | Keep |
| A→C | θ*= 0.3, broad posterior | +1.2 (removing this slightly improves evidence) | Remove |
| B→C | θ* = 0.6, moderate posterior | -5.1 | Keep |
| B→D | θ*= 0.1, very broad posterior | +2.8 (removing this significantly improves evidence) | Remove |
| C→D | θ* = 0.7, tight posterior | -11.3 | Keep |
| D→A | θ* = 0.2, broad posterior | +0.3 (marginal improvement) | Remove (marginal) |

1. The reduced model has connections: A→B, B→C, C→D. Draw the reduced network.
2. Why did broad posteriors tend to be removed? (Broad posterior = parameter is poorly identified = not well-supported by data)
3. What does this procedure correspond to biologically? (Sleep-dependent pruning)

{fill:textarea}

## Part 3: Structure Learning Simulation

> **Learning Goal:** Trace a structure learning algorithm.

**Exercise**: Starting with a fully connected model of 4 variables (A, B, C, D = 6 possible edges), discover the true structure:

True structure: A → B → D, A → C → D (a diamond graph)

1. **Score-based approach**: How many models must you evaluate with 4 variables? (2⁶ = 64 possible edge combinations)
2. **Constraint-based approach**: Test A ⊥ D | {B, C}. If true, remove direct A→D edge. Continue until all conditional independences are tested.
3. **BMR approach**: Start fully connected. Remove edges one at a time using BMR. Order of removal depends on which parameter is least well-supported.

Which approach is most efficient? Which is most reliable?

{fill:textarea}

## Part 4: Hierarchical Model Design

> **Learning Goal:** Design a hierarchical Bayesian model for group inference.

**Exercise**: Design a PEB model for a neuroimaging study with N=30 subjects:

1. **Level 1 (Within-subject)**: Each subject has their own copy of a cognitive model with parameters θᵢ. Fit each subject's data independently.
2. **Level 2 (Group-level)**: The subject-level parameters are drawn from a group distribution: θᵢ ~ N(μ_group, Σ_group)
3. **Level 3 (Hyperprior)**: μ_group and Σ_group have their own hyperpriors

How does PEB "borrow strength" from the group? (Subjects with noisy data are pulled toward the group mean)

Design the model for a specific study: comparing a patient group (N=15) with controls (N=15). What parameters differ between groups?

{fill:textarea}

## Part 5: Reflection

In 300 words, reflect: BMS and BMR provide powerful tools for scientific model comparison. But they assume that the "true" model is in the model space being compared. What happens when all candidate models are wrong (model misspecification)? Does BMS still identify the best approximation, or can it systematically mislead?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Model comparison | BMS with Occam's Razor |
| 2 | Model pruning | BMR application |
| 3 | Structure discovery | Structure learning algorithms |
| 4 | Hierarchical design | PEB for group inference |
| 5 | Critical evaluation | Model misspecification |
