import requests
from datetime import datetime, timezone, timedelta

'''
A class that populates itself with weather data from openweathermap.org's api
'''

class WeatherData:
    def __init__(self):
        self.url = "http://api.openweathermap.org/data/2.5/weather?id=2179537&appid=a84b5238c6d1533e7f7baaf8023abca4"
        self.weather_data = requests.get(self.url).json()
        self.current_temp = self.weather_data["main"]["feels_like"]
        self.description = self.weather_data["weather"][0]["description"]
        self.humidity = self.weather_data["main"]["humidity"]
        self.wind_speed = self.weather_data["wind"]["speed"]
        self.wind_direction = self.weather_data["wind"]["deg"]
        self.current_temp_c = round((self.current_temp - 273.15), 1)
        self.current_temp_f = round((self.current_temp_c * (9/5) + 32), 0)

    def get_ordinal_date_suffix(day):
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
            return suffix
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
            return suffix

