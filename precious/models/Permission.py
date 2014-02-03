# -*- coding: utf-8 -*-

from precious import db
from precious.utils import ProjectRole


class Permission(db.Model):
    __tablename__ = 'permissions'

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    role = db.Column(db.SmallInteger, default=ProjectRole.Build)
