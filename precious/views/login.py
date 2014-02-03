# -*- coding: utf-8 -*-

from flask import flash, render_template, redirect, url_for
from flask.ext.login import login_required, logout_user, login_user
from precious import *
from precious.models import *

@app.route("/login", methods=["GET", "POST"])
def login():
    #if form.validate_on_submit():
    #    login_user(user)
    #    flash("Logged in successfully.")
    #    return redirect(url_for("index"))
    return render_template("login.html")

@app.route('/logged_in', methods=['POST'])
def login_callback():
    token = request.form['token']
    payload = {'format': 'json', 'token': token}
    response = requests.get(request.host_url + 'velruse/auth_info', params=payload)

    #TODO parse response here

    return redirect(url_for("index"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
