# The Things Network and OKdo Integration using Arduino IDE and CR02

This example demonstrates how to transmit and receive information to and from the OKdo IoT cloud using LoRaWAN and the The Things Network. The CR02 with an onboard radio module is our LoRaWAN device. We will be transferring SW01 and SL01 environmental data from CR02 and receiving data from OKdo to the CR02 enabling us to actuate a relay onboard OC03.

## Requirements

- 1 x [IP01](https://xinabox.cc/products/ip01)/[IP02](https://xinabox.cc/products/ip02) - USB Programming Interface (FT232R)
- 1 x [OC03](https://xinabox.cc/products/oc03) - Relay Output (PCA9554A & TLP241A)
- 1 x [XC10](https://xinabox.cc/products/xc10) - 10-Pack xBus Connectors
- 1 x [SW01](https://xinabox.cc/products/sw01)- Temperature, Humidity, Pressure (BME280)
- 1 x [SL01](https://xinabox.cc/products/sl01)- Ambient Light and UV Sensor (VEML6075 & TSL4531)
- [Arduino IDE](https://www.arduino.cc/en/main/software)
- [OKdo IoT cloud](https://okdo.allthingstalk.com/)
- [The Things Network](https://thethingsnetwork.org)
- [arduino-SL01](https://github.com/xinabox/arduino-SL01)
- [arduino-SW01](https://github.com/xinabox/arduino-SW01)
- [arduino-OC03](https://github.com/xinabox/arduino-OC03)
- [arduino-CORE](https://github.com/xinabox/arduino-CORE)
- [arduino-LMIC](https://github.com/xinabox/arduino-LMIC)

## xChip Configuration

Assemble IP01, CR02, SW01, OC03 and SL01 as per the image below and insert it into your computer.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/cr02arduino.jpg" alt="alt text" width="35%" height="auto" align="center">

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

6. Add new assets to your device. For sensor data you’d want to create a sensor asset with a number data type. For actuating the OC03, you’d create an actuator asset with a boolean data type. Assets will need to be created with the names temperature, humidity, pressure, lux, uva, uvb and uvi. The OC03 asset will be named relay. Example shown below using t, h, p and r for names.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo5.png" alt="alt text" width="70%" height="auto" align="center">  <img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo6.png" alt="alt text" width="70%" height="auto" align="center">

6. Assets will be shown similar to below

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo7.png" alt="alt text" width="70%" height="auto" align="center">

7. In the settings menu in the top right corner, navigate to payload formats 

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo8.png" alt="alt text" width="70%" height="auto" align="center">

9. Enable use ABCL to convert custom binary data. We will be converting all binary data manually.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo9.png" alt="alt text" width="70%" height="auto" align="center">

10. Paste the okdoabcl.json contents in the field.

11. Create a new pinboard to visualize your data and to easily control OC03. New Pinboard > Pinboard Name > Arrange Pinboard > New pin > Select the toggle pin and assign it to your relay asset. You can assign the data log pin for sesnot data.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo11.png" alt="alt text" width="70%" height="auto" align="center">

That completes the OKdo setup


## Arduino Code

Replace the keys in the ttn-otaa.ino file with your keys from the The Things Network. Upload the code to CR02 using Arduino Pro Mini as the board. The keys will expand to array format when you click on the arrows. Change it to lsb for dev eui and appeui.


<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/ttn3.png" alt="alt text" width="70%" height="auto" align="center">

```c
static const u1_t PROGMEM APPEUI[8]={ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };
void os_getArtEui (u1_t* buf) { memcpy_P(buf, APPEUI, 8);}
 
// This should also be in little endian format, see above.
static const u1_t PROGMEM DEVEUI[8]={ 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };
void os_getDevEui (u1_t* buf) { memcpy_P(buf, DEVEUI, 8);}
 
// This key should be in big endian format (or, since it is not really a
// number but a block of memory, endianness does not really apply). In
// practice, a key taken from ttnctl can be copied as-is.
// The key shown here is the semtech default key.
static const u1_t PROGMEM APPKEY[16] = { 0x2B, 0x7E, 0x15, 0x16, 0x28, 0xAE, 0xD2, 0xA6, 0xAB, 0xF7, 0x15, 0x88, 0x09, 0xCF, 0x4F, 0x3C };
void os_getDevKey (u1_t* buf) {  memcpy_P(buf, APPKEY, 16);}
```

## Result

The green LED on CR02 will light up when you have succesfully connected to The Things Network. The LED will remain RED if a connection is being attempted.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/cr02joining .jpg" alt="alt text" width="30%" height="auto" align="center"> <img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/cr02joined.jpg" alt="alt text" width="30%" height="auto" align="center">

In your Things Network Console you’ll see data being received from CR02 as bytes. Data is only sent every minute to the Things Network. When actuating the relay from OKdo using the toggle pin, a value of 0xFF is scheduled for downlink. On the next cycle, the value is sent to CR02 to actuate the relay. You will see the LED on OC03 light up indicating the relay’s contact is closed.

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/ttn7.png" alt="alt text" width="70%" height="auto" align="center">

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/okdo12.png" alt="alt text" width="70%" height="auto" align="center">

<img src="https://github.com/xinabox/arduino-LMIC/blob/master/extras/cr02contactclosed.jpg" alt="alt text" width="70%" height="auto" align="center">


