# Lab: The Hook-Yarn Boundary

## Objective

Crochet a small swatch and physically identify the internal states, external states, and Markov blanket of your crochet system in real time.

## Materials

* Worsted weight yarn (any color), approximately 20 yards
* Crochet hook, size H/8 (5.0mm)
* Stitch marker (or a scrap of contrasting yarn)
* Pen and paper (or sticky notes) for labeling
* Scissors

## Prerequisites

* Ability to make a foundation chain and single crochet stitches (or willingness to learn during the lab)
* Reading of Module 01: Systems lecture (module.md)

## Steps

### Part 1: Setting Up the System (10 minutes)

1. **Before you begin crocheting**, lay out your materials on the table: yarn, hook, scissors, stitch marker. On a piece of paper, write three labels: "INTERNAL," "EXTERNAL," and "BLANKET."
2. Place the labels near the corresponding materials. At this point, everything is external — no system exists yet. Note this on your paper: "Before the first stitch, there are no internal states."
3. Make a **slip knot** on your hook. Pause. You now have a single live loop. Ask yourself: has a system come into existence? Where is the Markov blanket?
4. Write down your answer before continuing.

### Part 2: Building Internal States (15 minutes)

5. Chain 15. As you chain, notice how each new chain stitch transitions from external state (unworked yarn) to internal state (completed chain) through the blanket (your hook and the live loop).
6. Turn your work. Single crochet in the second chain from the hook and in each chain across (14 sc total).
7. Pause at the end of the row. Place a sticky note labeled "INTERNAL" on the completed row. Place "EXTERNAL" on the ball of yarn. Place "BLANKET" on the hook and live loop area.
8. Crochet 4 more rows of single crochet (5 rows total). After each row, pause briefly and notice: the internal region has grown, the external region (yarn ball) has shrunk, and the blanket has moved.

### Part 3: Observing the Boundary (10 minutes)

9. Hold your swatch up and look at the **working edge** — the row you are currently on. This is the Markov blanket. Notice:
   - The live loop on your hook (active state — you can act through it)
   - The top loops of the previous row (sensory state — they tell you where to insert your hook)
   - The yarn coming from the skein (external input crossing into the blanket)
10. Gently tug the working yarn. Feel how the tension travels from the external state (skein) through the blanket (your fingers and hook) to affect the internal states (the fabric tightens or loosens). This is sensory information crossing the Markov blanket.
11. Now deliberately insert your hook into the next stitch but do not yarn over yet. You are poised at the boundary. The hook tip is inside the fabric (touching internal states) while the working yarn is still external. The moment you yarn over and pull through, you convert external yarn into internal fabric through the blanket.

### Part 4: Boundary Disruption (10 minutes)

12. Carefully remove your hook from the live loop (do not pull the yarn — just slide the hook out). Observe what happens. The live loop is still there, but it is unsecured. The Markov blanket is weakened. If you tugged the yarn, the fabric could unravel.
13. Reinsert your hook into the live loop. The blanket is restored.
14. Now **frog** (rip back) one full row. As you pull the yarn, watch each stitch dissolve: internal states become external states again. The boundary moves backward.
15. Stop after one row is frogged. Crochet that row again. The boundary moves forward once more.

### Part 5: Reflection and Discussion (15 minutes)

16. On your paper, draw a simple diagram of your crochet system showing:
    - Internal states (completed fabric)
    - External states (yarn, environment)
    - Blanket states (working edge, hook, live loop)
    - Arrows showing the flow of yarn from external through blanket to internal

## Discussion Questions

* At what exact moment did the system come into existence — with the slip knot, the first chain, or the first row?
* When you frogged a row, did the system shrink, or did the boundary simply move?
* If you set your work down and left the room, does the system still exist? What has changed about the Markov blanket?
* How does this hands-on experience change your understanding of what a "system boundary" means in Active Inference?

## Wrap-Up

Fasten off your swatch (or leave the live loop on the hook secured with a stitch marker). You have physically enacted the creation, maintenance, and partial dissolution of a system's Markov blanket. Bring your labeled swatch to the next crochet circle meeting for group discussion.
