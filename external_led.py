import machine
import utime

led_external = machine.Pin(15, machine.Pin.OUT)
led_onboard = machine.Pin(25, machine.Pin.OUT)

while True:
    if led_external.value():
        led_onboard.value(1)
        led_external.value(0)
    else:
        led_onboard.value(0)
        led_external.value(1)
    
    utime.sleep(1)