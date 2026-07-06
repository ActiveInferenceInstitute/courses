"""Middleware utilities for Danvas.

Provides feature-flag gating, role-based permission checking, and
request logging wrappers that can be composed around handler functions.
"""

from typing import Dict, List, Optional

from . import config

try:
    from ..batch_processing.logging_config import get_logger
except Exception:
    import logging

    def get_logger(name: str) -> logging.Logger:
        """Fallback logger factory."""
        _logger = logging.getLogger(name)
        if not _logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter("%(levelname)s | %(name)s | %(message)s"))
            _logger.addHandler(handler)
            _logger.setLevel(logging.INFO)
        return _logger


logger = get_logger("danvas.middleware")


# ──────────────────────────────────────────────────────────────────────────────
# Feature-flag middleware
# ──────────────────────────────────────────────────────────────────────────────

# Maps handler name prefixes to feature flags
_FEATURE_MAP: Dict[str, str] = {
    "gradebook": "gradebook",
    "announcements": "announcements",
    "calendar": "calendar",
    "roster": "roster",
}


def check_feature_flag(handler_name: str) -> bool:
    """Return ``True`` if the feature for *handler_name* is enabled.

    If no feature flag applies to the handler, returns ``True``
    (default-open).
    """
    for prefix, flag in _FEATURE_MAP.items():
        if prefix in handler_name:
            enabled = config.FEATURE_FLAGS.get(flag, True)
            if not enabled:
                logger.info("Feature '%s' is disabled — blocking %s", flag, handler_name)
            return enabled
    return True


# ──────────────────────────────────────────────────────────────────────────────
# Permission middleware
# ──────────────────────────────────────────────────────────────────────────────

# Maps handler name keywords to required permission strings
_PERMISSION_MAP: Dict[str, str] = {
    "handle_gradebook_post": "edit_gradebook",
    "handle_gradebook": "view_gradebook",
    "handle_announcements_post": "post_announcement",
    "handle_announcements": "view_announcement",
    "handle_calendar_post": "manage_calendar",
    "handle_calendar": "view_calendar",
    "handle_roster_post": "manage_roster",
    "handle_roster": "view_roster",
    "handle_course_detail": "view_course",
    "handle_dashboard": "view_course",
}


def check_permission(handler_name: str, role: str) -> bool:
    """Return ``True`` if *role* has permission for *handler_name*.

    If no permission mapping exists for the handler, returns ``True``
    (default-open).

    Args:
        handler_name: The handler function name.
        role: User role (must be one of ``config.ROLES``).

    Returns:
        ``True`` if access is allowed, ``False`` otherwise.
    """
    required = _PERMISSION_MAP.get(handler_name)
    if required is None:
        return True

    permissions = config.ROLE_PERMISSIONS.get(role, [])
    allowed = required in permissions
    if not allowed:
        logger.warning(
            "Permission denied: role '%s' lacks '%s' for %s",
            role, required, handler_name,
        )
    return allowed


def get_permissions_for_role(role: str) -> List[str]:
    """Return the permission list for a given role.

    Args:
        role: User role string.

    Returns:
        List of permission strings, or empty list for unknown roles.
    """
    return config.ROLE_PERMISSIONS.get(role, [])


# ──────────────────────────────────────────────────────────────────────────────
# Request logging
# ──────────────────────────────────────────────────────────────────────────────


def log_request(method: str, path: str, handler_name: Optional[str] = None) -> None:
    """Log an incoming request.

    Args:
        method: HTTP method.
        path: Request path.
        handler_name: Matched handler name, or ``None`` for 404.
    """
    if handler_name:
        logger.info("%s %s → %s", method, path, handler_name)
    else:
        logger.info("%s %s → 404", method, path)
