# MultiPicoBox V2

A simple PCB with a Raspberry Pi Pico and some buttons, LEDs for gaming.

This new version have :
* 1 GPIO expander with a MCP23017 chip (**I2C communication with the Pico**,  with configurable jumpers address)
* 4 rotary encoders with a push button
* 4 push buttons, 1 temporary position (0/1)
* 4 push buttons, 1 fix position (0-1)
* 4 toggle switches, 3 fixes positions (1-0-2)
* 6 LEDs for warnings/alerts

This Raspberry Pi Pico use [CircuitPython](https://circuitpython.org) version 9 with external libraries :
- Adafruit module [CircuitPython_MCP230xx](https://github.com/adafruit/Adafruit_CircuitPython_MCP230xx)

- Joystick module [CircuitPython_JoystickXL](https://github.com/fasteddy516/CircuitPython_JoystickXL)

## Printed Circuit Board (PCB) :

The schematic and PCB are made with [KiCad](https://www.kicad.org) version 8 ([kicad](https://github.com/Mick3DIY/MultiPicoBox/tree/main/kicad) folder).

First V2 prototype **8 x 8 cm only**, from [AISLER](https://aisler.net) manufacturer :

![MultiPicoBox_V2_2025-10-15](assets/MultiPicoBoxV2_2025-10-15.png)

Some useful plugins for KiCad :
* AISLER Push for KiCad : https://github.com/aislerhq
* Interactive Html Bom : https://github.com/openscopeproject/InteractiveHtmlBom
* Board2Pdf : https://gitlab.com/dennevi/Board2Pdf
* Solarized Dark Theme : https://github.com/pointhi/kicad-color-schemes

Many thanks to [@Kochise](https://github.com/kochise) for his help and tips for the PCB :beers:

## Code :

* **MultiPicoBoxV2_PCB_test** is for testing the PCB with all external components

*Work In Progress :*

* **MultiPicoBoxV2_JoystickXL_test** is for testing everything like a gamepad :joystick:

Look at the [code](https://github.com/Mick3DIY/MultiPicoBox/tree/main/code) folder for more details.

## Documentation :

Bus I2C :
* https://www.i2c-bus.org
* https://learn.adafruit.com/working-with-i2c-devices?view=all
* https://learn.sparkfun.com/tutorials/i2c/i2c-at-the-hardware-level

Microchip GPIO expander MCP23017 :
* https://www.microchip.com/en-us/product/mcp23017
* https://learn.adafruit.com/using-mcp23008-mcp23017-with-circuitpython?view=all
* https://www.woolseyworkshop.com/2021/03/18/adding-digital-io-to-your-arduino-part-3-the-mcp23017/

Rotary encoders :
* https://learn.adafruit.com/rotary-encoder?view=all
* https://howtomechatronics.com/tutorials/arduino/rotary-encoder-works-use-arduino/
* ALPS EC11 series : https://tech.alpsalpine.com/e/products/category/encorders/sub/01/series/ec11e/

## Bill Of Materials (BOM) :

| Reference  | Qty | Value | Footprint | Description |
| :----- | :-----: | :----- | :----- | :----- |
| C1|1|10uF|Capacitor_THT:C_Disc_D3.8mm_W2.6mm_P2.50mm|Unpolarized capacitor, small symbol |
| C2|1|0.1uF|Capacitor_THT:C_Disc_D3.8mm_W2.6mm_P2.50mm|Unpolarized capacitor, small symbol |
| D1,D2,D3,D4,D5,D6|6|LED||Light emitting diode |
| J1,J2,J3,J4|4|Conn_01x03_Pin|Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical|Generic connector, single row, 01x03 |
| J5,J6,J7,J8|4|Conn_01x05_Pin|Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical|Generic connector, single row, 01x05 |
| J9 -> J22|14|Conn_01x02_Pin|Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical|Generic connector, single row, 01x02 |
| J26,J27|2|Conn_01x20_Socket|Connector_PinSocket_2.54mm:PinSocket_1x20_P2.54mm_Vertical|Generic connector, single row, 01x20 |
| J28 (I2C) |1|Conn_02x03_Top_Bottom|MuliPicoBox_V2:PinHeader_2x03_P2.54mm_Vertical_Re-Order-Pins|Generic connector, double row, 02x03 |
| R1,R2,R3,R4|4|330|Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P2.54mm_Vertical| |
| R5,R6,R7,R8,R9,R10|6|270|Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P2.54mm_Vertical| |
| R11 -> R18|8|10K|Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P2.54mm_Vertical| |
| SW1,SW2,SW3,SW4|4|SW_SPDT_MSM||Switch, single pole double throw, center OFF position |
| SW5,SW6,SW7,SW8|4|RotaryEncoder_Switch||Rotary encoder, dual channel, incremental quadrate outputs, with switch |
| SW9,SW10,SW11,SW12|4|SW_Push||Push button switch, generic, two pins |
| SW13,SW14,SW15,SW16|4|SW_SPST||Single Pole Single Throw (SPST) switch |
| U1|1|MCP23017_I2C|Package_DIP:DIP-28_W7.62mm|16-bit I/O expander, I2C, interrupts, w pull-ups, SPDIP-28 |

Big thanks to the [Adafruit](https://www.adafruit.com) company, the [Python](https://www.python.org/) and [MicroPython](https://micropython.org) communities. :heart: Happy coding & have fun ! :partying_face:
