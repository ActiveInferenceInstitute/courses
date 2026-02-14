"""Configuration and curriculum registry for course generation.

Contains all 8 curriculum definitions organized by type:
- AGE_LEVEL_CURRICULA: ES, MS, Family, 101, 401
- DOMAIN_CURRICULA: Embodied, Robotics, Organizations
- ALL_CURRICULA: Combined registry
"""

from .schema import CurriculumConfig, CourseConfig, ModuleConfig, MODULE_TOPICS

# ─── Module subtitle/concept tables per curriculum ──────────────────────────
# Each entry: (subtitle, [key_concepts], [learning_goals])

_ES_MODULES = {
    "systems": ("Your World is Full of Systems!", ["boundaries", "inside vs outside", "steady states"], ["Identify systems around you", "Draw a system boundary", "Explain what keeps a system stable"]),
    "agents": ("What Makes You... You?", ["living things", "goals", "needs"], ["Describe what makes something alive", "Identify an agent's needs", "Explain how agents are different from rocks"]),
    "perception": ("The Surprise Monster", ["senses", "expectations", "surprise"], ["Name your five senses", "Explain what surprise feels like", "Draw what you expected vs what happened"]),
    "cognition": ("Your Brain's Best Guess", ["guessing", "imagination", "updating"], ["Explain how your brain guesses", "Show how guesses can be wrong", "Describe updating a guess"]),
    "action": ("Making Things Happen", ["moving", "trying", "helping"], ["Describe how actions change the world", "Identify actions that explore", "Identify actions that help"]),
    "learning": ("Getting Better Every Day", ["practice", "mistakes", "growth"], ["Explain how practice helps", "Describe learning from mistakes", "Show a before-and-after skill"]),
    "communication": ("Talking, Sharing, Helping", ["words", "signals", "teamwork"], ["Identify ways we communicate", "Explain why sharing helps", "Describe teamwork as communication"]),
    "planning": ("The Treasure Map", ["steps", "goals", "choosing"], ["Draw a simple plan", "Explain why order matters", "Choose between two paths"]),
}

_MS_MODULES = {
    "systems": ("Systems Everywhere: Phones, Schools, and You", ["Markov blanket", "homeostasis", "feedback loops"], ["Define a system using boundaries", "Explain homeostasis with an example", "Identify feedback loops in daily life"]),
    "agents": ("What Makes an Agent Tick?", ["autonomy", "goals", "generative model"], ["Distinguish agents from objects", "Describe an agent's internal model", "Explain goal-directed behavior"]),
    "perception": ("Seeing is Believing... Or Is It?", ["prediction", "prediction error", "sensory input"], ["Explain perception as prediction", "Identify prediction errors in illusions", "Describe how the brain filters input"]),
    "cognition": ("Thinking Fast and Slow", ["beliefs", "updating", "inference"], ["Explain belief updating", "Describe fast vs slow thinking", "Apply inference to a mystery scenario"]),
    "action": ("Actions Speak Louder", ["pragmatic action", "epistemic action", "expected free energy"], ["Distinguish exploration from exploitation", "Explain how actions reduce uncertainty", "Describe a policy as a plan"]),
    "learning": ("Level Up: How We Learn", ["parameter learning", "model updating", "adaptation"], ["Explain learning as model updating", "Describe how repetition changes the brain", "Apply learning concepts to study habits"]),
    "communication": ("Connected: Social Brains", ["shared models", "social inference", "cultural learning"], ["Explain how we model other minds", "Describe cultural knowledge transfer", "Identify examples of social inference"]),
    "planning": ("Game Plan: Thinking Ahead", ["future states", "decision trees", "risk vs reward"], ["Map out a decision tree", "Explain risk vs reward trade-offs", "Describe planning as imagining futures"]),
}

_FAMILY_MODULES = {
    "systems": ("Your Family is a System", ["family boundaries", "routines", "balance"], ["Recognize your family as a system", "Identify daily routines as stability", "Notice when balance is disrupted"]),
    "agents": ("Your Baby is an Agent", ["curiosity", "needs", "reaching"], ["See your baby as an active explorer", "Identify what your baby needs", "Notice goal-directed reaching and grasping"]),
    "perception": ("Why Babies Cry When Surprised", ["expectation", "novelty", "startle"], ["Understand crying as prediction error", "Recognize novelty-seeking play", "Support gradual exposure to new things"]),
    "cognition": ("Little Minds, Big Guesses", ["object permanence", "peekaboo", "mental models"], ["Connect peekaboo to prediction", "Understand object permanence stages", "Support cognitive development through play"]),
    "action": ("Crawling, Reaching, Doing", ["motor development", "trial and error", "co-regulation"], ["Understand movement as prediction fulfillment", "Support safe exploration", "Practice co-regulation during frustration"]),
    "learning": ("Every Day is a School Day", ["habituation", "scaffolding", "attachment"], ["Recognize signs of learning", "Use scaffolding in daily activities", "Connect secure attachment to learning"]),
    "communication": ("First Words and Beyond", ["babbling", "joint attention", "turn-taking"], ["Recognize pre-verbal communication", "Practice joint attention activities", "Support language through turn-taking"]),
    "planning": ("Growing Into the Future", ["developmental milestones", "routines as plans", "parenting goals"], ["Set age-appropriate expectations", "Use routines as planning tools", "Reflect on your parenting journey"]),
}

_C101_MODULES = {
    "systems": ("Dynamical Systems and Markov Blankets", ["state space", "Markov blanket", "steady-state density"], ["Formalize systems using state spaces", "Define Markov blankets mathematically", "Derive steady-state conditions"]),
    "agents": ("Autonomous Agents and Generative Models", ["generative model", "recognition density", "variational inference"], ["Construct a simple generative model", "Distinguish generative from recognition models", "Explain variational inference"]),
    "perception": ("Predictive Processing and Bayesian Inference", ["prediction error", "Bayesian updating", "hierarchical models"], ["Derive Bayesian belief updating", "Implement a simple predictive coding model", "Explain hierarchical message passing"]),
    "cognition": ("Free Energy and Belief Optimization", ["variational free energy", "KL divergence", "ELBO"], ["Derive the free energy functional", "Relate KL divergence to surprise", "Compute ELBO for a simple model"]),
    "action": ("Active Inference and Expected Free Energy", ["expected free energy", "pragmatic value", "epistemic value"], ["Derive the EFE decomposition", "Implement policy selection", "Compare active inference to reinforcement learning"]),
    "learning": ("Structure Learning and Model Reduction", ["Dirichlet learning", "Bayesian model comparison", "Occam's window"], ["Implement parameter learning", "Perform Bayesian model comparison", "Apply Occam's principle to model selection"]),
    "communication": ("Multi-Agent Active Inference", ["shared generative models", "communication as inference", "social cognition"], ["Model multi-agent interactions", "Formalize communication as belief alignment", "Implement a simple social inference model"]),
    "planning": ("Planning as Inference and Deep Models", ["planning as inference", "deep temporal models", "sophisticated inference"], ["Implement planning as inference", "Build a deep temporal model", "Compare model-based and model-free approaches"]),
}

_C401_MODULES = {
    "systems": ("Non-Equilibrium Steady States and Random Dynamical Systems", ["NESS", "Fokker-Planck", "Langevin dynamics"], ["Derive the Fokker-Planck equation", "Analyze NESS conditions", "Relate NESS to biological self-organization"]),
    "agents": ("The Bayesian Brain and Markov Decision Processes", ["POMDP", "belief MDP", "information geometry"], ["Formalize agents as POMDPs", "Derive belief-space representations", "Apply information geometry to inference"]),
    "perception": ("Predictive Coding and Neural Process Theories", ["canonical microcircuits", "precision weighting", "empirical Bayes"], ["Derive predictive coding update rules", "Analyze precision dynamics in cortical columns", "Review empirical evidence for predictive coding"]),
    "cognition": ("Variational Methods and Free Energy Minimization", ["mean-field approximation", "Bethe free energy", "message passing algorithms"], ["Derive variational message passing", "Compare mean-field and Bethe approximations", "Implement belief propagation"]),
    "action": ("Path Integrals and Optimal Control", ["path integral control", "KL control", "stochastic optimal control"], ["Derive path integral formulations", "Connect KL control to active inference", "Analyze continuous-time active inference"]),
    "learning": ("Bayesian Mechanics and Structure Learning", ["Bayesian mechanics", "variational Laplacian", "model evidence"], ["Formalize Bayesian mechanics", "Derive structure learning from first principles", "Compute log model evidence for nested models"]),
    "communication": ("Collective Intelligence and Cultural Affordances", ["shared Markov blankets", "stigmergy", "epistemic communities"], ["Model collective inference", "Analyze stigmergic coordination", "Formalize cultural niche construction"]),
    "planning": ("Open Problems and Research Frontiers", ["scale-free inference", "consciousness", "artificial general intelligence"], ["Identify open mathematical problems", "Critically evaluate FEP scope claims", "Design a novel research proposal"]),
}

_EMBODIED_MODULES = {
    "systems": ("Feeling the Boundary of Your Skin", ["skin as boundary", "inside feeling", "grounding"], ["Feel where you end and the world begins", "Notice the sense of containment", "Practice grounding in your body"]),
    "agents": ("You Are the One Who Notices", ["presence", "aliveness", "intention"], ["Sense your own aliveness", "Notice the difference between doing and being done to", "Feel intention before movement"]),
    "perception": ("What Does Surprise Feel Like?", ["gut feeling", "startle", "felt sense"], ["Notice surprise in your body", "Distinguish thinking about from feeling", "Practice the felt sense check-in"]),
    "cognition": ("The Body Thinks Too", ["embodied knowing", "intuition", "somatic markers"], ["Access intuition through body awareness", "Notice somatic markers in decisions", "Practice thinking with the whole body"]),
    "action": ("Moving from the Inside Out", ["impulse", "flow", "expression"], ["Feel the impulse before the movement", "Practice flowing movement", "Express inner states through gesture"]),
    "learning": ("How the Body Remembers", ["muscle memory", "habit", "embodied wisdom"], ["Notice how the body stores learning", "Feel the difference between new and practiced", "Honor the body's accumulated wisdom"]),
    "communication": ("Resonance Between Bodies", ["attunement", "mirroring", "co-regulation"], ["Feel resonance with another person", "Practice mirroring exercises", "Experience co-regulation in pairs"]),
    "planning": ("Listening to What Wants to Happen", ["emergence", "readiness", "trust"], ["Sense what the body is ready for", "Practice emergent movement", "Trust the body's intelligence"]),
}

_ROBOTICS_MODULES = {
    "systems": ("Robotic Systems Architecture", ["sensors", "actuators", "embedded controllers"], ["Design a sensor-actuator architecture", "Implement a control loop on hardware", "Analyze system boundaries in robots"]),
    "agents": ("Embodied Agents and Morphological Computation", ["morphology", "body-brain coupling", "soft robotics"], ["Explain morphological computation", "Design a minimal cognitive agent", "Implement body-brain coupling"]),
    "perception": ("Sensor Fusion and State Estimation", ["Kalman filter", "sensor noise", "Bayesian fusion"], ["Implement a Kalman filter", "Fuse multi-modal sensor data", "Analyze noise models for common sensors"]),
    "cognition": ("Probabilistic World Models for Robots", ["occupancy grids", "factor graphs", "SLAM"], ["Build a probabilistic world model", "Implement a simple SLAM algorithm", "Use factor graphs for inference"]),
    "action": ("Active Inference Control", ["PID control", "model predictive control", "active inference controller"], ["Compare PID and active inference control", "Implement an MPC controller", "Design an active inference controller"]),
    "learning": ("Adaptive Robotics and Online Learning", ["adaptive control", "sim-to-real transfer", "lifelong learning"], ["Implement online parameter adaptation", "Analyze sim-to-real transfer challenges", "Design a lifelong learning architecture"]),
    "communication": ("Multi-Robot Coordination", ["swarm robotics", "consensus algorithms", "distributed inference"], ["Implement a consensus algorithm", "Design swarm coordination behaviors", "Analyze distributed active inference"]),
    "planning": ("Autonomous Navigation and Mission Planning", ["path planning", "task allocation", "human-robot interaction"], ["Implement a path planning algorithm", "Design a mission planning system", "Prototype a human-robot interaction loop"]),
}

_ORG_MODULES = {
    "systems": ("Organizations as Living Systems", ["organizational boundaries", "internal states", "homeostasis"], ["Map an organization as a Markov blanket", "Identify organizational steady states", "Analyze how firms maintain stability"]),
    "agents": ("Individual and Collective Agency", ["roles", "incentives", "organizational cognition"], ["Describe individual vs collective agency", "Map incentive structures as priors", "Analyze organizational decision-making"]),
    "perception": ("Market Signals and Environmental Scanning", ["signal detection", "competitive intelligence", "sense-making"], ["Analyze market signals as observations", "Design an environmental scanning process", "Apply sense-making frameworks"]),
    "cognition": ("Organizational Beliefs and Strategy", ["mental models", "strategic assumptions", "organizational learning"], ["Map an organization's mental model", "Identify strategic blind spots", "Design belief-updating processes"]),
    "action": ("Strategic Action and Implementation", ["strategic planning", "resource allocation", "execution risk"], ["Analyze actions as free energy minimization", "Design a resource allocation framework", "Assess execution risk using uncertainty"]),
    "learning": ("Organizational Learning and Adaptation", ["double-loop learning", "knowledge management", "innovation"], ["Apply double-loop learning models", "Design a knowledge management system", "Analyze innovation as exploration"]),
    "communication": ("Internal Communication and Culture", ["information flow", "culture as shared model", "team dynamics"], ["Map information flows in an organization", "Analyze culture as a shared generative model", "Design effective team communication"]),
    "planning": ("Futures Thinking and Organizational Resilience", ["scenario planning", "resilience", "adaptive strategy"], ["Conduct a scenario planning exercise", "Assess organizational resilience", "Design an adaptive strategy framework"]),
}


def _build_modules(table: dict) -> list[ModuleConfig]:
    """Build a list of 8 ModuleConfig instances from a module table."""
    modules = []
    for i, topic in enumerate(MODULE_TOPICS, 1):
        subtitle, concepts, goals = table[topic]
        modules.append(ModuleConfig(
            number=i, topic=topic, subtitle=subtitle,
            key_concepts=list(concepts), learning_goals=list(goals),
        ))
    return modules


def _build_courses(
    specs: list[tuple[str, str, str, str]], module_table: dict
) -> list[CourseConfig]:
    """Build 4 CourseConfig instances from specs and a shared module table.

    Args:
        specs: List of (dir_name, title, perspective, lab_type) tuples.
        module_table: Per-topic (subtitle, concepts, goals) dictionary.
    """
    courses = []
    for i, (dir_name, title, perspective, lab_type) in enumerate(specs, 1):
        courses.append(CourseConfig(
            number=i, dir_name=dir_name, title=title,
            perspective=perspective, lab_type=lab_type,
            modules=_build_modules(module_table),
        ))
    return courses


# ─── Age-Level Curricula ────────────────────────────────────────────────────

CURRICULUM_ES = CurriculumConfig(
    id="active_inference_es",
    title="Active Inference for Elementary School",
    audience="Grades K-5",
    tone="Wonder, play, storytime. No formulas. Drawings and songs.",
    courses=_build_courses([
        ("01_story_time", "Story Time", "Narrative & imagination", "Storytime Activity"),
        ("02_our_bodies", "Our Bodies", "Simple body science", "Drawing & Coloring Lab"),
        ("03_counting_patterns", "Counting & Patterns", "Shapes, sorting, counting", "Hands-On Puzzle"),
        ("04_robots_helpers", "Robots & Helpers", "Simple machines & digital helpers", "Build & Play"),
    ], _ES_MODULES),
)

CURRICULUM_MS = CurriculumConfig(
    id="active_inference_ms",
    title="Active Inference for Middle School",
    audience="Grades 6-8",
    tone="Curious, meme-aware, relatable. Light math (fractions, percentages). Scratch/block coding.",
    courses=_build_courses([
        ("01_real_life_skills", "Real Life Skills", "Everyday decision-making", "Group Challenge"),
        ("02_body_science", "Body Science", "Anatomy & health", "Investigation Lab"),
        ("03_math_detectives", "Math Detectives", "Probability as mystery-solving", "Guided Worksheet"),
        ("04_code_create", "Code & Create", "Block coding & simple Python", "Guided Coding Lab"),
    ], _MS_MODULES),
)

CURRICULUM_FAMILY = CurriculumConfig(
    id="active_inference_family",
    title="Active Inference for Families",
    audience="Families with babies and small children",
    tone="Warm, nurturing, practical parenting. No jargon. Focus on attachment, co-regulation, play.",
    courses=_build_courses([
        ("01_growing_together", "Growing Together", "Daily family life & routines", "Family Activity"),
        ("02_tiny_bodies_big_brains", "Tiny Bodies, Big Brains", "Infant/toddler development", "Observation Journal"),
        ("03_patterns_in_play", "Patterns in Play", "Counting, sorting with toys", "Play-Based Activity"),
        ("04_screens_toys_tools", "Screens, Toys & Tools", "Age-appropriate technology", "Parent-Child Activity"),
    ], _FAMILY_MODULES),
)

CURRICULUM_101 = CurriculumConfig(
    id="active_inference_101",
    title="Active Inference 101: College First Semester",
    audience="College 1st semester undergraduates",
    tone="Rigorous but accessible. Full mathematical notation. Python/NumPy. Textbook-quality.",
    courses=_build_courses([
        ("01_cognitive_science", "Cognitive Science", "Mind, brain, behavior", "Essay & Discussion"),
        ("02_computational_neuroscience", "Computational Neuroscience", "Neural circuits & Bayesian brain", "Simulation Lab"),
        ("03_mathematical_frameworks", "Mathematical Frameworks", "Probability, information theory, variational methods", "Problem Set"),
        ("04_implementation", "Implementation & Simulation", "Python, pymdp, agent-based modeling", "Coding Assignment"),
    ], _C101_MODULES),
)

CURRICULUM_401 = CurriculumConfig(
    id="active_inference_401",
    title="Active Inference 401: Advanced PhD Seminar",
    audience="Advanced PhD students and researchers",
    tone="Research-level. Dense mathematical formalism. Open questions. Paper discussions.",
    courses=_build_courses([
        ("01_philosophical_foundations", "Philosophical Foundations", "Epistemology, phenomenology, 4E cognition", "Seminar Discussion"),
        ("02_neuroscientific_frontiers", "Neuroscientific Frontiers", "Predictive processing, precision, neural dynamics", "Paper Review"),
        ("03_advanced_theory", "Advanced Theory", "Stochastic thermodynamics, Bayesian mechanics, path integrals", "Proof Workshop"),
        ("04_research_methods", "Research Methods", "Experimental design, model comparison, open problems", "Research Proposal"),
    ], _C401_MODULES),
)

# ─── Domain Curricula ──────────────────────────────────────────────────────

CURRICULUM_EMBODIED = CurriculumConfig(
    id="active_inference_embodied",
    title="Active Inference: Embodied Experience",
    audience="Anyone seeking qualitative, felt understanding",
    tone="Somatic, poetic, experiential. First-person felt sense. Meditative. Zero equations, zero code.",
    parent_dir="course_development/domains",
    courses=_build_courses([
        ("01_felt_sense", "Felt Sense", "Body awareness & interoception", "Somatic Exercise"),
        ("02_living_presence", "Living Presence", "Breath, heartbeat, embodied being", "Mindfulness Practice"),
        ("03_intuitive_knowing", "Intuitive Knowing", "Pattern-feeling without numbers", "Reflective Journaling"),
        ("04_moving_through_world", "Moving Through the World", "Dance, yoga, martial arts", "Movement Lab"),
    ], _EMBODIED_MODULES),
)

CURRICULUM_ROBOTICS = CurriculumConfig(
    id="active_inference_robotics",
    title="Active Inference for Robotics",
    audience="Robotics engineers and researchers",
    tone="Engineering-focused. Hardware + software. ROS2, sensor fusion, control theory.",
    parent_dir="course_development/domains",
    courses=_build_courses([
        ("01_robotic_systems", "Robotic Systems", "Sensors, actuators, embedded systems", "Hardware Lab"),
        ("02_bioinspired_design", "Bio-Inspired Design", "Biomimicry & neural architectures", "Design Challenge"),
        ("03_control_estimation", "Control & Estimation", "Kalman filters, PID, MPC, active inference", "Simulation Lab"),
        ("04_autonomous_agents", "Autonomous Agents", "SLAM, navigation, multi-robot coordination", "ROS2 Project"),
    ], _ROBOTICS_MODULES),
)

CURRICULUM_ORGANIZATIONS = CurriculumConfig(
    id="active_inference_organizations",
    title="Active Inference for Organizations",
    audience="Business leaders, managers, organizational scientists",
    tone="Business/management. Strategic planning, team dynamics, organizational cognition.",
    parent_dir="course_development/domains",
    courses=_build_courses([
        ("01_organizational_systems", "Organizational Systems", "Firms as adaptive systems", "Case Study"),
        ("02_collective_intelligence", "Collective Intelligence", "Teams, culture, shared mental models", "Workshop"),
        ("03_strategic_modeling", "Strategic Modeling", "Scenario planning, risk, decision frameworks", "Strategy Exercise"),
        ("04_digital_transformation", "Digital Transformation", "AI integration, data-driven organizations", "Implementation Plan"),
    ], _ORG_MODULES),
)

# ─── Registries ─────────────────────────────────────────────────────────────

AGE_LEVEL_CURRICULA: dict[str, CurriculumConfig] = {
    c.id: c for c in [
        CURRICULUM_ES, CURRICULUM_MS, CURRICULUM_FAMILY,
        CURRICULUM_101, CURRICULUM_401,
    ]
}

DOMAIN_CURRICULA: dict[str, CurriculumConfig] = {
    c.id: c for c in [
        CURRICULUM_EMBODIED, CURRICULUM_ROBOTICS, CURRICULUM_ORGANIZATIONS,
    ]
}

ALL_CURRICULA: dict[str, CurriculumConfig] = {
    **AGE_LEVEL_CURRICULA,
    **DOMAIN_CURRICULA,
}
