# Study Questions: The Prototype as a System

## Analytical Questions

1. Explain how a prototype functions as a physical generative model. What does the prototype "predict," and what constitutes its "prediction error"?

2. Define the Markov blanket of a prototype in terms of its sensory states, active states, internal states, and external states. Why is this partition useful for prototyping decisions?

3. Compare low-fidelity and high-fidelity prototypes in terms of model resolution. Under what conditions does a low-fidelity prototype provide more useful information than a high-fidelity one?

4. What is the "kitchen sink prototype" failure mode? Explain why including too many components in a prototype can make it harder to learn from test results, using the concept of confounded variables.

5. How does the modularity principle in Active Inference apply to prototype decomposition? What conditions must hold for a sub-system to be prototyped independently?

6. Explain the relationship between a prototype's sensory surface and what can be learned from testing. What happens if the sensory surface does not include a variable that is critical to the final product?

7. In what sense is prototype design and test design "two aspects of the same act of inference"? How does the Markov blanket formalism unify these two activities?

8. Describe how the concept of expected free energy guides the choice between different fidelity levels. What are the epistemic and pragmatic components of this choice?

9. How does the concept of nested Markov blankets apply to the relationship between a prototype's sub-systems and the integrated prototype?

10. What is the difference between a prototype that tests a parameter hypothesis (e.g., "the optimal spring constant is 5 N/m") and one that tests a structural hypothesis (e.g., "a spring mechanism is better than a magnetic mechanism")? How do their Markov blankets differ?

## Applied Questions

11. You are developing a new type of bicycle helmet. Your core hypothesis is that a honeycomb internal structure absorbs impact force more effectively than traditional EPS foam. Design the Markov blanket for a prototype that tests this hypothesis. What is inside the blanket? What is excluded?

12. A software startup is building a language-learning app. They are debating whether to build a fully functional prototype with speech recognition or a "Wizard of Oz" prototype where a human simulates the speech recognition. Analyze this choice using the concept of prototype fidelity and Markov blankets.

13. You have built a prototype of a solar-powered water purifier, but test results are inconsistent — sometimes the purifier works well, sometimes it does not. Using systems thinking, identify possible reasons why the prototype's Markov blanket might be inadequately defined.

14. An inventor is developing a wearable device that monitors blood oxygen levels. The device has three sub-systems: an optical sensor, a signal processing unit, and a display. In what order should these sub-systems be prototyped and tested? Justify your answer using Active Inference principles.

15. Compare NASA's approach to Mars rover prototyping (using separate test rigs for gravity, atmosphere, and terrain) with a startup's approach of building a single integrated prototype. When is modular testing worth the overhead?

16. You are prototyping a children's toy that teaches basic physics through play. The toy involves rolling balls down adjustable ramps. Identify three fidelity levels for this prototype and specify what hypothesis each level can and cannot test.

17. A team has built a high-fidelity prototype of an electric scooter and is getting positive feedback from testers. However, the prototype cost $50,000 to build. Using the expected free energy framework, argue whether this was a good or bad prototyping decision. What information could they have obtained with a cheaper prototype?

18. Your invention is a new type of packaging that changes color when the food inside has expired. Design two prototypes with different Markov blankets — one that tests the color-changing chemistry and one that tests user comprehension of the color signal. Why must these be separate prototypes?

19. Consider a "digital twin" — a computer simulation of a physical product. In Active Inference terms, how does a digital twin relate to a physical prototype? What are the advantages and limitations of each as a generative model?

20. You are three months into prototyping and have built twelve iterations of your invention. Each iteration has changed something, but you are not sure if you are converging on a solution. Using the systems concepts from this module, describe how you would audit your prototyping process to determine whether you are making progress.
