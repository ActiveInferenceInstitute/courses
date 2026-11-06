# GNN model: course 04 computer science T-maze

## GNNSection

ActInfPOMDP

## GNNVersionAndFlags

GNN v1

## ModelName

Course T-Maze

## ModelAnnotation

The T-maze used by the computer-science module of the Active Inference course.
States are 0 center, 1 left arm, 2 right arm, 3 cue. Observations are 0 null,
1 reward, 2 no-reward. Actions are 0 move-left, 1 move-right, 2 stay.

From the center, move-left enters the left arm and move-right enters the right
arm. Both arms are absorbing under every action. The cue is absorbing, and the
stay action is the identity at every state. The cue observation has no reward
information in this fixture; the reward likelihood is 0.8 on the matching arm
and 0.2 on the other arm. The initial state is the center with probability 1.

This model is the repository-owned fixture at
`course_development/active_inference/04_computer_science/tests/conftest.py::tmaze_model`,
and the benchmark described in
`course_development/active_inference/04_computer_science/05_action/module.md`.
It deliberately omits the optional habit prior E, learning, policy inference,
and the course visualization/publishing layers. It is not one of the five
verbatim upstream exemplars under `course_development/gnn/01_gnn_syntax/models/`.
The reference integration loop runs five steps.

## StateSpaceBlock

s[4,1,type=float]        # State: 0 center, 1 left, 2 right, 3 cue
o[3,1,type=int]          # Observation: 0 null, 1 reward, 2 no-reward
u[1,type=int]            # Action: 0 move-left, 1 move-right, 2 stay
A[3,4,type=float]        # Likelihood P(o | s)
B[4,4,3,type=float]      # Transitions: next_state, previous_state, action
C[3,type=float]          # Log preferences over observations
D[4,type=float]          # Initial state prior
t[1,type=int]            # Discrete time step

## Connections

D>s
s-A
A>o
s>B
u>B
B>s
C-o

## InitialParameterization

# A[observation, state].
A={
  (1.0, 0.0, 0.0, 1.0),
  (0.0, 0.8, 0.2, 0.0),
  (0.0, 0.2, 0.8, 0.0)
}

# B[next_state, previous_state, action]: each outer tuple is one next-state
# slice; within a slice rows are previous states and columns are actions.
# Actions are 0 move-left, 1 move-right, 2 stay.
B={
  (
    (0.0, 0.0, 1.0),
    (0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0)
  ),
  (
    (1.0, 0.0, 0.0),
    (1.0, 1.0, 1.0),
    (0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0)
  ),
  (
    (0.0, 1.0, 0.0),
    (0.0, 0.0, 0.0),
    (1.0, 1.0, 1.0),
    (0.0, 0.0, 0.0)
  ),
  (
    (0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0),
    (1.0, 1.0, 1.0)
  )
}

# C is a log-preference vector, not a probability vector: consumers softmax it.
C={
  (0.0, 2.0, -2.0)
}

# D starts at center.
D={
  (1.0, 0.0, 0.0, 0.0)
}


## Equations

A[o,s] = P(o | s); each A column sums to 1.
B[s',s,a] = P(s' | s,a); each B[:,s,a] column sums to 1 over s'.
C = (0,2,-2) is a log-preference vector, not a normalized probability.
D = (1,0,0,0) starts the agent at center.
Belief update: q(s) proportional to D[s] * A[o,s].

## Time

Dynamic
DiscreteTime=t
ModelTimeHorizon=5

## ActInfOntologyAnnotation

s=HiddenState
o=Observation
u=Action
A=LikelihoodMatrix
B=TransitionMatrix
C=PreferenceVector
D=Prior
t=Time

## ModelParameters

num_hidden_states: 4
num_obs: 3
num_actions: 3
num_timesteps: 5
num_modalities: 1
num_factors: 1
b_tensor_order: next_state_previous_state_action

## Footer

Course T-Maze v1.0 - repository-owned fixture from the computer-science module.
Four states, three observations, three actions.

## Signature

Cryptographic signature goes here
