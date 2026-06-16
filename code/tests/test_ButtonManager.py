# MultiPicoBoxV2 unit tests (pytest)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Pytest documentation : https://docs.pytest.org
# Unittest documentation : https://docs.python.org/3/library/unittest.html

import pytest
import unittest
from unittest.mock import patch, MagicMock
from MultiPicoBoxV2 import ButtonManager


class test_ButtonManager(unittest.TestCase):

    def test_init_success(self):
        """Test for the push buttons or momentary switches sub-class"""

        # Fake button with fake pin
        my_button = ButtonManager(93, "test_button_name")
        assert my_button.get_button().direction == "INPUT"
        assert my_button.get_button().pull == "DOWN"
        # Push button name in uppercase
        assert (my_button.get_name() == "TEST_BUTTON_NAME"), "Push button name is not correct !"

    def test_str_method(self):
        """Test button __str__ method"""

        # Fake button with fake pin
        my_button = ButtonManager(93, "test_button_name")
        assert str(my_button) == "Push button/switch: TEST_BUTTON_NAME"
