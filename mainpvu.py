#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                               InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


positions = [180, 140, 90, 0]
colors = [Color.BLUE, Color.RED, Color.YELLOW, Color.GREEN]

def variables():
    checkcolor=False
    dropcolorspecial=False
    checkangle=True
    mycolor = []


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

def calibrate_motors_and_sensors():
    print("Calibrating base motor to initial position...")
    base_motor.run(-60)
    while not touch_sensor.pressed():
        pass
    base_motor.stop()
    base_motor.reset_angle(0)
    print("Base motor is calibrated.")

    print("Calibrating elbow motor...")
    elbow_motor.run_until_stalled(-50, then=Stop.HOLD, duty_limit=30)
    elbow_motor.reset_angle(0)
    print("Elbow motor is calibrated.")

    print("Opening gripper for initial setup...")
    open_grip()

    print("Calibration complete. Ready for operations.")
    ev3.speaker.beep()
    open_grip()
  

def close_grip():  
    gripper_motor.run_until_stalled(200,then=Stop.COAST, duty_limit=25) #här
     


def open_grip():
    gripper_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=25) #här
    gripper_motor.reset_angle(0) 
    gripper_motor.run_target(200, -90)

# def open_grip():
#     gripper_motor.run_until_stalled(-200, then=Stop.HOLD, duty_limit=50)
#     gripper_motor.reset_angle(0)




# def elbow_up():
#     elbow_motor.run_until_stalled(50, then=Stop.HOLD, duty_limit=50)
#     elbow_motor.reset_angle(90) 

def elbow_up():
    elbow_motor.run_until_stalled(50, then=Stop.COAST, duty_limit=25) #här
    elbow_motor.reset_angle(1000)

# def elbow_down():
#     elbow_motor.run_until_stalled(-50, then=Stop.COAST, duty_limit=25)

def elbow_down():
    elbow_motor.run_until_stalled(-50, then=Stop.COAST, duty_limit=25) #här


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


def go_to_start_position():
    pos = int(input("Enter start position (0-3): ")) 
    position = positions[pos]  
    elbow_up()
    go_to_position(position)
    elbow_down()
    close_grip()

def go_to_position(pos): 
    elbow_up()
    base_motor.run_target(60, pos)


def pickup_position(pos):
    elbow_up()
    base_motor.run_target(90, pos)



def check_color(): 
    Colorfound = False
    ev3.speaker.say("Checking color")
    elbow_motor.reset_angle(0)
    elbow_motor.run_target(50, 40)
    wait(2000)

    while Colorfound == False: 
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


# def checking_angles(): # denna behöver man inte kalla på eftersom den tillkallas i nästa funktion
#    present = False
#    angle=(gripper_motor.angle())
#    ev3.screen.print(str(angle))


#    if angle<-20:
#        ev3.speaker.say("The motor is holding a block.")


#        present = True
  
#    else:
#        ev3.speaker.say("The motor is not holding a block.")
#    wait(1000)
#    return present

def checking_angles():
    angle = gripper_motor.angle()  # Hämta vinkeln för grippermotorn
    ev3.screen.print(str(angle))

    if angle < -20:
        ev3.speaker.say("The motor is holding a block.")
        return True
    else:
        ev3.speaker.say("The motor is not holding a block.")
        wait(1000)
        go_to_base_position()  # Gå tillbaka till baspositionen om motorn inte håller ett block
        if __name__ == "__main__":
            main()
  # Visa huvudmenyn igen
        return False


def checking_if_present(pos):
   present = False   
   pickup_position(pos)
   while present == False:
       open_grip()
       elbow_down()
       close_grip()
       present = checking_angles()
       elbow_up()

def pick_up(pos, cc):  # går till angiven position och tar upp klossen och läser av färgen, anta att cc är true, avlutas nere med closed grip
    ev3.screen.print("PICK UP")
    pickup_position(pos) 
    open_grip()
    elbow_down()
    close_grip()
    checking_angles()
    if cc is True:
        color = check_color()
    elbow_up()
    ev3.speaker.beep()
    if cc is True:
        return color

def startup(): # används i elevated
    ev3.speaker.say("Start")
    go_to_base_position()


def finished():  # används i elevated
    go_to_start_position()
    ev3.speaker.say("Finish")

def dropoff(position, color, dropcolorspecial): # ger positionen baserat på färgen
   if dropcolorspecial == True:    
        if color == Color.BLUE:
            position = positions[0]  # Uppdatera variabeln position istället för positions
        if color == Color.RED:
            position = positions[1]
        if color == Color.GREEN:
            position = positions[2]
        if color == Color.YELLOW:
            position = positions[3]



def elevated_pickup(pos, elevation):
    checkcolor = False
    dropcolor = False
    checkangle = True
    mycolor = []
   
    startup() 
    pickup_position(pos)
    open_grip()
    elbow_up()
    elbow_motor.run_target(50, elevation)
    wait(2000)
    close_grip()
    elbow_down()
    check_color()
    dropoff(positions[0], mycolor, dropcolor) 
    finished()

    

def elevated_dropoff(pos, elevation):
    checkcolor = False
    dropcolor = False
    checkangle = True
    mycolor = []

    go_to_position(90)
    elbow_up()
    elbow_motor.run_target(50, elevation)
    open_grip()
    finished()





def drop_off(color):
    if color == Color.BLUE:
        go_to_position(180)
    elif color == Color.RED:
        go_to_position(140)
    elif color == Color.GREEN:
        go_to_position(90)
    elif color == Color.YELLOW:
        go_to_position(0)
    elbow_down()  
    open_grip()
    elbow_up()


def main():
    while True:
        choice = menu()
        if choice == '1':
            pick_up_and_return()
        elif choice == '2':
            pick_up_and_drop_off()  
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


def pick_up_and_return():
    pos_pickup = int(input("Enter pick-up position (0-3): "))
    if pos_pickup == 0:
        pos = 40
    elif pos_pickup == 1:
        pos = 85
    elif pos_pickup == 2:
        pos = 135
    elif pos_pickup == 3:
        pos = 175
    pick_up(pos, True) 
    wait(2000)  
    go_to_base_position()
    open_grip()


def pick_up_and_drop_off():
    input_val = int(input("Enter pick-up position (0-3): "))
    if input_val == 0:
        pos = 40
    elif input_val == 1:
        pos = 85
    elif input_val == 2:
        pos = 135
    elif input_val == 3:
        pos = 175
    color = pick_up(pos, True)  
    wait(2000)  
    drop_off(color) 
    wait(2000)  
    go_to_base_position()  



def finished():
    go_to_base_position()  
    ev3.speaker.say("Finish")  
    menu()  


def menu():
    print("\nMain Menu:")
    print("1. Pick up and return")
    print("2. Pick up and drop off")
    print("3. Exit")
    return input("Enter your choice: ")


calibrate_motors_and_sensors()
open_grip()
go_to_base_position()
if __name__ == "__main__":
    main()







    
 

