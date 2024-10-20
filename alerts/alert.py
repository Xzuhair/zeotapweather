import time
from config import TEMP_THRESHOLD, WEATHER_CONDITION_ALERT
from processing.storage import save_alert

# Alert state flags
alert_triggered = {
    'temperature': False,
    'weather': False
}

def check_alerts(city, temperature, weather, temp_threshold, weather_condition_alert):
    """Checks if the weather data triggers an alert based on temperature and weather condition thresholds."""
    
    print(f"DEBUG: Checking alerts for {city} - Temperature: {temperature}, Weather Alert Triggered: {alert_triggered['weather']}, Temperature Alert Triggered: {alert_triggered['temperature']}")

    # Check if the dominant weather condition matches the alert condition
    if weather == weather_condition_alert:
        if not alert_triggered['weather']:
            print(f"ALERT: {weather} condition detected in {city}!")
            trigger_alert(city, temperature, weather, alert_type='weather')
            alert_triggered['weather'] = True  # Set weather alert triggered
    else:
        alert_triggered['weather'] = False  # Reset weather alert if condition changes

    # Check if temperature exceeds the threshold
    print(f"DEBUG: Checking temperature against threshold: {temperature} > {temp_threshold} ({'Exceeds' if temperature > temp_threshold else 'Does not exceed'})")
    
    if temperature > temp_threshold:
        if not alert_triggered['temperature']:  # Trigger only if alert hasn't been triggered
            print(f"\nALERT: High temperature detected in {city}!")
            print(f"Temperature: {temperature}°C exceeds {temp_threshold}°C\n")
            trigger_alert(city, temperature, weather, alert_type='temperature')
            alert_triggered['temperature'] = True  # Set temperature alert triggered
    else:
        if alert_triggered['temperature']:  # Only reset if it was previously triggered
            print(f"DEBUG: Temperature is below threshold. Resetting temperature alert for {city}.")
            alert_triggered['temperature'] = False  # Reset temperature alert if below threshold

def trigger_alert(city, temperature, weather, alert_type):
    """Triggers an alert and stores it in a file."""
    print(f"\nALERT: {alert_type.capitalize()} detected in {city}!")
    if alert_type == 'temperature':
        print(f"Temperature: {temperature}°C exceeds the threshold\n")
    else:
        print(f"Weather condition: {weather}!\n")
    
    print("Triggering alert and saving to alerts.json")
    # Store the alert details in a file
    alert_data = {
        'city': city,
        'temperature': temperature,
        'weather': weather,
        'timestamp': time.time()
    }
    save_alert(alert_data)  # This will save the alert.
