# Module 05: Action — Motor Control and Active Inference

> **Course**: Active Inference 401 | **Unit**: Neuroscientific Frontiers | **Audience**: Advanced undergraduates / graduate students

## Learning Objectives

1. Analyze how **motor cortex and spinal cord** implement active inference through proprioceptive predictions.
2. Evaluate the **active inference account of movement** — action as fulfilling proprioceptive predictions rather than sending motor commands.
3. Examine the roles of **cerebellum, basal ganglia, and supplementary motor areas** in motor active inference.
4. Connect motor Active Inference to clinical motor disorders and rehabilitation.

## Introduction

The motor system has been the battleground for one of Active Inference's boldest claims: movements are not caused by commands sent from motor cortex, but by proprioceptive predictions fulfilled by spinal reflexes. This module examines the evidence.

> **Key Insight — Predictions Not Commands**: The classical motor neuroscience view treats M1 as a command center issuing movement instructions. Active Inference replaces this with a fundamentally different picture: M1 issuing predictions about where the body *should be*, and classical spinal reflex arcs doing the actual work of getting it there. The elegance of this proposal is that it uses the same computational architecture (predictions and prediction errors) for both perception and action.

## Key Concepts

### 1. Movement as Proprioceptive Prediction Fulfillment

The most radical claim of Active Inference for motor neuroscience: **movements are not caused by motor commands — they are caused by proprioceptive predictions that are fulfilled by spinal cord reflexes.**

The classical view: Motor cortex sends commands → spinal cord executes → muscles contract → movement occurs.

The Active Inference view: Motor cortex sends *predictions* about expected proprioceptive states (e.g., "my arm will be at position X") → these predictions descend to the spinal cord → spinal reflex arcs detect the *prediction error* between predicted and actual position → classical reflex arcs move the limb to fulfill the prediction.

**Key evidence**:

- Primary motor cortex neurons encode *intended trajectories* (predicted proprioceptive states) more than muscle activation patterns. Decoding studies show motor cortex represents where the limb *should be*, not how to get there
- The corticospinal tract terminates not only on motor neurons but extensively on spinal interneurons — consistent with modulating reflexes rather than directly commanding muscles
- Deafferentation studies: When proprioceptive feedback is removed (dorsal root section), movements become grossly inaccurate despite intact motor cortex — if M1 sent complete commands, proprioceptive feedback wouldn't be essential

> **Cross-Track Connection — Philosophical Foundations (Module 05)**: The "predictions not commands" framework resonates deeply with the enactivist and ecological traditions in philosophy of action — agency is not about issuing commands but about maintaining a sensorimotor loop. The philosophical argument against the "homunculus" (who in the brain sends the commands?) is dissolved when action is reconceptualized as prediction.

### 2. The Cerebellum as Forward Model

The cerebellum implements a critical component of motor active inference — the **forward model** that predicts the sensory consequences of motor actions:

**Cerebellar prediction**: Before a movement is executed, the cerebellum generates a prediction of what the sensory feedback will be (efference copy). This prediction is compared with actual feedback to compute a **motor prediction error** (signaled by climbing fibers from the inferior olive).

**Learning**: Motor prediction errors update the cerebellar forward model (through long-term depression at parallel fiber-Purkinje cell synapses), gradually improving motor predictions. This is why practice improves motor skill — the forward model becomes more accurate.

**Timing**: The cerebellum is critical for temporal prediction — predicting *when* the sensory consequence will arrive, not just *what* it will be. Cerebellar lesions produce timing deficits (dysmetria of time).

**Beyond motor control**: Recent evidence implicates the cerebellum in cognitive and social prediction — predictions about the consequences of thoughts and social interactions, not just movements. Cerebellar contributions to language, emotion, and social cognition may reflect this extended forward-modeling role.

> **Clinical Vignette — Cerebellar Ataxia**: Patients with cerebellar degeneration show increasingly inaccurate movements — not because they can't generate motor "commands" but because their forward model no longer accurately predicts movement consequences. They systematically over- or under-shoot targets (dysmetria), showing that the brain relies on predictive models even for seemingly simple reaching movements. Interestingly, these patients can partially compensate by relying more heavily on sensory feedback (increasing proprioceptive precision), though this makes movements slower and more effortful — a precision-based trade-off.

### 3. Basal Ganglia and Action Selection

The basal ganglia implement **policy selection** for motor active inference:

**Direct pathway**: Facilitates selected actions by disinhibiting the thalamus → "go" signal for the selected policy.
**Indirect pathway**: Suppresses competing actions by maintaining thalamic inhibition → "no-go" for alternative policies.
**Hyperdirect pathway**: Rapidly suppresses all actions → global "stop" — implementing the need to pause and re-evaluate when surprising events occur.

In Active Inference terms:

- Direct pathway = selecting the policy with lowest expected free energy
- Indirect pathway = suppressing policies with high expected free energy
- Hyperdirect pathway = resetting policy evaluation when a large prediction error arrives

**Dopamine**: D1 receptors on direct pathway neurons increase sensitivity to "go" signals (selecting the best policy). D2 receptors on indirect pathway neurons decrease sensitivity to "no-go" signals (reducing suppression of alternatives). The balance of D1/D2 signaling implements the precision of policy selection (γ).

**Vigor and movement speed**: The basal ganglia also control movement *vigor* — how fast and forceful an action is. Mazzoni et al. (2007) showed that Parkinson's patients can make accurate movements but choose to move slowly — a precision deficit affecting the "energization" of the selected policy, not the policy itself.

### 4. Supplementary Motor Areas and Sequencing

The supplementary motor area (SMA) and pre-SMA implement **action sequencing** — stringing individual actions into multi-step policies:

**Pre-SMA**: Plans the overall sequence structure — which actions come first, second, third. This corresponds to the generation of multi-step policies in Active Inference.

**SMA proper**: Executes the sequence in order — triggering each action at the right moment. This implements the step-by-step unfolding of the selected policy.

**Readiness potential**: The Bereitschaftspotential (RP) — a slow negative potential building up before voluntary movement — originates in SMA and represents the ramping up of precision for the upcoming action. The "decision to act" is the moment when policy precision exceeds a threshold.

> **Key Insight — Free Will and the RP**: Libet's famous experiment (1983) showing that the RP precedes conscious awareness of the "will to move" has been interpreted as evidence against free will. Active Inference offers a different interpretation: the RP is not a "decision" that precedes awareness — it is the gradual accumulation of precision for a policy that is about to be executed. Conscious awareness of the intention arises when precision crosses a threshold, not when the "decision" is made. The debate is reframed from "when does the homunculus decide?" to "when does policy precision peak?"

### 5. Saccadic Eye Movements as Active Inference

Eye movements provide an elegant model system for motor active inference:

**Saccades**: Rapid eye movements to a target are not ballistic commands — they are proprioceptive predictions fulfilled by oculomotor reflexes. The superior colliculus generates a prediction of the target location; brainstem circuits compute the prediction error between predicted and actual eye position; reflex arcs move the eyes to fulfill the prediction.

**Smooth pursuit**: Tracking a moving target requires continuously updating the prediction of target location. The frontal eye fields (FEF) generate predictions; the cerebellum provides the forward model of eye dynamics; visual cortex computes prediction errors.

**Fixation precision**: The precision of the oculomotor prediction determines fixation stability. Disorders of fixation (nystagmus, saccadic intrusions) can be understood as precision abnormalities in the oculomotor predictive model.

**Active vision**: Saccades are not just motor acts — they are epistemic actions (information-seeking). The brain generates saccades to regions of the visual scene with highest expected information gain (highest epistemic value). Foveal fixation converts low-resolution peripheral predictions into high-resolution foveal evidence, reducing uncertainty. Eye-tracking data show that saccade patterns closely match predictions from Active Inference models.

### 6. Sensory Attenuation and the Agency Signal

A crucial prediction of motor Active Inference: self-generated sensory consequences should be **attenuated** compared to identical externally generated stimuli.

**The tickling problem**: You can't tickle yourself because your forward model predicts the sensory consequences of your own touch. The prediction is subtracted from the actual sensation, leaving little prediction error. Externally generated tickling is unpredicted, producing large prediction errors and the ticklish sensation.

**Force matching**: When asked to reproduce a force applied to their finger, people systematically apply more force than was applied to them. The forward model predicts and attenuates their own force, so they must press harder to "feel" the same magnitude.

**Schizophrenia and agency**: Patients with schizophrenia show reduced sensory attenuation for self-generated stimuli — they can tickle themselves. Active Inference interpretation: the self-model's motor predictions are imprecise, so self-generated sensory consequences are not properly predicted and attenuated. This contributes to auditory hallucinations (interpreting inner speech as external because it is not predicted) and passivity experiences (feeling that one's own actions are externally controlled).

## Summary

Active Inference reconceptualizes movement as proprioceptive prediction fulfillment rather than motor command execution. The cerebellum provides the forward model (now extending beyond movement to cognition), the basal ganglia select policies with their direct/indirect/hyperdirect architecture, the SMA sequences actions, and spinal reflexes reduce proprioceptive prediction errors. Sensory attenuation — the cancellation of predicted sensory consequences — provides a key test of the framework, with clinical implications for schizophrenia and agency. This framework unifies motor control, motor learning, and motor disorders under a single inferential principle.

## Further Reading

- Adams, R. A. et al. (2013). Predictions not commands. *Brain Structure and Function*, 218(3), 611-643.
- Friston, K. J. et al. (2010). Action and behavior: A free-energy formulation. *Biological Cybernetics*, 102(3), 227-260.
- Wolpert, D. M. & Flanagan, J. R. (2001). Motor prediction. *Current Biology*, 11(18), R729-R732.
- Blakemore, S. J. et al. (2002). Abnormalities in the awareness of action. *Trends in Cognitive Sciences*, 6(6), 237-242.
- Mazzoni, P. et al. (2007). An implicit plan overrides an explicit strategy during visuomotor adaptation. *Journal of Neuroscience*, 27(25), 7847-7858.
