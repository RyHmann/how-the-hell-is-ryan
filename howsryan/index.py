from flask import (
    Blueprint, redirect, render_template, request, url_for, flash
)
from werkzeug.exceptions import abort
from .auth import login_required
from .support.weather import WeatherData
from .support.outlook import Outlook
from .support.nztime import FormatTimeByUTC
from .support.tweet import Tweet
from howsryan.database import db_session
from howsryan.forms import UpdateForm
from howsryan.models import Book, Status, Project

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    current_time = FormatTimeByUTC(12)
    print(current_time.date)
    print(current_time.time)
    current_view = Outlook()
    weather_data = WeatherData()
    recent_tweet = Tweet()
    current_book = get_current_book()
    current_status = get_current_status()
    current_project = get_current_project()
    return render_template(
        "home.html",
        weather_data_vm=weather_data,
        current_time_vm=current_time,
        current_book_vm=current_book,
        current_status_vm=current_status,
        current_project_vm=current_project,
        current_view_vm=current_view,
        recent_tweet_vm=recent_tweet
    )


@bp.route('/update', methods=('GET', 'POST'))
@login_required
def update():
    form = UpdateForm()
    if form.validate_on_submit():
        updated_book = Book(title=form.book_title.data, author=form.book_author.data)
        updated_status = Status(status=form.status.data)
        updated_project = Project(project=form.project.data)
        db_session.add(updated_book)
        db_session.add(updated_status)
        db_session.add(updated_project)
        db_session.commit()
        flash("Update successful")
        return redirect(url_for("index.html"))
    return render_template("update.html", title="Update Ryan", form=form)


def get_current_book():
    return Book.query.order_by('id').first()


def get_current_status():
    return Status.query.order_by('id').first()


def get_current_project():
    return Project.query.order_by('id').first()

