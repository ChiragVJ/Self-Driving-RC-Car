# Self-Driving-RC-Car

## Description
Self Driving Remote Control car with the use of a raspberry pi. Project cost was around £150 for RPI, the car and the connecting parts. This was my first ever try at anything to do with circuits so I had used an online tutorial in order to figure out how to do motor and sensor connections with the GPIO on the RPI. The car I bought had side doors that opened which made turning the RPI on and off much easier. I did have to drill some holes at the top and front so the camera and sensor wires could be put through.

In order to use, VNC into the RPI and run the programs as mentioned in the Instructions section.

## Pictures 

![Outside](https://raw.githubusercontent.com/ChiragVJ/Self-Driving-RC-Car/master/car%20pics/outside.jpg)
![Inside](https://github.com/ChiragVJ/Self-Driving-RC-Car/blob/master/car%20pics/inside.jpg)
![Indside Zoomed in](https://raw.githubusercontent.com/ChiragVJ/Self-Driving-RC-Car/master/car%20pics/inside%20zoom.jpg)
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

