from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route("/")
def welcome():
    #grab weather data
    weather_data = requests.get("http://api.openweathermap.org/data/2.5/weather?id=2179537&appid=a84b5238c6d1533e7f7baaf8023abca4")
    weather_json = weather_data.json()
    current_temp = weather_json["main"]["feels_like"] - 273.15
    return render_template("home.html", current_temp=current_temp)