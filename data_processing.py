import numpy as np

def analyse_weather(df):
    max_temp=np.max(df["temperature"])
    min_temp=np.min(df["temperature"])
    avg_temp=np.mean(df["temperature"])
    avg_humidity=np.mean(df['humidity'])

    return {
        "Max Temperature": max_temp,
        "Min Temperature": min_temp,
        "Average Temperature": avg_temp,
        "Average Humidity": avg_humidity
    }