import time
import random
import math
import pandas as pd

class AutonomousVehicle:
    def __init__(self, route_map):
        self.speed = 0
        self.direction = 'forward'
        self.obstacle_detected = False
        self.route_map = route_map
        self.current_position_index = 0

    def detect_obstacle(self):
        # Simulate obstacle detection using LiDAR
        self.obstacle_detected = random.choice([True, False])

    def change_direction(self):
        if self.obstacle_detected:
            self.direction = 'left' if self.direction == 'forward' else 'forward'
            print(f"Obstacle detected! Changing direction to {self.direction}.")
        else:
            print("No obstacle detected. Continuing forward.")

    def calculate_speed(self, current_position, next_position):
        # Calculate the distance between the current position and the next position
        distance = math.sqrt((next_position[0] - current_position[0]) ** 2 + (next_position[1] - current_position[1]) ** 2)
        
        # Assume a constant time interval for simplicity
        time_interval = 1
        
        # Calculate speed as distance divided by time
        speed = distance / time_interval
        return speed

    def move(self):
        current_position = (self.route_map['x'][self.current_position_index], self.route_map['y'][self.current_position_index])
        self.update_position()
        next_position = (self.route_map['x'][self.current_position_index], self.route_map['y'][self.current_position_index])
        
        # Update speed based on the distance to the next position
        self.speed = self.calculate_speed(current_position, next_position)
        
        print(f"Moving to position {next_position} at speed {self.speed}.")

    def update_position(self):
        # Update the current position based on the route map
        if self.current_position_index < len(self.route_map['x']) - 1:
            self.current_position_index += 1
            current_position = (self.route_map['x'][self.current_position_index], self.route_map['y'][self.current_position_index])
            print(f"Current position: {current_position}")
        else:
            print("Reached the end of the route map.")

    def navigate_route(self):
        while self.current_position_index < len(self.route_map['x']) - 1:
            self.detect_obstacle()
            self.change_direction()
            self.move()
            time.sleep(1)
        print("Completed the route!")

if __name__ == "__main__":
    # Load the route map from the Excel file
    route_map_df = pd.read_excel('route_map.xlsx', engine='openpyxl')
    route_map = route_map_df.to_dict(orient='list')

    vehicle = AutonomousVehicle(route_map)
    vehicle.navigate_route()