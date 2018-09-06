# Arduino-LMIC
```C
This code is based on the pull request in the original code, where no DIO-pins are needed!

// Pin mapping
const lmic_pinmap lmic_pins = {
  .nss = 10,
  .rxtx = LMIC_UNUSED_PIN,
  .rst = LMIC_UNUSED_PIN,
  .dio = {LMIC_UNUSED_PIN, LMIC_UNUSED_PIN, LMIC_UNUSED_PIN}, //2,4,na
};
```
This repository contains the IBM LMIC (LoraMAC-in-C) library, slightly
modified to run in the Arduino environment, allowing using the SX1272,
SX1276 tranceivers and compatible modules (such as some HopeRF RFM9x
modules).

This library mostly exposes the functions defined by LMIC, it makes no
attempt to wrap them in a higher level API that is more in the Arduino
style. To find out how to use the library itself, see the examples, or
see the PDF file in the doc subdirectory.

This library requires Arduino IDE version 1.6.6 or above, since it
requires C99 mode to be enabled by default.

## Requirements
- Installation of the Arduino IDE from the [Arduino Website](https://www.arduino.cc/en/main/software)
- ☒CHIP CR01/CR02/CR03

## Installation Guide
To install the libraries please followed the guide provided on the [Arduino Website](https://www.arduino.cc/en/Guide/Libraries) under "**Importing a .zip Library**".

## License
Most source files in this repository are made available under the
Eclipse Public License v1.0. The examples which use a more liberal
license. Some of the AES code is available under the LGPL. Refer to each
individual source file for more details.
