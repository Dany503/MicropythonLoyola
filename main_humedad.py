from machine import ADC
import time
adc = ADC() # creamos el objeto para el convertidor
pin_analogico = adc.channel(pin='P13', attn=ADC.ATTN_11DB) 
while(True):
# configuramos el pin 13, no olvidar el atenuador
    valor = pin_analogico.value() # realizamos la lectura
    print(valor) # mostramos por pantalla
    time.sleep(1)
