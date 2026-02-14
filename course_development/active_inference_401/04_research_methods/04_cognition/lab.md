# Lab: Behavioral Paradigms for Active Inference

> **Learning Goal:** Design, analyze, and evaluate behavioral experiments testing Active Inference predictions.

## Part 1: Eye-Tracking Experiment Design

**Exercise**: Design an eye-tracking study testing epistemic foraging:

**Task**: Visual scene containing objects at 8 locations. Some locations are familiar (low uncertainty), others novel (high uncertainty). Participant's goal: identify all objects.

**Active Inference prediction**: First fixations should be directed toward high-uncertainty (novel) locations — epistemic foraging maximizes information gain.

Specify:

1. **Stimulus design**: 8 objects, 4 familiar (seen in training) + 4 novel
2. **Dependent variable**: Proportion of first fixations to novel vs. familiar locations
3. **Expected result**: >70% first fixations to novel locations
4. **Control experiment**: Repeat with explicit reward at specific locations (pragmatic motive) — does pragmatic value override epistemic foraging?
5. **Analysis**: Compute information gain for each fixation sequence and correlate with scanpath data

{fill:textarea}

## Part 2: Pupillometry Experiment

> **Learning Goal:** Design a pupillometry study testing precision and surprise.

**Exercise**: Task = auditory oddball with 3 conditions:

| Condition | Standard Probability | Deviant Probability | Expected Pupil Response to Deviant |
|-----------|---------------------|--------------------|------------------------------------|
| Predictable | 90% | 10% | Large dilation (high PE due to strong prediction) |
| Moderate | 70% | 30% | Moderate dilation |
| Unpredictable | 50% | 50% | Small dilation (weak prediction = small PE) |

**Prediction**: Pupil dilation to deviants scales with prediction strength (more predictable contexts → larger PE → larger pupil dilation).

Additionally measure **tonic pupil size**:

- Unpredictable condition → larger tonic pupils (higher uncertainty / volatility)
- Predictable condition → smaller tonic pupils

Specify the analysis: How do you isolate the phasic (event-related) from tonic pupil components?

{fill:textarea}

## Part 3: Reversal Learning Analysis

> **Learning Goal:** Analyze computational signatures in reversal learning data.

**Exercise**: A participant completes 200 trials of probabilistic reversal learning (2 options, reward reversals every ~30 trials):

**Behavioral signatures to identify**:

| Signature | Description | Computational Interpretation |
|-----------|-------------|------------------------------|
| Win-stay probability | P(repeat choice | previous reward) | Policy precision β |
| Lose-shift probability | P(switch | previous loss) | Learning rate α |
| Post-reversal perseveration | Trials to switch after reversal | Prior volatility ω (low ω → more perseveration) |
| Pre-reversal switching | Premature switches before reversal | High ω (over-estimating volatility) |
| Choice consistency | Overall stability of choice patterns | β (policy precision) |

Estimate the participant's computational phenotype from these behavioral signatures.

{fill:textarea}

## Part 4: Information Sampling Task

> **Learning Goal:** Design a task that measures the exploration-exploitation trade-off.

**Exercise**: Design a "when to commit" task:

**Task**: Participant sees 12 boxes. Each box hides a token (red or blue). They can open boxes (information sampling) or commit to guessing which color is majority (decision). Reward if correct.

**Active Inference prediction**: Agent opens boxes until EFE(commit) < EFE(sample):

- G(commit) = risk of wrong guess (pragmatic cost)  
- G(sample) = cost of time + expected information gain

**Manipulation**: Vary the cost of sampling (low cost vs. high cost per box opened)

| Sampling Cost | Predicted Behavior | AI Parameter |
|--------------|-------------------|-------------|
| Low (1 point per box) | Open many boxes (~8-10) | High epistemic value threshold |
| High (5 points per box) | Open few boxes (~3-4) | Lower threshold, accept more risk |

How would clinical populations differ? (Jumping-to-conclusions in schizophrenia → open fewer boxes)

{fill:textarea}

## Part 5: Reflection

In 300 words, reflect: Behavioral experiments are necessarily indirect — we observe choices, reaction times, and eye movements, not prediction errors or precision. How confident can we be that the computational variables we infer actually correspond to brain processes? What additional evidence (neural, pharmacological) is needed?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Experiment design | Epistemic foraging via eye-tracking |
| 2 | Pupillometry design | Precision and surprise measurement |
| 3 | Data interpretation | Computational phenotyping from behavior |
| 4 | Task design | Exploration-exploitation trade-off |
| 5 | Critical reflection | Inference-to-brain mapping |
