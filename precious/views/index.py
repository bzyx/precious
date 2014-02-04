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


@app.route('/workers', methods=["GET", "POST"])
@login_required
def workers():
    return render_template('workers.html', info=worker.root.sysinfo())


@app.route('/settings', methods=["GET", "POST"])
@login_required
def settings():
    return render_template('base.html')
