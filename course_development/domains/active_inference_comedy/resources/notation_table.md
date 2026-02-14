# Notation Table: Comedy & Active Inference

> Canonical notation mapping comedy terms to Active Inference concepts. All module content must use these mappings consistently.

---

## Core Mappings

| Comedy Term | Active Inference Concept | Notation | Description |
|------------|------------------------|----------|-------------|
| Setup | Prediction-generating utterance | S → P(o) | The setup installs a prediction P(o) about the forthcoming observation |
| Punchline | Prediction error | PE = o − P(o) | The punchline is the observation that violates the setup's prediction |
| Timing / Beat | Precision accumulation window | Δt_π | Time during which the audience's precision π on the prediction increases |
| Tag / Topper | Secondary prediction error | PE₂ | Additional prediction error following the initial punchline |
| Blow | Maximum prediction error | PE_max | Terminal, highest-amplitude prediction error in the routine |
| Callback | Posterior reactivation | P(θ|o_past) → PE_new | Previously resolved belief reactivated to generate fresh error |
| Rule of three | Prior + violation | P₁, P₂ → ¬P₃ | Two instances build the prior; third violates it |

---

## Agent Mappings

| Comedy Role | Active Inference Role | Key Parameters |
|------------|----------------------|----------------|
| Straight man | High-precision prior agent | π_prior ≫ π_likelihood |
| Comic / Funny man | Volatile model agent | π_prior ≪ π_likelihood, high learning rate |
| Audience | Meta-inference agent | Tracks both performer models; generates laughter at PE threshold |
| Director / Emcee | Policy-selecting agent | Selects action sequences to maximize EFE |
| Heckler | Adversarial inference agent | Attempts to destabilize performer's generative model |

---

## System Mappings

| Comedy Structure | Active Inference Structure | Example |
|-----------------|--------------------------|---------|
| Bit / Routine | Bounded inference episode | "Who's on First?" = one long bit |
| Set | Action policy sequence | A comedian's 20-minute set |
| Tight five | Optimized policy | Maximum PE per unit time |
| Open mic | Exploration / epistemic foraging | Sampling novel actions |
| Headliner set | Exploitation | Deploying proven policies |
| Genre (stand-up, improv, sketch) | Generative model class | Different model architectures |

---

## "Who's on First?" Specific Mappings

| Routine Element | Active Inference Mapping |
|----------------|-------------------------|
| "Who" (the player) | Observation with degenerate likelihood: P(name|"Who") vs P(question|"Who") |
| "Who" (the question) | Epistemic action: query intended to reduce uncertainty |
| Abbott's assertion | High-precision prior: π("Who" = name) → ∞ |
| Costello's question | Low-precision query: π("Who" = question) fluctuating |
| The loop / escalation | Non-convergent inference: free energy F(t) is non-decreasing |
| Costello's frustration | Cumulative free energy without discharge: ΣF(t) → explosion |
| Audience laughter | Free energy discharge: social prediction error acknowledgment |
| "Third base!" | Partial resolution: one player name unambiguously decoded |
| "I Don't Know" (third base) | Meta-level prediction error: even the "answer" is a confusion |

---

## Mathematical Notation

| Symbol | Meaning | Comedy Application |
|--------|---------|-------------------|
| F | Variational free energy | The "tension" in a joke before the punchline |
| D_KL | KL divergence | Size of the laugh: distance between prior and posterior |
| π | Precision (inverse variance) | How confidently a prediction is held |
| o | Observation | What is heard, seen, or perceived by the comedic agent |
| s | Hidden state | The "true" meaning behind an utterance |
| P(o|s) | Likelihood | How probable the observation is given the hidden state |
| P(s) | Prior | What the agent believes before the observation |
| P(s|o) | Posterior | What the agent believes after the observation |
| G | Expected free energy | Anticipated surprise + information gain from a future action |
| σ | Policy | A sequence of planned comedic actions |

---

*Last updated: 2026-02-14*
