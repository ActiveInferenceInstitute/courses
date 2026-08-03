# 🤝 Contributing Guide

> **Navigation**: [← Docs Index](README.md) | [Testing](TESTING.md) | [Architecture](ARCHITECTURE.md)

We welcome contributions to the Active Inference Institute courses! This guide details our development standards and workflows.

---

## 🛠️ Development Setup

1. **Install uv**: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. **Clone & Sync**:

   ```bash
   git clone https://github.com/ActiveInferenceInstitute/courses.git
   cd courses/software
   uv sync
   ```

3. **Verify Environment**:

   ```bash
   uv run pytest tests/
   ```

---

## 🚨 The "No Mocks" Policy

**We do not use mocks, stubs, or fakes in our test suite.**

Everything must be tested against **real implementations**.

- **File System**: Use the `temp_dir` fixture to create real files.
- **External Libs**: Call the actual library functions (e.g., WeasyPrint, gTTS).
- **Network**: Tests that require internet should be marked (see [Testing](TESTING.md)).

### Why?

Mocks drift from reality. Real tests ensure that upgrades to our dependencies (like WeasyPrint 64.0) instantly reveal breaking changes in our pipeline.

---

## 📝 Code Standards

We use `ruff` (via `uv`) to enforce standards.

```bash
# Format code
uv run ruff format src/ scripts/

# Lint code
uv run ruff check src/ scripts/

# Type check
uv run mypy src/
```

### Module Structure

Every module in `src/` must follow the [Modular Architecture](ARCHITECTURE.md):

- `main.py`: **Public API**. Only these functions should be imported by other modules.
- `utils.py`: **Private logic**. Internal helpers not exposed to the rest of the system.
- `config.py`: **Configuration**. Constants and schemas.

---

## 🧪 Testing

We require **tests for all new features** using real implementations (no mocks). The
suite currently collects 1,014 tests with ~75% source coverage; the CI gate runs all
tests except the internet/API/whisper-marked ones (~995 passing) and does not configure
a `--cov-fail-under` threshold — new code should keep coverage from regressing.

```bash
# Run all tests
uv run pytest tests/ -v

# Run with coverage
uv run pytest tests/ --cov=src --cov-report=html
```

See **[TESTING.md](TESTING.md)** for detailed patterns on writing real-implementation tests.

---

## 📦 Adding a New Course

1. **Create Content**: Add your source files to `course_development/<new_course_id>/`.
2. **Register**: Add an entry to `COURSE_REGISTRY` in `src/batch_processing/config.py`.
3. **Enable**: Add the course ID to `publish.toml` (default to `false` if experimental).
4. **Test**: Run `uv run python scripts/generate_all_outputs.py --course <new_course_id>`.

---
*Last Updated: 2026-08-02*
