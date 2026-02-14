# Lab: Feeling Topology

## Objective

Explore how crocheters perceive topological features — curvature, flatness, and shape — through touch alone. By working blindfolded with pre-made curvature samples, you will experience your own hands as topological sensors and compare tactile feature extraction to visual feature extraction. This lab connects the crocheter's embodied perception to how convolutional neural networks detect features in images.

## Materials

* Three pre-crocheted curvature samples (see Preparation below)
* Crochet hook, size H/8 (5.0mm)
* Worsted weight yarn in any color
* Blindfold or sleep mask
* Blank paper and colored pencils or markers (at least 3 colors)
* Flat surface (table or blocking mat)
* A partner or crochet circle companions (recommended)
* Curvature Log sheet (template below)
* Pins (for the curvature mapping exercise)

## Preparation (Before the Lab Session — 30 minutes)

Prepare three curvature samples in advance. Each is a small circle worked in single crochet, in the round, starting with a magic ring. Use the same yarn and hook for all three so that the only variable is curvature.

**Sample A — Flat (Zero Curvature)**
- Round 1: 6 sc into magic ring (6)
- Round 2: 2 sc in each st around (12)
- Round 3: *sc, 2 sc in next st* around (18)
- Round 4: *sc in next 2 sts, 2 sc in next st* around (24)
- Round 5: *sc in next 3 sts, 2 sc in next st* around (30)
- Round 6: *sc in next 4 sts, 2 sc in next st* around (36)
- Fasten off. This circle should lie perfectly flat.

**Sample B — Positive Curvature (Dome/Cup)**
- Round 1: 6 sc into magic ring (6)
- Round 2: 2 sc in each st around (12)
- Round 3: *sc, 2 sc in next st* around (18)
- Round 4: sc in each st around (18) — no increases
- Round 5: *sc in next 2 sts, 2 sc in next st* around (24)
- Round 6: sc in each st around (24) — no increases
- Fasten off. This piece should cup into a dome or bowl shape.

**Sample C — Negative Curvature (Ruffle/Hyperbolic)**
- Round 1: 6 sc into magic ring (6)
- Round 2: 2 sc in each st around (12)
- Round 3: 2 sc in each st around (24)
- Round 4: *sc, 2 sc in next st* around (36)
- Round 5: *sc, 2 sc in next st* around (54)
- Fasten off. This piece should ruffle dramatically — it has far too many stitches for its radius.

Label each sample on the back with a small tag (A, B, C) that participants will not feel during the blind test.

## Curvature Log Template

| Trial | Sample | Tactile Observations | My Guess (Flat / Dome / Ruffle) | Actual | Correct? | Notes |
|-------|--------|---------------------|---------------------------------|--------|----------|-------|
| 1 | ? | | | | | |
| 2 | ? | | | | | |
| 3 | ? | | | | | |

## Steps

### Part 1: Blindfolded Topology Detection (20 minutes)

1. A partner shuffles the three samples and places them in random order in front of you.
2. Put on the blindfold. Take a breath. Let your hands become your primary sensors.
3. Pick up the first sample. Explore it with both hands. Notice:
   - Does it lie flat on the table, or does it resist flatness?
   - When you press it flat, does it spring back? In which direction?
   - Does it feel like it has "extra" fabric, or "not enough"?
   - Can you feel the edge behavior — does the edge lie still, or does it wave?
4. In your Curvature Log, record your tactile observations and your guess: Flat, Dome (positive curvature), or Ruffle (negative curvature).
5. Set it aside and repeat for the second and third samples.
6. Remove your blindfold. Check your guesses against the labels. Record your accuracy.

**Discussion pause**: In your circle, share your results. What tactile cues were most diagnostic? Did anyone get one wrong? Which curvature was easiest to identify by touch? Which was hardest?

### Part 2: Visual Topology Detection (10 minutes)

7. Now examine all three samples visually, side by side on a flat surface.
8. For each sample, observe:
   - How does it sit on the table? Flat, cupping up, or ruffling?
   - Look at the edge: straight, pulling in, or waving?
   - Look at the center: does it rise, sink, or stay level?
9. In your notes, describe the visual features that tell you about the curvature. Compare these to the tactile features you used while blindfolded.

**Discussion pause**: Which was faster — identifying curvature by touch or by sight? Which gave you more information? Which gave you different information?

### Part 3: Drawing Curvature Maps (20 minutes)

10. Take a blank sheet of paper for each sample. Place the sample on the paper and trace its outline (approximately — it does not need to be perfect).
11. Using colored pencils, create a curvature map for each sample:
    - **Blue** = areas of zero curvature (flat regions)
    - **Red** = areas of positive curvature (cupping, doming)
    - **Green** = areas of negative curvature (ruffling, waving)
12. Color in your traced outline to show where each type of curvature occurs. For the flat sample, it should be mostly blue. For the dome, the center will be red. For the ruffle, the edges will be green with increasingly intense ruffling toward the outside.
13. Add arrows showing the direction of curvature — does the fabric curve up, down, or wave side to side?
14. Label each map with the stitch count per round and note how the increase rate creates the curvature.

### Part 4: Connecting to Neural Networks (15 minutes)

15. Look at your three curvature maps. You have just performed manual feature extraction — detecting and classifying curvature features in a physical surface.
16. Now consider: if a CNN were trained on photographs of crocheted circles, what features would it need to detect to classify curvature type?
    - **Layer 1 features**: Individual stitch texture, light and shadow patterns
    - **Layer 2 features**: Row-level patterns, gauge consistency
    - **Layer 3 features**: Edge behavior (straight, pulling, waving), surface behavior (flat, rising, folding)
    - **Layer 4 features**: Overall shape classification (flat circle, dome, hyperbolic surface)
17. On a new sheet of paper, draw a simple diagram of a four-layer neural network. Label each layer with both the CNN features (edges, textures, parts, objects) and the crochet perception features (stitch, row, section, shape). Draw arrows showing how information flows from raw input to final classification.
18. Mark where prediction errors would occur in each layer if the network (or the crocheter) encountered an unexpected curvature.

### Part 5: Reflection and Group Discussion (10 minutes)

19. Review your Curvature Log, curvature maps, and network diagram. Reflect on the following:
    - What surprised you about how much (or how little) you could perceive through touch alone?
    - Did the visual examination reveal anything that touch missed, or vice versa?
    - How does the hierarchical structure of your crochet perception compare to the layered structure of a neural network?
20. Share one insight with your crochet circle.

## Discussion Questions

* When you felt the ruffling sample blindfolded, could you tell that it had negative curvature, or did you just know it was "not flat"? What is the difference between detecting that something is wrong and knowing what kind of wrong it is?
* Daina Taimina used crochet to make hyperbolic geometry tangible for mathematicians. After this lab, do you understand hyperbolic curvature better through touch than through equations? What does this tell you about the role of embodied perception in understanding abstract concepts?
* In your curvature maps, was the curvature uniform across each sample, or did it vary from center to edge? What does this tell you about how increase rate affects local versus global curvature?
* If you were designing a "curvature sensor" for a robot that needed to assess crocheted fabric, what tactile measurements would you program it to take? How would you organize those measurements into a hierarchical feature extractor?

## Wrap-Up

You have used your hands as topological instruments, detecting Gaussian curvature through touch before confirming it with vision. You have drawn curvature maps that visualize the geometry embedded in yarn, and you have connected your perceptual experience to the layered feature extraction of convolutional neural networks. Keep your three curvature samples and your maps — they will serve as reference objects in upcoming modules.

**Estimated Total Time**: 75 minutes (plus 30 minutes preparation for samples)
