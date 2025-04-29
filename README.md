Installation of ROS2 Jazzy Jalisco in Linux Ubuntu 24.04 (Noble)

1.Resources
Status Page:
•ROS 2 Jazzy (Ubuntu Noble 24.04): amd64, arm64
•Jenkins Instance
•Repositories


2.System setup (Follow the commands one by one)
# Open the terminal and enter "wsl"

(i)Set locale

 Locale     # Check for UTF-8
     sudo apt update && sudo apt install locales
     sudo locale-gen en_US en_US.UTF-8
     sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
     export LANG=en_US.UTF-8
     locale     # verify settings

(ii)Enable required repositories

•First ensure that the Ubuntu Universe repository is enabled.
     sudo apt install software-properties-common
     sudo add-apt-repository universe

•Now add the ROS 2 GPG key with apt.
     sudo apt update && sudo apt install curl -y
     sudo curl -sSL  https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

•Then add the repository to your sources list.

     echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null


3.Install development tools
     sudo apt update && sudo apt install ros-dev tools


4.Install ROS 2

•Update & Upgrade your apt repository caches after setting up the repositories.

     sudo apt update
     sudo apt upgrade
     sudo apt install ros-jazzy-desktop
     sudo apt install ros-jazzy-ros-base


5.Setup Environment
source /opt/ros/jazzy/setup.bash

