#!/usr/bin/env bash
# Audit script for Active Inference for Organizations
# Verifies structural completeness of all modules.

set -euo pipefail

PASS=0; FAIL=0; WARN=0

check_file() {
    if [ -f "$1" ]; then
        PASS=$((PASS + 1))
    else
        echo "  FAIL: Missing $1"
        FAIL=$((FAIL + 1))
    fi
}

check_module() {
    local dir="$1"
    for f in module.md questions.md practice_quiz.md lab.md dashboard.html README.md AGENTS.md; do
        check_file "$dir/$f"
    done
}

check_course() {
    local course_dir="$1"
    local course_name="$2"
    echo "--- Course: $course_name ---"
    check_file "$course_dir/README.md"
    check_file "$course_dir/AGENTS.md"
    check_file "$course_dir/syllabus.md"
    for mod_dir in "$course_dir"/[0-9][0-9]_*/; do
        [ -d "$mod_dir" ] && check_module "$mod_dir"
    done
}

echo "=== Active Inference for Organizations Audit ==="
echo ""

echo "--- Root-level files ---"
check_file "README.md"
check_file "OVERVIEW.md"
check_file "AGENTS.md"

echo "--- Resource files ---"
for f in glossary.md notation_table.md references.md cross_course_map.md learning_pathways.md faq.md README.md AGENTS.md; do
    check_file "resources/$f"
done

check_course "01_organizational_systems" "Organizational Systems"
check_course "02_collective_intelligence" "Collective Intelligence"
check_course "03_strategic_modeling" "Strategic Modeling"
check_course "04_digital_transformation" "Digital Transformation"

echo ""
echo "--- Placeholder Check ---"
if grep -r "\[TODO\]\|\[PLACEHOLDER\]\|TBD\|FIXME" --include="*.md" . 2>/dev/null | grep -v AGENTS.md | grep -v audit_modules.sh; then
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
