# MultiPicoBoxV2 unit tests configuration (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Pytest documentation : https://docs.pytest.org

import os
import sys

# https://docs.python.org/3/library/unittest.html
from unittest.mock import MagicMock

# Add parent 'tests' folder to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# https://circuitpython-mocks.readthedocs.io/en/latest/
# Manual mocking for the I2C, SPI, UART, DigitalInOut
pytest_plugins = ["circuitpython_mocks.fixtures"]

# https://docs.circuitpython.org/en/latest/shared-bindings/busio/
# https://docs.circuitpython.org/en/latest/shared-bindings/digitalio/index.html
# Manual mocking for the busio, digitalio modules
mock_busio = MagicMock()
mock_digitalio = MagicMock()
mock_digitalio.Direction = MagicMock(INPUT="INPUT", OUTPUT="OUTPUT")
mock_digitalio.Pull = MagicMock(UP="UP", DOWN="DOWN", NONE="NONE")
sys.modules["busio"] = mock_busio
sys.modules["digitalio"] = mock_digitalio

# https://docs.circuitpython.org/en/latest/shared-bindings/rotaryio/index.htm
# Manual mocking for the rotaryio module
mock_rotaryio = MagicMock()
mock_rotaryio.IncrementalEncoder = MagicMock()
sys.modules["rotaryio"] = mock_rotaryio

# https://docs.circuitpython.org/projects/mcp230xx/en/latest/
# Manual mocking for the MCP23017
mock_mcpmodule = MagicMock()
mock_mcpclass = MagicMock()
mock_mcpmodule.MCP23017 = mock_mcpclass
sys.modules["adafruit_mcp230xx"] = mock_mcpmodule
sys.modules["adafruit_mcp230xx.mcp23017"] = mock_mcpmodule
