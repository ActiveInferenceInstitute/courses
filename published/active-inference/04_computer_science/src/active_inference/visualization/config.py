"""Centralized visualization configuration.

Provides a ``VizConfig`` dataclass for runtime-configurable styling,
output paths, colour palettes, and accessibility settings.

Usage
-----
>>> from active_inference.visualization.config import get_config, configure
>>> configure(output_dir="./output", dpi=150)
>>> cfg = get_config()
>>> cfg.dpi  # 150

All visualization modules read from ``get_config()`` at render time,
so changes take effect immediately for subsequent plots.
"""

import os
import logging
from dataclasses import dataclass, field
from typing import Optional, Dict, Any

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")

logger = logging.getLogger(__name__)

# Default output directory (relative to the CS course root)
_DEFAULT_OUTPUT_DIR: str = os.path.join(
    os.path.dirname(__file__), "..", "..", "..", "output"
)


@dataclass
class VizConfig:
    """Runtime-configurable visualization settings.

    Attributes
    ----------
    output_dir : str
        Default directory for saved figures.
    dpi : int
        Figure resolution (dots per inch).
    font_size : int
        Base font size (≥16 for accessibility).
    title_size : int
        Title font size.
    label_size : int
        Axis label font size.
    tick_size : int
        Tick label font size.
    legend_size : int
        Legend font size.
    annotation_size : int
        In‑cell annotation font size.
    fig_width : float
        Default figure width (inches).
    fig_height : float
        Default figure height (inches).
    cmap_probability : str
        Colour map for probability matrices (0–1).
    cmap_diverging : str
        Colour map for signed values (e.g. log-preferences).
    cmap_concentration : str
        Colour map for Dirichlet concentrations.
    cmap_states : str
        Colour map for discrete state colouring.
    grid_alpha : float
        Alpha for grid lines.
    save_format : str
        Default file extension for saved figures (png, pdf, svg).
    style_overrides : dict
        Extra matplotlib rcParams to apply.
    """

    # ── Output ────────────────────────────────────────────────────────
    output_dir: str = ""
    save_format: str = "png"

    # ── Sizes ─────────────────────────────────────────────────────────
    dpi: int = 100
    font_size: int = 16
    title_size: int = 18
    label_size: int = 16
    tick_size: int = 14
    legend_size: int = 14
    annotation_size: int = 14
    fig_width: float = 10.0
    fig_height: float = 6.0

    # ── Colour palettes ───────────────────────────────────────────────
    cmap_probability: str = "YlOrRd"
    cmap_diverging: str = "RdBu_r"
    cmap_concentration: str = "viridis"
    cmap_states: str = "tab10"

    # ── Rendering ─────────────────────────────────────────────────────
    grid_alpha: float = 0.3

    # ── Advanced ──────────────────────────────────────────────────────
    style_overrides: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not self.output_dir:
            self.output_dir = os.path.abspath(_DEFAULT_OUTPUT_DIR)
        else:
            self.output_dir = os.path.abspath(self.output_dir)

    def apply(self) -> None:
        """Push settings to matplotlib rcParams."""
        rc = {
            "font.size": self.font_size,
            "axes.titlesize": self.title_size,
            "axes.labelsize": self.label_size,
            "legend.fontsize": self.legend_size,
            "xtick.labelsize": self.tick_size,
            "ytick.labelsize": self.tick_size,
            "figure.figsize": (self.fig_width, self.fig_height),
            "figure.dpi": self.dpi,
        }
        rc.update(self.style_overrides)
        plt.rcParams.update(rc)
        logger.debug("Applied VizConfig to rcParams: %s", rc)

    def ensure_output_dir(self) -> str:
        """Create output directory if it doesn't exist; return its path."""
        os.makedirs(self.output_dir, exist_ok=True)
        return self.output_dir

    def output_path(self, filename: str) -> str:
        """Build a full path under ``output_dir`` for a filename.

        Appends ``save_format`` extension if not already present.
        """
        if "." not in os.path.basename(filename):
            filename = f"{filename}.{self.save_format}"
        self.ensure_output_dir()
        return os.path.join(self.output_dir, filename)


# ── Module-level singleton ────────────────────────────────────────────
_config: VizConfig = VizConfig()
_config.apply()


def get_config() -> VizConfig:
    """Return the current global ``VizConfig``."""
    return _config


def configure(**kwargs) -> VizConfig:
    """Update the global ``VizConfig`` and re-apply to matplotlib.

    Parameters
    ----------
    **kwargs
        Any ``VizConfig`` field name and value.  Invalid fields raise
        ``TypeError``.

    Returns
    -------
    VizConfig
        The updated configuration.

    Examples
    --------
    >>> configure(dpi=150, output_dir="./output")
    >>> configure(cmap_probability="Blues", font_size=18)
    """
    global _config
    for key, val in kwargs.items():
        if not hasattr(_config, key):
            raise TypeError(f"VizConfig has no field '{key}'")
        setattr(_config, key, val)
    # Re-resolve output dir if changed
    if "output_dir" in kwargs:
        _config.output_dir = os.path.abspath(_config.output_dir)
    _config.apply()
    logger.info("VizConfig updated: %s", kwargs)
    return _config


def reset_config() -> VizConfig:
    """Reset the global ``VizConfig`` to defaults."""
    global _config
    _config = VizConfig()
    _config.apply()
    logger.info("VizConfig reset to defaults")
    return _config
