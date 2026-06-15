# MultiPicoBoxV2 unit tests (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Pytest documentation : https://docs.pytest.org

import pytest
import unittest
from unittest.mock import patch, MagicMock
from MultiPicoBoxV2 import *


@patch("MultiPicoBoxV2.MCP23017")  # Second
@patch("MultiPicoBoxV2.busio.I2C")  # First
class test_MCPManager(unittest.TestCase):

    def test_init_success(self, m_i2c_class, m_mcp_class):
        """Tests where the MCP is found, with default address"""

        m_i2c_instance = MagicMock()
        m_i2c_class.return_value = m_i2c_instance
        m_mcp_instance = MagicMock()
        m_mcp_class.return_value = m_mcp_instance
        # Fake MCP with fake pins
        I2C_address = 0x20
        my_mcp = MCPManager(94, 95)
        m_i2c_class.assert_called_once_with(94, 95)
        m_mcp_class.assert_called_once_with(m_i2c_instance, I2C_address)
        m_i2c_instance.unlock.assert_called_once()
        assert my_mcp._address == hex(I2C_address)
        assert my_mcp._mcp == m_mcp_instance

    def test_init_failure(self, m_i2c_class, m_mcp_class):
        """Tests where the MCP is not found (Exception)"""

        m_i2c_instance = MagicMock()
        m_i2c_class.return_value = m_i2c_instance
        m_mcp_class.side_effect = Exception("No MCP23017 found !")
        # Fake MCP with fake pins
        I2C_address = 0x20
        my_mcp = MCPManager(94, 95, I2C_address)
        assert my_mcp._address is None
        m_i2c_instance.unlock.assert_called_once()

    def test_get_address(self, m_i2c_class, m_mcp_class):
        """Tests the MCP I2C address"""

        m_i2c_instance = MagicMock()
        m_i2c_class.return_value = m_i2c_instance
        m_mcp_instance = MagicMock()
        m_mcp_class.return_value = m_mcp_instance
        # Fake MCP with fake pins, with new address
        I2C_address = 0x22
        my_mcp = MCPManager(94, 95, I2C_address)
        assert my_mcp.get_address() == hex(I2C_address)

    def test_get_toggle(self, m_i2c_class, m_mcp_class):
        """Tests Toggle switch (2x DigitalInOut) from the MCP"""

        m_i2c_instance = MagicMock()
        m_i2c_class.return_value = m_i2c_instance
        m_mcp_instance = MagicMock()
        m_mcp_class.return_value = m_mcp_instance
        m_pin1 = m_pin3 = MagicMock()
        m_mcp_instance.get_pin.side_effect = [m_pin1, m_pin3]
        # Fake MCP with fake pins
        my_mcp = MCPManager(m_pin1, m_pin3)
        toggle = my_mcp.get_toggle(1, 2, "test_mcp_name")
        assert len(toggle) == 3  # DigitalInOut, DigitalInOut, str
        for i in range(2):
            assert toggle[i].direction == "INPUT"
            assert toggle[i].pull == "UP"
        # Toggle name in uppercase
        assert toggle[2] == "TEST_MCP_NAME"

    def test_get_led(self, m_i2c_class, m_mcp_class):
        """Tests LEDs from the MCP"""
        m_i2c_instance = MagicMock()
        m_i2c_class.return_value = m_i2c_instance
        m_mcp_instance = MagicMock()
        m_mcp_class.return_value = m_mcp_instance
        m_led = MagicMock()
        m_led.direction = MagicMock(OUTPUT="OUTPUT")
        m_led.value == False
        m_mcp_instance.get_pin.return_value = m_led
        my_mcp = MCPManager(94, 95)
        # LED with fake pin
        led = my_mcp.get_led(96)
        assert led.direction == "OUTPUT"
        assert led.value == False

    def test_str_method(self, m_i2c_class, m_mcp_class):
        """Tests MCP __str__ method"""

        m_i2c_instance = MagicMock()
        m_i2c_class.return_value = m_i2c_instance
        m_mcp_instance = MagicMock()
        m_mcp_class.return_value = m_mcp_instance
        # Fake MCP with fake pins, with new address
        I2C_address = 0x24
        my_mcp = MCPManager(94, 95, I2C_address)
        assert str(my_mcp) == f"MCP23017 address: {hex(I2C_address)}"
