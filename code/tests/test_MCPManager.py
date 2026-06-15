# MultiPicoBoxV2 unit tests (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Pytest documentation : https://docs.pytest.org

import pytest
import unittest
from unittest.mock import patch, MagicMock
from MultiPicoBoxV2 import MCPManager


@patch("MultiPicoBoxV2.MCP23017")  # Second
@patch("MultiPicoBoxV2.busio.I2C")  # First
class test_MCPManager(unittest.TestCase):

    def _setup_mocks(self, mock_i2c_class, mock_mcp_class):
        """Internal helper for common mocks"""
        self.m_i2c_instance = MagicMock()
        mock_i2c_class.return_value = self.m_i2c_instance
        self.m_mcp_instance = MagicMock()
        mock_mcp_class.return_value = self.m_mcp_instance
        return self.m_i2c_instance, self.m_mcp_instance

    def test_init_success(self, mock_i2c_class, mock_mcp_class):
        """Test where the MCP is found, with default address"""

        self._setup_mocks(mock_i2c_class, mock_mcp_class)
        # Fake MCP with fake pins
        I2C_address = 0x20
        my_mcp = MCPManager(94, 95)
        mock_i2c_class.assert_called_once_with(94, 95)
        mock_mcp_class.assert_called_once_with(self.m_i2c_instance, I2C_address)
        self.m_i2c_instance.unlock.assert_called_once()
        assert my_mcp._address == hex(I2C_address)
        assert my_mcp._mcp == self.m_mcp_instance

    def test_init_failure(self, mock_i2c_class, mock_mcp_class):
        """Test where the MCP is not found (Exception)"""

        self._setup_mocks(mock_i2c_class, mock_mcp_class)
        mock_mcp_class.side_effect = Exception("No MCP23017 found !")
        # Fake MCP with fake pins
        I2C_address = 0x20
        my_mcp = MCPManager(94, 95, I2C_address)
        mock_i2c_class.assert_called_once_with(94, 95)
        mock_mcp_class.assert_called_once_with(self.m_i2c_instance, I2C_address)
        assert my_mcp._address is None
        self.m_i2c_instance.unlock.assert_called_once()

    def test_get_address(self, mock_i2c_class, mock_mcp_class):
        """Test the MCP I2C address"""

        # Fake MCP with fake pins, with new address
        I2C_address = 0x22
        my_mcp = MCPManager(94, 95, I2C_address)
        assert my_mcp.get_address() == hex(I2C_address)

    def test_get_toggle(self, mock_i2c_class, mock_mcp_class):
        """Test Toggle switch (2x DigitalInOut) from the MCP"""

        # Fake MCP with fake pins
        my_mcp = MCPManager(94, 95)
        toggle = my_mcp.get_toggle(1, 2, "test_mcp_name")
        assert len(toggle) == 3  # DigitalInOut, DigitalInOut, str
        for i in range(2):
            assert toggle[i].direction == "INPUT"
            assert toggle[i].pull == "UP"
        # Toggle name in uppercase
        assert toggle[2] == "TEST_MCP_NAME"

    def test_get_led(self, mock_i2c_class, mock_mcp_class):
        """Test LEDs from the MCP"""

        # Fake MCP with fake pins
        my_mcp = MCPManager(94, 95)
        led = my_mcp.get_led(96)
        assert led.direction == "OUTPUT"
        assert led.value == False

    def test_str_method(self, m_i2c_class, m_mcp_class):
        """Test MCP __str__ method"""

        # Fake MCP with fake pins, with new address
        I2C_address = 0x24
        my_mcp = MCPManager(94, 95, I2C_address)
        assert str(my_mcp) == f"MCP23017 address: {hex(I2C_address)}"
