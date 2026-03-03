# Lab: Implementing Multi-Agent Communication

> **Learning Goal:** Build communicating agents, simulate conversations, and measure synchrony.

## Part 1: Set Up Two Agents

```python
# 3-state world (e.g., weather: sunny, cloudy, rainy)
A_a = np.array([[0.8, 0.1, 0.1], [0.1, 0.8, 0.1], [0.1, 0.1, 0.8]])
A_b = np.array([[0.7, 0.2, 0.1], [0.1, 0.7, 0.2], [0.2, 0.1, 0.7]])
B = np.eye(3).reshape(3, 3, 1)  # static world
C = np.zeros(3)
D = np.array([0.33, 0.34, 0.33])

agent_a = CommunicatingAgent(A_a, B, C, D, name="Alice")
agent_b = CommunicatingAgent(A_b, B, C, D, name="Bob")

print(f"Alice initial beliefs: {agent_a.qs.round(3)}")
print(f"Bob initial beliefs: {agent_b.qs.round(3)}")
print(f"Initial synchrony: {compute_synchrony(agent_a.qs, agent_b.qs):.3f}")
```


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Run a Conversation

Run 5 rounds of communication about the shared state (true state = 0):

```python
agent_a, agent_b = simulate_conversation(agent_a, agent_b, shared_state=0, num_rounds=5)
```

Track synchrony at each round. Does it increase?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Effect of Initial Disagreement

**Exercise**: Create agents with different priors:

- Alice: D_a = [0.8, 0.1, 0.1] (believes it's sunny)
- Bob: D_b = [0.1, 0.1, 0.8] (believes it's rainy)

Run 10 rounds. Do they converge? How many rounds does it take?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Noisy Communication Channel

**Exercise**: Introduce noise in the message channel (agent receives the wrong message sometimes):

```python
def noisy_receive(agent, message, noise=0.2):
    if np.random.random() < noise:
        message = np.random.randint(0, agent.A.shape[0])
    return agent.receive_message(message)
```

Compare synchrony with noise = 0, 0.2, 0.5. What happens?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Reflection

In 150 words, reflect: What did you learn about communication by implementing it as coupled inference? How does prior agreement (shared cultural norms) affect convergence speed?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Multi-agent setup | Two-agent initialization |
| 2 | Conversation simulation | Belief convergence |
| 3 | Disagreement analysis | Different priors |
| 4 | Channel noise | Communication reliability |
| 5 | Reflection | Communication as inference |
