# 🧬 Course Generator

> **Navigation**: [← Docs Index](README.md) | [Modules](MODULES.md) | [Course Catalog](COURSE_CATALOG.md)

Schema-driven curriculum generation tool. Creates directory structures and content scaffolds for new courses, following the standardized 4-unit × 8-module pattern.

---

## 🚀 Quick Start

```bash
cd software

# List available curricula
uv run python -m src.course_generator.main list

# Generate a specific curriculum
uv run python -m src.course_generator.main generate active_inference_101

# Generate with LLM enrichment
uv run python -m src.course_generator.main generate active_inference_101 --llm --model llama3.2
```

---

## 📐 The 8-Topic Spine

All curricula follow this canonical structure, adapted for the audience level and domain:

1. **Systems** — Foundational concepts and system boundaries
2. **Agents** — Autonomous entities and agent models
3. **Perception** — Sensory processing and observation models
4. **Cognition** — Internal model updating and belief revision
5. **Action** — Policy selection and motor control
6. **Learning** — Model adaptation and parameter updates
7. **Communication** — Information exchange between agents
8. **Planning** — Temporal reasoning and goal-directed behavior

Each topic maps to one module per unit, giving 8 modules × 4 units = **32 modules** per course.

---

## 🤖 LLM Enrichment

Optionally use **Ollama** to flesh out the scaffolded content with substantive, domain-appropriate material.

```bash
# Generate with AI enrichment
uv run python -m src.course_generator.main generate active_inference_101 --llm --model llama3.2
```

**Note**: Requires [Ollama](https://ollama.com) running locally.

### How LLM Enrichment Works

1. **Scaffold first**: Directory structure and file stubs are created.
2. **Context injection**: Each file stub includes metadata about the course, unit, module, topic, and target audience.
3. **Generation**: Ollama generates content that fills the stub, preserving the expected Markdown structure.
4. **Validation**: Output is checked against the expected file schema (`module.md`, `questions.md`, etc.).

---

## 📂 Output Structure

Each generated course follows a strict directory layout:

```
course_development/<course_id>/
├── syllabus.md
├── AGENTS.md
├── 01_introduction/
│   ├── AGENTS.md
│   ├── 01_systems/
│   │   ├── module.md         # Main lesson content
│   │   ├── questions.md      # Discussion/review questions
│   │   ├── practice_quiz.md  # Multiple-choice self-assessment
│   │   ├── lab.md            # Hands-on exercise
│   │   └── AGENTS.md
│   ├── 02_agents/
│   │   └── ...
│   └── ...
├── 02_core_concepts/
│   └── ...
├── 03_advanced_topics/
│   └── ...
└── 04_synthesis/
    └── ...
```

### Per-Module Content Files

| File | Purpose | Key Requirements |
| :--- | :--- | :--- |
| `module.md` | Main lesson content | 500+ words, structured with headers |
| `questions.md` | Discussion/review questions | 10 questions with model answers |
| `practice_quiz.md` | Multiple-choice quiz | 10 questions, 4 options each |
| `lab.md` | Hands-on exercise | Step-by-step instructions |

---

## 🔧 Customization

The generator schema is defined in `src/course_generator/config.py`. You can customize:

- **Unit names** per course (e.g., "Introduction", "Core Concepts", "Advanced Topics", "Synthesis")
- **Topic spine** (while the default 8-topic spine is recommended, it can be overridden)
- **Content file templates** (headers, metadata, placeholder text)
- **Target audience metadata** (grade level, prerequisites)

---
*Last Updated: 2026-02-15*
