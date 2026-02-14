# Danvas — Course Management Server

> **Navigation**: [← Docs Index](README.md) | [Modules](MODULES.md) | [Configuration](CONFIGURATION.md)

Danvas is a lightweight, self-hosted course management system found in `software/src/danvas/`.

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

---

## 🛠️ Features

- **Course Browser**: Auto-generated from your local `course_development/` folder.
- **Gradebook**: Track student progress (stored locally).
- **Announcements**: Post updates to course streams.
- **Roster**: Manage student enrollment.

---

## ⚙️ Configuration

| Option | Default | Description |
| :--- | :--- | :--- |
| `--port` | `8420` | Server port |
| `--host` | `127.0.0.1` | Bind address |
| `--data-dir` | `~/.danvas/` | Location of JSON database |

---
*Last Updated: 2026-02-14*
