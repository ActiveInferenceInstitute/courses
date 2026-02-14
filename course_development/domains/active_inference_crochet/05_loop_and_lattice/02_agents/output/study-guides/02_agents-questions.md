# Study Questions: Agents

1. The module describes the crocheter as a "neural architect." In what sense is this literal rather than metaphorical? What does the crocheter's brain and the crocheted fabric have structurally in common?

2. When a crocheter chooses between single crochet, double crochet, and treble crochet for a given row, they are selecting among different connection types. Compare this to a neural network engineer choosing an activation function. How does each stitch type transform the "signal" passing through the fabric?

3. Two crocheters follow the same pattern with the same yarn but produce noticeably different fabric — one is stiff and dense, the other is drapey and soft. In neural network terms, what parameter differs between them, even though the architecture is identical?

4. Describe the process of making a gauge swatch in terms of Active Inference. What is the generative model? What is the prediction? What constitutes prediction error? How does the crocheter minimize free energy?

5. At the moment of inserting the hook into the next stitch, the crocheter faces a decision node. List at least five distinct micro-decisions available at this single point (where to insert, how deep, which loops, which stitch type, how much tension).

6. An experienced crocheter can work while watching television, barely glancing at their hands. What does this tell us about the role of the generative model in Active Inference? How well-trained must the model be for this to work?

7. A beginning crocheter must look at every stitch, count constantly, and frequently pause to check their work. Compare their Active Inference cycle to that of the experienced crocheter. Where is most of the free energy?

8. When crocheting a shell stitch (5 dc in 1 st), the crocheter creates a fan-out node — one parent stitch connecting to five children. Compare this to a neural network layer that expands dimensionality. What information processing purpose might this serve in both the fabric and the network?

9. A decrease stitch (sc2tog or dc2tog) merges multiple nodes into one. In what crochet situations do you use decreases, and what is the architectural effect on the network? How does this compare to pooling layers in a convolutional neural network?

10. Consider the concept of **dropout** in neural networks, where random connections are temporarily removed during training. Is there a crochet analog? Think about skipped stitches, chain spaces, and lace patterns.

11. A crocheter working freeform (without a pattern) is making architectural decisions purely from their internal generative model. Describe this process in Active Inference terms. What replaces the external pattern as the source of predictions?

12. The module suggests that tension is a continuous weight parameter. If you deliberately vary your tension across a single row — starting tight and gradually loosening — what happens to the fabric? How does this compare to a neural network with non-uniform weights across a layer?

13. When a crocheter discovers a mistake three rows back, they face a choice: frog back to fix it, or continue and compensate. Frame this as an Active Inference decision. What are the costs and benefits of each strategy in terms of free energy minimization?

14. In a crochet circle, multiple agents build separate modules (squares, motifs) that are later joined into a collective piece. How does this compare to modular or ensemble neural network architectures? What happens at the "joining" step that did not exist at the individual building step?

15. The module describes a "neural network building a neural network." Unpack this recursion. The crocheter's brain encodes the pattern, predicts stitch outcomes, processes sensory feedback, and issues motor commands. The yarn fabric receives these commands and provides feedback. Draw the loop connecting these two networks.

16. Working into the front loop only (FLO) or back loop only (BLO) leaves one loop unworked. In neural network terms, this is like pruning a connection. What is the structural and visual effect on the fabric? When might a crocheter-architect deliberately choose this "pruned" connection?

17. A crochet pattern is an external representation of a network architecture. Compare the pattern to a neural network specification (number of layers, nodes per layer, connection types). What information does a crochet pattern encode, and what does it leave to the crocheter's discretion?

18. The crocheter's hands receive constant tactile feedback: yarn tension, hook resistance, fabric flexibility. This sensory stream is processed by the brain's neural network and used to adjust motor output. Describe this feedback loop as an Active Inference cycle, identifying sensory states, active states, and the Markov blanket between the crocheter's nervous system and the fabric.

19. Consider a crocheter who invents a new stitch — a novel combination of yarn overs, insertions, and pull-throughs that creates a connection pattern no standard stitch produces. In neural network terms, what has this crocheter done? How does this relate to the concept of architecture innovation?

20. Reflect on your own crochet practice (or imagine yourself learning to crochet). At what point does the crocheter stop being a "pattern follower" and start being a "neural architect"? What skills, knowledge, or experiences mark the transition from executing someone else's architecture to designing your own?
