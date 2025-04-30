import RPi.GPIO as GPIO

import time

LED1 = 11
key = input()


GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED1, GPIO.OUT)

try:
    while 1:
        if key == '1':
            GPIO.output(LED1, GPIO.HIGH)

        elif key == '0':
            GPIO.output(LED1, GPIO.LOW)
    
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

