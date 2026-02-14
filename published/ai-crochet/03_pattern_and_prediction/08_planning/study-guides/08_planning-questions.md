# Study Questions: Planning — Estimating Yardage and Shaping

1. Explain why yardage estimation is prediction under uncertainty. What are the known inputs and what are the sources of uncertainty?

2. Why do experienced crocheters often buy one extra skein of yarn? Frame this behavior in terms of learned precision about estimation uncertainty.

3. How does shaping (increases and decreases) require your generative model to compute future states of the fabric?

4. Compare top-down and bottom-up construction methods in terms of when you receive feedback about fit. Which provides earlier prediction error detection?

5. What hidden variables does blocking introduce? Why must these be anticipated during the planning phase?

6. How does the choice between modular construction (separate pieces joined) and seamless construction (one piece) affect the error correction process?

7. Explain why time estimation for a project requires your model to operate at a higher level of abstraction than stitch-level planning.

8. A crocheter plans a blanket that requires 12 skeins. They buy 13. What does this extra skein represent in terms of their model's self-assessed uncertainty?

9. How does the fiber content of yarn affect blocking predictions? Why must your planning model account for material properties?

10. Describe the planning required to create a garment with multiple size options (S, M, L, XL). What must the designer's model predict for each size?

11. When a pattern says "work until piece measures 15 inches," this is a different planning specification than "work 48 rows." Compare the precision and flexibility of each.

12. How does the choice of construction method (top-down vs. bottom-up) reflect different tradeoffs between planning complexity and feedback frequency?

13. A crocheter is making a color-blocked blanket and needs to plan how to distribute yarn across color sections. What calculations does their model need to perform?

14. Explain why planning for lace projects requires predicting the post-blocking dimensions, not the pre-blocking dimensions. What makes this cognitively challenging?

15. How does the concept of "ease" in garment design (planned extra room beyond body measurements) reflect the designer's model of acceptable prediction range?

16. When you plan the order of operations for a complex project (make the body, then the sleeves, then join), you are defining a construction sequence. How does this sequence affect error propagation?

17. A crocheter weighs their remaining yarn mid-project to determine if they have enough. What type of real-time model updating is this?

18. How does planning for a gift (unknown recipient measurements) differ from planning for yourself? What additional uncertainty must the model account for?

19. Explain why seasonal timing constraints ("I need this done by Christmas") change the planning problem. How does a deadline affect decision-making about modifications and error correction?

20. If you were planning the most complex project you have ever attempted, what planning steps would you take to maximize the probability of success? Frame your answer in terms of active inference.
