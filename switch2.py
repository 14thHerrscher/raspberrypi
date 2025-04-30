import RPi.GPIO as GPIO

def button_callback(channel):
	print("Button was pushed!")

Switch= 10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(Switch,GPIO.RISING,callback=button_callback)

message = input("Press enter to quit\n\n")
GPIO.cleanup()
