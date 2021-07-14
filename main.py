from machine import Pin
import time

led = Pin(25, Pin.OUT)


##Blink Led 2 fast then wait 1
def blink():
    while True:
        led(1)
        time.sleep(1)
        led(0)
        time.sleep(1)
        led(1)
        time.sleep(1)
        led(0)
        time.sleep(2)
        print('done')
