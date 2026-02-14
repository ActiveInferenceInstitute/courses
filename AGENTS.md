# Active Inference Institute — Courses Repository — Agent Guidelines

> **Quick Navigation**: [README](./README.md) | [Course Development](./course_development/AGENTS.md) | [Software](./software/AGENTS.md) | [Published](./published/AGENTS.md) | [Summaries](./summaries/AGENTS.md)

## Repository Overview

This repository contains the complete curriculum infrastructure for the Active Inference Institute: **10 courses**, **320 modules**, **3,400+ content files**, a **Python publishing engine**, and a **YouTube transcript archive** with **1,020 passing tests**.

---

## Directory Roles

| Directory | Purpose | AGENTS.md |
|-----------|---------|-----------|
| `course_development/` | Source curricula — all authoring happens here | [AGENTS.md](course_development/AGENTS.md) |
| `published/` | Rendered outputs for distribution (generated, not hand-edited) | [AGENTS.md](published/AGENTS.md) |
| `software/` | Python engine: 21 modules, 21 scripts, 18 docs, 1,020 tests | [AGENTS.md](software/AGENTS.md) |
| `summaries/` | Generated course summaries | [AGENTS.md](summaries/AGENTS.md) |
| `publish.py` | Top-level pipeline entry point | — |
| `publish.toml` | Publishing configuration (courses, formats, options) | — |

---

## Universal Rules

### 1. Real Methods Only

All code and content must use **real methods** — no mocks, stubs, fakes, `[TODO]`, `[PLACEHOLDER]`, or `TBD` markers. Every function must have a real implementation; every module must contain substantive, accurate content.

### 2. Modular, Intelligent, Functional, Logged, Tested, Documented

Every component must be:

- **Modular** — Self-contained, reusable, independently testable
- **Intelligent** — Thoughtfully designed with clear purpose
- **Functional** — Working implementation with proper error handling
- **Logged** — Appropriate logging for debugging and monitoring
- **Tested** — Covered by real tests (no mocks)
- **Documented** — README.md and AGENTS.md at every level

### 3. AGENTS.md at Every Level

Every directory in this repository must have an `AGENTS.md` file that documents:

- Directory purpose and contents
- Critical rules and conventions for that context
- Links to child and parent AGENTS.md files

### 4. Audience-Appropriate Content

Course content must match the target audience's level:

| Level | Formalism | Code | Lab Style |
|-------|-----------|------|-----------|
| ES (K-5) | None | None | Stories, drawing |
| Family (0-6) | None | None | Parent-child activities |
| MS (6-8) | Fractions | Scratch | Group challenges |
| HS (9-12) | Algebra | Python basics | Guided labs |
| 101 (Undergrad) | Full notation | Python/NumPy | Simulations, essays |
| Core (Graduate) | Full formalism | Custom library | Case studies, proofs |
| 401 (PhD) | Advanced | Research code | Seminars, proposals |

### 5. The 8-Topic Spine

All 10 courses follow this exact topic order in every unit:

1. **Systems** → 2. **Agents** → 3. **Perception** → 4. **Cognition** → 5. **Action** → 6. **Learning** → 7. **Communication** → 8. **Planning**

This order is fixed and reflects the logical dependency chain of the Free Energy Principle.

---

## AGENTS.md Hierarchy

```text
courses/
├── AGENTS.md                          ← THIS FILE (top-level)
├── course_development/
│   ├── AGENTS.md                      ← Master curriculum guidelines
│   ├── active_inference/AGENTS.md     ← Core curriculum (4 tracks)
│   ├── active_inference_*/AGENTS.md   ← Level-adapted courses
│   ├── domains/AGENTS.md             ← Domain curricula
│   └── [per-unit, per-module AGENTS.md]
├── published/
│   └── AGENTS.md                      ← Published outputs guidelines
├── software/
│   ├── AGENTS.md                      ← Software technical reference
│   ├── src/AGENTS.md                 ← Source modules
│   ├── scripts/AGENTS.md            ← CLI tools
│   ├── tests/AGENTS.md              ← Test infrastructure
│   ├── docs/AGENTS.md               ← Documentation
│   └── [per-module AGENTS.md]
└── summaries/
    └── AGENTS.md                      ← Summaries guidelines
```

---

## Cross-Reference Convention

Always use relative paths when linking between files:

```markdown
See [QUICKSTART.md](software/docs/QUICKSTART.md) for setup instructions.
See [Curriculum Overview](course_development/README.md) for the full course map.
```

---

## Key Resources

| Resource | Path | Purpose |
|----------|------|---------|
| Publishing config | [`publish.toml`](publish.toml) | Toggle courses, formats, options |
| Quick start | [`software/docs/QUICKSTART.md`](software/docs/QUICKSTART.md) | Installation & setup |
| Architecture | [`software/docs/ARCHITECTURE.md`](software/docs/ARCHITECTURE.md) | System design |
| Course catalog | [`software/docs/COURSE_CATALOG.md`](software/docs/COURSE_CATALOG.md) | All courses at a glance |
| Contributing | [`software/docs/CONTRIBUTING.md`](software/docs/CONTRIBUTING.md) | How to contribute |

---

> *"Minimize surprise. Maximize evidence."* — Active Inference Institute
