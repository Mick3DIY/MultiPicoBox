# MultiPicoBoxV2 unit tests (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox

import pytest
from unittest.mock import MagicMock
from MultiPicoBoxV2 import *


def test_EncoderManager():
    """Tests for the encoders sub-class"""

    # Fake encoder
    f_encoder = MagicMock()
    my_encoder = EncoderManager("PIN_A", "PIN_B", "PIN_SW", "test_encoder_name")
    # Encoder default position
    assert (my_encoder.get_position() == 0), "Encoder position is not zero by default !"
    # Encoder positions
    my_encoder.set_last_position(5)
    assert my_encoder.get_last_position() == 5, "Encoder last position is not correct !"
    # Fake encoder push button
    f_button = MagicMock()
    f_button = my_encoder.get_button()
    f_button.value = False
    # Encoder push button
    assert (my_encoder.get_button().value == False), "Encoder push button is not False by default !"
    # Encoder name in uppercase
    assert my_encoder.get_name() == "TEST_ENCODER_NAME", "Encoder name is not correct !"
    # Encoder __str__ method
    assert str(my_encoder) == "Encoder: TEST_ENCODER_NAME"
