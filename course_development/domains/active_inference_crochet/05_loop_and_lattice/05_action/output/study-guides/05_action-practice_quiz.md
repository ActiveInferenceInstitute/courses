# Practice Quiz: Action

## Part A: Multiple Choice

1. When a crocheter works 2 sc into a single stitch (an increase), the local effect on the fabric is:
A) Positive Gaussian curvature — the fabric cups inward
B) Negative Gaussian curvature — the fabric ruffles outward
C) Zero Gaussian curvature — the fabric stays flat
D) The curvature is unaffected by increases

2. In a flat single crochet circle, the standard rule is to add 6 increases per round. If you add only 3 increases per round instead, the fabric will:
A) Ruffle dramatically because there is too much surface area
B) Stay perfectly flat
C) Cup into a bowl shape because there is not enough surface area for flatness
D) Form a tube

3. Frogging (ripping back multiple rows) is best understood as analogous to which neural network operation?
A) Adding a new hidden layer
B) Rolling back gradient descent steps to an earlier weight configuration
C) Increasing the learning rate
D) Deploying the trained model to production

4. When a crocheter skips a stitch and chains over the gap, the topological effect is:
A) A change in Gaussian curvature only
B) An increase in the genus of the surface — a hole has been created
C) A decrease in surface area with no topological change
D) The fabric becomes a closed surface

5. Joining the last stitch of a row to the first stitch with a slip stitch transforms the fabric from:
A) A sphere to a torus
B) A tube to a flat disc
C) A strip (open edges) to a tube (closed loop)
D) A surface of genus 1 to genus 0

6. In active inference, the crocheter selects shaping actions (increases, decreases, stitch placement) to:
A) Maximize the difference between the pattern and the fabric
B) Minimize free energy — the gap between the predicted shape and the observed shape
C) Avoid all changes to the fabric topology
D) Randomly explore the action space

7. A crocheter working into the front loop only (FLO) instead of both loops is performing an operation that:
A) Has no effect on the fabric structure
B) Changes the connectivity between the current row and the row below, creating a visible ridge
C) Increases the genus of the surface
D) Converts the fabric from a manifold to a non-manifold surface

## Part B: Short Answer

1. An amigurumi sphere starts with a magic ring, increases outward to the widest point, works several straight rounds, then decreases to close. Describe the Gaussian curvature at each phase (magic ring expansion, straight middle, closing decreases) and explain how the crocheter's shaping actions control it.

2. A crocheter notices that their intended flat circle is ruffling after round 5. Describe this situation using the active inference framework: What is the generative model's prediction? What is the observed state? What actions might the crocheter select to reduce the free energy (the gap between prediction and reality)?

3. Compare the crocheter tracing a shaping error back to its source (and frogging to that point) with the backpropagation algorithm tracing error through a neural network. What is being "propagated backward" in each case, and what gets adjusted?
