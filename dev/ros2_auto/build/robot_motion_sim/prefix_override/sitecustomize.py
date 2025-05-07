import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mahasreeki_23/ros2_auto/install/robot_motion_sim'
