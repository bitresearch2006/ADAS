import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random

class RandomMover(Node):
    def __init__(self):
        super().__init__('random_mover')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.move_randomly)  # Every 0.5 seconds
        self.get_logger().info('Random movement started')

    def move_randomly(self):
        msg = Twist()
        
        # Generate random linear and angular velocities
        msg.linear.x = random.uniform(0.5, 2.0)  # Forward speed between 0.5 and 2.0
        msg.angular.z = random.uniform(-2.0, 2.0)  # Turn rate between -2 and 2
        
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: linear={msg.linear.x:.2f}, angular={msg.angular.z:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = RandomMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
