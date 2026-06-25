# MultiPicoBoxV2 unit tests (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Pytest documentation : https://docs.pytest.org
# Unittest documentation : https://docs.python.org/3/library/unittest.html

import pytest
import unittest
from unittest.mock import patch, MagicMock
from MultiPicoBoxV2 import *


class test_MultiPicoBoxV2(unittest.TestCase):

    def test_init_success(self):
        """Test for the main class"""

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
        # Check LEDs
        assert my_box._ledOnboard.direction == "OUTPUT"
        my_box.switch_on_ledOnboard()
        assert my_box._ledOnboard.value == True
