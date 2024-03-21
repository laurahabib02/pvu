#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                               InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Steg 1: öppna och stänga klon, requirement 1

# from ev3dev.ev3 import MediumMotor, TouchSensor, Sound
# import time

# Initiera motor och sensor
grip_motor = Motor(Port.A)  # Antag att greppmotorn är ansluten till port A
touch_sensor = TouchSensor()

# Funktion för att öppna greppet
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

# Lägg till kod för att lyfta objektet här om så önskas
