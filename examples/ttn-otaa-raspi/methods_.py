import smbus2
from time import sleep
import RPi.GPIO as gpio

oc03_addr = 0x38
cr02_addr = 0x08

bus = smbus2.SMBus(1)

def stringToBytes(string):
    retVal = []
    for i in string:
        retVal.append(ord(i))
    return retVal

def oc03_init():
    bus.write_byte_data(oc03_addr, 0x03, 0x00)

def oc03_write(state):
    bus.write_byte_data(oc03_addr, 0x01, state)


def transmitData(buf):
    try:
       busdata = bus.write_i2c_block_data(cr02_addr, 48, buf)
       sleep(1)
    except:
       pass

def receiveData():
    try:
       result = bus.read_byte(cr02_addr) & 0xFF
       sleep(1)
       return result
    except:
        pass

def cr02_init(appeui,deveui,appkey,debug):
    bus.write_byte(cr02_addr, int(debug))
    sleep(0.05)
    bus.write_byte(cr02_addr, 97)
    sleep(0.05)
    bus.write_i2c_block_data(cr02_addr, int(appeui[0]), appeui[1:16])
    sleep(0.05)
    bus.write_byte(cr02_addr, 98)
    sleep(0.05)
    bus.write_i2c_block_data(cr02_addr, int(deveui[0]), deveui[1:16])
    sleep(0.05)
    bus.write_byte(cr02_addr, 99)
    sleep(0.05)
    bus.write_i2c_block_data(cr02_addr, int(appkey[0]), appkey[1:32])
    sleep(0.05)


def cr02_reset():
    cr02_reset_pin = 18
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(cr02_reset_pin, gpio.OUT)
    gpio.output(cr02_reset_pin, gpio.LOW)
    sleep(0.01)
    gpio.output(cr02_reset_pin, gpio.HIGH)
    sleep(2)

