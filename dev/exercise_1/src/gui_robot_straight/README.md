GUI - STRAIGHT SIMULATION

#Source & Navigate to workspace

source /opt/ros/jazzy/setup.bash

cd ~/ADAS/exercise_1

#Build and Source

colcon build

source install/setup.bash

#Open a new terminal (GUI)

source /opt/ros/jazzy/setup.bash

source ~/ADAS/exercise_1/install/setup.bash

ros2 run gui_robot_straight straight_simulator

#Open another terminal (Publisher)

source /opt/ros/jazzy/setup.bash

source ~/ADAS/exercise_1/install/setup.bash

ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 1.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"





