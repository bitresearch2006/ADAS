import rclpy
from rclpy.node import Node
import pygame
import math

class CircleRobotGUI(Node):
    def __init__(self):
        super().__init__('circle_robot_gui')
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("2D Robot - Circle Path")
        self.clock = pygame.time.Clock()

        # Robot state
        self.radius = 100
        self.angle = 0.0
        self.center_x = 300
        self.center_y = 300
        self.robot_size = 20

        self.get_logger().info("2D Circular Robot GUI Initialized.")
        self.run()

    def run(self):
        running = True
        while running and rclpy.ok():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update robot position along circular path
            self.angle += 0.03  # speed
            x = self.center_x + self.radius * math.cos(self.angle)
            y = self.center_y + self.radius * math.sin(self.angle)

            self.screen.fill((255, 255, 255))  # Clear screen
            pygame.draw.circle(self.screen, (0, 0, 255), (int(x), int(y)), self.robot_size)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


def main(args=None):
    rclpy.init(args=args)
    gui_node = CircleRobotGUI()
    gui_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
