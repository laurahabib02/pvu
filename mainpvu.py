#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                               InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#amna
# Create your objects here. Detta för att styra huvudenheten
ev3 = EV3Brick()


# Configure the gripper motor on Port A with default settings.
gripper_motor = Motor(Port.A)


# Configure the elbow motor. It has an 8-teeth and a 40-teeth gear
# connected to it. We would like positive speed values to make the
# arm go upward. This corresponds to counterclockwise rotation
# of the motor.
elbow_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])


# Configure the motor that rotates the base. It has a 12-teeth and a
# 36-teeth gear connected to it. We would like positive speed values
# to make the arm go away from the Touch Sensor. This corresponds
# to counterclockwise rotation of the motor.
base_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])


# Limit the elbow and base accelerations. This results in
# very smooth motion. Like an industrial robot.
elbow_motor.control.limits(speed=60, acceleration=120)
base_motor.control.limits(speed=60, acceleration=120)


# Set up the Touch Sensor. It acts as an end-switch in the base
# of the robot arm. It defines the starting point of the base.
base_switch = TouchSensor(Port.S1)


# Set up the Color Sensor. This sensor detects when the elbow
# is in the starting position. This is when the sensor sees the
# white beam up close.
elbow_sensor = ColorSensor(Port.S2)


# Initialize the elbow. First make it go down for one second.
# Then make it go upwards slowly (15 degrees per second) until
# the Color Sensor detects the white beam. Then reset the motor
# angle to make this the zero point. Finally, hold the motor
# in place so it does not move.
elbow_motor.run_time(-30, 1000)
elbow_motor.run(15)
while elbow_sensor.reflection() < 32:
   wait(10)
elbow_motor.reset_angle(0)
elbow_motor.hold()


# Initialize the base. First rotate it until the Touch Sensor
# in the base is pressed. Reset the motor angle to make this
# the zero point. Then hold the motor in place so it does not move.
base_motor.run(-60)
while not base_switch.pressed():
   wait(10)
base_motor.reset_angle(0)
base_motor.hold()


# Initialize the gripper. First rotate the motor until it stalls.
# Stalling means that it cannot move any further. This position
# corresponds to the closed position. Then rotate the motor
# by 90 degrees such that the gripper is open.
gripper_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
gripper_motor.reset_angle(0)
gripper_motor.run_target(200, -90)




def robot_pick(position):
   # This function makes the robot base rotate to the indicated
   # position. There it lowers the elbow, closes the gripper, and
   # raises the elbow to pick up the object.


   # Rotate to the pick-up position.
   base_motor.run_target(60, position) #vår indicated position är right 90 grader
   # Lower the arm.
   elbow_motor.run_target(60, -40) # armen sänks lite här
   # Close the gripper to grab the wheel stack.
   gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
   # Raise the arm to lift the wheel stack.
   elbow_motor.run_target(60, 0) # den lyfter EXTREMT lite om ens något, x borde vara grader och y hastighet, hur tillämpas hastigheten?




def robot_release(position):
   # This function makes the robot base rotate to the indicated
   # position. There it lowers the elbow, opens the gripper to
   # release the object. Then it raises its arm again.


   # Rotate to the drop-off position.
   base_motor.run_target(60, position)
   # Lower the arm to put the wheel stack on the ground.
   elbow_motor.run_target(60, -40)
   # Open the gripper to release the wheel stack.
   gripper_motor.run_target(200, -90) # ändra inte -90 eftersom det innebär öppen claw
   # Raise the arm.
   elbow_motor.run_target(60, 0)




# Play three beeps to indicate that the initialization is complete.
for i in range(3):
   ev3.speaker.beep()
   wait(100)


# Define the three destinations for picking up and moving the wheel stacks.
LEFT = 160
MIDDLE = 100
RIGHT = 40


# This is the main part of the program. It is a loop that repeats endlessly.
#
# First, the robot moves the object on the left towards the middle.
# Second, the robot moves the object on the right towards the left.
# Finally, the robot moves the object that is now in the middle, to the right.
#
# Now we have a wheel stack on the left and on the right as before, but they
# have switched places. Then the loop repeats to do this over and over.






while True:
   # Move a wheel stack from the left to the middle.
   robot_pick(LEFT)
   robot_release(MIDDLE)


   # Move a wheel stack from the right to the left.
   robot_pick(RIGHT)
   robot_release(LEFT)


   # Move a wheel stack from the middle to the right.
   robot_pick(MIDDLE)
   robot_release(RIGHT)





# Konfigurera motorer för hjul
# left_wheel_motor = Motor(Port.A)
# right_wheel_motor = Motor(Port.B)

# Skapa en DriveBase-instans för att styra hjulen
# robot = DriveBase(left_wheel_motor, right_wheel_motor, wheel_diameter=56, axle_track=114)


# # Konfigurera motorer för att styra olika delar av robotarmen
# tower_motor = Motor(Port.C)  # Motor för att rotera tornet
# arm_motor = Motor(Port.D)	# Motor för att lyfta/sänka armen
# claw_motor = Motor(Port.E)   # Motor för att öppna/stänga klon

# # Konfigurera färgsensor för att mäta färgerna på objekten
# color_sensor = ColorSensor(Port.S1)
# # Konfigurera trycksensor för att upptäcka begränsningen för rotation
# touch_sensor = TouchSensor(Port.S2)



# # Funktion för att köra roboten rakt framåt med en viss hastighet
# def drive_forward(speed):
# 	left_wheel_motor.run(speed)
# 	right_wheel_motor.run(speed)

# # Funktion för att köra roboten rakt bakåt med en viss hastighet
# def drive_backward(speed):
# 	left_wheel_motor.run(-speed)
# 	right_wheel_motor.run(-speed)

# # Funktion för att svänga roboten åt vänster med en viss hastighet
# def turn_left(speed):
# 	left_wheel_motor.run(-speed)
# 	right_wheel_motor.run(speed)

# # Funktion för att svänga roboten åt höger med en viss hastighet
# def turn_right(speed):
# 	left_wheel_motor.run(speed)
# 	right_wheel_motor.run(-speed)

# # Funktion för att stoppa robotens rörelse
# def stop():
# 	left_wheel_motor.stop()
# 	right_wheel_motor.stop()

# #### Wait ska läggas till med,  användbart att inkludera väntetider mellan rörelserna för att ge tillräckligt med tid för roboten att utföra varje rörelse innan den går vidare till nästa steg i programmet.


# # Definiera en funktion för att rotera tornet till en viss vinkel med en viss hastighet
# def rotate_tower(angle, speed):
# 	# Beräkna antalet grader som motorn behöver rotera för att nå önskad vinkel
# 	motor_angle = tower_motor.angle() + angle
# 	# Starta motorn och låt den rotera till den angivna vinkeln med den angivna hastigheten
# 	tower_motor.run_target(speed, motor_angle, Stop.HOLD, False)

# # Rotera tornet 90 grader med en hastighet på 100 - exepel för att se om den gör det
# rotate_tower(90, 100)
