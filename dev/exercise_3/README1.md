SLAM LIKE SETUP USING TURTLE SIMULATION

source /opt/ros/jazzy/setup.bash
cd ~/exercise_3
colcon build --packages-select slam_turtle
source install/setup.bash

#Open new terminal

source /opt/ros/jazzy/setup.bash
source ~/exercise_3/install/setup.bash
ros2 run turtlesim turtlesim_node

#Open another terminal

source /opt/ros/jazzy/setup.bash
source ~/exercise_3/install/setup.bash
ros2 run slam_turtle slam_like_node  #Forward movement of the turtle
ros2 run slam_turtle free_mover      #Rotates when close to the wall
ros2 run slam_turtle random_mover    #Exhibits random movement until we stop it 


