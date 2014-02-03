# -*- coding: utf-8 -*-

from flask import flash, render_template, redirect
from flask.ext.login import login_required, logout_user, login_user
from precious import *
from precious.models import *

@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		login_user(user)
		flash("Logged in successfully.")
		return redirect(flask.url_for("index"))
	return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect("http://onet.pl")