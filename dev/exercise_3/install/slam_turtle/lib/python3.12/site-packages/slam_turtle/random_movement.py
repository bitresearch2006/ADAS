import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random

class RandomTurtleMover(Node):
    def __init__(self):
        super().__init__('random_turtle_mover')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.pose = None
        self.timer = self.create_timer(1.0, self.move_turtle)

    def pose_callback(self, msg):
        self.pose = msg

    def move_turtle(self):
        if self.pose is None:
            return

        twist = Twist()

        # Check boundaries
        if self.pose.x < 2.0 or self.pose.x > 9.0 or self.pose.y < 2.0 or self.pose.y > 9.0:
            # If close to wall, turn randomly
            twist.linear.x = 0.0
            twist.angular.z = random.uniform(1.0, 3.0)
            self.get_logger().info('Too close to wall. Turning...')
        else:
            # Move forward randomly
            twist.linear.x = random.uniform(1.0, 2.0)
            twist.angular.z = random.uniform(-1.0, 1.0)
            self.get_logger().info('Moving randomly.')

        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = RandomTurtleMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
