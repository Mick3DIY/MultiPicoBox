""" MultiPicoBoxV2 PCB test code in CircuitPython (V9) and standard boot.py"""

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