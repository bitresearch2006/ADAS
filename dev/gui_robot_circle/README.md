GUI-BASED 2D ROBOT SIMULATION IN A CIRCLE

#Step 1: Open terminal, source ROS 2, and go to workspace source directory

source /opt/ros/jazzy/setup.bash

cd ~/ros2_ws/src

#Step 2: Create a New Package

ros2 pkg create --build-type ament_python gui_robot_circle

#Step 3: Create Python Script

cd ~/ros2_ws/src/gui_robot_circle

touch circle_simulator.py

chmod +x circle_simulator.py

nano circle simulator.py

#Step 4: Update setup() file

nano ~/ros2_ws/src/gui_robot_circle/setup.py

#Step 5: Build and Source

cd ~/ros2_ws

colcon build --packages-select gui_robot_circle

source install/setup.bash

#Step 6: Run simulation

#Open new terminal:

source ~/ros2_ws/install/setup.bash

ros2 run gui_robot_circle circle_robot
