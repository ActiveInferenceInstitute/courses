# Unit 03: Mathematical Foundations of Active Inference

## Learning Objectives

1. Understand **Bayes' theorem** as the mathematical core of belief updating and explain how it formalizes the process of learning from evidence.
2. Apply concepts from **probability theory** and **information theory** -- including entropy, surprise, and KL divergence -- to real-world reasoning problems.
3. Connect the **variational free energy** equation to its component parts and explain what each term means intuitively.
4. Develop comfort with mathematical reasoning under uncertainty, recognizing that precise thinking about imprecise information is a fundamental life skill.

## Introduction

Mathematics is often taught as a collection of techniques for solving well-defined problems with exact answers. But the most important problems in life -- Should I trust this person? Is this news article reliable? What career should I pursue? -- are problems of reasoning under uncertainty. There are no exact answers, only better and worse ways of weighing evidence.

Active Inference is built on a branch of mathematics designed precisely for this: **probability theory** and its extension into **information theory**. These tools give us a rigorous way to talk about beliefs, evidence, surprise, and learning. Bayes' theorem, the centerpiece of this unit, is arguably the most important equation you have never been taught in school -- a simple formula that describes how rational agents should update their beliefs when they encounter new evidence.

This unit does not require advanced math. If you can work with fractions and basic algebra, you have everything you need. What it does require is a willingness to think carefully about uncertainty -- to treat "I don't know" not as a failure but as a starting point for precise reasoning.

## Unit Structure

This unit contains eight modules that follow the Active Inference spine:

1. **Systems** -- Probability spaces, sample spaces, and how mathematical systems model uncertainty.
2. **Agents** -- Bayesian agents: how to model a rational decision-maker who updates beliefs using Bayes' theorem.
3. **Perception** -- Likelihood functions, sensory evidence, and the math of interpreting noisy data.
4. **Cognition** -- Prior beliefs, posterior beliefs, and the internal mathematics of model updating.
5. **Action** -- Expected free energy, decision theory, and choosing actions that minimize future uncertainty.
6. **Learning** -- Parameter learning, model comparison, and how mathematical systems get better over time.
7. **Communication** -- Information theory, entropy, and Shannon's mathematical framework for communication.
8. **Planning** -- Sequential decision-making, planning as inference, and the mathematics of thinking ahead.

## Key Themes

### Probability Is About Belief, Not Just Frequency

Most people think of probability as counting outcomes: a coin has a 50% chance of heads because half the time it lands heads. But in Active Inference, probability represents **degree of belief**. A 70% probability that it will rain tomorrow does not mean it will rain 70% of the time -- it means that, given all available evidence, a rational agent should have 70% confidence in rain. This Bayesian interpretation of probability is the foundation of Active Inference.

### Surprise Is a Mathematical Quantity

When something unexpected happens, you experience surprise. In information theory, surprise has a precise mathematical definition: it is the negative log probability of an observation. Something with a 1% chance of happening carries much more surprise (mathematically) than something with a 50% chance. Active Inference proposes that biological systems are fundamentally in the business of minimizing this mathematical quantity.

### Free Energy Connects Everything

The variational free energy equation is the mathematical heart of Active Inference. It combines two ideas: how surprising your observations are (accuracy) and how far your beliefs have moved from your prior expectations (complexity). Minimizing free energy means finding beliefs that are both accurate (they explain the data) and simple (they do not overfit). This is a deep principle that connects perception, learning, and action under a single mathematical umbrella.

## Discussion Questions

1. A medical test for a rare disease is 99% accurate, yet if you test positive, the probability that you actually have the disease might be less than 10%. How does Bayes' theorem explain this apparent paradox?
2. Why is the concept of "surprise" in information theory measured on a logarithmic scale? What does this imply about how we experience very unlikely events versus somewhat unlikely ones?
3. How does the trade-off between accuracy and complexity in the free energy equation relate to the common advice "keep it simple"?

## Summary

The mathematics of Active Inference is not abstract symbol manipulation -- it is a formal language for reasoning about uncertainty, evidence, and belief. Bayes' theorem, information theory, and the free energy principle provide a unified mathematical framework that connects perception, action, and learning. By the end of this unit, you will have the quantitative tools to understand not just *that* Active Inference works, but *why* it works -- and you will have a new appreciation for the power of mathematical thinking in everyday life. In the final unit, we apply all of this to the technology and AI systems that are reshaping the world around you.
