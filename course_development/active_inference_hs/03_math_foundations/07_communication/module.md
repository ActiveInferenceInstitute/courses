# Module 07: Communication — Information Theory and Shared Models

## Learning Objectives

1. Calculate the **information content** of a message using Shannon's formula.
2. Explain the concepts of **redundancy**, **compression**, and **channel capacity**.
3. Connect information theory to how agents share generative models through communication.

## Introduction

Communication is the transfer of information from one agent to another. Claude Shannon (1948) founded **information theory** to answer a precise question: how much can you compress a message before you start losing meaning? This module introduces Shannon's ideas and connects them to the Active Inference view of communication as model alignment.

## Key Concepts

### 1. Information Content

The **information content** of an event is inversely related to its probability:

$$I(x) = -\log_2 P(x) \text{ bits}$$

A certain event ($P = 1$) carries 0 bits of information — you already knew it would happen. A very unlikely event ($P = 0.01$) carries about 6.6 bits — it is highly surprising and informative. This is exactly the Active Inference concept of **surprisal**.

### 2. Redundancy and Compression

Natural language is highly **redundant**. English has about 1.0 to 1.5 bits of information per character (far below the theoretical maximum of $\log_2(26) ≈ 4.7$ bits). This redundancy is why you can read "th_qu_ck br_wn f_x" — your brain's generative model *predicts* the missing letters. Compression algorithms (ZIP, MP3, JPEG) exploit redundancy to shrink files. They remove the predictable parts and keep only the surprising parts.

### 3. Communication as Model Alignment

In Active Inference, communication is not just transferring data — it is aligning generative models between agents. When a teacher explains a concept, they are transmitting compressed representations of their generative model. When a student asks a clarifying question, they are reporting a prediction error: "my model doesn't match yours — please send more data." Successful communication occurs when both agents' models converge.

## Applications

* **Text Compression**: Students can compute the information content of each letter in a message and see which letters carry the most surprise (rare letters like 'z' carry more bits than common letters like 'e').
* **Social Media**: A meme that goes viral contains high information in a compact format — it aligns millions of generative models simultaneously. A meme that flops has a model mismatch: the sender's intended meaning does not align with the receiver's prior.

## Discussion Questions

1. Why are common words (like "the," "is," "a") so short, while rare words (like "antidisestablishmentarianism") are so long? How does this relate to information content?
2. If you text a friend "k" and they understand you mean "okay, I agree," how much information is actually transmitted? How?

## Summary

Communication is the transfer of information between agents. Shannon's information theory measures surprisal in bits. Redundancy allows compression. In Active Inference, communication is the process of aligning generative models, and prediction errors drive the conversation forward.

## References

* Shannon, C. E. (1948). A Mathematical Theory of Communication. *Bell System Technical Journal*, 27(3), 379–423.
