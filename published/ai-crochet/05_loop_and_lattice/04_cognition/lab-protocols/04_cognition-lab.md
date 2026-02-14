# Lab: Building a Layered Sampler

## Objective

Crochet a small sampler where each row uses a different stitch pattern, creating a physical object with visible "layers." Then diagram the sampler as a neural network — mapping each row to a network layer, annotating what features each layer represents, and tracing how information transforms from the foundation chain (input) to the final row (output). This lab makes the hidden-layer structure of both crochet and neural networks tangible and visual.

## Materials

* Worsted weight yarn, solid light color (light colors show stitch texture best)
* Crochet hook, size H/8 (5.0mm)
* Scissors
* Tapestry needle (for weaving ends)
* Blank paper (at least 2 large sheets, letter size or bigger)
* Colored pencils or markers (5-6 colors)
* Ruler
* Stitch markers (optional, for counting)
* A partner or crochet circle companions (recommended for discussion)

## The Sampler Pattern

You will crochet a sampler that is 20 stitches wide and 7 rows tall. Each row uses a different stitch, creating distinct visible layers. If you are comfortable adjusting, feel free to make it wider — the key is that each row uses a different stitch pattern.

**Foundation Chain (Input Layer)**
- Chain 21.

**Row 1 — Single Crochet (sc)**
- Sc in 2nd chain from hook and in each chain across. (20 sc)
- Turn.

**Row 2 — Half Double Crochet (hdc)**
- Ch 2 (does not count as a stitch). Hdc in each st across. (20 hdc)
- Turn.

**Row 3 — Double Crochet (dc)**
- Ch 3 (counts as first dc). Dc in each st across. (20 dc)
- Turn.

**Row 4 — Shell Stitch**
- Ch 1. Sc in first st. *Skip 2 sts, 5 dc in next st (shell made), skip 2 sts, sc in next st.* Repeat * to * across. You should get approximately 3 full shells depending on your count. Adjust as needed to end with a sc.
- Turn.

**Row 5 — Back Post Double Crochet (bpdc)**
- Ch 3 (counts as first dc). *Bpdc around the post of the next dc-height stitch in the row below (you will be reaching into the shell row — find the tall stitches).* Work bpdc or dc across as the stitches allow, aiming for 20 stitches. This row creates a ribbed, textured surface.
- Turn.

**Row 6 — Seed Stitch (alternating sc and ch-1)**
- Ch 1. *Sc in next st, ch 1, skip next st.* Repeat across, ending with sc in last st.
- Turn.

**Row 7 — Single Crochet Border (Output Layer)**
- Ch 1. Sc in each st and ch-1 space across, ensuring you end with 20 sc. This final row unifies the varied textures below into a clean, even edge.
- Fasten off. Weave in ends.

**Note for beginners**: If any stitch is unfamiliar, substitute a stitch you know. The goal is variety between rows, not perfection. Even using just single crochet, half double crochet, and double crochet in alternating rows will create visible layers.

**Estimated crocheting time**: 30-40 minutes.

## Steps

### Part 1: Crocheting the Sampler (30-40 minutes)

1. Work through the sampler pattern above, one row at a time. As you crochet each row, pay attention to how the new stitch pattern changes the texture and appearance of the fabric.
2. After completing each row, pause briefly and feel the fabric. Notice how the current row's texture differs from the row below. This is the tactile difference between hidden layers.
3. When the sampler is complete, lay it flat and look at it from the side (the edge). You should be able to see the distinct layers — each row contributing a different texture to the whole.

### Part 2: Diagramming the Neural Network (20 minutes)

4. Take a large sheet of paper and draw a diagram of your sampler as a neural network. Use this structure:

```
[Input Layer: Foundation Chain — 21 chain stitches]
        |
[Hidden Layer 1: Single Crochet — 20 sc]
        |
[Hidden Layer 2: Half Double Crochet — 20 hdc]
        |
[Hidden Layer 3: Double Crochet — 20 dc]
        |
[Hidden Layer 4: Shell Stitch — ~3 shells + sc between]
        |
[Hidden Layer 5: Back Post Double Crochet — 20 bpdc]
        |
[Hidden Layer 6: Seed Stitch — alternating sc and ch-1]
        |
[Output Layer: Single Crochet Border — 20 sc]
```

5. For each layer, annotate the following using different colored pencils:
   - **Stitch count** (how many "neurons" in this layer)
   - **Stitch height** (sc is short, dc is tall — this is like the activation function's range)
   - **Texture produced** (smooth, ribbed, scalloped, open, etc.)
   - **What "feature" does this layer represent?** (dense base, medium texture, tall open fabric, fan shapes, ribbed texture, open mesh, unified border)

6. Draw lines connecting the layers. Notice that each stitch in a row connects to one or more stitches in the row below — just as each neuron connects to neurons in the previous layer. The shell stitch layer is especially interesting: each shell gathers input from three stitches below and fans out into five stitches, like a neuron with a wide receptive field.

### Part 3: Tracing Information Transformation (15 minutes)

7. On your diagram, trace the "information flow" from the foundation chain to the final row. Use arrows to show how the raw input (a plain chain) is transformed layer by layer:
   - The chain becomes individual stitches (Layer 1).
   - The stitches gain height and openness (Layers 2-3).
   - The stitches are grouped into emergent patterns — shells (Layer 4).
   - The texture is transformed into ribbing (Layer 5).
   - The ribbing opens into mesh (Layer 6).
   - The mesh is consolidated back into a uniform edge (Output layer).

8. Ask yourself: at which layer does the sampler become "interesting"? At which layer do emergent features appear that are not present in the input? Mark this on your diagram. This is where the hidden representations begin.

9. Now mark where information is "lost" or "compressed." The shell stitch layer takes 20 stitches and groups them into roughly 3 shells — this is a form of compression, like a pooling layer in a CNN. The final sc row takes the varied texture and flattens it into a uniform surface — this is like the output layer reducing a complex representation to a simple classification.

### Part 4: Connecting to the Crocheter's Mental Model (10 minutes)

10. On a new sheet of paper, draw the same layer diagram but from the perspective of your mind while crocheting. Label each layer with what you were thinking about at that level:
    - **Stitch level**: "Yarn over, insert hook, pull through..." (the mechanical actions)
    - **Row level**: "This row is half double crochet. I need 20 stitches." (the pattern instructions)
    - **Texture level**: "This row should create a taller, looser fabric than the one below." (the expected feature)
    - **Sampler level**: "I am building a sampler that shows how different stitches create different textures." (the project goal)

11. Draw arrows showing how your top-down understanding of the project ("I am making a sampler") shaped your moment-to-moment decisions at the stitch level. This is the deep generative model at work.

### Part 5: Reflection and Group Discussion (10 minutes)

12. Lay your physical sampler next to your neural network diagram. Compare the two:
    - Does the diagram capture the structure of the sampler? What does it miss?
    - Which layer of the sampler is the most "hidden" — the most different from what you would expect based on the input alone?
    - If you frogged back to Row 3 and re-crocheted Rows 4-7 with different stitches, how would the "output" change? This is like retraining the upper layers of a network while keeping the lower layers frozen.

13. Share your diagram and sampler with your crochet circle. Compare how different people annotated their layers. Did everyone identify the same features?

## Discussion Questions

* The shell stitch layer takes 20 input stitches and produces approximately 3 shells. This is a kind of spatial compression. How does this compare to a pooling layer in a CNN, which reduces spatial resolution to capture higher-level features?

* Your sampler's final row (single crochet) creates a uniform edge that "hides" the complexity of the layers below, much as a neural network's output layer reduces complex hidden representations to a simple prediction. Is the output layer the most informative layer, or the least? Where does the real work happen?

* If you were to teach a neural network to recognize which stitch pattern was used in each row of your sampler from a photograph, what features would each layer of the CNN need to detect? How does this network-perceiving-a-network idea make you think about the relationship between the fabric's structure and the observer's cognition?

* When you picked up the project after completing Row 4 (shells) and started Row 5, did you have to "re-read" the fabric to figure out where to insert your hook? If so, you were performing perceptual inference on your own hidden layers — using your generative model to decode the emergent structure you had just created.

## Wrap-Up

You have built a physical neural network out of yarn — a layered structure where each row transforms the input from the row below, creating emergent textures that no single row could produce on its own. Your diagram maps this structure onto the architecture of a deep neural network, and your annotations trace the flow of information from raw chain to finished edge. Keep your sampler and diagram for reference in upcoming modules, where we will explore how action (the hand movements that create stitches) maps to network training, and how learning in crochet parallels learning in neural networks.

**Estimated Total Time**: 85-95 minutes
- Crocheting: 30-40 minutes
- Diagramming: 20 minutes
- Tracing information: 15 minutes
- Mental model mapping: 10 minutes
- Discussion: 10 minutes
