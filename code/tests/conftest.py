# MultiPicoBoxV2 unit tests configuration (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Pytest documentation : https://docs.pytest.org

import os
import sys
import pytest
from unittest.mock import MagicMock

# Add parent 'tests' folder to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

mock_busio = MagicMock()
mock_digitalio = MagicMock()
mock_rotaryio = MagicMock()
mock_mcp = MagicMock()

mock_digitalio.Direction = MagicMock(INPUT="INPUT", OUTPUT="OUTPUT")
mock_digitalio.Pull = MagicMock(UP="UP", DOWN="DOWN")

sys.modules["busio"] = mock_busio
sys.modules["digitalio"] = mock_digitalio
sys.modules["rotaryio"] = mock_rotaryio
sys.modules["adafruit_mcp230xx.mcp23017"] = mock_mcp


@pytest.fixture(autouse=True)
def clean_global_mocks():
    """Clean global mocks before each test"""
    mock_busio.reset_mock()
    mock_digitalio.reset_mock()
    mock_rotaryio.reset_mock()
    mock_mcp.reset_mock()
    mock_mcp.MCP23017.side_effect = None
