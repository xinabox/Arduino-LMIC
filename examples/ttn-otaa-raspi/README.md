# The Things Network and OKdo Integration using Raspberry Pi and CR02

This example demonstrates how to transmit and receive information to and from the OKdo IoT cloud using LoRaWAN and the The Things Network. The CR02 with an onboard radio module is programmed as an I2C slave device. We will be transferring SW01 environmental data from the Raspberry Pi to the CR02 and receiving data from OKdo to the CR02 enabling us to actuate a relay onboard OC03.

## Requirements

- 1 x [IP01](https://xinabox.cc/products/ip01)/[IP02](https://xinabox.cc/products/ip02) - USB Programming Interface (FT232R)
- 1 x [OC03](https://xinabox.cc/products/oc03) - Relay Output (PCA9554A & TLP241A)
- 1 x [XC10](https://xinabox.cc/products/xc10) - 10-Pack xBus Connectors
- 1 x [SW01](https://xinabox.cc/products/sw01)- Temperature, Humidity, Pressure (BME280)
- 1 x [BR01](https://xinabox.cc/products/br01) - Raspberry Pi Bridge
- 1 x [Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
- [Arduino IDE](https://www.arduino.cc/en/main/software) (optional)
- [OKdo IoT cloud](https://okdo.allthingstalk.com/)
- [The Things Network](https://console.thethingsnetwork.org)


## CR02 Configuration



The easiest method to upload the code to CR02 is by flashing *ttn-otaa-raspi.bin* using [xLoader](https://github.com/xinabox/xLoader). You may select CR03 as the device. Alternatively, use the Arduino IDE and upload *ttn-otta-raspi.ino* to the CR02 selecting Arduino Pro Mini as the board. This method requires [arduino-LMIC](https://github.com/xinabox/arduino-LMIC) library to be installed.
