import RPi.GPIO as GPIO
import drivers
from time import sleep
GPIO.setmode(GPIO.BCM)
SW1  = 27  
SW2  = 17
num_spaces = 0
lcd_position = 0
num_cols = 16
text_to_print = "LAB 7"
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)
display = drivers.Lcd()

try:
    while True:
        if GPIO.event_detected(SW1):
            lcd_position+=1
            num_spaces+=1
            print(lcd_position)
            print(num_spaces)
            if lcd_position == 12:
                lcd_position = 11
                num_spaces = 11
            else:
                message = " " *num_spaces
                display.lcd_display_string(message + text_to_print, 1)
        elif GPIO.event_detected(SW2):
            print(num_spaces)
            print(lcd_position)
            if lcd_position == 0:
                lcd_position =0
                num_spaces = 0
            else:
                lcd_position-=1
                num_spaces-=1
                message = " " *num_spaces
                message1=" "
                display.lcd_display_string(message+text_to_print+message1, 1)
except KeyboardInterrupt:

	print("Cleaning up!")
	display.lcd_clear()