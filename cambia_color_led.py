import pycom # incluimos la librería de la tarjeta
import time # incluimo la librería time (para esperar tiempo)

pycom.heartbeat(False)
# los heartbeat son para comprobar que la tarjeta
# está funcionando se encienden y se apaga el led

for cycles in range(10): # un bucle que intera diez veces
    pycom.rgbled(0x007f00) # verde
    time.sleep(2) # espermos 2 segundos
    pycom.rgbled(0x7f7f00) # amarillo
    time.sleep(2) # esperamos 2 segundos
    pycom.rgbled(0x7f0000) # rojo
    time.sleep(4) # esperamos dos segundos
