import RPi.GPIO as GPIO
from time import sleep
import pygame

pygame.init()
pygame.display.set_mode((250, 250))

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
 


  
def backward():
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        GPIO.output(Motor2E,GPIO.HIGH)
        #print("hello")
        
def forward():
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)
        #print("hello")
        
def stop():
        #print("hello")
        GPIO.output(Motor2E,GPIO.LOW)
        
def right():
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.HIGH)

def left():

        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)
        
def stop2():
        #print("hello")
        GPIO.output(Motor1E,GPIO.LOW)

control = True
while control:
     for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
            key_input = pygame.key.get_pressed()
            
            if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
                print("Forward Right")
                forward()
                right()
                

            elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
                print("Forward Left")
                forward()
                left()
                

            elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
                print("Reverse Right")
                backward()
                right()
               

            elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
                print("Reverse Left")
                backward()
                left()
            elif key_input[pygame.K_UP]:
                print("Forward")
                forward()

            elif key_input[pygame.K_DOWN]:
                print("Reverse")
                backward()

            elif key_input[pygame.K_RIGHT]:
                print("Right")
                right()

            elif key_input[pygame.K_LEFT]:
                print("Left")
                left()
            elif key_input[pygame.K_x] or key_input[pygame.K_q]:
                print("exit")
                control = False
                break
         if event.type == pygame.KEYUP:
            stop()
            stop2()
         if event.type == pygame.QUIT:
            stop()
            stop2()







