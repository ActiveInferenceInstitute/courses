# Lab: Tracing Signals Through Mesh

## Objective

Crochet a small filet crochet mesh, then physically trace signal paths through the fabric by pulling on various points and observing how force transmits. Map the signal paths on paper and compare the result to a neural network diagram, identifying "strong connections" (solid stitches) and "weak connections" (chain spaces).

## Materials

* Worsted weight yarn in a light color (approximately 40 yards) — light color makes the mesh structure easy to see
* Crochet hook, size H/8 (5.0mm) or I/9 (5.5mm)
* Blank paper (at least 2 sheets) and pen or pencil
* Colored pencils or markers (at least 3 colors)
* Ruler
* Scissors
* Tapestry needle (for weaving ends)
* Optional: a second color of yarn (10 yards) for Part 4
* Optional: a small piece of solid single crochet fabric for comparison (if you have one from a previous lab)

## Steps

### Part 1: Crocheting the Mesh (20 minutes)

You will crochet a filet crochet grid that is 8 blocks wide and 8 rows tall. Each block is either a solid block (3 dc) or an open block (ch 2, dc). For this lab, crochet the following pattern — it includes a mix of solid and open blocks to create varied signal paths.

**Foundation:** Ch 28.

**Row 1 (right side):** Dc in 4th ch from hook (the first 3 chains count as the first dc), dc in next 2 ch [first solid block made], *ch 2, sk 2 ch, dc in next ch [open block made], dc in next 2 ch, dc in next ch [solid block made]*, repeat * to * across. You should have an alternating pattern of solid and open blocks. (4 solid blocks, 4 open blocks — alternating)

If you find the alternating pattern tricky, you may simplify: crochet 4 rows of all open blocks and 4 rows of all solid blocks, or any combination that gives you a grid with both types.

**Rows 2-8:** Continue working filet crochet in the grid pattern. For solid blocks: dc in each of the next 3 dc. For open blocks: ch 2, sk 2 sts, dc in next dc. Turn at the end of each row with ch 3 (counts as first dc of next row).

When finished, you should have a roughly square mesh with clearly visible solid and open sections. Fasten off and weave in ends.

### Part 2: Physical Signal Tracing (15 minutes)

1. Lay the mesh flat on a table. Observe the structure: where are the solid blocks? Where are the open spaces? Notice how the mesh feels when you press down on different areas.

2. **Test 1 — Corner pull.** Gently hold the bottom-left corner with one hand and the top-right corner with the other. Pull gently. Observe:
   - Does the force transmit evenly across the mesh?
   - Do the solid blocks resist stretching more than the open blocks?
   - Does the fabric distort — does one area stretch more than another?

3. **Test 2 — Edge pull.** Hold the left edge with one hand and pull gently on a single stitch in the middle of the mesh with the other hand. Watch how the tug ripples outward. Does it travel more easily along a row of solid blocks or through a row of open blocks?

4. **Test 3 — Point load.** Place one finger on a stitch at the center of the mesh and push gently downward. Observe which surrounding stitches move. Do stitches connected by solid posts move more than stitches connected by chain spaces?

5. **Test 4 — Comparison (optional).** If you have a solid single crochet swatch from a previous lab, perform Tests 1-3 on it as well. Compare: how does the signal propagation differ between the mesh and the solid fabric?

Record your observations for each test. Use phrases like "the force traveled mostly along..." or "the chain spaces stretched while the solid blocks stayed rigid."

### Part 3: Mapping the Signal Paths (15 minutes)

6. On a blank sheet of paper, draw a grid representing your filet crochet mesh. Make each block a small square (about 1 cm). Mark solid blocks with an "S" or fill them in. Mark open blocks with an "O" or leave them empty.

7. Using your observations from Part 2, draw signal paths on the grid:
   - **Strong paths** (where force traveled quickly and directly): draw in one color — bold, solid lines.
   - **Weak paths** (where force was absorbed or dampened): draw in a second color — dashed or thin lines.
   - **Blocked paths** (where force did not seem to transmit at all): mark with an "X" in a third color.

8. Look at your completed signal map. Can you identify any "highways" — continuous paths of solid blocks where signals travel most efficiently? Can you identify any "bottlenecks" — places where a single solid stitch is the only connection between two regions of the mesh?

### Part 4: Neural Network Comparison (15 minutes)

9. On a second sheet of paper, draw a simple feedforward neural network with:
   - An input layer of 8 nodes (bottom row)
   - Two hidden layers of 8 nodes each (middle rows)
   - An output layer of 8 nodes (top row)

   Connect the nodes with lines. Use thick lines for strong connections and thin lines for weak connections.

10. Now compare your two drawings — the filet crochet signal map and the neural network diagram. Answer these questions in writing:
    - Where in the mesh are the "strong connections" (high-weight synapses)? Where are the "weak connections" (low-weight synapses)?
    - Is there a path through the mesh where a signal could travel from the bottom row to the top row entirely through solid blocks? This would be like a "high-confidence path" through a neural network.
    - If you wanted to "block" a signal from reaching a specific area of the mesh, which stitches would you need to change from solid to open? This is analogous to setting connection weights to zero in a neural network (pruning).

11. **(Optional, 10 minutes):** Using the second color of yarn, do a row of surface slip stitches across the mesh, connecting two non-adjacent rows. This creates a "skip connection" — a direct path between layers that bypasses the intermediate rows, just like a residual connection in a ResNet architecture. Pull gently on each end of the surface crochet. Does the signal bypass the intermediate mesh? How does this change the network's behavior?

### Part 5: Stitch Chart as Network Diagram (10 minutes)

12. Using standard crochet chart symbols (T for dc, chain symbol for ch, dot for sl st), draw a symbol chart for 3-4 rows of your filet crochet mesh.

13. Look at the chart. It is a network diagram: each symbol is a node, each connection is an edge. The chart simultaneously represents:
    - The physical layout of the fabric
    - The connectivity of the stitch network
    - The signal paths you traced in Part 2

Write a short paragraph describing how reading this chart is similar to reading a circuit diagram or a neural network architecture drawing.

## Discussion Questions

* Which signal tests (corner pull, edge pull, point load) revealed the most about how the mesh transmits information? Why?
* Were you surprised by how differently the solid blocks and chain spaces behaved under tension? How does this map to the idea of strong and weak connections in a neural network?
* If you were designing a crochet mesh to carry signals efficiently from one corner to the opposite corner, what pattern of solid and open blocks would you use? Sketch it.
* How does the experience of physically feeling signal propagation through fabric change your understanding of how information flows through neural networks?
* If the mesh is a "lossy network" (signals weaken as they travel through chain spaces), what would you need to change to make it a "lossless network"?

## Wrap-Up

You have built a physical network from yarn, tested how signals propagate through it, mapped the signal paths, and compared the result to a neural network diagram. The mesh on your table is not a metaphor for a network — it IS a network, one you built with your own hands. Keep your mesh swatch and signal map for the final module, where we will design network architectures from scratch and plan the topology of our most ambitious crochet projects yet.

**Estimated total time: 75 minutes** (with optional activities: 95 minutes)
