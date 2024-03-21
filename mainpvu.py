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
color_sensor = ColorSensor(Port.S2)
gripper_motor = Motor(Port.A)
elbow_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])
base_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])
touch_sensor = TouchSensor(Port.S1)
color_sensor = ColorSensor(Port.S2)


# Steg 2: Öppna och stänga klon

def close_grip():  
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
     

def open_grip():
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    gripper_motor.reset_angle(0) 
    gripper_motor.run_target(200, -90)


# Steg 3: Lyfta på armen upp och ner

def elbow_up():
    elbow_motor.run_until_stalled(50, then=Stop.HOLD, duty_limit=50)
    elbow_motor.reset_angle(90) 


def elbow_down():
    elbow_motor.run_until_stalled(-50, then=Stop.COAST, duty_limit=25)


# Steg 4: 


def base_position():
    elbow_up()
    base_motor.run(-90)
    while not touch_sensor.pressed():
        pass
    base_motor.stop()
    wait(1000)
    base_motor.reset_angle(0)

def gotoendposition():
    elbow_up()
    gotoposition(38)
    elbow_down()


def gotoposition(pos):
    elbow_up()
    base_motor.run_target(60, pos)


def pickupposition(pos):
    elbow_up()
    base_motor.run_target(90, pos)

gotoposition(pos)