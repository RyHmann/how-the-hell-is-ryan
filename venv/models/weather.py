import requests
import json

class WeatherData:
    def __init__(self, url):
        self.weather_data = requests.get(url).json()
        self.current_temp = self.weather_data["main"]["feels_like"]
        self.description = self.weather_data["weather"][0]["description"]
        self.humidity = self.weather_data["main"]["humidity"]
        self.wind_speed = self.weather_data["wind"]["speed"]
        self.wind_direction = self.weather_data["wind"]["deg"]
        self.current_temp_c = round((self.current_temp - 273.15), 1)
        self.current_temp_f = round((self.current_temp_c * (9/5) + 32), 0)

