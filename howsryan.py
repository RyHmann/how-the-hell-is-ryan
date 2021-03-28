from flask import Flask, render_template, url_for
from models.weather import WeatherData
from datetime import datetime
from models.outlook import Outlook
from models.ryanstatus import RyanStatus


app = Flask(__name__)


@app.route("/")
def welcome():
    current_time = datetime.now().strftime("%I:%M%p")
    current_view = Outlook()
    weather_data = WeatherData()
    ryan_status = RyanStatus()
    return render_template("home.html", weather_data=weather_data, current_time=current_time, current_view=current_view, ryan_status=ryan_status)

