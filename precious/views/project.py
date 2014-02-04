# -*- coding: utf-8 -*-

from copy import deepcopy
from flask import render_template, request, flash, redirect, url_for
from flask.ext.login import login_required
from precious import *
from precious.models import *
from precious.worker import ProjectManagment
from precious.plugins import FormElements


@app.route('/project/new', methods=["GET", "POST"])
@login_required
def project_new():
    if request.method == 'POST' and request.form.get("name"):
        project = Project(request.form["name"], request.form["description"])
        db.session.add(project)
        db.session.commit()
        flash("Project %s deleted." % (project.name), "success")
        return redirect(url_for("projects"))
    return render_template("project/new.html")


@app.route('/project/<int:project_id>')
@login_required
def project_history(project_id):
    project = Project.query.get(project_id)
    if not project.history:
        flash("%s has no builds." % (project.name), "info")
        return redirect(url_for("projects"))
    return render_template("project/history.html", project=project)


@app.route('/project/<int:project_id>/edit', methods=["GET", "POST"])
@login_required
def project_edit(project_id):
    project = Project.query.get(project_id)
    step_plugins = plugins.get_build_steps()

    if request.method == 'POST':
        bs = deepcopy(project.build_steps)

        if request.form.get("project_name"):
            project.name = request.form.get("project_name")
        else:
            flash("Project name is too short", "warning")

        project.description = request.form.get("project_description")

        for i in range(len(bs)):
            args = bs[i].get_args()
            for key, value in bs[i].description()[1].iteritems():
                if value[1] == FormElements.Checkbox:
                    args[key] = True if request.form.get("step%r_%s" % (i+1, key)) is not None else False
                else:
                    args[key] = request.form.get("step%r_%s" % (i+1, key))
            bs[i].set_args(**args)
            print bs[i].get_args()

        project.build_steps = bs
        db.session.add(project)
        db.session.commit()

    return render_template("project/edit.html", project=project, plugins=step_plugins)


@app.route('/project/<int:project_id>/step_add/<step_name>')
@login_required
def project_step_add(project_id, step_name):
    step_plugins = plugins.get_build_steps()
    project = Project.query.get(project_id)

    project.build_step_append(step_plugins[step_name]())

    db.session.add(project)
    db.session.commit()
    return redirect(url_for("project_edit", project_id=project.id))


@app.route('/project/<int:project_id>/step_del/<int:step_index>')
@login_required
def project_step_del(project_id, step_index):
    project = Project.query.get(project_id)

    project.build_step_remove(step_index-1)

    db.session.add(project)
    db.session.commit()
    return redirect(url_for("project_edit", project_id=project.id))


@app.route('/project/<int:project_id>/step_move_up/<int:step_index>')
@login_required
def project_step_move_up(project_id, step_index):
    project = Project.query.get(project_id)

    project.build_step_move_up(step_index-1)

    db.session.add(project)
    db.session.commit()
    return redirect(url_for("project_edit", project_id=project.id))


@app.route('/project/<int:project_id>/step_move_down/<int:step_index>')
@login_required
def project_step_move_down(project_id, step_index):
    project = Project.query.get(project_id)

    project.build_step_move_down(step_index-1)

    db.session.add(project)
    db.session.commit()
    return redirect(url_for("project_edit", project_id=project.id))


@app.route('/project/<int:project_id>/build', methods=["GET", "POST"])
@login_required
def project_build(project_id):
    project = Project.query.get(project_id)
    if request.method == 'POST':
        try:
            pm = ProjectManagment(project)
            pm.start_project()
            pm.build_project()
            flash("Build of %s started." % (project.name), "info")
        except:
            flash("Cannot connect to worker.", "warning")
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
                           back=url_for("project_edit", project_id=project.id),
                           type="danger")
