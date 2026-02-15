# Danvas — Course Management Server

> **Navigation**: [← Docs Index](README.md) | [Modules](MODULES.md) | [Configuration](CONFIGURATION.md)

Danvas is a lightweight, self-hosted course management system found in `software/src/danvas/`. It provides a browser-based interface for browsing courses, tracking progress, and managing student rosters — all without external dependencies.

---

## 🚀 Quick Start

```bash
cd software

# Start the server (auto-discovers courses from COURSE_REGISTRY)
uv run python -m src.danvas.main --repo-root ..
```

Open **`http://127.0.0.1:8420`** in your browser.

---

## 🏗️ Architecture

Built on Python's standard `http.server` with **zero external dependencies**.

| Component | Description |
| :--- | :--- |
| **Router** | URL pattern matching to handlers. |
| **Store** | JSON-backed persistence in `~/.danvas/`. |
| **Discovery** | Scans `COURSE_REGISTRY` for available content. |
| **Templates** | Inline HTML for zero-dependency deployment. |

### Design Principles

- **No database required**: All data stored as flat JSON files.
- **No JavaScript frameworks**: Pure HTML served from Python string templates.
- **Portable**: Runs anywhere Python runs — no Docker, no npm, no build step.
- **Registry-aware**: Automatically discovers all courses defined in `COURSE_REGISTRY`.

---

## 🛠️ Features

- **Course Browser**: Auto-generated from your local `course_development/` folder. Displays all 17 courses across levels and domains.
- **Gradebook**: Track student progress per module and unit (stored locally as JSON).
- **Announcements**: Post updates to course streams.
- **Roster**: Manage student enrollment per course.

### API Endpoints

| Method | Path | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Dashboard with course listing |
| `GET` | `/course/<id>` | Course detail view with unit/module navigation |
| `GET` | `/gradebook/<id>` | Per-course gradebook view |
| `POST` | `/gradebook/<id>` | Update grades for a student |
| `GET` | `/roster/<id>` | Student enrollment list |
| `POST` | `/announcement/<id>` | Post a new announcement |

---

## ⚙️ Configuration

| Option | Default | Description |
| :--- | :--- | :--- |
| `--port` | `8420` | Server port |
| `--host` | `127.0.0.1` | Bind address |
| `--repo-root` | `..` | Path to the repository root |
| `--data-dir` | `~/.danvas/` | Location of JSON database |

### Data Directory Structure

```
~/.danvas/
├── gradebook.json      # Student grades per course/module
├── roster.json         # Student enrollment
└── announcements.json  # Posted announcements
```

---

## 🧪 Testing

```bash
cd software
uv run pytest tests/test_danvas/ -v
```

The Danvas tests use **real HTTP requests** (no mocks), verifying actual server behavior including course discovery, template rendering, and data persistence.

---
*Last Updated: 2026-02-15*
