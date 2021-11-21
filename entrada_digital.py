from machine import Pin
import time
led = Pin('P9', mode = Pin.OUT)
button = Pin('P10', mode = Pin.IN)
while True:
    if(button() == 1):
        led.value(1)
    else:
        led.value(0)
