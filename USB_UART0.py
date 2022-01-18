from machine import UART, Pin
import time

uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

send = b'hello world\n\r'
uart0.write(send)  # write 5 bytes

time.sleep(5)

recv = bytes()
while uart0.any() > 0:
    recv += uart0.read(1)
    
print("Recived: ", recv.decode("utf-8"))