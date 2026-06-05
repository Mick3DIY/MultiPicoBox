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

# https://docs.circuitpython.org/en/latest/shared-bindings/rotaryio/index.htm
# Manual mocking for the rotaryio module
mock_rotaryio = MagicMock()
mock_rotaryio.IncrementalEncoder = MagicMock()
sys.modules["rotaryio"] = mock_rotaryio
# Manual mocking for the digitalio module
mock_digitalio = MagicMock()
mock_digitalio.DigitalInOut = MagicMock()
sys.modules["digitalio"] = mock_digitalio
