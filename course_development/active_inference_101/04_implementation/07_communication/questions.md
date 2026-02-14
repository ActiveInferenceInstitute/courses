# Implementation — Module 07: Communication — Study Questions

1. How does the CommunicatingAgent class extend the basic agent?
2. What does `generate_message` return? How is it computed?
3. How does `receive_message` process incoming information?
4. In `simulate_conversation`, what is the flow of information each round?
5. Why do both agents get private observations before communicating?
6. What is Jensen-Shannon divergence? Why use it instead of KL divergence for synchrony?
7. What does synchrony = 1.0 mean? What does synchrony = 0.0 mean?
8. How does the synchrony typically evolve over rounds of conversation?
9. What are shared priors? How do they affect initial synchrony?
10. What happens when agents start with very different priors?
11. How does the reliability of agents' private observations affect convergence?
12. What does it mean to model a "message" as the argmax of beliefs?
13. How could you implement richer messages (not just single integers)?
14. How would deception (sending misleading messages) be modeled?
15. What is the relationship between this code and the math in Module 07 of Math Frameworks?
16. What tests would verify communication is working correctly?
17. How would you extend this to 3+ agents?
18. How does the A matrix of the message channel affect communication quality?
19. When does communication fail to produce synchrony?
20. How does this implementation relate to real human conversation?
