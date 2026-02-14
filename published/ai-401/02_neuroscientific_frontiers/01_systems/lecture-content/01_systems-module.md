# Module 01: Systems — Neural Architecture for Active Inference

> **Course**: Active Inference 401 | **Unit**: Neuroscientific Frontiers | **Audience**: Advanced undergraduates / graduate students

## Learning Objectives

1. Map the **cortical hierarchical architecture** onto the generative model structure that supports Active Inference.
2. Analyze the roles of **feedforward** and **feedback** connections in implementing prediction errors and predictions.
3. Evaluate the evidence for **canonical microcircuit** implementations of Active Inference in cortex.
4. Integrate subcortical and neuromodulatory systems into a comprehensive neural Active Inference architecture.

## Introduction

Active Inference 101 introduced the computational principles of the FEP. This track asks: How does the brain actually implement these computations? We begin with the fundamental neural architecture — how cortical circuits, subcortical nuclei, and neuromodulatory systems create the hardware for active inference.

> **Key Insight — The Neural Argument**: Active Inference is not merely a normative theory about what the brain *should* do — it makes specific claims about *how* identifiable neural circuits implement free energy minimization. This module maps those claims onto anatomy, providing the basis for empirical testing throughout this track.

## Key Concepts

### 1. The Cortical Hierarchy as a Generative Model

The neocortex is organized as a **hierarchical system** of interconnected regions. This hierarchy maps directly onto the generative model:

**Lower levels** (V1, S1, A1): Represent fine-grained sensory features — edges, textures, tones. These correspond to the lowest level of the generative model, making precise predictions about sensory data.

**Middle levels** (V4, IT, parietal cortex): Represent objects, categories, and spatial relations. These encode intermediate abstractions in the generative model — predictions about what objects are present and where.

**Higher levels** (prefrontal cortex, anterior temporal lobe): Represent abstract concepts, goals, contexts, and narratives. These encode the deepest priors of the generative model — the agent's high-level understanding of its situation.

**The key principle**: Each level generates predictions sent *downward* to the level below, and receives prediction errors sent *upward* from the level below. This creates a bidirectional message-passing architecture that implements variational inference.

> **Cross-Track Connection — Advanced Theory (Module 04)**: The cortical hierarchy implements the deep temporal models discussed in the Advanced Theory track — each level operates at a progressively slower temporal scale, from millisecond-level sensory processing to minute- and hour-level narrative processing. This is the physical instantiation of the mathematical state-space hierarchy.

### 2. Feedforward vs. Feedback Connections

The asymmetry between ascending (feedforward) and descending (feedback) connections is central:

**Feedforward (bottom-up) connections**: Originate primarily from **superficial pyramidal cells** (layers 2/3). They are *driving* connections that carry prediction errors — the discrepancy between predictions and observations. They target layer 4 of the higher area.

**Feedback (top-down) connections**: Originate primarily from **deep pyramidal cells** (layers 5/6). They are *modulatory* connections that carry predictions — the top-down expectations. They target layers 1 and 6 of the lower area, modulating but not driving neural activity.

**Critical evidence**:

- Feedback connections are more diffuse and modulatory, consistent with carrying broad predictive signals
- Feedforward connections are sharper and more driving, consistent with carrying precise error signals
- Lesion studies show that removing feedback connections disrupts perceptual priors while preserving basic sensory responses
- Feedback connections often use NMDA receptors (slower, more modulatory), while feedforward connections use AMPA receptors (faster, more driving)
- **Laminar fMRI**: Recent ultra-high-field (7T) fMRI can resolve individual cortical layers, confirming that feedforward activity peaks in layer 4 while feedback activity peaks in layers 1/5/6 (Lawrence et al., 2019)
- **Granger causality analysis**: Directed information flow from V1→V4 is predominantly in the gamma band, while V4→V1 flow is predominantly beta — consistent with the oscillatory predictions from Module 03

### 3. The Canonical Microcircuit

Bastos et al. (2012) proposed a **canonical microcircuit** for predictive coding that maps Active Inference onto cortical layers:

| Layer | Cell Type | Signal | Role | Disruption Effect |
|-------|-----------|--------|------|-------------------|
| Layer 1 | Apical dendrites | Top-down predictions | Context modulation | Loss of contextual priors |
| Layer 2/3 | Superficial pyramidal | Prediction errors | Forward to next level | Perceptual learning fails |
| Layer 4 | Stellate/spiny | Feedforward input | Receives driving input | Sensory disconnection |
| Layer 5 | Deep pyramidal (thick) | Motor/output | Action and deep predictions | Motor paralysis |
| Layer 6 | Deep pyramidal (thin) | Feedback predictions | Backward to lower level | Perception becomes bottom-up only |

This canonical circuit is repeated across the entire cortex — each cortical column implements one "node" in the generative model, computing local prediction errors and updating local beliefs.

> **Clinical Vignette — Charles Bonnet Syndrome**: Patients with macular degeneration who lose bottom-up visual input sometimes experience vivid visual hallucinations — the generative model runs "unopposed" by feedforward evidence. This demonstrates that perception normally requires the interplay of top-down predictions and bottom-up errors. When errors are absent, predictions "hallucinate" a visual world.

### 4. Subcortical Contributions

The cortex doesn't work alone. Subcortical structures play critical roles:

**Basal ganglia**: Implement **policy selection** — evaluating actions by their expected free energy and selecting the best policy. The striatum encodes expected values, the pallidum implements competition among policies, and dopaminergic signals provide precision-weighted prediction errors about reward. Direct pathway (D1) = "go" for selected policy; indirect pathway (D2) = "no-go" for competing policies; hyperdirect pathway = global "stop" for re-evaluation.

**Cerebellum**: Implements **forward models** for motor control — predicting the sensory consequences of actions before they're executed. Cerebellar prediction errors (climbing fiber signals from the inferior olive) update the forward model. The cerebellum contains more neurons than the rest of the brain combined — a testament to the computational demands of forward modeling.

**Thalamus**: Acts as a **precision gate** — controlling the flow of prediction errors to cortex by modulating their gain. The reticular nucleus of the thalamus gates which prediction errors reach cortical awareness. The pulvinar nucleus specifically gates visual and attentional prediction errors.

**Hippocampus**: Implements **temporal inference** — maintaining an internal model of temporal unfolding and enabling episodic memory. The hippocampal formation maps states to their temporal context, supporting the "where am I in time" component of the generative model. Place cells, grid cells, and time cells create a spatiotemporal scaffold for the generative model.

**Superior colliculus**: Integrates multisensory prediction errors and generates orienting responses — the "what is it?" reflex that directs sensory resources toward unexpected events. This implements a low-level precision reallocation mechanism.

### 5. Precision and Neuromodulation

The concept of **precision** (inverse variance of prediction errors) is neurally implemented through neuromodulation:

| Neuromodulator | Source | Function in Active Inference | Clinical Deficit | Clinical Excess |
|----------------|--------|------------------------------|-----------------|-----------------|
| Dopamine | VTA/SNc | Precision of reward prediction errors; policy evaluation | Parkinson's (apathy, indecision) | Schizophrenia (aberrant salience) |
| Norepinephrine | Locus coeruleus | Overall arousal; expected precision of environmental volatility | Inattention, drowsiness | Panic, hypervigilance |
| Acetylcholine | Basal forebrain | Precision of sensory prediction errors; attention to input | Alzheimer's (perceptual confusion) | Sensory overwhelm |
| Serotonin | Raphe nuclei | Temporal discounting; precision over longer time horizons | Impulsivity | Excessive caution |

> **Key Insight — The Neuromodulatory Quartet**: These four neuromodulators constitute the brain's "precision control panel." Together they modulate what the brain attends to (ACh), how volatile it believes the world is (NE), how confident it is about its policies (DA), and how far ahead it plans (5-HT). Nearly all psychoactive drugs — therapeutic and recreational — work by modifying these precision parameters.

### 6. The Neural Architecture Debate: Open Questions

Despite strong evidence, several questions remain unresolved:

1. **Columnar precision**: Are cortical columns really the fundamental unit of the generative model, or is the relevant scale finer (mini-columns) or coarser (cortical patches)?
2. **Layer specificity**: Is the layer-by-layer mapping to predictions/errors as strict as the canonical microcircuit assumes, or is computation more distributed across layers?
3. **Non-hierarchical processing**: How do horizontal (lateral) connections within a cortical level fit into the framework? They may implement precision normalization across the cortical sheet.
4. **Cerebellar role expansion**: Recent evidence suggests the cerebellum contributes to cognition and emotion, not just motor control — extending the forward model concept beyond movement.

## Summary

The brain implements Active Inference through a cortical hierarchy where feedforward connections carry prediction errors and feedback connections carry predictions. The canonical microcircuit maps each cortical column to a node in the generative model. Subcortical structures handle policy selection (basal ganglia), forward models (cerebellum), precision gating (thalamus), temporal inference (hippocampus), and orienting (superior colliculus). Neuromodulators control the precision of prediction errors, with each neuromodulator tuning a different dimension of inferential precision. Open questions remain about the exact scale and specificity of these mappings.

## Further Reading

- Bastos, A. M. et al. (2012). Canonical microcircuits for predictive coding. *Neuron*, 76(4), 695-711.
- Shipp, S. (2016). Neural elements for predictive coding. *Frontiers in Psychology*, 7, 1792.
- Parr, T. & Friston, K. (2017). The active construction of the visual world. *Neuropsychologia*, 104, 92-101.
- Pezzulo, G. et al. (2015). Active Inference, homeostatic regulation and adaptive behavioural control. *Progress in Neurobiology*, 134, 17-35.
- Lawrence, S. J. D. et al. (2019). Laminar fMRI: Applications for cognitive neuroscience. *NeuroImage*, 197, 785-791.
