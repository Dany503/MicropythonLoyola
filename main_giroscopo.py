from machine import I2C
import time
i2c = I2C(1, pins=('P10','P11'))     # utilizamos los pines por defecto (P10=SDA, P11=SCL)
i2c.init(I2C.MASTER, baudrate=20000) # iniciamos como máster
print(i2c.scan()) # mostramos la lista de esclavos

PRODUCTID_REG = const(0x0F)
ACC_I2CADDR = const(0x69)

while True:
    print(i2c.readfrom_mem(ACC_I2CADDR, PRODUCTID_REG, 1))
    time.sleep(1)