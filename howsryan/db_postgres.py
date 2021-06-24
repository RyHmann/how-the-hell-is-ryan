import psycopg2
import click
from flask import current_app, g
from flask.cli import with_appcontext
from werkzeug.security import check_password_hash, generate_password_hash


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(seed_db_command)


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Database initialized')


@click.command('seed-db')
@with_appcontext
def seed_db_command():
    seed_db()
    click.echo('Database Seeded')


def seed_db():
    db = get_db()

    db.execute(
        'INSERT INTO user (username, password)'
        ' VALUES (?, ?)',
        ('ryan', generate_password_hash('admin'))
    )
    db.commit()
    db.execute(
        'INSERT INTO status (wellbeing, projects, books)'
        ' VALUES ("Feeling motivated", "Finishing up The Pantry, updating HowsRyan", "Clean Code by Uncle Bob")'
    )
    db.commit()


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()