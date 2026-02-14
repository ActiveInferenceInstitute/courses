# Module 06: Learning — Synaptic Plasticity and Model Updating

> **Course**: Active Inference 101 | **Unit**: Computational Neuroscience | **Audience**: First-semester undergraduates

## Learning Objectives

1. Describe **synaptic plasticity** (Hebbian learning, LTP/LTD) as the neural basis of model updating.
2. Explain how **reward prediction errors** (dopamine signals) drive reinforcement learning in the basal ganglia.
3. Describe the role of the **hippocampus** in memory consolidation and replay.

## Introduction

Learning is the brain's ability to update itself with experience. At the neural level, this means changing the strength of connections between neurons — **synaptic plasticity**. This module explores the specific neural mechanisms that implement learning.

## Key Concepts

### 1. Hebbian Learning — "Neurons That Fire Together Wire Together"

The most fundamental rule of synaptic plasticity:

- If neuron A repeatedly helps fire neuron B, the connection A→B gets stronger
- This is **long-term potentiation (LTP)**: a lasting increase in synaptic strength
- The reverse is **long-term depression (LTD)**: when connections weaken because neurons stop co-activating

In Active Inference terms, LTP/LTD update the generative model's parameters — strengthening associations that predict well and weakening those that don't.

### 2. NMDA Receptors — The Coincidence Detector

The molecular mechanism behind LTP involves **NMDA receptors**:

- NMDA receptors require *both* presynaptic activity (glutamate) *and* postsynaptic depolarization to open
- They act as **coincidence detectors** — they only activate when input and output are simultaneously active
- When activated, calcium enters the cell, triggering molecular cascades that strengthen the synapse

This is a beautiful neural implementation of Bayesian updating — learning happens when prior expectations (postsynaptic activity) coincide with sensory evidence (presynaptic input).

### 3. Dopamine and Reward Prediction Errors

Dopamine neurons in the VTA fire specifically to **reward prediction errors**:

- **Unexpected reward**: Dopamine burst → "This was better than expected" → strengthen actions that led here
- **Expected reward received**: No dopamine change → "As predicted, no update needed"
- **Expected reward absent**: Dopamine dip → "This was worse than expected" → weaken actions that led here

This signal teaches the basal ganglia which policies lead to good outcomes. It's remarkably similar to the TD (temporal difference) learning algorithm used in AI.

### 4. Hippocampal Memory and Replay

The **hippocampus** is critical for forming new episodic memories and spatial maps:

- During experience: The hippocampus rapidly encodes events as patterns of neural activity
- During sleep (sharp-wave ripples): The hippocampus **replays** these patterns, transferring information to the cortex for long-term storage
- This replay implements the slow parameter updates discussed in Module 06 (Cognitive Science)

Place cells and grid cells in the hippocampus form a **cognitive map** — a generative model of space that allows navigation and planning.

### 5. Spike-Timing Dependent Plasticity (STDP)

Modern research has refined Hebb's rule with temporal precision:

- If presynaptic neuron fires *just before* postsynaptic neuron → LTP (the input *predicted* the output)
- If presynaptic neuron fires *just after* postsynaptic neuron → LTD (the input *didn't predict* the output)
- The timing window is ~20-40ms

STDP is essentially prediction-error-driven learning at the synaptic level: connections that successfully predict postsynaptic activity are strengthened.

## Summary

Learning at the neural level involves synaptic plasticity (LTP/LTD), mediated by NMDA receptors that detect coincident activity. Dopamine signals reward prediction errors that update policy preferences. The hippocampus rapidly encodes memories and replays them during sleep for cortical consolidation. STDP provides a temporal mechanism where synapses that predict successfully are strengthened.

## Further Reading

- Schultz, W. (2016). Dopamine reward prediction error. *Current Opinion in Neurobiology*, 29, 105-110.
- Bi, G. & Poo, M. (1998). Synaptic modifications in cultured hippocampal neurons. *Journal of Neuroscience*, 18(24), 10464-10472.
- O'Reilly, R. C. & Frank, M. J. (2006). Making working memory work. *Neural Computation*, 18(2), 283-328.
