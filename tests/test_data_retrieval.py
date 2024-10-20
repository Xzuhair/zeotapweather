import unittest
from unittest.mock import patch
from data.weather_data import get_weather_data

class TestDataRetrieval(unittest.TestCase):

    @patch('data.weather_data.requests.get')
    def test_retrieve_weather_data(self, mock_get):
        mock_response = {
            "main": {"temp": 300, "feels_like": 305, "temp_min": 295, "temp_max": 310},
            "weather": [{"main": "Clouds"}],
            "dt": 1629396446
        }
        
        # Mock the API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        city = "London"
        unit = "C"
        temp_threshold = 20.0
        weather_condition_alert = "Rain"
        
        result = get_weather_data(city, unit, temp_threshold, weather_condition_alert)
        self.assertIsNotNone(result)
        self.assertEqual(result['city'], city)
        self.assertAlmostEqual(result['temperature'], 26.85, places=2)  
        self.assertEqual(result['main_weather'], 'Clouds')


if __name__ == '__main__':
    unittest.main()
