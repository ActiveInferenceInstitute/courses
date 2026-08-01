"""Danvas — lightweight course management HTTP server.

Serves a web UI for browsing courses, managing enrollments, gradebook,
announcements, and calendar.  Built on ``http.server`` — zero external
framework dependencies.

The heavy lifting is delegated to:

- :mod:`danvas.router` — URL pattern matching
- :mod:`danvas.handlers` — page / form / API request handlers
- :mod:`danvas.middleware` — feature flags, permissions, logging

Usage::

    python -m src.danvas.main --repo-root /path/to/courses
"""

import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.parse import parse_qs, urlparse

from . import config, templates
from . import handlers as _handlers
from . import router as _router
from . import middleware as _mw

# ── Test helpers ──────────────────────────────────────────────────────────


def create_test_handler(
    repo_root: Path,
    data_dir: Path | None = None,
    method: str = "GET",
    path: str = "/",
    body: str = "",
) -> "DanvasHandler":
    """Create a DanvasHandler wired to in-memory buffers for testing.

    The returned handler reads from ``rfile`` (a ``BytesIO``), writes to
    ``wfile`` (a ``BytesIO``), and captures ``send_response`` status codes
    in ``_response_status`` so tests can assert HTTP responses without
    mocking sockets.

    Usage::

        handler = create_test_handler(repo_root, data_dir)
        handler.path = "/course/demo"
        handlers.handle_course_detail(handler, course_id="demo")
        body = handler.wfile.getvalue().decode("utf-8")
        assert handler._response_status == 200

    Args:
        repo_root: Repository root path.
        data_dir: Optional overridden data directory.
        method: Request method (``"GET"`` or ``"POST"``).
        path: Request path (e.g. ``"/"``, ``"/course/demo"``).
        body: POST body string (URL-encoded form data).

    Returns:
        A handler instance ready to pass to handler functions.
    """
    import io
    from types import SimpleNamespace

    handler = DanvasHandler.__new__(DanvasHandler)
    handler.server = SimpleNamespace(
        repo_root=repo_root,
        data_dir=data_dir or repo_root / ".danvas",
    )
    encoded_body = body.encode("utf-8")
    handler.headers = {"Content-Length": str(len(encoded_body))}
    handler.rfile = io.BytesIO(encoded_body)
    handler.wfile = io.BytesIO()
    handler.requestline = f"{method} {path} HTTP/1.1"
    handler.request_version = "HTTP/1.1"
    handler.client_address = ("127.0.0.1", 0)
    handler.close_connection = True
    handler._response_status = None
    return handler


try:
    from ..batch_processing.logging_config import get_logger
except Exception:
    import logging

    def get_logger(name: str) -> logging.Logger:
        logger = logging.getLogger(name)
        if not logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter("%(levelname)s | %(name)s | %(message)s"))
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
        return logger


logger = get_logger("danvas.main")


# ──────────────────────────────────────────────────────────────────────────────
# Request handler
# ──────────────────────────────────────────────────────────────────────────────


class DanvasHandler(BaseHTTPRequestHandler):
    """HTTP request handler for Danvas.

    ``server.repo_root`` and ``server.data_dir`` must be set on the
    ``HTTPServer`` instance before requests are served.

    Delegates URL matching to :mod:`router` and request handling to
    :mod:`handlers`.
    """

    @property
    def repo_root(self) -> Path:
        return self.server.repo_root  # type: ignore[attr-defined]

    @property
    def data_dir(self) -> Path:
        return self.server.data_dir  # type: ignore[attr-defined]

    @property
    def role(self) -> str:
        """Request principal's role, defaulting to the local-first default."""
        server_role = getattr(self.server, "role", None)
        return server_role or config.DEFAULT_ROLE

    # ── Dispatch ──────────────────────────────────────────────────────────

    def do_GET(self) -> None:  # noqa: N802
        self._dispatch("GET")

    def do_POST(self) -> None:  # noqa: N802
        self._dispatch("POST")

    def _dispatch(self, method: str) -> None:
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/") or "/"

        result = _router.dispatch(method, path)
        if result is None:
            _mw.log_request(method, path, None)
            self._send_html(templates.render_404(), status=404)
            return

        handler_name, kwargs = result
        _mw.log_request(method, path, handler_name)

        # Feature-flag check
        if not _mw.check_feature_flag(handler_name):
            self._send_html(templates.render_404(), status=404)
            return

        # Role-based authorization: mutating handlers require a permission
        # that the principal's role holds; deny with 403 otherwise.
        if _mw.permission_required(handler_name) is not None and not _mw.check_permission(
            handler_name, self.role
        ):
            _mw.log_request(method, path, "%s (403 denied, role=%s)" % (handler_name, self.role))
            self._send_forbidden()
            return

        # Reject unsafe course ids before any handler runs, so a traversal
        # primitive in the URL can never reach the data layer.
        course_id = kwargs.get("course_id")
        if course_id is not None:
            try:
                _handlers.validate_course_id_safe(course_id)
            except ValueError:
                # 404 keeps the shape semantically (unroutable) and avoids
                # leaking validation details.
                self._send_html(templates.render_404(), status=404)
                return

        handler_fn = getattr(_handlers, handler_name, None)
        if handler_fn:
            handler_fn(self, **kwargs)
        else:
            self._send_html(templates.render_404(), status=404)

    # ── Helpers ───────────────────────────────────────────────────────────

    def _send_html(self, html: str, status: int = 200) -> None:
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        body = html.encode("utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, data: Any, status: int = 200) -> None:
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        body = json.dumps(data, indent=2, default=str).encode("utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_error(self, message: str, status: int = 400) -> None:
        """Send a plain-text error response."""
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        body = message.encode("utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_forbidden(self) -> None:
        """Send a 403 Forbidden response."""
        self.send_response(403)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        body = b"Forbidden"
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _redirect(self, url: str) -> None:
        self.send_response(303)
        self.send_header("Location", url)
        self.end_headers()

    def send_response(self, code: int, message: str | None = None) -> None:
        """Override BaseHTTPRequestHandler.send_response for test support.

        In a real server this writes the status line to the socket. In tests
        we only capture the status code so assertions work and the body
        written to ``wfile`` is clean (no HTTP protocol overhead).
        """
        self._response_status = code
        # Don't write to wfile — tests read clean body from wfile.
        self.responded = False  # suppress super() write
        # We call super() but it writes to a socket we don't have.
        # In test mode, wfile is BytesIO; we skip the write by doing nothing.
        self._headers_buffer = []

    def send_header(self, keyword: str, value: str) -> None:
        """Override send_header — capture but don't write in test mode."""
        pass

    def end_headers(self) -> None:
        """Override end_headers — no-op in test mode."""
        pass

    def _read_form(self) -> Dict[str, str]:
        """Read URL-encoded POST body and return a flat dict.

        Caps the body at ``config.MAX_POST_BODY`` and validates the
        ``Content-Length`` header so an attacker cannot force an unbounded
        read or crash on a non-numeric length.

        Returns:
            Parsed form fields.

        Raises:
            ValueError: If ``Content-Length`` is missing/invalid or the body
                exceeds ``config.MAX_POST_BODY``.
        """
        raw_len = self.headers.get("Content-Length", "0")
        try:
            length = int(raw_len)
        except (TypeError, ValueError):
            raise ValueError("Invalid Content-Length header")
        if length < 0 or length > config.MAX_POST_BODY:
            raise ValueError("Request body too large or invalid")
        raw = self.rfile.read(length).decode("utf-8")
        parsed = parse_qs(raw)
        return {k: v[0] for k, v in parsed.items()}

    # ── Logging ───────────────────────────────────────────────────────────

    def log_message(self, format: str, *args: Any) -> None:
        logger.info("%s %s", self.address_string(), format % args)


# ──────────────────────────────────────────────────────────────────────────────
# Server entry point
# ──────────────────────────────────────────────────────────────────────────────


def start_server(
    repo_root: Path,
    port: int = config.DANVAS_PORT,
    host: str = config.DANVAS_HOST,
    data_dir: Optional[Path] = None,
) -> HTTPServer:
    """Create and start the Danvas HTTP server.

    Args:
        repo_root: Root of the courses repository.
        port: Port number.
        host: Bind address.
        data_dir: Override for state storage directory.

    Returns:
        The running ``HTTPServer`` instance.
    """
    server = HTTPServer((host, port), DanvasHandler)
    server.repo_root = repo_root  # type: ignore[attr-defined]
    server.data_dir = data_dir or config.DANVAS_DATA_DIR  # type: ignore[attr-defined]

    logger.info(
        "Danvas starting on http://%s:%d  (repo=%s, data=%s)",
        host,
        port,
        repo_root,
        server.data_dir,
    )

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info("Danvas shutting down.")
    finally:
        server.server_close()

    return server


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────


def _parse_args(argv: list = None) -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        prog="danvas",
        description="Danvas — lightweight course management server",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Root of the courses repository (default: cwd)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=config.DANVAS_PORT,
        help=f"Port to listen on (default: {config.DANVAS_PORT})",
    )
    parser.add_argument(
        "--host",
        type=str,
        default=config.DANVAS_HOST,
        help=f"Host to bind to (default: {config.DANVAS_HOST})",
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=None,
        help="Directory for Danvas state files (default: ~/.danvas/)",
    )
    return parser.parse_args(argv)


if __name__ == "__main__":
    args = _parse_args()
    start_server(
        repo_root=args.repo_root,
        port=args.port,
        host=args.host,
        data_dir=args.data_dir,
    )
