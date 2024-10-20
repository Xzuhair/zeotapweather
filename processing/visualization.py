import matplotlib.pyplot as plt
from processing.storage import load_daily_summaries

def plot_temperature_trend(cities, average_temps):
    # Ensure that cities and temperatures are provided
    if len(average_temps) == len(cities):
        plt.plot(cities, average_temps, label='Average Temperature', marker='o')
        plt.legend()
        plt.xlabel('Cities')
        plt.ylabel('Temperature')
        plt.title('Average Temperature Trend')
        plt.show()
    else:
        print("Error: The number of cities and average temperatures do not match.")

def load_and_plot_temperature_trend(cities):
    summaries = load_daily_summaries() 
    average_temps = []

    # Loop through each city to get average temperatures
    for city in cities:
        city_avg_temp = None
        for summary in summaries:
            if isinstance(summary, dict) and summary.get('city') == city:  # Ensure summary is a dict
                city_avg_temp = summary['average_temp'] 
                break
        
        if city_avg_temp is not None:  # Ensure there's an average temperature
            average_temps.append(city_avg_temp)

    # Call the function to plot temperatures with cities and average temperatures
    plot_temperature_trend(cities, average_temps)
