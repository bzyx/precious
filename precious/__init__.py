# -*- coding: utf-8 -*-

import os
import logging
import logging.config

import pam

from flask import Flask
import flask.ext.login as flask_login
from flask.ext.sqlalchemy import SQLAlchemy

from precious.utils import get_logger_config_file_path, parse_config

__all__ = ['config', 'app', 'db', 'logger', 'login_manager']

# Application config
config = parse_config()

# Flask
app = Flask(__name__)
app.config.update(
    DEBUG=config.getboolean('webserver', 'debug'),
    SECRET_KEY=config.get('webserver', 'sekret_key'),
    SQLALCHEMY_DATABASE_URI=config.get('database', 'uri').replace('$HOME', os.path.expanduser('~'))
)

# Flask-SQLAlchemy
db = SQLAlchemy(app)

# Logger
logging.config.fileConfig(get_logger_config_file_path())
logger = logging.getLogger("server")

# Flask-Login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

from precious import views, models

@login_manager.user_loader
def load_user(userid):
    return None
