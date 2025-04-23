import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/nand_mahasreeki_23/ADAS/exercise_2/install/gui_robot_circle'
