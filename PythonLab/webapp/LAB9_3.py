from flask import Flask, render_template, request
import RPi.GPIO as GPIO
green = 2
red = 3
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(red,GPIO.OUT)
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/redon',methods=['POST'])
def redon():
    GPIO.output(red,True)
    return render_template('back.html')
@app.route('/redoff',methods=['POST'])
def redoff():
    GPIO.output(red,False)
    return render_template('back.html')
@app.route('/greenon',methods=['POST'])
def greenon():
    GPIO.output(green,True)
    return render_template('back.html')
@app.route('/greenoff',methods=['POST'])
def greenoff():
    GPIO.output(green,False)
    return render_template('back.html')
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')