from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import uuid

from datetime import datetime

# init here to make use of db in whole project
db = SQLAlchemy()
ma = Marshmallow()

# configuration
DEBUG = True


def create_app():
    app = Flask(__name__)

    app.config.from_object(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../tmp/test.db'
    app.config['CORS_HEADERS'] = 'Content-Type'

    db.init_app(app)
    ma.init_app(app)

    # blueprint for api routes
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    # blueprint for auth routes
    #from .auth import auth as auth_blueprint
    #app.register_blueprint(auth_blueprint)

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    return app