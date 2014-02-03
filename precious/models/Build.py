# -*- coding: utf-8 -*-

from precious import db
from datetime import datetime


class Build(db.Model):
    __tablename__ = 'builds'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    date = db.Column(db.DateTime)
    revision = db.Column(db.LargeBinary)
    stdout = db.Column(db.UnicodeText)
    success = db.Column(db.Boolean)

    def __init__(self, project_id, revision, stdout=u"", success=True, date=datetime.now()):
        self.project_id = project_id
        self.date = date
        self.revision = revision
        self.stdout = stdout
        self.success = success

    def __repr__(self):
        return '<Build id:%r project_id:%r>' % (self.id, self.project_id)
