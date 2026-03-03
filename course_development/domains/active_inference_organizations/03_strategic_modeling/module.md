# Unit 03: Strategic Modeling — Overview

## Learning Objectives

1. Define organizational **strategy as policy selection** under Expected Free Energy, balancing pragmatic value (goal achievement) and epistemic value (market learning).
2. Analyze how organizations use **scenario planning, competitive analysis, and market research** as epistemic actions to reduce strategic uncertainty.
3. Apply the **exploration-exploitation trade-off** to real strategic decisions: when to commit to a strategy and when to pivot.

## Introduction

Strategy is the organization's answer to the question: "What should we do?" In Active Inference, this is **policy selection under Expected Free Energy** — evaluating possible courses of action by considering both their expected goal achievement (pragmatic value) and their expected information gain (epistemic value).

This unit formalizes strategic modeling as Active Inference. The key insight is that good strategy is not simply choosing the most profitable option — it is balancing exploitation (pursuing known opportunities) with exploration (reducing uncertainty about the competitive landscape, emerging technologies, and shifting customer preferences).

## Key Concepts

### 1. Strategy as Expected Free Energy Minimization

Each strategic option π (enter a new market, launch a product, acquire a competitor) has an Expected Free Energy G(π):

**G(π) = -Pragmatic Value(π) - Epistemic Value(π)**

- **Pragmatic value**: Will this strategy produce the outcomes we prefer? Revenue growth, market share, customer satisfaction. Encoded in the organizational C vector (preferred observations).
- **Epistemic value**: Will this strategy teach us something? Does entering a test market reduce our uncertainty about demand? Does a pilot program clarify whether a technology works?

The best strategies minimize G(π) — they simultaneously pursue goals *and* reduce the organization's uncertainty about its environment.

### 2. Scenario Planning as Generative Modeling

Scenario planning (Shell's landmark methodology from the 1970s) is the organizational practice of constructing multiple generative models of the future. Each scenario is a *different* generative model of market evolution:

- **Scenario A**: "Energy prices rise, regulation tightens, demand shifts to renewables"
- **Scenario B**: "Status quo persists, existing business models remain profitable"
- **Scenario C**: "Disruptive technology eliminates the core market"

The strategic value of scenario planning is *epistemic* — it reduces the organization's model uncertainty by forcing explicit articulation of alternative futures. Organizations that scenario-plan are more robust to surprise because they have already rehearsed their inference under multiple generative models.

### 3. Competitive Analysis as Coupled Inference

In competitive markets, organizations are **coupled Active Inference agents** — each company's actions affect its competitors' observations, and vice versa. Understanding a competitor's generative model (their beliefs about the market, their strategic priorities, their capabilities) is essential for predicting their behavior.

Porter's Five Forces can be reinterpreted as five coupling channels through which competitive prediction errors flow: rivalry (direct observation of competitors), supplier power, buyer power, threat of substitutes, and threat of new entrants.

### 4. The Pivot as Bayesian Model Selection

A strategic pivot is **Bayesian model selection** at the organizational level: the evidence (market data, customer feedback, financial results) no longer supports the current generative model, and the organization switches to an alternative model. The lean startup's "build-measure-learn" loop is precisely a free energy minimization cycle — build a product (act), measure customer response (observe), learn (update the generative model), and pivot if the model evidence drops too low.

## Applications

- **Amazon's epistemic strategy**: Amazon's early investment in AWS was driven by epistemic value — the company learned about cloud infrastructure by using it internally, then discovered an enormous external market. The decision to offer cloud services externally (2006) was a strategic policy selected for both pragmatic value (new revenue) and epistemic value (learning about enterprise demand).
- **Kodak's failure to pivot**: Kodak invented the digital camera in 1975 but failed to update its generative model — its internal model (film is profitable) had such high precision that the prediction errors from digital photography were systematically attenuated. The organization's Markov blanket was too rigid to admit the signal that its core market was disappearing.

## Conclusion

Strategic modeling is Active Inference at the organizational level: policy selection under Expected Free Energy, scenario planning as multi-model inference, competitive intelligence as coupled inference, and strategic pivots as Bayesian model selection. This unit's 8 modules deepen each of these themes through the full Active Inference spine.
