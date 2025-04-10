
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class SquareMover(Node):
    def __init__(self):
        super().__init__('square_mover')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.move_in_square)
        self.cmd = Twist()
        self.counter = 0
        self.turning = False
        self.get_logger().info("Started moving in square.")

    def move_in_square(self):
        if self.counter >= 8:
            self.cmd.linear.x = 0.0
            self.cmd.angular.z = 0.0
            self.publisher_.publish(self.cmd)
            self.get_logger().info("Finished moving in square.")
            rclpy.shutdown()
            return

        if self.turning:
            self.cmd.linear.x = 0.0
            self.cmd.angular.z = 1.57  # Turn 90 degrees
            time.sleep(1)
        else:
            self.cmd.linear.x = 2.0
            self.cmd.angular.z = 0.0
            time.sleep(1)

        self.publisher_.publish(self.cmd)
        self.turning = not self.turning
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = SquareMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
