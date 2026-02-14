#!/usr/bin/env python3
"""Fix course name abbreviations in ALL .md source files (not just module.md).

Expands Hs -> High School, Ms -> Middle School, Es -> Elementary School
in questions.md, practice_quiz.md, and lab.md files.
"""

import os
import re

BASE = "/Users/4d/Documents/GitHub/courses/course_development"

EXPANSIONS = {
    "Hs": "High School",
    "Ms": "Middle School",
    "Es": "Elementary School",
}

FILE_TYPES = ["questions.md", "practice_quiz.md", "lab.md"]

fixed_count = 0
for root, dirs, files in os.walk(BASE):
    if "/output/" in root or "/.pytest_cache/" in root or "/.benchmarks/" in root:
        continue
    for fname in files:
        if fname not in FILE_TYPES:
            continue
        filepath = os.path.join(root, fname)
        with open(filepath, "r") as f:
            content = f.read()

        original = content
        for abbrev, expanded in EXPANSIONS.items():
            content = re.sub(rf"\b{re.escape(abbrev)}\b", expanded, content)

        if content != original:
            with open(filepath, "w") as f:
                f.write(content)
            fixed_count += 1
            short = filepath.replace(BASE + "/", "")
            print(f"  {short}")

print(f"\nTotal files fixed: {fixed_count}")
