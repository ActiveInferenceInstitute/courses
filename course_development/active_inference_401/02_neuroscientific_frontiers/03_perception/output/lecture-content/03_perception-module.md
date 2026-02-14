# Module 03: Perception — Neural Oscillations and Predictive Coding

> **Course**: Active Inference 401 | **Unit**: Neuroscientific Frontiers | **Audience**: Advanced undergraduates / graduate students

## Learning Objectives

1. Analyze how **neural oscillations** (alpha, beta, gamma) implement the distinction between predictions and prediction errors.
2. Evaluate the **gamma-for-errors, beta-for-predictions** hypothesis and its empirical support.
3. Examine how **attention** modulates perceptual inference through precision weighting of oscillatory signals.

## Key Concepts

### 1. Oscillatory Implementation of Predictive Coding

Neural oscillations provide the temporal infrastructure for Active Inference. Different frequency bands serve different computational roles:

**Gamma oscillations (30-100 Hz)**: Associated with **feedforward processing** — bottom-up prediction errors traveling from lower to higher cortical areas. Gamma power increases when stimuli are unexpected (large prediction errors). Gamma is generated primarily in superficial cortical layers (L2/3), consistent with the canonical microcircuit's identification of L2/3 as the prediction error layer.

**Beta oscillations (13-30 Hz)**: Associated with **feedback processing** — top-down predictions traveling from higher to lower cortical areas. Beta power increases when predictions are strong and confirmed. Beta is generated primarily in deep cortical layers (L5/6), consistent with the canonical microcircuit. When you expect a stimulus and it arrives as predicted, beta coherence increases — the predictive model is "winning."

**Alpha oscillations (8-12 Hz)**: Associated with **precision gating** — controlling which prediction errors are given high or low weight. Alpha power *increases* over task-irrelevant cortical regions (suppressing unattended prediction errors) and *decreases* over task-relevant regions (boosting attended prediction errors). Alpha implements the precision mechanism of attention.

### 2. Empirical Evidence for the Oscillatory Framework

**Mismatch negativity (MMN)**: When a deviant stimulus breaks a pattern of standards (e.g., "beep beep beep BOOP"), a negative-going ERP component appears at ~150ms. This has been extensively modeled as a prediction error signal, associated with increased gamma power over auditory cortex.

**Ketamine and NMDA**: Ketamine blocks NMDA receptors, which are critical for feedback (top-down) processing. Under ketamine, prediction errors increase (gamma rises) because top-down predictions can no longer suppress expected input. This is the pharmacological evidence for the feedforward/feedback distinction.

**Visual illusions**: Binocular rivalry studies show that gamma coherence increases with the dominant percept (the winning prediction), while beta coherence tracks the overall predictive framework. This demonstrates oscillatory dynamics tracking perception in real time.

**Magnetoencephalography (MEG) studies**: Laminar MEG has directly measured feedforward gamma and feedback beta in human cortex during perceptual tasks, providing direct support for the oscillatory predictive coding framework (Michalareas et al., 2016).

### 3. Attention as Precision Optimization

Active Inference explains attention as the optimization of precision — the synaptic gain of prediction error units:

**Spatial attention**: When you attend to a location, prediction errors from that location receive higher gain (precision). Neurally, alpha power decreases over the contralateral visual cortex, "opening the gate" for prediction errors.

**Feature attention**: Attending to a feature (color, motion) increases precision for that feature across the visual field. This is implemented by selective gain modulation of feature-specific prediction error neurons.

**Temporal attention**: Attending to a moment in time increases precision for stimuli arriving at that moment. This is coordinated by delta-theta oscillations (1-4 Hz) that create rhythmic fluctuations in excitability.

**The attentional blink**: When two targets appear in rapid succession, the second is often missed. Active Inference explains this as temporary depletion of precision resources — the first target consumes attentional precision, leaving insufficient gain for the second.

### 4. Cross-Frequency Coupling

Predictions and errors at different hierarchical levels are linked through cross-frequency coupling:

**Phase-amplitude coupling (PAC)**: The phase of a slow oscillation (theta/alpha from higher levels) modulates the amplitude of a fast oscillation (gamma from lower levels). This implements hierarchical control — higher-level predictions (encoded in slow oscillations) gate lower-level error signaling (encoded in fast oscillations).

**Example**: During visual search, frontal theta (representing the search target prediction) modulates visual gamma (representing feature-level processing). The prediction literally shapes what errors are computed.

### 5. Predictive Coding in Sensory Systems

**Visual system**: V1 neurons show robust surround suppression — responses to expected stimuli within the receptive field context are suppressed, while unexpected stimuli generate strong responses. This is prediction error in action.

**Auditory system**: Stimulus-specific adaptation (SSA) — neurons reduce responses to repeated stimuli but respond strongly to deviants. This implements the prediction error for the mismatch negativity paradigm.

**Somatosensory system**: Self-generated touch is perceived as less intense than externally generated touch (sensory attenuation). Active Inference: the motor system generates a prediction of the expected touch, which is subtracted from the actual signal, reducing the prediction error.

### 6. Cross-Modal Prediction Errors

When predictions are violated across sensory modalities simultaneously, distinct oscillatory signatures emerge:

**Audiovisual mismatch**: The McGurk effect demonstrates that visual lip-reading predictions modulate auditory perception. When audiovisual signals conflict, cross-modal prediction errors generate enhanced gamma activity spanning temporal and parietal cortex — reflecting the brain's attempt to reconcile conflicting modality-specific predictions under a single hierarchical generative model.

**Multisensory binding**: Beta coherence between sensory cortices increases when cross-modal signals are congruent — the generative model successfully predicts across modalities. This explains the temporal binding window (~200ms) within which multisensory stimuli are fused: coherent beta oscillations integrate predictions across modalities within this window.

> **Clinical Vignette — Chronic Pain as Precision Disorder**: Chronic pain often persists without ongoing tissue damage. Active Inference offers a compelling explanation: the precision of interoceptive prediction errors is pathologically elevated. The brain weights pain-related prediction errors too highly (aberrant alpha suppression over somatosensory cortex), causing phantom nociceptive signals to dominate perception. This reframes chronic pain as a *precision disorder* rather than a sensory disorder — and suggests that treatments targeting precision (meditation, TENS, placebo/expectation manipulation) work by rebalancing oscillatory gain control rather than by blocking sensory transmission.

> **Cross-Track Connection — Advanced Theory (Module 03)**: The precision-weighting of cross-modal prediction errors connects directly to the mathematical treatment of precision matrices in the variational inference framework. The diagonal elements of the precision matrix Π correspond to within-modal precision, while off-diagonal elements capture cross-modal expectations.

## Summary

Neural oscillations implement Active Inference: gamma carries prediction errors feedforward, beta carries predictions feedback, and alpha implements precision gating (attention). Cross-frequency coupling links hierarchical levels. Cross-modal prediction errors produce distinctive oscillatory signatures, and chronic pain can be understood as a precision disorder. Empirical evidence from MMN, ketamine studies, binocular rivalry, and laminar MEG supports this framework. Attention is precision optimization — the modulation of synaptic gain on prediction error units.

## Further Reading

- Bastos, A. M. et al. (2015). Visual areas exert feedforward and feedback influences through distinct frequency channels. *Neuron*, 85(2), 390-401.
- Michalareas, G. et al. (2016). Alpha-beta and gamma rhythms subserve feedback and feedforward influences among human visual cortical areas. *Neuron*, 89(2), 384-397.
- Arnal, L. H. & Giraud, A. L. (2012). Cortical oscillations and sensory predictions. *Trends in Cognitive Sciences*, 16(7), 390-398.
- Sedley, W. et al. (2016). Neural signatures of perceptual inference. *eLife*, 5, e11476.
- Wiech, K. (2016). Deconstructing the sensation of pain: The influence of cognitive processes on pain perception. *Science*, 354(6312), 584-587.
