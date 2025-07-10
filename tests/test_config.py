"""
Tests for the configuration module.
"""

import pytest
from config import config_manager


def test_config_manager_initialization():
    """Test that config manager initializes correctly."""
    assert config_manager is not None
    assert hasattr(config_manager, 'config_path')


def test_get_interactive_frameworks():
    """Test getting interactive frameworks."""
    frameworks = config_manager.get_interactive_frameworks()
    assert isinstance(frameworks, dict)
    assert "nextjs" in frameworks
    assert "reactjs" in frameworks


def test_get_simple_frameworks():
    """Test getting simple frameworks."""
    frameworks = config_manager.get_simple_frameworks()
    assert isinstance(frameworks, dict)
    assert "express" in frameworks
    assert "flask" in frameworks


def test_get_framework_config():
    """Test getting framework configuration."""
    config = config_manager.get_framework_config("nextjs")
    assert isinstance(config, dict)
    assert "features" in config


def test_get_ui_config():
    """Test getting UI configuration."""
    config = config_manager.get_ui_config()
    assert isinstance(config, dict)
    assert "colors" in config


def test_invalid_framework_config():
    """Test getting config for invalid framework."""
    config = config_manager.get_framework_config("invalid_framework")
    assert config == {} 