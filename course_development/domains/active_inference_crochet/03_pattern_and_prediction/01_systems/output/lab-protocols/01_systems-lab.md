# Lab: Pattern Design Workshop — Reading the Pattern as a Whole

## Objective

Analyze a crochet pattern as a complete generative model by identifying its system components, mapping its information flow, and evaluating the quality of its system boundary.

## Materials Needed

- Two crochet patterns of your choice (one simple, one complex — or one free, one paid)
- A printed or digital copy you can annotate
- Colored pens or highlighters (4 colors)
- Your crochet journal or notebook

## Exercise 1: Pattern Anatomy (30 minutes)

Take your simpler pattern and annotate it using four colors:

1. **Color 1 — Priors**: Highlight everything that specifies assumptions before stitching begins (yarn weight, hook size, gauge, skill level, finished measurements, notions needed)
2. **Color 2 — Likelihood**: Highlight the stitch-by-stitch transformation instructions (row/round instructions, stitch abbreviations, special stitch definitions)
3. **Color 3 — Checksums**: Highlight all verification points (stitch counts, measurement checkpoints, "your piece should now measure...")
4. **Color 4 — Posterior predictions**: Highlight everything that describes the expected outcome (finished measurements, photos of completed project, schematic diagrams)

**Record in your journal**:
- How much of the pattern is dedicated to each category?
- Where are the gaps — areas where the pattern assumes knowledge without stating it?
- If a total beginner picked up this pattern, where would they first encounter a prediction error?

## Exercise 2: System Boundary Comparison (30 minutes)

Now compare your two patterns side by side.

Create a table with these columns:
| Feature | Pattern A | Pattern B |
| --- | --- | --- |
| Materials specified (how precisely?) | | |
| Gauge information provided? | | |
| Photos included? How many? | | |
| Schematic diagrams? | | |
| Stitch counts per row? | | |
| Special stitch definitions? | | |
| Size options? | | |
| Difficulty rating given? | | |
| Finishing instructions? | | |

**Discuss**: Which pattern has a thicker Markov blanket? Which one requires you to carry more of the generative model in your own head?

## Exercise 3: Build a Minimal Generative Model (30 minutes)

Write a pattern for a simple flat rectangle (such as a dishcloth or scarf) that functions as a complete generative model. Your pattern must include:

1. **Explicit priors**: Specific yarn, specific hook size, target gauge
2. **Likelihood mapping**: Row-by-row instructions
3. **At least 3 checksums**: Points where the reader can verify the model's predictions
4. **Posterior prediction**: A description or sketch of what the finished piece should look like, with measurements

Now, deliberately remove one component (for example, delete the gauge information) and have a partner read the pattern. Can they predict the finished dimensions? This exercise demonstrates how incomplete system boundaries increase prediction error.

## Exercise 4: System Feedback (20 minutes)

If you have access to Ravelry or another pattern platform, look up a popular pattern and read 5-10 project notes from other crocheters. For each note, identify:

- What prediction errors did they encounter?
- Which system component failed (prior mismatch, unclear likelihood, missing checksum)?
- How did they resolve the mismatch — by adjusting their own behavior or by modifying the pattern?

**Record your findings**: What patterns (no pun intended) do you notice in how prediction errors arise and get resolved?

## Discussion Questions for the Circle

1. Have you ever abandoned a pattern because its system boundary was too thin — too little information to work from? What was missing?
2. When you adapt a pattern (change the size, substitute yarn), are you modifying the system's priors or its likelihood function? Or both?
3. How does your experience level change the thickness of the system boundary you need? Do advanced crocheters need thinner blankets?

## Wrap-Up

Write a brief reflection (3-5 sentences) on what you learned about patterns-as-systems. Has this changed how you will read your next pattern?
