"""Inline HTML templates for the Danvas web UI.

All templates use f-string interpolation.  The design reuses the CSS language
from ``html_website/config.py`` — dark mode, resizable sidebar, collapsible
sections, responsive layout.
"""

from typing import Any, Dict, List

from . import config

# ──────────────────────────────────────────────────────────────────────────────
# Shared CSS
# ──────────────────────────────────────────────────────────────────────────────

DANVAS_CSS = """\
:root {
  --primary: #4f46e5;
  --primary-light: #818cf8;
  --primary-dark: #3730a3;
  --success: #10b981;
  --warning: #f59e0b;
  --danger: #ef4444;
  --bg: #f8fafc;
  --bg-card: #ffffff;
  --bg-sidebar: #1e1b4b;
  --text: #1e293b;
  --text-muted: #64748b;
  --text-sidebar: #e2e8f0;
  --border: #e2e8f0;
  --sidebar-width: 260px;
  --radius: 12px;
  --shadow: 0 1px 3px rgba(0,0,0,.08), 0 1px 2px rgba(0,0,0,.06);
  --shadow-lg: 0 10px 15px -3px rgba(0,0,0,.1), 0 4px 6px -4px rgba(0,0,0,.1);
  --font: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --transition: .2s ease;
}

body.dark-mode {
  --bg: #0f172a;
  --bg-card: #1e293b;
  --bg-sidebar: #0c0a1d;
  --text: #e2e8f0;
  --text-muted: #94a3b8;
  --border: #334155;
  --shadow: 0 1px 3px rgba(0,0,0,.3);
  --shadow-lg: 0 10px 15px -3px rgba(0,0,0,.4);
}

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* { margin:0; padding:0; box-sizing:border-box; }

body {
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  display: flex;
  min-height: 100vh;
  transition: background var(--transition), color var(--transition);
}

/* ── Sidebar ─────────────────────────────────────── */
.sidebar {
  width: var(--sidebar-width);
  background: var(--bg-sidebar);
  color: var(--text-sidebar);
  padding: 24px 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  position: fixed;
  top: 0; left: 0; bottom: 0;
  overflow-y: auto;
  z-index: 100;
  transition: transform .3s ease;
}

.sidebar .logo {
  font-size: 1.6rem;
  font-weight: 700;
  letter-spacing: -0.5px;
  margin-bottom: 4px;
  background: linear-gradient(135deg, var(--primary-light), #a78bfa);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.sidebar .tagline {
  font-size: .75rem;
  color: #94a3b8;
  margin-bottom: 20px;
}

.sidebar a {
  color: var(--text-sidebar);
  text-decoration: none;
  padding: 10px 14px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: .9rem;
  transition: background var(--transition);
}

.sidebar a:hover, .sidebar a.active {
  background: rgba(255,255,255,.1);
}

.sidebar a .icon { font-size: 1.1rem; }

.sidebar .section-title {
  font-size: .7rem;
  text-transform: uppercase;
  letter-spacing: 1.2px;
  color: #64748b;
  margin: 16px 0 6px 14px;
}

/* ── Main content ────────────────────────────────── */
.main {
  margin-left: var(--sidebar-width);
  flex: 1;
  padding: 32px 40px;
  max-width: 1200px;
}

.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 32px;
}

.top-bar h1 {
  font-size: 1.75rem;
  font-weight: 700;
}

.top-bar .actions { display: flex; gap: 10px; }

.btn {
  padding: 8px 18px;
  border-radius: 8px;
  border: none;
  font-size: .85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all var(--transition);
  font-family: var(--font);
}

.btn-primary {
  background: var(--primary);
  color: #fff;
}
.btn-primary:hover { background: var(--primary-dark); }

.btn-outline {
  background: transparent;
  border: 1.5px solid var(--border);
  color: var(--text);
}
.btn-outline:hover { border-color: var(--primary); color: var(--primary); }

/* ── Cards ───────────────────────────────────────── */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.card {
  background: var(--bg-card);
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: var(--shadow);
  transition: transform var(--transition), box-shadow var(--transition);
  border: 1px solid var(--border);
}

.card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
}

.card .card-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 8px;
}

.card .card-meta {
  font-size: .8rem;
  color: var(--text-muted);
  margin-bottom: 14px;
}

.card .card-link {
  display: inline-block;
  color: var(--primary);
  font-weight: 600;
  font-size: .85rem;
  text-decoration: none;
}
.card .card-link:hover { text-decoration: underline; }

/* ── Progress bar ────────────────────────────────── */
.progress-bar {
  height: 6px;
  border-radius: 3px;
  background: var(--border);
  margin: 12px 0 6px;
  overflow: hidden;
}
.progress-fill {
  height: 100%;
  border-radius: 3px;
  background: linear-gradient(90deg, var(--primary), var(--primary-light));
  transition: width .4s ease;
}

/* ── Tables ──────────────────────────────────────── */
.table-wrap {
  overflow-x: auto;
  border-radius: var(--radius);
  border: 1px solid var(--border);
  background: var(--bg-card);
  box-shadow: var(--shadow);
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: .88rem;
}

th, td {
  padding: 12px 16px;
  text-align: left;
  border-bottom: 1px solid var(--border);
}

th {
  background: var(--bg);
  font-weight: 600;
  font-size: .78rem;
  text-transform: uppercase;
  letter-spacing: .5px;
  color: var(--text-muted);
}

tr:hover td { background: rgba(79,70,229,.04); }

/* ── Announcement timeline ───────────────────────── */
.timeline { display: flex; flex-direction: column; gap: 16px; }

.timeline-item {
  background: var(--bg-card);
  border-radius: var(--radius);
  padding: 20px 24px;
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
  border-left: 4px solid var(--primary);
}

.timeline-item .tl-title { font-weight: 600; font-size: 1rem; margin-bottom: 4px; }
.timeline-item .tl-meta { font-size: .78rem; color: var(--text-muted); margin-bottom: 10px; }
.timeline-item .tl-body { font-size: .9rem; line-height: 1.6; }

/* ── Calendar ────────────────────────────────────── */
.event-list { display: flex; flex-direction: column; gap: 10px; }

.event-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 14px 18px;
  background: var(--bg-card);
  border-radius: var(--radius);
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
}

.event-date-badge {
  background: var(--primary);
  color: #fff;
  border-radius: 8px;
  padding: 8px 12px;
  text-align: center;
  min-width: 60px;
  font-weight: 600;
  font-size: .82rem;
}

.event-info .event-title { font-weight: 600; }
.event-info .event-desc { font-size: .82rem; color: var(--text-muted); }

/* ── Module list ─────────────────────────────────── */
.module-list { display: flex; flex-direction: column; gap: 10px; }

.module-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px 20px;
  background: var(--bg-card);
  border-radius: var(--radius);
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
  text-decoration: none;
  color: var(--text);
  transition: transform var(--transition), box-shadow var(--transition);
}

.module-item:hover {
  transform: translateX(4px);
  box-shadow: var(--shadow-lg);
}

.module-num {
  background: var(--primary);
  color: #fff;
  width: 40px; height: 40px;
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-weight: 700;
  font-size: .95rem;
}

.module-info .module-name { font-weight: 600; }
.module-info .module-files { font-size: .78rem; color: var(--text-muted); }

/* ── Forms ───────────────────────────────────────── */
.form-group { margin-bottom: 16px; }
.form-group label {
  display: block;
  font-weight: 600;
  font-size: .85rem;
  margin-bottom: 6px;
}

input[type="text"], input[type="number"], input[type="date"],
textarea, select {
  width: 100%;
  padding: 10px 14px;
  border-radius: 8px;
  border: 1.5px solid var(--border);
  background: var(--bg-card);
  color: var(--text);
  font-family: var(--font);
  font-size: .9rem;
  transition: border-color var(--transition);
}

input:focus, textarea:focus, select:focus {
  outline: none;
  border-color: var(--primary);
}

textarea { min-height: 120px; resize: vertical; }

/* ── Badge ───────────────────────────────────────── */
.badge {
  display: inline-block;
  padding: 3px 10px;
  border-radius: 20px;
  font-size: .72rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .5px;
}

.badge-instructor { background: #dbeafe; color: #1d4ed8; }
.badge-ta { background: #fef3c7; color: #92400e; }
.badge-student { background: #d1fae5; color: #065f46; }

body.dark-mode .badge-instructor { background: #1e3a5f; color: #93c5fd; }
body.dark-mode .badge-ta { background: #451a03; color: #fcd34d; }
body.dark-mode .badge-student { background: #064e3b; color: #6ee7b7; }

/* ── Mobile ──────────────────────────────────────── */
.mobile-toggle {
  display: none;
  position: fixed;
  top: 14px; left: 14px;
  z-index: 200;
  background: var(--primary);
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 8px 12px;
  font-size: 1.2rem;
  cursor: pointer;
}

@media (max-width: 768px) {
  .sidebar { transform: translateX(-100%); }
  .sidebar.open { transform: translateX(0); }
  .main { margin-left: 0; padding: 24px 16px; padding-top: 60px; }
  .mobile-toggle { display: block; }
  .card-grid { grid-template-columns: 1fr; }
}

/* ── Empty state ─────────────────────────────────── */
.empty-state {
  text-align: center;
  padding: 60px 20px;
  color: var(--text-muted);
}
.empty-state .icon { font-size: 3rem; margin-bottom: 12px; }
.empty-state p { font-size: .95rem; }
"""

# ──────────────────────────────────────────────────────────────────────────────
# Base layout
# ──────────────────────────────────────────────────────────────────────────────

_BASE_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — Danvas</title>
  <style>{css}</style>
</head>
<body>
  <button class="mobile-toggle" onclick="document.querySelector('.sidebar').classList.toggle('open')">☰</button>
  {sidebar}
  <div class="main">
    {content}
  </div>
  <script>{js}</script>
</body>
</html>
"""

_DARK_MODE_JS = """\
function toggleDarkMode() {
  document.body.classList.toggle('dark-mode');
  localStorage.setItem('danvasDark', document.body.classList.contains('dark-mode'));
}
(function() {
  if (localStorage.getItem('danvasDark') === 'true') document.body.classList.add('dark-mode');
})();
"""


def _sidebar_html(active: str = "", course_id: str = "", course_title: str = "") -> str:
    """Build the sidebar HTML."""
    links = [
        ("🏠", "Dashboard", "/", "dashboard"),
    ]

    html = '<nav class="sidebar">\n'
    html += f'<div class="logo">{config.APP_NAME}</div>\n'
    html += f'<div class="tagline">{config.APP_TAGLINE}</div>\n'

    # Main nav
    for icon, label, href, key in links:
        cls = ' class="active"' if active == key else ""
        html += f'<a href="{href}"{cls}><span class="icon">{icon}</span> {label}</a>\n'

    # Course sub-nav
    if course_id:
        html += f'<div class="section-title">{course_title or course_id}</div>\n'
        course_links = [
            ("📚", "Modules", f"/course/{course_id}", "modules"),
            ("📊", "Gradebook", f"/course/{course_id}/gradebook", "gradebook"),
            ("📢", "Announcements", f"/course/{course_id}/announcements", "announcements"),
            ("📅", "Calendar", f"/course/{course_id}/calendar", "calendar"),
            ("👥", "Roster", f"/course/{course_id}/roster", "roster"),
        ]
        for icon, label, href, key in course_links:
            if not config.FEATURE_FLAGS.get(key, True) and key != "modules":
                continue
            cls = ' class="active"' if active == key else ""
            html += f'<a href="{href}"{cls}><span class="icon">{icon}</span> {label}</a>\n'

    # Footer
    html += '<div style="flex:1"></div>\n'
    html += '<a href="#" onclick="toggleDarkMode(); return false;"><span class="icon">🌓</span> Toggle Theme</a>\n'
    html += "</nav>\n"
    return html


def _page(
    title: str, content: str, active: str = "", course_id: str = "", course_title: str = ""
) -> str:
    """Wrap content in the full page layout."""
    return _BASE_TEMPLATE.format(
        title=title,
        css=DANVAS_CSS,
        sidebar=_sidebar_html(active, course_id, course_title),
        content=content,
        js=_DARK_MODE_JS,
    )


# ──────────────────────────────────────────────────────────────────────────────
# Public template functions
# ──────────────────────────────────────────────────────────────────────────────


def render_dashboard(courses: List[Dict[str, Any]]) -> str:
    """Render the main dashboard with course cards."""
    cards = ""
    for c in courses:
        cards += f"""
        <div class="card">
          <div class="card-title">{_esc(c["title"])}</div>
          <div class="card-meta">{c["module_count"]} modules</div>
          {f'<div class="card-meta">{_esc(c.get("description", ""))}</div>' if c.get("description") else ""}
          <div class="progress-bar"><div class="progress-fill" style="width:{min(c["module_count"] * 10, 100)}%"></div></div>
          <a class="card-link" href="/course/{c["id"]}">Open Course →</a>
        </div>"""

    if not courses:
        cards = """
        <div class="empty-state">
          <div class="icon">📚</div>
          <p>No courses discovered. Make sure <code>course_development/</code> exists.</p>
        </div>"""

    content = f"""
    <div class="top-bar">
      <h1>📚 My Courses</h1>
    </div>
    <div class="card-grid">{cards}</div>
    """
    return _page("Dashboard", content, active="dashboard")


def render_course_detail(
    course: Dict[str, Any],
    modules: List[Dict[str, Any]],
    announcements: List[Dict[str, Any]],
) -> str:
    """Render course detail / modules page."""
    mod_html = ""
    for m in modules:
        file_count = len(m.get("files", []))
        mod_html += f"""
        <a class="module-item" href="/course/{course["id"]}/module/{m["number"]}">
          <div class="module-num">{m["number"]}</div>
          <div class="module-info">
            <div class="module-name">{_esc(m["name"])}</div>
            <div class="module-files">{file_count} files</div>
          </div>
        </a>"""

    if not modules:
        mod_html = (
            '<div class="empty-state"><div class="icon">📂</div><p>No modules found.</p></div>'
        )

    # Recent announcements (up to 3)
    ann_html = ""
    for a in announcements[:3]:
        ann_html += f"""
        <div class="timeline-item">
          <div class="tl-title">{_esc(a["title"])}</div>
          <div class="tl-meta">{_esc(a.get("author", ""))} · {_esc(a.get("posted_at", ""))}</div>
          <div class="tl-body">{_esc(a["body"][:200])}</div>
        </div>"""

    content = f"""
    <div class="top-bar">
      <h1>{_esc(course["title"])}</h1>
      <div class="actions">
        <a class="btn btn-outline" href="/">← All Courses</a>
      </div>
    </div>
    <h2 style="margin-bottom:16px; font-size:1.15rem;">Modules</h2>
    <div class="module-list">{mod_html}</div>
    {'<h2 style="margin:32px 0 16px; font-size:1.15rem;">Recent Announcements</h2><div class="timeline">' + ann_html + "</div>" if ann_html else ""}
    """
    return _page(
        course["title"],
        content,
        active="modules",
        course_id=course["id"],
        course_title=course["title"],
    )


def render_module_detail(course: Dict[str, Any], module: Dict[str, Any]) -> str:
    """Render a single module's file listing."""
    files_html = ""
    for f in sorted(module.get("files", [])):
        files_html += f"<tr><td>📄 {_esc(f)}</td></tr>\n"

    content = f"""
    <div class="top-bar">
      <h1>Module {module["number"]}: {_esc(module["name"])}</h1>
      <div class="actions">
        <a class="btn btn-outline" href="/course/{course["id"]}">← Back to Modules</a>
      </div>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Files</th></tr></thead>
        <tbody>{files_html or '<tr><td class="empty-state">No files.</td></tr>'}</tbody>
      </table>
    </div>
    """
    return _page(
        f"Module {module['number']}",
        content,
        active="modules",
        course_id=course["id"],
        course_title=course["title"],
    )


def render_gradebook(course: Dict[str, Any], grades: Dict[str, Any]) -> str:
    """Render the gradebook page."""
    rows = ""
    for user, assignments in grades.items():
        for asg, entry in assignments.items():
            rows += f"""
            <tr>
              <td>{_esc(user)}</td>
              <td>{_esc(asg)}</td>
              <td>{_esc(entry.get("score", ""))}/{_esc(entry.get("max_score", ""))}</td>
              <td>{_esc(entry.get("percentage", ""))}%</td>
              <td>{_esc(entry.get("updated_at", ""))}</td>
            </tr>"""

    form = f"""
    <div class="card" style="margin-top:24px; max-width:500px;">
      <div class="card-title">Record Grade</div>
      <form method="POST" action="/course/{course["id"]}/gradebook">
        <div class="form-group"><label>Student</label><input type="text" name="user_name" required></div>
        <div class="form-group"><label>Assignment</label><input type="text" name="assignment" required></div>
        <div class="form-group"><label>Score</label><input type="number" name="score" step="0.1" required></div>
        <div class="form-group"><label>Max Score</label><input type="number" name="max_score" value="100" step="0.1"></div>
        <button class="btn btn-primary" type="submit">Save Grade</button>
      </form>
    </div>
    """

    content = f"""
    <div class="top-bar">
      <h1>📊 Gradebook</h1>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Student</th><th>Assignment</th><th>Score</th><th>%</th><th>Updated</th></tr></thead>
        <tbody>{rows or '<tr><td colspan="5" class="empty-state">No grades recorded yet.</td></tr>'}</tbody>
      </table>
    </div>
    {form}
    """
    return _page(
        "Gradebook",
        content,
        active="gradebook",
        course_id=course["id"],
        course_title=course["title"],
    )


def render_announcements(course: Dict[str, Any], announcements: List[Dict[str, Any]]) -> str:
    """Render the announcements timeline page."""
    items = ""
    for a in announcements:
        items += f"""
        <div class="timeline-item">
          <div class="tl-title">{_esc(a["title"])}</div>
          <div class="tl-meta">{_esc(a.get("author", ""))} · {_esc(a.get("posted_at", ""))}</div>
          <div class="tl-body">{_esc(a["body"])}</div>
        </div>"""

    if not announcements:
        items = (
            '<div class="empty-state"><div class="icon">📢</div><p>No announcements yet.</p></div>'
        )

    form = f"""
    <div class="card" style="margin-top:24px; max-width:600px;">
      <div class="card-title">Post Announcement</div>
      <form method="POST" action="/course/{course["id"]}/announcements">
        <div class="form-group"><label>Title</label><input type="text" name="title" required></div>
        <div class="form-group"><label>Author</label><input type="text" name="author" value="Instructor"></div>
        <div class="form-group"><label>Message</label><textarea name="body" required></textarea></div>
        <button class="btn btn-primary" type="submit">Post</button>
      </form>
    </div>
    """

    content = f"""
    <div class="top-bar"><h1>📢 Announcements</h1></div>
    <div class="timeline">{items}</div>
    {form}
    """
    return _page(
        "Announcements",
        content,
        active="announcements",
        course_id=course["id"],
        course_title=course["title"],
    )


def render_calendar(course: Dict[str, Any], events: List[Dict[str, Any]]) -> str:
    """Render the calendar events page."""
    items = ""
    for e in events:
        items += f"""
        <div class="event-item">
          <div class="event-date-badge">{_esc(e["date"])}</div>
          <div class="event-info">
            <div class="event-title">{_esc(e["title"])}</div>
            <div class="event-desc">{_esc(e.get("description", ""))}</div>
          </div>
        </div>"""

    if not events:
        items = (
            '<div class="empty-state"><div class="icon">📅</div><p>No events scheduled.</p></div>'
        )

    form = f"""
    <div class="card" style="margin-top:24px; max-width:500px;">
      <div class="card-title">Add Event</div>
      <form method="POST" action="/course/{course["id"]}/calendar">
        <div class="form-group"><label>Title</label><input type="text" name="title" required></div>
        <div class="form-group"><label>Date</label><input type="date" name="date" required></div>
        <div class="form-group"><label>Type</label>
          <select name="event_type">
            <option value="assignment">Assignment</option>
            <option value="lecture">Lecture</option>
            <option value="exam">Exam</option>
            <option value="holiday">Holiday</option>
            <option value="other">Other</option>
          </select>
        </div>
        <div class="form-group"><label>Description</label><textarea name="description"></textarea></div>
        <button class="btn btn-primary" type="submit">Add Event</button>
      </form>
    </div>
    """

    content = f"""
    <div class="top-bar"><h1>📅 Calendar</h1></div>
    <div class="event-list">{items}</div>
    {form}
    """
    return _page(
        "Calendar",
        content,
        active="calendar",
        course_id=course["id"],
        course_title=course["title"],
    )


def render_roster(course: Dict[str, Any], enrollments: List[Dict[str, Any]]) -> str:
    """Render the roster / enrollment page."""
    rows = ""
    for e in enrollments:
        role = e.get("role", "student")
        badge_cls = f"badge-{role}" if role in {"instructor", "ta", "student"} else "badge-student"
        rows += f"""
        <tr>
          <td>{_esc(e["user_name"])}</td>
          <td><span class="badge {badge_cls}">{_esc(role)}</span></td>
          <td>{_esc(e.get("enrolled_at", ""))}</td>
        </tr>"""

    form = f"""
    <div class="card" style="margin-top:24px; max-width:500px;">
      <div class="card-title">Enroll User</div>
      <form method="POST" action="/course/{course["id"]}/roster">
        <div class="form-group"><label>Name</label><input type="text" name="user_name" required></div>
        <div class="form-group"><label>Role</label>
          <select name="role">
            <option value="student">Student</option>
            <option value="ta">TA</option>
            <option value="instructor">Instructor</option>
          </select>
        </div>
        <button class="btn btn-primary" type="submit">Enroll</button>
      </form>
    </div>
    """

    content = f"""
    <div class="top-bar"><h1>👥 Roster</h1></div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Name</th><th>Role</th><th>Enrolled</th></tr></thead>
        <tbody>{rows or '<tr><td colspan="3" class="empty-state">No enrolled users.</td></tr>'}</tbody>
      </table>
    </div>
    {form}
    """
    return _page(
        "Roster",
        content,
        active="roster",
        course_id=course["id"],
        course_title=course["title"],
    )


def render_404() -> str:
    """Render a 404 page."""
    content = """
    <div class="empty-state" style="padding-top:120px;">
      <div class="icon">🔍</div>
      <p style="font-size:1.2rem; font-weight:600;">Page Not Found</p>
      <p style="margin-top:8px;"><a href="/" style="color:var(--primary)">← Back to Dashboard</a></p>
    </div>
    """
    return _page("Not Found", content)


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────


def _esc(text: str) -> str:
    """Basic HTML escaping."""
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#x27;")
    )
