#!/usr/bin/env python3
"""Phase 1: Mechanical fixes for course_development module.md template files.

Fixes applied:
1. Removes <!-- Content padding to ensure file size requirements --> comments
2. Resolves [Previous Topic] / [Next Topic] references using Active Inference spine
3. Expands course name abbreviations (Hs -> High School, Ms -> Middle School, Es -> Elementary School)
"""

import os
import re

BASE = "/Users/4d/Documents/GitHub/courses/course_development"

# Active Inference 8-part spine ordering
SPINE = ["Systems", "Agents", "Perception", "Cognition", "Action", "Learning", "Communication", "Planning"]
SPINE_MAP = {}
for i, topic in enumerate(SPINE):
    SPINE_MAP[topic] = {
        "prev": SPINE[(i - 1) % len(SPINE)],
        "next": SPINE[(i + 1) % len(SPINE)]
    }

# Course name abbreviation expansions (word-boundary safe)
COURSE_EXPANSIONS = {
    "Hs": "High School",
    "Ms": "Middle School",
    "Es": "Elementary School",
}


def extract_topic(content: str) -> str | None:
    """Extract the Active Inference topic from the module heading."""
    match = re.search(r'^# Module \d+:\s+(\w+)\s+in\s+', content, re.MULTILINE)
    if match:
        return match.group(1)
    return None


def extract_course_name(content: str) -> str | None:
    """Extract the course name from the module heading."""
    match = re.search(r'^# Module \d+:\s+\w+\s+in\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def fix_file(filepath: str) -> list[str]:
    """Apply all mechanical fixes to a module.md file. Returns list of changes made."""
    with open(filepath, 'r') as f:
        content = f.read()

    original = content
    changes = []

    # 1. Remove HTML padding comments
    padding_count = content.count('<!-- Content padding to ensure file size requirements -->')
    if padding_count > 0:
        # Remove padding lines and their surrounding blank lines
        content = re.sub(
            r'\n*<!-- Content padding to ensure file size requirements -->\n*',
            '\n',
            content
        )
        changes.append(f"Removed {padding_count} padding comments")

    # 2. Fix [Previous Topic] and [Next Topic]
    topic = extract_topic(content)
    if topic and topic in SPINE_MAP:
        if '[Previous Topic]' in content:
            content = content.replace('[Previous Topic]', SPINE_MAP[topic]["prev"])
            changes.append(f"[Previous Topic] -> {SPINE_MAP[topic]['prev']}")
        if '[Next Topic]' in content:
            content = content.replace('[Next Topic]', SPINE_MAP[topic]["next"])
            changes.append(f"[Next Topic] -> {SPINE_MAP[topic]['next']}")

    # 3. Expand course name abbreviations
    course_name = extract_course_name(content)
    if course_name and course_name in COURSE_EXPANSIONS:
        expanded = COURSE_EXPANSIONS[course_name]
        # Use word-boundary regex to safely replace
        content = re.sub(rf'\b{re.escape(course_name)}\b', expanded, content)
        changes.append(f"Course name: {course_name} -> {expanded}")

    # 4. Clean up multiple consecutive blank lines (max 2)
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = content.rstrip() + '\n'

    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return changes
    return []


def main() -> None:
    fixed_count = 0
    total_scanned = 0

    for root, dirs, files in os.walk(BASE):
        # Skip output directories
        if '/output/' in root or '/.pytest_cache/' in root or '/.benchmarks/' in root:
            continue
        for fname in files:
            if fname != 'module.md':
                continue
            filepath = os.path.join(root, fname)
            total_scanned += 1

            with open(filepath, 'r') as f:
                content = f.read()

            # Only process files with known placeholders
            markers = ['[Previous Topic]', '[Next Topic]', '<!-- Content padding']
            if not any(marker in content for marker in markers):
                continue

            changes = fix_file(filepath)
            if changes:
                fixed_count += 1
                short_path = filepath.replace(BASE + '/', '')
                print(f"  {short_path}")
                for c in changes:
                    print(f"    -> {c}")

    print(f"\n{'=' * 60}")
    print(f"Total module.md files scanned: {total_scanned}")
    print(f"Total files fixed: {fixed_count}")


if __name__ == '__main__':
    main()
