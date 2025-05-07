import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan, Imu

class MotionNode(Node):
    def __init__(self):
        super().__init__('motion_node')
        self.sub_lidar = self.create_subscription(LaserScan, '/scan', self.lidar_callback, 10)
        self.sub_imu = self.create_subscription(Imu, '/imu', self.imu_callback, 10)
        self.moving = False
        self.last_distance = float('inf')

    def lidar_callback(self, msg):
        min_distance = min(msg.ranges)
        self.last_distance = min_distance

        if min_distance < 0.5:
            self.get_logger().info('Obstacle too close! Reversing')
        else:
            self.get_logger().info('Path clear. Moving forward')

    def imu_callback(self, msg):
        # Simulate using IMU angular velocity
        angular_z = msg.angular_velocity.z
        self.get_logger().info(f"IMU angular velocity: {angular_z:.2f}")

def main(args=None):
    rclpy.init(args=args)
    node = MotionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
