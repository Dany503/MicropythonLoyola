from machine import Pin
import time
led = Pin('P9', mode=Pin.OUT)
while True:
    print("high")
    led.value(1)
    time.sleep(1)
    print("low")
    led.value(0)
    time.sleep(1)
