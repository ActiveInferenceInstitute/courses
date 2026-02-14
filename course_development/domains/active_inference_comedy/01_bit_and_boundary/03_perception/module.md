# Module 03: Perception in Comedy

## Learning Objectives

1. Analyze how the phoneme "Who" is parsed differently by agents with different generative models — the core **likelihood degeneracy** of the routine.
2. Understand **perceptual inference** as the process by which observations are mapped to hidden states.
3. Identify how comedic timing exploits the temporal dynamics of perception.

## Introduction

Listen to Abbott say "Who's on first." Four syllables. One breath. And in that breath, two completely different perceptions occur. Abbott hears himself stating a fact: a player named Who plays first base. Costello hears a question: who is the player on first base? The audience hears both simultaneously — and this tripled perception is the engine of the routine.

Perception in Active Inference is not passive reception. It is active inference about hidden states from ambiguous observations. When your ears receive the phoneme sequence /huːz ɒn fɜːrst/, your brain runs a rapid inference: what hidden state of the world produced this observation? The answer depends on your generative model — your prior beliefs about what kinds of things people say and mean.

## Key Concepts

### 1. Likelihood Degeneracy: One Sound, Two Meanings

In Active Inference, perception involves inverting a **likelihood mapping** — going from an observation back to the hidden state that caused it. The likelihood P(o|s) tells you: "If the hidden state is s, how probable is observation o?"

"Who's on First?" exploits a **degenerate likelihood**: the observation "Who" is equally probable under two incompatible hidden states. If the hidden state is *name = "Who"*, the observation "Who" is perfectly natural (probability ≈ 1). If the hidden state is *question being asked*, the observation "Who" is also perfectly natural (probability ≈ 1). The observation cannot distinguish between the two states.

This is not a weakness in human perception — it is a genuine ambiguity in the input. The English language has a design feature (or, from the comedian's perspective, a design *gift*): proper nouns can be homophonous with function words. "Who's on First?" discovers this gift and builds an entire cosmos around it.

### 2. Prior-Dependent Perception

When the likelihood is degenerate, perception depends entirely on the **prior**. Abbott's prior — informed by his knowledge of the team roster — assigns high probability to *name = "Who"*. So when he hears or says "Who," his perception resolves unambiguously to the name. Costello's prior — informed by normal English usage — assigns high probability to *question being asked*. So when he hears "Who," his perception resolves unambiguously to the question.

Both perceptions are Bayes-optimal given their respective priors. Neither agent is being stupid. Both are doing the best possible inference given their models. The comedy arises because the priors are irreconcilable, and the evidence (the spoken words) cannot adjudicate between them.

### 3. Auditory Scene Analysis and Comedic Timing

Perception is not instantaneous. When Costello hears "Who's on first," there is a temporal unfolding: the /h/ sound, the /uː/, the /z/, then "on first." During this brief window, Costello's auditory system is parsing, predicting, and resolving — a cascade of perceptual inference that happens in milliseconds.

Comedic timing exploits this cascade. A well-timed pause after "Who's on first" gives the audience time to run *both* parses (name and question), recognize the ambiguity, and anticipate Costello's confusion — all before Costello responds. The pause is a precision accumulation window: the audience's model builds confidence in its dual-parse, and the prediction error when Costello confirms the wrong parse is therefore larger.

## Applications

- **Mishearing as Perceptual Inference Failure**: Many comedy routines exploit mishearing — one character says something, another hears something different. Every mishearing gag is a case of perceptual inference under a wrong prior. "Who's on First?" is the most extreme version: the hearing is *perfect* but the inference is still wrong.

- **Visual Comedy and Perceptual Ambiguity**: Slapstick, physical comedy, and sight gags exploit visual ambiguity the same way "Who's on First?" exploits auditory ambiguity. A character slipping on a banana peel is a perceptual prediction error — you predicted they would keep walking; the slip violates the prediction.

## Conclusion

Perception in "Who's on First?" is not broken — it is working exactly as designed, in two incompatible ways. The same observation is parsed through different generative models, producing different percepts that are each internally consistent but mutually exclusive. The audience perceives both parses and holds them in tension. This is the perceptual engine of the routine, and it runs on pure likelihood degeneracy. In the next module, we examine what happens inside the performers' heads after perception: cognition, belief perseveration, and the inability to update.
