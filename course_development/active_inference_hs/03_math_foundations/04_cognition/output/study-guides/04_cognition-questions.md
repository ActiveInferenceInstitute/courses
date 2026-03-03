# Study Questions: Cognition

1.  Define **Cognition** in your own words, specifically as it applies to High School.

2.  How does the Free Energy Principle constrain our understanding of Cognition?

3.  Contrast the Classical view of Cognition with the Active Inference view.

4.  Calculate the entropy H = -sum(p * log2(p)) for a multiple-choice question with 4 equally likely answers versus one where you are 90% sure of one answer. What does the difference tell you about cognitive uncertainty?

5.  In the matrix multiplication example, an input vector is multiplied by a weight matrix to produce a prediction. Write out a simple 2x2 example and show how the error vector is computed.

6.  Explain how backpropagation in neural networks is analogous to cognition updating its internal model. What mathematical operation computes the gradient of the error?

7.  What is the relationship between entropy and uncertainty? If entropy equals zero, what does that imply about the agent's cognitive state?

8.  Describe how the concept of a loss function in machine learning relates to variational free energy in Active Inference. What mathematical properties must both share?

9.  A student studying for an exam reduces their cognitive entropy from H = 2.0 bits to H = 0.5 bits. Interpret what this means in terms of their understanding of the material.

10.  How does matrix multiplication serve as a model of cognitive inference? Explain what the weight matrix "knows" and how it transforms sensory input into predictions.

11.  Compare the mathematical structure of a simple linear regression model with a single-layer neural network. How are they similar, and what does each one represent as a generative model?

12.  What happens to the entropy of a belief distribution as you receive more and more evidence? Sketch a graph of entropy versus number of observations and explain its shape.

13.  Explain why cognition in Active Inference involves both reducing prediction errors AND maintaining model simplicity. What mathematical penalty prevents overfitting?

14.  Calculate the KL divergence between two simple probability distributions: P = (0.7, 0.3) and Q = (0.5, 0.5). Interpret the result in terms of how far the agent's beliefs are from maximum uncertainty.

15.  How does the concept of dimensionality reduction (e.g., PCA) relate to cognitive compression? Why would an Active Inference agent prefer a lower-dimensional representation?

16.  A neural network with 1000 parameters fits training data perfectly but fails on new data. A network with 10 parameters has some training error but generalizes well. Explain this tradeoff using the free energy framework.

17.  Describe the mathematical difference between "thinking fast" (using a cached generative model) and "thinking slow" (performing full Bayesian inference). Which has lower computational cost, and which has lower free energy?

18.  How would you measure whether an agent's cognition has "converged"? Define a mathematical criterion using entropy or free energy.

19.  Explain how cognitive biases could be modeled as fixed priors in a Bayesian framework. Give a mathematical example where a strong prior leads to incorrect conclusions despite contradictory evidence.

20.  Design a simple mathematical model of cognition that takes in three observations, maintains a belief state, and updates its predictions. Specify the update rule, the loss function, and how you would measure the model's cognitive accuracy.

