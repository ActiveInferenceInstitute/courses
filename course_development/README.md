# Active Inference Course Development

> **Active Inference Institute** | 10 Courses | 320 Modules | 3,400+ Files

This directory contains all course materials for the Active Inference Institute's curriculum. Each course follows the same 8-topic spiral structure (Systems, Agents, Perception, Cognition, Action, Learning, Communication, Planning) adapted for its target audience.

---

## Curriculum Map

### Core Curriculum

| Course | Audience | Description |
|--------|----------|-------------|
| [Active Inference](./active_inference/) | Graduate / Advanced | Full 4-perspective curriculum: Philosophy, Cognitive Science, Mathematics, Computer Science |

### Level-Adapted Curricula (Developmental Progression)

| Course | Audience | Description |
|--------|----------|-------------|
| [Elementary School](./active_inference_es/) | Grades K-5 | Story-based learning with drawings and simple systems |
| [Family](./active_inference_family/) | Families & Young Children | Family-centered activities connecting AI concepts to daily life |
| [Middle School](./active_inference_ms/) | Grades 6-8 | Real-life applications: phones, schools, social media, feedback loops |
| [High School](./active_inference_hs/) | Grades 9-12 | NGSS-aligned: Everyday Life, Biology & Health, Math Foundations, Technology & AI |
| [College 101](./active_inference_101/) | Undergraduates | First-semester introduction: Cognitive Science, Neuroscience, Formal Methods, Computation |
| [Advanced 401](./active_inference_401/) | Graduate Students | Research-level: Philosophical Foundations, Neural Dynamics, Information Geometry, Advanced Computation |

### Domain Curricula

| Course | Domain | Description |
|--------|--------|-------------|
| [Embodied Cognition](./domains/active_inference_embodied/) | Body & Movement | Felt sense, living presence, intuitive knowing, moving through the world |
| [Organizations](./domains/active_inference_organizations/) | Systems & Strategy | Organizational systems, collective intelligence, strategic modeling, digital transformation |
| [Robotics](./domains/active_inference_robotics/) | Engineering | Robotic systems, bio-inspired design, control & estimation, autonomous agents |

---

## Color Identity & Visual System

Each course has a distinct accent color, gradient, and semantic meaning used in dashboards and navigation.

| Course | Accent Color | Hex | Gradient | Semantic Meaning |
|--------|-------------|-----|----------|-----------------|
| Active Inference (Core) | Sky Blue | `#38bdf8` | Blue → Indigo | Foundational, intellectual |
| College 101 | Cyan | `#22d3ee` | Cyan → Purple | Fresh, accessible |
| Advanced 401 | Purple | `#a78bfa` | Purple → Pink | Advanced, sophisticated |
| Elementary School | Green | `#4ade80` | Green → Cyan | Growth, playful |
| Family | Orange | `#fb923c` | Orange → Yellow | Warm, nurturing |
| High School | Indigo | `#818cf8` | Indigo → Violet | Energetic, youthful |
| Middle School | Teal | `#2dd4bf` | Teal → Blue | Curious, explorative |
| Embodied Cognition | Rose | `#fb7185` | Rose → Purple | Somatic, intuitive |
| Organizations | Amber | `#fbbf24` | Amber → Red | Strategic, decisive |
| Robotics | Emerald | `#34d399` | Emerald → Blue | Technical, precise |

---

## Theory Framework

### The Free Energy Principle

The **Free Energy Principle (FEP)** unifies all 10 courses: every living system maintains itself by minimizing prediction error (variational free energy). **Active Inference** is the process framework — agents act on the world to confirm their predictions and update their models when surprised.

### The 8-Topic Dependency Chain

The 8 topics form a logical dependency chain, each building on the previous:

| # | Topic | FEP Role | Central Question |
|---|-------|----------|-----------------|
| 1 | **Systems** | What EXISTS | What defines a system's boundary? |
| 2 | **Agents** | Which systems ACT | What makes something an agent? |
| 3 | **Perception** | How agents SENSE | How do agents build internal models? |
| 4 | **Cognition** | How agents THINK | How are beliefs weighted and updated? |
| 5 | **Action** | How agents DO | How do agents select and execute policies? |
| 6 | **Learning** | How agents IMPROVE | How do agents improve their models? |
| 7 | **Communication** | How agents COORDINATE | How do agents share and align models? |
| 8 | **Planning** | How agents PLAN | How do agents reason about the future? |

### Spiral Learning

Each course revisits all 8 topics from a different disciplinary lens. A learner progressing through the developmental sequence (ES → Family → MS → HS → 101 → Core → 401) encounters the same conceptual spine at increasing levels of formalism — from stories and drawings to proofs and research proposals. The domain courses (Embodied, Organizations, Robotics) provide parallel professional applications of the same spine.

---

## Unit Directory

All 10 courses contain 4 units each (40 units total). Each unit contains 8 modules following the topic spine.

### Core Curriculum

| # | Active Inference (Core) |
|---|------------------------|
| 1 | Philosophy |
| 2 | Cognitive Science |
| 3 | Mathematics |
| 4 | Computer Science |

### Level-Adapted Curricula

| # | ES (K-5) | Family (0-6) | MS (6-8) | HS (9-12) | 101 (Undergrad) | 401 (PhD) |
|---|----------|-------------|----------|-----------|-----------------|-----------|
| 1 | Story Time | Growing Together | Real Life Skills | Everyday Life | Cognitive Science | Philosophical Foundations |
| 2 | Our Bodies | Tiny Bodies, Big Brains | Body Science | Biology & Health | Computational Neuroscience | Neuroscientific Frontiers |
| 3 | Counting & Patterns | Patterns in Play | Math Detectives | Math Foundations | Mathematical Frameworks | Advanced Theory |
| 4 | Robots & Helpers | Screens, Toys & Tools | Code & Create | Technology & AI | Implementation | Research Methods |

### Domain Curricula

| # | Embodied Cognition | Organizations | Robotics |
|---|-------------------|---------------|----------|
| 1 | Felt Sense | Organizational Systems | Robotic Systems |
| 2 | Living Presence | Collective Intelligence | Bio-Inspired Design |
| 3 | Intuitive Knowing | Strategic Modeling | Control & Estimation |
| 4 | Moving Through World | Digital Transformation | Autonomous Agents |

### YouTube Transcript Archive

| Course | Audience | Description |
|--------|----------|-------------|
| [YouTube Archive](./youtube/) | All | Transcript collection from Active Inference Institute YouTube channel (~2,600 videos across 38 playlists) |

---

## Course Structure

Every course contains **4 units** with **8 modules** each (32 modules total).

### Module Files (7 per module)

| File | Description |
|------|-------------|
| `module.md` | Full lesson content with objectives, concepts, examples |
| `questions.md` | 20 study questions |
| `practice_quiz.md` | Part A: Multiple Choice + Part B: Short Answer/Free Response |
| `lab.md` | Hands-on activity (lab type varies by course) |
| `dashboard.html` | Interactive HTML dashboard with quiz, concept cards, progress tracking |
| `README.md` | Module overview and navigation |
| `AGENTS.md` | Agent guidelines for content generation |

### Shared Resources (per course)

Each course has a `resources/` directory with:

- `notation_table.md` - Mathematical symbols and notation
- `glossary.md` - Key term definitions
- `references.md` - Citations and reading lists
- `cross_course_map.md` - Cross-course navigation
- `learning_pathways.md` - Suggested study orders
- `faq.md` - Frequently asked questions

---

## Statistics

| Metric | Value |
|--------|-------|
| Total Courses | 10 |
| YouTube Playlists | 90+ |
| Total Units | 40 |
| Total Modules | 320 |
| Files per Module | 7 |
| Total Content Files | 3,400+ |
| Interactive Dashboards | 320 |
| Audience Range | K-5 through Graduate |

---

## Tools

| Script | Location | Description |
|--------|----------|-------------|
| `generate_dashboards.py` | `software/scripts/` | Regenerate interactive dashboards from module content |
| `publish.py` | Repo root | Full rendering pipeline (PDF, HTML, DOCX, TXT, MP3, MD) |
| `audit_modules.sh` | `active_inference/` | Structural validation (core curriculum only) |
| `fix_stub_*.py` | `software/scripts/` | Batch expand content for labs, quizzes, and questions |

---

> *Minimize surprise. Maximize evidence.* -- Active Inference Institute
