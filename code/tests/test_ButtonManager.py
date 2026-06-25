# MultiPicoBoxV2 unit tests (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Pytest documentation : https://docs.pytest.org
# Unittest documentation : https://docs.python.org/3/library/unittest.html

import pytest
from MultiPicoBoxV2 import ButtonManager
from conftest import mock_digitalio


@pytest.fixture
def manager():
    """Fixture for each test"""
    return ButtonManager(93, "test_button_name")


def test_init_success(manager):
    """Test for the push button or momentary switch itself"""
    assert manager.get_button().direction == "INPUT"
    assert manager.get_button().pull == "DOWN"
    # Push button name in uppercase
    assert manager.get_name() == "TEST_BUTTON_NAME"
    mock_digitalio.DigitalInOut.assert_called_once_with(93)


def test_button_switch_state(manager):
    """Test for the push button or momentary switch"""
    manager._button.value = False
    assert manager.get_button().value == False
    manager._button.value = True
    assert manager.get_button().value == True


def test_str_representation(manager):
    """Test for the magic method __str__."""
    assert str(manager) == "Push button/switch: TEST_BUTTON_NAME"
