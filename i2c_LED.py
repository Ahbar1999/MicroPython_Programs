import machine
import utime

sda = machine.Pin(0)
scl = machine.Pin(1)

i2c = machine.I2C(0, sda=sda, scl=scl)

utime.sleep_ms(50)

addr = i2c.scan()[0]
print("Address in use:", addr)

i2c.writeto(addr, '\x38H')
i2c.writeto(addr, '\x0EH')
utime.sleep_ms(50)

i2c.writeto(addr, "Hello")
utime.sleep_ms(50)
# BACKLIGHT ON
i2c.writeto(addr, '\x08')

utime.sleep(2)
