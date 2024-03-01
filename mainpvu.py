#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                             	InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here. Detta för att styra huvudenheten
ev3 = EV3Brick()

# Konfigurera motorer för hjul
left_wheel_motor = Motor(Port.A)
right_wheel_motor = Motor(Port.B)

# Skapa en DriveBase-instans för att styra hjulen
robot = DriveBase(left_wheel_motor, right_wheel_motor, wheel_diameter=56, axle_track=114)


# Konfigurera motorer för att styra olika delar av robotarmen
tower_motor = Motor(Port.C)  # Motor för att rotera tornet
arm_motor = Motor(Port.D)	# Motor för att lyfta/sänka armen
claw_motor = Motor(Port.E)   # Motor för att öppna/stänga klon

# Konfigurera färgsensor för att mäta färgerna på objekten
color_sensor = ColorSensor(Port.S1)
# Konfigurera trycksensor för att upptäcka begränsningen för rotation
touch_sensor = TouchSensor(Port.S2)



# Funktion för att köra roboten rakt framåt med en viss hastighet
def drive_forward(speed):
	left_wheel_motor.run(speed)
	right_wheel_motor.run(speed)

# Funktion för att köra roboten rakt bakåt med en viss hastighet
def drive_backward(speed):
	left_wheel_motor.run(-speed)
	right_wheel_motor.run(-speed)

# Funktion för att svänga roboten åt vänster med en viss hastighet
def turn_left(speed):
	left_wheel_motor.run(-speed)
	right_wheel_motor.run(speed)

# Funktion för att svänga roboten åt höger med en viss hastighet
def turn_right(speed):
	left_wheel_motor.run(speed)
	right_wheel_motor.run(-speed)

# Funktion för att stoppa robotens rörelse
def stop():
	left_wheel_motor.stop()
	right_wheel_motor.stop()

#### Wait ska läggas till med,  användbart att inkludera väntetider mellan rörelserna för att ge tillräckligt med tid för roboten att utföra varje rörelse innan den går vidare till nästa steg i programmet.


# Definiera en funktion för att rotera tornet till en viss vinkel med en viss hastighet
def rotate_tower(angle, speed):
	# Beräkna antalet grader som motorn behöver rotera för att nå önskad vinkel
	motor_angle = tower_motor.angle() + angle
	# Starta motorn och låt den rotera till den angivna vinkeln med den angivna hastigheten
	tower_motor.run_target(speed, motor_angle, Stop.HOLD, False)

# Rotera tornet 90 grader med en hastighet på 100 - exepel för att se om den gör det
rotate_tower(90, 100)
