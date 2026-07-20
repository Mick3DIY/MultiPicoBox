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
    """Fixture for each test"""
    # Internal mocks (from MultiPicoBoxV2 class)
    from conftest import mock_encoder_mgr, mock_button_mgr, mock_mcp_mgr

    return MultiPicoBoxV2()


def test_init_rotary_encoders(my_box):
    """Test for the rotary encoders"""
    assert len(my_box.rotary_encoders) == len(my_box.get_all_rot_encoders())
    assert all(
        isinstance(item, EncoderManager) for item in my_box.get_all_rot_encoders()
    )
    assert "SW5" in my_box.rotary_encoders  # First
    assert my_box.C_SW5 == "SW5"
    assert "SW8" in my_box.rotary_encoders  # Last
    assert my_box.C_SW8 == "SW8"


def test_init_push_buttons(my_box):
    """Test for the push buttons"""
    assert len(my_box.push_buttons) == len(my_box.get_all_push_buttons())
    assert all(
        isinstance(item, ButtonManager) for item in my_box.get_all_push_buttons()
    )
    assert "SW9" in my_box.push_buttons  # First
    assert my_box.C_SW9 == "SW9"
    assert "SW12" in my_box.push_buttons  # Last
    assert my_box.C_SW12 == "SW12"


def test_init_momentary_switches(my_box):
    """Test for the push buttons"""
    assert len(my_box.moment_switches) == len(my_box.get_all_mom_switches())
    assert all(
        isinstance(item, ButtonManager) for item in my_box.get_all_mom_switches()
    )
    assert "SW13" in my_box.moment_switches  # First
    assert my_box.C_SW13 == "SW13"
    assert "SW16" in my_box.moment_switches  # Last
    assert my_box.C_SW16 == "SW16"


def test_init_toggle_switches(my_box):
    """Test for the toggle switches (8 switches -> 4 toggles switches)"""
    assert len(my_box.toggle_switches) / 2 == len(my_box.get_all_tog_switches())
    assert "TSSW1_1" in my_box.toggle_switches  # First
    assert my_box.C_TSSW1_1 == "TSSW1_1"
    assert "TSSW4_1" in my_box.toggle_switches  # Last
    assert my_box.C_TSSW4_1 == "TSSW4_1"
