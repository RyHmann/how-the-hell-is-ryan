from flask import  (
    Blueprint, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from howsryan.db_sql import get_db
from .auth import login_required
from .support.weather import WeatherData
from .support.status import CurrentStatus
from .support.outlook import Outlook
from .support.nztime import FormatTimeByUTC
from .support.tweet import Tweet

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    existing_status = get_recent_status()
    ryan_status = CurrentStatus()
    ryan_status.current_status = existing_status[1]
    ryan_status.current_reads = existing_status[2]
    ryan_status.current_projects = existing_status[3]
    current_time = FormatTimeByUTC(12)
    current_view = Outlook()
    weather_data = WeatherData()
    recent_tweet = Tweet()
    return render_template(
        "home.html",
        weather_data=weather_data,
        current_time=current_time,
        ryan_status=ryan_status,
        current_view=current_view,
        recent_tweet=recent_tweet
    )


@bp.route('/update', methods=('GET', 'POST'))
@login_required
def update():
    try:
        status = get_recent_status()
        if request.method == 'POST':

            updated_status = request.form['status']
            updated_projects = request.form['projects']
            updated_reads = request.form['reads']

            if status is not None:
                db = get_db()
                db.execute(
                    'UPDATE status SET wellbeing = ?, projects = ?, books = ?',
                    (updated_status, updated_projects, updated_reads)
                )
                db.commit()
                return redirect(url_for('index'))
            else:
                db = get_db()
                db.execute(
                    'INSERT INTO status (wellbeing, projects, books)'
                    ' VALUES (?, ?, ?)',
                    (updated_status, updated_projects, updated_reads)
                )
                db.commit()
                return redirect(url_for('index'))

        ryan_status = CurrentStatus()
        ryan_status.current_status = status[1]
        ryan_status.current_projects = status[2]
        ryan_status.current_reads = status[3]
        return render_template("status.html", ryan_status=ryan_status)
    except IndexError:
        abort(404)


def get_recent_status():
    db = get_db()
    status = db.execute(
        'SELECT *'
        ' FROM status'
        ' ORDER BY id DESC' 
        ' LIMIT 1'
    ).fetchone()
    return status


