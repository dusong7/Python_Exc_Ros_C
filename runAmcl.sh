#! /bin/bash

#! /bin/bash

##run on QT UI
source /opt/ros/indigo/setup.bash
#gnome-terminal -x bash -c "ls -la;exec bash"
##gnome-terminal -x bash -c "ls;exec bash"&&gnome-terminal -x bash -c "ls;exec bash"&&gnome-terminal -x bash -c "ls;exec bash"&&
#gnome-terminal -x bash -c "roslaunch turtlebot_gazebo turtlebot_world.launch;exec bash"
#sleep 5
#gnome-terminal -x bash -c "roslaunch turtlebot_rviz_launchers view_navigation.launch;exec bash"
#sleep 3
#gnome-terminal -x bash -c "roslaunch turtlebot_gazebo amcl_demo.launch map_file:=/home/admini/map6.yaml;exec bash" 

##gnome-terminal -x bash -c "ls;exec bash"&&gnome-terminal -x bash -c "ls;exec bash"&&gnome-terminal -x bash -c "ls;exec bash"&&
gnome-terminal -x bash -c "roslaunch turtlebot_gazebo turtlebot_world.launch;exec bash"
sleep 10
gnome-terminal -x bash -c "roslaunch turtlebot_gazebo amcl_demo.launch map_file:=/home/admini/map6.yaml;exec bash" 
sleep 5
gnome-terminal -x bash -c "roslaunch turtlebot_rviz_launchers view_navigation.launch;exec bash"

##system("gnome-terminal -e ./test");  
