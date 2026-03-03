# Module 02: Agents — Autonomous Agents and Bots

## Learning Objectives

1. Define an **autonomous agent** in computer science (software that perceives and acts without human intervention).
2. Compare **rule-based** agents, **learning** agents, and **Active Inference** agents.
3. Discuss ethical considerations of deploying autonomous agents in society.

## Introduction

An AI agent is software that perceives its environment through sensors or data feeds, makes decisions, and takes actions — all without constant human supervision. From Siri to stock-trading bots to self-driving cars, autonomous agents are everywhere. But what makes a *good* agent? And how does Active Inference provide a principled architecture?

## Key Concepts

### 1. The Agent Architecture Spectrum

| Type | How It Decides | Strengths | Weaknesses |
|---|---|---|---|
| **Rule-based** | If-then rules | Simple, predictable, auditable | Brittle; breaks on unexpected inputs |
| **RL Agent** | Maximizes reward signal | Powerful optimization | Can exploit rewards in unintended ways |
| **Active Inference Agent** | Minimizes expected free energy | Balances exploration and exploitation naturally | Computationally expensive |

### 2. Perception and Action in Software

A chatbot's "perception" is the user's text input. Its "action" is the generated response. A self-driving car's perception is LIDAR point clouds and camera images. Its action is steering, braking, and accelerating. In every case, the sense-think-act loop from Module 02 (Math Foundations) applies.

### 3. AI Alignment: The Goal Specification Problem

A powerful AI agent that maximizes the wrong objective function can cause catastrophic harm. (In theory: "Maximize paperclip production" → convert all matter into paperclips.) Active Inference offers a potential solution: instead of maximizing an arbitrary reward, AIF agents minimize surprise relative to a *generative model of preferred outcomes*. The model itself constrains behavior.

## Applications

* **Chatbots (GPT, Claude)**: A Large Language Model (LLM) is an agent whose generative model is the statistical structure of language. It "predicts" the next token and "acts" by generating it. Hallucinations are prediction errors that the model fails to correct.
* **Recommendation Algorithms**: YouTube and TikTok agents predict what video you will watch next. The prediction error (you scroll past) causes a model update. Over time, the algorithm's model of your preferences converges — for better or worse.

## Discussion Questions

1. Is a social media recommendation algorithm an "agent"? Does it have beliefs, predictions, and actions? Justify your answer using the formal definition from Math Foundations.
2. What could go wrong if a self-driving car's objective function is "minimize travel time" with no other constraints?

## Summary

Autonomous agents perceive, decide, and act without human supervision. Active Inference provides a principled architecture: agents minimize expected free energy rather than maximizing arbitrary rewards. The alignment problem — ensuring AI agents pursue the right goals — is one of the most important challenges of our time.

## References

* Russell, S. & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach*. Chapter 2.
