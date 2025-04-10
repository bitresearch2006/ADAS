TURTLESIM OBSTACLE AVOIDANCE SIMULATION

#Step 1: Open your terminal and run

source /opt/ros/jazzy/setup.bash
        
cd ~/ros2_ws/src

#Step 2: Write the Python Node

cd ~/ros2_ws/src/turtle_obstacle_avoidance

touch obstacle_avoider.py

chmod +x obstacle_avoider.py

        
#Step 3: Open the file and write the code:

nano obstacle_avoider.py


#Step 4: Update setup.py

nano ~/ros2_ws/src/turtle_obstacle_avoidance/setup.py


#Step 5: Build and Source the Workspace

cd ~/ros2_ws

colcon build --packages-select turtle_obstacle_avoidance

source install/setup.bash

#Step 6: Launch the Simulation

Open Terminal 1:

source ~/ros2_ws/install/setup.bash

ros2 run turtlesim turtlesim_node

Open Terminal 2:

source ~/ros2_ws/install/setup.bash

ros2 run turtle_obstacle_avoidance obstacle_avoider
