# MultiPicoBoxV2 PCB test code in CircuitPython (V9)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Raspberry Pi Pico : https://www.raspberrypi.com/products/raspberry-pi-pico/
# Documentation, tutorials : https://projects.raspberrypi.org
# CircuitPython : https://learn.adafruit.com/welcome-to-circuitpython
# Thonny IDE : https://thonny.org

# Import the board classes
from MultiPicoBoxV2 import *

# -----------------------------------------------------------------------------
# Rotary encoders initial position SW5 -> SW8
encoderSW5pos = encoderSW6pos = encoderSW7pos = encoderSW8pos = 0
# The main board class
myBox = MultiPicoBoxV2()
# Show inputs status
myBox.show_debug()
# Check all LEDs at startup
myBox.blink_leds()
# Pico status
myBox.switch_on_ledOnboard()
# Main loop
try:
    encoders = myBox.get_all_rot_encoders()
    while True:
        # Show encoders pins values
        encoderSW5pos = myBox.show_encoder_pins(encoders[0], encoderSW5pos, "SW5")
        encoderSW6pos = myBox.show_encoder_pins(encoders[1], encoderSW6pos, "SW6")
        encoderSW7pos = myBox.show_encoder_pins(encoders[2], encoderSW7pos, "SW7")
        encoderSW8pos = myBox.show_encoder_pins(encoders[3], encoderSW8pos, "SW8")
        # Update physical inputs (Pico and MCP)
        myBox.update()
except Exception as err:
    print(f"Error: {err}")
finally:
    myBox.switch_off_leds()

