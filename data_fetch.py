import requests
import pandas as pd
from config import API_KEY, BASE_URL

def fetch_weather(city):
    params = {
        "q":city,
        "APPID":API_KEY,
        "units":"metric"    #get data in celcius
    }
    response = requests.get(BASE_URL,params=params)

    if response.status_code==200:
          data = response.json()
          weather_list=data["list"]

          #extract relevant fields
          weather_data=[]
          for entry in weather_list:
               weather_data.append({
                    "date": entry["dt_txt"],
                    "temperature": entry["main"]["temp"],
                    "humidity": entry["main"]["humidity"]
               })
          return pd.DataFrame(weather_data)
    else:
        print(f"Error: {response.status_code} - {response.json()}")
        return None

            