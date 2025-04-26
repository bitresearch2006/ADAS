import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class SpiralSearchNode(Node):
    def __init__(self):
        super().__init__('spiral_search_node')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move_in_spiral)
        self.speed = 1.0
        self.radius = 0.5
        self.angle = 0.0

    def move_in_spiral(self):
        msg = Twist()
        msg.linear.x = self.radius
        msg.angular.z = 1.0  # constant angular velocity

        self.radius += 0.05  # increase radius gradually to form a spiral
        self.publisher_.publish(msg)
        self.get_logger().info(f"Spiral Movement -> Linear: {msg.linear.x}, Angular: {msg.angular.z}")

def main(args=None):
    rclpy.init(args=args)
    node = SpiralSearchNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
