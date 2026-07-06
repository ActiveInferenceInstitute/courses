"""Lab generation logic from course content.

Refactored from software/scripts/fix_stub_labs.py.
"""

import re
from pathlib import Path
from typing import Any, Dict, List


STUB_PATTERN = re.compile(r"explore .* through hands-on engagement", re.IGNORECASE)


def find_stub_labs(base: Path) -> List[Path]:
    """Find all lab.md files with template/stub content."""
    stubs = []
    for lab in sorted(base.rglob("lab.md")):
        if "output" in lab.parts or "youtube" in lab.parts:
            continue
        try:
            text = lab.read_text(encoding="utf-8")
            if STUB_PATTERN.search(text):
                stubs.append(lab)
        except Exception:
            pass
    return stubs


from src.content_processing.utils import get_audience_info


def generate_lab_content(module_data: Dict[str, Any], course_info: Dict[str, Any]) -> str:
    """Generate a substantive lab from module content."""
    concepts = module_data.get("key_concepts", [])
    objectives = module_data.get("objectives", [])
    title = module_data.get("title", f"Module {course_info['module_num']}")
    subtitle = module_data.get("subtitle", "")
    overview = module_data.get("overview", "")
    summary = module_data.get("summary", "")
    subsections = module_data.get("subsections", [])

    audience = get_audience_info(course_info["course"])
    level = audience["level"]
    lab_heading = subtitle or title

    # Build materials list
    base_materials = [
        "Notebook or journal for recording observations",
        "Pen or pencil",
        "Access to this module's content ([module.md](./module.md))",
    ]

    if level == "elementary":
        base_materials.extend([
            "Colored pencils or crayons",
            "A partner or small group",
        ])
    elif level == "middle":
        base_materials.extend([
            "A partner for group activities",
            "Colored pens or markers (optional)",
        ])
    elif level in ("college", "graduate"):
        base_materials.extend([
            "A partner for discussion activities",
        ])
    elif level == "practitioner":
        base_materials.extend([
            "Comfortable clothing for movement",
            "A quiet space for practice",
        ])
    elif level == "professional":
        base_materials.extend([
            "Access to your organization's documentation or case studies",
        ])
    elif level == "technical":
        base_materials.extend([
            "Computer with Python or MATLAB (optional, for simulation)",
        ])

    materials_str = "\n".join(f"- {m}" for m in base_materials)

    # Build objective sentence
    lab_objectives = objectives[:3] if objectives else [
        f"explore the key concepts of {course_info['module_topic'].lower()}",
        "apply your understanding to real-world examples",
        f"reflect on how {course_info['module_topic'].lower()} connects to Active Inference",
    ]
    
    obj_sentence_parts = []
    for i, obj in enumerate(lab_objectives):
        # Clean leading verb emphasis
        obj_clean = re.sub(r"^\*\*\w+\*\*\s*", "", obj)
        obj_clean = obj_clean[0].lower() + obj_clean[1:] if obj_clean else obj
        obj_sentence_parts.append(obj_clean)

    obj_sentence = ", ".join(obj_sentence_parts[:-1])
    if len(obj_sentence_parts) > 1:
        obj_sentence += f", and {obj_sentence_parts[-1]}"
    else:
        obj_sentence = obj_sentence_parts[0] if obj_sentence_parts else "explore this module's key concepts"

    # ---- Generate lab parts based on content available ----
    lab_lines = []

    # Header
    lab_lines.append(f"# Lab: {lab_heading}\n")
    lab_lines.append(
        f"> **Module {course_info['module_num']}** | **{course_info['unit']}** "
        f"| **{course_info['course_name']}**"
    )
    lab_lines.append(f"> **Lab Type**: {audience['lab_style'].title()}\n")

    # Objective
    lab_lines.append("## Objective\n")
    lab_lines.append(
        f"In this lab, you will {obj_sentence}. "
        f"Through structured exercises and reflection, you will deepen your "
        f"understanding of how {course_info['module_topic'].lower()} operates "
        f"within the Active Inference framework.\n"
    )

    # Materials
    lab_lines.append("## Materials Needed\n")
    lab_lines.append(f"{materials_str}\n")
    lab_lines.append("---\n")

    # ---- PART 1: Concept Mapping / Exploration ----
    part_time = audience["part_times"][0]
    lab_lines.append(f"## Part 1: Concept Exploration ({part_time})\n")

    if concepts:
        if level == "elementary":
            lab_lines.append(
                "Look at the key ideas below. For each one, draw a picture or "
                "write one sentence that shows what it means.\n"
            )
            for i, (name, defn) in enumerate(concepts[:4]):
                lab_lines.append(f"**{i+1}. {name}**\n")
                lab_lines.append(f"*Hint*: {defn}\n")
                lab_lines.append("Your drawing or sentence: _______________________________________________\n")
        elif level == "middle":
            lab_lines.append(
                "For each key concept below, write a one-sentence definition in your own words "
                "and give a real-life example that you have personally experienced or observed.\n"
            )
            for i, (name, defn) in enumerate(concepts[:5]):
                lab_lines.append(f"**{i+1}. {name}**\n")
                lab_lines.append(f"- Module definition: {defn}")
                lab_lines.append("- Your definition: _______________________________________________")
                lab_lines.append("- Your example: _______________________________________________\n")
        elif level in ("college", "graduate"):
            lab_lines.append(
                "Create a concept map connecting the following key terms. "
                "Draw arrows between related concepts and label each arrow with "
                "the nature of the relationship (e.g., \"causes,\" \"is a type of,\" "
                "\"requires\").\n"
            )
            lab_lines.append("Key terms to include:\n")
            for name, defn in concepts[:6]:
                lab_lines.append(f"- **{name}**: {defn}")
            lab_lines.append("")
            lab_lines.append(
                "After building your map, identify which concept is most central "
                "(has the most connections) and write a one-paragraph explanation of why.\n"
            )
        elif level == "practitioner":
            lab_lines.append(
                "Begin in a comfortable standing or seated position. For each concept below, "
                "take 2-3 minutes to explore it through movement or stillness. "
                "Notice what arises in your body as you hold each idea.\n"
            )
            for i, (name, defn) in enumerate(concepts[:4]):
                lab_lines.append(f"**{i+1}. {name}**: {defn}\n")
                lab_lines.append(
                    "- What do you notice in your body when you consider this concept?")
                lab_lines.append(
                    "- Where do you feel it? What quality does it have?\n")
        elif level == "professional":
            lab_lines.append(
                "Consider each concept below in the context of your organization. "
                "For each one, identify a specific example from your professional experience.\n"
            )
            for i, (name, defn) in enumerate(concepts[:5]):
                lab_lines.append(f"**{i+1}. {name}**: {defn}\n")
                lab_lines.append("- Organizational example: _______________________________________________\n")
        elif level == "technical":
            lab_lines.append(
                "For each concept below, describe how it would be implemented "
                "or measured in a robotic system. Specify the relevant sensors, "
                "actuators, or algorithms.\n"
            )
            for i, (name, defn) in enumerate(concepts[:5]):
                lab_lines.append(f"**{i+1}. {name}**: {defn}\n")
                lab_lines.append("- Implementation approach: _______________________________________________\n")
        else:
            lab_lines.append(
                "Review the key concepts below. For each one, write a brief "
                "explanation and a real-world example.\n"
            )
            for i, (name, defn) in enumerate(concepts[:5]):
                lab_lines.append(f"**{i+1}. {name}**: {defn}\n")
                lab_lines.append("- Your example: _______________________________________________\n")
    else:
        # Fallback: use objectives
        lab_lines.append(
            "Review the module's learning objectives. For each one, "
            "rate your current understanding on a scale of 1-5 and "
            "note one specific question you still have.\n"
        )
        for i, obj in enumerate(objectives[:4]):
            lab_lines.append(f"**{i+1}.** {obj}\n")
            lab_lines.append("- Understanding (1-5): ___  Question: _______________________________________________\n")

    lab_lines.append("---\n")

    # ---- PART 2: Application / Investigation ----
    part_time = audience["part_times"][1]
    lab_lines.append(f"## Part 2: Application and Investigation ({part_time})\n")

    # Generate application exercises based on level and content
    if level == "elementary":
        c1 = concepts[0][0] if concepts else course_info["module_topic"].lower()
        c2 = concepts[1][0] if len(concepts) > 1 else "this idea"
        lab_lines.append(f"### Activity A: {c1} Detective\n")
        lab_lines.append(
            f"Look around your classroom, your home, or your playground. "
            f"Find three examples of **{c1}** in the real world. "
            f"For each example:\n"
        )
        lab_lines.append("1. Draw or describe what you found")
        lab_lines.append(f"2. Explain why it is an example of {c1}")
        lab_lines.append(f"3. What would happen if {c1} did not work in this example?\n")
        lab_lines.append("### Activity B: Teach a Friend\n")
        lab_lines.append(
            f"With a partner, take turns explaining **{c2}** using only "
            f"everyday words (no textbook language). Your partner should be "
            f"able to understand and repeat your explanation back to you.\n"
        )
    elif level == "middle":
        c1 = concepts[0][0] if concepts else course_info["module_topic"].lower()
        c2 = concepts[1][0] if len(concepts) > 1 else "this idea"
        lab_lines.append("### Exercise A: Real-World Analysis\n")
        lab_lines.append(
            f"Choose a situation from your daily life (at school, at home, with friends, "
            f"or in a hobby). Analyze it through the lens of **{c1}**:\n"
        )
        lab_lines.append("1. Describe the situation in 2-3 sentences")
        lab_lines.append(f"2. Identify where {c1} is at work")
        lab_lines.append("3. What predictions are being made? By whom or what?")
        lab_lines.append("4. What prediction errors might occur?\n")
        if len(concepts) > 1:
            lab_lines.append("### Exercise B: Compare and Contrast\n")
            lab_lines.append(
                f"Compare **{c1}** and **{c2}**. "
                f"Create a table or Venn diagram showing:\n"
            )
            lab_lines.append("- What they have in common")
            lab_lines.append("- How they differ")
            lab_lines.append("- How they work together in the Active Inference framework\n")
    elif level in ("college", "graduate"):
        c1 = concepts[0][0] if concepts else course_info["module_topic"].lower()
        lab_lines.append("### Exercise A: Case Analysis\n")
        lab_lines.append(
            f"Select a scenario relevant to {course_info['module_topic'].lower()} "
            f"(from the module content, from current research, or from your own experience). "
            f"Perform a structured analysis:\n"
        )
        lab_lines.append("1. **Describe** the scenario in 3-4 sentences")
        lab_lines.append("2. **Identify** the key Active Inference components at work "
                        "(generative model, prediction errors, belief updating, action selection)")
        lab_lines.append(f"3. **Analyze** how **{c1}** specifically operates in this scenario")
        lab_lines.append("4. **Predict** what would happen if one component were disrupted\n")
        if objectives:
            lab_lines.append("### Exercise B: Objective Deep-Dive\n")
            obj_focus = objectives[0] if objectives else f"understand {c1}"
            lab_lines.append(
                f"Choose the learning objective that you find most challenging: "
                f"*\"{obj_focus}\"*\n"
            )
            lab_lines.append(
                "Write a 200-word explanation of this objective as if you were "
                "teaching it to a classmate who missed this module. Include at "
                "least one concrete example and one potential misconception.\n"
            )
    elif level == "practitioner":
        c1 = concepts[0][0] if concepts else course_info["module_topic"].lower()
        lab_lines.append(f"### Practice A: Embodied Exploration of {c1}\n")
        lab_lines.append(
            f"Find a space where you can move freely. Spend 10 minutes exploring "
            f"**{c1}** through your body:\n"
        )
        lab_lines.append("1. Begin with simple, slow movements")
        lab_lines.append(f"2. Notice what {c1} feels like in your body")
        lab_lines.append("3. Gradually increase complexity or intensity")
        lab_lines.append(f"4. Find the edges — where does {c1} break down or transform?\n")
        lab_lines.append("Record your observations: What surprised you? What felt familiar?\n")
        lab_lines.append("### Practice B: Partner Mirror\n")
        lab_lines.append(
            f"With a partner, take turns leading and following movement. "
            f"The leader explores {c1} through movement while the follower mirrors. "
            f"After 5 minutes, switch roles. Discuss: How did the experience differ "
            f"between leading and following?\n"
        )
    elif level == "professional":
        c1 = concepts[0][0] if concepts else course_info["module_topic"].lower()
        lab_lines.append("### Exercise A: Organizational Mapping\n")
        lab_lines.append(
            f"Map how **{c1}** manifests in your organization:\n"
        )
        lab_lines.append(f"1. Identify 2-3 concrete instances where {c1} operates")
        lab_lines.append("2. For each instance, describe who is involved and what processes are affected")
        lab_lines.append("3. Rate the effectiveness of each instance (1-5) and explain your rating")
        lab_lines.append("4. Propose one improvement based on Active Inference principles\n")
        lab_lines.append("### Exercise B: Stakeholder Perspective\n")
        lab_lines.append(
            f"Choose one of the instances from Exercise A. Analyze it from "
            f"three different stakeholder perspectives (e.g., leadership, front-line "
            f"staff, customers/clients). How does each stakeholder's generative model "
            f"of {c1} differ? Where do prediction errors arise between perspectives?\n"
        )
    elif level == "technical":
        c1 = concepts[0][0] if concepts else course_info["module_topic"].lower()
        lab_lines.append("### Exercise A: System Design\n")
        lab_lines.append(
            f"Design a robotic system or subsystem that implements **{c1}**:\n"
        )
        lab_lines.append("1. **Sensors**: What information does the system need to acquire?")
        lab_lines.append(f"2. **Model**: What generative model would represent {c1}?")
        lab_lines.append("3. **Inference**: How does the system update its beliefs?")
        lab_lines.append("4. **Action**: What actions can the system take to minimize free energy?\n")
        lab_lines.append("Sketch a block diagram of your design.\n")
        lab_lines.append("### Exercise B: Comparative Analysis\n")
        if len(concepts) > 1:
            c2 = concepts[1][0]
            lab_lines.append(
                f"Compare two approaches to implementing {c1} and {c2} in a robotic system: "
                f"(a) a classical control approach, and (b) an Active Inference approach. "
                f"What are the trade-offs in terms of robustness, adaptability, and computational cost?\n"
            )
        else:
            lab_lines.append(
                f"Compare a classical control approach to {c1} with an Active Inference approach. "
                f"What are the trade-offs in terms of robustness, adaptability, and computational cost?\n"
            )
    else:
        c1 = concepts[0][0] if concepts else course_info["module_topic"].lower()
        lab_lines.append("### Exercise A: Real-World Observation\n")
        lab_lines.append(
            f"Find a real-world example of **{c1}** in your environment. "
            f"Describe it in detail, explaining how it connects to the "
            f"Active Inference framework.\n"
        )
        lab_lines.append("### Exercise B: Application\n")
        lab_lines.append(
            f"Apply your understanding of {c1} to a new context not discussed "
            f"in the module. Explain your reasoning step by step.\n"
        )

    lab_lines.append("---\n")

    # ---- PART 3: Reflection & Synthesis ----
    part_time = audience["part_times"][2]
    lab_lines.append(f"## Part 3: Reflection and Synthesis ({part_time})\n")

    lab_lines.append("Answer the following reflection questions in your lab journal:\n")

    # Generate reflection questions from concepts and objectives
    topic_lower = course_info["module_topic"].lower()
    refl_questions = []

    if concepts:
        c_name = concepts[0][0]
        refl_questions.append(
            f"How has your understanding of **{c_name}** changed after completing this lab?"
        )
    if len(concepts) > 1:
        c1, c2 = concepts[0][0], concepts[-1][0]
        refl_questions.append(
            f"What is the relationship between **{c1}** and **{c2}**? "
            f"How do they work together in the Active Inference framework?"
        )
    if objectives:
        refl_questions.append(
            "Which learning objective do you feel most confident about now? "
            "Which one still needs more work? Be specific about what you understand "
            "and what remains unclear."
        )

    refl_questions.append(
        f"How does {topic_lower} connect to what you learned in previous modules? "
        f"Identify at least one specific connection."
    )
    refl_questions.append(
        f"If you were to explain {topic_lower} to someone who has never heard of "
        f"Active Inference, what analogy or example would you use?"
    )

    for i, q in enumerate(refl_questions[:5]):
        lab_lines.append(f"**{i+1}.** {q}\n")

    lab_lines.append("---\n")

    # ---- Submission ----
    lab_lines.append("## Submission\n")
    if level == "elementary":
        lab_lines.append(
            "Share your drawings and observations with the class. "
            "Be ready to explain one thing you discovered during the lab.\n"
        )
    elif level == "middle":
        lab_lines.append(
            "Complete your lab journal entry with all exercises and reflection questions. "
            "Be prepared to share your real-world analysis with a small group.\n"
        )
    elif level in ("college", "graduate"):
        lab_lines.append(
            "Submit your completed concept map, case analysis, and reflection responses. "
            "Be prepared to discuss your analysis in a small-group session.\n"
        )
    elif level == "practitioner":
        lab_lines.append(
            "Record your observations and reflections in your practice journal. "
            "Be prepared to share one insight from your embodied exploration with the group.\n"
        )
    elif level == "professional":
        lab_lines.append(
            "Document your organizational mapping and stakeholder analysis. "
            "Be prepared to present your findings and improvement proposals to your team.\n"
        )
    elif level == "technical":
        lab_lines.append(
            "Submit your system design sketches, comparative analysis, and reflection responses. "
            "Include any code or pseudocode you developed during the exercises.\n"
        )
    else:
        lab_lines.append(
            "Complete your lab journal entry and be ready to share one insight with the group.\n"
        )

    lab_lines.append("---\n")
    lab_lines.append(
        f"*Lab for Module {course_info['module_num']}: "
        f"{lab_heading} ({audience['lab_style'].title()})*\n"
    )

    return "\n".join(lab_lines)
