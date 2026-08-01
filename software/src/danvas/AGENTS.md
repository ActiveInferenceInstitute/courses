# Danvas — Course Management Module

**Module**: `src/danvas/`
**Purpose**: Self-hosted course management system (Canvas clone) for classroom orchestration.

## Architecture

```text
danvas/
├── __init__.py          # Public API re-exports
├── config.py            # Feature flags, roles, grading schema, storage defaults
├── templates.py         # Inline HTML templates (f-string based, no Jinja)
├── AGENTS.md            # This file
│
│  ── Data Layer ──────────────────────────────────────────────
├── store.py             # JSON-backed persistence (load/save with atomic writes)
├── discovery.py         # Course discovery via COURSE_REGISTRY + module scanning
├── enrollment.py        # Roster management (enroll, unenroll, get_roster)
├── gradebook.py         # Grade recording, retrieval, and course-grade calculation
├── announcements.py     # Announcement posting and retrieval
├── calendar_events.py   # Calendar event creation and retrieval
│
│  ── HTTP Layer ──────────────────────────────────────────────
├── router.py            # URL pattern table + dispatch function (14 routes)
├── handlers.py          # Page, form, and API request handler functions
├── middleware.py         # Feature-flag gating, role permissions, request logging
├── main.py              # DanvasHandler, HTTP server entry point, CLI
│
│  ── Compatibility ───────────────────────────────────────────
└── utils.py             # Thin re-export shim (all data-layer functions)
```

## Key Design Decisions

1. **Zero external framework** — uses `http.server.HTTPServer` + `BaseHTTPRequestHandler`
2. **JSON file storage** — state persisted to `~/.danvas/<course_id>/danvas_store.json`
3. **Atomic writes** — temp file + `os.replace()` prevents corruption
4. **COURSE_REGISTRY integration** — discovers courses via `batch_processing.config.COURSE_REGISTRY`
5. **Inline HTML templates** — matches `html_website` CSS design language
6. **Modular decomposition** — each concern (store, discovery, enrollment, gradebook, announcements, calendar, routing, handlers, middleware) lives in its own module
7. **Backward compatibility** — `utils.py` re-exports all data-layer functions; `DanvasHandler` has delegate methods forwarding to `handlers.py`

## Features

| Feature | Status | Toggle |
|---|---|---|
| Course dashboard | ✅ Active | — |
| Module browsing | ✅ Active | — |
| Gradebook | ✅ Active | `FEATURE_FLAGS["gradebook"]` |
| Announcements | ✅ Active | `FEATURE_FLAGS["announcements"]` |
| Calendar | ✅ Active | `FEATURE_FLAGS["calendar"]` |
| Roster/Enrollment | ✅ Active | `FEATURE_FLAGS["roster"]` |
| Discussions | 🔜 Planned | `FEATURE_FLAGS["discussions"]` |
| Analytics | 🔜 Planned | `FEATURE_FLAGS["analytics"]` |

## Routes

### Web UI

| Route | Method | Handler |
|---|---|---|
| `/` | GET | Dashboard |
| `/course/<id>` | GET | Course detail + modules |
| `/course/<id>/module/<num>` | GET | Module detail |
| `/course/<id>/gradebook` | GET/POST | Gradebook |
| `/course/<id>/announcements` | GET/POST | Announcements |
| `/course/<id>/calendar` | GET/POST | Calendar |
| `/course/<id>/roster` | GET/POST | Enrollment |

### JSON API

| Route | Method |
|---|---|
| `/api/courses` | GET |
| `/api/course/<id>/grades` | GET |
| `/api/course/<id>/announcements` | GET |

## Usage

```bash
python -m src.danvas.main --repo-root /path/to/courses --port 8420
```

## Data Model

Each course stores its state in `~/.danvas/<course_id>/danvas_store.json`:

```json
{
  "enrollments": [{"id": "uuid", "user_name": "...", "role": "student", "enrolled_at": "..."}],
  "grades": {"user_name": {"assignment": {"score": 95, "max_score": 100, "percentage": 95.0}}},
  "announcements": [{"id": "uuid", "title": "...", "body": "...", "author": "...", "posted_at": "..."}],
  "calendar_events": [{"id": "uuid", "title": "...", "date": "2026-02-11", "event_type": "assignment"}]
}
```

## Role Permissions

Mutating handlers are gated by role via `middleware.check_permission`. The
default request role is the local-first `config.DEFAULT_ROLE` (`instructor`
unless `DANVAS_ROLE` is set), so the tool works out of the box on loopback.
When binding a non-loopback host, set `DANVAS_ROLE` to a least-privilege role
and treat the server as unauthenticated (no login/session model is included):
any anonymous client that can reach the server acts under that role.

| Permission | Instructor | TA | Student |
|---|---|---|---|
| View course | ✅ | ✅ | ✅ |
| Edit course | ✅ | ❌ | ❌ |
| View gradebook | ✅ | ✅ | ✅ |
| Edit gradebook | ✅ | ✅ | ❌ |
| Post announcements | ✅ | ✅ | ❌ |
| Manage roster | ✅ | ❌ | ❌ |
| Manage calendar | ✅ | ❌ | ❌ |

Denials return HTTP 403.  Roles map to permissions in `config.ROLE_PERMISSIONS`.

## Security hardening

- **Path/identifier safety** — `course_id` is validated against a strict
  ``[A-Za-z0-9_-]`` whitelist (`store.validate_course_id`) and enforced both in
  the HTTP dispatch layer and the data layer, with a resolved-path containment
  check in `_store_path`. Traversal ids (`..`, `/`, `%`) are rejected (404).
- **Authorization** — role-based permission checks run for every mutating
  handler before it is invoked (see Role Permissions above).
- **Input validation** — grades must be finite numbers with non-negative
  `max_score`; calendar events require a valid `YYYY-MM-DD` date and a
  whitelisted `event_type`; announcement/author/user-name/event-title lengths
  are capped.
- **Body limits** — POST bodies are capped at `config.MAX_POST_BODY` (64 KiB)
  and `Content-Length` is validated; oversized/invalid requests return 400.
- **Concurrency & durability** — data-layer mutations run inside
  `store.store_transaction` (per-course lock preventing lost updates), and
  writes `fsync` before `os.replace` for durability. A corrupt/truncated store
  falls back to the empty state instead of crashing every request.

## Testing

```bash
uv run pytest tests/test_danvas_utils.py tests/test_danvas_main.py tests/test_danvas_comprehensive.py -v
```

Tests cover templates, HTML escaping, path-traversal rejection, role-based
authorization (403), body-limit enforcement, store transactions, edge cases,
input validation, multi-course isolation, config, API round-trips, and route
dispatch.
