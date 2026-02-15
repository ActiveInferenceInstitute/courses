# Study Questions: Learning

1.  Define **Learning** in your own words, specifically as it applies to High School.

2.  How does the Free Energy Principle constrain our understanding of Learning?

3.  Contrast the Classical view of Learning with the Active Inference view.

4.  In curve fitting, the least-squares algorithm minimizes the sum of squared residuals. Write the formula for this sum and explain how each iteration updates the parameters m and b in y = mx + b.

5.  Explain why overfitting a polynomial to data points is mathematically analogous to a generative model that is too complex. What does the free energy framework say about model complexity?

6.  Calculate the sum of squared residuals for the data points (1,2), (2,4), (3,5) using the model y = 1.5x + 0.5. Is this a good fit? How would you improve it?

7.  What is the mathematical relationship between prediction error on training data and generalization to new data? Why do these sometimes move in opposite directions?

8.  Describe the accuracy-complexity tradeoff in free energy using a concrete example. If Model A has 2 parameters and Model B has 20 parameters, which might have lower free energy overall, and why?

9.  How does the concept of regularization in statistics (e.g., adding a penalty for large parameter values) relate to the complexity term in variational free energy?

10.  A student fits a degree-1, degree-5, and degree-15 polynomial to 20 data points. Sketch the expected training error and test error curves for each. Which polynomial minimizes free energy?

11.  Explain the concept of a "learning curve" in machine learning. How does prediction error change as the number of training examples increases? What does this mean for the generative model?

12.  How does gradient descent learn parameter values over time? Write the update rule for a single parameter and explain each term in the equation.

13.  What is the mathematical definition of "surprise" in Active Inference? How does it relate to the negative log-likelihood of an observation given the model?

14.  Compare and contrast supervised learning (fitting y = f(x) with labeled data) and unsupervised learning (finding structure without labels) in terms of the generative models they use.

15.  Why does the free energy principle predict that biological learners should prefer simpler models? Connect this to Occam's razor and the concept of minimum description length.

16.  A neural network is trained on images of cats and dogs. After training, it encounters an image of a horse. Describe mathematically what happens to the prediction error and free energy. How should the model "learn" from this new category?

17.  Explain the difference between learning the parameters of a model (parameter learning) and learning which model structure to use (model selection). Which is a deeper form of learning?

18.  How does the learning rate affect convergence? If the learning rate is alpha = 0.001 versus alpha = 1.0, sketch the expected trajectories of the loss function over training epochs.

19.  What does it mean for learning to "converge"? Define a mathematical stopping criterion based on the change in free energy between iterations.

20.  Design a simple learning experiment: generate 10 data points from y = 2x + 1 + noise. Fit both a linear and quadratic model. Compute the residuals for each. Which model has lower free energy, and why? Explain your reasoning using the accuracy-complexity tradeoff.

