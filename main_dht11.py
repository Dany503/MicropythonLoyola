from machine import Pin
import utime as time
from midht import DHT11, InvalidChecksum

dhtPIN = 'P10'
dhtSensor = DHT11(Pin(dhtPIN, Pin.OUT, Pin.PULL_DOWN))

while True:
    print("Temp: {}°C".format(dhtSensor.temperature), "| Hum: {0:.1%}".format(dhtSensor.humidity/100))
    time.sleep(1.1)