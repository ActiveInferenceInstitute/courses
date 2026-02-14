# Module 06: Learning — Synaptic Plasticity, Bayesian Model Reduction, and Developmental Change

## Learning Objectives

1. Explain how synaptic plasticity (LTP/LTD, spike-timing-dependent plasticity) implements the parameter learning of Active Inference.
2. Describe Bayesian Model Reduction as the brain's mechanism for structure learning — pruning unnecessary model complexity.
3. Connect these mechanisms to developmental critical periods, sleep consolidation, and the neuroscience of expertise.

## Introduction

The brain must learn from experience — updating its generative model to make better predictions. Active Inference identifies two forms of learning, each with distinct neural implementations: **parameter learning** (updating connection strengths within the existing model architecture) and **structure learning** (reorganizing the architecture itself). This module examines the neural evidence for both.

## Key Concepts

### 1. Parameter Learning and Synaptic Plasticity

Parameter learning corresponds to updating the brain's estimate of how environmental variables relate to each other. Neurally, this is implemented through **synaptic plasticity** — changes in the strength of connections between neurons.

- **Long-term potentiation (LTP)**: Strengthening of synapses when pre- and post-synaptic neurons fire together (Hebb's rule: "neurons that fire together, wire together").
- **Long-term depression (LTD)**: Weakening of synapses when activity is uncorrelated.
- **Spike-timing-dependent plasticity (STDP)**: The direction and magnitude of synaptic change depend on the precise timing of pre- and post-synaptic spikes — a temporal code for prediction error.

In Active Inference terms, STDP implements a form of online Bayesian updating: if the pre-synaptic neuron (carrying a prediction) fires just before the post-synaptic neuron (carrying sensory input), the synapse strengthens — the prediction was confirmed. If the timing is reversed, the synapse weakens — the prediction was wrong.

### 2. Structure Learning and Bayesian Model Reduction

Not all learning involves strengthening existing connections. Sometimes the brain must reorganize its model — adding new components or, more importantly, pruning unnecessary ones. Friston et al. (2017) proposed that **Bayesian Model Reduction (BMR)** — a computationally efficient method for comparing nested models — may be implemented during sleep.

During NREM sleep, the brain replays waking experiences and analytically evaluates whether simpler model structures (with fewer parameters) can explain the data equally well. If so, the simpler model is adopted. This connects to the phenomenon of **synaptic downscaling** during sleep (Tononi & Cirelli's synaptic homeostasis hypothesis): synapses are globally weakened during sleep, preserving only the strongest (most informative) connections.

### 3. Developmental Critical Periods and Expertise

**Critical periods** — windows of heightened plasticity in early development (e.g., for language, vision, emotional attachment) — can be understood as periods of high learning rate in the generative model. During critical periods, precision on prediction errors is high, driving rapid model updating. After the critical period closes, precision on existing priors increases, making the model more resistant to change.

Expertise represents the opposite end of the learning trajectory: a highly refined generative model with deep hierarchical structure, high-precision priors, and automated (habitual) policy selection.

## Clinical Connections

- **Alzheimer's disease**: Progressive loss of synaptic plasticity → inability to update the generative model → reliance on increasingly outdated predictions.
- **PTSD**: Maladaptive learning — a traumatic experience creates high-precision priors about danger that resist updating despite evidence of safety. Therapeutic approaches (exposure therapy, EMDR) work by reopening plasticity at the relevant prediction level.

## Conclusion

Learning in the brain is precision-weighted model updating, implemented through synaptic plasticity for parameters and through sleep-dependent model reduction for structure. Understanding these mechanisms connects Active Inference to developmental psychology, educational neuroscience, and psychiatric treatment. Module 07 examines how learned models are shared between brains — the neuroscience of communication.
