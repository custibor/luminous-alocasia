import requests
import json
import pandas as pd
import datetime

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=46.057&longitude=14.5057&hourly=temperature_2m,apparent_temperature,cloudcover,direct_radiation&current_weather=true&past_days=1")

#get weather json data
weather_json = response.json()

#get current time
curr_time = weather_json["current_weather"]["time"]
curr_time = datetime.datetime.strptime(curr_time,"%Y-%m-%dT%H:%M")

#weather data to dataFrame
weather_df = pd.DataFrame(data=weather_json["hourly"])
weather_df["time"] = weather_df["time"].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%dT%H:%M") ) 