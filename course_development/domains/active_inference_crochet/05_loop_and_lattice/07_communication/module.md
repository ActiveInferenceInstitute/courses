# Module 07: Signals Through the Mesh — Information Flow in Fabric and Networks

## Learning Objectives

1. Identify how information flows through crocheted fabric — mechanically, visually, and structurally — and relate these flows to signal propagation in neural networks.
2. Recognize that open mesh crochet patterns (filet crochet, chain spaces, lace) are literal communication networks whose connectivity determines which signals reach where.
3. Map stitch notation systems (written patterns, symbol charts, stitch diagrams) onto the concept of communication protocols, and understand crochet charts as graph representations of stitch networks.

## Introduction

Hold a piece of mesh crochet by one corner and give it a gentle tug. Watch what happens. The pull does not stay at the corner. It travels — through the chain spaces, along the double crochet posts, across the grid of the mesh — rippling outward like a message sent through a network. Some paths carry the tension directly. Others absorb it. The mesh filters, redirects, and transforms the force as it passes through.

You have just watched a signal propagate through a network.

This is not a metaphor. A crocheted mesh is a physical network of interconnected paths, and when force, color, or structural information enters at one point, it propagates through that network according to the connectivity pattern of the stitches. The mesh determines which signals reach where, how strongly, and how quickly — just as the architecture of a neural network determines how input signals are transformed into outputs.

In this module, we explore crochet as a communication system at three levels: the physical propagation of signals through fabric, the visual propagation of color and pattern through stitch placement, and the symbolic propagation of knowledge through pattern notation. At every level, the topology of the network shapes the message.

## Key Concepts

### 1. The Mesh as a Communication Network

Open mesh crochet — filet crochet, lace patterns, any fabric with deliberate holes and spaces — is one of the most visually obvious network structures in all of textile arts. A filet crochet grid consists of solid blocks (typically clusters of double crochets) and open spaces (chain stitches bridging between posts). Lay it flat and what you see is a grid: nodes connected by edges, some paths open and some paths filled.

In graph theory, this is a **lattice graph** — a regular network where nodes are arranged in rows and columns, each connected to its neighbors. The solid blocks are nodes with strong, direct connections. The chain spaces are nodes connected by longer, more flexible links. The entire fabric is a communication network, and its structure determines how information flows.

Consider what "information" means in a crocheted mesh. There are several kinds:

**Mechanical information.** When you stretch the fabric, the force transmits through the network. A solid block of double crochets transmits force rigidly — pull on one side and the other side moves almost immediately. A chain space transmits force more loosely — it stretches, absorbs, and dampens the signal before passing it along. A mesh with many chain spaces is a **lossy network**: signals attenuate as they travel. A solid fabric with no holes is a **low-loss network**: signals travel with minimal attenuation.

This has a direct parallel in neural networks. In a neural network, each connection between neurons has a **weight** — a number that determines how strongly a signal from one neuron affects the next. A high weight means the signal passes through strongly (like a solid stitch connection). A low weight means the signal is attenuated (like a chain space). A weight of zero means no connection at all (like a gap in the fabric with no stitch bridging it). The pattern of weights across the entire network determines how input signals are transformed into outputs — just as the pattern of solid blocks and open spaces determines how a tug on one corner of a filet crochet piece transforms as it reaches the opposite corner.

**Structural information.** Every stitch "knows" where it sits in the fabric because of its connections. A double crochet worked into the top of a chain-3 space knows it is bridging a gap. A double crochet worked into the top of another double crochet knows it is part of a solid block. This structural information — encoded in the physical connections between stitches — propagates through the fabric. A missed stitch or an extra stitch creates a local distortion that propagates outward, affecting the alignment of stitches in subsequent rows. Crocheters know this intimately: one mistake in Row 5 can ripple forward into Row 10 and beyond.

In neural network terms, this is like an **error signal** propagating through the network. In backpropagation — the algorithm used to train neural networks — error signals flow backward through the network from output to input, adjusting the weights along the way. In crochet, a structural error propagates forward through the rows, and the crocheter must detect it and adjust (frogging back, adding compensating stitches) to prevent it from distorting the entire piece.

**Visual information.** Color changes in crochet create visual signals that flow along paths determined by stitch placement. In a filet crochet grid, if you change yarn color for specific blocks, the color creates a pattern — a picture, a word, a design — that is "encoded" in the network. The mesh is the medium. The color is the message. And the stitch connectivity determines where the color appears.

This is strikingly similar to how neural networks process visual information. In a **convolutional neural network** (the kind used for image recognition), the network applies filters that detect patterns — edges, corners, textures — at specific locations in the image. A filet crochet chart is essentially a filter applied to a grid: fill this block, leave that one open. The result is a visual pattern that emerges from the structure of the network itself.

### 2. Signal Propagation in Crochet

Let us trace a signal through a crocheted fabric in detail, because the mechanics of propagation reveal the deep parallel with neural network computation.

**Forward propagation: from foundation to final row.** When you crochet a piece from bottom to top, each row builds on the one before it. The foundation chain sets the initial conditions — the number of stitches, the width of the fabric, the starting point. Row 1 transforms those initial conditions by working stitches into the chain. Row 2 transforms the output of Row 1. And so on, row after row, each layer receiving the output of the previous layer and transforming it.

This is **forward propagation** in a neural network. An input enters the first layer, gets transformed by the weights and activation functions of that layer, and passes to the next layer. Each layer applies its own transformation. The final layer produces the output. In crochet, the input is the foundation chain, the "weights" are the stitch types and placements specified by the pattern, and the output is the finished fabric.

The parallel becomes vivid when you think about what each "layer" (row) does to the signal. A row of single crochet is a simple, conservative transformation — it preserves width and adds minimal height. A row of double crochets is a taller, more open transformation. A row that combines increases, decreases, and chain spaces is a complex, non-linear transformation that can change the width, texture, and connectivity of the fabric.

In neural network language, each stitch type is an **activation function** — a mathematical operation that transforms the input in a specific way. Single crochet is like a **ReLU function** (simple, direct, passes the signal through with minimal modification). Double crochet is like a **sigmoid function** (smoother, taller, more gradual). A shell stitch (5 dc in one stitch) is like a **softmax function** — it fans the signal from one node into many, distributing it across a local neighborhood.

**Tension as a signal.** Every crocheter knows that tension is a message that travels through the fabric. Pull the working yarn and the tension propagates backward through the current row, through the live loops on the hook, and into the completed fabric. If your tension changes — tighter after a break, looser when you are relaxed — that change is recorded in the fabric as a visible stripe of slightly different gauge. The fabric is a record of your tension signals over time, like a seismograph recording vibrations.

In Active Inference terms, tension is a **sensory signal** that the crocheter monitors to maintain their generative model. The expected tension (based on your gauge swatch and the pattern requirements) is compared against the felt tension in real time. A mismatch — too tight, too loose — generates **prediction error**, and the crocheter adjusts their hand position and yarn feed to minimize that error. The fabric is the accumulated record of this ongoing signal-processing loop.

**Error propagation.** A dropped stitch, a missed increase, or a wrong stitch type creates a distortion that propagates forward through subsequent rows. In a mesh pattern, a missed chain space in Row 3 means the double crochet in Row 4 has no chain space to bridge, causing a misalignment that shifts every subsequent block in the row. The error does not stay local. It propagates through the network.

This is analogous to how errors propagate through neural networks — and, more importantly, to how **backpropagation** works. In backpropagation, the network calculates the error at the output (the difference between what the network produced and what was expected), then sends that error signal backward through the layers, adjusting the weights at each layer to reduce the error. When a crocheter notices a mistake, they perform their own version of backpropagation: they trace the error backward through the rows to find its origin, then frog (unravel) back to that point and re-crochet with the correct stitches. The crocheter is the backpropagation algorithm, and the frogging is the weight adjustment.

### 3. Stitch Notation as Communication Protocol

Step back from the physical fabric for a moment and think about how crochet knowledge moves between people. A designer conceives a pattern, works it out in yarn, then translates it into notation — written instructions, a chart, a diagram — that another crocheter can follow to reproduce the fabric. This is a communication system, and it has all the formal properties of a **communication protocol**.

A communication protocol is a set of agreed-upon rules that allow two parties to exchange information reliably. It includes a **syntax** (the format of the messages), a **semantics** (the meaning of the symbols), and a **channel** (the medium through which messages travel).

Crochet pattern notation is exactly this:

**Syntax.** The format is standardized: abbreviations (sc, dc, ch, sl st, sk, rep), parentheses for groups, asterisks for repeats, brackets for alternatives, stitch counts at the end of rows. "Row 1: Sc in 2nd ch from hook, *ch 1, sk 1, sc in next ch*, rep * to * across. (7 sc, 7 ch-1 spaces)" — this is a syntactically well-formed message in the crochet protocol.

**Semantics.** Each abbreviation maps to a specific physical action and a predicted outcome. "Dc" means: yarn over, insert hook, yarn over, pull through, yarn over, pull through two, yarn over, pull through two. The symbol on a chart — a vertical bar with a short crossbar — means the same thing. The semantics are shared between writer and reader through the conventions of the crochet community.

**Channel.** The message can travel through a printed book, a PDF, a website, a handwritten note, or a chart image. The channel is the medium of transmission. Each channel has its own strengths and limitations — a chart conveys spatial structure better than text, but text conveys the action sequence more precisely.

Now here is the beautiful part: **the topology of the notation system mirrors the topology of the fabric it describes.**

A written pattern is sequential — one instruction after another, like a linked list. It mirrors the sequential nature of crochet itself, where you work one stitch after another in a row, one row after another from bottom to top.

A stitch chart is a graph — nodes (stitch symbols) connected by their spatial positions in a grid. It mirrors the network topology of the fabric itself. A filet crochet chart is literally a graph drawing of the filet crochet mesh. The chart IS the network, drawn on paper instead of built in yarn.

This means that when a designer draws a chart, they are not merely describing the fabric. They are drawing a **network diagram** — a map of the signal paths that the fabric will contain. And when a crocheter reads a chart, they are reading a network diagram and translating it into a physical network made of yarn.

In Active Inference, this is communication of **generative model structure** through an encoded representation. The designer's generative model (their understanding of how the stitches connect and what the fabric will look like) is encoded into the chart, transmitted through the channel (the printed page or screen), and decoded by the crocheter into their own generative model. The chart is the shared language. The protocol ensures that the same chart produces the same fabric in different hands — or at least, it does when the protocol is followed correctly.

### 4. Applications

**Filet crochet as a pixel-based communication system.** Filet crochet is one of the oldest forms of message-encoding in fabric. Each block is either solid or open — a binary choice, like a pixel that is either on or off. By arranging solid and open blocks in a grid, crocheters have encoded words, pictures, names, and decorative motifs in mesh fabric for centuries. This is a **pixel-based communication system** where the mesh is the display and the solid blocks are the illuminated pixels. The resolution is determined by the gauge (stitches per inch), and the bandwidth is determined by the size of the grid.

The parallel to digital imaging is exact. A filet crochet chart is a bitmap — a grid of binary values. A 40-block-wide filet crochet piece with 60 rows has 2,400 pixels, each either solid or open. That is 2,400 bits of visual information encoded in yarn. The mesh is not just a carrier of aesthetic beauty. It is an information-bearing medium, and the information is encoded in the topology of the network.

**Color pooling as emergent signal patterns.** When you crochet with variegated yarn (yarn that changes color at regular intervals), the color transitions interact with the stitch pattern to produce visual effects that neither the yarn nor the pattern would create alone. This is **color pooling** — the emergence of visual patterns (argyle diamonds, zigzags, pooling effects) from the interaction of two independent signals: the color sequence in the yarn and the stitch placement in the pattern.

Color pooling is an emergent phenomenon. No one designed the argyle pattern into the yarn or the stitch pattern separately. It arises from the interaction of the two. In neural network terms, this is like the **emergent features** that arise in deep networks — patterns that no single layer was designed to detect but that emerge from the interaction of multiple layers processing the same signal. The crocheter who masters color pooling has learned to predict and control an emergent property of the signal flow through their fabric network.

**Stitch charts as circuit diagrams.** An electronic circuit diagram shows components (resistors, capacitors, transistors) connected by wires, with signals flowing through the circuit along paths determined by the connections. A crochet stitch chart shows stitches (sc, dc, ch, shell) connected by their physical relationships, with structural and visual signals flowing through the fabric along paths determined by the stitch connections. The formal similarity is not accidental. Both are **network diagrams** that describe how signals propagate through a system of connected components. A crocheter reading a chart and an electrical engineer reading a schematic are performing the same cognitive task: understanding a network and predicting what signals will emerge from it.

## Conclusion

Crochet is a communication technology. The mesh is a physical network that carries mechanical, structural, and visual signals. The pattern notation is a communication protocol that transmits network structure from designer to crocheter. The stitch chart is a graph diagram of the fabric network. And the act of crocheting a mesh pattern is the act of building a signal-processing network, node by node, edge by edge, with nothing but a hook and yarn.

In Active Inference, communication is the sharing of generative models between agents. When a designer encodes a pattern in notation and a crocheter decodes it into fabric, they are sharing a generative model of a network. The fidelity of this communication depends on the protocol (is the notation clear?), the channel (is the chart legible?), and the shared priors (do both parties use the same abbreviation conventions?). When the communication succeeds, the fabric that emerges is a physical instantiation of the shared model — a network you can hold, stretch, and trace with your finger.

In the final module, we bring everything together: planning. How do you design a topologically complex crochet project from scratch? How do you translate a neural network architecture into a crochet chart? How do you plan for the geometry of the surface you are about to create? Bring your graph paper and your hook — we are designing architectures in yarn.

## Key Terms

| Term | Crochet Meaning | Active Inference / Network Meaning |
| --- | --- | --- |
| Mesh | Open fabric with deliberate holes (chain spaces between posts) | A network or lattice graph with varying connection strengths |
| Signal propagation | The transmission of force, color, or structural information through fabric | The forward flow of activations through a neural network |
| Forward propagation | Building fabric row by row, each row transforming the last | Input signals flowing through network layers to produce output |
| Backpropagation | Frogging back to the source of an error and re-crocheting | Error signals flowing backward through the network to adjust weights |
| Connection weight | The strength of a stitch connection (solid block vs. chain space) | The numerical weight on a connection between neurons |
| Filet crochet | Grid-based mesh with solid and open blocks forming pictures | A binary pixel grid — a bitmap encoded in a network |
| Communication protocol | The system of abbreviations, charts, and conventions for sharing patterns | An agreed-upon set of rules for encoding and decoding messages |
| Stitch chart | A visual diagram of stitch placement using standard symbols | A graph representation of the fabric network — a circuit diagram |
| Color pooling | Emergent visual patterns from variegated yarn and stitch interaction | Emergent features arising from the interaction of signal and network structure |
| Activation function | The type of stitch used (sc, dc, shell) that transforms the signal | A mathematical function applied at each neuron to transform input |
| Error propagation | A mistake in one row affecting alignment in subsequent rows | Error signals flowing through a network, requiring correction |
| Lossy network | Mesh with many chain spaces that absorb and dampen force signals | A network where signal strength attenuates through weak connections |
