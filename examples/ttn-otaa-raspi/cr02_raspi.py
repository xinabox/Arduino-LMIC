import bme280
import cbor
import methods_
from time import sleep

# things network keys. paste keys between quotes
appeui = methods_.stringToBytes('')
deveui = methods_.stringToBytes('')
appkey = methods_.stringToBytes('')

debug = 48  # set to 49 to enable debugging on CR02


# reset CR02
methods_.cr02_reset()

# sw01 i2c address
sw01_addr = 0x76

calibration_params = bme280.load_calibration_params(methods_.bus, sw01_addr)

methods_.cr02_init(appeui, deveui, appkey, debug)
methods_.oc03_init()

# open the relay initially
methods_oc03_write(0)

while True:

    SW01 = bme280.sample(methods_.bus, sw01_addr, calibration_params)
    temperature = round(SW01.temperature,2)
    humidity = round(SW01.humidity,2)
    pressure = int(round(SW01.pressure,0))
    print("T:",temperature)
    print("H:",humidity)
    print("P:",pressure)

    # send data to TTN
    methods_.transmitData(cbor.dumps({"t":temperature,"h":humidity,"p":pressure}))

    oc03_state = methods_.receiveData()

    # actuate relay based on state from OKdo
    if oc03_state == 48:
        methods_.oc03_write(0)
    if oc03_state == 49:
        methods_.oc03_write(1)
    sleep(2)
