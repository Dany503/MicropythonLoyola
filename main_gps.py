from machine import UART
import time

com = UART(1,pins=("P2","P3")) 
    
while True:
    print(com.readline()) # leemos una línea completa
    time.sleep(0.5)
    