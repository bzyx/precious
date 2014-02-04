# -*- coding: utf-8 -*-

import logging
import logging.config

import rpyc

from flask import Flask
import flask.ext.login as flask_login
from flask.ext.sqlalchemy import SQLAlchemy

from precious.utils import get_logger_config_file_path, parse_config, get_db_uri, get_worker_port, get_worker_host


__all__ = ['config', 'app', 'db', 'logger', 'login_manager', 'Worker']

# Application config
config = parse_config()

# Flask
app = Flask(__name__)
app.config.update(
    DEBUG=config.getboolean('webserver', 'debug'),
    SECRET_KEY=config.get('webserver', 'sekret_key'),
    SQLALCHEMY_DATABASE_URI=get_db_uri()
)

# Flask-SQLAlchemy
db = SQLAlchemy(app)

# Logger
logging.config.fileConfig(get_logger_config_file_path())
logger = logging.getLogger("server")

# Flask-Login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"


class Worker(object):
    _instance = None

    def __new__(cls):
        if not cls._instance or not not cls._instance.root:
            try:
                cls._instance = rpyc.connect(get_worker_host(), get_worker_port())
            except:
                cls._instance = None
        return cls._instance


from precious import views, models


@login_manager.user_loader
def load_user(userid):
    return models.User.query.get(userid)
