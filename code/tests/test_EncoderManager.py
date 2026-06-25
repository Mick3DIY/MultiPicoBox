# MultiPicoBoxV2 unit tests (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Pytest documentation : https://docs.pytest.org
# Unittest documentation : https://docs.python.org/3/library/unittest.html

import pytest
from MultiPicoBoxV2 import EncoderManager
from conftest import mock_digitalio, mock_rotaryio


@pytest.fixture
def manager():
    """Fixture for each test"""
    return EncoderManager(90, 91, 92, "test_encoder_name")


def test_init_success(manager):
    """Test for the Encoder itself"""
    assert manager.get_button().direction == "INPUT"
    assert manager.get_button().pull == "UP"
    # Encoder default positions
    assert manager.get_position() == 0
    assert manager.get_last_position() == 0
    # Encoder name in uppercase
    assert manager.get_name() == "TEST_ENCODER_NAME"
    mock_rotaryio.IncrementalEncoder.assert_called_once_with(90, 91)
    mock_digitalio.DigitalInOut.assert_called_once_with(92)


def test_positions(manager):
    """Test for the Encoder position"""
    manager.set_last_position(5)
    assert manager.get_last_position() == 5


def test_button_state(manager):
    """Test for the Encoder button"""
    manager._button.value = False
    assert manager.get_button().value == False
    manager._button.value = True
    assert manager.get_button().value == True


def test_str_representation(manager):
    """Test for the magic method __str__."""
    assert str(manager) == "Encoder: TEST_ENCODER_NAME"
