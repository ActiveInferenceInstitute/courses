
import pytest
import os
import matplotlib.pyplot as plt
from active_inference.visualization.config import (
    VizConfig,
    configure,
    get_config,
    reset_config,
    _DEFAULT_OUTPUT_DIR
)

def test_viz_config_defaults():
    """Test default configuration values."""
    reset_config()
    cfg = get_config()
    assert cfg.dpi == 100
    assert cfg.font_size == 16
    assert cfg.save_format == "png"
    # Check default output dir resolves correctly
    assert os.path.isabs(cfg.output_dir)
    assert cfg.output_dir.endswith("output")

def test_configure_updates():
    """Test updating configuration."""
    reset_config()
    configure(dpi=200, font_size=12)
    cfg = get_config()
    assert cfg.dpi == 200
    assert cfg.font_size == 12
    # Verify it applied to matplotlib
    assert plt.rcParams["figure.dpi"] == 200
    assert plt.rcParams["font.size"] == 12

def test_configure_invalid_key():
    """Test that invalid keys raise TypeError."""
    reset_config()
    with pytest.raises(TypeError, match="VizConfig has no field 'invalid_key'"):
        configure(invalid_key="value")

def test_output_path_resolution(tmp_path):
    """Test output path generation and directory creation."""
    reset_config()
    # Use a temporary directory
    target_dir = tmp_path / "test_output"
    configure(output_dir=str(target_dir), save_format="pdf")
    
    cfg = get_config()
    assert cfg.output_dir == str(target_dir)
    
    # Test output_path generates correct path and suffix
    path = cfg.output_path("my_figure")
    assert path == str(target_dir / "my_figure.pdf")
    # Verify directory was created
    assert target_dir.exists()

def test_output_path_with_extension(tmp_path):
    """Test output path preserves existing extension."""
    reset_config()
    target_dir = tmp_path / "test_output_2"
    configure(output_dir=str(target_dir))
    
    path = cfg = get_config().output_path("my_figure.svg")
    assert path.endswith("my_figure.svg")

def test_style_overrides():
    """Test applying arbitrary style overrides."""
    reset_config()
    configure(style_overrides={"lines.linewidth": 5})
    assert plt.rcParams["lines.linewidth"] == 5

def test_post_init_rel_path():
    """Test that relative paths in init are made absolute."""
    cfg = VizConfig(output_dir="./rel_path")
    assert os.path.isabs(cfg.output_dir)
    assert cfg.output_dir.endswith("rel_path")
