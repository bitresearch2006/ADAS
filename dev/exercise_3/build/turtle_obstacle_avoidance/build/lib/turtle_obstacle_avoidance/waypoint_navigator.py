import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

class WaypointNavigator(Node):
    def __init__(self):
        super().__init__('waypoint_navigator')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscriber = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.pose = None
        self.timer = self.create_timer(0.1, self.navigate)
        self.waypoints = [(2, 2), (8, 2), (8, 8), (2, 8)]
        self.current_waypoint_index = 0

    def pose_callback(self, msg):
        self.pose = msg

    def navigate(self):
        if self.pose is None or self.current_waypoint_index >= len(self.waypoints):
            return

        goal_x, goal_y = self.waypoints[self.current_waypoint_index]

        distance = math.sqrt((goal_x - self.pose.x)**2 + (goal_y - self.pose.y)**2)
        angle_to_goal = math.atan2(goal_y - self.pose.y, goal_x - self.pose.x)
        angle_diff = angle_to_goal - self.pose.theta

        msg = Twist()

        # Correct orientation
        if abs(angle_diff) > 0.1:
            msg.angular.z = 2.0 * angle_diff
        else:
            msg.linear.x = 2.0 * distance

        if distance < 0.5:
            self.get_logger().info(f'Reached waypoint {self.current_waypoint_index + 1}')
            self.current_waypoint_index += 1

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = WaypointNavigator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
