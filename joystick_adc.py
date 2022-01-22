import machine
import utime

_x = machine.ADC(machine.Pin(27))
_y = machine.ADC(machine.Pin(26))
click = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

MAX_X = 100
MAX_Y = 100

def click_handler(pin):
        x_reading = (_x.read_u16() / 65535) * MAX_X
        y_reading = (_y.read_u16() / 65535) * MAX_Y  
        print("x coord:", x_reading, "y coord:", y_reading)
        utime.sleep(2)
        
click.irq(trigger=machine.Pin.IRQ_RISING, handler=click_handler)

while True:
    x_reading = _x.read_u16()
    y_reading =  _y.read_u16()
    print("x raw adc:", x_reading, "y raw adc:", y_reading)
    utime.sleep(2)


    