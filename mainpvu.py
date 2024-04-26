#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                               InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

RIGHT = 0
MIDDLE = 90
LEFT = 140
LEFT_LEFT = 180
positions = [LEFT_LEFT, LEFT, MIDDLE, RIGHT]
colors = [Color.BLUE, Color.RED, Color.YELLOW, Color.GREEN]

def variables():
    checkcolor=False
    dropcolorspecial=False
    checkangle=True
    mycolor = []

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

elbow_motor.control.limits(speed=120, acceleration=120)
base_motor.control.limits(speed=120, acceleration=120)

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


def go_to_start_position(): # går och pick upp från positionen vi anger som position, start position avser positionen den ska till och inte base
    elbow_up()
    go_to_position(positions) # anger graderna åt vänster från base position, position måste definieras utanför samt innan funktionerna tillkallas
    elbow_down()
    close_grip()


def go_to_position(pos): # tillkallas i andra funktioner
    elbow_up()
    base_motor.run_target(60, pos)


def pickup_position(pos): # lite oklart
    elbow_up()
    base_motor.run_target(90, pos)


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


def checking_angles(): # denna behöver man inte kalla på eftersom den tillkallas i nästa funktion
   present = False
   angle=(gripper_motor.angle())
   ev3.screen.print(str(angle))


   if angle<-20:
       ev3.speaker.say("The motor is holding a block.")


       present = True
  
   else:
       ev3.speaker.say("The motor is not holding a block.")
   wait(1000)
   return present


def checking_if_present(pos):
   present = False   # kan man ändra isblock till något annat
   pickup_position(pos)
   while present == False:
       open_grip()
       elbow_down()
       close_grip()
       present = checking_angles()
       elbow_up()

def pick_up(pos,cc):
    ev3.screen.print("PICK UP")

    pickup_position(pos) 

    open_grip()
    elbow_down()
    close_grip()
    if cc is True:
        color = check_color()
    elbow_up()
    ev3.speaker.beep()
    if cc is True:
        return color

def startup(): # används i elevated
    ev3.speaker.say("Start")
    go_to_position(30)
    go_to_base_position()


def finished():  # används i elevated
    go_to_start_position()
    ev3.speaker.say("Finish")

def dropoff(position, color, dropcolorspecial): # byt ut 0,1,2,3
   if dropcolorspecial == True:    
        if color == Color.BLUE:
            position = positions[0]
        if color == Color.RED:
            position = positions[1]
        if color == Color.GREEN:
            position = positions[2]
        if color == Color.YELLOW:
            position = positions[3]


def elevated_pickup(pos, elevation):
    checkcolor=False
    dropcolorspecial=False
    checkangle=True
    mycolor = []

    startup() 
    pickup_position(pos)
    open_grip()
    elbow_up()
    elbow_motor.run_target(50, elevation)
    wait(2000)
    close_grip()
    elbow_up()
    dropoff(positions[0], mycolor, dropcolorspecial)
    finished()

def elevated_dropoff(pos, elevation):
    checkcolor=False
    dropcolorspecial=False
    checkangle=True
    mycolor = []

    go_to_position(pos)
    elbow_up()
    elbow_motor.run_target(50, elevation)
    open_grip()
    finished()






def run():
    #checkcolor if False does not check color, if true does check color
    checkcolor=False
    dropcolorspecial=False
    checkangle=False
    startup()
    mycolor = pick_up(positions[3], checkcolor)
    if checkangle == True:
        isblock = checking_angles()
        if isblock == False:
            ev3.speaker.say("There is no block")
            finished()
            return
    dropoff(positions[0], mycolor, dropcolorspecial)
    finished()
   



def run_until_block():
    checkcolor=False
    dropcolorspecial=False
    checkangle=True
    mycolor = []
    startup()
    checking_if_present(positions[2])
    dropoff(positions[0], mycolor, dropcolorspecial)
    finished()



def runtest():
    checkcolor=False
    dropcolorspecial=False
    checkangle=False
    startup()

    mycolor = pick_up(positions[3], checkcolor)

    elevated_dropoff(positions[2], 0)


# def menu():
#     print("Welcome to the Menu:")
#     print("1. Pick a pick up position")
#     print("2. Pick a drop off")
#     print("3. Exit")
#     return input("Enter your choice: ")

# while True:
#     choice = menu()
#     if choice == "1":
#         run()
#     elif choice == "2":
#         runtest()
#     elif choice == "3":
#         break
#     else:
#         print("Invalid choice. Please select again.")

def menu():
    while True:  # This loop keeps the menu running until the user chooses to exit.
        print("""
        What do you want to do?
        (1) Start pickup and dropoff sequence
        (2) Run test sequence
        (3) Run until a block is found
        (4) Exit
        """)
        try:
            user_choice = int(input("Your choice: "))  # Get user input and convert to integer.

            if user_choice == 1:
                run()  # Start the main pickup and dropoff sequence.
            elif user_choice == 2:
                runtest()  # Run a test sequence.
            elif user_choice == 3:
                run_until_block()  # Continue until a block is detected.
            elif user_choice == 4:
                print("Exiting program.")
                break  # Exit the loop, thus ending the program.
            else:
                print("Invalid option, please try again.")
        except ValueError:
            print("Please enter a valid number.")

# Call the menu function to start the menu.
menu()