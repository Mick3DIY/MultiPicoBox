# MultiPicoBoxV2 unit tests (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Pytest documentation : https://docs.pytest.org
# Unittest documentation : https://docs.python.org/3/library/unittest.html

import pytest
from MultiPicoBoxV2 import MCPManager
from conftest import mock_busio, mock_digitalio, mock_mcp

I2C_address = 0x20


@pytest.fixture
def manager():
    """Fixture for each test"""
    return MCPManager(94, 95)


def test_init_success(manager):
    """Test for the MCP itself"""
    assert manager.get_address() == hex(I2C_address)
    mock_busio.I2C.assert_called_once_with(94, 95)
    mock_busio.I2C.return_value.unlock.assert_called_once()
    mock_mcp.MCP23017.assert_called_once_with(mock_busio.I2C.return_value, I2C_address)


def test_init_failure():
    """Test where the MCP is not found (Exception) without fixture"""
    mock_mcp.MCP23017.side_effect = Exception("No MCP23017 found !")
    manager_failed = MCPManager(96, 97, 0x98)
    assert manager_failed.get_address() == "None"


def test_get_toggle(manager):
    """Test Toggle switch (2x DigitalInOut) from the MCP"""
    toggle = manager.get_toggle(1, 2, "test_mcp_name")
    # manager._mcp.get_pin.assert_any_call(1)
    # manager._mcp.get_pin.assert_any_call(2)
    assert len(toggle) == 3  # DigitalInOut, DigitalInOut, str
    for i in range(2):
        assert toggle[i].direction == "INPUT"
        assert toggle[i].pull == "UP"
    # Toggle name in uppercase
    assert toggle[2] == "TEST_MCP_NAME"


def test_get_led(manager):
    """Test LED from the MCP"""
    led = manager.get_led(99)
    assert led.direction == "OUTPUT"
    assert led.value == False
    manager._mcp.get_pin.assert_called_with(99)


def test_str_representation(manager):
    """Test for the magic method __str__."""
    assert str(manager) == f"MCP23017 address: {hex(I2C_address)}"
