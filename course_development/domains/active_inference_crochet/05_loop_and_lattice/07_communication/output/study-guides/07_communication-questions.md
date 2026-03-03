# Study Questions: Communication — Signals Through the Mesh

1. When you tug on one corner of a filet crochet mesh, the force propagates through the fabric. Describe how the pattern of solid blocks and chain spaces determines which paths carry the force most strongly. How is this similar to connection weights in a neural network?

2. Explain the difference between a "lossy network" (mesh with many chain spaces) and a "low-loss network" (solid fabric with no holes) in terms of signal propagation. Give a crochet example of each and describe how pulling on one edge would feel different in each case.

3. In a filet crochet grid, a missed chain space in Row 3 causes a misalignment that propagates into subsequent rows. Compare this error propagation to how errors flow through a neural network. What does the crocheter's frogging-back process correspond to in neural network training?

4. Describe how the foundation chain of a crochet piece functions as the "input layer" of a neural network. What happens to this "input signal" as it passes through each subsequent row?

5. The module compares single crochet to a ReLU activation function (simple, direct) and shell stitches to a softmax function (one input fans into many outputs). Choose two other stitch types and propose what activation function they might correspond to. Explain your reasoning.

6. A filet crochet chart is described as a "bitmap" — a grid of binary values (solid or open). If a filet crochet piece is 50 blocks wide and 80 rows tall, how many "bits" of visual information does it encode? What determines the "resolution" of this pixel-based communication system?

7. Explain how color pooling is an emergent phenomenon. Why can neither the color sequence in the yarn nor the stitch pattern alone predict the visual result? What does this tell us about how signals interact in complex networks?

8. Written crochet patterns are sequential (one instruction after another), while stitch charts are spatial (showing the fabric layout as a grid). How does each format mirror a different aspect of the fabric's topology? Which is better for understanding signal paths, and why?

9. Describe the three components of crochet pattern notation as a communication protocol: syntax, semantics, and channel. Give a specific example of each and explain how a failure in any one component could cause miscommunication.

10. The module states that "the topology of the notation system mirrors the topology of the fabric it describes." Explain what this means by comparing a filet crochet chart to the physical mesh it represents. In what sense is the chart literally a network diagram?

11. A crocheter notices that their mesh fabric is pulling to one side — the tension on the left edge is tighter than on the right. Describe this as a signal propagation problem. What does the uneven tension tell you about the network's connectivity or the "weights" on different paths?

12. In Active Inference, prediction error drives model updating. When a crocheter is following a filet crochet chart and the fabric does not match the picture they expected, what kind of prediction error is this? What are the possible sources of the mismatch (pattern error, reading error, execution error)?

13. Compare a crochet stitch chart to an electronic circuit diagram. What are the "components" in each? What are the "wires"? What "signals" flow through each system? Where does the analogy hold strongly and where does it break down?

14. When a designer creates a crochet pattern, they encode their generative model of the fabric into notation. What information might be lost in this encoding? Think about tension, hand position, yarn behavior, and other aspects of the crafting experience that are hard to write down.

15. Describe how tension propagates backward through the fabric when you pull the working yarn. Why does this backward propagation matter for maintaining consistent gauge? Connect this to the concept of feedback signals in recurrent neural networks.

16. A crocheter working a lace pattern with many chain spaces and picots notices that the fabric is very flexible and stretchy compared to a solid double crochet fabric. Explain this difference in terms of signal attenuation — how the chain spaces act as "weak connections" that absorb and redistribute force.

17. Filet crochet has been used for centuries to encode words and pictures in fabric. Describe how this tradition makes filet crochet a literal communication medium — a way to send a message through textile. What are the "bandwidth" limitations of this medium compared to, say, a printed page?

18. In a neural network, a "dead neuron" is one whose activation function always outputs zero, effectively disconnecting it from the network. What would be the crochet equivalent of a dead neuron in a mesh? How would it affect signal propagation through the fabric?

19. The module describes the crocheter as performing "their own version of backpropagation" when they detect and fix errors. Walk through a specific example: you are crocheting a filet crochet piece and notice in Row 10 that your stitch count is off. Describe the steps of detecting the error, tracing it backward, and correcting it — and map each step to a phase of the backpropagation algorithm.

20. Reflect on your own experience reading crochet patterns. Do you prefer written instructions, charts, or videos? How does your preference relate to how you process information about network structure — sequentially or spatially? How might understanding your preference help you communicate crochet knowledge to others more effectively?
