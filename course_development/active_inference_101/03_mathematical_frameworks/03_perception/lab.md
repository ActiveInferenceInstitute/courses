# Lab: Free Energy and Perceptual Inference

> **Learning Goal:** Compute free energy and precision-weighted prediction errors for simple scenarios.

## Part 1: Computing Prediction Error

**Exercise**: For each scenario, identify o, g(s), and compute the prediction error (o - g(s)):

| Scenario | Observation o | Prediction g(s) | Error |
|---------|--------------|-----------------|-------|
| You expect the room to be 20°C but measure 24°C | 24 | 20 | |
| You predict your friend will arrive at 7:00 PM and they arrive at 7:00 PM | 7:00 | 7:00 | |
| You expect a package to weigh 1kg but it weighs 3kg | 3 | 1 | |

{fill:textarea}

## Part 2: Precision Weighting

> **Learning Goal:** See how precision changes the influence of prediction errors.

**Exercise**: Using the formula F ∝ ½ π(o - g(s))², compute weighted prediction error for:

| Scenario | Error (o - g(s)) | Precision π | Weighted error ½π(o-g(s))² | Interpretation |
|---------|-------------------|------------|---------------------------|---------------|
| Trusting a digital thermometer | 4 | 10 | | |
| Trusting a broken thermometer | 4 | 0.1 | | |
| Slight color difference in bright light | 2 | 5 | | |
| Slight color difference in dim light | 2 | 0.5 | | |

Which errors matter more? Why?

{fill:textarea}

## Part 3: Free Energy Decomposition

> **Learning Goal:** Analyze the accuracy-complexity trade-off.

**Scenario**: Two models explain why your friend is late:

- Model A (simple): "Traffic is bad" — complexity = 1, accuracy = 5
- Model B (complex): "There was a traffic jam caused by a circus elephant that escaped and a simultaneous meteor shower" — complexity = 10, accuracy = 6

1. Compute F = complexity - accuracy for each (note: lower F is better)
2. Which model does the free energy principle prefer? Why?
3. How does this relate to Occam's razor?

{fill:textarea}

## Part 4: Hierarchical Prediction Error

> **Learning Goal:** Trace prediction errors up and predictions down through a hierarchy.

**Exercise**: Consider a 3-level hierarchy for reading a word:

- Level 3 (context): Predicts the sentence topic
- Level 2 (word): Predicts the next word based on context
- Level 1 (letters): Predicts which letters based on the word

You're reading: "The cat sat on the ___" and the next word is "mat."

1. What does Level 3 predict? Is there prediction error?
2. What does Level 2 predict? Is there prediction error?
3. What does Level 1 predict? Is there prediction error?
4. Now change the word to "xylophone." Where are the prediction errors largest?

{fill:textarea}

## Part 5: Reflection

In 150 words, reflect: The equation F ∝ ½ π(o - g(s))² is remarkably simple — yet it formalizes perception, attention, and belief updating. Why is mathematical simplicity valuable in a scientific theory?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Prediction error computation | Basic prediction error |
| 2 | Precision analysis | Weighted prediction errors |
| 3 | Trade-off evaluation | Accuracy-complexity balance |
| 4 | Hierarchical tracing | Multi-level prediction errors |
| 5 | Theory reflection | Value of mathematical formalization |
