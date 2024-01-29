import RPi.GPIO as GPIO
import time
import drivers
GPIO.setmode(GPIO.BCM)
SW1  = 27  
SW2  = 17

lcd_position = 0


GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)

display = drivers.Lcd()
display.lcd_clear()


try:
    while True:
	
        if GPIO.event_detected(SW1):
            lcd_position += 1
            if lcd_position == 1:
                display.lcd_clear()
                display.lcd_display_string("Buranon", 1)
                display.lcd_display_string("116510400647-3", 2)
            elif lcd_position == 2:
                display.lcd_clear()
                display.lcd_display_string("Thibet", 1)
                display.lcd_display_string("116510400678-8", 2)
            elif lcd_position == 3:
                display.lcd_clear()
                display.lcd_display_string("Sataporn", 1)
                display.lcd_display_string("116510462047-1", 2)
                lcd_position = 0
        elif GPIO.event_detected(SW2):
            GPIO.cleanup()
            display.lcd_clear()
            print("\nBye...")

except KeyboardInterrupt:

   display.lcd_clear()
   print("\nBye...")