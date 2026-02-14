# Module 05: Action — Policy Selection via Expected Free Energy

## Learning Objectives

1. Compute Expected Free Energy $G(\pi)$ and decompose it into risk and ambiguity components.
2. Implement policy selection using softmax over negative EFE values.
3. Run the T-maze benchmark and analyze exploration–exploitation behavior.

## Introduction

Action selection in Active Inference is not reward maximization — it is free energy minimization projected into the future. The agent evaluates each candidate policy by computing the **Expected Free Energy** (EFE), $G(\pi)$, which scores how much surprise and uncertainty that policy would produce. Policies yielding preferred, informative outcomes receive lower $G$ and higher posterior probability.

## Key Concepts

### 1. Expected Free Energy: The Action-Selection Criterion

For a single-step policy $\pi = [a]$, EFE is:

$$G(\pi) = \underbrace{D_{KL}[q(o \mid \pi) \| \tilde{P}(o)]}_{\text{risk (pragmatic)}} + \underbrace{\mathbb{E}_{q(s' \mid \pi)}[H[P(o \mid s')]]}_{\text{ambiguity (epistemic)}}$$

- **Risk**: penalizes policies whose predicted observations deviate from preferences $\tilde{P}(o) = \sigma(C)$.
- **Ambiguity**: penalizes policies that lead to states where observations are hard to predict (high conditional entropy of the A-matrix).

```python
from active_inference.math import compute_efe, compute_efe_components

q_s = np.array([0.5, 0.5])
G = compute_efe(q_s, model.A, model.B, model.C, action=0)
print(f"G(action=0) = {G:.4f}")

comps = compute_efe_components(q_s, model.A, model.B, model.C, action=0)
print(f"Risk = {comps['risk']:.4f}, Ambiguity = {comps['ambiguity']:.4f}")
print(f"G = risk + ambiguity = {comps['G']:.4f}")
```

### 2. Policy Posterior via Softmax

Given EFE values for all policies, the posterior over policies is:

$$q(\pi) = \sigma(-\gamma \cdot G(\pi) + \ln E(\pi))$$

where $\sigma$ is the softmax function, $\gamma$ is precision, and $E(\pi)$ is the habit prior.

```python
from active_inference.math import run_policy_inference

result = run_policy_inference(
    q_s=agent.q_s,
    A=model.A, B=model.B, C=model.C,
    policies=[[0], [1]],   # single-step policies
    gamma=4.0,
    E=model.E,
)

print(result["q_pi"])             # policy posterior
print(result["G_values"])         # EFE for each policy
print(result["selected_action"])  # argmax of q(π)
```

### 3. How Risk Drives Goal-Directed Action

Risk measures the KL divergence between what the policy predicts the agent will observe and what it prefers to observe:

$$\text{risk}(\pi) = D_{KL}[q(o \mid \pi) \| \sigma(C)]$$

If a policy leads to states that produce preferred observations, risk is low. The T-maze demonstrates this clearly:

- Policy "go-left" leads to the reward arm → predicted $q(o \mid \pi)$ aligns with $\sigma(C)$ → low risk
- Policy "go-right" leads to the no-reward arm → predicted observations diverge from preferences → high risk

### 4. How Ambiguity Drives Information-Seeking

Ambiguity is the expected conditional entropy of the likelihood:

$$\text{ambiguity}(\pi) = \sum_{s'} q(s' \mid \pi) \cdot H[P(o \mid s')]$$

If a policy leads to a state where observations are highly informative (low entropy columns of A), ambiguity is low. This drives the agent toward states that reduce uncertainty — the computational basis of curiosity.

### 5. The T-Maze Benchmark

The T-maze is the canonical Active Inference benchmark:

```
         [Left/Reward]
              |
[Start] --- [Center]
              |
         [Right/No-Reward]
              |
          [Cue Location]
```

- 4 states, 3 observations, 3 actions
- The cue location reveals where the reward is
- An ideal agent visits the cue first (epistemic drive), then goes to the reward arm (pragmatic drive)

```python
from active_inference.visualization import plot_tmaze
plot_tmaze(current_state=0, reward_location="left")
```

### 6. EFE Decomposition Visualization

```python
from active_inference.visualization import plot_efe_decomposition

risk_values = [comps["risk"] for comps in efe_history]
ambiguity_values = [comps["ambiguity"] for comps in efe_history]
plot_efe_decomposition(risk_values, ambiguity_values)
```

## Applications

- **Exploration before exploitation**: In the T-maze, the ambiguity term drives the agent to visit the cue location before choosing an arm. Without the ambiguity term, the agent would guess randomly.
- **Risk-sensitive planning**: By adjusting the C-vector magnitude, you can make the agent more or less sensitive to avoiding aversive outcomes.
- **Policy comparison**: Plotting $G(\pi)$ for all policies reveals the agent's decision landscape.

## Conclusion

Action selection in Active Inference is a principled combination of goal seeking (risk minimization) and information gathering (ambiguity reduction). The `compute_efe()` function and `run_policy_inference()` implement this mechanism. Module 06 extends the framework to learning — updating the model's parameters based on experience.
