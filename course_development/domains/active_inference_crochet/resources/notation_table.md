# Notation Table: Active Inference: Crochet Circles

> Standard crochet abbreviations and their Active Inference interpretations.
> Level: Fiber artists, crafters, crochet circle participants, and the curious

## Stitch Abbreviations & Active Inference Mappings

| Abbreviation | Crochet Meaning | Active Inference Interpretation | First Introduced |
| --- | --- | --- | --- |
| ch | Chain — a loop pulled through the previous loop | The foundational prior; initial state commitment that constrains all subsequent inference | Course 1, M1 |
| sl st | Slip stitch — a minimal stitch used for joining or moving position | Zero-cost transition action; repositioning without generating new fabric (state change without prediction update) | Course 1, M1 |
| sc | Single crochet — short, dense stitch | High-precision, low-variance action; produces tight fabric with minimal uncertainty per stitch | Course 1, M5 |
| hdc | Half double crochet — medium-height stitch | Intermediate precision action; balances stitch density with working speed | Course 1, M5 |
| dc | Double crochet — tall stitch with one yarn-over | Lower-precision, higher-coverage action; each stitch spans more vertical space, trading density for speed | Course 1, M5 |
| tr | Treble crochet — very tall stitch with two yarn-overs | Extended reach action with compounded sub-predictions (each yarn-over is a sequential prediction step) | Course 2, M5 |
| yo | Yarn over — wrap yarn around hook | The atomic prediction-action unit; the smallest motor primitive from which all stitches are composed | Course 1, M1 |
| inc | Increase — two or more stitches in one | Controlled state-space expansion; the generative model predicts widening | Course 1, M5 |
| dec | Decrease — combine stitches into one | Controlled state-space contraction; the generative model predicts narrowing | Course 1, M5 |
| sk | Skip — pass over a stitch without working into it | Intentional null action; the model predicts a gap and the crocheter confirms it by not acting | Course 3, M5 |
| sp | Space — the gap created by a chain or skip | Predicted absence; a deliberate void that is part of the pattern's structure (as in lace or filet crochet) | Course 3, M3 |
| rep | Repeat — execute the enclosed sequence again | Hierarchical model iteration; compress a sequence into a reusable prediction chunk | Course 3, M1 |
| RS | Right side — the public-facing surface of the fabric | The observable output; the external states visible to others | Course 1, M3 |
| WS | Wrong side — the private, interior surface | The hidden internal states; the back side of the Markov blanket | Course 1, M3 |
| BLO | Back loop only — work into the rear strand of the stitch | Selective sensory sampling; attending to only one component of the available sensory evidence | Course 2, M3 |
| FLO | Front loop only — work into the front strand | Alternative selective sampling; choosing a different sensory channel from the same stitch | Course 2, M3 |
| pm | Place marker — insert a stitch marker | Epistemic action; offload state information to the environment | Course 1, M4 |
| tch | Turning chain — chains at row start for height | Transition prediction; accounting for the structural shift between rows | Course 1, M1 |
| rnd | Round — one complete circuit in circular work | A full prediction-action-observation cycle in the round | Course 3, M1 |
| FO | Finished object — completed project | Converged inference; the point where the generative model and the realized fabric are reconciled | Course 1, M8 |
| WIP | Work in progress — unfinished project | Ongoing inference; the partially realized object that embodies accumulated predictions | Course 1, M8 |
| UFO | Unfinished object — abandoned WIP | Suspended inference; a generative model that was abandoned before convergence | Course 4, M8 |

## Topology & Network Notation (Course 5: Loop & Lattice)

| Abbreviation | Crochet Meaning | Topology / Neural Network Interpretation | First Introduced |
| --- | --- | --- | --- |
| mr | Magic ring — adjustable starting loop for circular work | Topological origin point; a singularity from which the surface emanates, with deferred commitment until surrounding structure constrains it | Course 5, M1 |
| 2-in-1 | Two stitches worked into one stitch below (increase) | Negative curvature operator; locally expands the surface area, producing hyperbolic geometry when repeated | Course 5, M5 |
| sc2tog | Single crochet two together (decrease) | Positive curvature operator; locally contracts the surface area, producing spherical geometry when repeated | Course 5, M5 |
| FPdc | Front post double crochet — worked around the post of the stitch below | Skip connection; bypasses the normal layer-to-layer connectivity to create a direct link to a non-adjacent layer, analogous to ResNet skip connections | Course 5, M4 |
| BPdc | Back post double crochet — worked around the back of the post | Reverse skip connection; accesses the hidden (back) side of a previous layer's node | Course 5, M4 |
| mesh | Open mesh pattern — chain spaces and stitches forming a grid | Sparse network architecture; a fabric where not all possible connections are made, analogous to a neural network with dropout or sparse connectivity | Course 5, M7 |
| join | Slip stitch or chain to connect two points in the fabric | Topological surgery; changes the connectivity and potentially the genus of the surface (e.g., joining a strip into a tube) | Course 5, M1 |
| spiral | Working in a continuous spiral without joining rounds | Recurrent architecture; information flows continuously without discrete layer boundaries, analogous to recurrent neural networks | Course 5, M8 |

## Pattern Notation Conventions

| Symbol | Meaning | Active Inference Reading |
| --- | --- | --- |
| `*...*` or `[...]` | Repeat the enclosed sequence | Hierarchical chunk — iterate the sub-model |
| `( )` | Work all enclosed stitches into the same stitch or space | Convergent action — multiple predictions resolved at a single state |
| `,` | Separator between instructions | Sequential prediction boundary |
| `—` or `to end` | Continue the pattern to the end of the row | Extend the model's predictions to fill remaining state space |
| Row/Round number | Position in the vertical sequence | Temporal index in the inference process |

## Navigation

- [Glossary](./glossary.md)
- [References](./references.md)
- [Curriculum Overview](../OVERVIEW.md)
