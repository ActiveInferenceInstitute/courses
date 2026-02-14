# Lab: Decision-Making and Prefrontal Function

> **Learning Goal:** Analyze neural decision-making through Active Inference, focusing on EFE decomposition and dopaminergic control.

## Part 1: Prefrontal Policy Evaluation

**Exercise**: For a complex decision (choosing a career path), map each PFC region's contribution:

| PFC Region | Function | What It Computes for Career Choice |
|-----------|----------|-----------------------------------|
| dlPFC | Working memory / policy maintenance | Holds multiple career options in mind simultaneously |
| vmPFC | Pragmatic value computation | Estimates expected reward (salary, satisfaction) for each option |
| ACC | Conflict monitoring | Signals when options are close in value (high decision difficulty) |
| Frontopolar (BA10) | Counterfactual reasoning | Evaluates the "road not taken" — what if I chose differently? |
| OFC | Subjective value | Integrates personal preferences with objective outcomes |

Now trace a complete decision sequence: initial consideration → evaluation → conflict → resolution → commitment. What neural signal dominates at each stage?

{fill:textarea}

## Part 2: EFE Decomposition in Paradigms

> **Learning Goal:** Identify pragmatic and epistemic value in experimental paradigms.

**Exercise**: For each paradigm, identify the pragmatic and epistemic components:

| Paradigm | Pragmatic Value (reward) | Epistemic Value (information) | Which Dominates? |
|----------|------------------------|-------------------------------|-----------------|
| Two-armed bandit (exploitation phase) | Choosing the known high-reward arm | None — uncertainty already resolved | Pragmatic |
| Two-armed bandit (exploration phase) | Unknown reward at new arm | Sampling the new arm reveals its value | Epistemic |
| Foraging (rich environment) | Staying at current patch | Moving to unknown patch to estimate quality | Trade-off |
| Medical diagnosis | Prescribing treatment | Running diagnostic tests | Epistemic first, then pragmatic |
| Scientific experiment | Applying existing knowledge | Running experiment to reduce uncertainty | Epistemic |

For the foraging scenario, explain how the exploration-exploitation trade-off is resolved by EFE.

{fill:textarea}

## Part 3: Dopamine and Decision Confidence

> **Learning Goal:** Analyze how dopaminergic dysfunction affects decision-making.

**Exercise**: Complete the clinical analysis:

| Condition | Dopamine Status | Policy Precision (γ) | Behavioral Consequence | Active Inference Explanation |
|-----------|----------------|---------------------|----------------------|------------------------------|
| Healthy | Normal tonic DA | Moderate γ | Appropriate balance of decisive and flexible behavior | Precision-weighted EFE evaluation |
| Parkinson's (early) | Depleted tonic DA | Low γ | Indecisiveness, bradykinesia, apathy | Flat policy distribution → no clear winner |
| Schizophrenia (acute) | Elevated DA | High γ | Jumping to conclusions, aberrant salience, delusions | Overconfident belief in a single policy/model |
| ADHD | Dysregulated DA | Variable γ | Impulsive switching, difficulty maintaining focus | Moment-to-moment precision fluctuations |
| L-DOPA medication | Artificially elevated | Excessively high γ | Impulsive gambling, hypersexuality | Overshooting precision → compulsive exploitation |

For each condition, explain how medication or therapy could aim to recalibrate γ.

{fill:textarea}

## Part 4: Working Memory Experiment Design

> **Learning Goal:** Design an experiment testing the Active Inference account of working memory.

**Exercise**: Design an experiment to test the hypothesis that working memory capacity is limited by the number of gamma bursts within a theta cycle:

1. **Participants**: How many? What exclusion criteria?
2. **Task**: What working memory task? (e.g., sequential recall, change detection, spatial working memory)
3. **Neural measurements**: What brain signals would you record? (EEG/MEG for theta-gamma coupling)
4. **Predictions**: If the theta-gamma coupling hypothesis is correct, what specific result would you expect as working memory load increases from 1 to 6 items?
5. **Alternative hypothesis**: What would the result look like if working memory is not oscillation-based?

{fill:textarea}

## Part 5: Reflection

In 300 words, reflect: The neural decomposition of EFE into pragmatic and epistemic components is elegant, but real-world decisions rarely have clean pragmatic/epistemic separation. How well does this decomposition handle genuinely ambiguous decisions (e.g., choosing whether to have children, deciding whether to change careers)?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Neural mapping | PFC policy evaluation |
| 2 | Paradigm analysis | EFE decomposition |
| 3 | Clinical reasoning | Dopamine and decision confidence |
| 4 | Experiment design | Working memory oscillations |
| 5 | Critical reflection | Limits of decomposition |
