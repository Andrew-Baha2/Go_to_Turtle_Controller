#Go-To-Turtle-Controller

## Description
It ia a go to controller that control the movement of the turtle in turtlesim simulator by giving it desired position

## Run Code
First you have to download ROS and run code on ubuntu os (recommended: ROS Noetic, Ubuntu 20.04)
* Create a workspace and copy the turtle_controller_pkg in it and open the workspace in a terminal and write `catkin_make`
* Open a new terminal
* Write `roscore`
* Open a new terminal
* Write `roslaunch turtle_controller_pkg turtle_controller.launch`
* Turtlesim will open and enter X coordinate then enter Y coordinate in the terminal, the turtle will go to the desired coordinates
