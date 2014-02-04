# -*- coding: utf-8 -*-

from flask import render_template, abort
from flask.ext.login import login_required
from precious import *
from precious.models import *


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/projects', methods=["GET", "POST"])
@login_required
def projects():
    return render_template('projects.html', projects=Project.query.order_by('projects.id').all())


@app.route('/start_build/<int:project_id>/<secret_key>')
def start_build(project_id, secret_key):
    return abort(404)
