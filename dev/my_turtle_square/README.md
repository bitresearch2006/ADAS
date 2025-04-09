MOVE THE TURTLE IN A SQUARE PATH

#Step 1: Open terminal, source ROS 2, and go to workspace source directory

source /opt/ros/jazzy/setup.bash

cd ~/ros2_ws/src

#Step 2: Add your Python simulation script

cd ~/ros2_ws/src/my_turtle_square

touch turtle_square.py

chmod +x turtle_square.py

nano turtle_square.py

#Step 3: Update setup.py

nano ~/ros2_ws/src/my_turtle_square/setup.py

#Step 4: Build the workspace

cd ~/ros2_ws

colcon build

#Step 5: Source the environment

source install/setup.bash

#Step 6: Launch Turtlesim and your new node

Open Terminal 1:

source /opt/ros/jazzy/setup.bash

ros2 run turtlesim turtlesim_node

Open Terminal 2:

source ~/ros2_ws/install/setup.bash

ros2 run my_turtle_square turtle_square





