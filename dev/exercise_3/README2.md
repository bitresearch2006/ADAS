TURTLE OBSTACLE AVOIDANCE

source /opt/ros/jazzy/setup.bash
cd ~/exercise_3
colcon build --packages-select turtle_obstacle_avoidance
source install/setup.bash

#Open new terminal

source /opt/ros/jazzy/setup.bash
source ~/exercise_3/install/setup.bash
ros2 run turtlesim turtlesim_node

#Open another terminal

source /opt/ros/jazzy/setup.bash
source ~/exercise_3/install/setup.bash
ros2 run turtle_obstacle_avoidance obstacle_avoider     #Deviates when obstacle is detected
ros2 run turtle_obstacle_avoidance spiral_search        #Shows spiral movement
ros2 run turtle_obstacle_avoidance waypoint_navigator   #Reached the specified waypoints
