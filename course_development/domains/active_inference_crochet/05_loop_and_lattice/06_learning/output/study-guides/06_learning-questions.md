# Study Questions: Learning

1. Describe the first time you learned to crochet (or learned any new handcraft). What were the biggest sources of error in your earliest attempts? In neural network terms, which "weights" were most poorly calibrated?

2. Explain why a beginning crocheter improves rapidly in the first few hours of practice but then experiences a plateau. How does this parallel the **learning rate decay** seen in neural network training?

3. What does it mean for a crochet stitch to become "muscle memory"? Describe this in terms of neural network weight convergence — when the weights stabilize and the motor policy executes automatically.

4. A crocheter who has made fifty granny square blankets can execute a granny square flawlessly but struggles with amigurumi. Explain this as **overfitting** to a specific pattern type. What training data is their network missing?

5. How does trying a new yarn weight (switching from worsted to fingering weight, for example) function as a form of **data augmentation** for the crocheter's motor system? What specific motor parameters must adjust?

6. Compare the loss landscape of a simple single-crochet dishcloth to the loss landscape of a complex lace shawl with a 24-row repeat. Which has more local minima? Which is more forgiving of small errors?

7. A crocheter picks up a pattern that uses techniques they have never tried. Their prediction errors are high at first but decrease with each row. Draw a rough sketch of the expected **training curve** (error vs. rows) and label the steep improvement phase and the plateau.

8. In machine learning, **regularization** prevents overfitting by penalizing the network for becoming too specialized. Name three crochet practices that function as regularization — activities that prevent a crocheter from becoming too narrowly skilled.

9. Explain the difference between a crocheter who corrects a mistake consciously ("I need to insert the hook deeper") and one who corrects it unconsciously (the hand just finds the right depth over time). In neural network terms, is there a difference between these two types of weight update?

10. A crochet teacher watches a student and says, "You are wrapping the yarn over the wrong direction." How does this external correction compare to a **supervised learning** signal in neural network training? What role does the teacher play that self-practice does not provide?

11. Why does a crocheter who works exclusively with one brand of smooth acrylic yarn sometimes struggle when switching to handspun wool or slippery bamboo? Frame this in terms of **distribution shift** — a change in the input data that the trained network has not seen before.

12. Describe how a crochet pattern book organized from simple to complex projects (dishcloth, scarf, hat, sweater) functions as a **curriculum** in the machine learning sense. Why is this ordering more effective than starting with the sweater?

13. When a crocheter joins a crochet circle and learns techniques by watching others, how does this parallel **transfer learning** or **ensemble learning** in neural networks? What knowledge is being transferred?

14. A crocheter attempts a bullion stitch for the first time and fails repeatedly. After 20 attempts, it suddenly "clicks" and they can do it. Describe this breakthrough in terms of the loss landscape — what might have happened geometrically (a sudden drop from a plateau into a valley)?

15. How does the concept of a **local minimum** apply to crochet? Describe a situation where a crocheter develops a technique that works "well enough" but prevents them from achieving a better result — and how they might escape that local minimum.

16. Compare the learning process of a right-handed crocheter switching to left-handed crochet to the process of **fine-tuning** a pre-trained neural network on a new task. What transfers and what must be relearned?

17. In active inference, the generative model must be flexible enough to accommodate new observations. How does a crocheter's generative model update when they encounter a completely unfamiliar stitch for the first time? What is the prediction error, and how does it drive model updating?

18. A crocheter working on a complex colorwork pattern finds that they make more errors when tired. In neural network terms, what might be happening to their "inference" process under cognitive fatigue? How does this relate to the idea of noisy gradient updates?

19. Explain how frogging and re-doing a section (rather than accepting a flawed result) functions as a form of **regularization** in crochet learning. Why might accepting imperfect work actually slow long-term skill development?

20. Reflect on your own crochet learning trajectory. Plot it mentally as a training curve: where were the steep improvements? Where did you plateau? What broke you through a plateau (new techniques, new materials, new teachers, new project types)? How does your curve compare to a typical neural network training curve?
