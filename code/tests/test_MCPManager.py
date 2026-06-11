# MultiPicoBoxV2 unit tests (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox

import pytest
import unittest
from unittest.mock import patch, MagicMock
from MultiPicoBoxV2 import *


@patch('MultiPicoBoxV2.MCP23017')  # Second
@patch('MultiPicoBoxV2.busio.I2C')  # First
class test_MCPManager(unittest.TestCase):

    def test_init_success(self, m_i2c_class, m_mcp_class):
        """Tests for the MCPManager sub-class"""

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
        """Tests where the MCP23017 is not found (Exception)"""

        m_i2c_instance = MagicMock()
        m_i2c_class.return_value = m_i2c_instance
        m_mcp_class.side_effect = Exception("No MCP23017 found !")
        # Fake MCP with fake pins
        I2C_address = 0x20
        my_mcp = MCPManager(94, 95, I2C_address)
        assert my_mcp._address is None
        m_i2c_instance.unlock.assert_called_once()

    def test_get_address(self, m_i2c_class, m_mcp_class):
        """Tests MCP23017 I2C address"""

        m_i2c_instance = MagicMock()
        m_i2c_class.return_value = m_i2c_instance
        m_mcp_instance = MagicMock()
        m_mcp_class.return_value = m_mcp_instance
        # Fake MCP with fake pins, with new address
        I2C_address = 0x22
        my_mcp = MCPManager(94, 95, I2C_address)
        assert my_mcp.get_address() == hex(I2C_address)

    def test_get_toggle(self, m_i2c_class, m_mcp_class):
        """Tests Toggle switch (2x DigitalInOut)"""
        pass

    def test_get_led(self, m_i2c_class, m_mcp_class):
        """Tests LEDs"""
        pass

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
