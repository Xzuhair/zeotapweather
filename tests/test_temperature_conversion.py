import unittest
from data.weather_data import convert_temperature

class TestTemperatureConversion(unittest.TestCase):
    
    def test_kelvin_to_celsius(self):
        kelvin_temp = 300  
        expected_celsius = 26.85 
        self.assertAlmostEqual(convert_temperature(kelvin_temp, 'C'), expected_celsius, places=2)

    def test_kelvin_to_fahrenheit(self):
        kelvin_temp = 300  
        expected_fahrenheit = 80.33  
        self.assertAlmostEqual(convert_temperature(kelvin_temp, 'F'), expected_fahrenheit, places=2)
        
    def test_kelvin_default(self):
        kelvin_temp = 300  # Should return Kelvin when unit is unknown
        self.assertEqual(convert_temperature(kelvin_temp, 'K'), kelvin_temp)

if __name__ == '__main__':
    unittest.main()
