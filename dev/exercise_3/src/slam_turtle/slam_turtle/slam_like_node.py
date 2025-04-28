import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

class TurtleSLAM(Node):
    def __init__(self):
        super().__init__('turtle_slam_node')
        self.pose_subscriber = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.cmd_vel_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose = Pose()

    def pose_callback(self, msg):
        self.pose = msg
        self.get_logger().info(f"X: {msg.x:.2f}, Y: {msg.y:.2f}, Theta: {msg.theta:.2f}")

        # Move in a spiral - Simulated exploration
        vel_msg = Twist()
        vel_msg.linear.x = 2.0
        vel_msg.angular.z = 1.0 / msg.x if msg.x != 0 else 0
        self.cmd_vel_publisher.publish(vel_msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSLAM()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
