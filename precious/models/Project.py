# -*- coding: utf-8 -*-

from precious import db
from precious.utils import ProjectRole


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, index=True, unique=True)
    default_role = db.Column(db.SmallInteger, default=ProjectRole.None)
    description = db.Column(db.String)
    conf = db.Column(db.String)
