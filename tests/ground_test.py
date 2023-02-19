import unittest
from models.ground import Ground

class TestGround (unittest.TestCase):

    def setUp(self): 
        self.ground = Ground("Villa Park", "Aston Villa", "Birmingham", 42749, True)

    def test_ground_has_capacity(self):
        expected = 42749
        actual = self.ground.capacity
        self.assertEqual(expected, actual)