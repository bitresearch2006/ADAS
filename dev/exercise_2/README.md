GUI - CIRCLE SIMULATION

#Source & Navigate to workspace

source /opt/ros/jazzy/setup.bash

cd ~/ADAS/exercise_2

#Build and Source

colcon build

source install/setup.bash

#Open a new terminal 

source /opt/ros/jazzy/setup.bash

source ~/ADAS/exercise_2/install/setup.bash

ros2 run gui_robot_circle circle_simulator
