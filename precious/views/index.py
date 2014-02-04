# -*- coding: utf-8 -*-

from flask import request, render_template, flash
from flask.ext.login import login_required
from precious import *
from precious.utils import get_config_file_path, parse_config
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
    config = parse_config()
    sections = []
    for section in config.sections():
        sections.append((section, config.items(section)))

    if request.method == 'POST':
        for key, value in request.form.iteritems():
            s = [s for s in config.sections() if key.startswith("[{}]".format(s))][0]
            config.set(s, key.replace("[{}]".format(s), ""), value)
        try:
            config.write(open(get_config_file_path(), 'w'))
            flash("Saved.", "success")
        except:
            flash("Error writing file.", "danger")

    return render_template('settings.html', sections=sections)
