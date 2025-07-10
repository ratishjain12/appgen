"""
Tests for the CLI functionality.
"""

import pytest
from typer.testing import CliRunner
from appgen.cli import app


@pytest.fixture
def runner():
    """Create a CLI runner for testing."""
    return CliRunner()


def test_cli_help(runner):
    """Test that the CLI shows help."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "AppGen" in result.output


def test_list_frameworks(runner):
    """Test listing frameworks."""
    result = runner.invoke(app, ["list-frameworks"])
    assert result.exit_code == 0
    assert "nextjs" in result.output
    assert "express" in result.output


def test_config_command(runner):
    """Test config command."""
    result = runner.invoke(app, ["config"])
    assert result.exit_code == 0
    assert "Configuration" in result.output


def test_create_help(runner):
    """Test create command help."""
    result = runner.invoke(app, ["create", "--help"])
    assert result.exit_code == 0
    assert "framework" in result.output


def test_preset_help(runner):
    """Test preset command help."""
    result = runner.invoke(app, ["preset", "--help"])
    assert result.exit_code == 0
    assert "preset" in result.output 