# Module 08: Planning — AI Safety, Ethics, and the Future

## Learning Objectives

1. Identify the key **AI safety** challenges: alignment, interpretability, robustness, and fairness.
2. Explain how Active Inference's preference-based architecture offers potential advantages for safe AI.
3. Develop a personal, informed stance on the future of AI in society.

## Introduction

This final module steps back from the technical details to ask the most important questions: Where is AI headed? What are the risks? How can we build AI systems that are safe, fair, and aligned with human values? Planning — for engineers, policymakers, and citizens — is the most critical skill in the age of AI.

## Key Concepts

### 1. The Alignment Problem

The **alignment problem** asks: how do we ensure that a powerful AI system pursues the goals we *actually* intend, not a distorted or dangerous interpretation?

**Example**: An AI trained to maximize player engagement on a social media platform might learn that *outrage* is the most engaging content. The goal was "keep users on the platform" but the outcome is "polarize society." The objective function was *misaligned* with human values.

Active Inference offers a structural advantage: rather than optimizing an arbitrary reward signal, an AIF agent minimizes surprise relative to a *generative model of preferred outcomes*. This means the agent's behavior is constrained by its model of what *should* happen — not just what *could* maximize a number.

### 2. Interpretability and Black Boxes

A neural network with 175 billion parameters (GPT-3) is a **black box**: it produces impressive outputs, but we cannot easily understand *why* it made a particular decision. This is dangerous in high-stakes settings (medical diagnosis, criminal sentencing, military targeting).

**Interpretability** research tries to open the black box. Active Inference models are inherently more interpretable because they maintain explicit beliefs (probability distributions) about the world. You can *inspect* the agent's generative model and see what it expects, what surprised it, and why it chose a particular action.

### 3. Fairness and Bias

AI systems inherit the biases of their training data. A hiring algorithm trained on historical data (which reflects decades of discrimination) will reproduce that discrimination. A medical AI trained mostly on data from one demographic group will perform worse on other groups.

Mathematically, bias occurs when the training distribution $P_{\text{train}}(x)$ does not match the real-world distribution $P_{\text{real}}(x)$. This is a *structural prediction error* that no amount of training within the biased dataset can fix.

### 4. Your Role

Every student in this class will live in a world shaped by AI. You will vote on AI regulation, work alongside AI systems, and make personal choices about which AI tools to trust. Developing an informed, critical perspective — not blind techno-optimism or unfounded fear — is the most important outcome of this entire course.

## Applications

* **AI Regulation**: The EU's AI Act classifies AI systems by risk level (minimal, limited, high, unacceptable). High-risk systems (medical, educational, judicial) face strict transparency and testing requirements.
* **Deepfakes**: AI-generated videos that impersonate real people raise profound questions about truth, consent, and the reliability of evidence in a legal system.

## Discussion Questions

1. Should AI systems be legally required to explain their decisions? What would "explanation" look like for a neural network?
2. You are designing an AI system for college admissions. How would you test for fairness across different demographic groups?
3. In 10 years, what job do you want to have? How do you think AI will change that job? How will you need to adapt?

## Summary

AI safety, alignment, interpretability, and fairness are the defining challenges of the 21st century. Active Inference offers structural advantages for safe AI through its preference-based architecture and interpretable generative models. But ultimately, the future of AI depends on informed citizens who understand both the technology and its societal implications.

## References

* Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control*.
* Crawford, K. (2021). *Atlas of AI: Power, Politics, and the Planetary Costs of Artificial Intelligence*.
