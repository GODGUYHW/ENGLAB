import RPi.GPIO as GPIO
LED1 = 4
LED2 = 18
LED3 = 23
SW = 22
count = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW, GPIO.IN)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
try :
  while True :
    if GPIO.wait_for_edge (SW, GPIO.RISING):
        if count == 0:
            GPIO.output (LED1, False)
            GPIO.output (LED2, False)
            GPIO.output (LED3, False)
            count = count + 1
        elif count == 1:
            GPIO.output (LED1, False)
            GPIO.output (LED2, False)
            GPIO.output (LED3, True)
            count = count + 1
        elif count == 2:
            GPIO.output (LED1, False)
            GPIO.output (LED2, True)
            GPIO.output (LED3, False)
            count = count + 1
        elif count == 3:
            GPIO.output (LED1, False)
            GPIO.output (LED2, True)
            GPIO.output (LED3, True)
            count = count + 1
        elif count == 4:
            GPIO.output (LED1, True)
            GPIO.output (LED2, False)
            GPIO.output (LED3, False)
            count = count + 1
        elif count == 5:
            GPIO.output (LED1, True)
            GPIO.output (LED2, False)
            GPIO.output (LED3, True)
            count = count + 1
        elif count == 6:
            GPIO.output (LED1, True)
            GPIO.output (LED2, True)
            GPIO.output (LED3, False)
            count = count + 1
        elif count == 7:
            GPIO.output (LED1, True)
            GPIO.output (LED2, True)
            GPIO.output (LED3, True)
            count = count - 7
except KeyboardInterrupt:
    GPIO.cleanup()
print("\nBye...")