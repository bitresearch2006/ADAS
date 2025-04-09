import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class ObstacleAvoider(Node):
    def __init__(self):
        super().__init__('obstacle_avoider')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscriber = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.pose = None
        self.timer = self.create_timer(0.1, self.move_turtle)

    def pose_callback(self, msg):
        self.pose = msg

    def move_turtle(self):
        if self.pose is None:
            return

        cmd = Twist()

        # Simulated obstacle at (5, 5)
        obstacle_x = 5.0
        obstacle_y = 5.0
        distance = math.sqrt((self.pose.x - obstacle_x)**2 + (self.pose.y - obstacle_y)**2)

        if distance < 1.0:
            self.get_logger().info('Obstacle detected! Turning...')
            cmd.linear.x = 0.0
            cmd.angular.z = 2.0
        else:
            cmd.linear.x = 2.0
            cmd.angular.z = 0.0

        self.publisher.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
