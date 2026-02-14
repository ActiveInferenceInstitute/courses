# Module 08: Designing Architectures in Yarn — Planning Topologically Complex Projects

## Learning Objectives

1. Plan topologically complex crochet projects by choosing the appropriate surface topology (flat, spherical, toroidal, hyperbolic) before beginning to stitch, and understand the architectural consequences of these choices.
2. Use the Euler characteristic (V - E + F) as a planning tool to predict shaping requirements for different crochet topologies — from flat blankets to toroidal cowls to hyperbolic coral forms.
3. Translate neural network architectures (feedforward, recurrent, skip-connection) into concrete crochet design specifications, creating a design language that bridges computation and craft.

## Introduction

Every large crochet project begins the same way: not with a hook, but with a plan. What are you making? A blanket? A hat? A stuffed animal? A shawl? Each of these is a different kind of surface, with different topology, different geometry, and different structural requirements. The blanket is flat. The hat is a truncated sphere. The stuffed animal is a collection of closed surfaces sewn together. The shawl is a surface with a complex boundary — curved edges, pointed ends, perhaps scalloped trim.

A crocheter who starts without understanding the topology of their target surface is like a neural network architect who starts coding without deciding whether the network should be feedforward, recurrent, or convolutional. The architecture comes first. The stitching comes second.

In this final module of Loop & Lattice, we bring together everything we have learned about topology, neural networks, and Active Inference to tackle the most challenging question in crochet: how do you design something complex from scratch? How do you plan the topology of a surface, translate that plan into a stitch chart, and execute it with confidence that the geometry will work out? The answer, it turns out, involves the same principles that guide the design of neural network architectures — and the same Active Inference framework that tells us how to plan under uncertainty.

## Key Concepts

### 1. Architecture Before Stitching

A neural network designer does not start by writing code. They start by choosing an **architecture** — the high-level structure that determines how information flows through the network. How many layers? How many neurons per layer? What kind of connections? Feedforward or recurrent? Convolutional or fully connected? These are not implementation details. They are fundamental decisions that determine what the network can learn and what it cannot.

Crochet design works the same way. Before you pick up the hook, you are making architectural decisions with topological consequences:

**Flat vs. 3D.** A flat piece (blanket, scarf, dishcloth) is a two-dimensional surface with zero Gaussian curvature and an open boundary. A three-dimensional piece (hat, amigurumi, bag) is a surface with varying curvature and possibly a closed boundary. The choice between flat and 3D is a fundamental topological decision. It determines whether you will need increases, decreases, shaping, and joining — or whether you can simply crochet back and forth in rows.

**Open mesh vs. solid fabric.** As we explored in the Communication module, mesh and solid fabric have different network properties. Mesh is flexible, drapey, and transmits signals loosely. Solid fabric is stable, structured, and transmits signals directly. The choice between mesh and solid is a connectivity decision: how densely connected should the network be?

**Worked in rows vs. worked in the round.** This is the feedforward vs. recurrent decision. Rows are feedforward — information flows in one direction, layer by layer, no loops. Rounds are recurrent — the end of each layer connects back to the beginning, creating a loop in the graph. A scarf worked in rows has a fundamentally different topology (and a fundamentally different kind of structural integrity) than a hat worked in the round.

**Joined as you go vs. seamed.** When you crochet separate pieces and sew them together, you are building a modular architecture — separate components assembled into a whole, like separate neural network modules connected by a final layer. When you work a piece continuously, joining as you go, you are building a monolithic architecture — one continuous network from input to output.

Each of these decisions constrains what follows. Once you choose to work in the round, you are committed to a recurrent topology. Once you choose flat mesh, you are committed to a feedforward lattice. The architecture shapes the possibilities — just as choosing a convolutional neural network architecture constrains you to translation-invariant feature detection, while choosing a transformer architecture opens up attention-based long-range connections.

In Active Inference, planning is the process of evaluating possible actions (or sequences of actions) by calculating their **expected free energy** — a measure that balances the expected reward of an outcome against the expected uncertainty. A crocheter choosing between a flat blanket and a sculptural amigurumi is evaluating expected free energy: the blanket is lower uncertainty (flat topology is predictable) but perhaps lower reward (you have made many blankets before). The amigurumi is higher uncertainty (spherical topology requires careful shaping) but higher reward (a finished stuffed animal is delightful). The optimal plan depends on the crocheter's skill level, available time, and tolerance for uncertainty.

### 2. Planning with the Euler Characteristic

Here is where topology gives us a concrete planning tool. The **Euler characteristic** is a number that summarizes the topology of a surface:

**V - E + F = chi**

where V is the number of vertices, E is the number of edges, and F is the number of faces. For our purposes, the Euler characteristic tells you what kind of surface you are building and, crucially, how much total curvature you need to build into it.

**For a flat disc (or any flat surface with boundary): chi = 1.** When you crochet a flat circle — magic ring, increase 6 per round for single crochet — the total curvature over the surface sums to 2 pi (which corresponds to chi = 1 via the Gauss-Bonnet theorem for surfaces with boundary). The key insight for planning: to keep the surface flat, you must add exactly the right number of increases per round. For single crochet, that is 6 per round. For half double crochet, it is 8. For double crochet, it is 12. These numbers are not arbitrary — they are determined by the stitch height and the geometry of the surface.

**For a sphere: chi = 2.** An amigurumi ball starts with increases (positive curvature, like the top of the sphere), reaches a maximum circumference at the equator, then decreases (closing the surface back toward positive curvature). The total curvature over the entire closed surface sums to 4 pi. For planning, this means: whatever increases you add in the first half, you must remove in the second half. The increase rate and decrease rate must balance. If you increase 6 per round for 8 rounds (48 stitches at the equator), you must decrease 6 per round for 8 rounds to close the sphere. The Euler characteristic tells you the budget.

**For a torus (donut shape): chi = 0.** This is where it gets interesting. A torus has zero Euler characteristic, which means the total Gaussian curvature over the surface is zero. A crocheter planning a toroidal cowl (a tube joined end to end) must ensure that the positive curvature on the outer rim is exactly canceled by the negative curvature on the inner rim. In practice, this means the outside of the torus needs more stitches per round than the inside — which is why toroidal cowls are shaped with short rows or strategic increases on the outside edge.

**For a hyperbolic surface: chi is negative or the surface has boundary with excess curvature.** The coral reef crochet pieces that Daina Taimina and the Institute For Figuring have made famous are surfaces of constant negative curvature. Planning a hyperbolic piece means deliberately adding more increases than the flat-surface formula requires — making the fabric ruffle and fold. The degree of ruffling is directly proportional to how much the increase rate exceeds the flat-surface rate.

**The planning principle:** Before you begin a topologically complex project, determine the Euler characteristic of your target surface. This tells you the total curvature budget you must distribute across the piece. Then plan your increase and decrease schedule to match that budget. The Euler characteristic is your architectural blueprint — it constrains the shaping before you work a single stitch.

### 3. From Neural Network Blueprints to Crochet Charts

Now let us build the bridge between network architecture and crochet design in concrete terms. Imagine you wanted to "crochet" a neural network — to create a physical fabric whose structure mirrors the architecture of a specific type of network. What would that look like?

**Feedforward network as a scarf or blanket (worked in rows).** The simplest architecture: each layer feeds into the next, no loops, no skip connections. The foundation chain is the input layer. Each row is a hidden layer. The final row is the output layer. If the network has the same number of neurons in every layer (same width), the fabric has the same stitch count in every row — a simple rectangle. If the network narrows toward the output (a bottleneck architecture), the fabric decreases — a tapered scarf. If the network widens then narrows (an autoencoder architecture), the fabric increases then decreases — a diamond or leaf shape.

**Recurrent network as a hat or cowl (worked in the round).** A recurrent network has feedback loops — the output of a layer feeds back into the same layer or an earlier one. Working in the round is the crochet equivalent: the end of each round connects to the beginning, creating a continuous loop. A simple crocheted tube (cowl) is a single-layer recurrent network. A hat with a shaped crown is a recurrent network with decreasing layer width — the rounds get smaller as you approach the top, like a recurrent network with a shrinking hidden state.

**Convolutional network as a motif-based design.** A convolutional neural network applies the same small filter repeatedly across the input. Crochet pattern repeats are the exact same operation: a motif (the filter) is repeated across the row or round. A granny square blanket is a spatially repeated convolution. An intricate lace pattern with a 10-stitch repeat applied 20 times across a row is a convolution with a kernel size of 10 and 20 applications.

**Skip connections (ResNet) as surface crochet or post stitches.** A residual network (ResNet) uses skip connections that allow information to bypass one or more layers. In crochet, front post and back post stitches reach around the post of a stitch in a previous row, creating a connection that bypasses the intervening row. Spike stitches (inserting the hook one or more rows below the current working row) create even longer skip connections. Surface crochet — working slip stitches or chains on the face of the completed fabric — creates explicit skip connections between non-adjacent layers.

**Dropout as deliberately skipped stitches.** Dropout is a regularization technique where random neurons are temporarily disabled during training to prevent the network from relying too heavily on any single path. In crochet, deliberately skipping stitches in a mesh pattern (chain spaces that bridge gaps) has a similar structural effect: it prevents the fabric from being too rigid and forces the surrounding stitches to compensate. The mesh pattern IS dropout — random-looking gaps that make the overall network more flexible and resilient.

**Attention mechanisms as color changes or texture highlights.** In transformer networks, attention mechanisms allow the network to focus on specific parts of the input. In crochet, color changes, texture shifts, and stitch pattern variations draw the eye — and the structural emphasis — to specific parts of the fabric. A bobble stitch in a field of single crochet is an attention head: it highlights a specific location in the fabric by adding extra processing (extra wraps, extra loops) at that node.

This is not just an intellectual exercise. This translation between network architecture and crochet design gives you a powerful planning tool. If you understand what a feedforward network does, you understand what working in rows does. If you understand skip connections, you understand post stitches. The two design languages illuminate each other, and fluency in both makes you a better designer in each.

### 4. Applications

**Planning a hyperbolic coral reef piece.** The Crochet Coral Reef project requires pieces with constant negative curvature — ruffled, branching, coral-like forms. Planning such a piece starts with the Euler characteristic. Since the surface has negative curvature everywhere, you need to increase at a rate that exceeds the flat-surface formula. For single crochet, flat requires 6 increases per round. Hyperbolic might use 8, 10, or 12 increases per round — the more excess, the more extreme the ruffling. The planning process is: choose an increase rate, predict the degree of ruffling (more increases = more ruffles = more negative curvature), and crochet a test swatch to calibrate your prediction. This is Active Inference in action: form a hypothesis (generative model) about the curvature, test it against the observed fabric, and update the model.

**Designing a Klein bottle.** A Klein bottle is a surface with no inside or outside — a closed, non-orientable surface that cannot be embedded in three-dimensional space without self-intersection. Crocheting one requires careful planning. You begin with a tube (work in the round), then at one end, you narrow the tube, bend it back on itself, and pass it through the wall of the outer tube to join it to the other end. The topological challenge is that the "passing through" step requires you to break the fabric, crochet the inner tube through the hole, and then close the break — or to use a construction that mimics the self-intersection. The Euler characteristic of a Klein bottle is 0, same as a torus, but its non-orientability means the crocheter must plan for a twist that the torus does not have. Planning a Klein bottle is one of the most demanding topological planning exercises in crochet — and one of the most satisfying.

**Creating a crochet representation of a neural network.** Suppose you want to crochet a physical model of a 3-layer feedforward neural network with 8 input neurons, 4 hidden neurons, and 2 output neurons. Here is a planning approach:

- **Input layer (foundation):** Chain 24 (3 chains per "neuron" x 8 neurons). Work one row of dc to establish the input nodes.
- **Hidden layer with narrowing:** Work a row that decreases from 8 groups to 4 groups. Use dc2tog (double crochet two together) to merge pairs of nodes. This represents the connections from input to hidden layer, with each hidden neuron receiving input from 2 input neurons.
- **Output layer with further narrowing:** Work another row that decreases from 4 groups to 2 groups.
- **Connections (weights):** Use surface crochet in different colors to trace the connections between layers. Thick surface chains in bright colors for strong connections. Thin surface slip stitches in muted colors for weak connections.

The finished piece is a physical, textile model of a neural network — one you can hold, point to, and use to explain how information flows from input to output.

**Planning under uncertainty: the Active Inference approach.** Every crochet project involves uncertainty. Will the yarn behave as expected? Will your gauge match the pattern? Will the shaping produce the topology you intend? Active Inference provides a framework for planning under this uncertainty.

In Active Inference, planning is the evaluation of possible action sequences (policies) by their **expected free energy**. The expected free energy of a policy has two components: **pragmatic value** (will this policy achieve my goal?) and **epistemic value** (will this policy reduce my uncertainty?).

When a crocheter plans a complex project, they evaluate policies in exactly these terms. Making a gauge swatch has high epistemic value — it reduces uncertainty about stitch dimensions. Choosing a familiar yarn has high pragmatic value — it increases the likelihood of a predictable result. Starting with the most uncertain part of the project (the shaped crown of a hat, the complex increase section of a hyperbolic piece) has high epistemic value — if the hardest part fails, you discover early, before investing hours in the easy parts.

Experienced crocheters often plan in a sequence that minimizes expected free energy at each step: swatch first (reduce gauge uncertainty), then work the most uncertain section (reduce topology uncertainty), then complete the straightforward sections (execute with confidence). This is optimal planning under the Active Inference framework — and it is something that skilled crafters do intuitively, without ever writing down an equation.

## Conclusion

We have reached the end of Loop & Lattice, and we have come full circle — or perhaps full torus, since our ending connects back to our beginning. In the Systems module, we discovered that crochet creates topological surfaces. In the Agents module, we met the crocheter as a neural architect. Through Perception, Cognition, Action, Learning, and Communication, we traced how the crocheter senses, thinks about, shapes, trains, and shares their understanding of these surfaces and networks. And now, in Planning, we have arrived at the master skill: designing topologically complex projects from scratch, with the Euler characteristic as our guide, neural network architectures as our inspiration, and Active Inference as our framework for navigating uncertainty.

The next time you sit down with hook and yarn, planning your next project, know that you are performing the same operations as a neural network architect sitting down with a whiteboard. You are choosing an architecture. You are planning a topology. You are evaluating expected free energy — balancing ambition against uncertainty, novelty against familiarity, exploration against exploitation.

The hook is your stylus. The yarn is your medium. The fabric is your network, built node by node, edge by edge, layer by layer. And the mathematics — the Euler characteristic, the Gaussian curvature, the graph structure, the Markov blanket — has been there all along, in your hands, waiting for you to notice.

Welcome to the lattice. Now go design something extraordinary.

## Key Terms

| Term | Crochet Meaning | Active Inference / Topology Meaning |
| --- | --- | --- |
| Architecture | The high-level structure of a project: flat vs. 3D, rows vs. rounds, mesh vs. solid | The structural design of a neural network: layers, connections, information flow |
| Euler characteristic (chi) | The topological "budget" for curvature: determines shaping requirements for flat (chi=1), spherical (chi=2), toroidal (chi=0) forms | Topological invariant V - E + F that classifies surfaces |
| Feedforward (rows) | Fabric worked in rows, each building on the last, no loops | Neural network where information flows input to output with no recurrence |
| Recurrent (rounds) | Fabric worked in the round, each round connecting end to beginning | Neural network with feedback loops |
| Skip connection (post stitch) | Front post, back post, or spike stitch reaching past the previous row | Residual connection in a ResNet that bypasses intermediate layers |
| Convolution (pattern repeat) | A stitch motif repeated across a row or round | A filter applied repeatedly across the input in a convolutional neural network |
| Dropout (chain spaces) | Deliberately skipped stitches that create flexibility in the mesh | Random deactivation of neurons during training for regularization |
| Bottleneck (decrease section) | Rows with decreases that narrow the fabric | Network architecture that compresses representation into fewer neurons |
| Expected free energy | The crocheter's evaluation of a project: will it succeed? will I learn? | The quantity minimized in Active Inference planning: balances pragmatic and epistemic value |
| Gauge swatch | A test piece crocheted before the main project to calibrate expectations | An epistemic action — reducing uncertainty before committing to a policy |
| Klein bottle | A non-orientable surface crocheted by joining a tube back through itself | A closed surface with Euler characteristic 0 and no well-defined inside or outside |
| Curvature budget | The total shaping (increases/decreases) required by the target topology | The integral of Gaussian curvature over the surface, constrained by the Euler characteristic via the Gauss-Bonnet theorem |
