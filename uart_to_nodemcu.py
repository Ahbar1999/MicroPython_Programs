from machine import UART, Pin
import utime

sensor_temp = machine.ADC(4)

conversion_factor = 3.3 / (65535)

uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    
    # this equation converts the voltage into celsius temperature
    # this equation is given in the specification
    txData = temperature = 27 - (reading - 0.706)/0.0017121
    
    print(f"celsius reading: {txData}")
    uart0.write(bytes(int(txData)))
    utime.sleep(2)