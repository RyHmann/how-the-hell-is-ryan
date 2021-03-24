from flask import Flask, render_template
import requests
import json
from models.weather import WeatherData
from datetime import datetime



app = Flask(__name__)


@app.route("/")
def welcome():
    now = datetime.now()
    current_time = now.strftime("%I:%M%p")
    weather_data = WeatherData("http://api.openweathermap.org/data/2.5/weather?id=2179537&appid=a84b5238c6d1533e7f7baaf8023abca4")
    return render_template("home.html", current_temp_c=weather_data.current_temp_c, current_temp_f = weather_data.current_temp_f, current_description=weather_data.description, current_time=current_time)

