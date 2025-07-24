import unittest
from geometry_msgs.msg import Twist
from turtle_draw.main import compute_circle_velocity

class TestCircleVelocity(unittest.TestCase):

    def test_velocity_for_known_radius(self):
        speed = 2.5
        radius = 2.5
        msg = compute_circle_velocity(speed, radius)
        self.assertAlmostEqual(msg.linear.x, speed)
        self.assertAlmostEqual(msg.angular.z, 1.0)

    def test_zero_radius(self):
        speed = 2.5
        radius = 0.0
        msg = compute_circle_velocity(speed, radius)
        self.assertEqual(msg.angular.z, 0.0)

    def test_min_radius_boundary(self):
        speed = 2.5
        radius = 0.1
        msg = compute_circle_velocity(speed, radius)
        self.assertTrue(msg.angular.z > 0)

if __name__ == '__main__':
    unittest.main()
