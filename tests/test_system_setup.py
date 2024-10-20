import unittest
from data.weather_data import get_weather_data

class TestSystemSetup(unittest.TestCase):
    
    def test_api_connection(self):
        city = "London"
        unit = "C"  # Celsius
        temp_threshold = 20.0
        weather_condition_alert = "Rain"
        
        # Ensure the API call retrieves data successfully
        result = get_weather_data(city, unit, temp_threshold, weather_condition_alert)
        self.assertIsNotNone(result, "API response is None, check your API key and city name.")
        
if __name__ == '__main__':
    unittest.main()
