import unittest
from models.country import Country


class TestCountry (unittest.TestCase):

    def setUp(self):
        self.country = Country("England", "Logo", "Premier League")

    def test_country_has_name(self):
        expected = "England"
        actual = self.country.name
        self.assertEqual(expected, actual)