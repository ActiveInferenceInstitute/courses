# Lab: Electrophysiological Methods for Active Inference

> **Learning Goal:** Design experiments and analyze data using EEG/MEG to test Active Inference predictions.

## Part 1: MMN Experiment Design

**Exercise**: Design a roving oddball experiment to test precision-weighted prediction errors:

**Stimuli**: Pure tones at 500 Hz (standard) and 550 Hz (deviant)
**Design**: Sequences where the standard repeats 2, 5, or 10 times before the deviant replaces it

**Active Inference prediction**: MMN amplitude should increase with number of repetitions (more repetitions → stronger prediction → larger PE when violated)

Specify:

1. Number of trials per condition (min 100 deviants per repetition count)
2. Inter-stimulus interval (e.g., 500 ms)
3. EEG electrode sites for analysis (Fz, Cz for MMN)
4. Time window for MMN measurement (100-250 ms post-deviant)
5. Statistical analysis (repeated-measures ANOVA on MMN amplitude × repetition count)

**Expected results**: MMN amplitude: 2-rep < 5-rep < 10-rep. This confirms precision-weighted PE.

{fill:textarea}

## Part 2: Oscillatory Analysis

> **Learning Goal:** Map oscillatory signatures to Active Inference computations.

**Exercise**: Analyze the expected oscillatory pattern during a visual attention task:

Task: Attend to left or right visual field. Predict when a target (grating) will appear at the attended location.

| Time Period | Alpha (8-12 Hz) | Beta (13-30 Hz) | Gamma (30-80 Hz) |
|------------|-----------------|-----------------|-------------------|
| Pre-cue baseline | Bilateral, moderate | Bilateral, moderate | Low everywhere |
| Post-cue (attend left) | Decreased left (precision ↑), Increased right (precision ↓) | Increased bilaterally (maintaining prediction) | Increased left (anticipatory) |
| Target onset (expected) | Brief disruption | Beta decrease (prediction update) | Gamma burst (local processing) |
| Target onset (unexpected) | Large alpha disruption | Large beta decrease | Strong gamma burst |

Write a 200-word analysis: How does this pattern map onto the Active Inference message-passing architecture?

{fill:textarea}

## Part 3: Hierarchical Prediction Paradigm

> **Learning Goal:** Design a paradigm testing multi-level prediction.

**Exercise**: The "local-global" paradigm (Bekinschtein et al., 2009):

**Stimuli**: Sequences of 5 tones: AAAAB (local deviant at position 5) or AAAAA (local standard)
**Block structure**: In one block, AAAAB is frequent (global standard) and AAAAA is rare (global deviant)

**Two levels of prediction error**:

- **Local PE**: 5th tone differs from first 4 → early MMN (~100-200 ms), temporal cortex
- **Global PE**: Rare sequence in block → late P3b (~300-500 ms), frontal/parietal

**Active Inference predicts**:

1. Local PE should be present even in unaware/unconscious patients (bottom-up, automatic)
2. Global PE requires awareness/consciousness (top-down, requires deep temporal model)
3. Local PE is modulated by local precision; global PE by global (contextual) precision

Design the control conditions needed to isolate each level of PE.

{fill:textarea}

## Part 4: Intracranial Hypothesis

> **Learning Goal:** Design an ideal intracranial recording study.

**Exercise**: If you had access to patients with intracranial electrodes (e.g., epilepsy surgery candidates), design a study to directly test the laminar prediction error hypothesis:

**Hypothesis**: Superficial cortical layers (L2/3) carry ascending prediction errors; deep layers (L5/6) carry descending predictions.

1. **Electrode type**: Linear multi-electrode array spanning cortical layers
2. **Target area**: Primary auditory cortex (A1) — well-studied laminar structure
3. **Paradigm**: Oddball with varying predictability
4. **Expected CSD pattern**: Current source density (CSD) analysis showing:
   - Superficial sink/source pattern for unexpected stimuli (PE)
   - Deep sink/source pattern for predictable stimuli (top-down prediction)
5. **Statistical test**: Compare laminar profiles for expected vs. unexpected stimuli

What confounds must be controlled? (Stimulus-driven activity vs. prediction-related activity)

{fill:textarea}

## Part 5: Reflection

In 300 words, reflect: Electrophysiology provides the temporal resolution to test Active Inference's predictions about neural dynamics. But the mapping from mathematical quantities (prediction errors, precision, predictions) to neural signals (MMN, alpha, gamma) involves significant interpretive assumptions. How confident can we be in these mappings? What alternative explanations exist?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Experiment design | MMN and precision-weighted PE |
| 2 | Oscillatory interpretation | Frequency-band mapping |
| 3 | Multi-level paradigm | Hierarchical prediction errors |
| 4 | Intracranial study design | Laminar prediction hypothesis |
| 5 | Critical evaluation | Neural-computational mapping |
