# Practice Quiz: Communication (Implementation)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** In the multi-agent implementation, one agent's message becomes:
A) The other agent's action
B) An observation that the receiving agent processes through its inference pipeline
C) A direct modification of the other agent's beliefs
D) Noise

**2.** Generalized synchrony is measured using:
A) Euclidean distance
B) Jensen-Shannon divergence — symmetric, bounded, and interpretable
C) The number of messages exchanged
D) Physical proximity

**3.** A synchrony value of 1.0 means:
A) Agents disagree completely
B) Agents have identical belief distributions over hidden states
C) Communication has failed
D) One agent is correct

**4.** Shared priors between agents:
A) Prevent communication
B) Give agents similar starting beliefs, making convergence faster
C) Make agents identical
D) Are impossible to implement

**5.** `generate_message` returns the argmax of beliefs because:
A) It's the only option
B) The agent communicates its most confident belief — a simple communication protocol
C) argmax is always correct
D) NumPy requires it

**6.** Noisy communication channels:
A) Speed up convergence
B) Slow down or prevent belief convergence by corrupting messages
C) Have no effect
D) Always improve accuracy

**7.** Two agents with very different priors:
A) Cannot communicate
B) Take more rounds to converge because they must overcome initial disagreement
C) Converge instantly
D) Always deadlock

## Part B: Short Answer

**1.** Two agents start with beliefs A=[0.9, 0.1] and B=[0.1, 0.9]. Compute the initial synchrony using JSD. Show your work.

**2.** Explain how this implementation models an "echo chamber" — agents who already agree reinforcing each other's beliefs. What would the synchrony trajectory look like?

**3.** Design an extension where agents can choose NOT to communicate (silence as an action). How would this affect the implementation and convergence dynamics?
