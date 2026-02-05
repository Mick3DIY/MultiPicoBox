## Code :

* **MultiPicoBoxV2_PCB_test** is for testing the PCB with all external components
	- Requirement : [CircuitPython](https://circuitpython.org) version 9, [Adafruit_CircuitPython_MCP230xx](https://github.com/adafruit/Adafruit_CircuitPython_MCP230xx)
	- Code from `MultiPicoBoxV2_PCB_test.py` :

```python
# MultiPicoBoxV2 PCB test code in CircuitPython (V9)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Raspberry Pi Pico : https://www.raspberrypi.com/products/raspberry-pi-pico/
# Documentation, tutorials : https://projects.raspberrypi.org
# CircuitPython : https://learn.adafruit.com/welcome-to-circuitpython
# Thonny IDE : https://thonny.org
import board
import busio
# https://docs.circuitpython.org/en/latest/shared-bindings/digitalio/index.html
from digitalio import DigitalInOut, Direction, Pull
# https://docs.circuitpython.org/en/latest/shared-bindings/rotaryio/index.html
import rotaryio
# https://docs.circuitpython.org/projects/mcp230xx/en/latest/
from adafruit_mcp230xx.mcp23017 import MCP23017
from time import sleep

# ------------------------------------------------------------------------------------------------------
# Rotary encoders with push button (Pico)
# --------------------------------------------------------------
# Rotary encoder SW5 (J5)
encoderSW5 = rotaryio.IncrementalEncoder(board.GP0, board.GP1)
encoderSW5pb = DigitalInOut(board.GP2)
encoderSW5pos = encoderSW5.position
# Rotary encoder SW6 (J6)
encoderSW6 = rotaryio.IncrementalEncoder(board.GP3, board.GP4)
encoderSW6pb = DigitalInOut(board.GP5)
encoderSW6pos = encoderSW6.position
# Rotary encoder SW7 (J7)
encoderSW7 = rotaryio.IncrementalEncoder(board.GP6, board.GP7)
encoderSW7pb = DigitalInOut(board.GP8)
encoderSW7pos = encoderSW7.position
# Rotary encoder SW8 (J8)
encoderSW8 = rotaryio.IncrementalEncoder(board.GP9, board.GP10)
encoderSW8pb = DigitalInOut(board.GP11)
encoderSW8pos = encoderSW8.position
# Configure rotary encoders push buttons
pbencoders = {encoderSW5pb, encoderSW6pb, encoderSW7pb, encoderSW8pb}
for pbencod in pbencoders:
    pbencod.direction = Direction.INPUT
    pbencod.pull = Pull.UP
# --------------------------------------------------------------
# Push buttons (Pico)
# --------------------------------------------------------------
# Push button SW9 (J15)
pbSW9 = DigitalInOut(board.GP12)
# Push button SW10 (J16)
pbSW10 = DigitalInOut(board.GP13)
# Push button SW11 (J17)
pbSW11 = DigitalInOut(board.GP14)
# Push button SW12 (J18)
pbSW12 = DigitalInOut(board.GP15)
# Configure push buttons
pbuttons = {pbSW9, pbSW10, pbSW11, pbSW12}
for button in pbuttons:
    button.direction = Direction.INPUT
    button.pull = Pull.DOWN
# --------------------------------------------------------------
# Momentary switches (Pico)
# --------------------------------------------------------------
# Momentary switch SW13 (J19)
msSW13 = DigitalInOut(board.GP16)
# Momentary switch SW14 (J20)
msSW14 = DigitalInOut(board.GP17)
# Momentary switch SW15 (J21)
msSW15 = DigitalInOut(board.GP18)
# Momentary switch SW16 (J22)
msSW16 = DigitalInOut(board.GP19)
# Configure momentary switches
mswitches = {msSW13, msSW14, msSW15, msSW16}
for switch in mswitches:
    switch.direction = Direction.INPUT
    switch.pull = Pull.DOWN
# --------------------------------------------------------------
# Pico on-board LED (GPIO25)
# --------------------------------------------------------------
ledOnboard = DigitalInOut(board.GP25)
ledOnboard.direction = Direction.OUTPUT
# --------------------------------------------------------------
# Bus I2C Raspberry Pi Pico <-> MCP23017 (Default address '0x20')
# --------------------------------------------------------------
# Initialize the I2C bus (GPIO20, GPIO21)
i2c = busio.I2C(board.GP21, board.GP20)
# Use the default address
mcp = MCP23017(i2c, address=0x20)
# --------------------------------------------------------------
# MCP23017 module with pin numbers :
# GPA0 -> GPA7 = pin 0 -> 7     /!\ GPA7 (pin 7) & GPB7 (pin 15)
# GPB0 -> GPB7 = pin 8 -> 15    are OUTPUT only
# --------------------------------------------------------------
# Toggle switches (MCP)
# --------------------------------------------------------------
# Toggle switch SW1 (J1)
tsSW1_1 = mcp.get_pin(8)
tsSW1_3 = mcp.get_pin(9)
# Toggle switch SW2 (J2)
tsSW2_1 = mcp.get_pin(10)
tsSW2_3 = mcp.get_pin(11)
# Toggle switch SW3 (J3)
tsSW3_1 = mcp.get_pin(12)
tsSW3_3 = mcp.get_pin(13)
# Toggle switch SW4 (J4)
tsSW4_1 = mcp.get_pin(14)
tsSW4_3 = mcp.get_pin(0)
# Configure toggle switches
tswitches = {tsSW1_1, tsSW1_3, tsSW2_1, tsSW2_3, tsSW3_1, tsSW3_3, tsSW4_1, tsSW4_3}
for switch in tswitches:
    switch.direction = Direction.INPUT
    switch.pull = Pull.UP
# --------------------------------------------------------------
# LEDs (MCP)
# --------------------------------------------------------------
# LED D1 (J9)
D1 = mcp.get_pin(1)
# LED D2 (J10)
D2 = mcp.get_pin(2)
# LED D3 (J11)
D3 = mcp.get_pin(3)
# LED D4 (J12)
D4 = mcp.get_pin(4)
# LED D5 (J13)
D5 = mcp.get_pin(5)
# LED D6 (J14)
D6 = mcp.get_pin(6)
# Configure LEDs to output
dleds = {D1, D2, D3, D4, D5, D6}
for led in dleds:
    led.switch_to_output()
# --------------------------------------------------------------
# GPA7, GPB7 are OUTPUT only (MCP)
# --------------------------------------------------------------
# GPA7, GPB7 (J24)
GPA7 = mcp.get_pin(7)
GPB7 = mcp.get_pin(15)
gpab7 = {GPA7, GPB7}
# Force GPA7, GPB7 to output
for gpa in gpab7:
    gpa.switch_to_output()
#--------------------------------------------------------------------------------------------------
# Encoders manager for reading value
def encoder_manager(encod: IncrementalEncoder, encod_last_pos: int, debug: bool=False):
    """Encoder manager with one physical push button """
    enc_position = encod.position
    position_change = enc_position - encod_last_pos
    if debug == True:
        if position_change > 0:
            print ("Vi_pin_a ++")
        elif position_change < 0:
            print ("Vi_pin_b --")
    return enc_position
# --------------------------------------------------------------
# Blinking LEDs manager, at startup for example
def blink_all_leds(all_leds=[], duration=0.1):
    """Blink LEDs with minimal duration"""
    for led in all_leds:
        # Check if the object is a LED
        if hasattr(led, "direction"):
            led.value = True
            sleep(duration)
            led.value = False

# ------------------------------------------------------------------------------------------------------
# Check all LEDs
blink_all_leds((D1, D2, D3, D4, D5, D6, ledOnboard))
while True:
    # Encoder manager and show value if debug = True
    encoderSW5pos = encoder_manager(encoderSW5, encoderSW5pos, True)
    encoderSW6pos = encoder_manager(encoderSW6, encoderSW6pos, True)
    encoderSW7pos = encoder_manager(encoderSW7, encoderSW7pos, True)
    encoderSW8pos = encoder_manager(encoderSW8, encoderSW8pos, True)
    # Rotary encoder push buttons (Pico), PULL.UP
    for num, button in enumerate(pbencoders):
        if not button.value:
            print("Rotary encoder #", num, "pressed")
    # Push buttons (Pico), PULL.DOWN
    for num, button in enumerate(pbuttons):
        if button.value:
            print("Push button #", num, "pressed")
    # Momentary switches (Pico), PULL.DOWN
    for num, button in enumerate(mswitches):
        if button.value:
            print("Momentary switch #", num, "pressed")
    # Toggle switches (MCP), PULL.UP
    for num, button in enumerate(tswitches):
        if not button.value:
            print("Toggle switch #", num, "pressed")
    sleep(0.1)
```

*Work In Progress :*

* **MultiPicoBoxV2_JoystickXL_test** is for testing everything like a gamepad :joystick:
	- Requirements :  [CircuitPython](https://circuitpython.org) version 9, [Adafruit_CircuitPython_MCP230xx](https://github.com/adafruit/Adafruit_CircuitPython_MCP230xx), [CircuitPython_JoystickXL](https://github.com/fasteddy516/CircuitPython_JoystickXL)
	
* Useful software for testing the Pico in action (Windows, Linux) :space_invader:
	* AntiMicroX : https://github.com/AntiMicroX/antimicrox
