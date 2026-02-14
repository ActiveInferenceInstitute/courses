# Study Questions: Planning — Designing Architectures in Yarn

1. The module states that "the architecture comes first, the stitching comes second." List four architectural decisions a crocheter must make before beginning a project and explain how each one has topological consequences.

2. Explain the Euler characteristic (V - E + F = chi) in your own words. Why is chi = 1 for a flat disc, chi = 2 for a sphere, and chi = 0 for a torus? What does this number tell a crocheter about shaping requirements?

3. A crocheter is planning a flat circle in single crochet and knows they need to increase by 6 stitches per round. Explain why this number is not arbitrary — how does it relate to the geometry of the surface and the height of a single crochet stitch?

4. You want to crochet a toroidal cowl (chi = 0). The module explains that positive curvature on the outer rim must be canceled by negative curvature on the inner rim. In practical terms, what does this mean for your stitch count on the outside versus the inside of the torus?

5. Compare the architectural decision of "working in rows vs. working in the round" to the neural network decision of "feedforward vs. recurrent." How does each choice fundamentally change the topology of the resulting structure?

6. Describe how a granny square blanket is analogous to a convolutional neural network. What is the "kernel" (filter)? What is the "stride"? What does it mean that the same motif is applied repeatedly across the surface?

7. The module maps front post and back post stitches to skip connections in a ResNet. Explain this analogy in detail. What information is "skipping" when you work a front post double crochet around a stitch two rows below?

8. Explain how "dropout" in neural networks (randomly deactivating neurons during training) maps to chain spaces in a mesh pattern. Why does this deliberate introduction of gaps make both the neural network and the fabric more flexible and resilient?

9. A crocheter plans an amigurumi ball (sphere, chi = 2) with 6 increases per round for the first 8 rounds. How many stitches are at the equator? How many rounds of 6 decreases will be needed to close the sphere? Why must the increase and decrease rates balance?

10. Describe the Active Inference concept of "expected free energy" as it applies to choosing a crochet project. What is the pragmatic value component? What is the epistemic value component? Give a concrete example of a project choice where these two components pull in different directions.

11. The module suggests that making a gauge swatch is an "epistemic action" — an action whose primary value is reducing uncertainty. Explain why a gauge swatch has high epistemic value for planning purposes. Can you think of other epistemic actions in crochet planning?

12. Describe how you would plan a crochet piece that represents a 3-layer feedforward neural network with 8 input neurons, 4 hidden neurons, and 2 output neurons. What stitch operations correspond to the connections between layers? How would you represent "strong" versus "weak" connections?

13. A Klein bottle has Euler characteristic 0, the same as a torus. Yet the module says a Klein bottle is fundamentally different to crochet than a torus. What topological property distinguishes them, and how does this affect the planning process?

14. When planning a hyperbolic coral reef piece, why does increasing more than 6 stitches per round (for single crochet) produce ruffling? Connect the excess increases to the concept of negative Gaussian curvature and explain how the degree of ruffling relates to the magnitude of the excess.

15. Experienced crocheters often start complex projects by working the most uncertain part first (the shaped crown of a hat, the tricky lace panel of a shawl). Explain this strategy in terms of expected free energy minimization. Why is it better to encounter failure early rather than late?

16. The module describes attention mechanisms in transformer networks as analogous to color changes and texture highlights in crochet. Explain this analogy. How does a bobble stitch in a field of single crochet function like an attention head that "focuses" on a specific location?

17. If you were designing a crochet piece inspired by an autoencoder neural network (a network that first compresses and then expands its representation), what would the shape of the piece look like? Describe the increase and decrease schedule.

18. How does the choice between "joined as you go" and "seamed" construction relate to the difference between monolithic and modular neural network architectures? What are the advantages and disadvantages of each approach in crochet?

19. The module ends by saying that "the mathematics has been there all along, in your hands." Reflect on a specific crochet project you have made (or would like to make). Identify the topological decisions you made (or would make) and describe how understanding the Euler characteristic and neural network architecture would change your planning process.

20. Design, in words, a crochet project that combines at least two different neural network architectural principles (e.g., feedforward rows with skip connections, recurrent rounds with a bottleneck). Describe the piece, the stitch plan, and how the architecture of the fabric mirrors the architecture of the network.
