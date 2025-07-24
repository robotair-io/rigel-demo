from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        # Start the turtlesim node
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim_node',
            output='screen',
        ),

        # Start the draw_robotair node
        Node(
            package='turtle_draw',
            executable='draw_robotair',
            name='draw_robotair',
            output='screen',
        ),
    ])
