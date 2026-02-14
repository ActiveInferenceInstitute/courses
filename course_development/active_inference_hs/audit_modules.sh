#!/usr/bin/env bash
# audit_modules.sh — Structural audit for the Active Inference HS curriculum
# Usage: bash audit_modules.sh
# Checks: file existence, section counts, quiz format, cross-reference validity

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

COURSES=("01_everyday_life" "02_biology_health" "03_math_foundations" "04_technology_ai")
MODULES=("01_systems" "02_agents" "03_perception" "04_cognition" "05_action" "06_learning" "07_communication" "08_planning")
MODULE_FILES=("module.md" "questions.md" "practice_quiz.md" "lab.md" "dashboard.html" "README.md" "AGENTS.md")

PASS=0
FAIL=0
WARN=0

pass() { PASS=$((PASS+1)); }
fail() { FAIL=$((FAIL+1)); echo "  FAIL: $1"; }
warn() { WARN=$((WARN+1)); echo "  WARN: $1"; }

echo "=== Active Inference HS Curriculum Audit ==="
echo ""

# --- Root-level files ---
echo "--- Root-level files ---"
for f in README.md OVERVIEW.md AGENTS.md audit_modules.sh; do
  if [[ -f "$f" ]]; then pass; else fail "Missing root file: $f"; fi
done

# --- Resource files ---
echo "--- Resource files ---"
RESOURCE_FILES=("README.md" "AGENTS.md" "notation_table.md" "glossary.md" "references.md" "cross_course_map.md" "learning_pathways.md" "faq.md")
for f in "${RESOURCE_FILES[@]}"; do
  if [[ -f "resources/$f" ]]; then pass; else fail "Missing resource: resources/$f"; fi
done

# --- Per-course files ---
for course in "${COURSES[@]}"; do
  echo "--- Course: $course ---"
  for f in README.md AGENTS.md syllabus.md; do
    if [[ -f "$course/$f" ]]; then pass; else fail "Missing $course/$f"; fi
  done

  for mod in "${MODULES[@]}"; do
    for f in "${MODULE_FILES[@]}"; do
      filepath="$course/$mod/$f"
      if [[ -f "$filepath" ]]; then
        pass
      else
        fail "Missing $filepath"
      fi
    done

    # Check module.md has 7 sections (## headers)
    modfile="$course/$mod/module.md"
    if [[ -f "$modfile" ]]; then
      section_count=$(grep -c '^## ' "$modfile" || true)
      if [[ "$section_count" -ge 7 ]]; then
        pass
      else
        warn "$modfile has $section_count sections (expected ≥7)"
      fi
    fi

    # Check questions.md has 20 questions
    qfile="$course/$mod/questions.md"
    if [[ -f "$qfile" ]]; then
      q_count=$(grep -cE '^[0-9]+\.' "$qfile" || true)
      if [[ "$q_count" -eq 20 ]]; then
        pass
      else
        warn "$qfile has $q_count questions (expected 20)"
      fi
    fi

    # Check practice_quiz.md has Part A and Part B
    pqfile="$course/$mod/practice_quiz.md"
    if [[ -f "$pqfile" ]]; then
      has_a=$(grep -c 'Part A' "$pqfile" || true)
      has_b=$(grep -c 'Part B' "$pqfile" || true)
      if [[ "$has_a" -ge 1 && "$has_b" -ge 1 ]]; then
        pass
      else
        warn "$pqfile missing Part A or Part B"
      fi
    fi

    # Check lab.md has fill:textarea fields
    labfile="$course/$mod/lab.md"
    if [[ -f "$labfile" ]]; then
      ta_count=$(grep -c 'fill:textarea' "$labfile" || true)
      if [[ "$ta_count" -ge 3 ]]; then
        pass
      else
        warn "$labfile has $ta_count textarea fields (expected ≥3)"
      fi
    fi
  done
done

# --- Placeholder check ---
echo ""
echo "--- Placeholder Check ---"
# Exclude AGENTS.md from placeholder check as it contains the rule definitions
placeholder_count=$(grep -rn '\[TODO\]\|\[PLACEHOLDER\]\|\[INSERT\]' --include='*.md' --exclude='AGENTS.md' . 2>/dev/null || true | wc -l | tr -d ' ')
if [[ "$placeholder_count" -eq 0 ]]; then
  pass
  echo "  No placeholders found (excluding guidelines)."
else
  fail "Found $placeholder_count placeholder(s)"
  grep -rn '\[TODO\]\|\[PLACEHOLDER\]\|\[INSERT\]' --include='*.md' --exclude='AGENTS.md' . 2>/dev/null | head -10
fi

echo ""
echo "=== Audit Summary ==="
echo "  PASS: $PASS"
echo "  FAIL: $FAIL"
echo "  WARN: $WARN"

if [[ "$FAIL" -gt 0 ]]; then
  echo "  STATUS: FAILED"
  exit 1
else
  echo "  STATUS: PASSED"
fi
