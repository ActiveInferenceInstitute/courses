# Study Questions: Perception

1.  Define **Perception** in your own words, specifically as it applies to High School.

2.  How does the Free Energy Principle constrain our understanding of Perception?

3.  Contrast the Classical view of Perception with the Active Inference view.

4.  In the coin-flipping example, you start with a prior belief P(fair) = 0.5 and observe 7 heads out of 10 flips. Write out Bayes' theorem for this scenario and explain what happens to the posterior distribution.

5.  What is a Kalman filter, and how does it combine a predicted state with a noisy observation? Describe the mathematical weighting process in your own words.

6.  Explain the concept of "prediction error" mathematically. If a generative model predicts a value of 5.0 and the observation is 5.3, what is the prediction error, and how does the model use it?

7.  How does the precision (inverse variance) of observations affect Bayesian updating? If your GPS measurements are very noisy versus very precise, how does this change the weight given to new observations?

8.  Describe the difference between a prior distribution and a posterior distribution. Use a concrete mathematical example involving flipping a coin with unknown bias.

9.  A Kalman filter tracks a car's position using GPS data. If the GPS suddenly reports the car has teleported 100 miles, how does the filter handle this outlier? What mathematical mechanism prevents the model from fully trusting this observation?

10.  Explain why perception in Active Inference is described as "inference" rather than "detection." What mathematical operation transforms raw sensory data into a belief?

11.  Calculate the information content I = -log2(p) for an event with probability 0.5 versus one with probability 0.01. Which event is more surprising, and by how much?

12.  In the context of Bayesian updating, what happens when the prior is very strong (high confidence) and the likelihood from new data is weak? Show this mathematically using simple numbers.

13.  How does the concept of a generative model in Active Inference relate to the regression models you learn in statistics? What role do residuals play?

14.  A weather app predicts a 20% chance of rain, but you look outside and see dark clouds. How would you formally update the probability of rain using Bayes' theorem? Define your prior, likelihood, and posterior.

15.  Why is perception as "prediction error minimization" mathematically equivalent to maximizing the accuracy of a generative model? Show the relationship between minimizing error and maximizing fit.

16.  Explain the difference between supervised perception (you know the correct answer) and unsupervised perception (you must infer structure from data). Give a mathematical example of each.

17.  How would you model optical illusions using the framework of prediction error? What does it mean mathematically when the generative model produces a strong prediction that conflicts with sensory input?

18.  Describe the mathematical relationship between the Kalman filter's update equation and Bayes' theorem. Are they doing the same computation in different forms?

19.  If an agent's generative model has two possible hypotheses for an observation, explain how model comparison (using Bayes factors) determines which hypothesis better explains the data.

20.  Design a simple Bayesian perception system for a robot that must estimate the temperature of a room from noisy thermometer readings. Specify the prior, likelihood function, and update rule. How would the system's accuracy improve over time?

