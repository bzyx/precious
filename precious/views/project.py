# -*- coding: utf-8 -*-

from flask import render_template, request, flash, redirect, url_for
from flask.ext.login import login_required
from precious import *
from precious.models import *


@app.route('/project/new', methods=["GET", "POST"])
@login_required
def project_new():
    if request.method == 'POST' and request.form.get("name"):
        name = request.form["name"]
        project = Project(name)
        db.session.add(project)
        db.session.commit()
        flash("Project %s deleted." % (project.name), "success")
        return redirect(url_for("projects"))
    return render_template("project/new.html")


@app.route('/project/<int:project_id>')
@login_required
def project_history(project_id):
    project = Project.query.get(project_id)
    return "history %r" % (project_id)


@app.route('/project/<int:project_id>/edit', methods=["GET", "POST"])
@login_required
def project_edit(project_id):
    project = Project.query.get(project_id)
    return "edit %r" % (project_id)


@app.route('/project/<int:project_id>/build')
@login_required
def project_build(project_id):
    project = Project.query.get(project_id)
    if request.method == 'POST':
        flash("Build of %s started." % (project.name), "info")
        # TODO: build here
        return redirect(url_for("projects"))
    return render_template("confirm.html",
                           question="Build project?",
                           message=project.name,
                           back=url_for("projects"),
                           type="info")


@app.route('/project/<int:project_id>/delete', methods=["GET", "POST"])
@login_required
def project_delete(project_id):
    project = Project.query.get(project_id)
    if request.method == 'POST':
        flash("Project %s deleted." % (project.name), "warning")
        db.session.delete(project)
        db.session.commit()
        return redirect(url_for("projects"))
    return render_template("confirm.html",
                           question="Delete project?",
                           message=project.name,
                           back=url_for("projects"),
                           type="warning")
