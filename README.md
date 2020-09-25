# Self-Driving-RC-Car

## Pre-Requestites
Python3 working on RPI

OpenCV installed on RPI

Working VNC server on RPI


## Description
Self Driving Remote Control car with the use of a raspberry pi. Project cost was around £150 for RPI, the car and the connecting parts. This was my first ever try at anything to do with circuits so I had used an online tutorial in order to figure out how to do motor and sensor connections with the GPIO on the RPI. The car I bought had side doors that opened which made turning the RPI on and off much easier as well as charging the battery pack (Heads up, if you do decide to make one of these, make sure your battery pack can continuously output 5V/2.4A of power, otherwise your RPI will throttle). I did have to drill some holes at the top and front so the camera and sensor wires could be put through.

If your feeling frisky and want to control the RCCAR using your DualShock 4 controller you're going to need pyPS4Contoller installed on your RPI.
```bash
pip install pyPS4Controller
```
The code for controller control is dependant on how the motors are hooked onto the GPIO on the RPI. My code is on 
```bash
controller.py
```
But the GPIO numbers for you might be different.


In order to use, VNC into the RPI and run the programs as mentioned in the Instructions section.

## Pictures 

# Outside 
![Outside](https://raw.githubusercontent.com/ChiragVJ/Self-Driving-RC-Car/master/car%20pics/outside.jpg)
# Inside
![Inside](https://github.com/ChiragVJ/Self-Driving-RC-Car/blob/master/car%20pics/inside.jpg)
# Inside Zoom
![Indside Zoomed in](https://raw.githubusercontent.com/ChiragVJ/Self-Driving-RC-Car/master/car%20pics/inside%20zoom.jpg)
# Sideview
![Sideview](https://raw.githubusercontent.com/ChiragVJ/Self-Driving-RC-Car/master/car%20pics/sideview.jpg)

## Instructions

You can test if the car is working by using

```bash
keyboard_controls.py
```
To collect training data run

```bash
collect_data.py
```
Then run
```bash
video.py
```
Hit q on the pygame window once enough training is complete

Once the training data is collected run
```bash
model_training.py
```
This trains a model using the training data collected.

Finally, for self driving to begin run
```bash
self_drive.py
sensor.py
video.py
```

## Credits
This project was inspired by Ryan Zotti and his self driving rc car
His GitHub Project can be seen here : https://github.com/RyanZotti/Self-Driving-Car

## Links

[Training haar cascade]https://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html
