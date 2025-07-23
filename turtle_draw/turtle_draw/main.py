#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random

def compute_circle_velocity(speed: float, radius: float) -> Twist:
    msg = Twist()
    msg.linear.x = speed
    msg.angular.z = speed / radius if radius > 0 else 0.0
    return msg

class DrawCircle(Node):

    def __init__(self):
        super().__init__('draw_circle')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # Circle parameters
        self.max_radius = 2.8
        self.min_radius = 0.1
        self.speed = 2.5
        self.radius = random.uniform(self.min_radius, self.max_radius)

        self.get_logger().info(f'Drawing circle with radius: {self.radius:.2f}')
        self.timer = self.create_timer(0.1, self.update_circle)

    def update_circle(self):
        vel_msg = compute_circle_velocity(self.speed, self.radius)
        self.publisher_.publish(vel_msg)

    def destroy_node(self):
        stop_msg = Twist()
        self.publisher_.publish(stop_msg)
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircle()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
