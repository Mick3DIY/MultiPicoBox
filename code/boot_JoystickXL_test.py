"""MultiPicoBoxV2 JoystickXL test code in CircuitPython (V9) and JoystickXL standard boot.py"""

# https://docs.circuitpython.org/en/stable/shared-bindings/usb_hid/#module-usb_hid
import usb_hid
from joystick_xl.hid import create_joystick

# August 2026, setting a interface name may not work with last CircuitPython V9 or V10
# Set the interface name before enabling devices
usb_hid.set_interface_name("MyPicoBox")
# This will enable the standard CircuitPython USB HID devices otherwise the HID is disabled.
usb_hid.enable(
    (
        usb_hid.Device.KEYBOARD,
        usb_hid.Device.MOUSE,
        usb_hid.Device.CONSUMER_CONTROL,
        create_joystick(axes=0, buttons=28, hats=0),
    )
)
# Don't forget to reboot the Raspberry Pi Pico after updated this file
# and check the boot_out.txt file to see any error during the boot process

# https://docs.circuitpython.org/en/latest/shared-bindings/storage/
import storage

# Import the board classes
from MultiPicoBoxV2 import *

# The main board class
myBox = MultiPicoBoxV2()

# List of all push buttons (SW9 -> SW12)
pbuttons = myBox.get_all_push_buttons()  # list[ButtonManager]

# Press and hold the push button SW9 to expose the CIRCUITPY drive for editing,
# otherwise the USB drive is disabled.
if pbuttons[0].get_button().value:
    # Switch ON all leds briefly
    myBox.switch_on_leds()
else:
    storage.disable_usb_drive()
