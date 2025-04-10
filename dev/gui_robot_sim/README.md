GUI-BASED 2D ROBOT SIMULATION IN A STRAIGHT LINE

#Step 1: Open terminal, source ROS 2, and go to workspace source directory

source /opt/ros/jazzy/setup.bash

cd ~/ros2_ws/src

#Step 2: Install pygame

sudo apt update

sudo apt install python3-pygame

#Step 3: Create a new package

cd ~/ros2_ws/src

ros2 pkg create --build-type ament_python gui_robot_sim

#Step 4: Create the Python simulation script & write the code

cd ~/ros2_ws/src/gui_robot_sim

touch robot_simulator.py

chmod +x robot_simulator.py

nano robot_simulator.py

#Step 5: Update setup.py

nano ~/ros2_ws/src/gui_robot_sim/setup.py

Step 6: Build and source

cd ~/ros2_ws

colcon build --packages-select gui_robot_sim

source install/setup.bash

#step 7: Run the simulation

#In Terminal 1:

source ~/ros2_ws/install/setup.bash

ros2 run gui_robot_sim robot_simulator

#In Terminal 2, publish movement commands:

source ~/ros2_ws/install/setup.bash

ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 1.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"

