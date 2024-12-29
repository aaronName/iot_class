from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
import statistics

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# 設定馬達控制針腳
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
    
def setwheel(p17, p18, p22, p23):
    GPIO.output(17, p17)
    GPIO.output(18, p18)
    GPIO.output(22, p22)
    GPIO.output(23, p23)

app = Flask(__name__)

@app.route('/')
@app.route('/<cmd>')
def index(cmd=None):
    if cmd == 'stop':
        setwheel(False, False, False, False)
    if cmd == 'go':
        setwheel(False, True, False, True)
    if cmd == 'back':
        setwheel(True, False, True, False)
    if cmd == 'right':
        setwheel(False, False, False, True)
    if cmd == 'left':
        setwheel(False, True, False, False)
    if cmd == 'tare':
        hx.tare()
    
    return render_template('index2.html', cmd=cmd)

if(__name__ == "__main__"):
    app.run(host='0.0.0.0', port=5000, debug=True)
