#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                               InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Steg 1: Definiera alla motorer, sensorer och färger

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
colors = [Color.BLUE, Color.RED, Color.YELLOW, Color.GREEN]

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


# Steg 4: Hitta positionerna, base motor

def go_to_base_position(): # hittar utgångsläget, dvs graderna förhåller sig till detta
    open_grip()
    elbow_up()
    base_motor.run(-60)
    while not touch_sensor.pressed():
        pass
    base_motor.stop()
    wait(1000)
    base_motor.reset_angle(0)
    elbow_down()
    for i in range(3):
        ev3.speaker.beep()
        wait(100)


def go_to_start_position(): # går och pick upp från positionen vi anger som position
    elbow_up()
    go_to_position(position) # anger graderna åt vänster från base position, position måste definieras utanför samt innan funktionerna tillkallas
    elbow_down()
    close_grip()


def go_to_position(pos): # tillkallas i andra funktioner
    elbow_up()
    base_motor.run_target(60, pos)


def pickup_position(pos): # lite oklart
    elbow_up()
    base_motor.run_target(90, pos)



RIGHT = 45
MIDDLE = 90
LEFT = 135
LEFT_LEFT = 180

position = RIGHT
go_to_base_position()
go_to_start_position()
position = LEFT
go_to_start_position()
go_to_base_position()

def check_color(): # i check_color så begränsas elbow så att färgen kan läsas av
    Colorfound = False
    ev3.speaker.say("Checking color")
    elbow_motor.reset_angle(0)
    elbow_motor.run_target(50, 40)
    wait(2000)

    while Colorfound == False: # alla färger funkar sålänge den är nära nog
        measuredcolor = color_sensor.color()

        if measuredcolor in colors:
            if measuredcolor == Color.BLUE:
                ev3.speaker.say("blue")
            elif measuredcolor == Color.RED:
                ev3.speaker.say("red")
            elif measuredcolor == Color.GREEN:
                ev3.speaker.say("green")
            elif measuredcolor == Color.YELLOW:
                ev3.speaker.say("yellow")

            Colorfound = True
    return measuredcolor

  



# close_grip()
# check_color()
# elbow_down()
# open_grip()
# elbow_up()

