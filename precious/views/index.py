# -*- coding: utf-8 -*-

from flask import render_template, flash
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
    try:
        return render_template('workers.html', info=Worker().root.sysinfo())
    except:
        flash("Cannot connect to worker.", "warning")
        return render_template('base.html')


@app.route('/settings', methods=["GET", "POST"])
@login_required
def settings():
    return render_template('base.html')


@app.route('/permissions', methods=["GET", "POST"])
@login_required
def permissions():
    return render_template('base.html')
