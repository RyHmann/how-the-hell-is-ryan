from flask import Flask, render_template, url_for, request, abort, redirect
from models.weather import WeatherData
from datetime import datetime
from models.outlook import Outlook
from models.ryanstatus import RyanStatus
import models.howsryanda as data_access


app = Flask(__name__)


@app.route("/")
def welcome():
    current_time = datetime.now().strftime("%I:%M%p")
    current_view = Outlook()
    weather_data = WeatherData()
    ryan_status = RyanStatus()
    return render_template("home.html", weather_data=weather_data, current_time=current_time, current_view=current_view, ryan_status=ryan_status)


@app.route("/set_status", methods=["GET", "POST"])
def set_status():
    try:
        if request.method == "POST":
            current_status = {"message": request.form['status']}
            data_access.update_status(current_status)
            return redirect(url_for('welcome'))

        else:
                return render_template("status.html")
    except IndexError:
        abort(404)
