# MultiPicoBoxV2 JoystickXL test code in CircuitPython (V9)
# GitHub project : https://github.com/Mick3DIY/MultiPicoBox
# Raspberry Pi Pico : https://www.raspberrypi.com/products/raspberry-pi-pico/
# Documentation, tutorials : https://projects.raspberrypi.org
# CircuitPython : https://learn.adafruit.com/welcome-to-circuitpython
# Thonny IDE : https://thonny.org
import board
# https://docs.circuitpython.org/en/latest/shared-bindings/busio/
import busio
# https://docs.circuitpython.org/en/latest/shared-bindings/digitalio/index.html
from digitalio import DigitalInOut, Direction, Pull
# https://docs.circuitpython.org/en/latest/shared-bindings/rotaryio/index.html
import rotaryio
# https://docs.circuitpython.org/projects/mcp230xx/en/latest/
from adafruit_mcp230xx.mcp23017 import MCP23017
# https://circuitpython-joystickxl.readthedocs.io/en/latest/api.html#module-joystick_xl.inputs
from joystick_xl.inputs import Button
# https://circuitpython-joystickxl.readthedocs.io/en/latest/api.html#module-joystick_xl.joystick
from joystick_xl.joystick import Joystick
from time import sleep

# Global flag for debugging
DEBUG = True
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
i2c = busio.I2C(board.GP21, board.GP20, frequency=50000)
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
def encoder_manager(encod: IncrementalEncoder, vi_pin_a: VirtualInput, vi_pin_b: VirtualInput, encod_last_pos: int, debug: bool=False):
    """Encoder manager with one physical push button and two virtual inputs"""
    enc_position = encod.position
    position_change = enc_position - encod_last_pos
    if position_change > 0:
        vi_pin_a.source_value = True
        if debug == True:
            print ("Vi_pin_a ++")
    elif position_change < 0:
        vi_pin_b.source_value = True
        if debug == True:
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
# JoystickXL configuration (with boot.py)
js = Joystick()
js.add_input(
    # Rotary encoder SW5
    Button(encoderSW5pb), # Encoder physical push button
    Button(None, active_low=False), # Encoder virtual input buttons
    Button(None, active_low=False),
    # Rotary encoder SW6
    Button(encoderSW6pb),
    Button(None, active_low=False),
    Button(None, active_low=False),
    # Rotary encoder SW7
    Button(encoderSW7pb),
    Button(None, active_low=False),
    Button(None, active_low=False),
    # Rotary encoder SW8
    Button(encoderSW8pb),
    Button(None, active_low=False),
    Button(None, active_low=False),
    # Push buttons pbSW9 -> pbSW12
    Button(pbSW9, active_low=False), Button(pbSW10, active_low=False), Button(pbSW11, active_low=False), Button(pbSW12, active_low=False),
    # Momentary switches msSW13 -> msSW16
    Button(msSW13, active_low=False), Button(msSW14, active_low=False), Button(msSW15, active_low=False), Button(msSW16, active_low=False),
    # Toggle switches tsSW1_1 -> tsSW4_3
    Button(tsSW1_1, active_low=True), Button(tsSW1_3, active_low=True), Button(tsSW2_1, active_low=True), Button(tsSW2_3, active_low=True),
    Button(tsSW3_1, active_low=True), Button(tsSW3_3, active_low=True), Button(tsSW4_1, active_low=True), Button(tsSW4_3, active_low=True),
)
# ------------------------------------------------------------------------------------------------------
# Check all LEDs
blink_all_leds((D1, D2, D3, D4, D5, D6, ledOnboard, 0.3))
# Pico status
ledOnboard.value = True
try:
    while True:
        # Virtual inputs release for new impulses (Rotary encoders)
        js.button[1].source_value = False
        js.button[2].source_value = False
        js.button[4].source_value = False
        js.button[5].source_value = False
        js.button[7].source_value = False
        js.button[8].source_value = False
        js.button[10].source_value = False
        js.button[11].source_value = False

        if DEBUG == True:
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
                    
        # LEDs (D1 -> D3 with SW9 -> SW11)
        if js.button[12].is_pressed:
            D1.value = True
        else:
            D1.value = False
        if js.button[13].is_pressed:
            D2.value = True
        else:
            D2.value = False
        if js.button[14].is_pressed:
            D3.value = True
        else:
            D3.value = False
        # LEDs (D4 -> D6 with SW13 -> SW15)
        if js.button[16].is_pressed:
            D4.value = True
        else:
            D4.value = False
        if js.button[17].is_pressed:
            D5.value = True
        else:
            D5.value = False
        if js.button[18].is_pressed:
            D6.value = True
        else:
            D6.value = False
                
        # Encoder manager, show value if debug = True
        encoderSW5pos = encoder_manager(encoderSW5, js.button[1], js.button[2], encoderSW5pos, DEBUG)
        encoderSW6pos = encoder_manager(encoderSW6, js.button[4], js.button[5], encoderSW6pos, DEBUG)
        encoderSW7pos = encoder_manager(encoderSW7, js.button[7], js.button[8], encoderSW7pos, DEBUG)
        encoderSW8pos = encoder_manager(encoderSW8, js.button[10], js.button[11], encoderSW8pos, DEBUG)
        
        js.update()
        sleep(0.05) # Important !
except (Exception, KeyboardInterrupt) as err:
    print(err)
finally:
    ledOnboard.value = False

