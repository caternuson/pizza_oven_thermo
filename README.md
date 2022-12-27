Pizza Oven Temperature Display
==============================

Temperature readout display for pizza oven temperature.


Software
--------

Code is written in [CircuitPython](https://circuitpython.org/). See `code` directory.


Hardware
--------

Uses the following hardware:

  * [Adafruit Feather RP2040](https://www.adafruit.com/product/4884)
  * [Adafruit IS31FL3731 Matrix Driver](https://www.adafruit.com/product/2946)
  * [Adafruit 9x16 LED Matrix](http://www.adafruit.com/product/2948)
  * [Adafruit MCP9600 I2C Thermocouple Amp](https://www.adafruit.com/product/4101)
  * Type K thermocouple
  * LiPo battery


Digit Graphics
--------------

A sprite sheet is used for specifying the digits. It was created using
[GIMP](https://www.gimp.org) and exported as a BMP. The resulting image
is 99x16 pixels, comprised of 11 9x16 tiles. The first 10 of these are
the digits 0 thru 9. The 11th tile is a blank, provided for coding
convenience.

The resulting BMP looks like this
![sprite sheet](assets/digits.bmp)