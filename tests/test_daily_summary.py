import unittest
from processing.aggregation import calculate_daily_summary

class TestDailySummary(unittest.TestCase):

    def test_daily_summary(self):
        weather_data_list = [
            {'temperature': 30, 'max_temp': 32, 'min_temp': 28, 'main_weather': 'Clear'},
            {'temperature': 35, 'max_temp': 37, 'min_temp': 33, 'main_weather': 'Clouds'},
            {'temperature': 29, 'max_temp': 31, 'min_temp': 27, 'main_weather': 'Rain'},
        ]
        
        summary = calculate_daily_summary(weather_data_list)
        self.assertAlmostEqual(summary['average_temp'], 31.33, places=2)  
        self.assertEqual(summary['max_temp'], 37)
        self.assertEqual(summary['min_temp'], 27)
        self.assertEqual(summary['dominant_weather'], 'Clear') 


if __name__ == '__main__':
    unittest.main()
