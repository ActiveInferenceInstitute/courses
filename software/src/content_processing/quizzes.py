"""Practice quiz generation logic.

Refactored from software/scripts/fix_stub_quizzes.py.
"""

import re
from pathlib import Path
from typing import Dict, List, Any

from src.content_processing.utils import get_audience_info

STUB_PATTERN = re.compile(
    r"A core concept in|An unrelated idea from a different field|A synonym for|None of the above"
)


def find_stub_quizzes(base: Path) -> List[Path]:
    """Find all practice_quiz.md files with stub content."""
    stubs = []
    for pq in sorted(base.rglob("practice_quiz.md")):
        if "output" in pq.parts or "youtube" in pq.parts:
            continue
        text = pq.read_text(encoding="utf-8")
        if STUB_PATTERN.search(text):
            stubs.append(pq)
    return stubs


def generate_quiz_content(module_data: Dict[str, Any], course_info: Dict[str, Any]) -> str:
    """Generate a complete practice quiz from module data."""
    concepts = module_data.get("key_concepts", [])
    objectives = module_data.get("objectives", [])
    title = module_data.get("title", f"Module {course_info['module_num']}: {course_info['module_topic']}")
    subtitle = module_data.get("subtitle", "")
    
    # Get audience-specific details
    course = course_info["course"]
    audience = get_audience_info(course)
    # The original script had slightly different tone names here, but we can reuse get_audience_info
    # and map if strictly necessary, but sticking to standard levels is cleaner.
    # Labs uses get_audience_info, so should stay consistent.
    
    # Build questions from concepts
    mc_questions = []
    answer_key = []

    for i, (name, defn) in enumerate(concepts[:5]):
        # Build wrong answers from other concepts' definitions or plausible alternatives
        wrong = []
        for j, (other_name, other_defn) in enumerate(concepts):
            if j != i and len(wrong) < 3:
                wrong.append(other_defn)

        # If we need more, add generic discipline-appropriate wrongs
        generic_wrongs = [
            f"A process that operates independently of {concepts[0][0] if concepts else 'the system'}, with no feedback or adaptation",
            "A static label applied to observed behavior without reference to underlying mechanisms",
            "A purely theoretical abstraction that has no measurable or observable consequences",
        ]
        gi = 0
        while len(wrong) < 3:
            wrong.append(generic_wrongs[gi % len(generic_wrongs)])
            gi += 1

        # Format the question
        options = [defn] + wrong[:3]
        # Deterministic positioning based on concept index
        correct_idx = i % 4
        correct_option = options.pop(0)
        options.insert(correct_idx, correct_option)

        letters = "ABCD"
        q_num = i + 1
        mc_questions.append(
            f"**{q_num}.** Which of the following best describes **{name}**?\n\n"
            + "\n".join(f"{letters[k]}) {opt}" for k, opt in enumerate(options))
        )
        answer_key.append(
            f"| {q_num} | {letters[correct_idx]} | {name}: {defn} |"
        )

    # Add objective-based questions
    if objectives:
        q_num = len(mc_questions) + 1
        obj = objectives[0]
        correct_idx = (q_num - 1) % 4
        options = [
            obj,
            "Memorize technical vocabulary without understanding its application to real scenarios",
            "Focus exclusively on mathematical derivations while ignoring conceptual understanding",
            "Review material from a completely different course unit",
        ]
        correct_opt = options.pop(0)
        options.insert(correct_idx, correct_opt)
        letters = "ABCD"
        mc_questions.append(
            f"**{q_num}.** A primary learning goal of this module is to:\n\n"
            + "\n".join(f"{letters[k]}) {opt}" for k, opt in enumerate(options))
        )
        answer_key.append(
            f"| {q_num} | {letters[correct_idx]} | This module's first goal: {obj} |"
        )

    if len(objectives) > 1:
        q_num = len(mc_questions) + 1
        obj = objectives[-1]
        correct_idx = (q_num - 1) % 4
        options = [
            obj,
            "Reproduce lecture content verbatim on an exam without deeper engagement",
            "Skip this module's content and move directly to the next unit",
            "Rely on passive reading without practicing or applying the material",
        ]
        correct_opt = options.pop(0)
        options.insert(correct_idx, correct_opt)
        letters = "ABCD"
        mc_questions.append(
            f"**{q_num}.** By the end of this module you should also be able to:\n\n"
            + "\n".join(f"{letters[k]}) {opt}" for k, opt in enumerate(options))
        )
        answer_key.append(
            f"| {q_num} | {letters[correct_idx]} | Another key goal: {obj} |"
        )

    # Build free-response questions from concepts and objectives
    fr_questions = []
    if concepts:
        fr_questions.append(
            f"**{len(mc_questions) + 1}.** Define **{concepts[0][0]}** in your own words "
            f"and explain why it is important in the context of {course_info['module_topic'].lower()}."
        )
    if len(concepts) >= 2:
        fr_questions.append(
            f"**{len(mc_questions) + 2}.** Explain the relationship between "
            f"**{concepts[0][0]}** and **{concepts[1][0]}**. "
            f"How do they work together within the Active Inference framework?"
        )
    if objectives:
        fr_questions.append(
            f"**{len(mc_questions) + len(fr_questions) + 1}.** "
            f"Give a concrete, real-world example that illustrates how "
            f"{course_info['module_topic'].lower()} connects to the overall Active Inference framework."
        )

    # Build the rubric hints
    rubric_hints = []
    if concepts:
        rubric_hints.append(
            f"**{len(mc_questions) + 1}.** Strong answers will: "
            f"(i) provide a clear, accurate definition of {concepts[0][0]} "
            f"that goes beyond the textbook wording, "
            f"(ii) connect it to specific module content, "
            f"(iii) explain its functional role in {course_info['module_topic'].lower()}."
        )
    if len(concepts) >= 2:
        rubric_hints.append(
            f"**{len(mc_questions) + 2}.** Strong answers will: "
            f"(i) accurately describe both {concepts[0][0]} and {concepts[1][0]}, "
            f"(ii) explain how they interact or depend on each other, "
            f"(iii) use specific examples from the module content."
        )
    if objectives:
        rubric_hints.append(
            f"**{len(mc_questions) + len(fr_questions)}.** Strong answers will: "
            f"(i) identify a specific real-world scenario, "
            f"(ii) map it to Active Inference concepts from this module, "
            f"(iii) explain the connection clearly enough that someone unfamiliar with the theory could follow."
        )

    # Assemble the quiz
    quiz_lines = [
        f"# Module Quiz: {subtitle or title}\n",
        f"**Name**: _________________________ **Date**: _____________\n",
        "---\n",
        "## Part A: Multiple Choice\n",
        "*Choose the best answer for each question.*\n",
    ]

    for q in mc_questions:
        quiz_lines.append(q + "\n")

    quiz_lines.append("---\n")
    quiz_lines.append("## Part B: Free Response\n")

    for fr in fr_questions:
        quiz_lines.append(fr + "\n")
        quiz_lines.append("_______________________________________________")
        quiz_lines.append("_______________________________________________")
        quiz_lines.append("_______________________________________________\n")

    quiz_lines.append("---\n")
    quiz_lines.append("## Answer Key\n")
    quiz_lines.append("### Part A\n")
    quiz_lines.append("| # | Answer | Explanation |")
    quiz_lines.append("|---|--------|-------------|")
    for ak in answer_key:
        quiz_lines.append(ak)

    quiz_lines.append("\n### Part B — Rubric Hints\n")
    for rh in rubric_hints:
        quiz_lines.append(rh + "\n")

    quiz_lines.append("---\n")
    quiz_lines.append(f"*This quiz covers {title}.*\n")

    return "\n".join(quiz_lines)
