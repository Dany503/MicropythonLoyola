from machine import I2C
import time
i2c = I2C(1, pins=('P10','P11'))     # utilizamos los pines por defecto (P10=SDA, P11=SCL)
i2c.init(I2C.MASTER, baudrate=20000) # iniciamos como máster
print(i2c.scan()) # mostramos la lista de esclavos

ACC_I2CADDR = const(0x23)
CONTINUOUS_HIGH_RES_MODE_1 = 0x10
POWER_DOWN = 0x00 
POWER_ON = 0x01 
RESET = 0x07 

#i2c.writeto(ACC_I2CADDR, POWER_DOWN)
i2c.writeto(ACC_I2CADDR, POWER_ON)
i2c.writeto(ACC_I2CADDR, CONTINUOUS_HIGH_RES_MODE_1)
time.sleep(0.2)
medida = i2c.readfrom(ACC_I2CADDR, 2)
print(medida)


