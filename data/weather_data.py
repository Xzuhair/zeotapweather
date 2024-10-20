import requests
import json
import os
import sys
from processing.aggregation import calculate_daily_summary
from alerts.alert import check_alerts
from processing.storage import save_daily_summary

API_KEY = 'YOUR-API-KEY'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def convert_temperature(kelvin_temp, unit='C'):
    if unit.upper() == 'C':
        return kelvin_temp - 273.15
    elif unit.upper() == 'F':
        return (kelvin_temp - 273.15) * 9/5 + 32
    else:
        return kelvin_temp  # Default to Kelvin if unknown unit

def get_weather_data(city, unit, temp_threshold, weather_condition_alert):
    complete_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]['main']
        temperature = convert_temperature(main['temp'], unit)
        feels_like = convert_temperature(main['feels_like'], unit)
        min_temp = convert_temperature(main['temp_min'], unit)
        max_temp = convert_temperature(main['temp_max'], unit)
        timestamp = data['dt']
        
        print(f"\nWeather data for {city}:")
        print(f"Main Weather: {weather}")
        print(f"Temperature: {temperature:.2f}°{unit}")
        print(f"Feels Like: {feels_like:.2f}°{unit}")
        print(f"Min Temp: {min_temp:.2f}°{unit}, Max Temp: {max_temp:.2f}°{unit}")
        print(f"Timestamp: {timestamp}")

        check_alerts(city, temperature, weather, temp_threshold, weather_condition_alert)
        
        return {
            'city': city,
            'main_weather': weather,
            'temperature': temperature,
            'feels_like': feels_like,
            'min_temp': min_temp,
            'max_temp': max_temp,
            'timestamp': timestamp
        }
    else:
        print(f"\nError: Unable to retrieve data for {city}. Please check the city name and try again.")
        return None

def main():
    print("Welcome to the Weather Monitoring System!")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
