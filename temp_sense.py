import machine
import utime

sensor_temp = machine.ADC(4)

conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    
    # this equation converts the voltage into celsius temperature
    # this equation is given in the specification
    temperature = 27 - (reading - 0.706)/0.0017121
    
    print(f"celsius reading: {temperature}")
    utime.sleep(2)