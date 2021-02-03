from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import logging

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.config['CORS_HEADERS'] = ['Content-Type', 'Authorization']

    db.init_app(app)
    flask_bcrypt.init_app(app)
    CORS(app, headers=['Authorization', 'Content-Type'], methods=['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']) 
    logging.getLogger('flask_cors').level = logging.DEBUG

    return app