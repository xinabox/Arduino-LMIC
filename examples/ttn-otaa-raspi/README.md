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

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/ttn1.png" alt="alt text" width="70%" height="auto" align="center">

4. Below the devices heading register a new device. Provide an ID for the device and generate the Device EUI.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/ttn2.png" alt="alt text" width="70%" height="auto" align="center">

5. The keys will be generated similar to the image below. You will require these keys for OKdo.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/ttn3.png" alt="alt text" width="70%" height="auto" align="center">

6. Navigate back to devices and open up the integrations tab. Add the AllThingsTalk Maker intergation.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/ttn4.png" alt="alt text" width="70%" height="auto" align="center">

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/ttn5.png" alt="alt text" width="70%" height="auto" align="center">

7. Provide a unique ID and select the default access key and complete the integration. You have now created the integration between OKdo and The Things Network.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/ttn6.png" alt="alt text" width="70%" height="auto" align="center">

## OKdo Setup

1. Create an account on [OKdo All Things Talk](https://okdo.allthingstalk.com/)
2. Add a new ground

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo1.png" alt="alt text" width="70%" height="auto" align="center">

3. In the Devices menu, add a new device and select your own LoRa device

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo2.png" alt="alt text" width="70%" height="auto" align="center">

4. Add The Things Network integration

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo3.png" alt="alt text" width="70%" height="auto" align="center">

5. Provide a name for your device and paste your keys provided by The Things Network into the respective fields. ABP keys will only be generated when you connect to The Things Network. This can be reenetred afterwards by going to *settings > connectivity*

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo4.png" alt="alt text" width="70%" height="auto" align="center">

6. Add new assets to your device. For sensor data you’d want to create a sensor asset with a number data type. For actuating the OC03, you’d create an actuator asset with a boolean data type. Assets will need to be created with the names t, h, p and r.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo5.png" alt="alt text" width="70%" height="auto" align="center">  <img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo6.png" alt="alt text" width="70%" height="auto" align="center">

6. You should have the following assets on your screen

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo7.png" alt="alt text" width="70%" height="auto" align="center">

7. In the settings menu in the top right corner, navigate to payload formats 

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo8.png" alt="alt text" width="70%" height="auto" align="center">

9. Enable use ABCL to convert custom binary data. ABCL will only be used for actuation. Data is received as CBOR

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo9.png" alt="alt text" width="70%" height="auto" align="center">

10. Paste the actuate.json contents in the field.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo10.png" alt="alt text" width="70%" height="auto" align="center">

11. Create a new pinboard to visualize your data and to easily control OC03. New Pinboard > Pinboard Name > Arrange Pinboard > New pin > Select the toggle pin and assign it to your relay (r) asset. You can assign the data log pin for temperature, humidity and pressure.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo11.png" alt="alt text" width="70%" height="auto" align="center">

That completes the OKdo setup


## Raspberry Pi Configuration

Hardware setup for Raspberry Pi is shown below

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/raspisetup.jpg" alt="alt text" width="30%" height="auto" align="center">

Assuming Python 3 and pip3 is installed on your Raspberry Pi, the following python packages are required:

```python
sudo pip3 install smbus2
sudo pip3 install cbor
sudo pip3 install RPi.bme280
```

download the cr02_raspi.py and methods_.py files and run cr02_raspi.py

```python
sudo python3 cr02_raspi.py
```

## Result

The green LED on CR02 will light up when you have succesfully connected to The Things Network. The LED will remain RED if a connection is being attempted.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/raspijoining.jpg" alt="alt text" width="30%" height="auto" align="center"> <img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/raspijoined.jpg" alt="alt text" width="30%" height="auto" align="center">

In your Things Network Console you’ll see data being received from CR02 in CBOR format. Data is only sent every minute to the Things Network. When actuating the relay from OKdo using the toggle pin, a value of 0xFF is scheduled for downlink. On the next cycle, the value is sent to CR02 to actuate the relay. You will see the green LED on OC03 light up indicating the relay’s contact is closed.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/ttn7.png" alt="alt text" width="60%" height="auto" align="center">

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo12.png" alt="alt text" width="60%" height="auto" align="center">

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/oc03contactclosed.jpg" alt="alt text" width="30%" height="auto" align="center">

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/operation.gif" alt="alt text" width="30%" height="auto" align="center">

