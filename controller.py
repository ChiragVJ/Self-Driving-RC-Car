import RPi.GPIO as GPIO
from pyPS4Controller.controller import Controller
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
Motor2A = 19
Motor2B = 21
Motor2E = 23
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)
 
class MyController(Controller):

    def __init__(self, **kwargs):
            Controller.__init__(self, **kwargs)

    def on_L2_press(self, direction):
            GPIO.output(Motor2A,GPIO.LOW)
            GPIO.output(Motor2B,GPIO.HIGH)
            GPIO.output(Motor2E,GPIO.HIGH)
            #print("hello")
            
    def on_R2_press(self, direction):
            GPIO.output(Motor2A,GPIO.HIGH)
            GPIO.output(Motor2B,GPIO.LOW)
            GPIO.output(Motor2E,GPIO.HIGH)
            #print("hello")
            
    def on_R2_release(self):
            #print("hello")
            GPIO.output(Motor2E,GPIO.LOW)
    def on_L2_release(self):
            #print("hello")
            GPIO.output(Motor2E,GPIO.LOW)
            
    def on_L3_right(self, pressure):
            GPIO.output(Motor1A,GPIO.LOW)
            GPIO.output(Motor1B,GPIO.HIGH)
            GPIO.output(Motor1E,GPIO.HIGH)
   
    def on_L3_left(self, pressure):

            GPIO.output(Motor1A,GPIO.HIGH)
            GPIO.output(Motor1B,GPIO.LOW)
            GPIO.output(Motor1E,GPIO.HIGH)
            
    def on_L3_at_rest(self, **kwargs):
            #print("hello")
            GPIO.output(Motor1E,GPIO.LOW)

   

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)




