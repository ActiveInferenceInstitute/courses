# Lab: Deep Temporal Models and Hierarchical Inference

> **Learning Goal:** Analyze multi-scale temporal models, trace message passing, and evaluate planning at multiple temporal depths.

## Part 1: Constructing a Deep Temporal Model

**Exercise**: Design a 3-level deep temporal model for driving a car:

| Level | Temporal Scale | States Represented | Transition Dynamics |
|-------|---------------|-------------------|---------------------|
| 1 (Fast) | ~100ms | Steering angle, acceleration, brake pressure | Continuous motor control dynamics |
| 2 (Medium) | ~5-30s | Lane position, speed, following distance, maneuver type (cruising, turning, stopping) | Discrete events: lane change, turn, stop |
| 3 (Slow) | ~minutes-hours | Route, destination, traffic conditions, trip context | High-level navigation plan |

For each level, specify:

1. What observations does it receive (or generate for lower levels)?
2. What predictions does it send to the level below?
3. What prediction errors does it send to the level above?

Now trace what happens during a surprising event: a traffic light turns red unexpectedly.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Message Passing Trace

> **Learning Goal:** Trace ascending and descending messages through a concrete scenario.

**Exercise**: Using the driving model from Part 1, trace the messages during a lane change:

**Time t₀**: Driver decides to change lanes (Level 3 decision)

1. **Descending L3 → L2**: Prediction: "Begin lane change maneuver"
2. **L2 update**: L2 updates its belief: maneuver = lane_change. This generates...
3. **Descending L2 → L1**: Prediction: "Steering angle should shift by X degrees over Y seconds"
4. **L1 execution**: Motor system generates proprioceptive predictions fulfilled by steering reflexes

**Time t₁**: A car appears in the blind spot (unexpected!) → Level 1 sensory prediction error

1. **Ascending L1 → L2**: PE: "Something is in the target lane — large visual prediction error"
2. **L2 update**: L2 revises maneuver → abort lane change
3. **Ascending L2 → L3**: PE: "Lane change failed, alternative route needed"
4. **L3 update**: Route plan may need revision

Write a 200-word analysis: How does precision weighting determine whether the ascending PE is strong enough to override the descending prediction?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Planning at Multiple Scales

> **Learning Goal:** Analyze how expected free energy operates at different temporal scales.

**Exercise**: For a student planning their day, compute expected free energy at three levels:

**Level 3 (Day plan)**: Policies: {go to class, skip class, study at home}

- G₃(go to class) = pragmatic value (learns material) + epistemic value (resolves exam uncertainty)
- G₃(skip class) = pragmatic value (rest) + epistemic cost (misses material)

**Level 2 (Hour plan, given "go to class")**: Policies: {sit front, sit back, participate actively}

- G₂(participate) = pragmatic (better grade) + epistemic (gets feedback on understanding)
- G₂(sit back) = lower engagement cost but lower information gain

**Level 1 (Moment plan, given "participate actively")**: Policies: {raise hand, type notes, listen}

- G₁(raise hand) = epistemic value (resolve specific confusion)

How do higher-level policies constrain lower-level EFE calculations?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Imagination and Counterfactuals

> **Learning Goal:** Analyze how deep temporal models enable mental simulation.

**Exercise**: Design a counterfactual reasoning scenario:

Scenario: You are deciding between two job offers — Company A (safe, stable, known) and Company B (exciting, risky, unknown).

1. **Generative model forward pass for Company A**: Run the model forward 5 years. What does Level 3 predict? Level 2 (yearly events)? Level 1 (daily experience)?
2. **Forward pass for Company B**: Same exercise. Note the higher uncertainty (wider distributions) at each level.
3. **EFE comparison**: Company A has lower pragmatic uncertainty (known reward) but lower epistemic value (nothing to learn). Company B has higher epistemic value but higher pragmatic uncertainty.
4. **How does the model resolve this?** What role does risk tolerance (precision on C vector) play?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Reflection

In 300 words, reflect: Deep temporal models suggest that consciousness may be related to the depth of the temporal hierarchy — deeper models enable richer subjective experience. Do you find this plausible? What aspects of consciousness does it explain? What does it miss?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Model construction | Multi-level temporal architecture |
| 2 | Message tracing | Ascending/descending information flow |
| 3 | EFE computation | Multi-scale planning |
| 4 | Counterfactual reasoning | Mental simulation through forward model |
| 5 | Philosophical reflection | Temporal depth and consciousness |
