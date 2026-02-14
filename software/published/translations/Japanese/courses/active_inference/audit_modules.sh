#!/bin/bash
# Audit script for Active Inference curriculum module.md files
# Checks for:
# 1. Missing blank lines before --- horizontal rules
# 2. Section structure (## 1. through ## 7.)
# 3. Reference link to resources/references.md
# 4. Presence of Parr et al. (2022) in references
# 5. Cross-reference format in Section 6

ROOT="$(cd "$(dirname "$0")" && pwd)"
ISSUES=0
TOTAL_MODULES=0

echo "========================================="
echo "Active Inference Curriculum Audit"
echo "========================================="
echo ""

# --- Check 1: Missing blank lines before --- ---
echo "--- CHECK 1: Missing blank lines before '---' ---"
for f in "$ROOT"/0*/0*/module.md; do
    rel="${f#$ROOT/}"
    prev_was_blank=true
    line_num=0
    while IFS= read -r line; do
        line_num=$((line_num + 1))
        if [ "$line" = "---" ] && [ "$prev_was_blank" = false ]; then
            echo "  ISSUE: $rel:$line_num — '---' not preceded by blank line"
            ISSUES=$((ISSUES + 1))
        fi
        if [ -z "$line" ]; then
            prev_was_blank=true
        else
            prev_was_blank=false
        fi
    done < "$f"
done
echo ""

# --- Check 2: Section structure ---
echo "--- CHECK 2: Section structure (7 sections) ---"
for f in "$ROOT"/0*/0*/module.md; do
    rel="${f#$ROOT/}"
    TOTAL_MODULES=$((TOTAL_MODULES + 1))
    for i in 1 2 3 4 5 6 7; do
        if ! grep -q "## $i\." "$f"; then
            echo "  ISSUE: $rel — missing section ## $i."
            ISSUES=$((ISSUES + 1))
        fi
    done
done
echo "  Total modules checked: $TOTAL_MODULES"
echo ""

# --- Check 3: Reference link ---
echo "--- CHECK 3: Link to resources/references.md ---"
for f in "$ROOT"/0*/0*/module.md; do
    rel="${f#$ROOT/}"
    if ! grep -q "resources/references.md" "$f"; then
        echo "  ISSUE: $rel — missing link to resources/references.md"
        ISSUES=$((ISSUES + 1))
    fi
done
echo ""

# --- Check 4: Parr et al. (2022) ---
echo "--- CHECK 4: Parr et al. (2022) in references ---"
for f in "$ROOT"/0*/0*/module.md; do
    rel="${f#$ROOT/}"
    if ! grep -q "Parr" "$f"; then
        echo "  MISSING: $rel — no mention of Parr et al."
        ISSUES=$((ISSUES + 1))
    fi
done
echo ""

# --- Check 5: Cross-reference format in summary ---
echo "--- CHECK 5: Cross-reference format variety ---"
echo "  Format A (short): 'Course Module N (topic)'"
echo "  Format B (long):  'For the X, see Course N (Name), Module N'"
for f in "$ROOT"/0*/0*/module.md; do
    rel="${f#$ROOT/}"
    if grep -q "For the.*see.*Course" "$f"; then
        echo "  FORMAT B: $rel"
    elif grep -q "Cross-references" "$f"; then
        echo "  FORMAT A: $rel"
    fi
done
echo ""

# --- Check 6: Reference count in references.md ---
echo "--- CHECK 6: Reference count in references.md ---"
# references.md uses table format, not bullet lists — count data rows (exclude header/separator lines)
REF_COUNT=$(grep -c '^| [^-]' "$ROOT/resources/references.md" 2>/dev/null || echo "?")
# Subtract header rows (one per table section)
HEADER_COUNT=$(grep -c '^| #\|^| Reference\|^| Tool\|^| Author' "$ROOT/resources/references.md" 2>/dev/null || echo "0")
REF_COUNT=$((REF_COUNT - HEADER_COUNT))
echo "  references.md table entries: $REF_COUNT"
SYLLABUS_CLAIM=$(grep -o '[0-9]* canonical citations' "$ROOT/01_philosophy/syllabus.md" 2>/dev/null || echo "not found")
echo "  Philosophy syllabus claims: $SYLLABUS_CLAIM"
echo ""

echo "========================================="
echo "TOTAL ISSUES FOUND: $ISSUES"
echo "========================================="
