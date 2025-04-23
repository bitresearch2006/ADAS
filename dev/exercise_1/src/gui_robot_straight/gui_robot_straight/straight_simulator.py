import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import pygame
import sys

class StraightSimulator(Node):
    def __init__(self):
        super().__init__('straight_simulator')
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10)
        
        self.linear_velocity = 0.0
        self.angular_velocity = 0.0
        self.x = 300
        self.y = 300
        self.angle = 0

        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Straight Line Robot Simulator')
        self.clock = pygame.time.Clock()

    def listener_callback(self, msg):
        self.linear_velocity = msg.linear.x
        self.angular_velocity = msg.angular.z
        self.get_logger().info(f'Received velocity: linear={self.linear_velocity}, angular={self.angular_velocity}')

    def run(self):
        while rclpy.ok():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    rclpy.shutdown()
                    sys.exit()

            # Update position — only move in the x-direction
            self.x += self.linear_velocity
            self.y += 0

            self.screen.fill((255, 255, 255))  # White background
            pygame.draw.rect(self.screen, (0, 0, 255), (self.x, self.y, 30, 30))  # Blue square
            pygame.display.flip()
            self.clock.tick(30)

            rclpy.spin_once(self, timeout_sec=0.01)

def main(args=None):
    rclpy.init(args=args)
    node = StraightSimulator()
    node.run()
