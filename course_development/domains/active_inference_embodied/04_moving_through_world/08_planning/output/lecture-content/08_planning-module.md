# Module 08: Planning in Embodied Cognition — Route Planning and Wayfinding

## Learning Objectives

1. Define **embodied route planning** as the integration of somatic, spatial, and temporal information to select movement trajectories through the world.
2. Analyze how **cognitive maps, landmark sequences, and prospective kinesthetic simulation** support planning beyond immediate perception.
3. Apply the Active Inference framework to understand planning breakdowns (getting lost) and planning expertise (expert wayfinding).

## Introduction

Route planning is among the oldest cognitive challenges — every mobile organism must solve it. Finding water, shelter, food, or a mate requires constructing a plan that extends beyond current perception: the destination is not visible, the path is not obvious, and the terrain between here and there is uncertain.

## Key Concepts

### 1. Cognitive Map-Based Planning

Route planning uses the cognitive map as a **generative model for spatial simulation**:

- The agent imagines a trajectory through the map — a sequence of place-state transitions that lead from current location to goal
- Each candidate route is evaluated for Expected Free Energy: travel time (pragmatic cost), terrain difficulty (energy cost), uncertainty (epistemic cost), and safety (risk cost)
- The selected route minimizes total EFE — the route that is fastest, easiest, safest, and most certain

When the cognitive map is incomplete (unfamiliar territory), the agent balances route following (following known paths) with route discovery (exploring to improve the map) — the exploration-exploitation trade-off instantiated as a wayfinding decision.

### 2. Landmark-Based Wayfinding

Humans overwhelmingly navigate by landmarks rather than metric coordinates:

- Route instructions are landmark sequences: "Turn left at the big oak tree, go past the red house, turn right at the church"
- Each landmark is a **perceptual checkpoint** — when the expected landmark is perceived, the prediction error drops to zero, confirming the agent is on the correct route
- Missing an expected landmark generates a large prediction error that triggers recalculation: "I should have seen the church by now — am I lost?"

### 3. Time-Space Budgeting

Embodied route planning integrates spatial and temporal constraints:

- "I need to reach the summit before weather changes" → the spatial plan (which route) is constrained by temporal deadlines
- "I have energy for approximately 3 more hours of walking" → the spatial plan is constrained by metabolic resources
- "This route is shorter but steeper; that route is longer but flatter" → the decision requires integrating distance, elevation gain, and estimated energy expenditure into a unified EFE evaluation

Expert navigators develop accurate time-space budgets because their somatic generative models (calibrated by experience) generate precise predictions of travel time, energy cost, and physical difficulty for different terrain types.

### 4. Getting Lost: Planning Failure and Recovery

Getting lost is a **state estimation failure** — the agent's believed position diverges from the actual position:

- Progressive disorientation: Small navigation errors accumulate until the cognitive map's prediction errors become unresolvable
- Panic response: High free energy from spatial uncertainty triggers autonomic stress responses (elevated heart rate, hypervigilance) — the body's generic alarm signal for unmanageable surprise
- Recovery strategies: Backtracking to the last known position (returning to a low-free-energy state), climbing for a broader view (epistemic action to generate high-information observations), or following a linear feature (river, road, ridge) that constrains the position estimate to a 1D uncertainty

## Applications

- **Wilderness navigation instruction**: Teaching wilderness navigation through Active Inference principles involves calibrating the student's spatial generative model — training map reading (building the cognitive map), pace counting (calibrating the path integration B matrix), terrain association (learning to predict map features from landscape features), and deliberate positioning (maintaining the link between map and territory).
- **Urban wayfinding design**: Designing navigable cities requires understanding how pedestrians plan routes — logical street grids reduce cognitive map complexity; distinctive landmarks at decision points reduce wayfinding uncertainty; consistent signage provides precision-weighted observations that prevent disorientation. The "legibility" of a city (Lynch, 1960) is the inverse of average wayfinding free energy.

## Conclusion

Embodied route planning integrates cognitive mapping, landmark-based wayfinding, time-space budgeting, and recovery from disorientation. All are implementations of Active Inference planning in the spatial domain — evaluating routes by Expected Free Energy and selecting trajectories that balance pragmatic goals with epistemic uncertainty reduction. This completes the Moving Through World unit and the Embodied Cognition domain course.
