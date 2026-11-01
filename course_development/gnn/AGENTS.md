# GNN Syntax Track — Agent Guidelines

> **Quick Navigation**: [Track README](./README.md) | [Curriculum AGENTS](../AGENTS.md) | [Module AGENTS](./01_gnn_syntax/AGENTS.md)

## Overview

This directory is the **GNN Syntax Track**: a supplementary content tree that
teaches Generalized Notation Notation (GNN) using real exemplars from the GNN
project. It is registered in `COURSE_REGISTRY` as `gnn` so the standard
publishing pipeline renders it, but it is **not** one of the fourteen 8-topic
spiral courses and must never be counted as one.

---

## Directory Contents

| Path | Type | Description |
|------|------|-------------|
| `README.md` | File | Track overview, exemplar mapping, publishing commands |
| `AGENTS.md` | File | This file — track agent guidelines |
| `01_gnn_syntax/` | Directory | The lesson module (module, questions, quiz, lab, dashboard, models) |

---

## Critical Rules

1. **Exemplars are verbatim copies.** Files under `01_gnn_syntax/models/` come
   from the GNN repository at the commit recorded in
   [`models/README.md`](./01_gnn_syntax/models/README.md). Never hand-edit them;
   re-copy from the pinned commit and update the provenance table.
2. **Keep counts accurate.** State the shipped exemplar count (five) and the
   source revision exactly. Do not claim coverage of the full GNN corpus.
3. **No fabricated results.** Do not describe pipeline outputs, render
   successes, or execution results that were not produced by a real run.
   Framework support statements must match the GNN repository's documentation.
4. **Respect the level mapping.** Elementary and Family levels do not introduce
   GNN; middle school is a guided reading. Do not silently promote the mapping.
5. **Follow the module conventions.** `module.md`, `questions.md` (20
   questions), `practice_quiz.md` (7 MC + 3 short answer), `lab.md` (learning
   goals + `{fill:textarea}` + summary table), `README.md`, `AGENTS.md`, and a
   generated `dashboard.html` — see the
   [portfolio guidelines](../AGENTS.md).
6. **No placeholders.** Every worksheet field and exercise must be completable
   with the shipped materials.

---

## Cross-References

- [Course Development AGENTS](../AGENTS.md) — portfolio-wide content rules
- [GNN exemplar models](./01_gnn_syntax/models/README.md)
- [YouTube GNN episodes](../youtube/active-inferant-stream/) — stream transcripts 014.1 and 014.2
