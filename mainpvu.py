#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                               InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Steg 1: Definiera alla motorer och sensorer
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gripper_motor = Motor(Port.A)
touch_sensor = TouchSensor(Port.S1)
color_sensort = ColorSensor(Port.S2)

# Steg 2: Öppna och stänga klon

def close_grip():  
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
     

def open_grip():
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    gripper_motor.reset_angle(0) 
    gripper_motor.run_target(200, -90)


# Steg 3: Lyfta på armen


