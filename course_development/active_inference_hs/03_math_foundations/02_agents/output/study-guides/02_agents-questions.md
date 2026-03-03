# Study Questions: Agents

1.  Define **Agents** in your own words, specifically as it applies to High School.

2.  How does the Free Energy Principle constrain our understanding of Agents?

3.  Contrast the Classical view of Agents with the Active Inference view.

4.  In the chess-playing agent example, what does the probability distribution over board states represent mathematically? How does Bayes' theorem update it after each opponent move?

5.  Explain how a random walk on a number line becomes an Active Inference agent when you add a preferred state near zero. Write out the mathematical objective function that would bias the step probabilities.

6.  What is the difference between exploitation and exploration in game theory? How does the expected free energy formulation balance these two goals mathematically?

7.  Model a simple agent that wants to maintain a bank account balance near $100. Define the agent's belief state, its observations, and the actions it can take. What function does it minimize?

8.  How does the concept of a probability distribution over states differ from a single deterministic state? Why do Active Inference agents use distributions rather than point estimates?

9.  A passive stochastic process has no goals. What mathematical element must you add to turn it into an Active Inference agent? Express this formally.

10.  Describe how a chess-playing agent's generative model differs from a simple lookup table of moves. What advantages does the probabilistic model provide?

11.  Using the random walk example, calculate the expected position after 10 steps for (a) an unbiased walk and (b) a walk biased toward zero with a specific penalty function. Show your work.

12.  In game theory, what is a Nash equilibrium? How might Active Inference agents converge to or diverge from Nash equilibria compared to classical rational agents?

13.  Explain the role of the Markov blanket in defining what an agent can and cannot observe. Give a mathematical example using conditional independence.

14.  Design a simple mathematical agent that navigates a number line from position 5 to position 0. Specify its state space, action space, transition function, and objective function.

15.  How does an Active Inference agent handle ambiguity differently from a classical decision-making agent? Use a mathematical example involving uncertain payoffs.

16.  What happens to an Active Inference agent's behavior when its generative model is inaccurate? Describe the mathematical consequences of model mismatch in the random walk scenario.

17.  Compare the mathematical structure of a thermostat (simple controller) with an Active Inference agent. What does the agent have that the thermostat lacks?

18.  Explain how expected free energy differs from simple expected reward. What additional term does free energy include, and why does it matter for agent behavior?

19.  If an agent's prior beliefs strongly favor one state but observations consistently point to another, describe the mathematical tension that arises. How is it resolved?

20.  Propose a mathematical scenario (different from chess or random walks) where an agent must balance exploration and exploitation. Define the state space, actions, and the free energy objective explicitly.

