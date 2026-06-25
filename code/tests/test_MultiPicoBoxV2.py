# MultiPicoBoxV2 unit tests (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Pytest documentation : https://docs.pytest.org
# Unittest documentation : https://docs.python.org/3/library/unittest.html

import pytest
from MultiPicoBoxV2 import *
from conftest import mock_busio, mock_digitalio, mock_mcp

@pytest.fixture
def manager():
    """Fixture for each test"""
    pass