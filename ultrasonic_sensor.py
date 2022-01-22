import machine
from machine import Pin
import utime

trigg = Pin(1, Pin.OUT)
echo = Pin(0, Pin.IN)

button = Pin(10, Pin.IN, Pin.PULL_DOWN)


def measure_distance():
    # prepare the trigg pin to send the signal, it take 10us to transmit
    trigg.value(0) # reset the pin to prepare 
    utime.sleep_us(5)
    trigg.value(1) # start the pulse
    utime.sleep_us(10) # wait 10 us
    trigg.value(0) # end the pulse

    # at this point the echo pin is turned to 1..
    # ..and will stay 1 until the signal is recieved back

    # machine.time_pulse_us measures how long the pin (echo) was in the given state (1)
    # 38ms is the max waiting time for the echo to recieve back the signal in other words 38 ms is the max time the pulse stays alive for
    pulse_time = machine.time_pulse_us(echo, 1, 38000)

    print("time: ", pulse_time, "us")
    # speed of sound: 0.34320 mm/us
    print("distance: ", ( pulse_time * 0.34320 ) / 2, "mm")


def button_handler(pin):
    measure_distance()

button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)

while True:
    pass



