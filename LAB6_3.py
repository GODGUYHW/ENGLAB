import RPi.GPIO as GPIO
import time
 
SW=22
LED=18
ledstate = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)
try:
  while True :
    if GPIO.wait_for_edge(SW, GPIO.FALLING):
        ledstate +=1
        if ledstate%2:
          print(f"LED => OFF")
          GPIO.output(LED, False)
        else:
          print(f"LED => ON")
          GPIO.output(LED, True)
   
except KeyboardInterrupt:
  GPIO.cleanup()
print("\nBye…")