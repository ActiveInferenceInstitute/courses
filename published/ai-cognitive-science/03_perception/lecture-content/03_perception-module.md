# Module 03: Perception — Predictive Coding, Sensory Attenuation, and Hallucinations

## Learning Objectives

1. Describe the **predictive coding** architecture: how hierarchical cortical layers generate top-down predictions and bottom-up prediction errors.
2. Explain how **sensory attenuation** (the reduced perception of self-generated stimuli) demonstrates the profound action-perception duality at the core of Active Inference.
3. Understand **binocular rivalry** as a paradigmatic example of the brain's inferential struggle to settle on a single, coherent generative model of the world.
4. Analyze hallucinations in schizophrenia and other clinical conditions as catastrophic failures of the precision-weighted prediction error mechanism.

## Introduction

In classical cognitive science, perception is a passive, bottom-up process: the eye acts as a camera, sending data up to the brain for feature extraction and semantic labeling. Active Inference completely inverts this model. Building on the foundational work of Helmholtz (unconscious inference), perception is understood as an active, top-down process of hypothesis testing.

Rao and Ballard (1999) demonstrated that hierarchical predictive coding in the visual cortex could seamlessly explain both classical receptive field properties and context-dependent response modulation. Their model established the neural architecture for Active Inference's central claim: perception *is* inference. Higher cortical areas send **predictions** (priors) down the hierarchy; lower sensory areas send **prediction errors** (the difference between what was expected and what arrived) back up. Perception only occurs when these prediction errors are minimized, and the brain settles on the hypothesis that best explains the sensory data.

## Key Concepts

### 1. The Predictive Coding Architecture in the Cortex

The six-layered mammalian neocortex perfectly implements the message-passing scheme required by Active Inference:

- **Deep pyramidal cells** (layers 5/6) act as the generative model, sending **top-down predictions** about the expected state of the world to lower cortical areas.
- **Superficial pyramidal cells** (layers 2/3) act as the error-checking mechanism, computing the mismatch and sending **bottom-up prediction errors** to higher areas to force model updates.
- **The Granular layer** (layer 4) receives these integrating streams.

In the primary visual cortex (V1), this means that the firing rate of a neuron to a visual stimulus depends not just on what physical light hits the retina, but on whether that light was *predicted* by a higher area (like V2 or IT cortex). Fully expected stimuli produce attenuated, quiet responses (the prediction perfectly explained the data); unexpected stimuli produce massive, amplified firing responses (a large prediction error demanding the higher model to update).

### 2. Binocular Rivalry: The Struggle for Coherence

**Binocular rivalry** provides a stunning subjective demonstration of perception-as-inference. In a laboratory setting, if you present a picture of a house to a subject's left eye and a picture of a face to their right eye, they do not perceive a blended "face-house." The brain refuses to generate an impossible world model.

Instead, subjective perception *alternates*. The subject sees a house for a few seconds, then it dissolves into a face, then back to a house. In Active Inference terms, the brain possesses high-precision priors for both faces and houses, but a strong prior *against* blended objects. The generative model adopts the "house" hypothesis, which perfectly suppresses the prediction errors from the left eye but leaves massive, accumulating prediction errors from the right eye (which is seeing a face). Eventually, these rising errors force the model to undergo a catastrophic update, violently flipping to the "face" hypothesis. Perception is the phenomenological experience of the winning hypothesis.

### 3. Sensory Attenuation: Why You Can't Tickle Yourself

If perception is the minimization of prediction error, how do we distinguish between something touching us (which we need to notice) and us touching ourselves (which we can ignore)?

The answer is **sensory attenuation**. When you reach out to touch an object, the motor cortex doesn't just send a command to your arm; it sends an **efference copy** (a corollary discharge) of that command to the sensory cortex. The sensory cortex uses this copy to predict exactly what the tactile feedback will feel like. Because the feedback is perfectly predicted, the prediction error is zero, and the sensation is attenuated—it feels dull.

This is why you cannot tickle yourself. Your brain perfectly predicts the sensory consequences of your own fingers, neutralizing the prediction error. If a machine introduces even a 200-millisecond delay between your movement and the tickle, the prediction fails, a prediction error is generated, and the sensation becomes ticklish again (Blakemore et al., 1999).

Sensory attenuation is direct structural evidence for the Active Inference claim that action and perception share the exact same inferential machinery.

### 4. Hallucinations as Aberrant Inference

If perception relies on a delicate balance between top-down predictions and bottom-up sensory evidence (prediction errors), what happens when that balance breaks?

Hallucinations can be formally understood as conditions where the brain's internal predictions are granted such massive mathematical **precision** that they completely override incoming sensory evidence. Powers et al. (2017) demonstrated that individuals prone to psychotic hallucinations are uniquely susceptible to *Pavlovian* auditory hallucination induction in the lab. They "hear" a tone that was previously paired with a checkerboard, even when the tone is entirely absent.

Their brains overweight top-down conceptual predictions relative to bottom-up acoustic reality.

## Clinical Connections

- **Schizophrenia**: Auditory hallucinations (hearing voices) may reflect a tragic failure of sensory attenuation. If the brain fails to send an efference copy during inner speech, the self-generated thoughts produce unattenuated prediction errors. The generative model, struggling to explain these unexpected internal auditory signals, mistakenly infers that "someone else is speaking."
- **Charles Bonnet Syndrome**: Many individuals suffering from macular degeneration or blindness experience vivid, complex visual hallucinations (seeing faces or geometric patterns). As bottom-up sensory input from the dying retina goes silent, the brain aggressively amplifies its own baseline visual predictions to fill the void, resulting in waking dreams.

## Conclusion

Predictive coding provides the precise neural implementation of Active Inference's most radical claim: perception is not passive recording, but active, hallucinated construction, continuously constrained by sensory prediction errors. Through phenomena like binocular rivalry and sensory attenuation, we see a brain relentlessly minimizing surprise. Module 04 examines the specific cognitive mechanisms—attention, neuromodulation, and precision weighting—that regulate the gain on these prediction errors to keep the brain tethered to reality.

## Further Reading

- Rao, R. P., & Ballard, D. H. (1999). Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience*, 2(1), 79-87.
- Blakemore, S. J., Wolpert, D. M., & Frith, C. D. (1999). Why can't you tickle yourself? *Neuroreport*, 10(11), 2351-2356.
- Powers, A. R., Mathys, C., & Corlett, P. R. (2017). Pavlovian conditioning–induced hallucinations result from overweighting of perceptual priors. *Science*, 357(6351), 596-600.
- Hohwy, J., Roepstorff, A., & Friston, K. (2008). Predictive coding explains binocular rivalry: An epistemological review. *Cognition*, 108(3), 687-701.
