# Lab: Neural Architecture for Active Inference

> **Learning Goal:** Map cortical circuitry and subcortical systems onto Active Inference computations, analyzing empirical evidence.

## Part 1: Cortical Hierarchy Mapping

**Exercise**: For each brain region, specify its level in the generative hierarchy, the type of predictions it generates, and the prediction errors it receives:

| Brain Region | Hierarchy Level | Predictions Generated (top-down) | Prediction Errors Received (bottom-up) | Example |
|-------------|----------------|----------------------------------|----------------------------------------|---------|
| V1 (primary visual) | Lowest visual | Oriented edge expectations | Retinal contrast mismatches | Predicting edge at 45° |
| V4 (color/shape) | Intermediate visual | Shape and color expectations | V1 feature-combination errors | Predicting "round and red" |
| Inferior temporal (IT) | High visual | Object identity expectations | V4 shape errors | Predicting "apple" |
| Prefrontal cortex | Highest | Goal/context expectations | IT object relevance errors | Predicting "kitchen context" |

Now trace a specific percept (e.g., recognizing a friend's face) through this hierarchy. What predictions flow down? What errors flow up? How is the percept "constructed"?

{fill:textarea}

## Part 2: Canonical Microcircuit Analysis

> **Learning Goal:** Analyze how cortical layers implement predictive coding operations.

**Exercise**: For the Bastos et al. (2012) canonical microcircuit, explain the computational role of each layer and how damage to that layer would disrupt Active Inference:

| Layer | Computation | Effect of Damage |
|-------|------------|-----------------|
| L1 (apical dendrites) | Receives top-down context modulation | Loss of contextual modulation; perception becomes context-free |
| L2/3 (superficial pyramidal) | Computes and sends prediction errors upward | Loss of error signaling; higher levels receive no updates |
| L4 (stellate cells) | Receives feedforward driving input | Sensory input is disconnected from cortical processing |
| L5 (deep pyramidal, thick) | Generates motor output and deep predictions | Loss of action generation and deep generative structure |
| L6 (deep pyramidal, thin) | Sends predictions to L4 and L1 of lower area | Loss of top-down predictions; perception becomes purely bottom-up |

Write a 200-word analysis: What would perception look like if only feedforward connections remained (all feedback removed)? What does this predict about the experience of patients with specific lesion patterns?

{fill:textarea}

## Part 3: Subcortical System Analysis

> **Learning Goal:** Map subcortical structures to Active Inference computations.

**Exercise**: Complete the analysis for each subcortical structure:

| Structure | Active Inference Function | Key Neural Circuit | Clinical Significance |
|-----------|--------------------------|-------------------|----------------------|
| Basal ganglia (striatum) | Policy evaluation — expected value of actions | Cortex→Striatum→Pallidum→Thalamus→Cortex | Parkinson's: impaired policy selection |
| Cerebellum | Forward models for motor prediction | Pontine nuclei→cerebellum→red nucleus/thalamus | Ataxia: prediction errors in motor control |
| Thalamus (pulvinar) | Precision gating of prediction errors | Reticular nucleus inhibition of relay cells | Neglect syndromes: precision mis-allocation |
| Hippocampus | Temporal inference and episodic memory | CA3 recurrent collaterals→CA1→entorhinal | Amnesia: inability to contextualize in time |

For each structure, explain what would happen to Active Inference if it were removed.

{fill:textarea}

## Part 4: Neuromodulation and Precision

> **Learning Goal:** Analyze how neuromodulators implement precision weighting.

**Exercise**: Design a simple thought experiment for each neuromodulator:

1. **Dopamine (too much / too little)**: How does dopamine excess (e.g., schizophrenia) vs. deficiency (e.g., Parkinson's) affect policy selection and reward prediction?
2. **Norepinephrine (too high / too low)**: How does NE excess (e.g., panic attack) vs. deficiency (e.g., inattention) affect precision of environmental volatility?
3. **Acetylcholine (too high / too low)**: How does ACh excess vs. deficiency (e.g., Alzheimer's) affect sensory precision?
4. **Serotonin (too high / too low)**: How does serotonin excess vs. deficiency affect temporal discounting?

{fill:textarea}

## Part 5: Empirical Evidence Evaluation

> **Learning Goal:** Critically assess the evidence for neural Active Inference.

**Exercise**: Evaluate three key predictions of neural Active Inference against empirical evidence:

| Prediction | Evidence For | Evidence Against | Verdict |
|-----------|-------------|-----------------|---------|
| Feedforward = errors, feedback = predictions | Laminar fMRI, electrophysiology, lesion studies | Some feedback connections seem to carry error signals | |
| Cortical columns = generative model nodes | Anatomical organization, computational modeling | Column boundaries are less clear than assumed | |
| Neuromodulators = precision weighting | Psychopharmacology data, computational modeling | Multiple functions of each neuromodulator | |

Write a 300-word assessment: Is neural Active Inference well-supported, or is it still largely theoretical?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Anatomical mapping | Cortical hierarchy ↔ generative model |
| 2 | Circuit analysis | Canonical microcircuit |
| 3 | Systems analysis | Subcortical contributions |
| 4 | Clinical reasoning | Neuromodulation and precision |
| 5 | Evidence evaluation | Empirical support |
