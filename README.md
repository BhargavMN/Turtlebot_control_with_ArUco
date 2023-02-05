# TurtleSim Control with ArUco----------------------- Watch the MP4 video for visual understanding
Steps to use the node and the Repo</br>
----------------------------------
Clone the Repo</br>
Intialiaze the workspace using the Colcon build</br> 
Run the TurtleSim in seperate Terminal</br>
Using "ros2 run turtlesim turtlesim_node"
Source ros2 using bash
Run the node using "ros2 run my_rob_control camera_aruco"
Description-
The node is written using Python3 using rclpy , opencv, numpy, TutleSim and geometrymessages modules. The node subscribe the positional information of the turtleBot from the Topic "/turtle1/pose" and publishes velocity commands to the Topic "/turtle1/cmdvel". 
![alt text](https://github.com/BhargavMN/UR_5-control-with-ArUco-/blob/5ea09baa6a9233a046daddce9804c3738564d162/rosgraph.png)

</br>
The node "camera_aruco"  is used to publish linear velocity of X co-ordinates for the Turtlebot. This is computed by the relative position of the boundary box of Aruco Marker.If the center of the Boundary box is in upper part of the video feed, the linear X velocity is set to be positive, if it is in lower part of video feed , the linear X velocity will be set to negative.</br>
The Position of the Aruko Marker is detemined by the function "aruco_display" by drawing the boundary around marker, marks the center of each marker with a red dot and outputs the center co-ordinates of the marker.The function is the method the class "ArucoGenerator" which uses a pre-defined Aruco dictionary(ARCO_DICT).</br>

