# MultiPicoBoxV2 unit tests (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Pytest documentation : https://docs.pytest.org
# Unittest documentation : https://docs.python.org/3/library/unittest.html

import pytest
from unittest.mock import patch, MagicMock
from MultiPicoBoxV2 import *
from conftest import mock_busio, mock_digitalio, mock_mcp


@pytest.fixture
def my_box():
    """Fixture for the main class"""
    # Internal mocks (from MultiPicoBoxV2 class)
    from conftest import mock_encoder_mgr, mock_button_mgr, mock_mcp_mgr

    return MultiPicoBoxV2()


@pytest.fixture
def manager():
    """Fixture for MCP tests"""
    return MCPManager(94, 95)


def test_init_rotary_encoders(my_box):
    """Test for the rotary encoders (4)"""
    assert len(my_box.get_all_rot_encoders()) == 4
    assert all(
        isinstance(item, EncoderManager) for item in my_box.get_all_rot_encoders()
    )
    # Constants dictionnary
    assert "SW5" in my_box.rotary_encoders  # First
    assert my_box.C_SW5 == "SW5"
    assert "SW8" in my_box.rotary_encoders  # Last
    assert my_box.C_SW8 == "SW8"


def test_init_push_buttons(my_box):
    """Test for the push buttons (4)"""
    assert len(my_box.get_all_push_buttons()) == 4
    assert all(
        isinstance(item, ButtonManager) for item in my_box.get_all_push_buttons()
    )
    # Constants dictionnary
    assert "SW9" in my_box.push_buttons  # First
    assert my_box.C_SW9 == "SW9"
    assert "SW12" in my_box.push_buttons  # Last
    assert my_box.C_SW12 == "SW12"


def test_init_momentary_switches(my_box):
    """Test for the push buttons (4)"""
    assert len(my_box.get_all_mom_switches()) == 4
    assert all(
        isinstance(item, ButtonManager) for item in my_box.get_all_mom_switches()
    )
    # Constants dictionnary
    assert "SW13" in my_box.moment_switches  # First
    assert my_box.C_SW13 == "SW13"
    assert "SW16" in my_box.moment_switches  # Last
    assert my_box.C_SW16 == "SW16"


def test_init_toggle_switches(my_box):
    """Test for the toggle switches (8 switches -> 4 toggles switches)"""
    assert len(my_box.get_all_tog_switches()) == 4
    # Constants dictionnary
    assert "TSSW1_1" in my_box.toggle_switches  # First
    assert my_box.C_TSSW1_1 == "TSSW1_1"
    assert "TSSW4_1" in my_box.toggle_switches  # Last
    assert my_box.C_TSSW4_1 == "TSSW4_1"


def test_switch_mcp_leds(manager, my_box):
    """Test for switching ON/OFF the MCP LEDs and outputs"""
    led = manager.get_led(99, "d1")
    assert led[0].direction == "OUTPUT"
    assert led[0].value == False
    my_box.switch_mcp_leds([["d1", 1]])  # Lowercase, ON
    assert led[0].value == True
    my_box.switch_mcp_leds([["D1", 0]])  # Uppercase, OFF
    assert led[0].value == False


def test_raises_switch_mcp_leds(my_box):
    """Test for raising error to switch ON/OFF the MCP LEDs and outputs"""
    with pytest.raises(ValueError):
        # D99 don't exist in the board (D1 -> D6, GPA7, GPB7)
        my_box.switch_mcp_leds([["D99", 1]])
