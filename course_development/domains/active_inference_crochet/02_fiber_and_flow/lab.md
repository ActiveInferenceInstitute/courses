# Lab: Materials Exploration — How Yarn Shapes Inference

## Introduction

This lab puts different yarns in your hands and asks you to notice how your generative model adapts. You will crochet the same stitch pattern in three different fibers, compare the results, and discover that the "same" pattern produces different fabrics because the generative process (the yarn) is different even when the generative model (your pattern and technique) stays the same.

> **Intention:** By the end of this lab, you will have experienced how different materials require model adaptation, compared the sensory information provided by different fibers, and reflected on the relationship between material properties and creative flow.

## Materials

* Three different yarn samples (at least 15 yards each), ideally:
  - One animal fiber (wool, alpaca, or mohair)
  - One plant fiber (cotton, bamboo, or linen)
  - One synthetic fiber (acrylic, nylon, or polyester)
  - All in similar weight (worsted/aran) if possible
* Crochet hook appropriate for the yarn weight
* Ruler or gauge tool
* Notebook and pen
* Optional: blindfold or scarf for the eyes-closed exercise

## Procedure

### Part 1: First Touch — Sensory Profiling (10 minutes)

> **Intention:** Map the sensory information each yarn provides through the Markov Blanket.

1. Close your eyes (or use a blindfold). Pick up each yarn sample in turn.
2. For each yarn, notice and record:
   - Temperature: Does it feel warm, cool, or neutral?
   - Texture: Smooth, rough, fuzzy, slick, grippy?
   - Weight: Heavy, light, dense, airy?
   - Sound: Does it squeak against the hook? Slide silently? Crinkle?
   - Spring: When you stretch it, does it bounce back or stay stretched?

{fill:textarea}
**Reflection**: Which yarn gave you the most sensory information? Which gave the least? In Active Inference terms, which yarn's Markov Blanket transmitted the highest-precision signal to your fingers?

### Part 2: Same Pattern, Different Process (20 minutes)

> **Intention:** Experience how different generative processes produce different outcomes from the same model.

1. With each yarn, crochet a small swatch: Chain 15, then single crochet 10 rows.
2. Use the same hook for all three (unless the yarn weight demands a change — note if you switch).
3. Try to maintain your normal tension for each. Notice when this is easy and when it requires conscious effort.
4. After completing all three swatches, lay them side by side.

{fill:textarea}
**Reflection**: Compare the three swatches. How do they differ in size, drape, stitch definition, and hand-feel? You used the same generative model (same pattern, same stitch, same hook, same crocheter). The differences come entirely from the generative process — the yarn itself. Describe what each yarn's generative process "did" to your model's predictions.

### Part 3: Gauge Comparison (10 minutes)

> **Intention:** Quantify how different materials affect the match between model and process.

1. Using your ruler, measure the width and height of each swatch.
2. Count stitches per inch (or per 4 inches) and rows per inch for each.
3. Record in a table:

| Yarn | Fiber Content | Stitches per inch | Rows per inch | Width | Height |
|------|--------------|-------------------|---------------|-------|--------|
| Yarn A | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Yarn B | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Yarn C | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |

{fill:textarea}
**Reflection**: If a pattern specifies 4 stitches per inch, which yarn comes closest? Which deviates most? What adjustments (hook size, tension) would you make to bring each yarn in line with the pattern's expected gauge? This is model calibration — adjusting your generative model to match a new generative process.

### Part 4: Flow Check (10 minutes)

> **Intention:** Notice which material supports the easiest flow state.

1. Set a timer for 3 minutes. Crochet with Yarn A (no pattern — just single crochet back and forth).
2. After 3 minutes, rate your experience on a 1-5 scale:
   - Ease of stitching: (1 = fought every stitch, 5 = effortless)
   - Rhythm: (1 = halting, 5 = smooth and steady)
   - Enjoyment: (1 = frustrating, 5 = deeply satisfying)
3. Repeat with Yarn B and Yarn C.

| Yarn | Ease (1-5) | Rhythm (1-5) | Enjoyment (1-5) |
|------|-----------|-------------|-----------------|
| Yarn A | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Yarn B | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Yarn C | {fill:textarea} | {fill:textarea} | {fill:textarea} |

{fill:textarea}
**Reflection**: Which yarn brought you closest to a flow state? In Active Inference terms, which yarn produced the lowest prediction errors at the right level of engagement? Does this match which yarn you have the most experience with, and what does that tell you about the role of prior experience in flow?

### Part 5: The Blindfold Test (10 minutes)

> **Intention:** Isolate tactile inference by removing visual information.

1. Close your eyes or use a blindfold.
2. Have someone hand you one of the three yarns (without telling you which).
3. Crochet 5-10 stitches by touch alone.
4. Predict which yarn you are using. Open your eyes and check.
5. Repeat with the other two yarns.

{fill:textarea}
**Reflection**: Could you identify the yarn by touch? What tactile cues did you use? When visual information is removed, what happens to the precision of your remaining sensory channels? Did you notice things about the yarn by touch that you missed when your eyes were open?

## What Did You Notice?

| Activity | What did you observe? | Active Inference concept |
|----------|----------------------|------------------------|
| Sensory profiling | {fill:textarea} | Markov Blanket / sensory states |
| Same pattern, different yarn | {fill:textarea} | Generative process vs. generative model |
| Gauge comparison | {fill:textarea} | Model calibration / precision |
| Flow check | {fill:textarea} | Optimized inference / flow state |
| Blindfold test | {fill:textarea} | Sensory precision / modality shift |

## Discussion Questions

1. Did any yarn surprise you — either in how it felt or how the fabric turned out? What prediction was violated, and how did your model update?
2. If you had to choose only one of these three yarns for every project, which would you choose and why? What does your choice reveal about your prior preferences (the C vector)?
3. How would you describe the relationship between a crocheter and their yarn in Active Inference terms? Is the yarn part of the agent, part of the environment, or part of the Markov Blanket?
