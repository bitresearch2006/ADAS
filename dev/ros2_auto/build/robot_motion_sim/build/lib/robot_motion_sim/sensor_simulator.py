import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan, Imu
import random
import math
import time

class SensorSimulator(Node):
    def __init__(self):
        super().__init__('sensor_simulator')
        self.lidar_pub = self.create_publisher(LaserScan, '/scan', 10)
        self.imu_pub = self.create_publisher(Imu, '/imu', 10)
        self.timer = self.create_timer(1.0, self.publish_fake_data)

    def publish_fake_data(self):
        # Publish fake LIDAR scan
        lidar_msg = LaserScan()
        lidar_msg.ranges = [random.uniform(0.2, 5.0) for _ in range(360)]
        self.lidar_pub.publish(lidar_msg)

        # Publish fake IMU data
        imu_msg = Imu()
        imu_msg.linear_acceleration.x = random.uniform(-2.0, 2.0)
        imu_msg.angular_velocity.z = random.uniform(-1.0, 1.0)
        self.imu_pub.publish(imu_msg)

        self.get_logger().info('Published fake /scan and /imu data')

def main(args=None):
    rclpy.init(args=args)
    node = SensorSimulator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

