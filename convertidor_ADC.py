from machine import ADC
adc = ADC() # creamos el objeto para el convertidor
# configuramos el pin 13, no olvidar el atenuador
pin_analogico = adc.channel(pin='P13', attn=ADC.ATTN_11DB) 
valor = pin_analogico.value() # realizamos la lectura
print(valor) # mostramos por pantalla
tension = pin_analogico.voltage() # medimos la tensión
print(tension) # mostramos por pantalla
