# MultiPicoBoxV2 unit tests configuration (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Pytest documentation : https://docs.pytest.org

import os
import sys

# https://docs.python.org/3/library/unittest.html
from unittest.mock import MagicMock

# Add parent 'tests' folder to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# https://docs.circuitpython.org/en/latest/shared-bindings/board/#module-board
# Manual mocking for the board
mock_board = MagicMock()
sys.modules["board"] = mock_board

# https://docs.circuitpython.org/en/latest/shared-bindings/busio/
# https://docs.circuitpython.org/en/latest/shared-bindings/digitalio/index.html
# Manual mocking for the busio, digitalio modules
mock_busio = MagicMock()
mock_digitalio = MagicMock()
mock_digitalio.Direction = MagicMock(INPUT="INPUT", OUTPUT="OUTPUT")
mock_digitalio.Pull = MagicMock(UP="UP", DOWN="DOWN")
sys.modules["busio"] = mock_busio
sys.modules["digitalio"] = mock_digitalio

# https://docs.circuitpython.org/en/latest/shared-bindings/rotaryio/index.htm
# Manual mocking for the rotaryio module
mock_rotaryio = MagicMock()
mock_rotaryio.IncrementalEncoder = MagicMock()
sys.modules["rotaryio"] = mock_rotaryio
