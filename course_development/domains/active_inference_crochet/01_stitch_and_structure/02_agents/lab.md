# Lab: You Are the Crocheter

## Objective

Experience yourself as an Active Inference agent by working a short crochet pattern, deliberately introducing errors, detecting prediction errors, and choosing correction strategies.

## Materials

* Worsted weight yarn in a light color (makes stitches easy to see), approximately 30 yards
* Crochet hook, size H/8 (5.0mm)
* Printed or written pattern (provided below)
* Pen and a "Decision Log" sheet (provided below)
* Scissors
* Stitch markers (optional)

## Pattern to Follow

Work the following 6-row swatch:
- **Row 1**: Ch 16. Sc in 2nd ch from hook and in each ch across. (15 sc)
- **Row 2**: Ch 1, turn. Sc in each st across. (15 sc)
- **Row 3**: Ch 1, turn. Sc in each st across. (15 sc)
- **Row 4**: Ch 1, turn. *Sc in next 2 sts, skip 1 st, sc in next 2 sts.* Repeat * to * across. (Count will decrease — this is intentional)
- **Row 5**: Ch 1, turn. Sc in each st across. (Count the stitches — notice the change)
- **Row 6**: Ch 1, turn. Sc in each st across.

## Decision Log Template

For each row, record:
| Row | Expected stitch count | Actual stitch count | Match? | Feeling (smooth/uncertain/surprised) | Action taken |
|-----|----------------------|---------------------|--------|--------------------------------------|-------------|

## Steps

### Part 1: Building Your Generative Model (10 minutes)

1. Read through the entire pattern before you begin. As you read, form a mental image of what the swatch will look like. This is your **generative model** being initialized.
2. On your decision log, write your expected stitch count for each row before you start crocheting.
3. Note: Row 4 introduces skipped stitches. If you are not sure how many stitches will result, write your best guess. Uncertainty in your prediction is completely normal — it reflects a sparse generative model for that specific instruction.

### Part 2: Crocheting as Active Inference (20 minutes)

4. Begin crocheting Row 1. At the end, count your stitches. Record the actual count and whether it matches your expectation. Note how you feel: was the row smooth (low free energy) or uncertain (higher free energy)?
5. Continue through Rows 2 and 3. These are simple repetitions — your generative model should become more confident. Record each row in your log.
6. Now work Row 4 with the skip pattern. This row will feel different. Your generative model must accommodate a new instruction. Record the actual stitch count, your level of surprise, and how the row felt.
7. Rows 5 and 6: Continue in single crochet. Your stitch count has changed from the original 15. Record everything.

### Part 3: Deliberate Error and Response (15 minutes)

8. Now, crochet one more row (Row 7), but **deliberately skip a stitch** somewhere in the middle without marking where.
9. Count your stitches at the end of the row. You should be one short. Record the prediction error.
10. Now, make a choice — your **agent decision**:
    - **Option A (Active Inference — change the world)**: Frog back to the error and redo the row correctly.
    - **Option B (Model Update — change the model)**: Accept the count and plan to add a stitch in the next row.
    - **Option C (Perceptual Inference)**: Look again — maybe you miscounted? Re-inspect.
11. Record which option you chose and why. There is no wrong answer — each is a legitimate agent strategy.

### Part 4: Reflection and Discussion (15 minutes)

12. Review your decision log. In which rows did you feel the most "flow" (lowest free energy)? In which did you feel the most surprise?
13. When you reached the deliberate error, what was your gut reaction? Did you want to frog immediately, or were you tempted to let it go?
14. Discuss with your crochet circle: what determines whether you frog or accept an error in your own projects? What factors influence your decision?

## Discussion Questions

* How did it feel to read the pattern before crocheting versus actually working it? What does this tell you about the difference between a theoretical generative model and one tested against reality?
* At what point did the simple rows start to feel automatic? What changed in your agent processing?
* When you introduced the skip pattern in Row 4, did your stitching slow down? Why might an increase in generative model complexity slow the agent's actions?
* Describe your decision-making process when you found the deliberate error. What would an "ideal" Active Inference agent do?

## Wrap-Up

Keep your swatch and your decision log. They are a record of you acting as an Active Inference agent: forming predictions, observing outcomes, detecting errors, and choosing responses. Bring both to the next session for the Perception module.
