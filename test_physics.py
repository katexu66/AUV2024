import unittest
import physics as p

class TestPhysics(unittest.TestCase):
    def buoyancy_test(self):
        self.almostEqual(p.calculate_buoyancy(100, 9), 8829)
    
    def float_test(self):
        pass
    def pressure_test(self):
        pass
    def acceleration_test(self):
        pass
    def angular_accel_test(self):
        pass
    def torque_test(self):
        pass
    def moment_of_inertia_test(self):
        pass