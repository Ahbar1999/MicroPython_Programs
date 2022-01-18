from machine import I2C
import utime
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
print(I2C_ADDR)
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16


lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
lcd.clear()
lcd.putstr("Ahbar Siddiqui")
utime.sleep(1)