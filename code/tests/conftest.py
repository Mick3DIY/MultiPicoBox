# MultiPicoBoxV2 unit tests configuration (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Pytest documentation : https://docs.pytest.org

import os
import sys
import pytest
from unittest.mock import MagicMock

# Add parent 'tests' folder to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# External mocks (from Adafruit classes)
mock_board = MagicMock()
mock_busio = MagicMock()
mock_digitalio = MagicMock()
mock_rotaryio = MagicMock()
mock_mcp = MagicMock()
mock_digitalio.Direction = MagicMock(INPUT="INPUT", OUTPUT="OUTPUT")
mock_digitalio.Pull = MagicMock(UP="UP", DOWN="DOWN")

sys.modules["board"] = mock_board
sys.modules["busio"] = mock_busio
sys.modules["digitalio"] = mock_digitalio
sys.modules["rotaryio"] = mock_rotaryio
sys.modules["adafruit_mcp230xx.mcp23017"] = mock_mcp

# Internal mocks (from MultiPicoBoxV2 class)
mock_encoder_mgr = MagicMock()
mock_button_mgr = MagicMock()
mock_mcp_mgr = MagicMock()

sys.modules["encodermanager"] = mock_encoder_mgr
sys.modules["buttonmanager"] = mock_button_mgr
sys.modules["mcpmanager"] = mock_mcp_mgr


@pytest.fixture(autouse=True)
def clean_global_mocks():
    """Clean global mocks before each test"""
    for mock in [
        mock_board, mock_busio, mock_digitalio,
        mock_rotaryio, mock_mcp, 
        mock_encoder_mgr, mock_button_mgr, mock_mcp_mgr,]:
        mock.reset_mock()
    mock_mcp.MCP23017.side_effect = None
