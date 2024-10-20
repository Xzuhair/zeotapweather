# Real-Time Weather Monitoring System

This application is a Real-Time Weather Monitoring System that retrieves weather data from the OpenWeatherMap API, processes it to provide insights, and stores daily summaries. The application includes features such as temperature alerts, daily weather summaries, and visualizations.

## Features
- Real-time weather data retrieval for multiple cities in India (ex:Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).
- Temperature conversion between Celsius and Fahrenheit.
- Daily weather summaries with average, maximum, minimum temperatures, and dominant weather conditions. Also storing this in daily_summary.json file.
- Alerts triggered based on user-defined thresholds for temperature and weather conditions. Also stored in alerts.json file.
- Visualization of daily average temperature, also we can compare the average temperature between the cities
- Comprehensive unit tests implemented to verify the code implementation.

## Project Structure
<zeoweather>/
│
├── alerts/
│   └── alert.py              # Contains alert logic
│
├── data/
│   ├── weather_data.py       # Handles data retrieval from OpenWeatherMap API
│   └── weather_gui.py        # User interface for input and displaying weather data
│
├── processing/
│   ├── aggregation.py        # Contains data aggregation functions for rollups and summaries
│   ├── storage.py            # Contains functions to save and load data from json files
│   └── visualization.py      # Contains plotting functions
├── tests/
│   ├── test_alerts.py        # Unit tests for alert system
│   ├── test_daily_summaries.py # Unit tests for daily summary calculations
│   ├── test_data_retrieval.py # Unit tests for weather data retrieval
│   ├── test_system_setup.py  # Unit tests for system setup and API connection
│   └── test_temperature_conversion.py # Unit tests for temperature conversion logic
│
│
├── alerts.json               # Stores triggered alerts data
├── daily_summary.json        # Stores daily weather summaries
├── config.py                 # Configuration settings (API keys and thresholds)
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation


## Installation

- Clone the repository:
   ```bash
   git clone https://github.com/Xzuhair/zeotapweather.git
   cd zeoweather


## Requirements
-To run this application, you need to install the following dependencies:

requests
matplotlib
Tkinter

## Running the Application
-To run the application, use the following command:

```bash
python -m data.weather_gui

Notes:
1. Make sure to set your OpenWeatherMap API key in config.py.
2. The application retrieves data for the specified cities and displays it in a graphical interface.
3. Daily summaries and alerts are saved in daily_summary.json and alerts.json, respectively.

##Final Testing
- Run the following command to execute all unit tests:

python -m unittest discover tests

## Conclusion
- This project provides a robust weather monitoring solution, with the potential for future enhancements. Feel free to explore and extend its functionality as needed.

