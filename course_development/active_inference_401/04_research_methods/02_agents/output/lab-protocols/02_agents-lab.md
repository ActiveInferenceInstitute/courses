# Lab: Computational Phenotyping and Individual Differences

> **Learning Goal:** Design and validate computational phenotyping studies.

## Part 1: Parameter Recovery Design

**Exercise**: For a probabilistic reversal learning task with an Active Inference POMDP model, design a parameter recovery study:

**Model parameters** to recover:

1. α (learning rate): How quickly beliefs about reward probabilities update
2. ω (prior volatility): How much the agent expects the environment to change
3. β (policy precision): How deterministically actions follow the softmax policy
4. C_reward (preference strength): How strongly the agent prefers reward vs. no-reward

**Recovery procedure**:

1. Choose 100 parameter combinations spanning the realistic range
2. For each, simulate 200 trials of behavior
3. Fit the model to each simulated dataset
4. Plot recovered vs. true parameters

**Expected results table**:

| Parameter | Range | Recovery r² | Common Issues |
|-----------|-------|------------|---------------|
| α | [0.1, 0.9] | Should be >0.85 | May be confounded with ω |
| ω | [0.01, 0.5] | Should be >0.80 | Boundary effects near 0 |
| β | [1, 10] | Should be >0.90 | Well-identified by choice variability |
| C_reward | [1, 5] | Should be >0.85 | Confounded with β if no explicit reward manipulation |

What would you do if α and ω are poorly separated (r² < 0.5)?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Model Fitting to Data

> **Learning Goal:** Practice fitting Active Inference models to empirical data.

**Exercise**: You have behavioral data from a reversal learning task. A participant made 200 choices with outcomes. Key patterns:

- Trials 1-80: Chose option A consistently (A rewarded 80% of the time)
- Trials 81-100: Continued choosing A after reversal (slow to switch)
- Trials 101-200: Gradually shifted to B

What do these behavioral patterns suggest about the computational phenotype?

| Observation | Parameter Implication |
|------------|---------------------|
| Consistent initial choice | Moderate β (confident in policy) |
| Slow reversal detection | Low ω (prior: environment is stable) + moderate α |
| Gradual shift | Not extreme in any parameter |

Estimate: Is this a "stable learner" (low ω, moderate α) or a "confused learner" (low α, high β)?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Clinical Application

> **Learning Goal:** Design study using computational phenotyping for clinical classification.

**Exercise**: Design a computational phenotyping study for anxiety disorders:

**Hypothesis**: Patients with generalized anxiety disorder (GAD) have elevated precision on threat-related prediction errors (ω_threat ↑) and exaggerated volatility estimates (heightened uncertainty about safety).

1. **Task**: Go/No-Go task with threat and safe cues. Shock (unconditioned stimulus) follows threat cues with 70% probability. Safe cues never paired with shock.
2. **Model**: Active Inference POMDP with parameters: threat precision (ω_threat), safety precision (ω_safe), learning rate (α), policy precision (β)
3. **Groups**: 30 GAD patients, 30 matched controls
4. **Analysis plan**: Fit model to each participant → PEB group comparison → identify parameters that differ between groups
5. **Expected results**: GAD patients show higher ω_threat (over-weighting threat PEs) and possibly lower ω_safe (under-weighting safety evidence)

What additional analyses would strengthen the clinical utility? (Normative modeling? Treatment prediction? Longitudinal tracking?)


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Normative Modeling

> **Learning Goal:** Apply normative modeling to identify individual deviations.

**Exercise**: Given a population of N=200 healthy controls, each with a 4-parameter computational phenotype (α, ω, β, C), construct a normative model:

1. Fit a multivariate Gaussian to the control group: N(μ_control, Σ_control)
2. For a new patient, compute the Mahalanobis distance from the population center
3. Identify which parameters deviate most from the normative distribution

Example: Patient X has parameters α=0.9 (very high), ω=0.05 (very low), β=8 (high), C=2 (moderate)

Is this profile within the normative range or pathological? Which parameter(s) are most deviant?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Reflection

In 300 words, reflect: Computational phenotyping promises personalized psychiatry, but faces challenges: model misspecification, test-retest reliability, and the question of whether computational parameters truly capture stable traits or fluctuating states. How should these challenges be addressed?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Validation design | Parameter recovery |
| 2 | Data interpretation | Behavioral-to-computational mapping |
| 3 | Clinical study design | Computational phenotyping for psychiatry |
| 4 | Statistical modeling | Normative modeling |
| 5 | Critical evaluation | Practical challenges |
