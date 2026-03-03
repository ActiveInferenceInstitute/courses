# Active Inference Curriculum Portfolio — Agent Guidelines

> **Quick Navigation**: [README](./README.md) | [Core Curriculum](./active_inference/) | [ES](./active_inference_es/) | [Family](./active_inference_family/) | [MS](./active_inference_ms/) | [HS](./active_inference_hs/) | [101](./active_inference_101/) | [401](./active_inference_401/) | [Domains](./domains/)

## Portfolio Overview

This portfolio contains **14 courses**, **58 units**, **464 modules**, and **6,100+ content files** for the Active Inference Institute. All courses share a common 8-topic spiral structure grounded in the **Free Energy Principle (FEP)** and **Active Inference**, adapted for audiences ranging from kindergarten to PhD researchers.

Agents working anywhere in this repository must follow the universal rules below and consult the course-specific AGENTS.md for local conventions.

---

## Master Color Identity

Every course has a distinct visual identity used in dashboards, navigation, and branding.

| Course | ID | Accent Color | Hex | Gradient | Semantic Meaning |
|--------|----|-------------|-----|----------|-----------------|
| Core Curriculum | `active_inference` | Sky Blue | `#38bdf8` | Blue → Indigo | Foundational, intellectual, canonical |
| College 101 | `active_inference_101` | Cyan | `#22d3ee` | Cyan → Purple | Fresh, accessible, introductory |
| Advanced 401 | `active_inference_401` | Purple | `#a78bfa` | Purple → Pink | Advanced, sophisticated, research-level |
| Elementary School | `active_inference_es` | Green | `#4ade80` | Green → Cyan | Growth, playful, developmental |
| Family | `active_inference_family` | Orange | `#fb923c` | Orange → Yellow | Warm, nurturing, practical |
| High School | `active_inference_hs` | Indigo | `#818cf8` | Indigo → Violet | Energetic, youthful, aspirational |
| Middle School | `active_inference_ms` | Teal | `#2dd4bf` | Teal → Blue | Curious, explorative |
| Embodied Cognition | `active_inference_embodied` | Rose | `#fb7185` | Rose → Purple | Somatic, felt, intuitive |
| Organizations | `active_inference_organizations` | Amber | `#fbbf24` | Amber → Red | Strategic, dynamic, decisive |
| Robotics | `active_inference_robotics` | Emerald | `#34d399` | Emerald → Blue | Technical, precise, engineered |
| Crochet Circles | `active_inference_crochet` | Violet | `#a78bfa` | Violet → Fuchsia | Creative, textured, handcrafted |
| Inventions | `active_inference_inventions` | Lime | `#a3e635` | Lime → Emerald | Inventive, experimental, playful |
| Metallurgy | `active_inference_metallurgy` | Slate | `#94a3b8` | Slate → Zinc | Industrial, structural, elemental |
| Comedy | `active_inference_comedy` | Yellow | `#facc15` | Yellow → Orange | Surprising, rhythmic, communal |

---

## The 8-Topic Spine

All 14 courses follow this exact topic order in every unit:

1. **Systems** → 2. **Agents** → 3. **Perception** → 4. **Cognition** → 5. **Action** → 6. **Learning** → 7. **Communication** → 8. **Planning**

### Theory Rationale (Dependency Chain)

The order reflects a logical dependency chain grounded in the Free Energy Principle:

| # | Topic | FEP Role | Depends On | Central Question |
|---|-------|----------|------------|-----------------|
| 1 | Systems | Define what EXISTS | — | What defines a system's boundary? |
| 2 | Agents | Define which systems ACT | Systems | What makes something an agent? |
| 3 | Perception | How agents SENSE | Agents | How do agents build internal models? |
| 4 | Cognition | How agents THINK | Perception | How are beliefs weighted and updated? |
| 5 | Action | How agents DO | Cognition | How do agents select and execute policies? |
| 6 | Learning | How agents IMPROVE | Action | How do agents improve their models? |
| 7 | Communication | How agents COORDINATE | Learning | How do agents share and align models? |
| 8 | Planning | How agents PLAN | Communication | How do agents reason about the future? |

### Spiral Learning

Each course revisits all 8 topics from a different disciplinary lens, deepening understanding with each pass. A student progressing through ES → MS → HS → 101 → Core → 401 encounters the same conceptual spine at increasing levels of formalism, from stories and drawings (ES) to proofs and research proposals (401).

---

## Universal Rules for All Agents

### 1. Consult Shared Resources First

Every course has a `resources/` directory. Before generating or editing content, read:

| Resource | Purpose |
|----------|---------|
| `resources/notation_table.md` | Canonical notation — use before writing any formula |
| `resources/glossary.md` | Canonical definitions — use before using any technical term |
| `resources/references.md` | Canonical references — use before citing any source |
| `resources/cross_course_map.md` | Cross-course links — use before adding cross-references |

### 2. Never Use Placeholders

All content must use **real methods** — no mocks, stubs, `[TODO]`, `[PLACEHOLDER]`, or `TBD` markers. Every module must contain substantive, accurate content.

### 3. Audience-Appropriate Tone

Match the tone and complexity to the course's target audience:

| Level | Tone | Math | Code | Lab Style |
|-------|------|------|------|-----------|
| ES (K-5) | Wonder, play, storytime | None | None | Drawing, building, stories |
| Family (0-6) | Warm, nurturing, practical | None | None | Parent-child activities |
| MS (6-8) | Curious, relatable, meme-aware | Fractions, percentages | Scratch/blocks | Group challenges, investigations |
| HS (9-12) | Energetic, concrete-first | Algebra, basic probability | Python basics | Group activities, guided labs |
| 101 (Undergrad) | Rigorous but accessible | Full notation, Python/NumPy | Python | Essays, simulations, problem sets |
| Core (Graduate) | Academic, multi-perspective | Full formalism | Custom library | Thought experiments, case studies, proofs, coding |
| 401 (PhD) | Research-level, dense | Advanced formalism | Research code | Seminars, paper reviews, proofs, proposals |
| Embodied | Somatic, poetic, experiential | None | None | Somatic exercises, mindfulness, movement |
| Organizations | Business/management, strategic | Light formalism | None | Case studies, workshops, strategy exercises |
| Robotics | Engineering-focused, precise | Control theory, estimation | ROS2, Python | Hardware labs, simulations, design challenges |

### 4. Cross-Curriculum References

When linking between courses, always use relative paths. Format:

```markdown
See the [mathematical formulation](../active_inference/03_math/03_perception/module.md) for the formal derivation.
```

### 5. Quality Checklist (Universal)

Before marking any module complete, verify:

- [ ] No placeholder brackets `[...]` or `[TODO]` markers remain
- [ ] All notation matches the course's `resources/notation_table.md`
- [ ] All terms match the course's `resources/glossary.md`
- [ ] Cross-references use correct relative paths
- [ ] Module has all 7 files: `module.md`, `questions.md`, `practice_quiz.md`, `lab.md`, `dashboard.html`, `README.md`, `AGENTS.md`
- [ ] Content is appropriate for the target audience
- [ ] Questions are course-specific (not generic)
- [ ] Quiz Part A has exactly 7 MC questions; Part B has exactly 3 questions
- [ ] Lab has structured parts with learning goals
- [ ] Dashboard HTML is valid and interactive

---

## Course-Specific Guidelines

For detailed conventions, notation, terminology, and perspective tables, see each course's own AGENTS.md:

| Course | AGENTS.md |
|--------|-----------|
| Core Curriculum | [active_inference/AGENTS.md](./active_inference/AGENTS.md) |
| Elementary School | [active_inference_es/AGENTS.md](./active_inference_es/AGENTS.md) |
| Family | [active_inference_family/AGENTS.md](./active_inference_family/AGENTS.md) |
| Middle School | [active_inference_ms/AGENTS.md](./active_inference_ms/AGENTS.md) |
| High School | [active_inference_hs/AGENTS.md](./active_inference_hs/AGENTS.md) |
| College 101 | [active_inference_101/AGENTS.md](./active_inference_101/AGENTS.md) |
| Advanced 401 | [active_inference_401/AGENTS.md](./active_inference_401/AGENTS.md) |
| Embodied Cognition | [domains/active_inference_embodied/AGENTS.md](./domains/active_inference_embodied/AGENTS.md) |
| Organizations | [domains/active_inference_organizations/AGENTS.md](./domains/active_inference_organizations/AGENTS.md) |
| Robotics | [domains/active_inference_robotics/AGENTS.md](./domains/active_inference_robotics/AGENTS.md) |
| Crochet Circles | [domains/active_inference_crochet/AGENTS.md](./domains/active_inference_crochet/AGENTS.md) |
| Inventions | [domains/active_inference_inventions/AGENTS.md](./domains/active_inference_inventions/AGENTS.md) |
| Metallurgy | [domains/active_inference_metallurgy/AGENTS.md](./domains/active_inference_metallurgy/AGENTS.md) |
| Comedy | [domains/active_inference_comedy/AGENTS.md](./domains/active_inference_comedy/AGENTS.md) |

---

> *Minimize surprise. Maximize evidence.* -- Active Inference Institute
