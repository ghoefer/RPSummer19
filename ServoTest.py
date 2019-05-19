#program that opens and closes the server
#with help from Oscar Morrison Blog
import RPI.GPIO as IO
import time
pintOut = 4
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(pinOut,IO.OUT)
p = IO.PWM(pintOut,50)

def openFeeder():
    print('open feeder')
    p.start(2.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.75)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)
