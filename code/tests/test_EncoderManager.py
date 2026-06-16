# MultiPicoBoxV2 unit tests (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Pytest documentation : https://docs.pytest.org
# Unittest documentation : https://docs.python.org/3/library/unittest.html

import pytest
import unittest
from unittest.mock import patch, MagicMock
from MultiPicoBoxV2 import EncoderManager


class test_ButtonManager(unittest.TestCase):

    def test_init_success(self):
        """Test for the encoders sub-class"""

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