"""Core logic for structural scanning of course modules."""

import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Any, Tuple

# Placeholder patterns
PLACEHOLDER_RE = re.compile(r"\[TODO\]|\[PLACEHOLDER\]|\bTBD\b|coming\s+soon|Lorem", re.IGNORECASE)

# Quiz patterns
MC_QUESTION_RE = re.compile(r"^\s*(\d+)\.\s", re.MULTILINE)
PART_B_RE = re.compile(r"#+\s*Part\s+B", re.IGNORECASE)
FR_QUESTION_RE = re.compile(r"^\s*(\d+)\.\s", re.MULTILINE)

# Learning objectives
LEARNING_OBJ_RE = re.compile(
    r"(?:learning\s+objectives?|objectives?|learning\s+outcomes?)", re.IGNORECASE
)

# Internal links
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")

REQUIRED_FILES = [
    "module.md",
    "questions.md",
    "practice_quiz.md",
    "lab.md",
    "dashboard.html",
    "AGENTS.md",
    "README.md",
]


def check_placeholders(content: str, filepath: Path) -> List[Dict[str, Any]]:
    """Find placeholder text in content."""
    issues = []
    for i, line in enumerate(content.split("\n"), 1):
        matches = PLACEHOLDER_RE.findall(line)
        for m in matches:
            issues.append(
                {
                    "type": "placeholder",
                    "file": str(filepath),
                    "line": i,
                    "match": m,
                    "context": line.strip()[:120],
                }
            )
    return issues


def check_quiz_structure(content: str, filepath: Path) -> List[Dict[str, Any]]:
    """Check practice_quiz.md for 7 MC + 3 FR questions."""
    issues = []

    # Split into Part A and Part B
    part_b_match = PART_B_RE.search(content)

    if part_b_match:
        part_a_content = content[: part_b_match.start()]
        part_b_content = content[part_b_match.start() :]
    else:
        part_a_content = content
        part_b_content = ""
        issues.append(
            {"type": "quiz_structure", "file": str(filepath), "detail": "No 'Part B' header found"}
        )

    # Count Part A questions
    mc_questions = MC_QUESTION_RE.findall(part_a_content)
    mc_count = len(mc_questions)
    if mc_count != 7:
        issues.append(
            {
                "type": "quiz_mc_count",
                "file": str(filepath),
                "detail": f"Part A has {mc_count} questions (expected 7)",
            }
        )

    # Count Part B questions
    if part_b_content:
        fr_questions = FR_QUESTION_RE.findall(part_b_content)
        fr_count = len(fr_questions)
        if fr_count != 3:
            issues.append(
                {
                    "type": "quiz_fr_count",
                    "file": str(filepath),
                    "detail": f"Part B has {fr_count} questions (expected 3)",
                }
            )

    return issues


def count_study_questions(content: str, filepath: Path) -> Tuple[List[Dict[str, Any]], int]:
    """Count study questions in questions.md."""
    issues = []
    questions = MC_QUESTION_RE.findall(content)
    q_count = len(questions)
    if q_count < 15 or q_count > 25:
        issues.append(
            {
                "type": "questions_count",
                "file": str(filepath),
                "detail": f"Found {q_count} study questions (expected ~20)",
            }
        )
    return issues, q_count


def check_learning_objectives(content: str, filepath: Path) -> List[Dict[str, Any]]:
    """Check module.md for learning objectives section."""
    issues = []
    if not LEARNING_OBJ_RE.search(content):
        issues.append(
            {
                "type": "missing_learning_objectives",
                "file": str(filepath),
                "detail": "No learning objectives section found",
            }
        )
    return issues


def check_cross_references(content: str, filepath: Path) -> List[Dict[str, Any]]:
    """Check for internal links and validate paths."""
    issues = []
    for match in LINK_RE.finditer(content):
        text, link = match.group(1), match.group(2)
        # Skip external URLs and anchors
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        # Check if it's a relative path
        try:
            ref_path = (filepath.parent / link).resolve()
            if not ref_path.exists():
                issues.append(
                    {
                        "type": "broken_link",
                        "file": str(filepath),
                        "detail": f"Broken internal link: [{text}]({link})",
                    }
                )
        except Exception:
            issues.append(
                {
                    "type": "broken_link",
                    "file": str(filepath),
                    "detail": f"Invalid internal link format: [{text}]({link})",
                }
            )
    return issues


def scan_course(
    course_id: str, course_config: Dict[str, Any], root_path: Path
) -> Tuple[Dict[str, Any], Dict[str, Any], List[Dict[str, Any]]]:
    """Scan modules within a specific course configuration."""

    # Calculate base path from repo root
    base_path = root_path / course_config["rel_path"]

    course_stats: Dict[str, Any] = {
        "modules_expected": 0,  # Will be determined by glob
        "modules_found": 0,
        "missing_files": [],
        "small_files": [],
        "placeholder_count": 0,
        "quiz_issues": 0,
        "question_issues": 0,
        "learning_obj_issues": 0,
        "broken_links": 0,
    }

    course_issues = []

    # Find module directories
    module_glob = course_config.get("module_glob", "*")

    # Check if modules are in a subdirectory (though standard config implies flat list usually)
    # The config has "has_course_subdir" but also "rel_path" typically points to the container of modules
    # Let's trust "module_glob" relative to "rel_path"

    if not base_path.exists():
        course_issues.append(
            {
                "type": "missing_course_dir",
                "file": str(base_path),
                "detail": f"Course directory not found at {base_path}",
            }
        )
        return {}, {course_id: course_stats}, course_issues

    module_dirs = sorted(list(base_path.glob(module_glob)))

    # Filter out non-directories
    module_dirs = [d for d in module_dirs if d.is_dir()]

    course_stats["modules_expected"] = len(
        module_dirs
    )  # We expect what we find if we don't have a strict list

    for mod_path in module_dirs:
        course_stats["modules_found"] += 1

        for req_file in REQUIRED_FILES:
            fpath = mod_path / req_file

            # Check 1: File existence
            if not fpath.exists():
                course_stats["missing_files"].append(str(fpath))
                course_issues.append(
                    {"type": "missing_file", "file": str(fpath), "detail": "Required file missing"}
                )
                continue

            # Check 2: File size
            fsize = fpath.stat().st_size
            if fsize <= 500:
                course_stats["small_files"].append(f"{fpath} ({fsize}B)")
                course_issues.append(
                    {
                        "type": "small_file",
                        "file": str(fpath),
                        "detail": f"File is only {fsize} bytes (threshold: 500)",
                    }
                )

            # Read content for deeper checks
            try:
                content = fpath.read_text(encoding="utf-8")
            except Exception as e:
                course_issues.append({"type": "read_error", "file": str(fpath), "detail": str(e)})
                continue

            # Check 3: Placeholder detection
            ph_issues = check_placeholders(content, fpath)
            course_stats["placeholder_count"] += len(ph_issues)
            course_issues.extend(ph_issues)

            # Check 4: Quiz structure (practice_quiz.md only)
            if req_file == "practice_quiz.md":
                qi = check_quiz_structure(content, fpath)
                course_stats["quiz_issues"] += len(qi)
                course_issues.extend(qi)

            # Check 5: Questions count (questions.md only)
            if req_file == "questions.md":
                qi, qcount = count_study_questions(content, fpath)
                course_stats["question_issues"] += len(qi)
                course_issues.extend(qi)

            # Check 6: Learning objectives (module.md only)
            if req_file == "module.md":
                lo = check_learning_objectives(content, fpath)
                course_stats["learning_obj_issues"] += len(lo)
                course_issues.extend(lo)

            # Check 7: Cross-references (md files only)
            if req_file.endswith(".md"):
                cr = check_cross_references(content, fpath)
                course_stats["broken_links"] += len(cr)
                course_issues.extend(cr)

    # Accumulate global stats from this course
    stats_update = {
        "total_modules_expected": course_stats["modules_expected"],
        "total_modules_found": course_stats["modules_found"],
        "total_files_checked": course_stats["modules_found"] * len(REQUIRED_FILES),
        "missing_files": len(course_stats["missing_files"]),
        "small_files": len(course_stats["small_files"]),
        "placeholders": course_stats["placeholder_count"],
        "quiz_issues": course_stats["quiz_issues"],
        "question_count_issues": course_stats["question_issues"],
        "learning_obj_issues": course_stats["learning_obj_issues"],
        "broken_links": course_stats["broken_links"],
        "missing_module_dirs": 0,  # Not tracking anticipated vs found strictly here like original
    }

    return stats_update, {course_id: course_stats}, course_issues


def format_report(
    stats: Dict[str, int],
    course_summaries: Dict[str, Any],
    all_issues: List[Dict[str, Any]],
    base_path_str: str,
) -> str:
    """Format a structured text report."""
    lines = []
    lines.append("=" * 80)
    lines.append("STRUCTURAL SCAN REPORT - Active Inference Courses")
    lines.append("=" * 80)
    lines.append("")

    # Overall stats
    lines.append("## OVERALL STATISTICS")
    lines.append(f"  Total modules checked:      {stats.get('total_modules_found', 0)}")
    lines.append(f"  Total files checked:        {stats.get('total_files_checked', 0)}")
    lines.append(f"  Missing required files:     {stats.get('missing_files', 0)}")
    lines.append(f"  Files under 500 bytes:      {stats.get('small_files', 0)}")
    lines.append(f"  Placeholder occurrences:    {stats.get('placeholders', 0)}")
    lines.append(f"  Quiz structure issues:      {stats.get('quiz_issues', 0)}")
    lines.append(f"  Question count issues:      {stats.get('question_count_issues', 0)}")
    lines.append(f"  Missing learning objectives:{stats.get('learning_obj_issues', 0)}")
    lines.append(f"  Broken internal links:      {stats.get('broken_links', 0)}")
    lines.append("")

    # Per-course summary
    lines.append("## PER-COURSE SUMMARY")
    lines.append("-" * 80)

    # Group by top-level course if possible, but COURSE_REGISTRY structure is flat dict
    # We can group by prefix if we want, or just list them.
    # The original grouped by "active_inference" vs "domains" etc.
    # Let's just list them sorted by ID for now or try to recreate simple grouping.

    courses_sorted = sorted(course_summaries.items())

    for course_id, cs in courses_sorted:
        total_missing = len(cs["missing_files"])
        total_small = len(cs["small_files"])
        total_ph = cs["placeholder_count"]
        total_quiz = cs["quiz_issues"]
        total_qcount = cs["question_issues"]
        total_lo = cs["learning_obj_issues"]
        total_bl = cs["broken_links"]

        has_issues = (
            total_missing + total_small + total_ph + total_quiz + total_qcount + total_lo + total_bl
        ) > 0
        status = "ISSUES" if has_issues else "OK"

        lines.append(f"\n### {course_id} [{status}]")
        lines.append(f"    Modules found: {cs['modules_found']}")
        if total_missing:
            lines.append(f"    Missing files: {total_missing}")
        if total_small:
            lines.append(f"    Small files (<500B): {total_small}")
        if total_ph:
            lines.append(f"    Placeholders: {total_ph}")
        if total_quiz:
            lines.append(f"    Quiz issues: {total_quiz}")
        if total_qcount:
            lines.append(f"    Question count issues: {total_qcount}")
        if total_lo:
            lines.append(f"    Learning objective issues: {total_lo}")
        if total_bl:
            lines.append(f"    Broken links: {total_bl}")

    # Issues by type
    lines.append("")
    lines.append("=" * 80)
    lines.append("## ALL ISSUES BY TYPE")
    lines.append("=" * 80)

    issues_by_type = defaultdict(list)
    for issue in all_issues:
        issues_by_type[issue["type"]].append(issue)

    type_labels = {
        "missing_module_dir": "MISSING MODULE DIRECTORIES",
        "missing_file": "MISSING REQUIRED FILES",
        "small_file": "FILES UNDER 500 BYTES",
        "placeholder": "PLACEHOLDER TEXT FOUND",
        "quiz_structure": "QUIZ STRUCTURE ISSUES (missing Part B)",
        "quiz_mc_count": "QUIZ MULTIPLE CHOICE COUNT ISSUES",
        "quiz_fr_count": "QUIZ FREE RESPONSE COUNT ISSUES",
        "questions_count": "STUDY QUESTION COUNT ISSUES",
        "missing_learning_objectives": "MISSING LEARNING OBJECTIVES",
        "broken_link": "BROKEN INTERNAL LINKS",
        "read_error": "FILE READ ERRORS",
    }

    for issue_type, label in type_labels.items():
        issues = issues_by_type.get(issue_type, [])
        if not issues:
            continue
        lines.append(f"\n### {label} ({len(issues)} issues)")
        for iss in issues:
            short_path = str(iss["file"]).replace(base_path_str + "/", "")
            detail = iss.get("detail", "")
            context = iss.get("context", "")
            if detail:
                lines.append(f"  - {short_path}: {detail}")
            elif context:
                match_text = iss.get("match", "")
                lines.append(
                    f"  - {short_path}:L{iss.get('line', '?')}: '{match_text}' in: {context}"
                )
            else:
                lines.append(f"  - {short_path}")

    lines.append("")
    lines.append("=" * 80)
    lines.append("END OF REPORT")
    lines.append("=" * 80)

    return "\n".join(lines)
