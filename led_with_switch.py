import machine
import utime


led_external = machine.Pin(15, machine.Pin.OUT)
push_button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)


while True:
    if push_button.value() == 1:
        led_external.value(1)
        utime.sleep(2)
        
    led_external.value(0)