import pandas as pd
import json

def process_weather_data(weather_data):
    # Extract relevant data from the JSON response
    city = weather_data['name']
    main_weather = weather_data['weather'][0]['main']
    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    temp_min = weather_data['main']['temp_min']
    temp_max = weather_data['main']['temp_max']
    timestamp = weather_data['dt']  # Unix timestamp
    
    # Print the extracted weather data
    print(f"City: {city}")
    print(f"Main Weather: {main_weather}")
    print(f"Temperature: {temp}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Min Temp: {temp_min}°C, Max Temp: {temp_max}°C")
    print(f"Timestamp: {timestamp}")
    
    # Return the processed data for further analysis
    return {
        'city': city,
        'main_weather': main_weather,
        'temp': temp,
        'feels_like': feels_like,
        'temp_min': temp_min,
        'temp_max': temp_max,
        'timestamp': timestamp
    }


# To store weather data across the day
weather_data_store = []

def add_weather_data(data):
    """Adds processed weather data to the daily store."""
    weather_data_store.append(data)



def calculate_daily_summary(weather_data_list):
    total_temp = 0
    max_temp = float('-inf')
    min_temp = float('inf')
    weather_conditions = {}

    for data in weather_data_list:
        total_temp += data['temperature']
        max_temp = max(max_temp, data['max_temp'])
        min_temp = min(min_temp, data['min_temp'])
        
        # Count the occurrence of each weather condition
        condition = data['main_weather']
        if condition in weather_conditions:
            weather_conditions[condition] += 1
        else:
            weather_conditions[condition] = 1

    # Calculate average temperature
    average_temp = total_temp / len(weather_data_list)
    
    # Determine the dominant weather condition
    dominant_weather = max(weather_conditions, key=weather_conditions.get)

    return {
        'average_temp': average_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_weather': dominant_weather
    }


    # Calculate average temperature
    average_temp = total_temp / len(weather_data_list)
    
    # Determine the dominant weather condition
    dominant_weather = max(weather_conditions, key=weather_conditions.get)

    return {
        'average_temp': average_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_weather': dominant_weather
    }
