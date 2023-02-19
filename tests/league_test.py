import unittest
from models.league import League

class TestLeague (unittest.TestCase):

    def setUp(self): 
        self.league = League("Premier League", "Logo", "Villa Park")

    def test_league_has_grounds(self):
        expected = "Villa Park"
        actual = self.league.grounds
        self.assertEqual(expected, actual)