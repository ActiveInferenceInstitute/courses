#!/usr/bin/env python3
"""Generate questions.md and lab.md content for embodied cognition Active Inference course."""

import os

BASE = "/Users/4d/Documents/GitHub/courses/course_development/domains/active_inference_embodied"

SECTIONS = ["01_felt_sense", "02_living_presence", "03_intuitive_knowing", "04_moving_through_world"]
SUBMODULES = ["01_systems", "02_agents", "03_perception", "04_cognition", "05_action", "06_learning", "07_communication", "08_planning"]

SECTION_NAMES = {
    "01_felt_sense": "Felt Sense",
    "02_living_presence": "Living Presence",
    "03_intuitive_knowing": "Intuitive Knowing",
    "04_moving_through_world": "Moving Through World",
}

SUBMODULE_NAMES = {
    "01_systems": "Systems",
    "02_agents": "Agents",
    "03_perception": "Perception",
    "04_cognition": "Cognition",
    "05_action": "Action",
    "06_learning": "Learning",
    "07_communication": "Communication",
    "08_planning": "Planning",
}

# ============================================================================
# QUESTIONS DATA - 17 unique questions per section/submodule combination
# ============================================================================

QUESTIONS = {
    # ========================================================================
    # 01_FELT_SENSE
    # ========================================================================
    ("01_felt_sense", "01_systems"): [
        "How does the Markov blanket of the body correspond to the felt experience of having a skin boundary? Describe an exercise you could do right now to sense this boundary from the inside.",
        "In what ways does homeostatic regulation -- maintaining temperature, blood glucose, and pH -- constitute a form of bodily self-inference? How might you become aware of these regulatory processes through somatic attention?",
        "Damasio describes a nested hierarchy of life regulation from homeostasis to feelings to consciousness. How does each level contribute to the felt sense of being an integrated system rather than a collection of parts?",
        "What is the relationship between interoceptive prediction errors and the subjective experience of bodily discomfort? Provide an example from your own experience of a time when your body's felt sense signaled a systemic disruption.",
        "How does the concept of allostasis -- anticipatory regulation of set-points -- differ from simple homeostasis, and what does allostatic regulation feel like from the inside (e.g., the felt sense of hunger before a meal)?",
        "Thomas Fuchs argues that the body is simultaneously local and global -- a headache is both a neural event and a whole-organism experience. How does this insight change your understanding of what it means to be a feeling system?",
        "In a body scan meditation, you bring attention to each region of the body from feet to crown. How does this practice relate to the Active Inference concept of increasing precision on interoceptive signals?",
        "What is the proto-self as described by Damasio, and how does it relate to the generative model's deepest prior -- the prediction that 'I am a persisting, bounded system'?",
        "Compare the experience of dissociation or depersonalization with the Active Inference account of disrupted self-modeling. What might it feel like when the body's systemic self-inference breaks down?",
        "How do interoceptive sensors (baroreceptors, chemoreceptors, thermoreceptors) form the inward-facing surface of the body's Markov blanket? What kind of information do they provide that shapes the felt sense?",
        "In somatic therapy, clients sometimes report feeling 'not in their body' or 'fragmented.' How would you explain this phenomenological report using the language of self-organizing systems and Markov blankets?",
        "Design a brief somatic exercise (3-5 minutes) that would help a participant experientially grasp the difference between interoception and exteroception. Explain what Active Inference concepts the exercise illustrates.",
        "How does chronic stress disrupt the body's capacity to function as a coherent self-maintaining system? Describe the felt consequences in terms of prediction error and precision weighting.",
        "What role does the vagus nerve play in connecting visceral organs to the brain's generative model, and how might vagal tone affect the quality of one's felt sense?",
        "Compare the felt experience of a healthy body at rest with the felt experience during a panic attack. How do these two states differ in terms of free energy and prediction error at the systemic level?",
        "How might practices like cold water immersion or breath holding reveal the body's system boundaries through extreme interoceptive prediction error? What does such a practice teach about the Markov blanket?",
        "Reflect on a time when you became acutely aware of your body as a living, self-regulating system (e.g., during illness, intense exercise, or deep relaxation). What was the quality of that awareness, and how does it connect to Active Inference?",
    ],
    ("01_felt_sense", "02_agents"): [
        "Describe the felt difference between an action you initiated deliberately (raising your hand) and an involuntary bodily process (a heartbeat or a sneeze). What does this distinction reveal about embodied agency in Active Inference?",
        "Gallagher distinguishes between the sense of ownership (this body is mine) and the sense of agency (I am the author of this action). Design a brief somatic exercise that would help someone experientially distinguish these two senses.",
        "What does Maxine Sheets-Johnstone mean by the felt horizon of 'I can,' and how does this somatic apprehension of one's action capacities correspond to the agent's policy space in Active Inference?",
        "How might trauma disrupt the felt sense of agency? Describe what it might feel like to lose confidence in one's own motor predictions, using the language of prediction error and generative model collapse.",
        "In Active Inference, the sense of agency arises when motor prediction errors are minimal -- when the body accurately predicts the sensory flow of its own actions. Describe an everyday experience where this match is palpable.",
        "The pre-motor felt intention -- the body's readiness to move before movement begins -- is a key phenomenological marker of agency. How would you guide someone to notice this intention during a slow movement exercise?",
        "What is autonomic agency, and how does the act of taking a deep breath to calm oneself illustrate interoceptive agency within the Active Inference framework?",
        "Compare the felt quality of active touch (you exploring an object with your fingers) with passive touch (someone else touching your hand). How does agency transform the quality of sensation?",
        "In alien hand syndrome, patients experience purposeful actions they do not feel they initiated. How does this clinical condition illuminate the relationship between motor predictions and the felt sense of being an agent?",
        "How does the concept of efference copy -- the brain's prediction of the sensory consequences of its own motor commands -- relate to the ordinary, taken-for-granted feeling that 'I am the one who moved'?",
        "Describe how a somatic practice such as yoga or tai chi cultivates a refined sense of agency by slowing down the action-perception loop and making motor predictions experientially accessible.",
        "What is the relationship between learned helplessness (the chronic sense that one's actions do not produce expected results) and the Active Inference account of collapsed motor predictions?",
        "In what ways does the sense of agency extend beyond skeletal movement to include emotional self-regulation, breath control, and autonomic modulation? Provide a felt-sense example for each.",
        "How might the practice of Focusing (Gendlin) reveal subtle dimensions of agency -- specifically, the sense that one can attend to, unfold, and shift one's own bodily experience?",
        "Describe the felt phenomenology of a moment when your sense of agency was disrupted -- when your body did something unexpected or when an action felt alien. What was the quality of that surprise?",
        "How does the developmental emergence of agency in infancy (first reaching, first grasping, first stepping) illustrate the progressive building of a generative model's motor predictions?",
        "Reflect on the relationship between agency and vulnerability. When the body senses it cannot act effectively (e.g., during physical restraint or paralysis), what happens to the felt sense of self?",
    ],
    ("01_felt_sense", "03_perception"): [
        "Barrett's concept of affective realism holds that the body's physiological state colors perception before any conscious evaluation occurs. Describe a time when your mood measurably altered what you perceived in your environment.",
        "How does the interoceptive prediction that you are unsafe transform visual perception -- making neutral faces appear threatening and ambiguous shadows seem sinister? Explain using the vocabulary of precision weighting.",
        "Design a brief experiential exercise (3-5 minutes) that demonstrates how shifting bodily state (e.g., from tense to relaxed through deep breathing) changes the quality of visual or auditory perception.",
        "What does Merleau-Ponty mean when he says we always perceive from within our flesh? How does the body's current state of fatigue, vitality, or illness shape the felt quality of a perceived sunset or piece of music?",
        "In Active Inference, perception minimizes prediction error by jointly optimizing exteroceptive and interoceptive models. How does this joint optimization explain why the same room can feel welcoming at one moment and oppressive at another?",
        "Describe the somatic marker that accompanies your perception of a familiar person versus a stranger. Where in your body do you register the difference, and how does this bodily response shape what you see?",
        "Phantom limb pain illustrates how the generative model continues to predict sensory input from a missing limb. What does this tell us about the relationship between the body's felt sense and perceptual experience?",
        "How does depersonalization -- a state in which the world appears flat, distant, and unreal -- reveal the importance of interoceptive precision for creating vivid, felt perceptual experience?",
        "In somatic therapy, a client may discover that chronic muscular tension in the neck alters how they perceive faces (as more threatening or stern). Explain this phenomenon through the lens of embodied perception and prediction error.",
        "What is the relationship between respiratory state (calm deep breathing versus shallow anxious breathing) and perceptual clarity? How would Active Inference account for this connection?",
        "How does mindful eating -- attending fully to the taste, texture, and temperature of a single bite of food -- illustrate the difference between perception driven by top-down prediction versus perception enriched by bottom-up sensory evidence?",
        "Describe how a body scan meditation changes the quality of perception over the course of a session. What happens to the richness and specificity of what you perceive as interoceptive precision increases?",
        "Anil Seth proposes that consciousness is a 'controlled hallucination' shaped by interoceptive inference. How does this view challenge the common assumption that we passively receive sensory information from the world?",
        "How do somatic practices like Alexander Technique or Feldenkrais change perceptual experience by reorganizing the body's postural habits and thereby altering the generative model's baseline predictions?",
        "Describe the felt tone that accompanies perception of an object that holds personal significance (a childhood toy, a photograph of a loved one). How is this felt tone different from perception of a neutral object?",
        "In what way does the concept of 'aesthetic arrest' -- being stopped in one's tracks by beauty -- illustrate a sudden, intense alignment between interoceptive and exteroceptive prediction in the generative model?",
        "Reflect on how chronic pain alters the entire perceptual field -- not just the sensation of pain itself, but the quality of colors, sounds, and spatial experience. What does this reveal about the systemic nature of embodied perception?",
    ],
    ("01_felt_sense", "04_cognition"): [
        "How do Mark Johnson's image schemas (CONTAINER, BALANCE, SOURCE-PATH-GOAL) demonstrate that abstract thought is rooted in bodily experience? Choose one schema and describe the felt sense that underlies it.",
        "Damasio's Iowa Gambling Task showed that bodily signals guide cognitive decisions before conscious awareness. How does the felt sense 'lead' cognition in this experiment, and what Active Inference mechanism explains this?",
        "Design a brief exercise that demonstrates how posture changes cognitive style. What would you predict happens to the quality of problem-solving when someone shifts from a slumped to an upright posture?",
        "What does the embodied metaphor 'understanding is grasping' reveal about the neural relationship between physical manipulation and conceptual comprehension? How might you feel this connection in your own hands during learning?",
        "How do gut feelings function as cognitive shortcuts (Gigerenzer's 'fast and frugal heuristics') that bypass extensive deliberation? Describe a situation where your gut feeling arrived before your rational analysis.",
        "In what way does the felt sense of confusion -- the subtle nausea, the tightening around the eyes, the sense of cognitive fog -- serve as an informative signal within the Active Inference framework?",
        "How does the extended mind thesis (Clark and Chalmers) relate to the embodied felt sense of thinking? When a mathematician paces while solving a problem, what role does the body's movement play in cognition?",
        "Describe the somatic signature of the 'aha' moment -- the felt shift that accompanies sudden insight. Where in the body do you typically experience this, and what Active Inference process does it reflect?",
        "How does breath regulation (e.g., slow diaphragmatic breathing) change cognitive clarity and the quality of decision-making? Explain using the concepts of autonomic state and precision weighting on interoceptive signals.",
        "Lakoff and Johnson argue that morality is structured by embodied metaphors (purity/contamination, balance/fairness). How does the felt sense of moral disgust -- the visceral revulsion at injustice -- support this claim?",
        "In what way does gesturing while thinking serve as a cognitive resource rather than merely an expressive accompaniment? Describe an experiment you could try right now to test this embodied cognition claim.",
        "How does emotional state bias cognitive processing? Provide a concrete example of how anxiety narrows the scope of thought and how calm broadens it, using the language of precision and prediction error.",
        "What role does the felt sense play in creative cognition -- the generation of novel ideas, metaphors, and artistic expressions? How might somatic practices enhance creative thinking?",
        "Compare the cognitive experience of solving a problem while sitting still versus while walking outdoors. What does the difference in felt quality tell us about the body's contribution to cognitive processing?",
        "How does the somatic marker hypothesis explain the poor decision-making observed in patients with ventromedial prefrontal cortex damage who lose access to bodily signals during reasoning?",
        "Describe how a practice of tracking the felt sense of thinking (noticing bodily sensations during cognitive activity) might change your relationship to thoughts and improve metacognitive awareness.",
        "Reflect on a complex decision you have made. In retrospect, to what extent was your final choice guided by rational analysis versus the felt sense in your body? What does this reveal about embodied cognition?",
    ],
    ("01_felt_sense", "05_action"): [
        "How does Active Inference dissolve the classical perceive-think-act sequence by showing that action is itself a form of inference? Describe a moment when your body acted to change what you felt before conscious deliberation intervened.",
        "Nico Frijda proposed that emotions are fundamentally action tendencies. Describe the felt bodily readiness of fear (preparation for flight), anger (preparation for confrontation), and grief (collapse inward). Where in the body do you feel each?",
        "What are incomplete defensive responses (Peter Levine), and how do they manifest as chronic somatic holding patterns? Describe the felt quality of bracing, holding, or constriction that persists long after a threatening event.",
        "How do somatic practices like yoga, tai chi, and Feldenkrais generate new sensorimotor prediction errors that challenge the body's habitual motor priors? Describe the felt experience of releasing a long-held postural pattern.",
        "What is the difference between instrumental action (reaching for a glass) and expressive action (a gesture, a facial expression, a sigh)? How does Active Inference account for both, and what role does the felt sense play in each?",
        "Describe the felt experience of a spontaneous bodily impulse -- a desire to stretch, shift position, or take a deep breath. How does following such an impulse differ from suppressing it, and what does Active Inference say about this?",
        "How does crying function as a motor policy for resolving the autonomic prediction error of grief? Describe the felt progression from emotional pressure to tears to the relief that often follows.",
        "In Somatic Experiencing therapy, a client is guided to slowly complete a defensive movement that was interrupted during trauma. Describe what the 'felt shift' of completion might involve -- trembling, release, warmth.",
        "How does the felt sense of an action tendency (the pull to approach, the urge to withdraw) differ from the cognitive decision to act? Which arrives first in your experience, and what does this tell us about embodied agency?",
        "Describe the relationship between breath and action in a practice like yoga or martial arts. How does the coordination of breath with movement illustrate the active inference account of somatic action as interoceptive regulation?",
        "What does it mean to say that the body 'sculpts its own interoceptive landscape' through action? Provide an example from your own experience where a physical action changed how you felt inside.",
        "How do chronic tension patterns (tight jaw, raised shoulders, held breath) represent persistent motor policies that the body maintains to manage predicted interoceptive states? What might it take to update these policies?",
        "Compare the felt quality of effortful, deliberate action (learning a new dance step) with the felt quality of fluid, automatic action (walking). What has changed in the generative model between these two states?",
        "In what ways does massage or bodywork facilitate the updating of somatic holding patterns? Describe the felt experience of a muscle releasing tension that it has held for a long time.",
        "How does the concept of 'action as self-fulfilling prophecy' (the body making its predictions come true through movement) apply to the everyday act of reaching for and lifting a cup of coffee?",
        "Describe how a shaking or trembling response (as seen in animals after threat) functions as the body's natural mechanism for completing an interrupted stress response and reducing interoceptive free energy.",
        "Reflect on a somatic practice you have engaged in (dance, sport, yoga, martial arts, or any form of deliberate movement). How did sustained practice change the felt quality of action over time?",
    ],
    ("01_felt_sense", "06_learning"): [
        "A beginning meditator feels almost nothing -- a vague blur of sensation. After months of practice, the same person distinguishes anxiety from excitement, tension from ease, warmth from restlessness. What has the generative model learned?",
        "How does interoceptive discrimination learning -- the progressive differentiation of somatic signals -- transform 'feeling bad' into a rich vocabulary of distinct felt senses (tight chest, heavy limbs, hot face)?",
        "Describe the process of somatic memory: how does a childhood experience of humiliation become encoded as a chronic postural pattern (collapsed chest, lowered gaze) that persists into adulthood?",
        "What is Hebbian learning in the interoceptive system, and how does repeated pairing of a social context (criticism) with a bodily state (stomach constriction) create the embodied prior that constitutes dread?",
        "How does memory reconsolidation provide a window for somatic reconditioning? Describe how a feared situation encountered in a context of new bodily safety might update the generative model's predictions.",
        "What is interoceptive accuracy (the ability to perceive one's own heartbeat, breathing, or gastric signals), and how does it correlate with emotional awareness and decision-making quality?",
        "Design a one-week interoceptive differentiation journal practice. What specific prompts would you use to help someone progressively refine their felt-sense vocabulary over seven days?",
        "How does biofeedback (such as heart rate variability training) strengthen the connection between voluntary action and autonomic outcome, and what does the felt experience of gaining autonomic control resemble?",
        "Describe the process by which emotional conditioning creates maladaptive somatic priors. How might a single traumatic event create a bodily 'prediction' that similar situations will always be dangerous?",
        "How does the concept of neuroplasticity support the claim that the body's generative model can be deliberately retrained through practices like Somatic Experiencing, EMDR, or Sensorimotor Psychotherapy?",
        "What does Peter Levine mean when he says the body itself is the memory? How does this contrast with the common assumption that memories are stored exclusively in the brain?",
        "Describe the felt difference between a freshly learned somatic skill (the first time you held a yoga pose correctly) and a deeply embodied skill (a pose that now feels like second nature). What has changed in the generative model?",
        "How does autonomic flexibility -- the capacity to smoothly transition between sympathetic arousal and parasympathetic calm -- relate to the body's learning capacity in the Active Inference framework?",
        "In what ways does the practice of body scanning over weeks or months progressively refine the precision of interoceptive predictions? Describe the learning trajectory from coarse to fine-grained somatic awareness.",
        "How might maladaptive somatic learning (such as chronic pain sensitization) be understood as the generative model learning 'too well' -- creating prediction errors that amplify rather than resolve suffering?",
        "Describe how the felt sense changes as one develops expertise in a somatic practice (meditation, dance, martial arts). What does the transition from novice to expert feel like from the inside?",
        "Reflect on a time when you unlearned a somatic pattern -- a habitual tension, a reactive flinch, a postural habit. What was the process like, and what Active Inference concepts does it illustrate?",
    ],
    ("01_felt_sense", "07_communication"): [
        "Describe the experience of interoceptive resonance -- sitting with someone who is grieving and feeling heaviness arise in your own body without any words being exchanged. What Active Inference process is at work?",
        "How does vocal prosody (rhythm, pitch, volume, tonal quality) communicate directly to the listener's body, bypassing semantic processing? What does Stephen Porges's polyvagal theory say about why a calm voice produces a felt sense of safety?",
        "Gendlin observed that finding the right words for a felt sense produces a 'felt shift' -- a bodily release. How does this 'carrying forward' process correspond to free energy reduction in the generative model?",
        "What is affect attunement (Daniel Stern), and how does a caregiver's cross-modal matching of an infant's felt intensity constitute a form of embodied communication that precedes language?",
        "Design a brief exercise in empathic listening: while someone speaks, attend exclusively to the sensations arising in your own body. How might this somatic listening provide information that exceeds what the speaker's words convey?",
        "In what way does the concept of a shared Markov blanket illuminate the experience of deep interpersonal connection -- the sense that two bodies are resonating as a coupled system?",
        "How does the body communicate what language cannot? Describe a situation where silence, touch, shared breathing, or co-present stillness conveyed more meaning than any verbal formulation could.",
        "In Focusing partnerships, a listener accompanies a focuser without interpreting or advising. How does this relational container amplify the focuser's interoceptive precision and create conditions for felt-sense unfolding?",
        "Describe the somatic experience of communicating from an authentic place versus from a socially scripted persona. What feels different in the body when expression aligns with felt truth versus when it diverges?",
        "How do facial micro-expressions function as cross-Markov-blanket signals that transmit felt states between organisms in milliseconds? Why are these signals often more reliable than deliberate verbal communication?",
        "What is the relationship between the body's autonomic state (ventral vagal calm versus sympathetic arousal) and the quality of communication? How does your own nervous system state affect your capacity to listen and respond empathically?",
        "Describe how the practice of speaking from the felt sense -- pausing, noticing what is alive in the body, and letting words arise from that place -- differs from speaking from cognitive rehearsal. What changes in the quality of communication?",
        "How does therapeutic touch (in massage, Reiki, or simply holding someone's hand) communicate safety and regulate the recipient's nervous system through direct cross-blanket somatic signaling?",
        "In group settings, how does collective somatic resonance (a shared hush, a wave of laughter, the tension in a room) illustrate the alignment of multiple generative models through embodied channels?",
        "What role does breath play in interpersonal communication? How does the synchronization of breathing between conversation partners both reflect and deepen the alignment of their generative models?",
        "Describe the felt difference between hearing someone describe an experience intellectually versus hearing them speak from a place of embodied feeling. How does the listener's body respond differently in each case?",
        "Reflect on a communication experience where embodied signals (tone of voice, posture, facial expression) contradicted verbal content. Which did your body trust, and what does this reveal about the primacy of somatic communication?",
    ],
    ("01_felt_sense", "08_planning"): [
        "Describe the experience of somatic simulation: when you imagine a future scenario (a job interview, a vacation, a difficult conversation), what does your body do? Where do you feel the imagined future?",
        "How does allostatic anticipation -- the body's proactive preparation for expected future demands -- constitute a deep, pre-cognitive form of planning? Provide an example from daily life.",
        "In Active Inference, planning is the evaluation of policies based on expected free energy. How does the felt sense of a 'good plan' (opening, forward-leaning energy) differ from the felt sense of a 'bad plan' (constriction, pulling back)?",
        "Design a somatic decision-making exercise: vividly imagine two possible futures and track the bodily sensations that arise for each. How might this body-based evaluation complement rational analysis?",
        "What is the felt sense of temporal horizon? Compare the somatic quality of planning something immediate (reaching for a glass) with planning something distant (imagining retirement). Where and how do they differ in the body?",
        "How does worry function as maladaptive embodied planning in Active Inference terms? What happens to the body when the generative model generates high-precision predictions of negative outcomes that cycle without resolution?",
        "Describe the relationship between somatic rehearsal in athletes (a diver feeling each twist before stepping onto the board) and the Active Inference account of planning as running forward simulations in the generative model.",
        "How does the body integrate past experience (somatic memory), present state (current interoceptive condition), and anticipated future (simulated interoceptive consequences) into a coherent embodied plan?",
        "In what way does Gendlin's concept of felt-sense forward movement apply to planning? When the body leans toward a future, what Active Inference computation is this phenomenological forward-movement expressing?",
        "Describe the felt difference between planning from anxiety (constricted, urgent, tunnel-visioned) and planning from presence (open, spacious, responsive). How does the body's autonomic state shape the planning process?",
        "How does sleep and dreaming contribute to embodied planning? What might the body be doing during sleep that relates to the consolidation and refinement of the generative model's future-oriented predictions?",
        "Compare top-down cognitive planning (making a pros-and-cons list) with bottom-up somatic planning (noticing which option the body opens toward). In what situations might the somatic approach be more reliable?",
        "How do somatic practices like body scanning or breath awareness improve the quality of planning by recalibrating the precision of interoceptive signals that the generative model uses to evaluate future policies?",
        "Describe the phenomenology of regret: the felt sense that arises when the body simulates a past decision and generates the interoceptive prediction errors of 'what could have been.' How does this relate to planning for the future?",
        "What role do emotions play in constraining the planning process? How does the felt sense of fear eliminate certain policies from consideration while the felt sense of excitement opens others?",
        "In what way does setting an intention during meditation (feeling into what the body wants to move toward) constitute a form of embodied planning that operates without verbal deliberation?",
        "Reflect on a major life decision. To what extent did your body 'know' the right direction before your mind had finished deliberating? What does this experience reveal about the relationship between felt sense and planning?",
    ],
    # SECTION-LEVEL for 01_felt_sense
    ("01_felt_sense", None): [
        "How does Gendlin's concept of the felt sense -- a pre-verbal, holistic bodily knowing -- correspond to the Active Inference account of the body as a generative model predicting its own internal states?",
        "Describe the relationship between interoceptive prediction error and the subjective experience of emotion. When your body registers surprise at its own internal state, what do you feel?",
        "How do Damasio's somatic markers function as embodied priors that guide decision-making before conscious deliberation? Provide a personal example of a gut feeling that preceded rational analysis.",
        "What is the role of precision weighting in determining emotional intensity? How does high precision on interoceptive signals produce vivid felt experience, while low precision produces numbness or alexithymia?",
        "Describe Gendlin's Focusing technique as a practice of interoceptive free energy minimization. What happens in the body during the characteristic 'felt shift' that Focusing practitioners report?",
        "How does Peter Levine's Somatic Experiencing therapy work with the felt sense to resolve trauma held in the body? Describe the Active Inference mechanism underlying the release of chronic defensive postures.",
        "What is the difference between a sensation (localized, specific), an emotion (categorized, named), and a felt sense (holistic, pre-verbal, implicit)? Design an exercise to help someone experience each.",
        "How does the body's generative model use interoceptive signals to construct the felt tone that colors all experience? Why is there no such thing as emotionally neutral perception?",
        "Describe how chronic stress, anxiety, or trauma disrupts the felt sense by biasing precision weighting toward threat-related interoceptive signals. What does this disruption feel like from the inside?",
        "How does the practice of body scanning train the generative model to parse interoceptive signals with greater precision, transforming vague bodily awareness into differentiated felt experience?",
        "In what way does the felt sense exceed what language can articulate? Describe a bodily knowing you have experienced that resisted translation into words.",
        "How do different contemplative traditions (Buddhist vipassana, Gendlin's Focusing, somatic therapy) approach the felt sense differently while converging on the same underlying phenomenon of interoceptive awareness?",
        "Describe the felt sense of a situation that is going well versus a situation that is going badly, before any cognitive analysis has occurred. Where in the body do these assessments register?",
        "How does interoceptive inference -- the brain's predictive modeling of internal bodily states -- provide the computational foundation for what Gendlin called the body's 'implicit intricacy'?",
        "What is the relationship between the felt sense and the immune system? How might practices that enhance interoceptive awareness also influence physiological resilience?",
        "Describe how the felt sense functions as a compass for authenticity -- a bodily signal that registers alignment or misalignment between one's actions and one's deeper values or needs.",
        "Reflect on the central claim of this unit: that the body is not a passive container for the mind but an active generative model continuously predicting its own states. How does attending to the felt sense support or challenge this claim?",
    ],

    # ========================================================================
    # 02_LIVING_PRESENCE
    # ========================================================================
    ("02_living_presence", "01_systems"): [
        "How does Varela and Maturana's concept of autopoiesis -- self-making -- reframe the living body as a system whose awareness arises from its continuous self-production rather than from a separate consciousness?",
        "In sitting meditation, one of the first discoveries is the boundary between self and world. How does the experiential discovery of this boundary correspond to the Markov blanket formalism in Active Inference?",
        "Describe the felt quality of the body's autonomic self-regulation (heartbeat, breathing, digestion) when you sit quietly and simply witness it. What does it mean to say that this ceaseless activity is the foundation of presence?",
        "How does Stephen Porges's polyvagal theory connect ventral vagal activation to the state of calm, alert presence that contemplative traditions describe as the foundation of mindful awareness?",
        "In what way is the Markov blanket of the living body not a wall but a breathing membrane? Describe the felt experience of inhalation (drawing the world inside) and exhalation (giving something back) as an illustration of this dynamic boundary.",
        "How does chronic sympathetic arousal (fight-or-flight) disrupt the systemic foundation of living presence? What does it feel like when the body's self-regulatory predictions have been chronically violated?",
        "Design a 5-minute somatic exercise that helps someone experientially discover the body-as-system -- the integrated, undivided whole whose many processes converge in a single act of being present.",
        "What is the difference between trying to be present (a mental effort) and noticing that presence is already the system's fundamental mode of being? How does this distinction change the quality of meditation practice?",
        "How does the concept of the body as a nested hierarchy of systems (cells within organs within organism) relate to the phenomenological experience of attending to a sensation that is simultaneously local and global?",
        "Describe how mindfulness-based interventions (MBSR, MBCT) recalibrate the autonomic nervous system's predictions about internal safety, restoring the ventral vagal baseline from which living presence emerges.",
        "In Active Inference, the organism does not first exist and then become aware -- awareness is an aspect of its self-sustaining activity. How does this insight transform your understanding of what it means to meditate?",
        "What does the concept of circular causality in autopoiesis (the cell's membrane enables the processes that produce the membrane) feel like from the inside? How is this self-sustaining loop experientially accessible?",
        "Describe the phenomenological difference between scattered attention (the system dispersed across competing demands) and gathered attention (the system unified in present-moment awareness). What has changed at the systemic level?",
        "How does the quality of sleep relate to the body's capacity for systemic presence during waking hours? What Active Inference mechanisms connect restorative sleep to enhanced mindful awareness?",
        "In what way does the experience of deep relaxation (savasana in yoga, progressive muscle relaxation) reveal the body's systemic self-organization by removing the noise of chronic tension and allowing the system's natural coherence to emerge?",
        "How might the practice of listening to internal sounds (heartbeat, breath, digestive murmur) during meditation serve as a direct encounter with the body's autopoietic self-maintenance?",
        "Reflect on a moment when you felt profoundly present -- fully alive, integrated, and aware. What was the quality of your body's systemic organization in that moment, and how does it connect to the Active Inference account of living systems?",
    ],
    ("02_living_presence", "02_agents"): [
        "In mindfulness practice, the sense of a controlling agent often dissolves into the bare experience of processes occurring. How does Active Inference account for this shift from 'I am watching my breath' to 'breathing is happening'?",
        "During body-awareness meditation, the body makes micro-adjustments without conscious decision. How do these spontaneous actions reveal embodied agency operating beneath the threshold of deliberate will?",
        "How does the concept of minimal (pre-reflective) agency relate to the experience of present-moment awareness? What does it feel like to be an agent without the narrative layer of self-commentary?",
        "Describe the felt quality of intention as it arises in meditation. When you decide to return attention to the breath, where does the impulse originate? Is it experienced as 'I decide' or 'a decision arises'?",
        "How does sustained mindful practice transform the sense of agency from a fixed, controlling self to a fluid, moment-to-moment emergence? What Active Inference mechanism accounts for this transformation?",
        "In walking meditation, each step is a discrete act of agency. Describe the felt quality of lifting, moving, and placing the foot when performed with full present-moment attention.",
        "How does the practice of 'non-doing' (wu wei in Taoist tradition) challenge the Western assumption that agency requires a deliberate controller? How does Active Inference model effortless action?",
        "What happens to the sense of agency during states of flow or deep absorption? How does the felt quality of action change when the agent and the activity become phenomenologically indistinguishable?",
        "Describe the bodily experience of volition arising in meditation -- the moment between 'sitting still' and 'choosing to move.' What does this liminal moment reveal about the nature of embodied agency?",
        "How does the polyvagal state of the body (ventral vagal calm vs. sympathetic arousal vs. dorsal vagal shutdown) influence the quality and scope of felt agency? When the body feels safe, how does agency expand?",
        "In what way does present-moment awareness reveal that agency is not a fixed property of the self but an ongoing inferential achievement of the embodied organism? Provide a first-person phenomenological example.",
        "How does the mindful observation of involuntary processes (the heartbeat, peristalsis, blinking) change one's relationship to voluntary action? Does witnessing automaticity deepen the appreciation of deliberate agency?",
        "Describe the felt transition between effortful agency (straining to maintain focus) and effortless agency (attention resting naturally on the breath). What has shifted in the body's generative model?",
        "How do contemplative practices cultivate 'responsive agency' -- the capacity to act from presence rather than reactivity? Describe the somatic difference between a reactive impulse and a present-centered response.",
        "What role does bodily stillness play in revealing the subtlest dimensions of agency? When external movement ceases, what internal movements (breath, pulse, subtle muscular shifts) become experientially prominent?",
        "How does the practice of noting (silently labeling 'thinking,' 'feeling,' 'hearing' during meditation) reveal the constructive nature of the sense of agency -- showing that 'the observer' is itself a product of the generative model?",
        "Reflect on the paradox of meditative agency: the more you try to be present, the more you distance yourself from presence. How does Active Inference resolve this paradox through the concept of precision optimization rather than effortful control?",
    ],
    ("02_living_presence", "03_perception"): [
        "In open awareness meditation, sensory experience arrives before categorization. Describe the felt quality of perceiving bare sensory evidence -- sound, pressure, temperature -- before the generative model narrates it.",
        "During mindful eating, attending fully to a single raisin reveals how much ordinary perception is top-down prediction. How does living presence restore precision weighting on bottom-up sensory signals?",
        "How does the practice of choiceless awareness (receiving whatever arises without selecting or rejecting) relate to the Active Inference concept of reducing excessive top-down precision and allowing sensory evidence to update the model?",
        "Describe the felt difference between habitual perception (walking through your kitchen without really seeing it) and present-moment perception (suddenly noticing the play of light on the counter as if for the first time).",
        "How does breath awareness function as an anchor that recalibrates the entire perceptual field? What changes in the quality of vision, hearing, and touch when the breath becomes the primary object of attention?",
        "In vipassana meditation, practitioners develop the capacity to perceive impermanence directly -- to feel sensations arising and passing moment by moment. How does this relate to the Active Inference account of temporal precision?",
        "Describe the phenomenology of perceptual freshness -- the state meditators call 'beginner's mind.' What has changed in the generative model's precision architecture when the world appears vivid, alive, and novel?",
        "How does body position (sitting versus lying versus standing) change the quality of perceptual presence? Design a brief exercise that demonstrates how postural shifts alter what and how we perceive.",
        "What is the relationship between anxiety and perceptual narrowing? How does present-moment awareness reverse this narrowing by reducing the precision on threat-related predictions and broadening the perceptual field?",
        "In nature meditation (sitting outdoors with open awareness), perception often becomes richer and more spacious than in indoor settings. How might the environmental complexity of natural settings support more balanced precision weighting?",
        "Describe the felt quality of synesthetic perception -- moments when sensory modalities seem to blur (hearing a color, feeling a sound). How does deep present-moment awareness sometimes produce these cross-modal experiences?",
        "How does the practice of slow, deliberate looking (contemplating a flower, a stone, or a candle flame for several minutes) change the relationship between perceiver and perceived? What happens to the boundary?",
        "In what way does fatigue alter the quality of present-moment perception? Describe the felt difference between perceiving the world through a rested body versus an exhausted one, using Active Inference vocabulary.",
        "How does the concept of 'bare attention' in Buddhist psychology map onto the Active Inference framework? Is it possible to perceive without prediction, or is bare attention itself a refined form of prediction?",
        "Describe the perceptual effect of silence. When you sit in a truly quiet environment, what happens to the quality of hearing? How does the absence of expected auditory input change the generative model's predictions?",
        "How do contemplative traditions use sensory deprivation (darkness retreats, silent retreats) to strip away habitual perceptual predictions and reveal the generative model's constructed nature?",
        "Reflect on a moment of perceptual awe -- seeing something that stopped you in your tracks. What happened to the relationship between the body's interoceptive state and the exteroceptive perception in that moment?",
    ],
    ("02_living_presence", "04_cognition"): [
        "Varela, Thompson, and Rosch argued that cognition is not the manipulation of abstract symbols but the embodied activity of a living system. How does present-moment awareness of your own thinking process support this claim?",
        "Describe the somatic signature of a thought arising during meditation. Before you identify its content, where in the body does the thought register -- as a subtle tension, a shift in breathing, a felt pull?",
        "What is cognitive decentering (observing thoughts as mental events rather than truths), and how does Active Inference explain it through the concept of meta-cognitive precision weighting?",
        "How does the practice of thought labeling ('planning,' 'remembering,' 'judging') during meditation develop the capacity to observe the generative model's predictions without being captured by their content?",
        "Describe the felt difference between rumination (replaying the past) and present-moment awareness. What happens in the body when the generative model detaches from current sensory evidence and loops through counterfactual simulations?",
        "How does worry (rehearsing the future) relate to excessive reliance on deep temporal priors at the expense of current sensory likelihood? What somatic signals indicate that the mind has left the present?",
        "In Mindfulness-Based Cognitive Therapy (MBCT), patients learn to detect somatic markers of depressive patterns before the full syndrome develops. Describe the early bodily warning signs that might precede a cognitive downward spiral.",
        "How does anchoring attention on the breath create a stable reference frame from which thoughts can be observed as predictions rather than realities? Describe the felt quality of this grounded observational stance.",
        "What does the enactive tradition mean when it says 'everything said is said by someone'? How does this insight change the relationship between cognition and the embodied present?",
        "Describe the phenomenon of 'thinking about thinking' (meta-cognition) as it is experienced somatically during meditation. What does the observing awareness feel like in the body?",
        "How does present-moment awareness transform the cognitive landscape by enabling the practitioner to assign reduced precision to thought content while increasing precision on the process of thinking itself?",
        "In what way does sustained meditation practice change the relationship between thoughts and emotions? Describe how the somatic charge of thoughts (anxiety, excitement, sadness) diminishes as meta-cognitive capacity develops.",
        "How does the concept of the specious present (Husserl's 2-3 second window of lived temporal experience) relate to the balance between counterfactual cognitive depth and present-moment grounding?",
        "Describe the cognitive quality of equanimity -- the capacity to register experience fully without being captured by it. What has changed in the generative model's precision architecture to enable this balanced awareness?",
        "How does walking meditation combine present-moment kinesthetic awareness with cognitive presence, preventing the kind of disembodied thinking that characterizes rumination?",
        "Compare the felt quality of a thought that arises from genuine present-moment insight (a fresh perception, a spontaneous understanding) with a thought that arises from habitual cognitive patterns (worry, self-criticism). How do they differ somatically?",
        "Reflect on the claim that 'the deepest cognitive freedom comes not from thinking different thoughts but from changing one's relationship to thinking itself.' How does your contemplative experience support or challenge this?",
    ],
    ("02_living_presence", "05_action"): [
        "Merleau-Ponty described the body as our 'vehicle of being-in-the-world' through motor intentionality. How does mindful, slowed-down movement make this motor intentionality directly experienceable?",
        "Describe the felt experience of raising your hand very slowly -- feeling the initial impulse in the shoulder, the engagement of muscles, the streaming proprioceptive feedback. What does this reveal about action as continuous inference?",
        "How does Active Inference reframe action from 'response to perception' to 'self-fulfilling prediction'? Describe the felt quality of the body making its predictions come true through deliberate movement.",
        "In tai chi, a single gesture is extended over thirty seconds. How does this temporal decompression reveal the micro-structure of the action-perception loop that is normally invisible in rapid, habitual movement?",
        "What is the relationship between efference copies (predicted sensory consequences of action) and the moment-to-moment sense of agency during mindful movement? Describe the felt match between prediction and experience.",
        "How does walking meditation cultivate refined sensory awareness of the prediction-verification cycle in each step? Describe what happens when you feel the 'pull' of the predicted foot-ground contact before it occurs.",
        "Describe the felt quality of motor intentionality -- the body's reaching toward objects, spaces, and possibilities before conscious deliberation begins. How does mindful awareness illuminate this pre-reflective reaching?",
        "Gibson's concept of affordances takes on new meaning in the context of living presence. How does mindful awareness create a contemplative pause between perceiving an affordance and acting on it?",
        "Describe the felt difference between habitual action (reaching for your phone automatically) and mindful action (reaching with full present-moment awareness). What changes in the body's experience?",
        "How do slow movement practices help individuals with chronic pain by allowing the generative model to gather new evidence that contradicts its pain predictions? Describe the felt progression from avoidance to cautious exploration.",
        "In what way does mindful movement practice train the generative model to track the immediate, unfolding present rather than running ahead to future goals? Describe the felt quality of temporal presence during slow movement.",
        "Compare the felt quality of action performed with full embodied presence versus action performed while mentally elsewhere (eating while reading, walking while texting). What information is lost when presence is absent?",
        "How does the Alexander Technique's concept of 'inhibition' (pausing before habitual action to allow a new response) relate to Active Inference's account of policy selection under precision optimization?",
        "Describe the experience of Varela's 'moments of awareness' (2-3 second windows) during mindful movement. How does aligning action with these temporal windows produce the quality of 'being fully in the action'?",
        "How does the breath serve as a bridge between voluntary and involuntary action during movement meditation? Describe the felt quality of allowing the breath to flow naturally while moving deliberately.",
        "In contact improvisation or partner dance, two bodies coordinate movement through direct tactile communication. How does this shared action illustrate the alignment of generative models through embodied presence?",
        "Reflect on a practice of mindful movement you have engaged in (walking meditation, yoga, tai chi, dance). How did the quality of action change when you brought full present-moment awareness to each micro-phase of movement?",
    ],
    ("02_living_presence", "06_learning"): [
        "Describe the trajectory of learning in meditation: from restless settling to rapid stillness, from scattered attention to sustained focus. How does this trajectory reflect the progressive updating of the generative model's priors?",
        "How does repeated contemplative practice reshape the body's predictions? After weeks of daily sitting, the body comes to expect stillness, the shoulders drop, the jaw softens, the breathing deepens. What has the generative model learned?",
        "What is precision learning in contemplative practice? How does the meditator develop the capacity to assign high precision to the breath and low precision to transient noise -- the formal substrate of equanimity?",
        "Merleau-Ponty spoke of habit as 'sedimented knowledge.' How does the sedimentation of meditative practice create both the gift of effortless fluency and the risk of rigid automaticity?",
        "What is 'beginner's mind' in Zen practice, and how does it correspond to the deliberate loosening of deeply entrenched priors to allow fresh perception and response?",
        "Describe the neurobiology of embodied learning through contemplative practice: how do synaptic plasticity, structural neuroplasticity, and neuromodulatory changes implement the updating of the generative model?",
        "Sara Lazar found increased cortical thickness in meditators' insular cortex (interoception) and prefrontal cortex (attention). How does this structural change reflect the deepening of embodied presence through sustained practice?",
        "How does a contemplative journal practice (noting settling time, attention quality, and surprising moments after each session) make visible the gradual prior updating that is otherwise too slow to notice?",
        "Describe the felt quality of learning equanimity -- the moment when you first notice that a strong sensation or emotion arises and you can simply observe it without being captured. What has shifted in precision weighting?",
        "How does Jon Kabat-Zinn's MBSR program demonstrate that embodied learning extends beyond the nervous system, cascading into autonomic, endocrine, and immune regulation through the recalibration of the generative model?",
        "Describe the learning that occurs in the body during a meditation retreat (multiple days of sustained practice). How does immersive practice accelerate the updating of prior expectations?",
        "What is the relationship between sleep and contemplative learning? How does the consolidation of practice-related neural changes during sleep support the progressive refinement of the generative model?",
        "How does the concept of 'over-learning' apply to meditation -- the point at which sustained attention becomes so deeply sedimented that presence arises spontaneously, without deliberate effort?",
        "Describe the felt difference between a meditation session early in one's practice journey and a session after years of training. What has changed in the body's preparedness, the quality of attention, and the depth of stillness?",
        "How does the learning of equanimity relate to autonomic flexibility -- the smooth transition between arousal and calm? Why is this flexibility important for sustained present-moment awareness?",
        "In what way does embodied contemplative learning create 'self-fulfilling predictions' -- the body that has learned to expect calm settles into calm more readily, reinforcing the prediction?",
        "Reflect on your own learning trajectory in a contemplative or somatic practice. What changed most dramatically over time -- the body's settledness, the quality of attention, the depth of insight, or something else?",
    ],
    ("02_living_presence", "07_communication"): [
        "When sitting in silent meditation with another person, breathing often synchronizes spontaneously. How does Active Inference explain this interpersonal alignment of generative models without verbal exchange?",
        "Describe the felt quality of deep empathic listening -- attending to another's speech with your whole body rather than just your cognitive mind. What sensations arise, and how do they inform your understanding?",
        "What is participatory sense-making (Di Paolo and De Jaegher), and how does it redefine communication from information transfer to the joint creation of meaning through embodied interaction?",
        "In Insight Dialogue (Gregory Kramer), practitioners pause, relax, open, trust emergence, listen deeply, and speak truth. How does each guideline correspond to a specific precision optimization in the Active Inference framework?",
        "Describe the concept of a shared Markov blanket in interpersonal communication. When two people engage in genuine dialogue, how do the boundaries between their generative models become partially permeable?",
        "What is mutual incorporation (Fuchs and De Jaegher) -- the process by which another person's body becomes an extension of one's own experiential field? Describe a time you felt this during a deep conversation.",
        "How does speaking from embodied presence (pausing, feeling into the body, allowing words to arise from felt experience) differ from speaking from cognitive rehearsal? What changes in the quality of connection?",
        "Describe the non-verbal channels through which living presence is communicated in a therapeutic setting: the therapist's calm breathing, attuned gaze, responsive postural shifts. How do these create a stable predictive environment?",
        "What is brain-to-brain coupling (Hasson), and why is it strongest when both conversation participants are fully present and attentive? How does this neural synchrony reflect aligned generative models?",
        "How does collective meditation (sitting in a group) create a field of shared presence that individual practice cannot? Describe the felt quality of group energy and its effect on your own meditation.",
        "In what way does authentic speaking -- expressing what is genuinely felt rather than what is socially expected -- reduce the divergence between the internal model and its external expression, minimizing interpersonal free energy?",
        "Describe the somatic experience of being truly heard -- the felt shift that occurs when you sense that another person has received your communication at the bodily level, not just the cognitive level.",
        "How does the quality of the therapeutic alliance (the felt sense of connection between therapist and client) predict treatment outcomes regardless of therapeutic modality? What does this reveal about embodied communication?",
        "Describe how a practice of silent sitting with a partner (gazing softly, making no effort to communicate) reveals the non-verbal channels through which generative models spontaneously align.",
        "In what way does the voice carry the speaker's autonomic state? How do listeners' bodies respond differently to a voice speaking from ventral vagal calm versus one speaking from sympathetic arousal?",
        "How does contemplative communication practice (Insight Dialogue, council circle, authentic relating) create conditions for the kind of interpersonal free energy minimization that transforms superficial exchange into genuine meeting?",
        "Reflect on a communication experience where embodied presence transformed the quality of exchange -- where being fully present changed not just what was said but how it was received and what emerged between you.",
    ],
    ("02_living_presence", "08_planning"): [
        "During meditation, setting an intention by feeling into the body (rather than conceptual goal-setting) reveals planning as a somatic process. Describe the felt quality of an intention that resonates with bodily wisdom versus one that the mind imposes.",
        "How does expected free energy -- the anticipated surprise of future courses of action -- manifest as a felt evaluation in the body during contemplative intention-setting?",
        "Describe the tension between future-oriented planning and present-moment awareness. How does the enactive tradition resolve this by showing that planning is itself a present-moment activity?",
        "What is allostatic planning at the physiological level (the body adjusting hunger, fatigue, and arousal in anticipation of future demands)? How can mindful attention to these signals reveal the body's pre-cognitive planning?",
        "How does imagination function as embodied simulation rather than disembodied fantasy? When you imagine a future scenario during meditation, what does your motor cortex do? What does your body feel?",
        "Describe the phenomenology of anticipatory anxiety: the body generating high-precision negative predictions about the future that cycle without resolution. How does present-moment awareness interrupt this pattern?",
        "In what way does contemplative practice purify temporal depth -- stripping away anxious elaboration to reveal the generative model's clearest predictions about what truly matters over extended timescales?",
        "Compare planning from a state of mindful presence (the body open, the breath settled, the mind clear) with planning from a state of agitation (the body tense, the breath shallow, the mind racing). How do the plans differ?",
        "How does the body's autonomic state shape the planning horizon? When the body feels safe (ventral vagal), how does the range of envisioned futures expand compared to when the body feels threatened (sympathetic arousal)?",
        "Describe the practice of somatic intention-setting: sitting quietly, bringing a possible intention to mind, and tracking the body's response (expansive vs. constricting, warm vs. cold, light vs. heavy). How does this constitute embodied planning?",
        "What is the relationship between regret (the body simulating past decisions and generating prediction errors of 'what could have been') and future planning? How does present-moment awareness transform the experience of regret?",
        "How does the concept of 'temporal thickness of the present' (Husserl's specious present) relate to planning? In what way does healthy planning maintain the connection between anticipated futures and current bodily experience?",
        "Describe how sustained contemplative practice improves the quality of planning by developing the capacity to hold multiple imagined futures in somatic awareness simultaneously without collapsing into anxiety or impulsivity.",
        "How does sleep contribute to the consolidation and refinement of the generative model's planning capacities? What might the body be processing during dream states that relates to embodied anticipation?",
        "In what way does the contemplative practice of letting go (releasing attachment to specific outcomes) paradoxically improve planning by reducing the precision on preferred predictions and opening the model to new possibilities?",
        "Compare the quality of decisions made from contemplative presence with decisions made from habitual reactivity. How does the body's state of awareness influence the wisdom of the resulting plans?",
        "Reflect on a time when setting an embodied intention (feeling into what the body wanted rather than what the mind decided) led to an outcome that surprised you. What does this reveal about somatic planning?",
    ],
    # SECTION-LEVEL for 02_living_presence
    ("02_living_presence", None): [
        "How does Varela's enactive tradition redefine cognition from internal computation to the ongoing lived activity of an embodied agent coupled to its world? What does this mean for the practice of mindful awareness?",
        "Explain how attention functions as precision weighting in Active Inference. When you attend to your breath in meditation, what computationally is happening to the confidence assigned to respiratory prediction errors?",
        "What is the relationship between the breath's unique status (both autonomic and voluntary, both interoceptive and proprioceptive) and its central role in contemplative practices across traditions?",
        "How do movement meditation practices (tai chi, yoga, walking meditation) train the generative model to track the immediate, unfolding present rather than running ahead to future goals?",
        "Describe Husserl's concept of the 'specious present' -- the temporal thickness of lived experience. How does Active Inference model this through hierarchical generative models operating at multiple timescales?",
        "How does Evan Thompson's claim that 'the mind is not something the brain does but something the living system enacts' change your understanding of the relationship between awareness and embodiment?",
        "Describe the phenomenological quality of what contemplatives call 'just this' -- the state where the gap between prediction and experience has been reduced to near zero. What Active Inference concept does this reflect?",
        "How does the practice of three-minute breathing space (attending to breath at the nostrils, noticing wandering, gently redirecting) strengthen precision weighting on present-moment interoceptive signals over time?",
        "What is the relationship between mind-wandering (the generative model's default tendency toward counterfactual simulation) and the contemplative practice of returning attention to present-moment experience?",
        "In what way does the claim 'presence is not passivity but the most exquisite form of activity' challenge the common misconception that meditation is about 'doing nothing'?",
        "Describe the neurophysiological evidence (altered gamma-band synchrony, reduced default-mode network activity) that supports the claim that contemplative practice reshapes the brain's inferential architecture.",
        "How does the alignment of fast sensory dynamics, medium action dynamics, and slow mood dynamics characterize the experience of deep present-moment awareness? What does this multi-timescale convergence feel like?",
        "Compare the quality of awareness during sitting meditation, walking meditation, and eating meditation. How does each practice reveal different dimensions of living presence?",
        "How does the concept of 'optimal precision weighting' distinguish between productive present-moment awareness and maladaptive hyper-vigilance? Both involve heightened attention, but how do they differ?",
        "Describe the experience of returning to presence after an extended period of mind-wandering during meditation. What is the felt quality of this re-anchoring, and what Active Inference process does it involve?",
        "How do contemplative retreats (sustained multi-day practice in a simplified environment) create conditions for the deep recalibration of the generative model's precision architecture?",
        "Reflect on the central insight of this unit: that to be present is to be actively minimizing free energy at every level of the generative hierarchy. How does your contemplative experience illuminate this formal claim?",
    ],

    # ========================================================================
    # 03_INTUITIVE_KNOWING
    # ========================================================================
    ("03_intuitive_knowing", "01_systems"): [
        "An experienced ER nurse walks into a patient's room and immediately senses something is wrong before vital signs confirm it. How does her body function as an integrated diagnostic system whose generative model generates a system-level prediction error?",
        "A master sommelier identifies the origin, vintage, and quality of a wine from a single sip. Describe how his gustatory-olfactory-interoceptive system has minimized free energy over decades until pattern recognition operates as immediate bodily knowing.",
        "How does the concept of a Markov blanket apply to the expert body functioning as an intuitive system? What sensory surfaces constitute the boundary through which domain-specific information enters the expert's generative model?",
        "What is the relationship between system-level coherence and the speed of intuitive recognition? Why does an integrated, well-calibrated body-system produce faster and more reliable intuitions than a fragmented one?",
        "Compare the system-level organization of a novice perceiver (fragmented, effortful, sequential processing) with that of an expert (integrated, effortless, holistic recognition). What has changed at the systemic level of the generative model?",
        "How does the concept of nested systems (cells, organs, organism) apply to intuitive knowing? When a skilled bodyworker feels tension in a client's tissue, which levels of the system hierarchy are involved in the intuitive assessment?",
        "Describe how the autonomic nervous system contributes to intuitive systemic assessment. When an experienced clinician feels a 'gut sense' about a patient, what role does vagal signaling play in transmitting that intuition?",
        "What distinguishes a reliable intuitive system from a biased one? How might the Active Inference framework help differentiate between well-calibrated intuitive priors and systematically distorted ones?",
        "How does extensive deliberate practice transform the body from a system that processes domain-specific information sequentially into one that recognizes patterns holistically? What is the felt quality of this systemic transformation?",
        "Describe how a skilled musician's body functions as an integrated auditory-motor-affective system during improvisation. What does it mean for the entire system to be operating in a regime of minimal prediction error?",
        "How might system-level disruption (illness, exhaustion, emotional distress) temporarily impair intuitive knowing? What happens to the expert's pattern recognition when systemic coherence is compromised?",
        "What is the relationship between the body's homeostatic regulation and the reliability of intuitive judgment? Does a well-regulated body produce more trustworthy intuitions than a dysregulated one?",
        "Compare the systemic organization of intuitive knowing in different domains (medicine, cooking, athletics, music). What common features of bodily system organization underlie intuitive expertise across these diverse fields?",
        "How does the concept of allostatic regulation (anticipatory adjustment of set-points) apply to expert intuition? Does the expert's body proactively prepare for the patterns it expects to encounter?",
        "Describe a scenario where two different experts (e.g., an experienced surgeon and an experienced chef) both exhibit intuitive systemic knowing, but through entirely different Markov blanket surfaces and sensory channels.",
        "What does the experience of being 'in the zone' or 'in flow' reveal about systemic integration in intuitive performance? How does the entire body-as-system operate differently during peak intuitive functioning?",
        "Reflect on your own most reliable domain of intuitive knowing. In what area do you 'just know' things that you cannot fully explain? Describe the systemic organization of your body during these moments of intuitive recognition.",
    ],
    ("03_intuitive_knowing", "02_agents"): [
        "A firefighter feels a gut-level pull to evacuate seconds before a floor collapses. How does his embodied agency generate a prediction of catastrophic surprise that the body enacts as immediate withdrawal before conscious reasoning intervenes?",
        "A veteran midwife intuitively knows the baby has shifted position through ambiguous palpation findings. Describe how her embodied agency -- hands, proprioceptive sensitivity, visceral resonance -- produces an inference that feels like knowing rather than calculating.",
        "How does the Dreyfus model of skill acquisition (novice to expert) transform the nature of embodied agency? What changes in the felt quality of action as the agent moves from following rules to intuitive responsiveness?",
        "What is the relationship between autonomic agency (the body's self-regulatory intelligence) and intuitive decision-making? How does the agent's physiological state influence the quality of its intuitions?",
        "Describe the phenomenology of recognition-primed decision making (Gary Klein): the expert enters a situation and immediately 'sees' the right course of action. How does the embodied agent generate this instant assessment?",
        "How does embodied expertise dissolve the boundary between perception and action in the expert agent? When a skilled martial artist reacts to an attack, is the response perception, cognition, or action?",
        "In what way does the expert agent's sense of agency differ from the novice's? How does the shift from deliberate control to fluid responsiveness change the felt quality of being the author of one's actions?",
        "Describe how the concept of 'I can' (Sheets-Johnstone) expands with expertise. How does the expert's felt horizon of possibility differ from the novice's, and what Active Inference mechanism accounts for this expansion?",
        "What role does confidence (precision on motor predictions) play in the expert agent's capacity for intuitive action? How does the felt sense of 'I know what to do' relate to the generative model's certainty about its own predictions?",
        "Compare the expert agent's relationship to uncertainty with the novice's. How does the expert tolerate ambiguity and act decisively from incomplete information, while the novice requires explicit rules and clear data?",
        "How does the concept of 'embodied connoisseurship' (Eisner) apply to intuitive agency? Describe an expert whose body functions as a refined instrument of assessment -- tasting, touching, seeing with accumulated wisdom.",
        "Describe the felt quality of the expert's 'negative space' intuition -- knowing that something is missing or wrong without being able to specify what. How does the embodied agent detect absence through prediction error?",
        "How does fatigue or cognitive load impair the expert agent's intuitive capacity? What happens to the felt quality of embodied knowing when the system is overtaxed?",
        "In what way does the expert agent's intuitive response carry implicit ethical dimensions? When a clinician 'feels' that a patient needs compassion rather than information, what embodied agency is at work?",
        "Describe the developmental trajectory of an expert agent in your own field of interest. How does the progressive refinement of embodied priors transform the quality of agency from effortful to intuitive?",
        "What is the relationship between trust in one's own embodied agency and the reliability of intuitive performance? How does self-doubt (reduced precision on motor predictions) impair intuitive action?",
        "Reflect on a time when your embodied agency produced an intuitive response that surprised even you -- when your body 'knew' something before your conscious mind caught up. What was the quality of that knowing?",
    ],
    ("03_intuitive_knowing", "03_perception"): [
        "A chess grandmaster glances at a board and the right move presents itself as a perceptual gestalt. Describe how the buzz of recognition in her body confirms the match between the visual array and deep priors from thousands of games.",
        "An experienced martial artist reads a subtle shoulder shift as the precursor to a specific strike, with millisecond precision. How does the generative model complete the incoming visual signal into a full action trajectory experienced as direct bodily seeing?",
        "How does intuitive perception differ from ordinary perception in terms of precision weighting? What has changed in the expert's model that allows pattern recognition to operate as immediate seeing rather than effortful analysis?",
        "Describe the phenomenology of the expert's 'gaze' -- the quality of attention that allows a master diagnostician, a skilled tracker, or an experienced art appraiser to see what others miss. What is the perceptual mechanism?",
        "How does the concept of affordances (Gibson) expand with expertise? The novice perceives a rock face as a wall; the experienced climber perceives it as a connected path of holds. What has changed in the perceptual model?",
        "In what way does the expert's perception integrate multiple sensory channels simultaneously? A skilled chef tastes with her nose, eyes, and memory all at once. How does this multi-modal integration produce intuitive perceptual wholes?",
        "Describe the felt quality of perceptual fluency -- the ease with which the expert processes domain-relevant information. How does this fluency relate to the generative model's capacity to predict incoming sensory data accurately?",
        "What is the relationship between perceptual expertise and the ability to see meaningful structure where novices see only noise? Provide an example from medicine, art, nature, or athletics.",
        "How does the expert's perception extend beyond the immediate visual field? A basketball point guard 'sees' players behind her; a skilled driver 'feels' the car behind him. What Active Inference mechanism supports this expanded perceptual awareness?",
        "Describe the phenomenon of perceptual learning -- the progressive refinement of sensory discrimination through extended practice. How does a wine taster's palate become increasingly differentiated over years of tasting?",
        "How does the expert's embodied perception function as a form of compressed inference -- the generative model rapidly categorizing complex stimuli by matching them to deep perceptual priors? What is the felt quality of this compression?",
        "In what way does the expert's perception carry implicit evaluative content? When a master carpenter runs his hand along a joint, he simultaneously perceives its shape and evaluates its quality. How are perception and judgment fused?",
        "Describe how cultural and training differences shape intuitive perception. An Inuit elder sees twenty types of snow where a city dweller sees white. How does the generative model's learned categories structure what is directly perceived?",
        "What role does the body's current state (fatigue, alertness, emotional mood) play in modulating the quality of expert perception? When is intuitive perception most reliable, and when is it most vulnerable to error?",
        "How does the concept of perceptual prediction error operate in the expert's domain? What does the expert feel when something unexpected appears -- a pattern that violates the generative model's well-trained expectations?",
        "Compare intuitive perception in a visual domain (art appraisal), an auditory domain (music performance), and a tactile domain (surgical palpation). What common Active Inference principles underlie expert perception across sensory modalities?",
        "Reflect on your own domain of perceptual expertise (however humble). In what area can you see or sense things that others cannot? Describe the quality of that expert perception and how it developed through embodied practice.",
    ],
    ("03_intuitive_knowing", "04_cognition"): [
        "A mathematician reports that a proof 'feels right' before she can articulate the formal steps -- a warming expansion in her chest. How has the generative model compressed years of pattern recognition into somatic judgment?",
        "An experienced therapist senses concealed grief in a client's cheerful narrative through a tightening in her own diaphragm. How does this embodied cognitive process operate across the interpersonal Markov blanket?",
        "How does Polanyi's distinction between focal and subsidiary awareness apply to intuitive cognition? What is the relationship between what the expert attends to explicitly and the vast tacit knowledge that enables that attention?",
        "Describe the Dreyfus progression from rule-following to intuitive cognition. At the expert level, how does the generative model produce context-sensitive understanding without deliberative processing?",
        "What is the 'paradox of expertise and articulation' -- why does the expert struggle to explain what she knows? How does the high-dimensional, continuous generative model resist translation into low-dimensional, discrete verbal form?",
        "How does the concept of 'embodied mathematics' (Lakoff and Nunez) challenge the assumption that mathematical cognition is purely abstract? In what way is the felt sense of mathematical truth a somatic phenomenon?",
        "Describe the cognitive quality of intuitive pattern recognition: the moment when scattered data points suddenly coalesce into a meaningful whole. What is the felt quality of this gestalt formation, and what Active Inference process produces it?",
        "How does the expert's intuitive cognition handle novel situations that depart from previously encountered patterns? What role does the generative model's capacity for interpolation and extrapolation play?",
        "In what way does intuitive cognition integrate emotional and rational processing? Describe a scenario where the expert's gut feeling and analytical assessment converge on the same conclusion.",
        "What is the relationship between sleep, dream processes, and the consolidation of intuitive cognitive patterns? How might the body process complex domain knowledge during rest?",
        "Describe how the expert's cognitive engagement with a problem differs qualitatively from the novice's. What does it feel like to think about a complex problem from a place of deep tacit knowledge?",
        "How does the concept of 'incubation' (stepping away from a problem and returning with fresh insight) relate to the Active Inference account of generative model restructuring beneath conscious awareness?",
        "In what way does intuitive cognition carry implicit uncertainty estimates? The expert 'knows' the answer but also senses the confidence level of that knowing. How does precision weighting produce this dual awareness?",
        "Compare the cognitive style of intuitive expertise in a structured domain (chess, mathematics) with intuitive expertise in an unstructured domain (psychotherapy, leadership). How does the nature of the domain shape the quality of tacit knowing?",
        "What role does embodied metaphor play in intuitive cognition? When the expert says a solution 'clicks into place' or a situation 'smells wrong,' how do these bodily metaphors reflect genuine somatic cognitive processes?",
        "How does the accumulation of case experience (thousands of patients, thousands of games, thousands of negotiations) transform the generative model's cognitive architecture from explicit rules to implicit patterns?",
        "Reflect on a moment of intuitive cognition in your own life -- a time when you 'just knew' something without being able to explain how. What was the quality of that knowing, and what does it reveal about embodied intelligence?",
    ],
    ("03_intuitive_knowing", "05_action"): [
        "A jazz musician's fingers find an unexpected chord substitution that perfectly resolves harmonic tension without deliberate planning. How does the generative model's deep musical priors produce intuitive action that bypasses conscious thought?",
        "An aikido master responds to an attacker's grab with a fluid redirect that seems effortless and instantaneous. Describe how decades of embodied training create whole-body action policies that minimize free energy across the coupled system.",
        "How does the transition from deliberate practice to intuitive skilled action illustrate the Dreyfus model of expertise? Describe the felt quality of action at each stage from novice to master.",
        "What is the relationship between pre-reflective self-awareness (Gallagher) and intuitive skilled action? How does the expert act with tacit awareness that she is the source of the action without needing to reflect on it?",
        "Describe the phenomenon of 'muscle memory' through the lens of Active Inference. When a pianist's hands find the right chord without conscious direction, what has the generative model learned about sensorimotor contingencies?",
        "How does the concept of motor prediction error approach zero in expert skilled action? What does it feel like when the body's movement predictions and their sensory consequences are so well matched that action flows without interruption?",
        "In what way does intuitive action integrate perception, cognition, and motor execution into a single, undivided process? Describe this integration in the context of a skilled surgeon, potter, or dancer.",
        "What role does the body's autonomic state play in enabling intuitive skilled action? How does the physiological foundation (arousal level, breathing pattern, muscular readiness) support or impair expert performance?",
        "Describe the felt quality of 'improvisation' in expert action -- the capacity to generate novel, contextually appropriate responses in real time. How does the generative model support creative action that exceeds memorized sequences?",
        "How does the expert's action repertoire constitute a form of embodied knowledge that exceeds verbal description? Describe a skilled action that you can perform but cannot fully explain to someone else.",
        "What is the role of timing in intuitive skilled action? How does the expert's generative model predict not just what to do but precisely when to do it, producing the temporal precision that distinguishes mastery?",
        "Compare the felt quality of intuitive action under normal conditions with intuitive action under pressure (competition, emergency, performance). How does stress modulate the expert's capacity for fluid, pre-reflective action?",
        "Describe how the practice of 'deliberate practice' (Ericsson) -- targeted training at the edge of current ability -- generates the prediction errors necessary to update the generative model's motor priors toward expert-level fluency.",
        "How does the concept of 'action affordances' expand with expertise? The novice sees limited action possibilities; the expert perceives a rich field of potential responses. What has changed in the action dimension of the generative model?",
        "In what way does intuitive action carry implicit aesthetic qualities? The expert's movement is often described as 'beautiful' or 'elegant.' How does the minimization of free energy in skilled action produce aesthetic grace?",
        "What happens when the expert's intuitive action is disrupted -- when overthinking interrupts flow, when attention fragments the smooth arc of movement? Describe the felt quality of this disruption and its Active Inference explanation.",
        "Reflect on a domain where your own action has become intuitive through extended practice. Describe the felt quality of that intuitive action and how it differs from your deliberate, effortful action in unfamiliar domains.",
    ],
    ("03_intuitive_knowing", "06_learning"): [
        "A medical student initially checks diagnostic criteria consciously; after years, she walks into a room and 'just knows' the diagnosis. Describe this transition as progressive free energy minimization through embodied learning.",
        "A potter's hands initially struggle with coordination; after thousands of pots, they intuitively feel the exact moment to pull upward and the precise pressure to thin the wall. How has the generative model absorbed sensorimotor regularities?",
        "What is the '10,000 hour rule' (Ericsson) in terms of Active Inference? How does extended deliberate practice transform the generative model's structure from sparse, rule-dependent predictions to rich, context-sensitive intuitions?",
        "Describe the learning curve of intuitive knowing: early rapid improvement, followed by a plateau, then breakthrough. How do these phases correspond to different types of generative model updating (parameter learning vs. structure learning)?",
        "How does the concept of 'chunking' (Simon and Chase) apply to the development of intuitive expertise? As the learner groups individual elements into meaningful patterns, what changes in the generative model?",
        "What role does feedback (both external and somatic) play in the development of intuitive knowing? How does the body's prediction error signal guide the progressive refinement of expert priors?",
        "Describe the relationship between diversity of experience and the quality of intuitive expertise. Why does the expert who has encountered many varied cases develop more reliable intuitions than one with narrow experience?",
        "How does emotional learning (the accumulation of somatic markers across thousands of domain encounters) contribute to the formation of 'gut feelings' that guide expert judgment?",
        "What is the role of failure in developing intuitive expertise? How do significant prediction errors (mistakes, surprises, unexpected outcomes) contribute more to learning than successful confirmations?",
        "Describe how mentorship and apprenticeship facilitate the transmission of tacit knowledge. What does the apprentice learn from the master's body -- posture, timing, touch -- that cannot be communicated through verbal instruction?",
        "How does the development of intuitive expertise change the expert's relationship to explicit rules? At what point do rules become scaffolding to be transcended rather than prescriptions to be followed?",
        "What is the neuroscience of expertise-related consolidation? How do sleep, rest, and incubation periods contribute to the transformation of deliberate knowledge into intuitive knowing?",
        "Describe the phenomenon of 'overtraining' -- the point at which additional deliberate practice ceases to improve and may even impair intuitive performance. What Active Inference mechanism explains this plateau?",
        "How does cross-domain learning (studying multiple related disciplines) enhance intuitive knowing within a primary domain? What does the generative model gain from exposure to diverse but related prediction error landscapes?",
        "What distinguishes adaptive expertise (the capacity to apply intuitive knowing to novel situations) from routine expertise (reliable performance in familiar situations)? How does the generative model support each?",
        "Describe the felt quality of the moment when deliberate knowledge becomes intuitive -- the first time a complex skill executes itself without conscious direction. What has shifted in the body's predictive architecture?",
        "Reflect on the long arc of learning in your own primary domain. How has your relationship to knowledge changed from explicit understanding to embodied, intuitive knowing? What was lost and what was gained in this transition?",
    ],
    ("03_intuitive_knowing", "07_communication"): [
        "An experienced negotiator intuitively senses the moment to make a concession from a subtle shift in the room's energy that she registers as loosening in her own shoulders. How does her generative model decode micro-postural and tonal cues?",
        "A mother distinguishes her infant's hungry cry from the pain cry from across the house, feeling different somatic responses for each. Describe how deeply evolved embodied priors enable this intuitive communication.",
        "How does the expert communicator's tacit knowledge of social dynamics operate across Markov blankets? What bodily signals constitute the sensory evidence from which intuitive social inference is drawn?",
        "Describe the felt quality of intuitive rapport -- the expert therapist, interviewer, or negotiator's capacity to sense when connection has been established and when it has been lost. What somatic signals indicate this?",
        "In what way does the expert's communication operate through 'somatic resonance' -- feeling the other's state in one's own body? How does this cross-Markov-blanket inference support intuitive interpersonal knowing?",
        "How does the concept of 'thin-slicing' (Gladwell) -- making accurate judgments from minimal information -- relate to the expert communicator's refined generative model? What makes snap social judgments reliable or unreliable?",
        "Describe the felt difference between a conversation guided by intuitive social knowing (fluid, responsive, attuned) and one guided by explicit social rules (stilted, calculated, effortful). What has the expert's model learned?",
        "How does the expert's capacity to communicate tacit knowledge to apprentices operate through embodied channels? What does the mentor transmit through tone, timing, gesture, and presence that words alone cannot convey?",
        "What role does vocal prosody (the music of speech) play in intuitive social communication? How does the expert speaker's voice carry encoded information about intention, certainty, and emotional state?",
        "Describe the phenomenon of 'contagion' in expert group settings -- how the expert facilitator's embodied state (calm, energy, focus) spreads to the group through non-verbal channels. What Active Inference mechanism supports this transmission?",
        "How does intuitive communication operate in high-stakes environments (emergency rooms, crisis negotiations, surgical teams)? What role does embodied interpersonal knowing play when verbal communication is inadequate?",
        "In what way does the expert's capacity for 'reading the room' -- sensing collective mood, identifying unspoken tensions, detecting emerging consensus -- constitute a form of intuitive social cognition?",
        "Describe the communicative dimension of expert physical practices (partner dance, contact improvisation, martial arts sparring). How do two bodies communicate movement intentions through purely somatic channels?",
        "What is the relationship between empathic accuracy (correctly inferring another's emotional state) and the refinement of the generative model through accumulated interpersonal experience?",
        "How does cultural expertise -- deep familiarity with the norms, values, and communicative patterns of a specific community -- shape the intuitive communication of a cultural insider? What does this expertise feel like?",
        "Describe the experience of 'clicking' with another person -- the sudden establishment of deep intuitive rapport. What has happened at the level of generative model alignment that produces this felt experience of connection?",
        "Reflect on your own intuitive communicative strengths. In what social contexts do you 'just know' the right thing to say or do? What embodied knowledge underlies this intuitive social competence?",
    ],
    ("03_intuitive_knowing", "08_planning"): [
        "A veteran military commander surveys a battlefield and intuitively selects a strategy, feeling bodily rightness about one approach and unease about another. How does the generative model run compressed counterfactual simulations evaluated somatically?",
        "An experienced entrepreneur feels that one investment opportunity is 'alive' while another produces dull heaviness despite similar financial projections. How does the gut-level evaluation integrate vast implicit pattern knowledge into a somatic summary statistic?",
        "How does intuitive planning differ from analytical planning in terms of temporal compression? The expert evaluates complex future scenarios in seconds; the novice requires hours of deliberation. What has changed in the generative model?",
        "Describe the phenomenology of the expert's 'vision' -- the capacity to see a future path with clarity and felt conviction that exceeds what available data can logically support. How does deep experience produce this embodied foresight?",
        "What role does the expert's 'negative intuition' play in planning -- the sense that a particular plan is wrong before being able to articulate why? How does prediction error detection in the generative model produce this warning signal?",
        "How does the expert planner integrate multiple sources of tacit knowledge (market patterns, interpersonal dynamics, historical precedents, somatic cues) into a single intuitive assessment of a plan's viability?",
        "Describe the felt difference between planning from intuitive expertise (calm certainty, embodied confidence) and planning from anxious analysis (rumination, second-guessing, paralysis). What has changed in precision weighting?",
        "What is the relationship between experience-based pattern recognition and the reliability of intuitive planning? Under what conditions does the expert's gut feeling provide a more accurate forecast than analytical models?",
        "How does the concept of 'satisficing' (Simon) -- selecting the first option that meets a threshold of acceptability rather than optimizing -- relate to the expert's intuitive planning process?",
        "Describe the expert planner's capacity for 'mental simulation' -- running through a plan's execution in imagination and feeling the somatic consequences of each step. How does this embodied simulation differ from abstract scenario modeling?",
        "What is the role of emotional tagging in intuitive planning? How do the expert's accumulated somatic markers (positive associations with certain patterns, negative associations with others) shape policy selection?",
        "How does the expert planner maintain cognitive flexibility -- the capacity to abandon an intuitive plan when new evidence suggests it is wrong? What tension exists between commitment to intuitive judgment and openness to disconfirmation?",
        "Describe the interpersonal dimension of intuitive planning in team settings. How does the expert leader sense when the team is aligned with a plan and when there is hidden resistance, through embodied rather than verbal cues?",
        "What distinguishes wise intuitive planning from impulsive decision-making? Both bypass deliberation, but how does the quality of the underlying generative model determine whether the result is wisdom or recklessness?",
        "How does the expert's capacity for long-horizon intuitive planning (sensing what will matter in years rather than weeks) develop? What kind of experience and practice builds temporal depth in the generative model?",
        "Describe the felt quality of the moment when an intuitive plan crystallizes -- when the scattered elements of a complex situation suddenly organize into a clear course of action. What Active Inference process produces this clarity?",
        "Reflect on a decision you made largely on intuition that proved correct in hindsight. What embodied knowledge guided your planning, and how did the felt sense of the decision differ from analytically derived choices?",
    ],
    # SECTION-LEVEL for 03_intuitive_knowing
    ("03_intuitive_knowing", None): [
        "How does Polanyi's observation that 'we know more than we can tell' connect to the Active Inference account of the generative model encoding knowledge in parameters that resist propositional articulation?",
        "Describe the Dreyfus model of skill acquisition from novice to expert. How does each stage correspond to a different configuration of the generative model's precision architecture and predictive depth?",
        "What is the relationship between gut feelings and the generative model's capacity for rapid, compressed interoceptive inference? How does Gary Klein's recognition-primed decision making formalize the firefighter's instant situational awareness?",
        "How does extended practice transform deliberate rule-following into fluid pre-reflective performance? Describe the phenomenological shift from effortful compliance to intuitive mastery.",
        "What is the 'paradox of expertise and articulation' -- why does the expert struggle to explain what she knows? How does the high-dimensional generative model resist translation into low-dimensional verbal form?",
        "How does the concept of subsidiary awareness (the vast background of tacit knowledge that enables focal attention) apply to intuitive performance in your own domain of expertise?",
        "Describe the felt quality of flow state -- the experience of complete absorption in an activity where action arises without deliberation. How does Active Inference explain this state as chronically low free energy?",
        "How does the body's accumulated case experience (thousands of patients, games, performances, or negotiations) build the deep priors that constitute intuitive expertise? What role does sleep and consolidation play?",
        "In what way does intuitive knowing integrate perception, cognition, and action into a single undivided process? Provide an example from expert performance in any domain.",
        "How does the concept of 'pre-reflective self-awareness' (Gallagher) apply to the expert's experience of skilled action? The expert does not think about acting but simply acts with implicit self-knowledge.",
        "What distinguishes reliable intuition from unreliable bias? How might the Active Inference framework help differentiate between well-calibrated tacit knowledge and systematically distorted priors?",
        "Describe how the development of intuitive expertise changes the expert's relationship to uncertainty. The expert acts confidently with incomplete information; the novice requires explicit data. What enables this?",
        "How does intuitive knowing manifest differently in structured domains (chess, mathematics) versus unstructured domains (therapy, leadership, parenting)? What does this variation reveal about the nature of tacit knowledge?",
        "Describe the role of embodied practice (physical skill, somatic training, hands-on apprenticeship) in building the kind of intuitive knowing that purely intellectual study cannot produce.",
        "How does the concept of 'embodied connoisseurship' -- the refined capacity for aesthetic and evaluative judgment through bodily engagement -- illustrate the intersection of perception, knowledge, and felt sense?",
        "What is the relationship between humility (recognizing the limits of one's intuitive competence) and wisdom in expert practice? How does the well-calibrated generative model know what it does not know?",
        "Reflect on the central claim of this unit: that intuitive knowing is not a deficient form of cognition but its highest expression. How does your own experience of embodied expertise support or challenge this claim?",
    ],

    # ========================================================================
    # 04_MOVING_THROUGH_WORLD
    # ========================================================================
    ("04_moving_through_world", "01_systems"): [
        "When running along a rocky trail, your musculoskeletal, vestibular, and visual systems operate as a tightly coupled locomotor system. How does this whole-body system maintain its Markov blanket dynamically during rapid movement?",
        "A dancer performing complex choreography functions as an integrated system where respiratory rhythm, spinal undulation, limb trajectory, and spatial orientation are all coupled. What is the 'flow' of movement as systemic free energy minimization?",
        "How does Gibson's ecological psychology reframe the body-in-motion as a system defined not by internal properties alone but by its dynamic relationship with the environmental structure it traverses?",
        "Describe the systemic challenge of balance: the body as a multi-joint, multi-muscle system continuously predicting and correcting its own center of gravity. What does this look like in Active Inference terms?",
        "How does the vestibular system function as a core component of the moving body's systemic organization? What does the felt sense of spatial orientation contribute to the embodied generative model?",
        "Compare the systemic organization of walking (a relatively stable, rhythmic pattern) with the systemic organization of climbing (a dynamic, context-dependent pattern). How does the body-as-system adapt to different movement demands?",
        "What role does proprioception play as the internal communication channel of the moving body-as-system? How do proprioceptive signals maintain systemic coherence during complex multi-joint movements?",
        "Describe how the respiratory system integrates with the locomotor system during running (breath entrainment to stride pattern). What does this coupling reveal about the body's systemic organization during movement?",
        "How does injury disrupt the moving body's systemic organization? When a sprained ankle alters gait, how does the entire body-as-system reorganize its predictions and movement patterns?",
        "In what way does the concept of synergy (Bernstein) -- the body's capacity to coordinate multiple degrees of freedom into functional units -- illustrate systems-level organization in embodied movement?",
        "Describe the experience of moving in water (swimming) as a reconfiguration of the body's systemic boundaries. How does the aquatic environment change the Markov blanket of the moving body?",
        "How does the body-as-moving-system adapt to new gravitational environments (a trampoline, a slope, an escalator)? What prediction errors arise and how does the system recalibrate?",
        "What is the relationship between cardiovascular fitness and the moving body's systemic capacity? How does improved aerobic function expand the range of movement policies available to the active inference agent?",
        "Describe how a team sport (basketball, soccer, rugby) extends the concept of system beyond the individual body to a multi-agent system of coordinated moving bodies. What is the systemic organization of the team?",
        "How does the concept of dynamic stability (maintaining balance not through rigidity but through continuous adaptive movement) exemplify the Active Inference principle of active self-organization?",
        "In what way does warming up before physical activity illustrate the body-as-system recalibrating its predictions and preparing its interoceptive, proprioceptive, and motor subsystems for increased demands?",
        "Reflect on a movement experience where you felt your body operating as an integrated, coherent system -- running, dancing, swimming, climbing. What was the quality of that systemic experience?",
    ],
    ("04_moving_through_world", "02_agents"): [
        "A parkour practitioner sees a wall not as an obstacle but as an affordance -- a surface to vault, a ledge to grab. How does her body-as-agent perceive the environment in terms of what her movement repertoire allows?",
        "When navigating a crowded sidewalk, the body autonomously adjusts stride, pace, and trajectory to weave through gaps. How does this automatic locomotor agency operate beneath conscious awareness through active inference?",
        "How does the concept of motor agency differ between a novice walker (an infant) and an expert mover (a dancer or martial artist)? What has changed in the agent's felt horizon of movement possibility?",
        "Describe the experience of navigating a new physical environment (an unfamiliar building, a rocky beach, a dense forest). How does the embodied agent update its movement predictions in real time?",
        "How does the sense of spatial agency -- the felt capacity to move through and act upon the physical world -- relate to psychological well-being? What happens to this sense during physical disability or injury?",
        "In what way does tool use (riding a bicycle, skiing, driving a car) extend the body-agent's Markov blanket to include the tool's contact surface with the world? Describe the felt expansion of bodily agency.",
        "How does the moving agent's sense of 'peripersonal space' (the region immediately surrounding the body) shape the experience of navigating through environments? What happens when this space is violated by unexpected proximity?",
        "Describe the felt quality of locomotor autonomy -- the body's capacity to navigate complex terrain without conscious planning. How does this pre-reflective spatial agency relate to the Active Inference account of motor policy selection?",
        "How does the embodied agent's movement capacity constrain and enable its engagement with the world? Compare the affordance landscape perceived by a wheelchair user with that perceived by an able-bodied runner.",
        "What is the relationship between physical confidence (trust in one's movement capacities) and spatial agency? How does the felt sense of 'I can handle this terrain' shape the agent's willingness to explore?",
        "Describe how the body-agent adapts its movement strategies when carrying a heavy load. How does the additional mass change the agent's predictions about balance, stride length, and energy expenditure?",
        "In what way does the experience of vertigo or dizziness reveal the vulnerability of spatial agency? What happens to the sense of being a competent moving agent when vestibular predictions are disrupted?",
        "How do cooperative movement activities (partner dance, team sport, group hiking) create multi-agent systems where individual spatial agencies must coordinate? What does this coordination feel like from the inside?",
        "Describe the agent's experience of moving at different speeds (strolling, jogging, sprinting). How does the temporal grain of spatial agency shift as velocity increases?",
        "How does aging change the embodied agent's spatial capacity and the resulting felt sense of movement possibility? What happens to the agent's model as physical capacities gradually decline?",
        "In what way does the experience of play -- running, jumping, tumbling, climbing without purpose -- reveal the pure expression of spatial agency freed from instrumental goals?",
        "Reflect on a moment of peak spatial agency -- when your body navigated a challenging physical environment with fluid confidence. What was the quality of that embodied experience?",
    ],
    ("04_moving_through_world", "03_perception"): [
        "When riding a bicycle toward a narrow gap, you perceive the gap directly as 'passable' or 'too tight' through a felt sense of your body's width. How does the generative model transform visual information into motor-relevant affordances scaled to body dimensions?",
        "A rock climber scanning a cliff face perceives handholds as a connected path, feeling in her shoulders the effort each hold will require before touching it. How are seeing and feeling unified at the Markov blanket of the moving body?",
        "How does the concept of optic flow (the visual pattern generated by self-motion through the environment) function as a primary perceptual signal for the moving body? What does Active Inference say about predicting this flow?",
        "Describe the embodied perception of distance: the felt quality of 'how far' as experienced through the body's locomotor history (how many steps, how much effort, how long it takes). How does this differ from abstract spatial measurement?",
        "How does the perception of surfaces change depending on the body's movement intention? The same floor is perceived differently when you intend to walk versus when you intend to slide, crawl, or dance on it. What changes in the generative model?",
        "In what way does peripheral vision serve the moving body differently than foveal vision? How does the peripheral visual field provide the ecological information necessary for navigation and obstacle avoidance?",
        "Describe the multisensory integration required for spatial navigation: how do vision, proprioception, vestibular sensation, audition, and touch combine to create a unified perception of the moving body in space?",
        "How does the perception of affordances (sittable, climbable, passable, graspable) change with the body's current state? A bench is perceived differently when you are exhausted versus when you are energized. What mediates this shift?",
        "What is the relationship between kinesthesia (the felt sense of movement) and visual perception during locomotion? How does the body predict the visual consequences of its own movement, and what happens when predictions are violated?",
        "Describe the perceptual experience of navigating in darkness or with eyes closed. What sensory channels become primary, and how does the generative model adapt when visual prediction errors are unavailable?",
        "How does the moving body perceive time through space? The experience of duration during a long walk versus a short sprint illustrates the temporal dimension of embodied spatial perception. What Active Inference mechanism accounts for this?",
        "In what way does the perception of terrain (slope, texture, stability) integrate haptic feedback from the feet with visual preview from the eyes? Describe this integration during a walk on uneven ground.",
        "How does the experience of being a passenger (in a car, on a train) differ from being the driver or walker in terms of spatial perception? What changes when the body is moved rather than moving itself?",
        "Describe the perceptual phenomenon of 'affordance competition' -- when the environment simultaneously presents multiple action possibilities and the body must select one. What determines which affordance is perceived most saliently?",
        "How does the perception of other moving bodies (pedestrians, cyclists, animals) involve the simulation of their trajectories in the observer's own motor system? What does this simulation feel like?",
        "In what way does scale perception (perceiving whether a space is large or small, whether an object is heavy or light) depend on the body's own dimensions and capacities as a reference frame?",
        "Reflect on a moment when your perception of the environment was deeply shaped by your movement through it -- when walking, running, or climbing revealed aspects of a place that static observation never could. What did the movement add to perception?",
    ],
    ("04_moving_through_world", "04_cognition"): [
        "Walking through an unfamiliar city, your spatial cognition is grounded in locomotion -- you remember routes as sequences of bodily turns, uphill efforts, and landmark encounters. How does the generative model encode spatial knowledge through proprioceptive predictions?",
        "A basketball point guard surveys the court and feels the open passing lane as a bodily impulse in the throwing arm. How does the generative model fuse visual spatial perception with motor prediction in movement cognition?",
        "How does the concept of cognitive maps (Tolman) relate to embodied spatial cognition? In what way are mental maps grounded in the body's locomotor history rather than being abstract geometric representations?",
        "Describe the phenomenon of 'motor imagery' -- mentally rehearsing a movement sequence and feeling the body's simulation of it. What does this tell us about the relationship between motor cognition and physical action?",
        "How does wayfinding (navigating through complex environments) integrate embodied spatial cognition with memory, planning, and decision-making? Describe the felt quality of being oriented versus being lost.",
        "In what way does the hippocampal place cell system (place cells, grid cells, head-direction cells) implement a generative model of the body's position and orientation? How does this neural architecture support Active Inference about location?",
        "Describe the cognitive experience of 'dead reckoning' -- maintaining a sense of position and direction through accumulated movement evidence alone. What bodily signals contribute to this self-localization?",
        "How does embodied spatial cognition develop in children? Describe the progression from crawling-based spatial knowledge to walking-based spatial knowledge, and how the change in locomotor mode changes the cognitive map.",
        "What is the relationship between gesture and spatial thought? When describing a route, people gesture the turns and directions. How does this motor expression of spatial knowledge illustrate the embodied nature of cognition?",
        "Describe the cognitive demands of navigating in three dimensions (climbing, swimming, flying). How does the addition of a vertical axis challenge the generative model's spatial predictions?",
        "How does architectural design shape embodied spatial cognition? Describe how a well-designed building 'thinks for you' by creating environments whose spatial structure supports intuitive navigation.",
        "In what way does the experience of spatial disorientation (being lost, experiencing vertigo, navigating in fog) reveal the normally invisible workings of the body's spatial generative model?",
        "How does the body's spatial cognition handle scale transitions -- moving from a room to a building to a neighborhood to a city? What changes in the generative model's hierarchical organization?",
        "Describe the cognitive difference between knowing a route as a driver versus as a pedestrian versus as a cyclist. How does the mode of locomotion shape the spatial knowledge that the generative model acquires?",
        "What is the relationship between physical exploration (walking through a space) and spatial understanding? How does embodied engagement produce deeper spatial knowledge than studying a map?",
        "How does technology (GPS, maps on phones) change the body's spatial cognitive engagement with the environment? What is gained and lost when navigation is offloaded from embodied cognition to a device?",
        "Reflect on your own experience of spatial cognition. Think of a place you know well -- your home, your workplace, your neighborhood. How is your knowledge of this space stored in your body rather than in abstract mental images?",
    ],
    ("04_moving_through_world", "05_action"): [
        "A capoeira practitioner's ginga flows through continuous weight shifts, arm swings, and torso rotations that are simultaneously defensive, offensive, and expressive. How is this skilled action active inference at full embodiment?",
        "A surfer makes split-second adjustments of ankle, knee, hip, and arm to balance on a moving, changing surface. Describe the continuous action-perception cycle where the body sculpts its relationship with the moving environment.",
        "How does the Active Inference framework explain the difference between reactive movement (flinching from a thrown object) and proactive movement (reaching for an anticipated pass)? What role do temporal predictions play?",
        "Describe the felt quality of locomotor rhythm -- the cadence of walking, running, or cycling that the body maintains automatically. How does the generative model generate and sustain rhythmic motor patterns?",
        "How do skilled movement practices (martial arts, dance, gymnastics) transform the body's action repertoire by building rich libraries of motor predictions? What does this expanded repertoire feel like?",
        "In what way does the concept of dynamic affordances -- action possibilities that change moment to moment as the agent and environment interact -- apply to sports like surfing, skiing, or skateboarding?",
        "Describe the biomechanical concept of degrees of freedom (Bernstein's problem). How does the body-as-moving-agent solve the problem of coordinating dozens of joints and hundreds of muscles into coherent action?",
        "How does the body adapt its action patterns to different surfaces (ice, sand, mud, concrete)? Describe the prediction errors generated by a surface change and the rapid motor recalibration that follows.",
        "What is the role of elastic energy storage (in tendons, fascia, and muscle) in skilled movement? How does the body's biomechanical structure support efficient action that the generative model predicts and exploits?",
        "Describe the experience of 'coupling' between the body and an environmental feature during skilled movement -- the rock climber's hand conforming to the hold, the surfer's feet reading the wave. What Active Inference process produces this intimate body-environment fit?",
        "How does the body manage the transition between qualitatively different movement patterns (walking to running, standing to jumping, swimming to climbing out of the pool)? What prediction errors signal the need for mode switching?",
        "In what way does movement improvisation (freestyle dance, play, spontaneous physical exploration) represent action policies generated in real time from the generative model's creative capacity?",
        "Describe the felt quality of effortful movement (climbing a steep hill, lifting a heavy object) versus effortless movement (gliding downhill, floating in water). How does the body's energy expenditure prediction shape the experience of each?",
        "How do movement-based practices (yoga, tai chi, Alexander Technique, Feldenkrais) retrain the body's habitual action patterns by introducing novel movement that generates prediction errors and prompts model updating?",
        "What is the relationship between breath and movement in skilled physical practice? How does breathing coordination (inhale on extension, exhale on flexion) optimize the body's action efficiency?",
        "Describe the experience of learning a new movement skill (a dance step, a swimming stroke, a yoga pose). Trace the progression from awkward, effortful execution to smooth, efficient performance as prediction errors decrease.",
        "Reflect on a moment of peak physical action -- a time when your body performed at its best, when movement felt fluid, powerful, and precisely right. What was the quality of that embodied experience?",
    ],
    ("04_moving_through_world", "06_learning"): [
        "A child learning to ride a bicycle transitions from jerky over-corrections to imperceptibly small automatic adjustments. Describe this as the progressive reduction of sensorimotor prediction error through embodied learning.",
        "A ballet dancer's arabesque transforms from strained effortfulness to natural grace over years of practice. How does the generative model absorb the biomechanics of the pose into unified motor predictions?",
        "How does the concept of 'motor schema' (Schmidt) relate to Active Inference learning? As the body builds generalized movement programs, what kinds of predictions does the generative model form about classes of movement?",
        "Describe the learning process of adapting to a new movement environment (learning to swim, learning to ski, adjusting to a new bicycle). What prediction errors drive the initial learning, and how does the model eventually accommodate?",
        "What is the relationship between variability and motor learning? Why does early learning involve high movement variability, and how does this exploration serve the generative model's search for optimal motor predictions?",
        "How does observational learning (watching a skilled mover) contribute to motor learning? When you watch someone perform a movement, what happens in your own motor system that prepares you for imitation?",
        "Describe the phenomenon of 'savings' in motor learning -- the rapid relearning of a previously acquired skill after a period of disuse. What does this reveal about the persistence of motor priors in the generative model?",
        "How does the concept of 'transfer' in motor learning (skills in one domain facilitating learning in another) relate to the generative model's capacity for structural generalization across movement contexts?",
        "What role does proprioceptive feedback play in motor learning? How does the progressive refinement of the body's ability to sense its own movement contribute to improved motor performance?",
        "Describe the learning trajectory of spatial navigation in a new environment. From initial disorientation to confident wayfinding, how does the generative model build and refine its spatial predictions?",
        "How does motor learning in older adults differ from motor learning in children? What changes in the generative model's plasticity account for the different rates and qualities of movement learning across the lifespan?",
        "In what way does the experience of 'plateaus' in movement learning (periods of no apparent improvement) reflect restructuring in the generative model that will eventually produce breakthrough performance?",
        "Describe the role of play in movement learning. How does playful exploration (jumping, tumbling, climbing without purpose) build the diverse motor repertoire that underlies skilled movement?",
        "How does rehabilitation after injury (physical therapy, adaptive movement training) represent a specific form of motor relearning? What prediction errors must the generative model resolve to adapt to a changed body?",
        "What is the relationship between aerobic fitness and the rate of motor learning? How does the body's energy availability and cardiovascular capacity influence its ability to acquire new movement skills?",
        "Describe the phenomenon of 'overlearning' in movement -- the continued practice beyond the point of mastery that produces the automaticity and resilience characteristic of expert performance.",
        "Reflect on a movement skill you have developed over time (walking, a sport, a physical practice). Trace the learning arc from awkward beginner to competent mover. What changed in your body's relationship to the movement?",
    ],
    ("04_moving_through_world", "07_communication"): [
        "In partner dance (tango, contact improvisation), the lead communicates the next movement through subtle weight shifts and pressure through the hands. How do two bodies create a shared predictive loop through purely tactile communication?",
        "A basketball team executing a fast break communicates through coordinated movement -- pace changes, head fakes, and timing convey expected positions. How do shared generative models enable movement-based social coordination?",
        "How does the body communicate spatial intention (I am going to turn left, I am about to stop, I want to pass) through postural and kinetic signals that other movers can decode? Describe these non-verbal movement signals.",
        "Describe the concept of 'joint action' (Sebanz, Bekkering, Knoblich) -- the coordination of two or more bodies toward a shared movement goal. How does Active Inference model the alignment of generative models during cooperative movement?",
        "In what way does the experience of synchronized group movement (marching, group dance, rowing) create a felt sense of collective embodiment? What happens to individual body boundaries when many bodies move as one?",
        "How does spatial proxemics (the cultural regulation of interpersonal distance) function as a form of movement-based communication? What bodily signals indicate when someone has entered your personal space?",
        "Describe the communicative function of gait -- how the way someone walks (speed, rhythm, posture, direction) transmits information about their intention, mood, and social status to observers.",
        "How does the body communicate dominance, submission, or affiliation through spatial behavior -- taking up space, yielding space, approaching, retreating? What Active Inference mechanism underlies these spatial social signals?",
        "In what way does moving together through an environment (walking with a companion, hiking with a group) create a form of embodied companionship that differs from stationary conversation?",
        "Describe the communicative challenge of movement in urban environments: how pedestrians, cyclists, and drivers negotiate shared space through implicit, embodied communication of trajectory and intention.",
        "How does the body's spatial behavior in public spaces (choosing a seat, positioning in a queue, navigating a party) communicate social preferences and boundaries? What somatic signals guide these choices?",
        "In what way does the mirror neuron system support the perception and understanding of others' movements? How does observing someone move activate corresponding motor representations in the observer's body?",
        "Describe the communicative dimension of competitive movement (sports, martial arts sparring). How do opponents communicate through feints, probes, and reactions that constitute a dialogue of embodied intentions?",
        "How does the body communicate through the built environment -- choosing paths, modifying spaces, leaving traces of movement? In what way is the arrangement of physical space a form of extended bodily communication?",
        "What is the role of rhythm in movement-based communication? How does shared temporal structure (walking in step, clapping together, breathing in unison) create interpersonal coordination and felt connection?",
        "Describe the experience of 'movement empathy' -- feeling in your own body the effort, grace, or struggle of someone else's movement. How does this somatic resonance function as a communicative channel?",
        "Reflect on a shared movement experience (dance, sport, hiking, or simply walking with someone) where the movement itself was the primary medium of communication. What was communicated that words could not have conveyed?",
    ],
    ("04_moving_through_world", "08_planning"): [
        "A trail runner approaching a technical descent pre-selects foot placements three to five steps in advance, feeling in her ankles which rocks will be stable. How does this embodied planning project expected sensorimotor consequences across future time steps?",
        "A gymnast rehearses the entire vault sequence kinesthetically -- feeling each phase in muscles and joints before taking a step. Describe this pre-movement planning as the generative model evaluating expected free energy of the complete trajectory.",
        "How does route planning integrate embodied spatial knowledge (the felt memory of terrain, effort, and duration) with abstract map knowledge? Describe the felt quality of planning a familiar route versus an unfamiliar one.",
        "In what way does the body's anticipatory postural adjustment (preparing for a movement before it begins) constitute an automatic, pre-cognitive form of movement planning? What does the generative model predict?",
        "Describe the planning process involved in a complex physical task (packing a car, rearranging furniture, cooking a multi-dish meal). How does the body simulate the spatial sequence of actions required?",
        "How does the concept of 'look-ahead' in navigation (scanning the terrain ahead to plan a path) illustrate the generative model's temporal extension into the near future? What sensory channels contribute to this preview?",
        "What is the relationship between physical fitness and the body's movement planning capacity? How does fatigue constrain the range of future movement policies the generative model considers viable?",
        "Describe the planning required for a multi-day trek or expedition. How does the body integrate knowledge of its own energy reserves, terrain difficulty, and time constraints into an embodied plan?",
        "How does the body plan for safety during risky movement (climbing, surfing, skiing near cliffs)? What somatic signals indicate the boundary between acceptable and unacceptable risk?",
        "In team sports, how does the individual player's movement planning integrate with the team's collective strategic plan? Describe the felt quality of executing a planned play in real time.",
        "What is the role of mental rehearsal (imagery) in movement planning? How does the body's kinesthetic simulation of a planned movement sequence prepare the motor system for actual execution?",
        "Describe the experience of improvised movement planning -- navigating an obstacle course, dancing freestyle, or playing in an unstructured environment. How does the body generate plans in real time without deliberation?",
        "How does the body plan the coordination of whole-body movements that involve multiple limbs acting in sequence or simultaneously? Describe the temporal organization of a complex movement plan.",
        "In what way does the seasonal and circadian regulation of activity levels (more movement in summer, less in winter; more energy in the morning, less in the evening) constitute a long-timescale embodied planning process?",
        "How does the experience of watching others perform a planned movement (observing a gymnastics routine, a dance performance, or a surgical procedure) engage the observer's own movement planning systems?",
        "Describe the felt quality of the moment just before a planned movement is initiated -- the coiled readiness of a sprinter in the blocks, the gathered energy of a diver on the board. What is the generative model doing in this pre-launch state?",
        "Reflect on a complex movement task you have planned and executed (a road trip, a physical challenge, a home project). How did your body's spatial and temporal planning contribute to the outcome?",
    ],
    # SECTION-LEVEL for 04_moving_through_world
    ("04_moving_through_world", None): [
        "How does Gibson's concept of affordances redefine the environment from a collection of physical properties to a field of action possibilities directly perceived by the moving body?",
        "Describe the sensorimotor contingency theory (O'Regan and Noe): perception is constituted by the organism's mastery of the lawful regularities between actions and their sensory consequences. How does this apply to moving through space?",
        "How does Active Inference unify the ecological (Gibson) and enactive (Noe) perspectives on embodied movement? What does it mean to say that the agent and environment 'co-constitute' the meaningful world?",
        "Describe the concept of the extended body and tool use (Clark). When a carpenter wields a hammer or a cyclist rides a bike, how does the Markov blanket of the agent extend to include the tool?",
        "How does Maxine Sheets-Johnstone's 'primacy of movement' thesis challenge the assumption that cognition precedes movement? In what way is moving the foundational cognitive act from which all other cognition derives?",
        "Describe the experience of an 'affordance walk' -- moving through your environment with explicit attention to the action possibilities that surfaces, objects, and spaces offer your body. What do you notice?",
        "How does rehabilitation after stroke illustrate the necessity of rebuilding sensorimotor contingencies? What prediction errors must the generative model resolve as it learns the recovering body's new capabilities?",
        "What is the relationship between the hippocampal place cell system and the Active Inference account of spatial navigation? How does the brain implement a generative model of position and orientation?",
        "Describe how the perception of affordances shifts with the body's changing state -- a bench that affords sitting when tired affords stepping-over when energized. What mediates this state-dependent perception?",
        "How does the concept of path integration (maintaining a sense of position through accumulated movement evidence) relate to the generative model's continuous updating of spatial beliefs?",
        "In what way does the experience of moving through natural environments (forests, mountains, rivers) engage the body's evolutionary heritage of ecological perception and spatial navigation?",
        "Describe the embodied experience of speed: how moving fast changes perception, narrows attention, increases arousal, and demands more rapid prediction-action cycling. What does velocity feel like in the body?",
        "How does the concept of 'motor equivalence' (achieving the same goal through different movement patterns) illustrate the generative model's flexibility in selecting action policies?",
        "What is the relationship between exploration (curious movement through unfamiliar terrain) and exploitation (efficient movement through known routes) in the Active Inference framework?",
        "Describe the felt quality of 'being at home' in a physical space -- the sense of familiar affordances, practiced routes, and predictable spatial structure. What does this spatial familiarity reveal about the generative model?",
        "How does the loss of movement capacity (through injury, illness, or aging) change the individual's felt relationship to the physical world? What happens to the perception of affordances when the body can no longer act on them?",
        "Reflect on the central claim of this unit: that to move is to know and to know is to move. How does your own experience of navigating, exploring, and inhabiting physical spaces support this claim?",
    ],
}


# ============================================================================
# LABS DATA - experiential labs for sections 02, 03, 04
# ============================================================================

LABS = {
    # ========================================================================
    # 02_LIVING_PRESENCE LABS
    # ========================================================================
    ("02_living_presence", "01_systems"): """# Lab: Listening to the Living System

## Objective

Experience the body as a self-maintaining living system through sustained somatic attention, discovering that awareness does not need to be created but is already the system's fundamental mode of being. This lab connects autopoiesis and the Markov blanket to the felt experience of sitting with the body's systemic activity.

## Prerequisites

- A quiet space where you can sit undisturbed for 25 minutes
- Comfortable seating (cushion, chair, or bench)
- No prior meditation experience required

## Part 1: The Hum of Self-Maintenance (5 minutes)

Sit comfortably with your eyes closed. Do nothing. Do not try to meditate, relax, or focus. Simply sit and listen inward.

Gradually, you will begin to notice the body's ongoing systemic activity: the heartbeat, the rhythm of breathing, the subtle churning of digestion, the tiny adjustments of muscles maintaining your posture. These processes are happening without your direction. The system is sustaining itself.

In Active Inference terms, you are witnessing the organism's continuous free energy minimization -- the self-regulatory activity that constitutes life itself.

{fill:textarea}(What systemic processes did you notice? List at least five ongoing bodily activities that were happening without your conscious direction.)

## Part 2: The Breathing Membrane (5 minutes)

Bring attention to the boundary between your body and the surrounding air. Notice the coolness of inhaled air at the nostrils. Feel the warmth of exhaled air. Notice where your clothing meets your skin, where the chair supports your body.

Each inhalation draws the outside world in; each exhalation releases something outward. The boundary is not a wall -- it is a living membrane, pulsing with each breath.

In Active Inference, this pulsing boundary is the Markov blanket -- the dynamic interface between internal and external states, sustained by the system's ongoing activity.

{fill:textarea}(Describe the felt quality of the boundary between your body and the world. Was it sharp or diffuse? Did it pulse, shift, or breathe? How did attending to it change your sense of where "you" end and the world begins?)

## Part 3: Autonomic Weather (7 minutes)

Without trying to change anything, observe the body's autonomic shifts over the next seven minutes. The autonomic nervous system is continuously adjusting arousal level, like weather changing across a landscape.

Notice: Is the body calm and settled (ventral vagal)? Mildly alert or activated (sympathetic)? Heavy, sluggish, or withdrawn (dorsal vagal)? You may notice shifts between these states as you sit.

In polyvagal terms, you are observing the three-layered autonomic system that constitutes the physiological foundation of presence. Living presence arises most naturally from the ventral vagal state of calm engagement.

{fill:textarea}(Describe the autonomic weather you observed. Did your state shift during the exercise? What qualities of alertness, calm, or heaviness did you notice? Did any single state predominate?)

## Part 4: The Undivided Whole (5 minutes)

For the final five minutes, release all specific attention and simply be present to the body as a whole. Not the heart, not the breath, not the boundary -- but the entire living system at once.

Contemplative traditions emphasize that the body is not a collection of parts but an undivided whole. When you experience the system as a single, integrated field of awareness, you are witnessing the generative model's unified posterior belief about the organism's current state.

{fill:textarea}(What was the felt quality of experiencing the body as a whole system rather than a collection of parts? Was it possible to hold the entire body in awareness simultaneously? What shifted when you let go of focusing on specific elements?)

## Part 5: Reflection

{fill:textarea}(How did this lab change your understanding of what it means to be a living system? What did you discover about the relationship between awareness and the body's self-maintaining activity?)

## Reflection Table

| Systemic Aspect | What I Noticed | Active Inference Connection |
| --- | --- | --- |
| Self-maintenance | {fill:text} | Continuous free energy minimization sustaining life |
| Boundary (Markov blanket) | {fill:text} | Dynamic interface between internal and external states |
| Autonomic regulation | {fill:text} | Polyvagal states as systemic foundation of presence |
| Undivided wholeness | {fill:text} | Unified posterior belief of the generative model |
""",

    ("02_living_presence", "02_agents"): """# Lab: The Agent Who Dissolves

## Objective

Explore how present-moment awareness reveals agency as an ongoing inferential achievement rather than a fixed property of a controlling self. This lab uses mindful attention to observe the arising and dissolving of the sense of being an agent.

## Prerequisites

- A quiet space for 25 minutes
- Ability to sit and stand
- No prior meditation experience required

## Part 1: Watching the Watcher (5 minutes)

Sit with eyes closed. Bring attention to your breath. After a minute, ask yourself: who is watching the breath? Try to locate the watcher. Is it behind the eyes? In the center of the head? Somewhere else?

You will likely find that the watcher cannot be found as an object. It is not a thing but a process -- the ongoing activity of the generative model attending to itself. The sense of a controlling agent is itself a construction.

{fill:textarea}(When you tried to locate the "watcher," what did you find? Where did the sense of agency seem to reside? Did the search itself change the quality of your experience?)

## Part 2: Voluntary and Involuntary (5 minutes)

Observe three processes with different levels of agency:

1. **Involuntary**: Your heartbeat. Notice it. You are not doing it. Who is the agent here?
2. **Semi-voluntary**: Your breath. Let it go on its own for 30 seconds. Now take three deliberate breaths. Return to automatic. Notice the transition from "breathing happens" to "I am breathing" and back.
3. **Voluntary**: Slowly raise one hand. Notice the intention before the movement. Where does the intention come from? Did "you" create it, or did it arise?

{fill:textarea}(Describe the felt quality of each level of agency. When you moved between automatic and deliberate breathing, where did the sense of "I" appear and disappear?)

## Part 3: Action Without a Doer (7 minutes)

Stand up slowly. Now walk very slowly across the room. With each step, try to catch the moment of intention -- the instant before the body moves. Is there a clearly identifiable "I" who decides to step, or does the step seem to arise from the body's own intelligence?

Many meditators discover that action can proceed with exquisite precision without a felt sense of a central controller. The body is an active inference agent that generates coordinated movement through prediction and correction, not through executive command.

{fill:textarea}(During slow walking, could you identify a clear "decider" who initiated each step? Or did movement seem to arise from a broader, less localized process? Describe the felt quality of agency during very slow, deliberate movement.)

## Part 4: Effortful and Effortless Agency (5 minutes)

Return to sitting. Try two modes of attention:

1. **Effortful**: Forcefully concentrate on the breath. Grip your attention. Try hard to stay focused.
2. **Effortless**: Let attention rest on the breath gently, like a leaf on water. If it drifts, allow the return to be soft.

Notice the paradox: the more you try to be an attentive agent, the more tense and distracted you become. Effortless attention often produces deeper presence.

{fill:textarea}(Describe the somatic difference between effortful and effortless attention. What happened to the sense of agency in each mode? Which produced more sustained presence?)

## Part 5: Reflection

{fill:textarea}(After this lab, how would you describe the relationship between "you" and "your body"? Has your understanding of what it means to be an agent changed?)

## Reflection Table

| Dimension of Agency | What I Observed | Active Inference Connection |
| --- | --- | --- |
| The watcher | {fill:text} | Generative model attending to its own processes |
| Voluntary/involuntary spectrum | {fill:text} | Different levels of motor prediction hierarchy |
| Action without a doer | {fill:text} | Agency as process, not entity |
| Effortful vs. effortless | {fill:text} | Precision optimization vs. forceful control |
""",

    ("02_living_presence", "03_perception"): """# Lab: Seeing Before Naming

## Objective

Explore how present-moment awareness transforms perception by restoring the precision weighting on direct sensory evidence, revealing how much ordinary perception is top-down prediction rather than fresh encounter. This lab cultivates the contemplative quality of "beginner's mind."

## Prerequisites

- A quiet space for 25 minutes
- A small object (fruit, stone, leaf, or any everyday item)
- Optional: a raisin or small piece of food

## Part 1: Bare Perception (5 minutes)

Sit with eyes closed for one minute, settling into bodily awareness. Then open your eyes very slowly. Before naming anything, simply receive the visual field as it is -- colors, shapes, textures, light, shadow. Do not label "wall," "window," "floor." Let the visual field exist as pure visual sensation.

You are attempting to perceive before the generative model's categories take over -- to experience the raw sensory evidence at the Markov blanket before top-down predictions explain it away.

{fill:textarea}(Describe what you saw when you tried to perceive before naming. Was it possible to see without categorizing? What was the felt quality of pre-conceptual visual experience?)

## Part 2: The Raisin Exercise (7 minutes)

Take a raisin (or small piece of food) and examine it as if you have never seen such an object before.

1. **Visual**: Look at it closely. Notice wrinkles, color variations, translucency, texture. Spend two full minutes just looking.
2. **Tactile**: Roll it between your fingers. Feel its texture, weight, give. Notice what the generative model predicts about the next sensation.
3. **Olfactory**: Hold it near your nose. Breathe in. Notice the aroma and any salivary response.
4. **Gustatory**: Place it on your tongue. Do not chew. Feel it in your mouth. Then chew once, slowly. Notice the explosion of taste.

This classic mindfulness exercise reveals how much of ordinary perception is prediction rather than direct experience. Living presence restores the richness of sensory contact.

{fill:textarea}(Describe what you noticed about the raisin that you would normally miss. What was surprising? How did the experience differ from ordinary eating?)

## Part 3: Sound Bath (5 minutes)

Close your eyes and open your hearing to all sounds -- near and far, loud and soft, pleasant and neutral. Do not try to identify what is making the sounds. Simply receive the sonic field as pure auditory sensation.

Notice how quickly the generative model labels sounds ("that is a car," "that is a bird"). Each time you notice a label appearing, let it go and return to the bare quality of the sound itself.

{fill:textarea}(What happened when you tried to hear sounds without identifying their source? Could you sustain bare auditory perception, or did labels keep appearing? How did the quality of listening change?)

## Part 4: Shifting State, Shifting Perception (5 minutes)

1. First, tense your body: clench your fists, tighten your jaw, hunch your shoulders. Hold for 30 seconds. While tense, look around the room and notice the felt quality of what you see.
2. Now release completely: drop your shoulders, soften your face, let your hands open. Breathe deeply three times. Look around the room again.

Notice how the same visual environment is perceived differently through a tense body versus a relaxed one. The body's interoceptive state colors perception.

{fill:textarea}(How did the room look and feel different when your body was tense versus relaxed? What changed in the quality of colors, spatial relationships, or the overall atmosphere?)

## Part 5: Reflection

{fill:textarea}(After this lab, what do you understand about the relationship between bodily state and perception? How does present-moment awareness change what you see, hear, and feel?)

## Reflection Table

| Perceptual Dimension | What I Noticed | Active Inference Connection |
| --- | --- | --- |
| Pre-conceptual seeing | {fill:text} | Sensory evidence before top-down prediction |
| Mindful tasting | {fill:text} | Increased precision on bottom-up signals |
| Bare hearing | {fill:text} | Reducing categorical prediction, restoring openness |
| State-dependent perception | {fill:text} | Interoceptive priors coloring exteroceptive experience |
""",

    ("02_living_presence", "04_cognition"): """# Lab: Watching Thoughts Arise and Dissolve

## Objective

Explore the embodied nature of cognition through present-moment observation of the thinking process, discovering that thoughts have somatic signatures, arise without a thinker, and can be observed without being believed. This lab develops meta-cognitive awareness through embodied practice.

## Prerequisites

- A quiet space for 25 minutes
- Comfortable seating
- No prior meditation experience required

## Part 1: Where Do Thoughts Come From? (5 minutes)

Sit comfortably with eyes closed. Anchor your attention on the breath. Now wait for a thought to arrive. Do not invite one or try to think. Simply wait.

When a thought appears, notice: Did you choose it? Did you know what it would be before it arrived? Thoughts appear unbidden, like bubbles rising through water. In Active Inference, thoughts are predictions generated by the model -- not commands issued by a thinker.

Let the thought pass and wait for the next one. Observe five or six thoughts arriving and departing.

{fill:textarea}(Where did your thoughts seem to come from? Could you predict what the next thought would be? What was the quality of the gap between thoughts?)

## Part 2: The Somatic Signature of Thought (7 minutes)

Continue sitting. When the next thought arises, rather than attending to its content, attend to its bodily feel. Every thought has a somatic signature:

- "I need to call my mother" -- notice the tug in the chest.
- "What if I fail?" -- notice the tightening in the throat.
- "This is boring" -- notice the heaviness in the body.

For each of five or six thoughts, label the thought content briefly, then scan for its bodily accompaniment. Where does it live in the body? What is its texture -- heavy, buzzy, tight, warm, sharp?

{fill:textarea}(For each thought you observed, describe its content and its somatic signature. Where in the body did each thought register? What was its felt texture?)

## Part 3: Decentering -- The Thought Is Not the Thinker (5 minutes)

Practice the following shift: Instead of thinking "I am anxious," notice "a thought with an anxious quality is arising in awareness." Instead of "I should have done differently," notice "a regret-prediction is being generated by the model."

This shift -- cognitive decentering -- creates a gap between the thought and the thinker. You are not the thought; you are the awareness in which the thought appears. In Active Inference, decentering means adding a meta-cognitive layer that reduces precision on thought content while increasing precision on the process of thinking.

{fill:textarea}(Were you able to observe thoughts as events rather than truths? What was the felt quality of the space between the thought and the observer? How did decentering change your relationship to the thought's content?)

## Part 4: Breath as Anchor (5 minutes)

Notice how the mind naturally oscillates between present-moment awareness (the breath) and cognitive wandering (thoughts about past and future). Each time you notice wandering, gently return to the breath. Do not judge the wandering -- simply notice and return.

Track each oscillation: present (breath) --> wandering (thought) --> noticing (awareness) --> returning (present). How many cycles can you observe in five minutes?

{fill:textarea}(Approximately how many present-wandering-noticing-returning cycles did you observe? Did the quality of wandering or returning change over the five minutes? What was the felt quality of the moment of noticing?)

## Part 5: Reflection

{fill:textarea}(After this lab, how would you describe the relationship between your body, your thoughts, and "you"? What did you discover about the embodied nature of cognition?)

## Reflection Table

| Cognitive Dimension | What I Observed | Active Inference Connection |
| --- | --- | --- |
| Thought origination | {fill:text} | Predictions generated by the model, not chosen by a self |
| Somatic signatures | {fill:text} | Interoceptive correlates of cognitive predictions |
| Decentering | {fill:text} | Meta-cognitive precision reweighting |
| Present-moment oscillation | {fill:text} | Oscillation between sensory grounding and counterfactual inference |
""",

    ("02_living_presence", "05_action"): """# Lab: Slow Motion -- The Body Reveals Its Intelligence

## Objective

Experience action as continuous embodied inference by dramatically slowing movement to the speed of conscious awareness, making visible the prediction-verification cycle that is normally too rapid to observe.

## Prerequisites

- A space where you can stand and walk slowly for 25 minutes
- Comfortable, non-restrictive clothing
- Bare feet recommended

## Part 1: The Slowest Hand (5 minutes)

Stand or sit comfortably. Place your hands on your thighs. Very slowly -- as slowly as you possibly can -- begin to raise one hand. Move so slowly that an observer might not notice the movement for several seconds.

Feel: the moment the muscles first engage, the shifting distribution of weight in the forearm, the proprioceptive signals from each finger as they lift from the thigh, the changing pull of gravity as the hand rises.

Pause at several heights and notice: what does the generative model predict will happen next? Can you feel the "pull" of the expected trajectory?

{fill:textarea}(Describe the micro-experience of ultra-slow hand raising. What did you notice that you never notice during ordinary movement? Where did you feel the model's predictions? What was the quality of pausing mid-movement?)

## Part 2: Walking as If for the First Time (7 minutes)

Stand at one end of your space. Walk across the room so slowly that each step takes at least five seconds. Decompose each step into its micro-phases:

1. **Intention** -- the felt leaning-toward before the foot lifts
2. **Lifting** -- the foot breaking contact with the ground
3. **Moving** -- the leg swinging forward through space
4. **Placing** -- the foot descending toward the ground
5. **Contact** -- the moment of touch, the weight transferring
6. **Shifting** -- the full weight settling onto the forward foot

For each phase, notice the gap (or match) between what the body predicted and what it actually felt. This is the action-perception loop made visible.

{fill:textarea}(Describe your experience of ultra-slow walking. Which phase was most surprising? Could you feel the prediction-verification cycle? What happened to the sense of time?)

## Part 3: Affordance Pause (5 minutes)

Walk at normal speed through your environment. Each time you encounter an object that invites action (a door handle to grasp, a chair to sit in, a light switch to flip), pause before acting. Hold the intention without executing it. Feel the body's readiness -- the affordance pulling at the motor system.

This pause between perceiving an affordance and acting on it creates a contemplative gap that reveals the normally automatic flow of embodied prediction and action.

{fill:textarea}(Describe three affordances you paused before acting on. What did the body's readiness feel like? Was it difficult to pause, or did the pause enrich the experience of action?)

## Part 4: Breath-Synchronized Movement (5 minutes)

Stand with arms at your sides. Coordinate simple movements with the breath:

1. Inhale: slowly raise your arms to shoulder height. Exhale: slowly lower them.
2. Inhale: slowly rise onto your toes. Exhale: slowly settle back.
3. Inhale: slowly turn your head to the right. Exhale: return to center.

Notice how breath coordination creates a rhythm that unifies interoceptive and proprioceptive awareness. The body is simultaneously breathing and moving as a single, coordinated inference.

{fill:textarea}(How did coordinating movement with breath change the quality of action? What was the felt quality of the breath-movement unity? Did any movement feel more natural with a particular breath phase?)

## Part 5: Reflection

{fill:textarea}(What did slowing movement reveal about the body's intelligence? How has this lab changed your understanding of the relationship between prediction, action, and awareness?)

## Reflection Table

| Action Dimension | What I Noticed | Active Inference Connection |
| --- | --- | --- |
| Ultra-slow movement | {fill:text} | Action-perception loop made visible |
| Micro-phases of walking | {fill:text} | Step-by-step prediction verification |
| Affordance pause | {fill:text} | Gap between affordance detection and policy execution |
| Breath-movement unity | {fill:text} | Interoceptive-proprioceptive integration |
""",

    ("02_living_presence", "06_learning"): """# Lab: Tracking the Learning Body

## Objective

Observe the process of embodied learning in real time by attempting a novel somatic task while maintaining present-moment awareness, then tracking how the body's predictions shift over repeated practice.

## Prerequisites

- A quiet space for 25 minutes
- A journal and pen
- Willingness to attempt a novel physical task

## Part 1: Baseline -- What the Body Knows Now (5 minutes)

Sit comfortably with eyes closed. Take three deep breaths and arrive in present-moment awareness. Now scan your body from feet to head, noting the current state of the generative model -- areas of ease, tension, numbness, sensitivity.

This is your baseline: the body's current predictive landscape before new learning begins.

{fill:textarea}(Describe your baseline body scan. What areas felt most alive, most tense, most numb? What was the overall quality of somatic awareness?)

## Part 2: The Novel Challenge (10 minutes)

Choose one of the following novel somatic tasks (or invent your own):

**Option A -- Balancing**: Stand on one foot with eyes closed. Notice the body's constant micro-adjustments. Each wobble is a prediction error; each correction is the model updating. Practice for 2 minutes per foot, then compare sides.

**Option B -- Non-dominant hand**: Write your name slowly with your non-dominant hand. Notice the effort, the imprecision, the large prediction errors. Write it five times, noticing improvement.

**Option C -- Reverse breathing**: Inhale for 4 counts, hold for 4, exhale for 8. This reverses the typical breathing ratio. Notice how the body initially resists the unfamiliar pattern, then gradually accommodates.

Regardless of which you choose, maintain mindful awareness throughout. The goal is not to perform well but to observe the learning process as it unfolds in the body.

{fill:textarea}(Which task did you choose? Describe the experience of attempting it. What prediction errors arose? How did the body respond to novelty? Did you notice improvement over the practice period?)

## Part 3: Noticing Micro-Shifts (5 minutes)

Return to sitting. Close your eyes and perform another body scan, identical to Part 1. Compare this scan with your baseline.

Has anything shifted? Learning often produces subtle but noticeable changes: a region that was tense may have softened; an area that was numb may have become more vivid; the overall quality of somatic awareness may have subtly changed.

{fill:textarea}(What differences did you notice between the baseline scan and this post-learning scan? Were there any areas that changed in quality, sensitivity, or tone? What does this suggest about how the generative model updates?)

## Part 4: Journaling the Learning Process (5 minutes)

Reflect on the learning process you just observed. In your journal, write brief responses to:

1. What was the felt quality of encountering novelty (the first attempt)?
2. What was the felt quality of early improvement (the third or fourth attempt)?
3. What prediction errors were most prominent?
4. Where in the body was learning most evident?

{fill:textarea}(Share your journal responses. What patterns do you notice in the trajectory from novelty to familiarity? How does the body communicate its learning process through felt sensation?)

## Part 5: Reflection

{fill:textarea}(How does observing the body's learning process in real time change your understanding of what learning is? What did you discover about the relationship between present-moment awareness and the capacity to learn?)

## Reflection Table

| Learning Dimension | What I Observed | Active Inference Connection |
| --- | --- | --- |
| Baseline state | {fill:text} | Current generative model predictions |
| Novelty response | {fill:text} | Large prediction errors from unfamiliar patterns |
| Micro-improvement | {fill:text} | Rapid parameter updating reducing free energy |
| Post-learning shift | {fill:text} | Updated priors in the generative model |
""",

    ("02_living_presence", "07_communication"): """# Lab: Presence Between Bodies

## Objective

Explore embodied communication through exercises in shared presence, discovering how generative models align through non-verbal channels and how the quality of one's own presence transforms the quality of interpersonal exchange.

## Prerequisites

- A partner willing to participate (or modified solo exercises are provided)
- A quiet space for 25 minutes
- Two chairs facing each other

## Part 1: Silent Sitting Together (5 minutes)

Sit facing your partner at a comfortable distance (about three feet). Both close your eyes and spend one minute settling into individual breath awareness. Then open your eyes with a soft gaze (not staring, not avoiding). Simply be present with your own embodied experience while remaining aware of the other's presence.

Make no effort to communicate. Simply notice what happens between two present bodies.

(If solo: Sit facing a mirror. Maintain soft eye contact with your own reflection.)

{fill:textarea}(What did you notice in the shared silence? Did your breathing change? Did you feel the other's presence in your body? What was the quality of the space between you?)

## Part 2: Breath Synchronization (5 minutes)

With eyes gently open, begin to notice your partner's breathing rhythm. Without forcing it, allow your breath to naturally synchronize -- inhaling and exhaling together. If synchronization happens, notice the felt quality. If it does not, notice that too.

This spontaneous synchronization is an example of coupled inference: two generative models aligning through shared sensory channels.

(If solo: Listen to a recording of ocean waves or slow music and synchronize your breath with the rhythm.)

{fill:textarea}(Did breath synchronization occur? If so, what was the felt quality? If not, what seemed to prevent it? How did the attempt to synchronize change your awareness of the other person?)

## Part 3: Somatic Listening (7 minutes)

One person speaks for three minutes about something they are currently feeling (not a story, but a present-moment report of felt experience). The listener does not respond verbally. Instead, the listener brings full attention to their own body, tracking the sensations that arise in response to the speaker's words, tone, and presence.

After three minutes, switch roles.

(If solo: Listen to a recording of someone speaking from emotion -- a podcast interview, a therapy session recording. Track your body's response.)

{fill:textarea}(As listener, what did you feel in your body while the other person spoke? Where did their communication register somatically -- chest, belly, throat, shoulders? As speaker, how did the quality of being heard by a fully present listener affect your experience?)

## Part 4: Authentic Speaking (5 minutes)

Take turns speaking for two minutes each. Before speaking, pause. Feel into the body. Wait until words arise from felt experience rather than from cognitive rehearsal. Speak slowly, from the body, pausing whenever the felt source of the words needs time to refresh.

The listener simply receives, with full bodily presence.

{fill:textarea}(How did speaking from felt experience differ from speaking from thought? What was the quality of the words that arose from the body? How did the listener's presence affect the speaker's capacity for authentic expression?)

## Part 5: Reflection

{fill:textarea}(What did this lab reveal about the role of bodily presence in communication? How does the quality of one's own embodied awareness transform the quality of interpersonal exchange?)

## Reflection Table

| Communication Dimension | What I Noticed | Active Inference Connection |
| --- | --- | --- |
| Silent shared presence | {fill:text} | Non-verbal generative model alignment |
| Breath synchronization | {fill:text} | Coupled inference through respiratory signals |
| Somatic listening | {fill:text} | Cross-Markov-blanket interoceptive resonance |
| Authentic speaking | {fill:text} | Minimizing divergence between felt and expressed |
""",

    ("02_living_presence", "08_planning"): """# Lab: Feeling into the Future

## Objective

Experience planning as an embodied, present-moment activity by using somatic simulation to evaluate possible futures, discovering that the body's wisdom often precedes and surpasses cognitive deliberation.

## Prerequisites

- A quiet space for 25 minutes
- A genuine decision you are currently facing (even a small one)
- Journal and pen

## Part 1: Arriving in the Present (3 minutes)

Before planning the future, establish present-moment grounding. Sit comfortably with eyes closed. Take ten slow breaths. With each exhale, allow the body to settle more deeply into stillness. Feel the weight of the body, the temperature of the air, the rhythm of the heartbeat.

Planning from presence produces different results than planning from agitation. The autonomic state of the body shapes the quality of future-oriented thinking.

{fill:textarea}(Describe the quality of your body's state after settling. What is the autonomic weather right now -- calm, restless, heavy, alert? How does this state feel as a starting point for planning?)

## Part 2: Somatic Simulation of Futures (10 minutes)

Bring your decision to mind. Identify two or three options.

For each option, close your eyes and vividly imagine living with that choice for the next six months. Do not analyze pros and cons. Instead, let the imagined future unfold like a movie and track what happens in your body:

- **Option A**: Imagine choosing this path. What does your chest do? Your breathing? Your belly? Your jaw? Rate the overall felt quality on a spectrum: constricting <--> expanding, heavy <--> light, cold <--> warm.

- **Option B**: Clear the slate with three deep breaths. Now imagine choosing this path. Same body scan. Same spectrum rating.

- **Option C** (if applicable): Same process.

In Active Inference, you are running the generative model's counterfactual simulations and reading the expected free energy through interoceptive signals. The body is evaluating futures through somatic prediction.

{fill:textarea}(For each option, describe the somatic response. What did your body "say" about each possible future? Did the body have a clear preference? Did it differ from what your analytical mind would have chosen?)

## Part 3: The Body's Horizon (5 minutes)

Shift temporal scale. First, imagine what you will do in the next five minutes. Notice the somatic quality -- probably crisp, specific, localized.

Next, imagine next week. The somatic quality shifts -- more diffuse, less specific, more atmospheric.

Now imagine five years from now. The felt quality becomes vague, mood-like, almost impossible to ground in specific sensation.

These shifts reflect the generative model's temporal depth -- the body's decreasing predictive precision as it projects further into the future.

{fill:textarea}(Describe how the somatic quality of imagining the future changed across the three time horizons. At which scale was the felt sense most vivid? At which scale was it most diffuse?)

## Part 4: Intention Setting from Presence (5 minutes)

Return to the breath. Let go of the specific decision. Instead, invite the body to generate its own intention for the coming day. Do not think of an intention. Feel for one.

You may sense a word, an image, a quality, or a direction. It might be "gentleness," "courage," "curiosity," "slowness," or something with no name. Let it arrive from the body's own wisdom.

{fill:textarea}(What intention arose from the body? Was it what you expected? How does body-generated intention differ from mind-generated goal-setting? What did the chosen intention feel like somatically?)

## Part 5: Reflection

{fill:textarea}(How does planning from embodied presence differ from planning from cognitive analysis? In what ways can the body's somatic wisdom complement or correct the mind's deliberative planning?)

## Reflection Table

| Planning Dimension | What I Experienced | Active Inference Connection |
| --- | --- | --- |
| Somatic simulation | {fill:text} | Expected free energy evaluated through interoceptive prediction |
| Temporal horizon | {fill:text} | Decreasing precision at greater temporal depth |
| Body-generated intention | {fill:text} | Policy selection from deep generative model priors |
| Present-centered planning | {fill:text} | Autonomic state shaping the quality of anticipation |
""",

    # SECTION-LEVEL lab for 02_living_presence
    ("02_living_presence", None): """# Lab: Twenty Minutes of Living Presence

## Objective

Integrate the themes of this unit through a sustained sitting practice that moves through the body-as-system, attention-as-precision, breath-as-inference, and present-moment awareness as optimal free energy minimization.

## Prerequisites

- A quiet space for 25 minutes
- A timer set for 20 minutes (with a gentle sound)
- Comfortable seating on a cushion or chair

## Part 1: Arriving (3 minutes)

Sit down and close your eyes. For the first three minutes, do not try to meditate. Simply arrive. Feel the weight of the body, the temperature of the air, the ambient sounds. Let the body settle at its own pace, the way a snow globe settles when you stop shaking it.

{fill:textarea}(Describe the process of arriving. How long did it take for the body to begin to settle? What was the quality of the transition from doing to being?)

## Part 2: Breath as Home Base (5 minutes)

Bring attention to the natural rhythm of the breath at the nostrils. Do not change the breath; simply observe it. When attention wanders -- to thoughts, sounds, body sensations -- notice the wandering itself (this is a prediction error: the model expected breath-focus but generated something else), and gently return.

Track the oscillation: present with breath --> wandering --> noticing --> returning. Each return strengthens the precision weighting on present-moment interoceptive signals.

{fill:textarea}(How many times did attention wander and return during the five minutes? Did the quality of the wandering or the returning change over time? What was the felt quality of the breath as a home base?)

## Part 3: Open Awareness (5 minutes)

Release the focus on the breath and open awareness to everything at once -- sounds, bodily sensations, the visual field behind closed eyelids, the felt sense of the room. Do not select or reject any element. Simply receive what is present.

This is choiceless awareness: the generative model attending to the full field of sensory evidence without prioritizing any single channel.

{fill:textarea}(Describe the quality of open awareness. Was it spacious or overwhelming? Did certain sensations pull attention more strongly than others? How did this mode differ from focused breath attention?)

## Part 4: Stillness and Movement (5 minutes)

For the remaining time, simply sit. If the body wants to fidget, notice the impulse without acting on it. If stillness deepens, let it deepen. If restlessness arises, let it arise and dissolve. You are watching the body's moment-to-moment self-regulation in real time.

When the timer sounds, remain still for three additional breaths before opening your eyes.

{fill:textarea}(What happened during the final period of open sitting? Did stillness deepen, or did restlessness arise? What was the quality of the body's self-regulation? What was the felt quality of the moment before and after the timer sounded?)

## Part 5: Reflection

{fill:textarea}(What did you learn about living presence through this sustained sitting practice? How does the experience of sitting in awareness for twenty minutes differ from what you expected?)

## Reflection Table

| Practice Phase | What I Experienced | Active Inference Connection |
| --- | --- | --- |
| Arriving | {fill:text} | The system settling into baseline predictions |
| Breath focus | {fill:text} | Precision weighting on interoceptive signals |
| Open awareness | {fill:text} | Balanced precision across all sensory channels |
| Stillness | {fill:text} | The organism's free energy minimization in rest |
""",
}

# I'll generate the remaining labs programmatically by section/submodule theme
# For sections 03 and 04, we need experiential labs based on intuitive knowing and movement

LABS.update({
    # ========================================================================
    # 03_INTUITIVE_KNOWING LABS
    # ========================================================================
    ("03_intuitive_knowing", "01_systems"): """# Lab: The Expert Body as Diagnostic System

## Objective

Explore how the body functions as an integrated diagnostic system by practicing rapid holistic assessment in a familiar domain, noticing the difference between sequential analytical processing and instantaneous systemic recognition.

## Prerequisites

- A quiet space for 25 minutes
- 5-6 objects from a domain you know well (e.g., different teas, spices, fabrics, sounds, or images)
- Journal and pen

## Part 1: Analytical Mode (7 minutes)

Choose your set of objects (teas, spices, fabrics, or another domain). Examine the first object slowly and analytically. If it is a spice, name its color, texture, aroma component by component. Write each observation as a separate data point.

This is novice-mode processing: sequential, explicit, effortful. The generative model is assembling information piece by piece.

{fill:textarea}(Describe your analytical assessment of the first object. How many separate features did you identify? How long did it take? What was the quality of effort involved?)

## Part 2: Holistic Mode (7 minutes)

Now move through the remaining objects rapidly -- spending no more than 10 seconds with each. Do not analyze. Simply receive each object as a whole gestalt. Notice the immediate, pre-verbal impression: pleasant/unpleasant, familiar/novel, high-quality/low-quality.

You are switching from sequential analysis to systemic pattern recognition -- the mode that characterizes expert intuitive assessment.

{fill:textarea}(Describe your rapid, holistic impressions of each object. Were you able to form a global assessment in under 10 seconds? How did the quality of knowing differ from the analytical approach? Where in the body did the holistic impression register?)

## Part 3: Cross-Modal Integration (5 minutes)

Select one object and engage it through as many sensory channels as possible simultaneously: sight, touch, smell, and (if appropriate) taste and hearing. Rather than attending to each sense separately, try to receive them all at once as a single, integrated experience.

Expert systems produce holistic assessments because their Markov blankets integrate multiple sensory channels simultaneously, feeding a generative model that has learned unified patterns rather than isolated features.

{fill:textarea}(What was the quality of multi-sensory integration? Were you able to hold all channels in awareness simultaneously? Did the integrated impression differ from what any single sense provided alone?)

## Part 4: The Reliability Question (5 minutes)

Return to your holistic impressions from Part 2. For each rapid assessment, ask: how confident am I in this judgment? Rate your confidence from 1 (guessing) to 5 (certain).

Now consider: in which areas of your life do you make rapid, confident assessments that prove reliable? Where is your intuitive system well-calibrated, and where might it be biased?

{fill:textarea}(Rate your confidence in each holistic assessment. In which domains of your life is your intuitive systemic assessment most reliable? Where might it be less trustworthy? What distinguishes a well-calibrated intuitive system from a biased one?)

## Part 5: Reflection

{fill:textarea}(What did this lab reveal about the difference between analytical and intuitive knowing? How does the body-as-system process information differently when operating in holistic versus sequential mode?)

## Reflection Table

| Mode of Knowing | What I Noticed | Active Inference Connection |
| --- | --- | --- |
| Analytical (sequential) | {fill:text} | Explicit, high-precision processing of individual features |
| Holistic (systemic) | {fill:text} | Compressed pattern recognition through integrated priors |
| Cross-modal integration | {fill:text} | Unified Markov blanket processing across sensory channels |
| Confidence calibration | {fill:text} | Precision weighting on the system's own predictions |
""",

    ("03_intuitive_knowing", "02_agents"): """# Lab: Acting from the Gut

## Objective

Explore the embodied agent's capacity for rapid, intuitive action by practicing recognition-primed decision making in a timed exercise, then comparing the quality of gut-level choices with deliberated ones.

## Prerequisites

- A quiet space for 25 minutes
- A set of 10 photographs (from magazines, phones, or printed) showing diverse faces, landscapes, or scenes
- A timer
- Journal and pen

## Part 1: Rapid Judgment (5 minutes)

Spread your photographs before you. Give yourself exactly 3 seconds per image. For each, notice the first gut-level response: approach or avoid, trust or distrust, interest or indifference. Do not think. Let the body's immediate response speak.

Record each gut response with a single word or symbol.

{fill:textarea}(Record your rapid gut response to each image. What was the quality of these instant judgments -- where in the body did they arise? Were they clear or ambiguous?)

## Part 2: Deliberated Judgment (5 minutes)

Now go through the same images slowly, spending one minute with each of your top three selections. Analyze deliberately: what specifically makes this image appealing or unappealing? What visual features, memories, or associations are you drawing on?

Compare your deliberated assessments with your gut responses. Do they agree or diverge?

{fill:textarea}(For each of the three images, how did deliberated analysis compare with gut response? Where they agreed, what does that suggest about your intuitive model? Where they diverged, what might explain the discrepancy?)

## Part 3: Action Under Pressure (7 minutes)

Play a simple game with yourself: arrange the 10 images in order of preference in under 30 seconds (use a timer). Then do it again, with unlimited time.

Notice the felt quality of acting from time pressure (the gut agent) versus acting from leisure (the deliberating agent). Which ordering do you prefer? Which feels more authentic?

{fill:textarea}(How did the two orderings compare? What was the felt quality of rapid versus deliberate sorting? Did the pressured ordering reveal preferences that deliberation obscured or confirmed?)

## Part 4: Trusting the Body's Agent (5 minutes)

Sit quietly with eyes closed. Think of a current situation in your life where you need to make a choice. Rather than thinking through the options, ask the body directly: "What do you want to do?" Wait. Notice what arises somatically -- a leaning, a pulling, an opening, a closing.

The body-as-agent often has a clear preference that the mind has been debating endlessly.

{fill:textarea}(What did the body's agent communicate when asked directly? Was the somatic signal clear or vague? Did it match or contradict your cognitive analysis?)

## Part 5: Reflection

{fill:textarea}(What did this lab reveal about the relationship between gut-level agency and deliberative reasoning? In what situations should you trust the embodied agent's rapid assessment?)

## Reflection Table

| Dimension | What I Noticed | Active Inference Connection |
| --- | --- | --- |
| Rapid gut response | {fill:text} | Compressed inference from deep embodied priors |
| Deliberated analysis | {fill:text} | Explicit, sequential processing at higher model levels |
| Time pressure | {fill:text} | Forced reliance on fast, automatic prediction |
| Body's direct preference | {fill:text} | Policy selection from deep somatic evaluation |
""",

    ("03_intuitive_knowing", "03_perception"): """# Lab: Training the Expert Eye

## Objective

Experience how attention and practice transform perception from effortful analysis to rapid pattern recognition, illustrating the development of intuitive perceptual expertise through a structured observation exercise.

## Prerequisites

- A quiet space for 25 minutes
- A complex visual scene (a busy photograph, a natural scene, or a view from a window)
- Timer and journal

## Part 1: First Glance (3 minutes)

Look at your chosen scene for exactly 5 seconds. Close your eyes. Write down everything you noticed. Then look again for 5 seconds and add anything new.

This simulates novice perception: effortful, incomplete, serial.

{fill:textarea}(What did you notice in the first 5 seconds? What did you add in the second look? How much of the scene escaped your initial perception?)

## Part 2: Sustained Observation (10 minutes)

Now spend 10 full minutes observing the same scene. Do not analyze or name. Simply look with relaxed, receptive attention. Let the scene reveal itself to you.

Notice how perception changes over time: initially you see the obvious features, but gradually subtler details, relationships, and patterns emerge. Colors become richer, spatial depth increases, and previously invisible elements appear.

{fill:textarea}(What emerged through sustained observation that was invisible in the first glance? Describe at least five things you noticed after 5 minutes that you missed initially. How did the quality of seeing change over the 10 minutes?)

## Part 3: Pattern Recognition (5 minutes)

Now look at the scene through different "lenses":

1. **Color patterns**: Notice only the distribution and relationship of colors. What patterns emerge?
2. **Shape patterns**: Notice only geometric relationships -- lines, curves, repetitions.
3. **Movement patterns**: Notice anything that moves -- light shifts, leaves, shadows, people.

Each lens highlights different features, demonstrating how the generative model's predictions shape what is perceived.

{fill:textarea}(What did each perceptual lens reveal? How did deliberately shifting your focus change what appeared salient? Which lens produced the most surprising observations?)

## Part 4: Closing Your Eyes -- What Remains? (5 minutes)

Close your eyes and reconstruct the scene from memory. Notice what your generative model retained most vividly versus what has already faded. The most vivid elements are the ones your model weighted most heavily with precision.

Now open your eyes briefly and check: what did you remember accurately? What did you distort? What did you forget entirely?

{fill:textarea}(Describe your recalled image versus the actual scene. What was most vivid in memory? What was distorted or missing? What does this reveal about your generative model's priorities?)

## Part 5: Reflection

{fill:textarea}(How did sustained, deliberate observation change the quality of your perception? What does this exercise reveal about the development of perceptual expertise and the role of attention in shaping what we see?)

## Reflection Table

| Perceptual Mode | What I Noticed | Active Inference Connection |
| --- | --- | --- |
| First glance (novice) | {fill:text} | Sparse model with limited predictions |
| Sustained attention | {fill:text} | Progressive refinement of perceptual precision |
| Pattern lenses | {fill:text} | Top-down predictions shaping bottom-up perception |
| Memory reconstruction | {fill:text} | Generative model's retained predictions vs. actual evidence |
""",

    ("03_intuitive_knowing", "04_cognition"): """# Lab: When the Body Knows Before the Mind

## Objective

Explore the relationship between somatic signals and cognitive judgment by tracking bodily responses during a series of evaluation tasks, discovering moments when the body's assessment precedes and informs conscious thought.

## Prerequisites

- A quiet space for 25 minutes
- A set of 8-10 brief texts (quotes, short paragraphs, or statements) -- some true/wise, some false/misleading
- Journal and pen

## Part 1: Body-First Evaluation (7 minutes)

Read each statement or quote slowly. Before evaluating it intellectually, scan your body for its response. Does the statement produce a felt sense of rightness (opening, settling, warmth) or wrongness (tightening, unease, contraction)?

Record the body's verdict before writing your intellectual analysis.

{fill:textarea}(For each statement, describe the body's initial response and then your intellectual evaluation. How often did they agree? Where they disagreed, which proved more accurate upon reflection?)

## Part 2: The Somatic "Aha" (5 minutes)

Recall a recent moment of insight -- a time when something suddenly made sense, when you "got it." Relive this moment somatically. Where in the body did the insight register? What was the felt quality -- a release, an opening, a warming, a settling?

The "aha" moment has a distinctive somatic signature that is consistent across individuals: a sudden reduction in cognitive free energy experienced as physical relief and opening.

{fill:textarea}(Describe the somatic signature of your "aha" moment. Where did it register? What was the felt quality before and after the insight? How did the body know that understanding had arrived?)

## Part 3: Confusion as Bodily Experience (5 minutes)

Now recall a moment of genuine confusion -- a time when you could not understand something despite trying. Relive the somatic experience. What did confusion feel like in the body?

Confusion is elevated cognitive free energy experienced somatically: the generative model cannot find a good fit between its predictions and the incoming information.

{fill:textarea}(Describe the somatic experience of confusion. Where did it register -- forehead, chest, stomach? What was its quality -- pressure, fog, nausea, tightness? How does the felt sense of confusion differ from the felt sense of insight?)

## Part 4: Intuitive Evaluation of a Real Dilemma (7 minutes)

Bring to mind a question you are currently trying to understand or a judgment you need to make. Rather than thinking it through, hold the question lightly and attend to the body's response.

Ask the question silently and wait. Notice what arises somatically. Does the body lean toward an answer? Is there a felt direction, even if it is unclear?

{fill:textarea}(What question did you hold? What was the body's response? Did a felt direction emerge? Was it different from what your analytical mind had been suggesting?)

## Part 5: Reflection

{fill:textarea}(What did this lab reveal about the body's role in cognitive evaluation? How does somatic intelligence complement, precede, or correct intellectual analysis?)

## Reflection Table

| Cognitive Dimension | Somatic Experience | Active Inference Connection |
| --- | --- | --- |
| Rightness/wrongness | {fill:text} | Fit/misfit between prediction and evidence |
| Insight ("aha") | {fill:text} | Sudden reduction in cognitive free energy |
| Confusion | {fill:text} | Elevated free energy, poor model fit |
| Intuitive direction | {fill:text} | Deep priors generating somatic policy evaluation |
""",

    ("03_intuitive_knowing", "05_action"): """# Lab: The Hands That Know

## Objective

Experience intuitive skilled action by engaging in a hands-on task that requires fine motor coordination, observing the transition from deliberate, effortful movement to increasingly fluid, pre-reflective action.

## Prerequisites

- A quiet space for 25 minutes
- A manual skill activity: drawing, folding origami, shuffling cards, tying knots, or any handcraft
- Materials for your chosen activity

## Part 1: Beginner's Hands (7 minutes)

Choose a task at the edge of your current skill level -- something you can do, but not yet fluently. Perform it slowly, attending to every micro-movement of your hands and fingers.

Notice: the hesitations, the corrections, the gap between intention and execution. These are prediction errors -- the generative model's motor predictions do not yet match the required movements.

{fill:textarea}(Describe the quality of your hands' first attempts. Where were the hesitations? What did the prediction errors feel like? How large was the gap between what you intended and what your hands actually did?)

## Part 2: Repetition and Refinement (10 minutes)

Repeat the task five to eight times, maintaining present-moment attention throughout. With each repetition, notice: Are the hesitations decreasing? Are the corrections becoming smaller? Is the movement becoming smoother?

You are watching the generative model update its motor predictions in real time. The transition from effortful to fluid is the progressive minimization of sensorimotor prediction error.

{fill:textarea}(Describe the trajectory of improvement across repetitions. What changed most noticeably -- speed, smoothness, accuracy, or confidence? At what point did you first notice the hands beginning to "know" the movement without conscious direction?)

## Part 3: Hands Know, Mind Watches (5 minutes)

Now attempt the task while simultaneously carrying on a silent mental conversation (count backward from 100, or recite something you know). Notice: can the hands continue skillfully when the mind is occupied elsewhere?

If the hands can perform without conscious guidance, the motor predictions have begun to consolidate into automatic priors -- the foundation of intuitive skilled action.

{fill:textarea}(Could your hands continue the task while your mind was elsewhere? What was the quality of the hands' knowing when conscious attention was withdrawn? Where did errors creep in, if at all?)

## Part 4: Reflection on Embodied Skill (3 minutes)

Put down the materials. Close your eyes. Feel your hands from the inside. What knowledge do they now carry that they did not carry 25 minutes ago?

{fill:textarea}(Describe the felt state of your hands after the practice session. What has changed in their quality of readiness, sensitivity, or competence? How does this felt change relate to the generative model's updated motor priors?)

## Reflection Table

| Action Phase | What I Noticed | Active Inference Connection |
| --- | --- | --- |
| First attempt (novice) | {fill:text} | Large motor prediction errors, effortful correction |
| Progressive refinement | {fill:text} | Prediction error reduction through parameter updating |
| Dual-task performance | {fill:text} | Motor priors consolidated below conscious threshold |
| Post-practice hands | {fill:text} | Updated generative model with refined motor predictions |
""",

    ("03_intuitive_knowing", "06_learning"): """# Lab: Tracing the Arc from Explicit to Tacit

## Objective

Observe the learning trajectory from explicit, rule-governed knowledge to implicit, embodied knowing by tracking the felt quality of understanding at different stages of skill development.

## Prerequisites

- A quiet space for 25 minutes
- A novel physical pattern to learn (a simple dance step, a hand-clapping rhythm, a pen-spinning trick, or a novel finger sequence)
- Timer and journal

## Part 1: The Rule Phase (5 minutes)

Learn a novel physical pattern using explicit instructions. Follow the steps literally, consulting the instructions at each stage. Notice the quality of this rule-following: effortful, slow, requiring constant attention, with frequent errors.

(Suggested pattern: Learn a 4-beat hand-clapping rhythm by following written instructions, or a simple origami fold from step-by-step directions.)

{fill:textarea}(Describe the quality of rule-governed learning. How did it feel to follow explicit instructions? What kind of errors occurred? Where was your attention focused?)

## Part 2: The Practice Phase (10 minutes)

Practice the pattern repeatedly for 10 minutes, gradually reducing reliance on explicit instructions. Track the felt quality of the transition:

- Minutes 1-3: Still consulting instructions, effortful
- Minutes 4-6: Instructions less needed, beginning to feel the pattern
- Minutes 7-10: The pattern becoming more automatic, attention freed

Note the specific moment when you first felt the pattern "in the body" rather than "in the instructions."

{fill:textarea}(Describe the trajectory of learning across the 10 minutes. At what point did you notice the shift from following rules to feeling the pattern? What changed in the quality of your attention and the quality of movement?)

## Part 3: The Test of Tacitness (5 minutes)

Try to perform the pattern while doing something else (talking, counting, looking around the room). If the pattern survives the dual-task challenge, it has begun to become tacit -- encoded in the body rather than held in working memory.

Now try to teach the pattern to an imaginary student by articulating the steps in words. Notice the gap between what your body can do and what your words can capture.

{fill:textarea}(Could you perform the pattern while doing something else? When you tried to articulate the steps verbally, what was the gap between embodied performance and verbal description? What knowledge was lost in translation?)

## Part 4: Reflection on the Learning Trajectory (5 minutes)

In your journal, map the learning arc:

1. What was the felt quality of explicit, rule-governed knowing?
2. What was the felt quality of transitional, semi-automatic knowing?
3. What was the felt quality of emerging tacit, embodied knowing?

{fill:textarea}(Describe each stage of the learning trajectory. What metaphor best captures the felt shift from explicit to tacit knowing? How does this exercise illuminate the nature of intuitive expertise?)

## Reflection Table

| Learning Stage | Felt Quality | Active Inference Connection |
| --- | --- | --- |
| Rule-following (novice) | {fill:text} | High-precision explicit priors, large prediction errors |
| Practice transition | {fill:text} | Parameters updating, predictions improving |
| Emerging tacitness | {fill:text} | Deep priors consolidated below conscious threshold |
| Verbal articulation gap | {fill:text} | High-dimensional model resisting low-dimensional translation |
""",

    ("03_intuitive_knowing", "07_communication"): """# Lab: Reading the Room with Your Body

## Objective

Develop awareness of the body's capacity for intuitive social perception by practicing deliberate attention to non-verbal communication channels, discovering how much interpersonal information the body processes beneath conscious awareness.

## Prerequisites

- A quiet space for 25 minutes
- Access to video recordings of conversations or interviews (phone, laptop, or TV)
- Alternatively: a public space where you can observe interactions
- Journal and pen

## Part 1: Watching Without Sound (7 minutes)

Play a video of a conversation or interview with the sound muted. Watch only the body language: posture, gesture, facial expression, spatial relationship, timing of movements.

Before unmuting, write your intuitive assessment: What is the relationship between these people? Who holds more power? What emotions are present? Are they in agreement or conflict?

{fill:textarea}(Describe your body-language-only assessment. What did you "read" from the non-verbal signals? After unmuting, how accurate was your intuitive reading? What surprised you?)

## Part 2: Listening Without Watching (5 minutes)

Now play a different conversation, but close your eyes and listen only. Attend to vocal prosody: pitch, rhythm, volume, pace, tone, pauses, breathing.

Before opening your eyes, write your assessment: What is the emotional tone? Who is more engaged? Is there tension or ease?

{fill:textarea}(Describe your voice-only assessment. What did prosody reveal that words alone might not? How accurate was your reading when you opened your eyes? What channels of information does the voice carry beyond verbal content?)

## Part 3: Full-Channel Observation (7 minutes)

Now watch a third conversation with full audio and video. But rather than attending to the content of what is said, attend to your own body's response. Notice: does your posture shift? Does your breathing change? Do you feel tension, warmth, discomfort, or ease in any part of your body?

Your body is a resonance instrument, picking up interpersonal signals through somatic empathy. Track these somatic responses as data about the conversation.

{fill:textarea}(What did your body register during the full-channel observation? Where did you feel the conversation in your own body? What interpersonal information did your somatic responses provide that conscious analysis might have missed?)

## Part 4: Calibration -- When Intuition Errs (5 minutes)

Reflect on times when your intuitive social reading was wrong. What conditions produced the error? Possible factors: your own emotional state biasing perception, cultural unfamiliarity, projection of your own feelings onto others.

{fill:textarea}(Describe a time when your intuitive social reading was inaccurate. What led to the error? How might you calibrate your intuitive social perception -- distinguishing genuine empathic reading from projection or bias?)

## Reflection Table

| Communication Channel | What I Perceived | Active Inference Connection |
| --- | --- | --- |
| Body language (visual) | {fill:text} | Postural and gestural predictions about social state |
| Vocal prosody (auditory) | {fill:text} | Precision modulation through voice frequency and rhythm |
| Somatic resonance (interoceptive) | {fill:text} | Cross-Markov-blanket empathic prediction |
| Error calibration | {fill:text} | Distinguishing well-calibrated from biased priors |
""",

    ("03_intuitive_knowing", "08_planning"): """# Lab: Planning from the Gut

## Objective

Practice intuitive decision-making by comparing the body's rapid somatic evaluation of future scenarios with deliberate analytical planning, discovering the conditions under which embodied intuition provides reliable guidance.

## Prerequisites

- A quiet space for 25 minutes
- A genuine decision or planning challenge you are currently facing
- Journal and pen

## Part 1: The Analytical Plan (5 minutes)

Write a brief pros-and-cons analysis for your decision. List the rational arguments for each option. Attempt to determine the "logical" best choice. Notice the quality of this cognitive process -- its effort, its incompleteness, the way analytical reasoning often fails to produce a clear verdict.

{fill:textarea}(Describe your analytical assessment. What did the pros-and-cons analysis suggest? How confident do you feel in the analytical conclusion? What information felt like it was missing from the analysis?)

## Part 2: The Somatic Plan (7 minutes)

Set the analysis aside. Close your eyes and take five settling breaths. Now bring your decision to mind without analyzing it. Simply hold the question in open awareness and attend to the body.

For each option, imagine committing to it fully. Let the scenario unfold in imagination. Track the body's response: chest, belly, throat, shoulders, breath, jaw. Rate each option on a somatic scale:

Constricting <-------> Expanding | Heavy <-------> Light | Cold <-------> Warm | Dead <-------> Alive

{fill:textarea}(For each option, describe the somatic evaluation. What was the body's verdict? Did it agree with or diverge from the analytical assessment? Where in the body was the signal strongest?)

## Part 3: The Integration (5 minutes)

Now sit with both assessments -- the analytical and the somatic. Where do they agree? This is likely solid ground. Where do they diverge? This is the most interesting territory.

When gut and mind disagree, consider: Does the body know something the mind has not articulated? Or is the body responding to fear, habit, or bias that the mind has correctly overridden?

{fill:textarea}(How do the analytical and somatic assessments compare? Where they agree, how does that feel? Where they diverge, which do you trust more, and why? What might the disagreement reveal?)

## Part 4: Retrospective Calibration (5 minutes)

Think back to three past decisions: one where you followed your gut and it proved right, one where you overrode your gut and were glad you did, and one where you overrode your gut and wished you had listened.

This retrospective analysis helps calibrate the reliability of your intuitive planning in different contexts.

{fill:textarea}(Describe each scenario. What patterns emerge about when your intuitive planning is reliable versus when it misleads? What domains or conditions favor embodied intuition over analytical deliberation?)

## Part 5: Reflection

{fill:textarea}(How should analytical and intuitive planning relate to each other? What did this lab teach you about the conditions under which you should trust the body's evaluation of the future?)

## Reflection Table

| Planning Mode | Quality of Decision | Active Inference Connection |
| --- | --- | --- |
| Analytical (pros/cons) | {fill:text} | Explicit, sequential policy evaluation |
| Somatic (gut feeling) | {fill:text} | Compressed expected free energy evaluation |
| Agreement | {fill:text} | Convergent model validation |
| Disagreement | {fill:text} | Diagnostic of hidden information or bias |
""",

    # SECTION-LEVEL lab for 03_intuitive_knowing
    ("03_intuitive_knowing", None): """# Lab: Cultivating Embodied Expertise

## Objective

Integrate the themes of this unit by engaging in a focused practice session in a domain of personal expertise (however modest), observing the qualities of tacit knowledge, intuitive perception, and pre-reflective action as they manifest in real-time performance.

## Prerequisites

- A quiet space for 25 minutes
- Materials for a skilled activity you practice regularly (cooking, music, drawing, a sport, a craft)
- Journal and pen

## Part 1: Warm-Up with Awareness (5 minutes)

Begin your chosen activity slowly, with deliberate present-moment awareness. As you perform the opening movements, notice the body's readiness -- the hands' familiarity with the tools, the postural preparation, the autonomic settling into the task's rhythm.

{fill:textarea}(Describe the quality of your body's preparation for the skilled activity. What does familiarity feel like? What does the body "remember" that you do not need to consciously recall?)

## Part 2: Entering Flow (10 minutes)

Now perform your activity at full engagement for 10 minutes. Allow yourself to be absorbed. When you notice moments of intuitive action (the hand knowing where to go, the eye seeing what matters, the body anticipating what comes next), make a brief mental note without breaking the flow.

{fill:textarea}(After the 10 minutes, describe the moments of intuitive knowing you noticed. What were the qualities of perception, action, and cognition during engaged practice? Did you experience any moments of flow?)

## Part 3: The Articulation Challenge (5 minutes)

Try to explain in writing exactly how you do what you just did. Attempt to articulate the tacit knowledge that guided your performance. Notice the gap between fluent doing and verbal describing.

{fill:textarea}(How much of your skilled performance could you articulate in words? Where did language fail? What aspects of your embodied expertise resist verbal translation? What does this gap tell you about the nature of intuitive knowing?)

## Part 4: Reflection (5 minutes)

{fill:textarea}(What did this lab reveal about the relationship between practice, embodied knowledge, and intuitive expertise? How does the quality of knowing-in-the-body differ from knowing-in-words? What implications does this have for how expertise should be taught and learned?)

## Reflection Table

| Expertise Dimension | What I Observed | Active Inference Connection |
| --- | --- | --- |
| Bodily preparation | {fill:text} | Deep priors activating in anticipation of practiced task |
| Intuitive performance | {fill:text} | Low free energy through optimized generative model |
| Flow states | {fill:text} | Minimal prediction error, seamless perception-action coupling |
| Articulation gap | {fill:text} | High-dimensional model exceeding verbal bandwidth |
""",
})

# Now generate section 04 labs
LABS.update({
    ("04_moving_through_world", "01_systems"): """# Lab: The Body as Moving System

## Objective

Experience the body as an integrated locomotor system by performing a series of movement challenges that reveal the coordination of vestibular, proprioceptive, visual, and muscular subsystems in maintaining dynamic balance and fluid motion.

## Prerequisites

- A safe space for movement (indoors or outdoors), at least 10 feet of clear floor
- Comfortable clothing and bare feet if possible
- 25 minutes of uninterrupted time

## Part 1: Static to Dynamic (5 minutes)

Stand with feet hip-width apart, eyes closed. Feel the body's constant micro-adjustments to maintain balance -- ankle, knee, hip, and spine all making tiny corrections. This is the body-as-system maintaining its postural Markov blanket.

Now open your eyes and begin walking slowly. Notice how the entire system reorganizes: balance shifts from static to dynamic, breathing adjusts, vision begins to scan ahead, the arms swing in counter-rhythm to the legs.

{fill:textarea}(Describe the difference between the body's systemic organization in standing versus walking. What subsystems became active when you began to move? How did the quality of balance change from static to dynamic?)

## Part 2: Multi-Surface Navigation (7 minutes)

Walk across different surfaces if available (carpet to tile, grass to concrete, flat to inclined). If only one surface is available, vary your walking: tiptoe, heel-walk, wide stance, narrow stance.

Notice how each surface change or walking variation generates prediction errors that the body-as-system must resolve. The entire locomotor system recalibrates within a few steps.

{fill:textarea}(How did changing surfaces or walking patterns affect the body's systemic organization? What prediction errors did you notice? How quickly did the system recalibrate? What subsystems were most involved in the adjustment?)

## Part 3: Breath-Movement Coupling (5 minutes)

Walk at a comfortable pace and notice whether your breathing has naturally synchronized with your stride (many people inhale for 2-3 steps, exhale for 2-3 steps). Try different couplings: one breath per step, one breath per four steps.

This respiratory-locomotor coupling reveals how the body's subsystems are not independent but dynamically integrated in the moving system.

{fill:textarea}(Did you find a natural breath-stride coupling? How did changing the ratio affect the ease of movement? What does this coupling reveal about the body's systemic integration during locomotion?)

## Part 4: System Under Challenge (5 minutes)

Try one of these challenges:

- Walk in a straight line with eyes closed (10 steps, then open eyes)
- Walk backward for 20 steps
- Walk while turning your head from side to side

Notice how removing or disrupting one input (vision, direction, vestibular stability) forces the rest of the system to compensate.

{fill:textarea}(Which challenge did you try? How did the disruption affect the overall system? What compensations did the body automatically generate? What does this reveal about systemic resilience and adaptation?)

## Part 5: Reflection

{fill:textarea}(After this lab, how would you describe the body-in-motion as a system? What did the movement challenges reveal about the coordination, integration, and adaptability of the moving body?)

## Reflection Table

| System Challenge | What I Noticed | Active Inference Connection |
| --- | --- | --- |
| Static vs. dynamic balance | {fill:text} | Reorganization of generative model for locomotion |
| Surface adaptation | {fill:text} | Prediction error correction across coupled subsystems |
| Breath-movement coupling | {fill:text} | Interoceptive-locomotor integration |
| Sensory disruption | {fill:text} | Systemic compensation under degraded input |
""",

    ("04_moving_through_world", "02_agents"): """# Lab: The Moving Agent and Its Affordances

## Objective

Experience the body as a spatial agent by exploring how movement capacities shape the perception of environmental possibilities, discovering that the moving agent perceives a world structured by what its body can do.

## Prerequisites

- Access to a varied environment (a park, a building with stairs, or any space with diverse physical features)
- Comfortable clothing and footwear
- 25 minutes of uninterrupted time

## Part 1: The Affordance Walk (7 minutes)

Walk through your environment slowly. As you encounter each surface, object, and space, silently name the affordance it offers your body: "sittable," "climbable," "graspable," "passable," "lean-against-able."

Notice that you do not need to calculate these possibilities -- the body perceives them directly, immediately, as part of the visual field.

{fill:textarea}(List at least 10 affordances you perceived during your walk. Which were most obvious? Which required you to shift your attention to notice? How does naming affordances change the quality of environmental perception?)

## Part 2: Changing the Agent (5 minutes)

Now repeat a portion of the walk while imagining you are a different kind of agent:

- A small child (waist-high surfaces become mountains, low tables become tunnels)
- Someone using a wheelchair (stairs become barriers, ramps become passages)
- A cat (narrow ledges become walkways, high shelves become destinations)

Notice how the perceived affordances change completely when the agent's body changes.

{fill:textarea}(How did imagining a different body change the affordances you perceived? What surfaces or objects gained or lost their action possibilities? What does this reveal about the relationship between the body and the perceived world?)

## Part 3: Agent Under Fatigue (5 minutes)

Walk briskly enough to elevate your heart rate slightly (or recall the experience of being very tired). Notice how fatigue changes the affordance landscape: a bench becomes more inviting, a hill becomes more daunting, distances seem longer.

The moving agent's current state modulates its perception of the world's possibilities. A tired body perceives a different world than an energized one.

{fill:textarea}(How did fatigue or arousal change your perception of environmental affordances? What became more salient, and what receded? How does the agent's energy state shape the world it perceives?)

## Part 4: Spatial Confidence (5 minutes)

Find a low wall, a curb, or any safe elevation. Stand on it. Notice the felt quality of spatial confidence at this height. Now close your eyes briefly and notice how removing vision changes the felt quality.

Spatial confidence -- the body's trust in its own balance and movement capacity -- is the foundation of the moving agent's willingness to explore.

{fill:textarea}(Describe the felt quality of spatial confidence. How did height, vision, and balance interact? At what point did confidence shift toward caution? What does this threshold reveal about the agent's generative model?)

## Part 5: Reflection

{fill:textarea}(After this lab, how would you describe the relationship between the body-as-agent and the environment it perceives? What did you learn about affordances as the bridge between body and world?)

## Reflection Table

| Agent Dimension | What I Noticed | Active Inference Connection |
| --- | --- | --- |
| Affordance perception | {fill:text} | Environment perceived through the lens of action possibility |
| Agent body variation | {fill:text} | Different bodies produce different affordance landscapes |
| State-dependent perception | {fill:text} | Interoceptive state modulating expected free energy of actions |
| Spatial confidence | {fill:text} | Precision on motor predictions enabling exploratory behavior |
""",

    ("04_moving_through_world", "03_perception"): """# Lab: Perceiving Space Through Movement

## Objective

Discover how movement transforms spatial perception by comparing the experience of observing a space from a fixed position with the experience of moving through that space, revealing the body's role in constructing spatial understanding.

## Prerequisites

- Access to a room or outdoor area you can explore freely
- 25 minutes of uninterrupted time
- Journal and pen

## Part 1: Static Observation (5 minutes)

Stand at one point in your space and observe the environment without moving. Take in the room from this single vantage point. Note distances, spatial relationships, textures, and the overall layout.

{fill:textarea}(Describe the space as perceived from a fixed position. What could you see clearly? What was hidden, ambiguous, or unknown? How confident were you about spatial distances and relationships?)

## Part 2: Moving Through (10 minutes)

Now walk slowly through the entire space. Touch surfaces, look around corners, walk the perimeter, cross the center, approach objects. Spend 10 minutes exploring with your full body.

Notice how movement reveals what static observation cannot: the depth of a corner, the texture of a wall, the actual distance between objects, the slope of a floor, the acoustic quality of the space.

{fill:textarea}(How did moving through the space change your perception of it? What did you discover that was invisible from a fixed position? How did touching, approaching, and circling transform your spatial understanding?)

## Part 3: Proprioceptive Mapping (5 minutes)

Close your eyes in the center of the space. Point toward different objects and features from memory. Walk (carefully) toward one and see if you arrive at the right spot. Your body has built a proprioceptive map from its movement history.

{fill:textarea}(How accurate was your proprioceptive map? Which locations were you most confident about? Which were uncertain? What does this reveal about how the body encodes spatial knowledge through movement?)

## Part 4: Speed and Perception (5 minutes)

Walk through the space at three different speeds: very slow (half normal pace), normal, and brisk. Notice how speed changes perception: slow walking reveals detail, fast walking creates a more global, flowing impression.

{fill:textarea}(How did walking speed change your perception of the space? What was visible at slow speed that disappeared at fast speed? What spatial qualities emerged at fast speed that were absent at slow speed?)

## Part 5: Reflection

{fill:textarea}(What did this lab reveal about the relationship between movement and spatial perception? How does the body's passage through space construct knowledge that static observation cannot provide?)

## Reflection Table

| Perceptual Mode | What I Noticed | Active Inference Connection |
| --- | --- | --- |
| Static observation | {fill:text} | Limited predictions from single vantage point |
| Movement-based exploration | {fill:text} | Rich prediction updating through sensorimotor engagement |
| Proprioceptive mapping | {fill:text} | Spatial generative model built from locomotor experience |
| Speed-dependent perception | {fill:text} | Temporal grain of prediction matching movement velocity |
""",

    ("04_moving_through_world", "04_cognition"): """# Lab: Thinking with Your Feet

## Objective

Explore the relationship between locomotion and cognition by comparing the quality of thinking during different movement states, discovering how the body's spatial engagement with the world shapes and supports cognitive processing.

## Prerequisites

- Access to a walking route (indoor or outdoor)
- A moderately difficult cognitive task (a problem to solve, a plan to develop, or a creative project)
- 25 minutes and a journal

## Part 1: Seated Thinking (5 minutes)

Sit in a chair and work on your cognitive task for 5 minutes. Notice the quality of your thinking: its pace, its fluidity, the types of ideas that arise, and the felt quality of cognitive effort.

{fill:textarea}(Describe the quality of seated thinking. What was the pace and character of your thoughts? Where did you get stuck? What was the felt quality of cognitive effort in the body?)

## Part 2: Walking and Thinking (10 minutes)

Now take your cognitive task on a walk. Walk at a comfortable pace while continuing to think about the same problem. Do not force the thinking -- let it arise naturally as the body moves.

Notice: does the quality of thinking change? Do different types of ideas emerge? Is there a shift in cognitive pace, breadth, or fluidity?

{fill:textarea}(How did walking change the quality of your cognitive processing? What types of ideas emerged that were absent during seated thinking? Did the rhythmic quality of walking affect the rhythm of thought? Where did insights arise -- in the body, in the mind, or in the relationship between them?)

## Part 3: Standing Still and Thinking (5 minutes)

Stop walking and stand in one place. Continue thinking about the same task. Notice the transition: does the quality of cognition shift when the body stops moving?

Many people find that standing still after walking produces a distinctive cognitive state -- the residual momentum of movement continues to support thought for a time, then gradually fades.

{fill:textarea}(How did stopping affect the quality of thinking? Did the walking momentum carry over? How did standing-still cognition compare with both seated and walking cognition?)

## Part 4: Gesture and Spatial Thought (5 minutes)

Return to your seated position. Now think about your task while deliberately using gestures: point, draw diagrams in the air, use your hands to represent spatial relationships, timelines, or conceptual structures.

Notice how hand movement supports and shapes spatial thinking. The hands are not merely expressing thought -- they are participating in it.

{fill:textarea}(How did gesturing change the quality of spatial or relational thinking? Did hand movements produce any ideas that were absent during still thinking? What does this reveal about the body's contribution to cognition?)

## Part 5: Reflection

{fill:textarea}(After comparing four modes of embodied cognition (seated, walking, standing, gesturing), what have you learned about the relationship between physical movement and the quality of thought?)

## Reflection Table

| Cognitive Mode | Quality of Thinking | Active Inference Connection |
| --- | --- | --- |
| Seated | {fill:text} | Minimal motor contribution to cognitive predictions |
| Walking | {fill:text} | Locomotor rhythm supporting cognitive generation |
| Standing still | {fill:text} | Transition state between movement and stasis |
| Gesturing | {fill:text} | Motor system as active cognitive resource |
""",

    ("04_moving_through_world", "05_action"): """# Lab: The Dance of Balance

## Objective

Experience the body's dynamic action system through balance challenges that reveal the continuous prediction-correction cycle of skilled movement, illustrating active inference as the real-time sculpting of the body's relationship with gravity.

## Prerequisites

- A safe, clear floor space
- Comfortable clothing, bare feet recommended
- 25 minutes of uninterrupted time
- Optional: a cushion or yoga mat

## Part 1: The Standing Challenge (5 minutes)

Stand on both feet with eyes open. Notice the ease of balance -- the body-as-action-system maintaining equilibrium with minimal apparent effort.

Now close your eyes. Notice how removing visual input immediately increases the work of the other systems -- ankles, proprioceptors, vestibular apparatus. You can feel prediction errors arising and being corrected in real time.

Finally, stand on one foot with eyes open. Then close your eyes. Feel the body's action system working at increasing levels of challenge.

{fill:textarea}(Describe the experience at each difficulty level. How did removing vision change the body's balance strategy? What did you feel in the ankles, core, and arms during one-footed balance? What does the progressive challenge reveal about the body's layered action systems?)

## Part 2: Slow-Motion Weight Transfer (7 minutes)

Stand with feet shoulder-width apart. Transfer your weight from center to right foot as slowly as possible. Feel the progressive shifting: the left foot lightening, the right foot loading, the core adjusting, the spine adapting.

Move to the left. Then forward on your toes. Then back on your heels. Make each transfer take at least 15 seconds.

You are making visible the moment-to-moment action adjustments that are normally invisible in rapid walking. Each millimeter of weight transfer is a prediction-correction cycle.

{fill:textarea}(Describe the micro-experience of slow weight transfer. What muscles engaged and released? What was the quality of balance at the edges of the weight shift? Where was the body's "comfort zone" and where did it feel risky?)

## Part 3: Reactive Action (5 minutes)

Stand on one foot. Have a partner (or toss a pillow to yourself) create an unexpected perturbation -- a gentle nudge, a thrown object to catch, or a surface change (stepping onto a pillow).

Notice the body's rapid reactive action: how it recalibrates balance within milliseconds, how the arms compensate, how the ankle makes instant adjustments. This is the action system's prediction-error correction operating at full speed.

{fill:textarea}(Describe the reactive balance responses. How fast was the body's correction? What did you notice about the sequence of muscular responses? How did the body's action system handle the unexpected perturbation?)

## Part 4: Expressive Movement (5 minutes)

Put on music (or create your own rhythm) and move freely. Let the body express what it wants to express -- swaying, stepping, spinning, reaching. Do not choreograph; simply allow movement to emerge from the body's own impulses.

This is action freed from instrumental purpose -- movement as expression, play, and self-regulation.

{fill:textarea}(Describe the quality of free, expressive movement. What did the body want to do when given permission? How did the quality of action differ from the structured balance exercises? What was the emotional quality of moving freely?)

## Part 5: Reflection

{fill:textarea}(What did this lab reveal about the body's action system? How does the continuous prediction-correction cycle of balance illuminate the Active Inference account of embodied action?)

## Reflection Table

| Action Challenge | What I Experienced | Active Inference Connection |
| --- | --- | --- |
| Balance with reduced input | {fill:text} | Increased prediction error from sensory degradation |
| Slow weight transfer | {fill:text} | Action-perception loop made visible at slow speed |
| Reactive balance | {fill:text} | Rapid prediction error correction in real time |
| Expressive movement | {fill:text} | Action as embodied expression and self-regulation |
""",

    ("04_moving_through_world", "06_learning"): """# Lab: Learning a New Movement

## Objective

Observe the process of motor learning in real time by acquiring a novel movement pattern, tracking the progression from awkward, error-filled first attempts to increasingly smooth, coordinated execution.

## Prerequisites

- A safe space for movement
- 25 minutes of uninterrupted time
- A novel movement challenge (suggestions below)

## Part 1: Choose Your Challenge (2 minutes)

Select a movement you cannot currently perform fluently:

- **Option A**: Walk heel-to-toe in a perfectly straight line for 10 steps
- **Option B**: Stand on one foot and slowly lower to touch the floor with your fingertip, then rise back up
- **Option C**: Walk backward along a curved path (a semicircle)
- **Option D**: Perform a lateral shuffle (grapevine step) -- step right, left foot behind, step right, left foot in front

## Part 2: First Attempts (5 minutes)

Attempt your chosen movement five times. Do not try to be good at it -- simply observe the body's first encounters with the novel pattern.

Notice: Where are the prediction errors? What does the body expect to happen versus what actually happens? Where is the effort concentrated? What does failure feel like somatically?

{fill:textarea}(Describe your first five attempts. What were the dominant prediction errors? Where in the body was the effort concentrated? What was the felt quality of unfamiliarity -- frustration, curiosity, amusement, awkwardness?)

## Part 3: Deliberate Practice (10 minutes)

Practice the movement for 10 minutes, alternating between two strategies:

1. **Slow motion**: Perform the movement at half speed, attending to every micro-phase
2. **Full speed**: Perform at normal speed, letting the body find its own solutions

Track improvement: When do you first notice increased smoothness? What does improvement feel like in the body -- not as a concept, but as a sensation?

{fill:textarea}(Describe the learning trajectory over 10 minutes. At what point did you first notice improvement? What felt different between slow-motion practice and full-speed practice? How did the quality of prediction errors change over time?)

## Part 4: Integration Test (5 minutes)

Perform the movement while doing something cognitively simple (counting, humming a tune). If the movement survives the dual-task test with reasonable quality, it has begun to consolidate from explicit to implicit.

Now try to teach the movement to an imaginary student using only words (no demonstration). Notice the gap between your body's growing competence and your ability to articulate the movement.

{fill:textarea}(How well did the movement survive the dual-task test? What was the quality of performance compared to your best focused attempt? When you tried to verbalize the movement, what was lost in translation?)

## Part 5: Reflection

{fill:textarea}(What did this lab reveal about how the body learns new movements? How does the Active Inference framework illuminate the progression from prediction error to prediction accuracy in motor learning?)

## Reflection Table

| Learning Phase | What I Experienced | Active Inference Connection |
| --- | --- | --- |
| First attempts | {fill:text} | Large sensorimotor prediction errors |
| Deliberate practice | {fill:text} | Parameter updating through repeated correction |
| Growing fluency | {fill:text} | Prediction errors decreasing, smoothness increasing |
| Consolidation test | {fill:text} | Motor priors consolidating below conscious threshold |
""",

    ("04_moving_through_world", "07_communication"): """# Lab: Bodies in Conversation -- Movement as Communication

## Objective

Explore how bodies communicate through movement, spatial behavior, and physical coordination, discovering the rich non-verbal dialogue that occurs when bodies move together through shared space.

## Prerequisites

- A partner willing to participate (solo alternatives provided)
- A clear floor space
- 25 minutes of uninterrupted time

## Part 1: Mirroring (5 minutes)

Face your partner at arm's length. One person leads, moving slowly (raising arms, shifting weight, turning). The other follows, mirroring each movement as closely as possible. After 2.5 minutes, switch roles.

(Solo alternative: Stand facing a mirror and lead yourself through slow, deliberate movements, maintaining eye contact with your reflection.)

Notice: communication is happening through pure movement. The leader communicates intention through direction, speed, and quality of movement. The follower receives through visual and kinesthetic attunement.

{fill:textarea}(Describe the experience of leading and following. What was the quality of the movement communication? How did you "read" your partner's intended direction? What happened when the signals were ambiguous?)

## Part 2: Walking Together (5 minutes)

Walk side by side with your partner. Without speaking, try to synchronize your stride -- same foot forward at the same time, same pace, same rhythm. Then try walking at different paces and notice the felt tension of desynchronization.

(Solo alternative: Walk alongside a stream, a metronome app, or music, synchronizing your stride to the external rhythm.)

{fill:textarea}(How quickly did your strides synchronize? What was the felt quality of being in step versus out of step? How did the synchronization (or lack thereof) affect your sense of connection or disconnection?)

## Part 3: Spatial Negotiation (7 minutes)

Both partners walk freely in the shared space. Without speaking, navigate around each other. Vary the dynamics: approach closely and retreat, weave around each other, pause and wait, pass closely or give wide berth.

Notice the constant non-verbal negotiation: trajectory intentions communicated through body orientation, speed, and gaze direction.

(Solo alternative: Navigate a busy public space and attend to the non-verbal negotiation with other pedestrians.)

{fill:textarea}(What non-verbal signals did you use to communicate trajectory and intention? How did proximity affect the body's arousal level? What was the quality of near-misses versus generous spacing? What did spatial behavior communicate about the relationship?)

## Part 4: Still Communication (5 minutes)

Stand facing each other at three different distances: 6 feet (social), 3 feet (personal), 18 inches (intimate). At each distance, simply stand and notice what the proximity communicates to your body.

(Solo alternative: Stand at different distances from a wall or large mirror and notice how proximity changes felt quality.)

{fill:textarea}(How did the quality of communication change at each distance? What did your body feel at social distance versus intimate distance? How does spatial proximity function as a form of embodied communication?)

## Part 5: Reflection

{fill:textarea}(What did this lab reveal about movement as a form of communication? How do bodies exchange information through spatial behavior, synchronization, and physical coordination?)

## Reflection Table

| Movement Communication | What I Noticed | Active Inference Connection |
| --- | --- | --- |
| Mirroring | {fill:text} | Visual-motor prediction alignment between agents |
| Stride synchronization | {fill:text} | Coupled locomotor inference |
| Spatial negotiation | {fill:text} | Trajectory prediction and correction across Markov blankets |
| Proxemic communication | {fill:text} | Distance as precision signal for social inference |
""",

    ("04_moving_through_world", "08_planning"): """# Lab: Planning the Body's Path

## Objective

Experience embodied movement planning by navigating a series of spatial challenges that require anticipation, route selection, and kinesthetic simulation, discovering how the body plans its passage through the physical world.

## Prerequisites

- A varied indoor or outdoor environment with obstacles, elevation changes, or navigational choices
- 25 minutes of uninterrupted time
- Journal and pen

## Part 1: The Preview Scan (5 minutes)

Stand at the edge of a complex space (a cluttered room, a rocky path, a busy sidewalk). Before moving, scan the environment visually. Notice how the eyes and body are already planning: identifying foot placements, anticipating obstacles, mapping a path.

Feel the body's readiness -- ankles preparing for terrain, balance system calibrating, arms positioning for potential use.

{fill:textarea}(Describe your body's preview scan. What spatial features did the body prioritize? Where did you feel the anticipatory preparation -- in the feet, the core, the eyes, the arms? How did the body's plan manifest somatically before any movement began?)

## Part 2: Navigation with Constraints (7 minutes)

Navigate through the space with a constraint:

- Carry something fragile (a full cup of water, a balanced book on your head)
- Walk backward
- Navigate with one eye closed
- Move through as quietly as possible

Notice how the constraint forces the body to plan more carefully, revealing the normally invisible planning process.

{fill:textarea}(Which constraint did you choose? How did it change the body's planning process? What became more deliberate? What prediction errors arose from the constraint, and how did the body resolve them?)

## Part 3: Pre-Movement Simulation (5 minutes)

Stand before a physical challenge (stepping over an obstacle, climbing a step, reaching across a gap). Before executing, close your eyes and simulate the entire movement in kinesthetic imagination. Feel the sequence of muscle activations, the shift of weight, the moment of contact.

Then execute. Compare the simulation with the actual experience.

{fill:textarea}(Describe your kinesthetic simulation. How detailed was it? How did the simulated movement compare with the actual execution? Where was the simulation accurate, and where did it diverge from reality?)

## Part 4: Improvised Route Planning (5 minutes)

Walk a route through your environment that you have never walked before. Take turns you would not normally take, explore corners you usually ignore, navigate spaces you have not entered.

Notice the quality of improvised planning: the body must generate plans in real time, without the benefit of prior experience.

{fill:textarea}(Describe the felt quality of improvised navigation. How did navigating a novel route differ from a familiar one? Where did the body hesitate? Where did confidence arise despite unfamiliarity? What does this reveal about the generative model's capacity for real-time spatial planning?)

## Part 5: Reflection

{fill:textarea}(What did this lab reveal about how the body plans its movement through the physical world? How does embodied spatial planning differ from abstract route planning on a map?)

## Reflection Table

| Planning Dimension | What I Experienced | Active Inference Connection |
| --- | --- | --- |
| Visual preview | {fill:text} | Generative model scanning expected free energy landscape |
| Constrained navigation | {fill:text} | Planning under additional prediction error demands |
| Kinesthetic simulation | {fill:text} | Motor predictions run in offline mode |
| Improvised exploration | {fill:text} | Real-time policy generation in novel environments |
""",

    # SECTION-LEVEL lab for 04_moving_through_world
    ("04_moving_through_world", None): """# Lab: The Affordance Walk -- Perceiving the World Through a Moving Body

## Objective

Integrate the themes of this unit through a sustained walking practice that brings deliberate attention to affordances, sensorimotor contingencies, and the dynamic coupling between the moving body and the structured environment.

## Prerequisites

- A 15-20 minute walking route through a varied environment (indoor/outdoor mix ideal)
- Comfortable footwear or bare feet
- 25 minutes of uninterrupted time
- Small journal or phone for notes

## Part 1: Setting Out with Intention (3 minutes)

Before beginning, stand still at your starting point. Close your eyes and take five breaths. Feel your feet on the ground, the readiness of your legs, the orientation of your body in space. Set a simple intention: "I will perceive the world as my body's partner in a dance of possibilities."

Open your eyes and begin walking slowly.

{fill:textarea}(Describe your body's state at the starting point. What was the quality of spatial readiness? How did setting an intention change the quality of the first steps?)

## Part 2: Naming Affordances (7 minutes)

As you walk, silently name the affordances each surface and object offers: "sittable," "climbable," "graspable," "passable," "shelter," "obstacle." Notice how your body perceives these possibilities before your mind names them.

Pay special attention to how your energy level, mood, and physical state change which affordances appear most salient. A bench means different things to a tired body than to an energized one.

{fill:textarea}(List at least 15 affordances you perceived. Which were immediately obvious? Which required a shift in attention? How did your body's current state influence which affordances stood out most? Did any affordances surprise you?)

## Part 3: The Extended Body (5 minutes)

If available, pick up a stick, open an umbrella, or carry any object that extends beyond your body boundary. Walk with this object and notice how the Markov blanket of your moving body extends to include the object's tip.

If no object is available, walk close to a wall and notice how the wall becomes part of your spatial awareness -- you sense its proximity without touching it.

{fill:textarea}(How did carrying an object or walking near a wall change your spatial perception? Did you begin to "feel through" the object or "sense" the wall? What does this reveal about the body's capacity to extend its Markov blanket?)

## Part 4: Sensorimotor Discovery (5 minutes)

For the final stretch, slow your pace and attend to the sensorimotor contingencies of walking: the feel of the ground through your feet, the visual flow created by forward motion, the wind on your skin, the sound of your footsteps.

Let the walk become a meditation on the body's partnership with the world -- the continuous, reciprocal dance of prediction and sensation that constitutes moving through the world.

{fill:textarea}(Describe the sensorimotor qualities of walking that you attended to. What did you feel through your feet? What did the visual flow reveal? How did attending to these sensorimotor details change the quality of the walking experience?)

## Part 5: Reflection

{fill:textarea}(What did this affordance walk reveal about the relationship between your moving body and the world it inhabits? How does the Active Inference framework illuminate what you experienced?)

## Reflection Table

| Walking Dimension | What I Noticed | Active Inference Connection |
| --- | --- | --- |
| Affordance perception | {fill:text} | Expected free energy landscape perceived through body |
| State-dependent salience | {fill:text} | Interoceptive state modulating affordance perception |
| Extended body boundary | {fill:text} | Markov blanket incorporating tools and surfaces |
| Sensorimotor contingencies | {fill:text} | Action-conditioned predictions constituting spatial perception |
""",
})


def write_questions_file(section, submodule, questions):
    """Write a questions.md file with the first 3 original questions preserved and 17 new ones."""
    if submodule:
        path = os.path.join(BASE, section, submodule, "questions.md")
        topic = SUBMODULE_NAMES[submodule]
    else:
        path = os.path.join(BASE, section, "questions.md")
        topic = SECTION_NAMES[section]

    # Read existing file to get first 3 questions
    with open(path, "r") as f:
        content = f.read()

    lines = content.strip().split("\n")
    # Extract title and first 3 questions
    title = lines[0] if lines else f"# Study Questions: {topic}"

    # Find the first 3 questions
    q_lines = []
    q_count = 0
    for line in lines[1:]:
        stripped = line.strip()
        if stripped and stripped[0].isdigit() and "." in stripped[:5]:
            q_count += 1
            if q_count <= 3:
                q_lines.append(line)
            else:
                break
        elif q_count > 0 and q_count <= 3 and stripped:
            # Continuation of a question
            q_lines.append(line)

    # Build new content
    new_lines = [title, ""]
    # Add original questions 1-3
    for ql in q_lines:
        new_lines.append(ql)
        new_lines.append("")

    # Add new questions 4-20
    for i, q in enumerate(questions, start=4):
        new_lines.append(f"{i}.  {q}")
        new_lines.append("")

    with open(path, "w") as f:
        f.write("\n".join(new_lines))
    print(f"  WROTE questions: {path}")


def write_lab_file(section, submodule, lab_content):
    """Write a lab.md file."""
    if submodule:
        path = os.path.join(BASE, section, submodule, "lab.md")
    else:
        path = os.path.join(BASE, section, "lab.md")

    with open(path, "w") as f:
        f.write(lab_content.strip() + "\n")
    print(f"  WROTE lab: {path}")


def main():
    # Process questions
    print("=== PROCESSING QUESTIONS ===")
    for (section, submodule), questions in QUESTIONS.items():
        if submodule:
            path = os.path.join(BASE, section, submodule, "questions.md")
        else:
            path = os.path.join(BASE, section, "questions.md")
        if os.path.exists(path):
            write_questions_file(section, submodule, questions)
        else:
            print(f"  SKIP (not found): {path}")

    # Process labs
    print("\n=== PROCESSING LABS ===")
    for (section, submodule), lab_content in LABS.items():
        if submodule:
            path = os.path.join(BASE, section, submodule, "lab.md")
        else:
            path = os.path.join(BASE, section, "lab.md")
        if os.path.exists(path):
            # Only write if it's a stub (grid world) or section-level stub
            with open(path, "r") as f:
                current = f.read()
            if "grid world" in current.lower() or "grid world" in current:
                write_lab_file(section, submodule, lab_content)
            else:
                print(f"  SKIP (already good): {path}")
        else:
            print(f"  SKIP (not found): {path}")


if __name__ == "__main__":
    main()
