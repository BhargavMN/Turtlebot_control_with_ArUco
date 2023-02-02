# TurtleSim Control with ArUco
Steps to use the node and the Repo</br>
Clone the Repo</br>
Intialiaze the workspacen using the Colcon build</br> 
Run the TurtleSim in seperate Terminal</br>
Using "ros2 run turtlesim turtlesim_node"
Source ros2 using bash
Run the node using "ros2 run my_rob_control camera_aruco"
Description-
The node is written using Python3 using rclpy module, opencv, numpy, TutleSim, geometrymessages module. The nodes subscribe the positional information of the turtleBot from the Topic "/turtle1/pose" and publishes velocity commands to the Topic "/turtle1/cmdvel". 
rosgraph.png
