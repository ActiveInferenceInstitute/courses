# Estimating Yardage and Shaping: Planning Under Uncertainty

## Summary

Before a single stitch is made, the crocheter faces questions that require planning: How much yarn will I need? How will I shape the fabric to create the desired form? Should I work top-down or bottom-up? When should I block, and how will blocking change the dimensions? Each of these questions requires **prediction under uncertainty** — using your generative model to forecast outcomes when the inputs are imprecise and the process is long. This module explores planning in crochet as a window into how Active Inference agents navigate uncertainty about the future.

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain yardage estimation as prediction under uncertainty
2. Describe shaping calculations as planning under a generative model
3. Identify construction method choice as selecting between different model architectures

---

## Key Concepts

### 1. Yardage Estimation: Forecasting Under Uncertainty

Estimating how much yarn a project will require is one of the most common planning challenges in crochet. It is also a beautiful example of **prediction under uncertainty**:

**The inputs you have**:
- Gauge (stitches and rows per inch)
- Finished dimensions (width, length, or circumference)
- Stitch type (different stitches use different amounts of yarn per unit area)
- The pattern's stated yardage requirement

**The uncertainties**:
- Your gauge may not match the pattern's gauge exactly
- Your tension may drift over the course of a long project
- Stitch-type changes within the pattern (ribbing uses less yarn than open lace) make per-row estimates variable
- Finishing (seaming, borders, fringe) adds hard-to-predict yardage
- Dye lot availability — will you be able to buy more if you run short?

Experienced crocheters deal with this uncertainty in characteristic ways:
- **Buffer buying**: Buying one extra skein "just in case" — a learned prediction about their own estimation error
- **Weighing**: Weighing the completed portion and remaining yarn to project whether they have enough — real-time model updating
- **Pattern yardage trust calibration**: Learning which designers' yardage estimates to trust (some consistently overestimate, others underestimate)

Each of these strategies reflects a **precision-calibrated** approach to prediction. The crocheter has learned not just how to estimate yardage but how uncertain their estimates tend to be, and they plan accordingly.

### 2. Shaping: Computing Future States of the Fabric

Shaping — using increases, decreases, and construction techniques to create three-dimensional form from flat fabric — requires your generative model to compute future states:

**Increase planning**: To create a flat circle, you need to add stitches at a specific rate. For single crochet, roughly 6 increases per round maintains flatness. Too few increases and the circle cups into a bowl. Too many and it ruffles. Your model must predict the geometric consequences of stitch count changes.

**Decrease planning**: A hat crown requires decreasing from the full circumference down to a closed top. The decrease schedule determines the crown shape — rapid decreases create a pointy top, gradual decreases create a rounded top. Planning the schedule requires predicting how different decrease rates map to different shapes.

**Garment shaping**: Armholes, necklines, waist shaping, and bust darts all require planned stitch-count modifications at specific points. The crocheter must predict:
- Where in the row count to begin shaping
- How many stitches to remove or add
- How the shaping affects the finished garment's fit

This planning is **model-based prediction of future states**. You are not just thinking about the current row — you are running your model forward many rows to predict the fabric's eventual shape. The accuracy of this prediction depends on the quality of your model's geometric understanding.

### 3. Construction Order: Choosing the Model's Causal Direction

A garment can be constructed multiple ways, and the choice of construction method is a planning decision with significant consequences:

**Top-down construction**:
- Start at the neckline and work down to the hem
- Advantage: You can try it on as you go, providing continuous feedback
- Active Inference parallel: Rich sensory feedback throughout — you can detect and correct prediction errors early

**Bottom-up construction**:
- Start at the hem and work up to the neckline
- Advantage: Established traditional patterns, often simpler shaping logic
- Active Inference parallel: Delayed feedback — you cannot assess fit until pieces are joined, so you must rely more heavily on your model's predictions

**Modular construction**:
- Create separate pieces (front, back, sleeves) and join them
- Advantage: Portable pieces, easy to redo one section
- Active Inference parallel: Compartmentalized prediction — each piece can be validated independently before the whole is assembled

**Seamless construction**:
- Work the entire garment in one piece with no seaming
- Advantage: No seams to sew, drapes smoothly
- Active Inference parallel: Continuous state tracking required — any error propagates forward without natural breakpoints

The choice of construction method is, in Active Inference terms, **selecting a generative model architecture** — different methods structure the prediction-observation-correction loop differently, with different tradeoffs between feedback frequency and planning complexity.

### 4. Blocking and Finishing: Predicting Post-Construction Transformation

Blocking — wetting or steaming a finished piece and pinning it to shape — introduces **hidden variables** that must be anticipated during planning:

- **Fiber content affects blocking**: Acrylic does not block significantly. Wool can stretch dramatically. Cotton holds its shape firmly after blocking. Your model must predict how the fiber will respond to water and pinning.
- **Stitch pattern affects blocking**: Lace opens up dramatically when blocked. Dense single crochet barely changes. Planning for lace requires mentally subtracting the pre-blocking dimensions and predicting the post-blocking dimensions.
- **Gauge after blocking**: The "true" gauge may only be revealed after blocking. Planning a garment requires predicting the post-blocked measurements, which means planning for a transformation you cannot observe during construction.

Blocking planning requires your generative model to account for variables that are **hidden during construction** but become visible afterward. This is a hallmark of sophisticated planning — predicting transformations that occur in a future state you cannot yet observe.

### 5. Time and Resource Planning

Beyond the physical fabric, crocheters plan at a meta-level:

- **Time estimation**: "This blanket will take me about 60 hours." This prediction draws on experience with similar projects, adjusted for pattern complexity and available time per session.
- **Skill readiness**: "I should practice this stitch on a swatch before committing to the whole project." This is planning to acquire model capability before it is needed.
- **Material sourcing**: "This pattern calls for a discontinued yarn — I need to find a substitute." This requires predicting how a material change will affect the model's outputs.
- **Seasonal timing**: "I need to finish this sweater before October." This introduces a time constraint that affects the planning horizon.

All of these meta-planning activities require the generative model to operate at a higher level of abstraction — predicting not just what the fabric will look like, but how the entire project process will unfold.

---

## Applications: Sharpening Your Planning Skills

### The Yardage Estimation Challenge

Before starting your next project, make three independent yardage estimates: (1) from the pattern's stated requirement, (2) from your gauge and dimensions calculation, and (3) from weighing a completed section and extrapolating. Compare the three estimates. This reveals the uncertainty in your predictions.

### The Construction Method Comparison

Choose a simple garment (like a vest) and outline two different construction plans: top-down and bottom-up. For each, list the advantages for error detection and correction. Which provides more feedback, and when? This exercise builds awareness of how construction method affects the prediction-correction loop.

### The Blocking Prediction Exercise

Before blocking a completed swatch or project, measure its dimensions and predict the post-blocking measurements. Then block it and compare. The gap between prediction and reality reveals how well your model accounts for the hidden variables of blocking.

---

## Conclusion

Planning in crochet is prediction under uncertainty. Yardage estimation, shaping calculations, construction method choice, and blocking planning all require your generative model to forecast outcomes in situations where the inputs are imprecise and the future is partially hidden. Skilled planners are skilled predictors — they have calibrated models that not only generate estimates but also carry accurate assessments of how uncertain those estimates are. Understanding planning as active inference helps you make better decisions before, during, and after your projects.

This concludes the Pattern & Prediction course. From reading patterns as systems, to understanding yourself as an inference agent, to perceiving, thinking, acting, learning, communicating, and planning — every aspect of crochet pattern work can be illuminated by the framework of Active Inference. The next time you pick up a pattern, you will see it with new eyes: as a generative model waiting to be decoded, tested, and brought to life by your hands.

---

## Key Terms

| Term | Crochet Meaning | Active Inference Meaning |
| --- | --- | --- |
| Yardage estimation | Predicting total yarn needed | Forecasting under uncertainty |
| Buffer buying | Getting extra yarn just in case | Uncertainty-calibrated planning |
| Shaping schedule | Plan for increases/decreases | Model-based computation of future states |
| Top-down vs bottom-up | Construction direction | Model architecture selection |
| Blocking | Wetting and pinning to shape | Post-construction state transformation |
| Time estimation | Predicting project duration | Meta-level temporal planning |
