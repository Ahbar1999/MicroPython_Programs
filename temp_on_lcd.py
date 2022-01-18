from machine import I2C
import utime
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

# LCD INIT
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
print(I2C_ADDR)
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)


# TEMP SENSOR INIT
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    
    # this equation converts the voltage into celsius temperature
    # this equation is given in the specification
    temperature = 27 - (reading - 0.706)/0.0017121

    lcd.clear()
    lcd.putstr("Temp: ")
    lcd.putstr(str(temperature))
    utime.sleep(10)
    lcd.clear()
    lcd.putstr("Refreshing...")
    utime.sleep(2)
