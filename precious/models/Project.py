# -*- coding: utf-8 -*-

from precious import db
import jsonpickle


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.Unicode(80), index=True, unique=True)
    description = db.Column(db.UnicodeText)
    conf = db.Column(db.LargeBinary)
    schedule = db.Column(db.LargeBinary)
    history = db.relationship("Build", backref="projects")

    def __init__(self, name, description="", conf=None):
        self.name = name
        self.description = description
        self.conf = conf

    def set_conf(self, conf):
        self.conf = jsonpickle.encode(conf)

    def get_conf(self):
        jsonpickle.decode(self.conf)

    def set_schedule(self, schedule):
        self.schedule = jsonpickle.encode(schedule)

    def get_schedule(self):
        jsonpickle.decode(self.schedule)

    def __repr__(self):
        return '<Project id:%r name:%s>' % (self.id, self.name)
