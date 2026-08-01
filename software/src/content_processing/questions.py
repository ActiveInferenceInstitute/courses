"""Study question generation logic.

Refactored from software/scripts/fix_stub_questions.py.
"""

import re
from pathlib import Path
from typing import Dict, List, Any

from src.content_processing.utils import get_audience_info

STUB_PATTERN = re.compile(r"and why does it matter", re.IGNORECASE)


def find_stub_questions(base: Path) -> List[Path]:
    """Find all questions.md files with template content."""
    stubs = []
    for qf in sorted(base.rglob("questions.md")):
        if "output" in qf.parts or "youtube" in qf.parts:
            continue
        text = qf.read_text(encoding="utf-8")
        if STUB_PATTERN.search(text):
            stubs.append(qf)
    return stubs


def generate_questions_content(module_data: Dict[str, Any], course_info: Dict[str, Any]) -> str:
    """Generate substantive study questions from module content."""
    concepts = module_data.get("key_concepts", [])
    objectives = module_data.get("objectives", [])
    title = module_data.get("title", f"Module {course_info['module_num']}")
    subtitle = module_data.get("subtitle", "")

    heading = subtitle or title
    topic = course_info["module_topic"].lower()

    # Get audience-specific details
    audience = get_audience_info(course_info["course"])
    level = audience["level"]

    lines = []
    lines.append(f"# Study Questions: {heading}\n")
    lines.append(
        f"> **Module {course_info['module_num']}** | **{course_info['unit']}** "
        f"| **{course_info['course_name']}**\n"
    )
    lines.append(
        "Use these questions to check your understanding of this module's key concepts. "
        "Try to answer each question from memory before reviewing your notes.\n"
    )
    lines.append("---\n")

    q_num = 1

    # ---- Section 1: Recall / Remember ----
    lines.append("## Recall and Define\n")

    # Generate recall questions from concepts
    for i, (name, defn) in enumerate(concepts[:4]):
        if level == "elementary":
            lines.append(f"### Question {q_num}\n")
            lines.append(
                f"Can you explain **{name}** in your own words? Use a real-life example.\n"
            )
        elif level == "middle":
            lines.append(f"### Question {q_num}\n")
            lines.append(
                f"Define **{name}** in your own words. What makes it different from related concepts?\n"
            )
        elif level in ("college", "graduate"):
            lines.append(f"### Question {q_num}\n")
            lines.append(
                f"Define **{name}** and explain its role in the Active Inference framework. "
                f"How does it relate to the broader goal of minimizing free energy?\n"
            )
        elif level == "practitioner":
            lines.append(f"### Question {q_num}\n")
            lines.append(
                f"Describe **{name}** in terms of bodily experience. "
                f"What does it feel like to encounter this concept in movement practice?\n"
            )
        elif level == "professional":
            lines.append(f"### Question {q_num}\n")
            lines.append(
                f"Define **{name}** and describe how it manifests in organizational behavior. "
                f"Give a specific workplace example.\n"
            )
        elif level == "technical":
            lines.append(f"### Question {q_num}\n")
            lines.append(
                f"Define **{name}** in both theoretical and computational terms. "
                f"How would you implement or measure this in a robotic system?\n"
            )
        else:
            lines.append(f"### Question {q_num}\n")
            lines.append(f"Define **{name}** and give an example from everyday experience.\n")
        q_num += 1

    lines.append("---\n")

    # ---- Section 2: Understand / Apply ----
    lines.append("## Understand and Apply\n")

    # Generate application questions from objectives
    for i, obj in enumerate(objectives[:3]):
        obj_clean = re.sub(r"^\*\*\w+\*\*\s*", "", obj)
        if level in ("elementary", "middle"):
            lines.append(f"### Question {q_num}\n")
            lines.append(f"Think about: *{obj_clean}*\n")
            lines.append("Give an example of how this works in your everyday life.\n")
        elif level in ("college", "graduate"):
            lines.append(f"### Question {q_num}\n")
            lines.append(f"Demonstrate your understanding: *{obj_clean}*\n")
            lines.append(
                "Construct a detailed example that illustrates this concept in action. "
                "Identify the key components (beliefs, predictions, observations, actions) at each step.\n"
            )
        elif level == "practitioner":
            lines.append(f"### Question {q_num}\n")
            lines.append(f"Consider: *{obj_clean}*\n")
            lines.append(
                "How have you experienced this in your own movement practice? "
                "Describe a specific moment when this became apparent.\n"
            )
        elif level == "professional":
            lines.append(f"### Question {q_num}\n")
            lines.append(f"Apply: *{obj_clean}*\n")
            lines.append(
                "Design a brief intervention or process change for your organization "
                "that leverages this concept. What would you measure to evaluate success?\n"
            )
        elif level == "technical":
            lines.append(f"### Question {q_num}\n")
            lines.append(f"Apply: *{obj_clean}*\n")
            lines.append(
                "Describe a robotic scenario where this capability is essential. "
                "What sensors, algorithms, and control strategies would be needed?\n"
            )
        else:
            lines.append(f"### Question {q_num}\n")
            lines.append(
                f"How would you apply the idea of *{obj_clean}* to a new situation? "
                f"Give a specific example.\n"
            )
        q_num += 1

    lines.append("---\n")

    # ---- Section 3: Analyze / Synthesize ----
    lines.append("## Analyze and Synthesize\n")

    # Connection questions between concepts
    if len(concepts) >= 2:
        c1, c2 = concepts[0][0], concepts[1][0]
        lines.append(f"### Question {q_num}\n")
        lines.append(
            f"How are **{c1}** and **{c2}** related? "
            f"Can you have one without the other? Explain your reasoning with a concrete example.\n"
        )
        q_num += 1

    # Cross-module connection
    lines.append(f"### Question {q_num}\n")
    lines.append(
        f"How does {topic} connect to what you learned in previous modules about "
        f"the Active Inference framework? Identify at least two specific connections.\n"
    )
    q_num += 1

    # Critical thinking
    if concepts:
        c_name = concepts[-1][0] if len(concepts) > 2 else concepts[0][0]
        lines.append(f"### Question {q_num}\n")
        if level in ("elementary", "middle"):
            lines.append(
                f"What would happen if **{c_name}** stopped working? "
                f"Think of a real example and describe the consequences.\n"
            )
        elif level in ("college", "graduate"):
            lines.append(
                f"What are the limitations of the Active Inference account of **{c_name}**? "
                f"Can you think of a situation where this framework might not fully explain "
                f"what is observed?\n"
            )
        elif level == "practitioner":
            lines.append(
                f"Describe a practice situation where **{c_name}** becomes paradoxical — "
                f"where trying harder to achieve it makes it less accessible. "
                f"How do experienced practitioners navigate this?\n"
            )
        elif level == "professional":
            lines.append(
                f"What organizational risks arise when **{c_name}** is poorly managed? "
                f"Give an example you have witnessed or can imagine, and propose a mitigation strategy.\n"
            )
        elif level == "technical":
            lines.append(
                f"What are the computational trade-offs of implementing **{c_name}** in real-time robotic systems? "
                f"Compare the requirements for offline vs. online processing.\n"
            )
        else:
            lines.append(
                f"What are the limitations of the concept of **{c_name}**? "
                f"When might it not apply?\n"
            )
        q_num += 1

    lines.append("---\n")

    # ---- Section 4: Reflect ----
    lines.append("## Reflect and Connect\n")

    lines.append(f"### Question {q_num}\n")
    if level == "elementary":
        lines.append(
            f"What was the most surprising thing you learned in this module about {topic}? Why did it surprise you?\n"
        )
    elif level == "middle":
        lines.append(
            f"Has this module changed how you think about {topic} in your daily life? "
            f"Give a specific example of something you now see differently.\n"
        )
    elif level in ("college", "graduate"):
        lines.append(
            f"If you were explaining {topic} to a friend who has never encountered Active Inference, "
            f"what central insight from this module would you start with, and why?\n"
        )
    elif level == "practitioner":
        lines.append(
            "What insight from this module could you integrate into your daily practice starting today? "
            "Be specific about what you would do differently.\n"
        )
    elif level == "professional":
        lines.append(
            "What is one organizational change, however small, that this module's insights suggest? "
            "How would you present this idea to a colleague who is unfamiliar with Active Inference?\n"
        )
    elif level == "technical":
        lines.append(
            f"What is the most promising application of {topic} for future robotic systems? "
            f"What technical barriers need to be overcome?\n"
        )
    else:
        lines.append(
            "What from this module do you want to learn more about? "
            "What questions remain unanswered for you?\n"
        )
    q_num += 1

    lines.append(f"### Question {q_num}\n")
    lines.append(
        "Rate your confidence in each of this module's learning objectives on a scale of 1-5. "
        "For any objective rated 3 or below, write one specific action you can take to improve your understanding.\n"
    )
    q_num += 1

    lines.append("---\n")

    lines.append(
        f"*These questions cover the key concepts from Module {course_info['module_num']}: "
        f"{heading}.*\n"
    )

    return "\n".join(lines)
