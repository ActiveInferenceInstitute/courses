"""Content template rendering for course generation.

Produces substantive Markdown content for each file type
using the curriculum schema, without LLM calls.
"""

import logging
from .schema import CurriculumConfig, CourseConfig, ModuleConfig
from .utils import format_table_row, format_table_separator

logger = logging.getLogger("course_generator")


def render_module_md(
    module: ModuleConfig, course: CourseConfig, curriculum: CurriculumConfig
) -> str:
    """Render the main module.md lesson content.

    Args:
        module: Module configuration.
        course: Parent course configuration.
        curriculum: Top-level curriculum configuration.

    Returns:
        Complete Markdown string for module.md.
    """
    concepts_list = "\n".join(f"- **{c}**" for c in module.key_concepts)
    goals_list = "\n".join(
        f"{i}. {g}" for i, g in enumerate(module.learning_goals, 1)
    )

    return f"""# Module {module.number:02d}: {module.topic.title()}

## {module.subtitle}

> **Course**: {course.title} | **Curriculum**: {curriculum.title}
> **Audience**: {curriculum.audience}

## Overview

This module explores **{module.topic}** through the lens of {course.perspective.lower()}. \
As part of the {curriculum.title} curriculum, all content is designed for {curriculum.audience} \
with a tone that is {curriculum.tone.split('.')[0].lower().strip()}.

## Learning Goals

{goals_list}

## Key Concepts

{concepts_list}

## Lesson Content

### What is {module.topic.title()}?

In Active Inference, {module.topic} plays a central role in how agents interact with their \
environment. This module will build your understanding step by step, starting from intuition \
and building toward a deeper grasp of the concept.

### Core Idea

Every living system maintains itself by managing the boundary between what is "inside" and \
what is "outside." The concept of {module.topic} helps us understand how this process works \
at {_get_level_description(curriculum)}.

### Connections

This topic connects to the broader Active Inference framework:
- **Previous module**: {_get_adjacent_topic(module.number, -1)}
- **Next module**: {_get_adjacent_topic(module.number, 1)}

## Summary

In this module, you learned about {module.topic} from the perspective of {course.perspective.lower()}. \
The key takeaway is that {module.key_concepts[0] if module.key_concepts else module.topic} \
is fundamental to understanding how agents navigate their world.

## Further Reading

See [References](../../resources/references.md) and [Glossary](../../resources/glossary.md) \
for additional resources on {module.topic}.
"""


def render_questions_md(
    module: ModuleConfig, course: CourseConfig, curriculum: CurriculumConfig
) -> str:
    """Render the questions.md study questions file.

    Args:
        module: Module configuration.
        course: Parent course configuration.
        curriculum: Top-level curriculum configuration.

    Returns:
        Complete Markdown string for questions.md.
    """
    questions = _generate_questions(module, course, curriculum)
    q_list = "\n\n".join(
        f"### Question {i}\n\n{q}" for i, q in enumerate(questions, 1)
    )

    return f"""# Study Questions: {module.topic.title()}

> **Module {module.number:02d}** | **{course.title}** | **{curriculum.title}**

Use these questions to check your understanding of {module.topic}. \
Try to answer each one before looking at your notes.

{q_list}

---

*These questions cover the key concepts from Module {module.number:02d}: {module.subtitle}.*
"""


def render_quiz_md(
    module: ModuleConfig, course: CourseConfig, curriculum: CurriculumConfig
) -> str:
    """Render the practice_quiz.md file with MC and short-answer questions.

    Args:
        module: Module configuration.
        course: Parent course configuration.
        curriculum: Top-level curriculum configuration.

    Returns:
        Complete Markdown string for practice_quiz.md.
    """
    mc_questions = _generate_mc_questions(module, course, curriculum)
    mc_section = "\n\n".join(
        f"### {i}. {q['stem']}\n\n"
        + "\n".join(f"- {opt}" for opt in q["options"])
        for i, q in enumerate(mc_questions, 1)
    )

    return f"""# Practice Quiz: {module.topic.title()}

> **Module {module.number:02d}** | **{course.title}** | **{curriculum.title}**

## Part A: Multiple Choice

{mc_section}

## Part B: Short Answer

### 1. Define {module.key_concepts[0] if module.key_concepts else module.topic} in your own words.

### 2. Give an example of {module.topic} from {course.perspective.lower()}.

### 3. Explain how {module.topic} connects to the overall Active Inference framework.

---

*This quiz covers Module {module.number:02d}: {module.subtitle}.*
"""


def render_lab_md(
    module: ModuleConfig, course: CourseConfig, curriculum: CurriculumConfig
) -> str:
    """Render the lab.md hands-on activity file.

    Args:
        module: Module configuration.
        course: Parent course configuration.
        curriculum: Top-level curriculum configuration.

    Returns:
        Complete Markdown string for lab.md.
    """
    return f"""# Lab: {module.subtitle}

> **Module {module.number:02d}** | **{course.title}** | **{curriculum.title}**
> **Lab Type**: {course.lab_type}

## Objective

In this {course.lab_type.lower()}, you will explore {module.topic} through \
hands-on engagement with {course.perspective.lower()}.

## Materials Needed

- Notebook or journal for recording observations
- Writing/drawing materials
- Access to this module's content ([module.md](./module.md))

## Instructions

### Part 1: Exploration (15 minutes)

Begin by reviewing the key concepts of {module.topic}:
{chr(10).join(f"- {c}" for c in module.key_concepts)}

Think about how each concept appears in your own experience.

### Part 2: Investigation (20 minutes)

Choose one of the following activities:

1. **Observe**: Find a real-world example of {module.key_concepts[0] if module.key_concepts else module.topic} \
and describe it in detail.
2. **Create**: Make a diagram, drawing, or model that illustrates {module.topic}.
3. **Discuss**: With a partner, explain {module.topic} using only everyday language.

### Part 3: Reflection (10 minutes)

Answer the following reflection questions:

1. What was the most surprising thing you learned about {module.topic}?
2. How does {module.topic} connect to what you learned in previous modules?
3. Where do you see {module.topic} in your daily life?

## Submission

Complete your lab journal entry and be ready to share one insight with the group.

---

*Lab for Module {module.number:02d}: {module.subtitle} ({course.lab_type})*
"""


def render_readme_md(
    module: ModuleConfig, course: CourseConfig, curriculum: CurriculumConfig
) -> str:
    """Render the per-module README.md navigation file.

    Args:
        module: Module configuration.
        course: Parent course configuration.
        curriculum: Top-level curriculum configuration.

    Returns:
        Complete Markdown string for README.md.
    """
    file_rows = [
        format_table_row(["File", "Description"]),
        format_table_separator(2),
        format_table_row(["[module.md](./module.md)", f"Full lecture ({module.subtitle})"]),
        format_table_row(["[questions.md](./questions.md)", "20 Study Questions"]),
        format_table_row(["[practice_quiz.md](./practice_quiz.md)", "Practice Quiz (MC + Short Answer)"]),
        format_table_row(["[lab.md](./lab.md)", f"Lab: {module.subtitle}"]),
        format_table_row(["[dashboard.html](./dashboard.html)", "Interactive Dashboard"]),
    ]
    file_table = "\n".join(file_rows)

    goals_list = "\n".join(
        f"{i}. **{g.split()[0]}** {' '.join(g.split()[1:])}"
        for i, g in enumerate(module.learning_goals, 1)
    )

    return f"""# Module {module.number:02d}: {module.topic.title()}

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## {module.subtitle}

Part of **{course.title}**.

## Contents

{file_table}

## Learning Goals

{goals_list}

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
"""


def render_agents_md(
    module: ModuleConfig, course: CourseConfig, curriculum: CurriculumConfig
) -> str:
    """Render the per-module AGENTS.md conventions file.

    Args:
        module: Module configuration.
        course: Parent course configuration.
        curriculum: Top-level curriculum configuration.

    Returns:
        Complete Markdown string for AGENTS.md.
    """
    return f"""# Station: {module.topic.title()} ({course.title})

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: {course.perspective}
- **Topics**: {module.topic.title()}
- **Lab Style**: {course.lab_type}
- **Audience**: {curriculum.audience}
- **Tone**: {curriculum.tone.split('.')[0].strip()}

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
"""


def render_dashboard_html(
    module: ModuleConfig, course: CourseConfig, curriculum: CurriculumConfig
) -> str:
    """Render the interactive dashboard.html file.

    Args:
        module: Module configuration.
        course: Parent course configuration.
        curriculum: Top-level curriculum configuration.

    Returns:
        Complete HTML string for dashboard.html.
    """
    concept_cards = "\n".join(
        f'            <div class="card" onclick="this.classList.toggle(\'flipped\')">'
        f'<div class="front">{c}</div>'
        f'<div class="back">Part of {module.topic} in {course.title}</div></div>'
        for c in module.key_concepts
    )

    quiz_items = _generate_mc_questions(module, course, curriculum)
    quiz_js_data = ",".join(
        f'{{"q":"{q["stem"]}","a":{q.get("answer_idx", 0)}}}'
        for q in quiz_items[:3]
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module {module.number:02d}: {module.topic.title()} — {course.title}</title>
    <style>
        :root {{ --accent: #6366f1; --bg: #0f172a; --card: #1e293b; --text: #e2e8f0; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Inter', system-ui, sans-serif; background: var(--bg); color: var(--text); padding: 2rem; }}
        h1 {{ background: linear-gradient(135deg, var(--accent), #a78bfa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem; }}
        .subtitle {{ color: #94a3b8; margin-bottom: 2rem; }}
        .section {{ background: var(--card); border-radius: 1rem; padding: 1.5rem; margin-bottom: 1.5rem; }}
        .cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; }}
        .card {{ background: linear-gradient(135deg, #312e81, #1e1b4b); border-radius: 0.75rem; padding: 1.25rem; cursor: pointer; transition: transform 0.3s, box-shadow 0.3s; text-align: center; min-height: 100px; display: flex; align-items: center; justify-content: center; }}
        .card:hover {{ transform: translateY(-4px); box-shadow: 0 8px 25px rgba(99,102,241,0.3); }}
        .card .back {{ display: none; font-size: 0.85rem; color: #a5b4fc; }}
        .card.flipped .front {{ display: none; }}
        .card.flipped .back {{ display: flex; align-items: center; justify-content: center; }}
        .nav {{ display: flex; gap: 1rem; margin-top: 2rem; }}
        .nav a {{ color: var(--accent); text-decoration: none; padding: 0.5rem 1rem; border: 1px solid var(--accent); border-radius: 0.5rem; transition: all 0.3s; }}
        .nav a:hover {{ background: var(--accent); color: white; }}
        .goals li {{ margin: 0.5rem 0; padding-left: 0.5rem; }}
    </style>
</head>
<body>
    <h1>Module {module.number:02d}: {module.topic.title()}</h1>
    <p class="subtitle">{module.subtitle} — {course.title} ({curriculum.title})</p>

    <div class="section">
        <h2>🎯 Learning Goals</h2>
        <ul class="goals">
            {"".join(f"<li>{g}</li>" for g in module.learning_goals)}
        </ul>
    </div>

    <div class="section">
        <h2>💡 Key Concepts (click to flip)</h2>
        <div class="cards">
{concept_cards}
        </div>
    </div>

    <div class="nav">
        <a href="./module.md">📖 Lesson</a>
        <a href="./questions.md">❓ Questions</a>
        <a href="./practice_quiz.md">📝 Quiz</a>
        <a href="./lab.md">🔬 Lab</a>
        <a href="../README.md">⬆ Course</a>
        <a href="../../README.md">🏠 Home</a>
    </div>

    <script>
        const quizData = [{quiz_js_data}];
    </script>
</body>
</html>"""


# ─── Course-level content ──────────────────────────────────────────────────

def render_course_readme(
    course: CourseConfig, curriculum: CurriculumConfig
) -> str:
    """Render the per-course README.md."""
    mod_rows = [
        format_table_row(["#", "Topic", "Subtitle", "Lab Type"]),
        format_table_separator(4),
    ]
    for m in course.modules:
        mod_rows.append(format_table_row([
            str(m.number),
            f"[{m.topic.title()}](./{m.dir_name}/README.md)",
            m.subtitle,
            course.lab_type,
        ]))
    mod_table = "\n".join(mod_rows)

    return f"""# {course.title}

> Part of **{curriculum.title}** | [Curriculum Home](../README.md)

## Overview

**{course.title}** explores Active Inference through the lens of {course.perspective.lower()}. \
This course is designed for {curriculum.audience}.

**Tone**: {curriculum.tone}

## Modules

{mod_table}

## Files Per Module

| File | Description |
| --- | --- |
| module.md | Full lesson content |
| questions.md | Study questions |
| practice_quiz.md | Practice quiz |
| lab.md | {course.lab_type} |
| dashboard.html | Interactive dashboard |
| README.md | Navigation and overview |
| AGENTS.md | Conventions and metadata |

## Resources

- [Glossary](../resources/glossary.md)
- [Notation Table](../resources/notation_table.md)
- [References](../resources/references.md)
- [Cross-Course Map](../resources/cross_course_map.md)
"""


def render_course_agents(
    course: CourseConfig, curriculum: CurriculumConfig
) -> str:
    """Render the per-course AGENTS.md."""
    return f"""# Course AGENTS: {course.title}

> **Quick Navigation**: [Course README](./README.md) | [Curriculum AGENTS](../AGENTS.md)

## Identity

- **Course**: {course.title}
- **Number**: {course.number}
- **Perspective**: {course.perspective}
- **Lab Type**: {course.lab_type}
- **Audience**: {curriculum.audience}
- **Tone**: {curriculum.tone}

## Conventions

All modules in this course must:

1. Use language appropriate for {curriculum.audience}.
2. Frame all concepts through the lens of {course.perspective.lower()}.
3. Include {course.lab_type.lower()} activities.
4. Adhere to notation standards in [../resources/notation_table.md](../resources/notation_table.md).
5. Cross-reference the shared [../resources/glossary.md](../resources/glossary.md).
"""


def render_course_syllabus(
    course: CourseConfig, curriculum: CurriculumConfig
) -> str:
    """Render the per-course syllabus.md."""
    schedule = "\n".join(
        f"| Week {m.number} | [{m.topic.title()}](./{m.dir_name}/module.md) "
        f"| {m.subtitle} | {course.lab_type} |"
        for m in course.modules
    )

    return f"""# Syllabus: {course.title}

> **{curriculum.title}** | **Audience**: {curriculum.audience}

## Course Description

{course.title} explores Active Inference through {course.perspective.lower()}. \
Over 8 modules, students will build a comprehensive understanding of how living \
systems perceive, think, act, and learn.

## Schedule

| Week | Module | Topic | Activity |
| --- | --- | --- | --- |
{schedule}

## Assessment

Each module includes:
- **Study Questions** (questions.md) — self-assessment
- **Practice Quiz** (practice_quiz.md) — formative evaluation
- **Lab Activity** (lab.md) — {course.lab_type.lower()}

## Resources

- [Glossary](../resources/glossary.md)
- [Notation Table](../resources/notation_table.md)
- [References](../resources/references.md)
"""


# ─── Root-level content ────────────────────────────────────────────────────

def render_root_readme(curriculum: CurriculumConfig) -> str:
    """Render the curriculum-level README.md."""
    course_rows = [
        format_table_row(["#", "Course", "Perspective", "Lab Type"]),
        format_table_separator(4),
    ]
    for c in curriculum.courses:
        course_rows.append(format_table_row([
            str(c.number),
            f"[{c.title}](./{c.dir_name}/README.md)",
            c.perspective,
            c.lab_type,
        ]))
    course_table = "\n".join(course_rows)

    return f"""# {curriculum.title}

> **Audience**: {curriculum.audience}
> **Estimated files**: {curriculum.total_files}

## Overview

Welcome to **{curriculum.title}**. This curriculum teaches Active Inference — \
the theory that all living systems work by constantly predicting and acting \
to minimize surprise.

**Tone**: {curriculum.tone}

## Courses

{course_table}

## Curriculum Structure

Each course contains **8 modules** following the Active Inference topic spine:
Systems → Agents → Perception → Cognition → Action → Learning → Communication → Planning

Each module contains 7 files: lesson, study questions, practice quiz, lab, \
dashboard, README, and AGENTS.

## Resources

- [Glossary](./resources/glossary.md) — Key terms and definitions
- [Notation Table](./resources/notation_table.md) — Symbols and notation
- [References](./resources/references.md) — Reading list
- [Cross-Course Map](./resources/cross_course_map.md) — How modules connect
- [Learning Pathways](./resources/learning_pathways.md) — Suggested routes
- [FAQ](./resources/faq.md) — Frequently asked questions

## Quick Start

1. Choose a course based on your interest.
2. Start with Module 01 (Systems) and work through sequentially.
3. Use the dashboard for interactive review.
4. Complete the lab for hands-on practice.
"""


def render_root_overview(curriculum: CurriculumConfig) -> str:
    """Render the curriculum-level OVERVIEW.md."""
    course_sections = "\n\n".join(
        f"### Course {c.number}: {c.title}\n\n"
        f"**Perspective**: {c.perspective}\n\n"
        f"Modules: " + ", ".join(
            f"[{m.topic.title()}](./{c.dir_name}/{m.dir_name}/README.md)"
            for m in c.modules
        )
        for c in curriculum.courses
    )

    return f"""# {curriculum.title} — Pedagogical Overview

## Vision

This curriculum makes Active Inference accessible to {curriculum.audience} \
through four complementary lenses. Each course covers the same 8 foundational \
topics but from a different disciplinary perspective.

## Tone & Style

{curriculum.tone}

## Course Map

{course_sections}

## Cross-Course Connections

The same 8 topics appear in every course, building a spiral of understanding. \
See [Cross-Course Map](./resources/cross_course_map.md) for detailed connections.

## How to Use This Curriculum

- **Sequential**: Work through one course start to finish.
- **Parallel**: Study the same module across all 4 courses.
- **Exploratory**: Use the [Learning Pathways](./resources/learning_pathways.md).
"""


def render_root_agents(curriculum: CurriculumConfig) -> str:
    """Render the curriculum-level AGENTS.md."""
    return f"""# AGENTS: {curriculum.title}

## Identity

- **Curriculum**: {curriculum.title}
- **ID**: {curriculum.id}
- **Audience**: {curriculum.audience}
- **Courses**: {len(curriculum.courses)}
- **Modules per course**: 8
- **Total estimated files**: {curriculum.total_files}

## Critical Rules

1. **Audience first**: All content must be appropriate for {curriculum.audience}.
2. **Tone**: {curriculum.tone}
3. **No placeholders**: Every file must contain substantive content.
4. **Shared resources**: Always consult `resources/` before writing.
5. **Cross-references**: Link to glossary and notation table.
6. **Spiral learning**: The 8-topic spine repeats across all 4 courses.

## Notation Standards

See [resources/notation_table.md](./resources/notation_table.md).

## Content Format

- **module.md**: Full lesson (500-1500 words depending on level)
- **questions.md**: 10-20 study questions
- **practice_quiz.md**: MC + short answer
- **lab.md**: Hands-on activity ({', '.join(c.lab_type for c in curriculum.courses)})
- **dashboard.html**: Interactive concept cards and quiz
- **README.md**: Navigation hub
- **AGENTS.md**: Maintenance conventions
"""


def render_audit_script(curriculum: CurriculumConfig) -> str:
    """Render the audit_modules.sh verification script."""
    course_checks = "\n".join(
        f'check_course "{c.dir_name}" "{c.title}"'
        for c in curriculum.courses
    )

    return f"""#!/usr/bin/env bash
# Audit script for {curriculum.title}
# Verifies structural completeness of all modules.

set -euo pipefail

PASS=0; FAIL=0; WARN=0

check_file() {{
    if [ -f "$1" ]; then
        PASS=$((PASS + 1))
    else
        echo "  FAIL: Missing $1"
        FAIL=$((FAIL + 1))
    fi
}}

check_module() {{
    local dir="$1"
    for f in module.md questions.md practice_quiz.md lab.md dashboard.html README.md AGENTS.md; do
        check_file "$dir/$f"
    done
}}

check_course() {{
    local course_dir="$1"
    local course_name="$2"
    echo "--- Course: $course_name ---"
    check_file "$course_dir/README.md"
    check_file "$course_dir/AGENTS.md"
    check_file "$course_dir/syllabus.md"
    for mod_dir in "$course_dir"/[0-9][0-9]_*/; do
        [ -d "$mod_dir" ] && check_module "$mod_dir"
    done
}}

echo "=== {curriculum.title} Audit ==="
echo ""

echo "--- Root-level files ---"
check_file "README.md"
check_file "OVERVIEW.md"
check_file "AGENTS.md"

echo "--- Resource files ---"
for f in glossary.md notation_table.md references.md cross_course_map.md learning_pathways.md faq.md README.md AGENTS.md; do
    check_file "resources/$f"
done

{course_checks}

echo ""
echo "--- Placeholder Check ---"
if grep -r "\\[TODO\\]\\|\\[PLACEHOLDER\\]\\|TBD\\|FIXME" --include="*.md" . 2>/dev/null | grep -v AGENTS.md | grep -v audit_modules.sh; then
    echo "  WARN: Placeholders found!"
    WARN=$((WARN + 1))
else
    echo "  No placeholders found (excluding guidelines)."
fi

echo ""
echo "=== Audit Summary ==="
echo "  PASS: $PASS"
echo "  FAIL: $FAIL"
echo "  WARN: $WARN"
if [ $FAIL -eq 0 ]; then
    echo "  STATUS: PASSED"
else
    echo "  STATUS: FAILED"
    exit 1
fi
"""


# ─── Resource content ──────────────────────────────────────────────────────

def render_resource_glossary(curriculum: CurriculumConfig) -> str:
    """Render the resources/glossary.md file."""
    # Collect all unique concepts across all courses
    all_concepts: list[str] = []
    for course in curriculum.courses:
        for module in course.modules:
            all_concepts.extend(module.key_concepts)
    unique = sorted(set(all_concepts))

    entries = "\n\n".join(
        f"### {term.title()}\n\n"
        f"A key concept in Active Inference related to {term.lower()}. "
        f"See the relevant module for a full explanation."
        for term in unique
    )

    return f"""# Glossary: {curriculum.title}

> Definitions of key terms used throughout the curriculum.
> Designed for {curriculum.audience}.

{entries}
"""


def render_resource_notation(curriculum: CurriculumConfig) -> str:
    """Render the resources/notation_table.md file."""
    return f"""# Notation Table: {curriculum.title}

> Standard symbols and notation used throughout the curriculum.
> Level: {curriculum.audience}

## Core Symbols

| Symbol | Plain English | Formal Meaning | First Introduced |
| --- | --- | --- | --- |
| System | A thing with a boundary | An entity with internal and external states | Course 1, M1 |
| Agent | Something that acts | A system that minimizes free energy | Course 1, M2 |
| Prediction | A guess about what will happen | Expected sensory input | Course 1, M3 |
| Surprise | When reality ≠ expectation | Negative log probability | Course 1, M3 |
| Action | Making something happen | Changing the world to match predictions | Course 1, M5 |
| Learning | Getting better | Updating model parameters | Course 1, M6 |

## Navigation

- [Glossary](./glossary.md)
- [References](./references.md)
- [Home](../README.md)
"""


def render_resource_references(curriculum: CurriculumConfig) -> str:
    """Render the resources/references.md file."""
    return f"""# References: {curriculum.title}

> Recommended reading and resources for {curriculum.audience}.

## Foundational

1. Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.
2. Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press.

## Further Reading

3. Clark, A. (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. *Behavioral and Brain Sciences*, 36(3), 181-204.
4. Hohwy, J. (2013). *The Predictive Mind*. Oxford University Press.
5. Seth, A. K. (2021). *Being You: A New Science of Consciousness*. Penguin.

## Online Resources

- [Active Inference Institute](https://activeinference.org/)
- [Active Inference Journal](https://activeinferencejournal.org/)

## Navigation

- [Glossary](./glossary.md)
- [Notation Table](./notation_table.md)
- [Home](../README.md)
"""


def render_resource_cross_course_map(curriculum: CurriculumConfig) -> str:
    """Render the resources/cross_course_map.md file."""
    from .schema import MODULE_TOPICS

    sections = []
    for topic in MODULE_TOPICS:
        rows = [
            format_table_row(["Course", "Subtitle", "Key Concepts", "Link"]),
            format_table_separator(4),
        ]
        for course in curriculum.courses:
            mod = next((m for m in course.modules if m.topic == topic), None)
            if mod:
                concepts = ", ".join(mod.key_concepts[:3])
                link = f"[Go](../{course.dir_name}/{mod.dir_name}/README.md)"
                rows.append(format_table_row([
                    course.title, mod.subtitle, concepts, link,
                ]))
        table = "\n".join(rows)
        sections.append(f"## Module {MODULE_TOPICS.index(topic)+1}: {topic.title()}\n\n{table}")

    body = "\n\n---\n\n".join(sections)

    return f"""# Cross-Course Map: {curriculum.title}

> How the same topic is taught across all 4 courses.

{body}
"""


def render_resource_learning_pathways(curriculum: CurriculumConfig) -> str:
    """Render the resources/learning_pathways.md file."""
    return f"""# Learning Pathways: {curriculum.title}

> Suggested routes through the curriculum for {curriculum.audience}.

## Pathway 1: Sequential (Recommended)

Complete one course fully before starting the next:

1. {curriculum.courses[0].title if curriculum.courses else "Course 1"}
2. {curriculum.courses[1].title if len(curriculum.courses) > 1 else "Course 2"}
3. {curriculum.courses[2].title if len(curriculum.courses) > 2 else "Course 3"}
4. {curriculum.courses[3].title if len(curriculum.courses) > 3 else "Course 4"}

## Pathway 2: Parallel (Comparative)

Study the same module across all courses:

For each module 1-8, read the lesson in all 4 courses before moving on.

## Pathway 3: Interest-Driven

Start with whichever course matches your interest, then explore connections.

## Navigation

- [Cross-Course Map](./cross_course_map.md)
- [Home](../README.md)
"""


def render_resource_faq(curriculum: CurriculumConfig) -> str:
    """Render the resources/faq.md file."""
    return f"""# FAQ: {curriculum.title}

> Frequently asked questions for {curriculum.audience}.

## What is Active Inference?

Active Inference is a theory from neuroscience that says all living things work by \
making predictions about the world and then acting to make those predictions come true.

## Who is this curriculum for?

This curriculum is designed for **{curriculum.audience}**.

## How should I use this curriculum?

See [Learning Pathways](./learning_pathways.md) for suggested routes.

## What are the 8 modules about?

1. **Systems** — What is a system and where are its boundaries?
2. **Agents** — What makes something an agent?
3. **Perception** — How do we sense the world?
4. **Cognition** — How do we think and form beliefs?
5. **Action** — How do we act on the world?
6. **Learning** — How do we get better over time?
7. **Communication** — How do we share with others?
8. **Planning** — How do we think about the future?

## Navigation

- [Glossary](./glossary.md)
- [Home](../README.md)
"""


def render_resource_readme(curriculum: CurriculumConfig) -> str:
    """Render the resources/README.md file."""
    return f"""# Shared Resources: {curriculum.title}

> Centralized reference materials for the entire curriculum.

## Contents

| File | Description |
| --- | --- |
| [glossary.md](./glossary.md) | Key terms and definitions |
| [notation_table.md](./notation_table.md) | Symbols and notation |
| [references.md](./references.md) | Reading list |
| [cross_course_map.md](./cross_course_map.md) | How modules connect across courses |
| [learning_pathways.md](./learning_pathways.md) | Suggested learning routes |
| [faq.md](./faq.md) | Frequently asked questions |

## Navigation

- [Curriculum Home](../README.md)
"""


def render_resource_agents(curriculum: CurriculumConfig) -> str:
    """Render the resources/AGENTS.md file."""
    return f"""# AGENTS: Shared Resources

> **Quick Navigation**: [Resources README](./README.md) | [Curriculum AGENTS](../AGENTS.md)

## Purpose

These shared resources serve as the single source of truth for terminology, \
notation, and references across all courses in {curriculum.title}.

## Maintenance Rules

1. Update the glossary when new terms are introduced in any module.
2. Keep the notation table synchronized with all courses.
3. Verify cross-course map links after any structural changes.
4. All tables must use proper MD060-compliant formatting (spaces around pipes).
"""


# ─── Private helpers ────────────────────────────────────────────────────────

def _get_level_description(curriculum: CurriculumConfig) -> str:
    """Get a level-appropriate description for lesson content."""
    level_map = {
        "active_inference_es": "a level that young learners can connect with through stories and play",
        "active_inference_ms": "a level that connects to everyday teen experiences",
        "active_inference_family": "a level that helps parents understand their children's development",
        "active_inference_101": "an introductory college level with formal mathematical foundations",
        "active_inference_401": "an advanced research level with rigorous mathematical formalism",
        "active_inference_embodied": "a deeply felt, experiential level through the body",
        "active_inference_robotics": "an engineering level with hardware and software implementation",
        "active_inference_organizations": "a strategic management level with business applications",
    }
    return level_map.get(curriculum.id, "an appropriate level for the audience")


def _get_adjacent_topic(module_number: int, offset: int) -> str:
    """Get the topic name of an adjacent module."""
    from .schema import MODULE_TOPICS
    idx = module_number - 1 + offset
    if 0 <= idx < len(MODULE_TOPICS):
        return MODULE_TOPICS[idx].title()
    return "N/A (this is the first/last module)"


def _generate_questions(
    module: ModuleConfig, course: CourseConfig, curriculum: CurriculumConfig
) -> list[str]:
    """Generate study questions based on module concepts."""
    questions = []
    for concept in module.key_concepts:
        questions.append(f"What is {concept} and why does it matter for {module.topic}?")
        questions.append(f"Give an example of {concept} from {course.perspective.lower()}.")
    for goal in module.learning_goals:
        questions.append(f"In your own words, {goal.lower()}.")
    # Pad to at least 10
    while len(questions) < 10:
        questions.append(
            f"How does {module.topic} connect to other concepts in Active Inference?"
        )
    return questions[:20]


def _generate_mc_questions(
    module: ModuleConfig, course: CourseConfig, curriculum: CurriculumConfig
) -> list[dict]:
    """Generate multiple-choice questions for quizzes and dashboards."""
    questions = []
    if module.key_concepts:
        questions.append({
            "stem": f"Which of the following best describes {module.key_concepts[0]}?",
            "options": [
                f"A) A core concept in {module.topic}",
                "B) An unrelated idea from a different field",
                f"C) A synonym for {module.topic}",
                "D) None of the above",
            ],
            "answer_idx": 0,
        })
    if len(module.key_concepts) > 1:
        questions.append({
            "stem": f"How does {module.key_concepts[1]} relate to {module.topic}?",
            "options": [
                f"A) It is central to understanding {module.topic}",
                f"B) It is only relevant in {course.title}",
                f"C) It contradicts {module.topic}",
                "D) It has no relationship",
            ],
            "answer_idx": 0,
        })
    if module.learning_goals:
        questions.append({
            "stem": "After completing this module, you should be able to:",
            "options": [
                f"A) {module.learning_goals[0]}",
                "B) Recite the textbook from memory",
                "C) Ignore the topic entirely",
                "D) Only study for the final exam",
            ],
            "answer_idx": 0,
        })
    return questions
