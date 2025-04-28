import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class ObstacleAvoider(Node):
    def __init__(self):
        super().__init__('obstacle_avoider')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.pose = Pose()
        self.timer = self.create_timer(0.5, self.move_turtle)
        self.get_logger().info('Obstacle Avoider Initialized.')

    def pose_callback(self, msg):
        self.pose = msg

    def move_turtle(self):
        msg = Twist()
        if 1.0 < self.pose.x < 10.0 and 1.0 < self.pose.y < 10.0:
            msg.linear.x = 2.0
            msg.angular.z = 0.0
        else:
            msg.linear.x = 0.0
            msg.angular.z = 2.0
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
