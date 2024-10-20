import tkinter as tk
import json
from data.weather_data import get_weather_data
from processing.storage import save_daily_summary, load_daily_summaries
from processing.aggregation import calculate_daily_summary
from processing.visualization import plot_temperature_trend
from collections import Counter

def get_weather_summary():
    cities = city_entry.get().split(',')  # Dynamically get cities from the entry field
    unit = 'metric' if temp_unit_var.get().strip().upper() == 'C' else 'imperial'  # Choose the correct unit based on user input
    temp_threshold = float(temp_threshold_entry.get())  # Get threshold from entry field
    weather_condition_alert = weather_condition_entry.get().split(',')  # Get weather conditions from the entry field

    all_weather_data = []
    cities_with_data = []
    avg_temperatures = []
    
    result_text.delete(1.0, tk.END)  # Clear previous results

    for city in cities:
        city = city.strip()  # Clean city name
        weather_data = get_weather_data(city, unit, temp_threshold, weather_condition_alert)  # Retrieve weather data
        
        if weather_data:
            # Check if unit is 'metric' (Celsius) or 'imperial' (Fahrenheit)
            if unit == 'metric':
                temperature = weather_data['temperature'] - 273.15  # Convert from Kelvin to Celsius
                feels_like = weather_data['feels_like'] - 273.15
                min_temp = weather_data['min_temp'] - 273.15
                max_temp = weather_data['max_temp'] - 273.15
                temp_unit = "°C"
            else:
                temperature = (weather_data['temperature'] - 273.15) * 9/5 + 32  # Convert from Kelvin to Fahrenheit
                feels_like = (weather_data['feels_like'] - 273.15) * 9/5 + 32
                min_temp = (weather_data['min_temp'] - 273.15) * 9/5 + 32
                max_temp = (weather_data['max_temp'] - 273.15) * 9/5 + 32
                temp_unit = "°F"
            
            result_text.insert(tk.END, f"Weather data for {city.capitalize()}:\n")
            result_text.insert(tk.END, f"Main Weather: {weather_data['main_weather']}\n")
            result_text.insert(tk.END, f"Temperature: {temperature:.2f}{temp_unit}\n")
            result_text.insert(tk.END, f"Feels Like: {feels_like:.2f}{temp_unit}\n")
            result_text.insert(tk.END, f"Min Temp: {min_temp:.2f}{temp_unit}, Max Temp: {max_temp:.2f}{temp_unit}\n")
            result_text.insert(tk.END, f"Timestamp: {weather_data['timestamp']}\n")
            
            weather_alert_triggered = weather_data['main_weather'].lower() in [wc.strip().lower() for wc in weather_condition_alert]
            temperature_alert_triggered = temperature > temp_threshold if unit == 'imperial' else temperature > (temp_threshold - 273.15)  # Threshold logic based on unit
            
            if weather_alert_triggered:
                result_text.insert(tk.END, f"Weather Alert: {city.capitalize()} is experiencing extreme weather: {weather_data['main_weather']}.\n")
            if temperature_alert_triggered:
                result_text.insert(tk.END, f"Temperature Alert: {city.capitalize()} temperature {temperature:.2f}{temp_unit} exceeds the threshold.\n")
            
            # Add valid weather data to lists for plotting
            all_weather_data.append(weather_data)
            cities_with_data.append(city.capitalize())  # Save the city name
            avg_temperatures.append(temperature)  # Save the converted temperature
            
            # Create a daily summary dictionary
            daily_summary = {
                'city': city.capitalize(),
                'average_temp': temperature,  # Use the current temperature as average (converted)
                'max_temp': max_temp,  # Converted max temp
                'min_temp': min_temp,  # Converted min temp
                'dominant_weather': weather_data['main_weather'],
            }
            
            # Save the daily summary
            save_daily_summary(daily_summary)

    # Load daily summaries
    loaded_summaries = load_daily_summaries()
    
    if loaded_summaries is None or len(loaded_summaries) == 0:
        result_text.insert(tk.END, "No daily summaries available.\n")
    else:
        for city in cities_with_data:  # Only process cities with valid data
            city_summaries = [summary for summary in loaded_summaries if isinstance(summary, dict) and summary.get('city', '').lower() == city.lower()]
            
            if city_summaries:
                result_text.insert(tk.END, f"Daily summary for {city}: {city_summaries[-1]}\n")  # Show the latest summary
            else:
                result_text.insert(tk.END, f"No daily summary available for {city}.\n")
    
    if len(cities_with_data) == len(avg_temperatures):
        plot_temperature_trend(cities_with_data, avg_temperatures)  # Pass both cities and temperatures
    else:
        result_text.insert(tk.END, "Error: The number of cities and average temperatures do not match.\n")


# GUI Setup
root = tk.Tk()
root.title("Weather Monitoring App")

# Input Fields
tk.Label(root, text="Enter cities (comma-separated):").pack()
city_entry = tk.Entry(root)
city_entry.pack()

tk.Label(root, text="Temperature Unit (C/F):").pack()
temp_unit_var = tk.StringVar(value='C')
tk.Entry(root, textvariable=temp_unit_var).pack()

tk.Label(root, text="Temperature Threshold:").pack()
temp_threshold_entry = tk.Entry(root)
temp_threshold_entry.pack()

tk.Label(root, text="Weather Condition Alert (comma-separated):").pack()
weather_condition_entry = tk.Entry(root)
weather_condition_entry.pack()

# Result Text Box
result_text = tk.Text(root, height=10, width=50)
result_text.pack()

# Get Weather Summary Button
summary_button = tk.Button(root, text="Get Weather Summary", command=get_weather_summary)
summary_button.pack()

root.mainloop()
