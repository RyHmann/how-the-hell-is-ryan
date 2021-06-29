import os
from flask import Flask
from . import auth
from . import index
from howsryan.database import db_session


app = Flask(__name__, instance_relative_config=True)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(auth.bp)
app.register_blueprint(index.bp)
app.add_url_rule('/', endpoint='index')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


