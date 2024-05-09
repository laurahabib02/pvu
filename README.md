1. Introduction
   - The customer has a problem with sorting the incoming packages in a warehouse. It is estimated that the delivery of packages poses a risk of injury to workers due to the irregular shapes as well as the
heavy weight of the packages.

   - Our team has been given the task to implement a program to enable robots to handle the sorting of the incoming packages in the warehouse. This by using different attributes such as color to sort the packages
into given categories. 



2. Getting started

To start the project, you need a working computer. On this computer you need to download python and VS code. The next step to be able to use your LEGO MINDSTORM robot is that you need to download the latest version
of Pybricks. This can be helpful because Pybricks offers, among other things, ready-made functions that can directly control the parts and motors that your robot has. You will also need to install the VSCode extension
LEGO Mindstorms EV3 MicroPython. Something else that can be recommended is to install GitHub, which is a perfect tool that facilitates group coding.


Links: 
VSCode download https://code.visualstudio.com/download 

Github download https://desktop.github.com/ 

Python download https://www.python.org/downloads/ 

Bricks download https://pybricks.com/install/ 


3. Building and Running

Building: 
In order to get the robot up and running you need to: 
1) Press on the start button on the robot. 
2) Start your VS code on your computer. 
3) Connecting the robot to the computer can be done by using a USB cable.
4) Upload the written code to your LEGO robot by choosing the right file and then pressing the upload button and then proceed with running the program. 
5) Calibrate on the robot to make it aline with the given project requirements.


Running: 
After setting up the needed tools such as VS code, LEGO robot and USB cable etc.
The robot starts by configuring and connecting the motors and sensors and setting the speed and acceleration limits. It then undergoes a calibration to make the motors and sensors more precise 
to achieve the correct positions and angles.

The user is then given three options:
1) Pick up and return.
   Here the robot picks up a block based on the user's input, and returns to the predetermined base position.
2) Pick up and drop off.
  Here the robot goes to the user's selected position, reads if there is a block, if the block is detected, it reads the color and drops off the block at the color's predetermined position.
3) Exit.
  Here the program ends.

For this to be possible, there are several functions that make the robot's claw open and close, the arm move up and down and color sensor, etc.



4. Requirements: 

- Pick up items (US01): The robot needs to have a mechanism to grasp and lift items securely from a surface.
- Drop off items (US02): The robot should be able to release items at specified locations, adjusting height and direction (in degrees) as necessary.
- Determine item presence (US03): The robot should through its sensors be able to detect the presence of an item at a given location.
- Color identification (US04): The robot should be equipped with a color sensor capable of identifying the color of an item.
- Color-based drop-off (US05): The robot should be capable of recognizing the color of an item and dropping it off at different pre-defined locations based on the identified color.
- Designated pick up (US01B): The robot should be able to pick up items at a specific and designated position.
- Color identification at designated position (US04B): The robot should have a color sensor to identify the color of the object at a designated position. 
- Customize pick up and drop off zone (US12): The robot should be able to get input by the user and there by determine the pick up and drop off zone. 
- US16: As a customer, I want the robot to be able to pick an item up and put it in the designated drop -off location within 5 seconds.





