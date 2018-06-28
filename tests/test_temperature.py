import unittest
from temperature.conversion import fahr_to_cels, fahr_to_kelv


class TemperatureTestCase(unittest.TestCase):
    def test_fahrenheit_to_kelvin(self):
        k = fahr_to_kelv(0.)
        self.assertAlmostEqual(k, 255.37, places=2)

    def test_fahrenheit_to_celsius(self):
        k = fahr_to_cels(0.)
        self.assertAlmostEqual(k, -17.777, places=2)


if __name__ == '__main__':
    unittest.main()
