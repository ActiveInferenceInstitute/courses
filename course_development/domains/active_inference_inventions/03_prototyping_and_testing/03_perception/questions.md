# Study Questions: Reading the Prototype's Signals

## Analytical Questions

1. Explain the difference between observation and inference in prototype testing. Why is it important to record raw observations before interpreting them?

2. How does Active Inference's perception equation apply to prototype testing? Why will two inventors with different priors perceive different things in identical test data?

3. Classify the following test signals into the four categories (quantitative, qualitative, behavioral, failure): (a) a user clicks the back button three times, (b) the motor draws 2.3 amps, (c) a reviewer says "this looks professional," (d) the hinge snaps during the 50th cycle.

4. Why are failure events described as the "highest-value perceptual signals" in testing? How does this relate to the concept of prediction error in Active Inference?

5. Explain the distinction between parameter updating and structure updating in the context of test signals. What types of signals trigger each?

6. How does instrumentation extend the inventor's perceptual Markov blanket? Give an example of a hidden state that becomes observable through instrumentation.

7. What is the precision-richness trade-off between quantitative and qualitative test data? When is each type more informative?

8. Explain how behavioral observation reveals a user's implicit generative model. Why might behavioral signals be more informative than verbal feedback?

9. What does it mean to say that "prototype design and perception design are linked"? How does the prototype's Markov blanket constrain what can be perceived?

10. How can an inventor design a test to maximize the information content of the signals it produces? What role does signal diversity play?

## Applied Questions

11. You are testing a new kitchen knife design. A user says "it feels good" while cutting tomatoes but struggles visibly with harder vegetables. Which signal — the verbal feedback or the behavioral observation — is more informative? Justify your answer using signal taxonomy concepts.

12. Your prototype solar panel produces 85 watts in testing, but your model predicted 100 watts. Describe how you would use this quantitative signal to update your generative model. What additional signals would you need to determine whether this is a parameter error or a structure error?

13. A medical device prototype passes all quantitative performance tests but receives qualitative feedback from nurses that it is "stressful to use." What type of model update does this qualitative signal suggest? What hidden variables might be missing from the inventor's model?

14. Design an instrumentation plan for a wearable fitness device prototype. Identify at least three hidden states that need to be made observable, and specify the instruments that would transduce them.

15. The Tacoma Narrows Bridge case shows how engineers can observe a signal (dramatic oscillations) but fail to perceive its significance. Describe a situation in your own invention project where you might be observing a signal without understanding its true cause.

16. You are conducting user testing of a mobile app. You have screen recordings, tap logs, session durations, and post-test survey responses. Organize these data sources into the signal taxonomy and explain what each uniquely contributes.

17. An inventor observes that their prototype fails at high temperatures but not at room temperature. Their generative model does not include temperature as a variable. Is this a parameter update or a structure update? What should the inventor do next?

18. Compare the information value of a single dramatic failure vs. ten minor, ambiguous test results. Which provides more useful information for updating the generative model? Under what conditions might the answer change?

19. You have budget for either (a) 50 quantitative stress tests or (b) 10 qualitative user interviews. Your prototype is a new type of backpack. Which do you choose and why? What information do you sacrifice?

20. Design a "failure listening" protocol for your invention project: a structured approach to recording, classifying, and analyzing every failure event during testing. What categories would you use? What information would you record for each event?
