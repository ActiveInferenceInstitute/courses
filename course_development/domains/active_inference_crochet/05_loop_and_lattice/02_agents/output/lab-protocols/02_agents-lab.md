# Lab: Mapping Your Stitch Decisions

## Objective

Crochet a small sampler where you make deliberate, varied stitch choices across several rows. Then map those choices as a decision tree and draw the resulting network graph. By comparing your decisions to the way a neural network architect selects layer types, you will see your own agency as a network designer.

## Materials

* Worsted weight yarn (one color), approximately 30 yards
* Crochet hook, size H/8 (5.0mm)
* Stitch markers (at least 2)
* Scissors
* Paper and pen (two sheets — one for the decision tree, one for the network graph)
* Colored pencils or markers (at least 3 colors) — optional but helpful

## Prerequisites

* Ability to chain (ch), single crochet (sc), double crochet (dc), and half double crochet (hdc)
* Reading of Module 02: The Crocheter as Neural Architect (module.md)
* Completion of Lab 01 (Crocheting Three Surfaces) is recommended but not required

## Steps

### Part 1: Crocheting the Sampler (20 minutes)

You are going to crochet a sampler with 6 rows, each using a different stitch or combination. The key is that **you** will choose the stitch for each row. The pattern provides the framework; you provide the architectural decisions.

1. **Foundation:** Ch 16.

2. **Row 1 — Single Crochet (prescribed).** Sc in 2nd ch from hook and in each ch across. Turn. (15 sc)
   - Before you start: On your decision tree paper, write "Row 1" and draw a box labeled "sc." This is a prescribed decision — no choice involved.

3. **Row 2 — Your Choice.** Choose one: all sc, all hdc, all dc, or a mix (e.g., alternating sc and dc). Work your chosen stitch(es) across the row. Turn.
   - On your decision tree paper, write "Row 2" and draw a branching tree: the options you considered (sc / hdc / dc / mix), and circle the one you chose. Why did you choose it? Write a brief note.

4. **Row 3 — Your Choice.** Again, choose freely. You may repeat your Row 2 choice or try something different. Work across. Turn.
   - Update your decision tree. Note what influenced your choice. Did the look of Row 2 affect your Row 3 decision?

5. **Row 4 — Deliberate Contrast.** Choose a stitch that is noticeably different from Row 3. If Row 3 was sc, try dc. If Row 3 was dc, try sc. Work across. Turn.
   - On the decision tree, note that this was a deliberate contrast decision. Mark how the fabric feels different in your hands.

6. **Row 5 — Mixed Row.** Work a mix of stitch types across the row. For example: *sc in next 3 sts, dc in next 3 sts* — repeat. Or make up your own pattern. Turn.
   - On the decision tree, note this as a "mixed architecture" row. Record the specific combination you used.

7. **Row 6 — Free Choice.** Make the final row whatever feels right to complete the sampler. Work across. Fasten off.
   - Final entry on the decision tree. Note what "felt right" means — what was your generative model predicting for the finished piece?

8. Weave in ends. Hold up your sampler and look at it.

### Part 2: Drawing the Decision Tree (10 minutes)

Review the decision tree you have been building as you crocheted. It should now show 6 rows, with branching options for Rows 2 through 6. For each decision point:

1. Draw the available options as branches.
2. Circle your actual choice.
3. Note the reason for the choice. Categories might include:
   - **Pattern compliance** — "The instructions said to contrast."
   - **Aesthetic prediction** — "I thought dc would look better after sc."
   - **Tactile feedback** — "The fabric felt too stiff; I wanted something more open."
   - **Generative model** — "I had an image in my mind of the finished sampler."
   - **Habit** — "I always default to sc when I am unsure."

4. Look at the tree as a whole. How many decisions did you make? How many did you make consciously versus automatically? Which rows required more deliberation?

### Part 3: Drawing the Network Graph (15 minutes)

Now take your second sheet of paper. You are going to draw the stitch network of your sampler, showing how the architecture changes from row to row.

1. **Row 1 (foundation layer).** Draw 15 small circles in a horizontal line. These are your 15 sc stitches — the input layer.

2. **Row 2.** Above the first row, draw circles for the stitches in Row 2. If you used sc, draw the same 15 circles directly above, each connected by a short vertical line to the stitch below. If you used dc, draw the circles slightly higher (to represent the taller stitch) and use longer vertical lines.

3. **Rows 3-6.** Continue stacking rows. Adjust the height between layers based on stitch type:
   - sc = short gap (tight connection)
   - hdc = medium gap
   - dc = tall gap (extended connection)

4. **Mixed rows.** If a row has mixed stitch types (like Row 5), vary the connection heights within the row. The sc sections should have short connections; the dc sections should have tall ones.

5. **Color coding (optional).** If you have colored pencils, use different colors for different stitch types: one color for sc connections, another for hdc, another for dc.

6. **Examine the network.** Step back and look at your drawing. You have a layered network graph — just like a neural network diagram. Each row is a layer. Each stitch is a node. Each connection (where hook entered the previous row) is an edge. The height and character of the connection varies with stitch type, just as connection weights vary in a neural network.

### Part 4: Comparing Crocheter and Neural Network Architect (10 minutes)

On your decision tree paper, answer the following:

1. **Layer types.** A neural network architect chooses the type of each layer (dense, convolutional, recurrent). You chose the stitch type for each row. Look at your sampler — you built a network with mixed layer types. Why might a neural network architect do the same thing? (Hint: different layer types are good at different things, just as different stitches produce different textures and structural properties.)

2. **Weights.** Feel the fabric with your fingers. Do some rows feel tighter or looser? Did your tension vary across the sampler? This is weight variation. A neural network's weights are its learned parameters; your tension is yours.

3. **Architecture vs. training.** The stitch choices you made are architecture decisions (what kind of connections). The tension you applied is a weight/parameter decision. Both shaped the final fabric. In neural networks, both architecture and weights determine the output. Which do you think matters more for the character of your sampler — the stitch choices or the tension?

4. **The generative model.** When you made Row 6 — the free choice — you chose what "felt right." That feeling was your generative model producing a prediction of the finished sampler. Describe what that prediction looked like. Did the actual Row 6 match the prediction, or did you experience prediction error?

### Part 5: Reflection and Discussion (5 minutes)

Hold your sampler in one hand and your decision tree in the other.

## Discussion Questions

* Over 6 rows and 15 stitches per row, you made approximately 90 explicit stitch decisions and many more micro-decisions (hook placement, tension, timing). Were you aware of each one, or did many happen automatically? What does this tell you about the relationship between conscious and unconscious decision-making in Active Inference?

* Your decision tree shows the reasons behind your choices. How many of those reasons were about matching a prediction (generative model), and how many were about responding to something unexpected (prediction error)? Which rows involved more active inference and which involved more perceptual inference?

* Compare your sampler to a classmate's (or imagine someone else making the same lab exercise). Even though you started with the same foundation chain and the same options, the resulting fabrics would differ. What is the crocheter-equivalent of what machine learning calls "trained on different data"?

* If you were to crochet this sampler again from scratch, would you make the same decisions? What has your generative model learned from this first iteration that would change the second?

## Wrap-Up

You have experienced what it means to be a neural architect: making layer-by-layer decisions that shape a physical network, recording those decisions as a tree, and mapping the result as a graph. Your sampler is a six-layer network with heterogeneous layer types — something a neural network engineer might call a "mixed architecture." Your decision tree is the design log. Your network graph is the blueprint of what you built.

Keep the sampler, the decision tree, and the network graph together. They form a complete record of architectural agency — the crocheter as designer, builder, and reflective practitioner. Bring all three to the next crochet circle for group comparison: how different are the architectures that different crafters build from the same starting point?
