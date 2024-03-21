#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                               InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Definiera alla motorer och sensorer
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gripper_motor = Motor(Port.A)
touch_sensor = TouchSensor(Port.S1)
color_sensort = ColorSensor(Port.S2)

# Steg 1: öppna och stänga klon, requirement 1

def open_grip():
    grip_motor.run_to_rel_pos(position_sp=-500, speed_sp=250)  # Justera dessa värden
    grip_motor.wait_while('running')
    time.sleep(0.5)

# Funktion för att stänga greppet
def close_grip():
    grip_motor.run_forever(speed_sp=100)  # Justera hastigheten efter behov
    while not touch_sensor.is_pressed:  # Vänta tills touch sensorn är aktiverad
        pass
    grip_motor.stop()
    Sound.beep()  # Bekräftelse på att objektet har greppats

# Huvudprogram
open_grip()
close_grip()

def closegrip():  
    ev3.screen.print("CLOSE GRIP")
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
     


def opengrip():
    ev3.screen.print("OPEN GRIP")
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    gripper_motor.reset_angle(0) 
    gripper_motor.run_target(200, -90)