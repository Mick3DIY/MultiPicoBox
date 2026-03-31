# MultiPicoBoxV2 JoystickXL test code in CircuitPython (V9)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Raspberry Pi Pico : https://www.raspberrypi.com/products/raspberry-pi-pico/
# Documentation, tutorials : https://projects.raspberrypi.org
# CircuitPython : https://learn.adafruit.com/welcome-to-circuitpython
# Thonny IDE : https://thonny.org

# https://circuitpython-joystickxl.readthedocs.io/en/latest/api.html#module-joystick_xl.inputs
from joystick_xl.inputs import Button

# https://circuitpython-joystickxl.readthedocs.io/en/latest/api.html#module-joystick_xl.joystick
from joystick_xl.joystick import Joystick

# Import the board classes
from MultiPicoBoxV2 import *

# -----------------------------------------------------------------------------
# The main board class
myBox = MultiPicoBoxV2()
# Show inputs status
myBox.show_debug()
# The main JoystickXL class
js = Joystick()
# Add rotary encoders SW5 -> SW8 to JoystickXL
for encoder in myBox.get_all_rot_encoders():
    js.add_input(
        Button(encoder.get_button()),  # Encoder physical push button
        Button(None, active_low=False),  # Encoder virtual input buttons
        Button(None, active_low=False),
    )
# Add push buttons pbSW9 -> pbSW12
for switch in myBox.get_all_push_buttons():
    js.add_input(Button(switch.get_button(), active_low=False))
# Add momentary switches msSW13 -> msSW16
for switch in myBox.get_all_mom_switches():
    js.add_input(Button(switch.get_button(), active_low=False))
# Add toggle switches tsSW1_1 -> tsSW4_3
for toogle in myBox.get_all_tog_switches():
    for switch in toogle:
        if not isinstance(switch, str):
            js.add_input(Button(switch, active_low=True))
# Rotary encoders update with JoystickXL
jsVIs = [
    (myBox.get_all_rot_encoders()[0], js.button[1], js.button[2]),
    (myBox.get_all_rot_encoders()[1], js.button[4], js.button[5]),
    (myBox.get_all_rot_encoders()[2], js.button[7], js.button[8]),
    (myBox.get_all_rot_encoders()[3], js.button[10], js.button[11]),
]
# Check all LEDs at startup
myBox.blink_leds()
# Pico status
myBox.switch_on_ledOnboard()
# Main loop
try:
    while True:
        # Update physical inputs (Pico and MCP)
        myBox.update()
        # Update virtual inputs for JoystickXL
        myBox.update_vi(jsVIs)
        # Update JoystickXL itself
        js.update()
except Exception as err:
    print(f"Error: {err}")
finally:
    myBox.switch_off_leds()

