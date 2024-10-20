import unittest
from io import StringIO
from unittest.mock import patch
from alerts.alert import check_alerts

class TestAlertingThresholds(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_temperature_alert(self, mock_stdout):
        # Sample weather data and thresholds for the test
        weather_data = {
            'city': 'Delhi',
            'temperature': 45,  # Simulated data
            'weather': 'Clear'  
        }
        thresholds = {
            'temp_threshold': 40,  # User-defined threshold
            'weather_condition_alert': 'thunderstorm'  # Condition for triggering alerts
        }
        
        # Call check_alerts with all necessary arguments
        check_alerts(weather_data['city'], weather_data['temperature'], weather_data['weather'], thresholds['temp_threshold'], thresholds['weather_condition_alert'])
        
        output = mock_stdout.getvalue()

        # Check if the correct alert was printed
        self.assertIn('ALERT: High temperature detected in Delhi!', output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_weather_condition_alert(self, mock_stdout):
        # Sample weather data and thresholds for the test
        weather_data = {
            'city': 'Mumbai',
            'temperature': 30,  # Simulated temperature data
            'weather': 'Rain'  # Simulated weather condition
        }
        thresholds = {
            'temp_threshold': 40,  # User-defined threshold
            'weather_condition_alert': 'Rain'  # Condition for triggering alerts
        }
        
        # Call check_alerts with all necessary arguments
        check_alerts(weather_data['city'], weather_data['temperature'], weather_data['weather'], thresholds['temp_threshold'], thresholds['weather_condition_alert'])
        
        # Capture the printed output
        output = mock_stdout.getvalue()

        # Check if the correct alert was printed
        self.assertIn('ALERT: Rain condition detected in Mumbai!', output)

if __name__ == '__main__':
    unittest.main()
