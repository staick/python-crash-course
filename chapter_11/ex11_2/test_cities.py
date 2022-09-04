import unittest

from city_functions import display_city_country

class CityCountryTestCase(unittest.TestCase):
    """Test for 'city_functions.py.'"""

    def test_city_country(self):
        """Do display like 'Santiago, Chile' work?"""
        display = display_city_country('santigo', 'chile')
        self.assertEqual(display, 'Santigo, Chile')

    def test_city_country_population(self):
        """Do display like 'Santiago, Chile - population 5000000'"""
        display = display_city_country('santiago', 'chile', population=5000000)
        self.assertEqual(display, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
