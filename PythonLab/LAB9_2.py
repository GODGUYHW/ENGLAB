from flask import Flask
import RPi.GPIO as GPIO
green = 3
red = 5
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(red,GPIO.OUT)
 
app = Flask(__name__)
 
@app.route('/<opt>/<opt1>')
def control(opt,opt1):
    if opt =='led1':
        if opt1 =='on':
            GPIO.output(green,True)
        elif opt1=='off':
            GPIO.output(green,False)
    elif opt =='led2':
        if opt1 =='on':
            GPIO.output(red,True)
        elif opt1=='off':
            GPIO.output(red,False)
    return f'{opt}-{opt1}'
 
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')