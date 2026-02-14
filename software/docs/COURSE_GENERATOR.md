# 🧬 Course Generator

> **Navigation**: [← Docs Index](README.md) | [Modules](MODULES.md) | [Course Catalog](COURSE_CATALOG.md)

Schema-driven curriculum generation tool. Creates directory structures and content scaffolds.

---

## 🚀 Quick Start

```bash
cd software

# List available curricula
uv run python -m src.course_generator.main list

# Generate a specific curriculum
uv run python -m src.course_generator.main generate active_inference_101
```

---

## 📐 The 8-Topic Spine

All curricula follow this canonical structure, adapted for the audience:

1. **Systems**
2. **Agents**
3. **Perception**
4. **Cognition**
5. **Action**
6. **Learning**
7. **Communication**
8. **Planning**

---

## 🤖 LLM Enrichment

Optionally use **Ollama** to flesh out the scaffolded content.

```bash
# Generate with AI enrichment
uv run python -m src.course_generator.main generate active_inference_101 --llm --model llama3.2
```

**Note**: Requires [Ollama](https://ollama.com) running locally.

---

## 📂 Output Structure

```
course_development/active_inference_101/
├── 01_introduction/
│   ├── 01_systems/
│   │   ├── module.md
│   │   ├── questions.md
│   │   ├── practice_quiz.md
│   │   ├── lab.md
│   │   └── AGENTS.md
...
```

---
*Last Updated: 2026-02-14*
