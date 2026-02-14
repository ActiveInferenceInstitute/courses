# Module 03: Perception — Electrophysiological Methods for Active Inference

> **Course**: Active Inference 401 | **Unit**: Research Methods | **Audience**: Graduate students / researchers

## Learning Objectives

1. Apply electrophysiological methods (**EEG, MEG, intracranial recordings**) to test Active Inference predictions.
2. Analyze the relationship between **neural oscillations** and Active Inference computations.
3. Evaluate experimental paradigms that dissociate **prediction, prediction error, and precision**.

## Key Concepts

### 1. Neural Signatures of Predictive Processing

Active Inference makes specific predictions about neural signals that can be tested with electrophysiology:

**Prediction errors**: Sensory prediction errors should manifest as **mismatch negativity (MMN)** in EEG — a neural response to unexpected stimuli. The MMN amplitude indexes the magnitude of the prediction error.

**Predictions**: Top-down predictions should be encoded in **pre-stimulus oscillatory activity**. Alpha-band (8-12 Hz) power reflects precision-weighted predictions — stronger alpha = more confident prior, less reliance on sensory input.

**Precision**: The gain on prediction errors is modulated by precision. In EEG, this maps to **attention-related changes in oscillatory power**: increased gamma (>30 Hz) at the attended location reflects increased precision weighting; increased alpha at the unattended location reflects decreased precision.

### 2. Oscillatory Markers of Hierarchical Inference

Active Inference predicts specific roles for different frequency bands:

| Frequency Band | Active Inference Role | EEG/MEG Signature | Experimental Evidence |
|---------------|---------------------|-------------------|---------------------|
| Delta (1-4 Hz) | Slowest-level predictions | Entrainment to speech rhythm | Ding et al. (2016) |
| Theta (4-8 Hz) | Memory-guided prediction | Hippocampal theta during prediction | Rizzuto et al. (2003) |
| Alpha (8-12 Hz) | Precision modulation (suppression of irrelevant PE) | Alpha increase at unattended locations | Foxe & Snyder (2011) |
| Beta (13-30 Hz) | Maintenance of predictions (status quo) | Beta reduction during prediction update | Engel & Fries (2010) |
| Gamma (30-100 Hz) | Prediction error / local computation | Gamma at expected mismatch locations | Bastos et al. (2012) |

**Directional flow**: Bottom-up (prediction error) signals predominantly travel in gamma/theta. Top-down (prediction) signals predominantly travel in beta/alpha. This can be measured with **Granger causality** or **directed transfer function** on frequency-resolved signals.

### 3. Key Experimental Paradigms

**Mismatch Negativity (MMN)**: Present a train of standard stimuli (e.g., identical tones), then an occasional deviant. The MMN (deviant - standard difference wave) indexes prediction error. Active Inference predicts: larger MMN for more predictable contexts (stronger prediction = larger error when violated).

**Roving Oddball**: The standard changes every few trials. As the number of repetitions increases, the brain's prediction strengthens, and the MMN to the deviant grows. This directly tests belief updating — each repetition updates the generative model's precision about the standard.

**Oddball with Varying Volatility**: Manipulate how often the standard changes. In volatile blocks (frequent changes), the brain should weight recent evidence more heavily (higher learning rate). In stable blocks, it should weight accumulated evidence. Active Inference predicts measurable differences in PE magnitude and latency.

**Hierarchical Prediction Paradigms**: Use stimuli with structure at multiple levels (e.g., sequences of tones grouped into patterns, with patterns grouped into blocks). Prediction errors at different levels should have different latencies and scalp distributions:

- Local (within-pattern) PE: early, sensory cortex
- Global (between-pattern) PE: late, frontal cortex

### 4. Intracranial Recordings

Invasive recordings in neurosurgical patients provide unprecedented resolution:

**Laminar recordings**: Multi-electrode arrays spanning cortical layers can directly measure:

- Superficial layers (L2/3): prediction errors (ascending messages)
- Deep layers (L5/6): predictions (descending messages)
- Layer 4: input from thalamus

**Single-neuron correlates**: Individual neurons can be classified as:

- **Error neurons**: Fire to unexpected stimuli, silent to expected
- **Prediction neurons**: Active during anticipation, suppressed by input
- **Precision neurons**: Modulate gain on other neurons' responses

### 5. Analysis Methods

**Time-frequency analysis**: Decompose the signal into time-varying frequency content using wavelets or short-time FFT. This reveals when different oscillatory processes engage.

**Source localization**: Reconstruct the cortical sources of scalp-recorded signals (beamforming, LCMV, MNE). This maps oscillatory signatures to specific brain regions.

**Dynamic Causal Modelling for EEG/MEG**: DCM applied to event-related potentials or oscillatory data. Uses neural mass models (populations of neurons with mean-field dynamics) as the generative model.

## Summary

Electrophysiology provides direct tests of Active Inference through neural prediction error signals (MMN), oscillatory correlates of predictions and precision (alpha, beta, gamma), and laminar recordings distinguishing ascending and descending messages. Key paradigms include mismatch negativity, roving oddball, and hierarchical prediction tasks.

## Further Reading

- Garrido, M. I. et al. (2009). The mismatch negativity: A review of underlying mechanisms. *Clinical Neurophysiology*, 120(3), 453-463.
- Bastos, A. M. et al. (2012). Canonical microcircuits for predictive coding. *Neuron*, 76(4), 695-711.
- Sedley, W. et al. (2016). Neural signatures of perceptual inference. *eLife*, 5, e11476.
