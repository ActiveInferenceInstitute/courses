# Module 05: Action in Crochet Circles

## Learning Objectives

1. Recognize each stitch as a **policy execution** — a specific motor sequence that transforms the state of the fabric.
2. Analyze hook insertion angle, yarn over technique, and pull-through motion as components of a **motor policy** selected by the crocheter.
3. Understand frogging as **corrective action** — the agent actively reshaping the world to reduce accumulated prediction error.

## Introduction

Every stitch you make changes the fabric. This sounds obvious, but it is profound: in Active Inference, **action** is the mechanism by which an agent changes the world to bring it closer to its predictions. When you insert your hook, yarn over, and pull through, you are not just making a stitch — you are executing a policy, transforming external states (unworked yarn) into internal states (completed fabric) through the Markov blanket. This module examines the action side of crochet: the motor policies that compose each stitch, the choices embedded in every hook insertion, and the powerful corrective action of frogging.

## Key Concepts

### 1. Each Stitch as Policy Execution

In Active Inference, a **policy** is a sequence of actions selected by the agent to minimize expected free energy — to bring the world closer to the agent's preferred states. In crochet, each stitch is a micro-policy: a coordinated sequence of motor actions that produces a specific outcome in the fabric.

Consider a single crochet stitch. The policy is: (1) insert hook into the next stitch, (2) yarn over, (3) pull through the stitch (two loops on hook), (4) yarn over, (5) pull through both loops. Each step transforms the state of the system. Before the policy, there is one live loop on the hook and an unworked stitch below. After the policy, there is one new live loop, and the previous stitch has been secured into the fabric.

A double crochet has a different policy: (1) yarn over, (2) insert hook, (3) yarn over, (4) pull through (three loops on hook), (5) yarn over, (6) pull through two, (7) yarn over, (8) pull through remaining two. Same components — insertion, yarn over, pull-through — but a different sequence producing a taller stitch with different fabric properties.

The crocheter selects among these policies based on the pattern (the generative model's plan). The pattern says "dc in next 5 sts" and the crocheter executes the double crochet policy five times. This is Active Inference's perception-action loop at its most concrete: perceive the current state (where is the next stitch?), select the policy (which stitch type?), execute the action, observe the outcome, repeat.

### 2. Hook Insertion and Yarn Over as Motor Components

Within each stitch policy, there are **sub-actions** — individual motor components that the crocheter controls with precision. These are the building blocks of all crochet action:

**Hook insertion angle** determines where the hook enters the fabric. Inserting under both top loops of the previous stitch (the standard method) produces one texture. Inserting under the front loop only produces a ridged texture. Inserting under the back loop only produces a different ridge. Inserting into the space between stitches produces an open, lacy effect. Each variation is a different motor sub-action that produces a different fabric outcome — a different way of acting on the world through the Markov blanket.

**Yarn over technique** — the motion of wrapping the yarn around the hook before pulling through — determines the orientation of the new loop and its tightness. A consistent yarn over produces even stitches; an inconsistent one produces uneven fabric. The direction of the yarn over (over the top of the hook versus under) affects stitch appearance.

**Pull-through force** determines stitch tightness. Too much force compresses the stitch; too little leaves it loose. The crocheter calibrates this force continuously, adjusting for yarn type, hook material, and the desired fabric density.

These sub-actions are not consciously decomposed by experienced crocheters — they are bundled into the stitch policy and executed as a unit. But they become explicit when learning a new technique, troubleshooting tension problems, or teaching someone else. The transition from conscious control of individual sub-actions to automatic execution of the full policy is a key feature of skill acquisition in Active Inference.

### 3. Frogging as Corrective Action

**Frogging** — ripping back stitches or rows — is the crocheter's most dramatic form of action. It is not a failure; it is one of the agent's most important policies for reducing free energy.

In Active Inference, when prediction error accumulates beyond a tolerable threshold, the agent must take corrective action. Small errors might be absorbed (accept a slightly off count, compensate in the next row), but large or systematic errors demand a reset. Frogging is that reset: the crocheter pulls the yarn, stitches unravel, and completed fabric (internal states) reverts to unworked yarn (external states). The system boundary moves backward.

The decision to frog is itself a policy selection based on expected free energy. The crocheter evaluates: "If I continue despite this error, how much will the accumulated prediction error affect the finished project? If I frog back, what is the cost in time and effort, and how much error will be eliminated?" This cost-benefit analysis happens quickly, sometimes instinctively, but it is a genuine evaluation of competing policies.

Frogging also demonstrates a key Active Inference principle: the agent acts on the world, not just on its beliefs. When the fabric is wrong, the crocheter does not simply change their expectations — they change the fabric. This is active inference in its most literal sense: inference through action.

## Applications

In crochet, we see Action manifest in:

* **Stitch Variety as Policy Repertoire**: The range of stitches a crocheter knows — chain, slip stitch, single crochet, half double, double, treble, post stitches, bobbles, popcorns — constitutes their **policy repertoire**. Each stitch is a different policy with a different outcome. A larger repertoire gives the agent more options for shaping the fabric. Learning a new stitch is literally expanding your set of available actions.

* **Increases and Decreases as Shaping Actions**: Working two stitches into the same space (increase) or combining two stitches into one (decrease) are specialized actions that change the geometry of the fabric. A flat circle requires strategic increases; a hat crown requires strategic decreases. These shaping actions are policies selected to achieve a specific three-dimensional form — the crocheter is sculpting with yarn, using action to bring the fabric closer to the predicted shape.

## Conclusion

Every stitch is an action that changes the world. The hook insertion, yarn over, and pull-through form a motor policy executed at the Markov blanket of the crochet system. The crocheter selects among available policies based on the pattern's plan, executes them with calibrated precision, and corrects errors through the powerful action of frogging. In the next module, we explore how these actions are learned and refined over time — how muscle memory develops, how new stitches are acquired, and how the crocheter's skill grows with practice.
