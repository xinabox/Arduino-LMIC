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
- [The Things Network](https://thethingsnetwork.org)


## CR02 Configuration

Assemble IP01 and CR02 as per the image below and insert it into your computer.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/ip01cr02.jpg" alt="alt text" width="15%" height="auto" align="center">

The easiest method to upload the code to CR02 is by flashing *ttn-otaa-raspi.hex* using [xLoader](https://github.com/xinabox/xLoader). You may select CR03 as the device. Alternatively, use the Arduino IDE and upload *ttn-otta-raspi.ino* to the CR02 selecting Arduino Pro Mini as the board. This method requires [arduino-LMIC](https://github.com/xinabox/arduino-LMIC) library to be installed.

That completes the CR02 configuration.

## The Things Network Setup

1. Create an account on [The Things Network](https://thethingsnetwork.org)
2. Navigate to [The Things Console](https://console.thethingsnetwork.org)
3. Select application and add a new application. Give the application a name and an optional description.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/ttn1.jpg" alt="alt text" width="15%" height="auto" align="center">

4. Below the devices heading register a new device. Provide an ID for the device and generate the Device EUI.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/ttn2.jpg" alt="alt text" width="15%" height="auto" align="center">

5. The keys will be generated similar to the image below.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/ttn3.jpg" alt="alt text" width="15%" height="auto" align="center">

6. Navigate back to devices and open up the integrations tab. Add the AllThingsTalk Maker intergation.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/ttn4.jpg" alt="alt text" width="15%" height="auto" align="center">

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/ttn5.jpg" alt="alt text" width="15%" height="auto" align="center">

7. Provide a unique ID and select the default access key and complete the integration. You have now created the integration between OKdo and The Things Network.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/ttn6.jpg" alt="alt text" width="15%" height="auto" align="center">

8. 
