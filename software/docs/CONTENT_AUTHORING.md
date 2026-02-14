# ✍️ Content Authoring Guide

> **Navigation**: [← Docs Index](README.md) | [Course Catalog](COURSE_CATALOG.md)

Guide for creating module content in the Active Inference Institute curriculum.

---

## 📂 Module Structure

Every module directory (e.g., `01_systems/`) **must** contain:

| File | Purpose |
| :--- | :--- |
| **`module.md`** | Main lecture content with Learning Objectives. |
| **`questions.md`** | exactly 20 study questions (numbered 1-20). |
| **`practice_quiz.md`** | 7 Multiple Choice + 3 Free Response questions. |
| **`lab.md`** | Hands-on lab protocol or thought experiment. |
| **`README.md`** | Navigation hub for the module. |
| **`AGENTS.md`** | Context for AI agents. |

---

## 1. `module.md` (Lecture)

The core text. Rendered to PDF, HTML, MP3.

```markdown
# Module Title

## Learning Objectives
1. Objective A
2. Objective B

## Section 1: Introduction
Content goes here use **bold** for key terms.

## Section 2: Deep Dive
...

## Summary
...
```

---

## 2. `questions.md` (Self-Study)

**Strict Rule**: Must have exactly 20 questions, numbered 1-20.

```markdown
# Module 1: Study Questions

1. What is a specific question?
2. What is another question?
...
20. Final question.
```

*Tip: Use `uv run python scripts/renumber_questions.py` to fix numbering.*

---

## 3. `practice_quiz.md` (Assessment)

Format: 7 MC + 3 FR.

```markdown
# Practice Quiz

## Multiple Choice

### Question 1
Question text?
a) Option A
b) Option B
c) Option C
d) Option D

**Answer: b**
**Explanation**: Why B is correct.

...

## Free Response

### Question 8
Describe X.

**Model Answer**: X is...
```

---

## 4. `lab.md` (Activity)

Uses `{fill:textarea}` for interactive PDFs/HTML.

```markdown
# Lab: Title

## Procedure

1. Do step one.
   {fill:textarea}

2. Do step two.
   {fill:textarea}
```

---

## ✅ Quality Checklist

- [ ] All 4 required files exist.
- [ ] `module.md` has learning objectives.
- [ ] `questions.md` has exactly 20 items.
- [ ] `practice_quiz.md` has answers/explanations.
- [ ] Key terms are **bolded** on first use.
- [ ] No "TODO" or placeholder text (use "Coming Soon" if needed).

---
*Last Updated: 2026-02-14*
