import json
import os

def save_daily_summary(daily_summary, filename='daily_summary.json'):
    """Saves the daily weather summary to a JSON file."""
    # Check if the file exists, if not, create it
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
    else:
        data = []

    # Add the new summary to the existing data
    data.append(daily_summary)

    # Write the updated data back to the file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def load_daily_summaries(filename='daily_summary.json'):
    """Loads the daily weather summaries from the JSON file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return data  # Make sure this is a list of summaries
    return []


def save_alert(alert_data, filename='alerts.json'):
    """Saves the alert details to a JSON file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
    else:
        data = []
    
    # Add the new alert to the list
    data.append(alert_data)
    
    # Write the updated data back to the file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
