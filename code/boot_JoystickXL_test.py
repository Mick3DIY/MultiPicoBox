""" MultiPicoBoxV2 JoystickXL test code in CircuitPython (V9) and JoystickXL standard boot.py"""

import usb_hid
from joystick_xl.hid import create_joystick

# This will enable the standard CircuitPython USB HID devices along with a USB HID joystick.
usb_hid.enable(
    (
#        usb_hid.Device.KEYBOARD,
#        usb_hid.Device.MOUSE,
#        usb_hid.Device.CONSUMER_CONTROL,
        create_joystick(axes=0, buttons=28, hats=0),
    )
)

# Import the board classes
from MultiPicoBoxV2 import *

# https://docs.circuitpython.org/en/latest/shared-bindings/storage/
import storage

# The main board class
myBox = MultiPicoBoxV2()

# List of all push buttons (SW9 -> SW12)
pbuttons = myBox.get_all_push_buttons() # List[ButtonManager]

# Press and hold the push button SW9 to expose the CIRCUITPY drive for editing,
# otherwise the USB drive is disabled.
if pbuttons[0].get_button().value:
    # Switch ON all leds briefly
    myBox.switch_on_leds()
else:
    storage.disable_usb_drive()