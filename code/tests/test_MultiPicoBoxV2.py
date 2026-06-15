# MultiPicoBoxV2 unit tests (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Pytest documentation : https://docs.pytest.org

import pytest
from unittest.mock import MagicMock
from MultiPicoBoxV2 import *


def test_EncoderManager():
    """Tests for the encoders sub-class"""

    # Fake encoder with fake pins
    my_encoder = EncoderManager(90, 91, 92, "test_encoder_name")
    # Encoder
    assert my_encoder.get_button().direction == "INPUT"
    assert my_encoder.get_button().pull == "UP"
    # Encoder default positions
    assert my_encoder.get_position() == 0, "Encoder position is not zero by default !"
    assert my_encoder.get_last_position() == 0
    # Encoder positions
    my_encoder.set_last_position(5)
    assert my_encoder.get_last_position() == 5, "Encoder last position is not correct !"
    # Fake encoder push button
    f_button = MagicMock()
    f_button = my_encoder.get_button()
    f_button.value = False
    # Encoder push button
    assert my_encoder.get_button().value == False, "Encoder push button is not False by default !"
    # Encoder name in uppercase
    assert my_encoder.get_name() == "TEST_ENCODER_NAME", "Encoder name is not correct !"
    # Encoder __str__ method
    assert str(my_encoder) == "Encoder: TEST_ENCODER_NAME"


def test_ButtonManager():
    """Tests for the push buttons or momentary switches sub-class"""

    # Fake button with fake pin
    my_button = ButtonManager(93, "test_button_name")
    # Push button
    assert my_button.get_button().direction == "INPUT"
    assert my_button.get_button().pull == "DOWN"
    assert my_button.get_button().value == False, "Push button is not False by default !"
    # Push button name in uppercase
    assert my_button.get_name() == "TEST_BUTTON_NAME", "Push button name is not correct !"
    # Push button __str__ method
    assert str(my_button) == "Push button/switch: TEST_BUTTON_NAME"


def test_MultiPicoBoxV2():
    """Tests for the main class"""

    # Fake MultiPicoBox
    my_box = MultiPicoBoxV2()
    # Check rotary encoders
    assert len(my_box.rotary_encoders) == len(my_box.get_all_rot_encoders())
    assert all(isinstance(item, EncoderManager) for item in my_box.get_all_rot_encoders())
    # Check push buttons
    assert len(my_box.push_buttons) == len(my_box.get_all_push_buttons())
    assert all(isinstance(item, ButtonManager) for item in my_box.get_all_push_buttons())
    # Check momentary switches
    assert len(my_box.moment_switches) == len(my_box.get_all_mom_switches())
    assert all(isinstance(item, ButtonManager) for item in my_box.get_all_mom_switches())
    # Check toggle switches (8 switches -> 4 toggles switches)
    assert len(my_box.toggle_switches) / 2 == len(my_box.get_all_tog_switches())
    for toggles in my_box.get_all_tog_switches():
        # Objects <adafruit_mcp230xx.digital_inout.DigitalInOut>
        for i in range(2):
            assert toggles[i].direction == "INPUT"
            assert toggles[i].pull == "UP"
            assert toggles[i].value == True
        assert isinstance(toggles[2], str)
