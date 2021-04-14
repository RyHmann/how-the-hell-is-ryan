from flask import Flask, render_template, url_for, request, abort, redirect
from .support.weather import WeatherData
from .support.outlook import Outlook
from .support.ryanstatus import RyanStatus
from .support.nztime import FormatTimeByUTC
from .support.howsryanda import update_status


app = Flask(__name__)


@app.route("/")
def welcome():
    current_time = FormatTimeByUTC(12)
    current_view = Outlook()
    weather_data = WeatherData()
    ryan_status = RyanStatus()
    return render_template("home.html", weather_data=weather_data, current_time=current_time, current_view=current_view, ryan_status=ryan_status)


@app.route("/set_status", methods=["GET", "POST"])
def set_status():
    try:
        if request.method == "POST":
            current_status = {"message": request.form['status'], "projects": request.form["projects"], "current_reads": request.form["reads"]}
            update_status(current_status)
            return redirect(url_for('welcome'))

        else:
            ryan_status = RyanStatus()
            return render_template("status.html", ryan_status=ryan_status)
    except IndexError:
        abort(404)
