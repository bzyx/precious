from functools import wraps
from flask import current_app
from flask.ext.login import current_user
from precious.models import *
from enum import Enum

ProjectRole = Enum('None', 'View', 'Build', 'Edit', 'Admin')
UserRole = Enum('Admin', 'User')


def need_role(role):
    def decorator(method):
        @wraps(method)
        def decorated_view(*args, **kwargs):
            db = current_app.db
            user = current_user
            project = Project.get(kwargs['project_id'])


            if current_app.login_manager._login_disabled:
                return method(*args, **kwargs)
            elif not current_user.is_authenticated():
                return current_app.login_manager.unauthorized()
            return method(*args, **kwargs)


        return decorated_view
    return decorator


def a(ar):
    def decorator(method):
        @wraps(method)
        def f(*args, **kwargs):
            if(ar == 'cycki'):
                print ar
                return method(*args, **kwargs)
            else:
                print "GOWNO!"
        return f
    return decorator
