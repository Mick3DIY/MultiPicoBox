# MultiPicoBox

A simple PCB with Raspberry Pi Pico with some buttons, LEDs for gaming.

This new version have :
* 1 GPIO expander with a MCP23017 chip (I2C communication with the Pico,  with jumper configurable address)
* 4 rotary encoders with a push button
* 4 push buttons, 1 temporary position (0/1)
* 4 push buttons, 1 fix position (0-1)
* 4 toggle switches, 3 fixes positions (1-0-2)
* 6 LEDs for warnings/alerts

The schematic and PCB are made with [KiCad](https://www.kicad.org) version 8.

The Raspberry Pi Pico use [CircuitPython](https://circuitpython.org) version 9 with external libraries :

- custom joystick controller [CircuitPython_JoystickXL](https://github.com/fasteddy516/CircuitPython_JoystickXL)

Work In Progress :)

Documentation :

ALPS EC11 rotary encoders : https://tech.alpsalpine.com/e/products/category/encorders/sub/01/series/ec11e/

Bus I2C : https://www.i2c-bus.org

Microchip GPIO expander MCP23017 :
https://www.microchip.com/en-us/product/mcp23017

Bill Of Materials (BOM) : TODO


Happy coding & have fun ! :partying_face: