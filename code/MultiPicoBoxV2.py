# MultiPicoBoxV2 main class in CircuitPython (V9)
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

# https://docs.circuitpython.org/en/latest/shared-bindings/rotaryio/index.html
import rotaryio

# https://docs.circuitpython.org/projects/mcp230xx/en/latest/
from adafruit_mcp230xx.mcp23017 import MCP23017

from time import sleep


# --------------------------------------------------------------
class EncoderManager:
    """Sub-class for managing encoders"""

    def __init__(self, pin_a, pin_b, pin_sw, name) -> None:
        """Encoder pin_a, pin_b, pin_switch, name"""
        self._encoder = rotaryio.IncrementalEncoder(pin_a, pin_b)
        self._button = DigitalInOut(pin_sw)
        self._button.direction = Direction.INPUT
        self._button.pull = Pull.UP
        self._last_position = self._encoder.position
        self._name = str.upper(name)

    def get_position(self) -> int:
        """Encoder position"""
        return self._encoder.position

    def set_last_position(self, value: int):
        """Set encoder last position"""
        self._last_position = value

    def get_last_position(self) -> int:
        """Encoder last position"""
        return self._last_position

    def get_button(self) -> DigitalInOut:
        """Encoder button switch"""
        return self._button

    def get_name(self) -> str:
        """Encoder name"""
        return self._name

    def __str__(self):
        """Encoder user-friendly detail"""
        return f"Encoder: {self._name}"


# --------------------------------------------------------------
class ButtonManager:
    """Sub-class for managing push buttons or momentary switches"""

    def __init__(self, pin_p, name) -> None:
        """Push or momentary switch pin, name"""
        self._button = DigitalInOut(pin_p)
        self._button.direction = Direction.INPUT
        self._button.pull = Pull.DOWN
        self._name = str.upper(name)

    def get_button(self) -> DigitalInOut:
        """Push button, momentary switch themselves"""
        return self._button

    def get_name(self) -> str:
        """Push button, momentary switch name"""
        return self._name

    def __str__(self):
        """Push button, momentary switch user-friendly detail"""
        return f"Push button/switch: {self._name}"


# --------------------------------------------------------------
class MCPManager:
    """Sub-class for managing the MCP23017 with toggle switches and LEDs"""

    def __init__(self, pin_scl, pin_sda, address=0x20) -> None:
        """MCP23017 serial_clock_pin, serial_data_pin, I2C address"""
        # Initialize the I2C bus
        _i2c = busio.I2C(pin_scl, pin_sda)
        # Use the default address '0x20'
        self._mcp = MCP23017(_i2c, address)

    def get_toggle(self, pin_1, pin_3, name) -> List[DigitalInOut, DigitalInOut, str]:
        """Toggle switch pin_1, pin_3, name"""
        _toggleSwitch = [self._mcp.get_pin(pin_1), self._mcp.get_pin(pin_3)]
        for switch in _toggleSwitch:
            switch.direction = Direction.INPUT
            switch.pull = Pull.UP
        _toggleSwitch.append(str.upper(name))
        return _toggleSwitch

    def get_led(self, pin_2) -> DigitalInOut:
        """LEDs themselves"""
        _led = self._mcp.get_pin(pin_2)
        _led.switch_to_output()
        return _led


# -----------------------------------------------------------------------------
class MultiPicoBoxV2:
    """Main class for the MultiPicoBoxV2 PCB"""

    def __init__(self) -> None:
        """Create all objects in the board"""

        # Showing messages for debug
        self._debug_ = False
        # --------------------------------------------------------------
        # Rotary encoders with push button (Pico)
        # --------------------------------------------------------------
        # Rotary encoder SW5 (J5)
        self._sw5 = EncoderManager(board.GP0, board.GP1, board.GP2, "SW5")
        # Rotary encoder SW6 (J6)
        self._sw6 = EncoderManager(board.GP3, board.GP4, board.GP5, "SW6")
        # Rotary encoder SW7 (J7)
        self._sw7 = EncoderManager(board.GP6, board.GP7, board.GP8, "SW7")
        # Rotary encoder SW8 (J8)
        self._sw8 = EncoderManager(board.GP9, board.GP10, board.GP11, "SW8")
        # Constants for dictionnary, for actions
        self.rotary_encoders = {}
        for encoder in self._sw5, self._sw6, self._sw7, self._sw8:
            # self.C_SWX = "SWX" -> set constants with "SWX" for each encoder
            _const = f"C_{encoder.get_name()}"
            setattr(self, _const, encoder.get_name())
            # self.C_SWX = self.swx -> set index for actions for each encoder
            self.rotary_encoders[encoder.get_name()] = encoder
        # --------------------------------------------------------------
        # Push buttons (Pico)
        # --------------------------------------------------------------
        # Push button SW9 (J15)
        self._sw9 = ButtonManager(board.GP12, "SW9")
        # Push button SW10 (J16)
        self._sw10 = ButtonManager(board.GP13, "SW10")
        # Push button SW11 (J17)
        self._sw11 = ButtonManager(board.GP14, "SW11")
        # Push button SW12 (J18)
        self._sw12 = ButtonManager(board.GP15, "SW12")
        # Constants for dictionnary, for actions
        self.push_buttons = {}
        for pbutton in self._sw9, self._sw10, self._sw11, self._sw12:
            _const = f"C_{pbutton.get_name()}"
            setattr(self, _const, pbutton.get_name())
            self.push_buttons[pbutton.get_name()] = pbutton
        # --------------------------------------------------------------
        # Momentary switches (Pico)
        # --------------------------------------------------------------
        # Momentary switch SW13 (J19)
        self._sw13 = ButtonManager(board.GP16, "SW13")
        # Momentary switch SW14 (J20)
        self._sw14 = ButtonManager(board.GP17, "SW14")
        # Momentary switch SW15 (J21)
        self._sw15 = ButtonManager(board.GP18, "SW15")
        # Momentary switch SW16 (J22)
        self._sw16 = ButtonManager(board.GP19, "SW16")
        # Constants for dictionnary, for actions
        self.moment_switches = {}
        for mswitch in self._sw13, self._sw14, self._sw15, self._sw16:
            _const = f"C_{mswitch.get_name()}"
            setattr(self, _const, mswitch.get_name())
            self.moment_switches[mswitch.get_name()] = mswitch
        # --------------------------------------------------------------
        # Pico on-board LED (GPIO25)
        # --------------------------------------------------------------
        self._ledOnboard = DigitalInOut(board.GP25)
        self._ledOnboard.direction = Direction.OUTPUT
        # --------------------------------------------------------------
        # Bus I2C Raspberry Pi Pico <-> MCP23017 (Default address '0x20')
        # --------------------------------------------------------------
        self._mcp = MCPManager(board.GP21, board.GP20)
        # Toggle switch SW1 (J1)
        self._tssw1 = self._mcp.get_toggle(8, 9, "TSSW1")
        # Toggle switch SW2 (J2)
        self._tssw2 = self._mcp.get_toggle(10, 11, "TSSW2")
        # Toggle switch SW3 (J3)
        self._tssw3 = self._mcp.get_toggle(12, 13, "TSSW3")
        # Toggle switch SW4 (J4)
        self._tssw4 = self._mcp.get_toggle(14, 0, "TSSW4")
        # Constants for dictionnary, for actions
        self.toggle_switches = {}
        for tswitch in self._tssw1, self._tssw2, self._tssw3, self._tssw4:
            _pin1, _pin3, _name = f"{tswitch[2]}_1", f"{tswitch[2]}_3", tswitch[2]
            # Set constants with "TSSWX" for pin 1
            setattr(self, f"C_{_pin1}", _pin1)
            # Set constants with "TSSWX" for pin 3
            setattr(self, f"C_{_pin3}", _pin3)
            self.toggle_switches[_pin1] = tswitch[0]
            self.toggle_switches[_pin3] = tswitch[1]
        # --------------------------------------------------------------
        # LEDs (MCP)
        # --------------------------------------------------------------
        # LED D1 (J9)
        self._d1 = self._mcp.get_led(1)
        # LED D2 (J10)
        self._d2 = self._mcp.get_led(2)
        # LED D3 (J11)
        self._d3 = self._mcp.get_led(3)
        # LED D4 (J12)
        self._d4 = self._mcp.get_led(4)
        # LED D5 (J13)
        self._d5 = self._mcp.get_led(5)
        # LED D6 (J14)
        self._d6 = self._mcp.get_led(6)
        # --------------------------------------------------------------
        # Free connectors : GPA7, GPB7 are OUTPUT only like LEDs (MCP)
        # --------------------------------------------------------------
        # GPA7, GPB7 (J24)
        self._gpa7 = self._mcp.get_led(7)
        self._gpb7 = self._mcp.get_led(15)
        # --------------------------------------------------------------
        # Free connector : GP22 as a input (Pico)
        # --------------------------------------------------------------
        # GP22 (J25)
        self._sw17 = ButtonManager(board.GP22, "SW17")

    # --------------------------------------------------------------
    # Static methods for internal actions
    # --------------------------------------------------------------
    @staticmethod
    def _action_encoders(self, name: str) -> None:
        """Actions for rotary encoder push buttons"""
        if name == self.C_SW5:
            self._action_debug(self, f"Rotary encoder pressed n°1 : {name}")
        elif name == self.C_SW6:
            self._action_debug(self, f"Rotary encoder pressed n°2 : {name}")
        elif name == self.C_SW7:
            self._action_debug(self, f"Rotary encoder pressed n°3 : {name}")
        elif name == self.C_SW8:
            self._action_debug(self, f"Rotary encoder pressed n°4 : {name}")
        else:
            raise ValueError("_action_encoders wrong value")

    @staticmethod
    def _action_pushbuttons(self, name: str) -> None:
        """Actions for push buttons"""
        if name == self.C_SW9:
            self._action_debug(self, f"Push button pressed n°1 : {name}")
        elif name == self.C_SW10:
            self._action_debug(self, f"Push button pressed n°2 : {name}")
        elif name == self.C_SW11:
            self._action_debug(self, f"Push button pressed n°3 : {name}")
        elif name == self.C_SW12:
            self._action_debug(self, f"Push button pressed n°4 : {name}")
        else:
            raise ValueError("_action_pushbuttons wrong value")

    @staticmethod
    def _action_momswitches(self, name: str) -> None:
        """Actions for momentary switches"""
        if name == self.C_SW13:
            self._action_debug(self, f"Momentary switch pressed n°1 : {name}")
        elif name == self.C_SW14:
            self._action_debug(self, f"Momentary switch pressed n°2 : {name}")
        elif name == self.C_SW15:
            self._action_debug(self, f"Momentary switch pressed n°3 : {name}")
        elif name == self.C_SW16:
            self._action_debug(self, f"Momentary switch pressed n°4 : {name}")
        else:
            raise ValueError("_action_momswitches wrong value")

    @staticmethod
    def _action_togswitches(self, name: str) -> None:
        """Actions for toggle switches"""
        if name == self.C_TSSW1_1:
            self._action_debug(self, f"Toggle switch pressed n°1 : {name}")
        elif name == self.C_TSSW1_3:
            self._action_debug(self, f"Toggle switch pressed n°2 : {name}")
        elif name == self.C_TSSW2_1:
            self._action_debug(self, f"Toggle switch pressed n°3 : {name}")
        elif name == self.C_TSSW2_3:
            self._action_debug(self, f"Toggle switch pressed n°4 : {name}")
        elif name == self.C_TSSW3_1:
            self._action_debug(self, f"Toggle switch pressed n°5 : {name}")
        elif name == self.C_TSSW3_3:
            self._action_debug(self, f"Toggle switch pressed n°6 : {name}")
        elif name == self.C_TSSW4_1:
            self._action_debug(self, f"Toggle switch pressed n°7 : {name}")
        elif name == self.C_TSSW4_3:
            self._action_debug(self, f"Toggle switch pressed n°8 : {name}")
        else:
            raise ValueError("_action_togswitches wrong value")

    @staticmethod
    def _action_debug(self, message: str) -> None:
        """Show action messages from all inputs"""
        if self._debug_:
            print(message)

    # --------------------------------------------------------------
    # Public methods for external updates
    # --------------------------------------------------------------
    def update(self) -> None:
        """Physical inputs from Pico and MCP"""

        # Rotary encoders push button (Pico), PULL.UP
        for name, button in self.rotary_encoders.items():
            if not button.get_button().value:
                self._action_encoders(self, name)
        # Push buttons (Pico), PULL.DOWN
        for name, button in self.push_buttons.items():
            if button.get_button().value:
                self._action_pushbuttons(self, name)
        # Momentary switches (Pico), PULL.DOWN
        for name, button in self.moment_switches.items():
            if button.get_button().value:
                self._action_momswitches(self, name)
        # Toggle switches (MCP), PULL.UP
        for name, button in self.toggle_switches.items():
            if not button.value:
                self._action_togswitches(self, name)

    def update_vi(self, encoders_vi) -> None:
        """Encoder virtual inputs for JoystickXL"""

        # Rotary encoders update (Pico) with two virtual inputs :
        # <EncoderManager>, <Button>, <Button>
        for encoder, vi_pin_a, vi_pin_b in encoders_vi:
            _current_pos = encoder.get_position()
            _pos_change = _current_pos - encoder.get_last_position()
            if _pos_change != 0:
                vi_pin_a.source_value = _pos_change > 0  # True or False ?
                vi_pin_b.source_value = _pos_change < 0
                encoder.set_last_position(_current_pos)
            else:
                vi_pin_a.source_value = vi_pin_b.source_value = False

    def show_encoder_pins(self, encoder: EncoderManager, encoder_last_pos: int, encoder_name: str) -> int:
        """Show encoders pins values WITHOUT JoystickXL"""
        _enc_position = encoder.get_position()
        _position_change = _enc_position - encoder_last_pos
        if _position_change > 0:
            print(f"Rotary encoder ({_enc_position}) pin_a ++ : {encoder_name}")
        elif _position_change < 0:
            print(f"Rotary encoder ({_enc_position}) pin_b -- : {encoder_name}")
        return _enc_position

    def get_all_rot_encoders(self) -> List[EncoderManager]:
        """Return all rotary encoders"""
        return (self._sw5, self._sw6, self._sw7, self._sw8)

    def get_all_push_buttons(self) -> List[ButtonManager]:
        """Return all push buttons"""
        return (self._sw9, self._sw10, self._sw11, self._sw12)

    def get_all_mom_switches(self) -> List[ButtonManager]:
        """Return all momentary switches"""
        return (self._sw13, self._sw14, self._sw15, self._sw16)

    def get_all_tog_switches(self) -> List[[DigitalInOut, DigitalInOut]]:
        """Return all toggle switches"""
        return (self._tssw1, self._tssw2, self._tssw3, self._tssw4)

    @staticmethod
    def _get_all_leds(self) -> List[DigitalInOut]:
        """Return all LEDs in the board"""
        return (self._d1, self._d2, self._d3, self._d4, self._d5, self._d6, self._ledOnboard)

    def blink_leds(self, duration=0.1) -> None:
        """Blink all LEDs with minimal duration"""
        for led in self._get_all_leds(self):
            led.value = True
            sleep(duration)
            led.value = False

    def switch_on_ledOnboard(self):
        """Switch on the onboard LED"""
        self._ledOnboard.value = True

    def switch_off_leds(self) -> None:
        """Switch off all LEDs onboard"""
        for led in self._get_all_leds(self):
            led.value = False

    def show_debug(self) -> None:
        """Show debug messages"""
        self._debug_ = True
