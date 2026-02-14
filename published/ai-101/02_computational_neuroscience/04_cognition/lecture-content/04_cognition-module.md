# Module 04: Cognition — Neural Substrates of Belief Updating

> **Course**: Active Inference 101 | **Unit**: Computational Neuroscience | **Audience**: First-semester undergraduates

## Learning Objectives

1. Describe how the **prefrontal cortex** maintains and updates beliefs through working memory.
2. Explain how **attention** is implemented neurally through precision-weighted gain modulation.
3. Identify neural correlates of free energy minimization in working memory and decision-making circuits.

## Introduction

Cognition — thinking, reasoning, deciding — depends on the brain's ability to maintain beliefs, update them with new evidence, and direct attention to relevant information. This module explores the neural circuits that make cognition possible.

## Key Concepts

### 1. Prefrontal Cortex and Working Memory

The **prefrontal cortex (PFC)** is the brain's executive hub. It maintains **working memory** — the ability to hold information in mind temporarily:

- PFC neurons can sustain activity for seconds, maintaining a representation (belief) even after the stimulus is gone
- This persistent activity represents the brain's current "best guess" about the relevant hidden states
- Different PFC regions handle different aspects: dorsolateral PFC for spatial/abstract, ventrolateral PFC for object/verbal

In Active Inference, working memory is the neural substrate of the approximate posterior q(s) — the brain's current beliefs about hidden states.

### 2. Attention Networks

The brain has two major attention networks:

- **Dorsal attention network** (top-down): Voluntary, goal-directed attention. "I will focus on the lecture." Increases precision on task-relevant information.
- **Ventral attention network** (bottom-up): Stimulus-driven, involuntary attention. "What was that sound?" Detects salient (high prediction error) stimuli.

Both implement precision weighting — the dorsal network turns up the gain on what you *want* to attend to, while the ventral network automatically boosts signals that are unexpectedly large.

### 3. Prefrontal-Parietal Interactions

Cognition involves tight collaboration between the PFC and parietal cortex:

- PFC generates abstract goals and maintains context
- Parietal cortex represents spatial relationships and current sensory state
- Together, they form a **fronto-parietal network** that implements goal-directed behavior

When this network is disrupted (e.g., in ADHD, schizophrenia), the ability to maintain context, shift attention, and update beliefs is impaired.

### 4. Neural Correlates of Belief Updating

When the brain updates beliefs, specific neural signatures can be measured:

- **P300 event-related potential**: A positive voltage deflection ~300ms after a surprising stimulus — reflects the updating of context/beliefs
- **Frontal theta oscillations (4-8 Hz)**: Increase during cognitive control, conflict detection, and model updating
- **Reduced prefrontal activity with learning**: As a situation becomes predictable, PFC activity decreases — less updating is needed

### 5. Computational Psychiatry

Disruptions in belief updating circuits produce characteristic psychiatric symptoms:

- **Schizophrenia**: Aberrant precision on prediction errors → inappropriate belief updating → delusions
- **ADHD**: Impaired precision modulation → difficulty maintaining focus and filtering irrelevant signals
- **Depression**: Reduced gain on positive prediction errors → difficulty updating toward positive beliefs
- **Anxiety**: Excessive gain on threat-related prediction errors → overestimation of danger

## Summary

Cognition is implemented through prefrontal working memory circuits that maintain beliefs, attention networks that control precision weighting, and fronto-parietal interactions that coordinate goal-directed behavior. Neural signatures like the P300 and frontal theta reveal real-time belief updating. Psychiatric conditions can be understood as characteristic disruptions of these precision-weighting mechanisms.

## Further Reading

- Miller, E. K. & Cohen, J. D. (2001). An integrative theory of prefrontal cortex function. *Annual Review of Neuroscience*, 24, 167-202.
- Corbetta, M. & Shulman, G. L. (2002). Control of goal-directed and stimulus-driven attention in the brain. *Nature Reviews Neuroscience*, 3(3), 201-215.
- Corlett, P. R. et al. (2019). Hallucinations and strong priors. *Trends in Cognitive Sciences*, 23(2), 114-127.
