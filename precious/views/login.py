# -*- coding: utf-8 -*-

from flask import flash, render_template, redirect, url_for, request
from flask.ext.login import login_required, logout_user, login_user
from precious import *
from precious.models import *
import pam


def get_user(username, provider, password=None):
    if provider == "Local":
        u = User.query.filter_by(name=username, provider=provider).first()
        if u is not None and u.check_password(password):
            return u
    elif provider == "PAM":
        if pam.authenticate(username, password):
            u = User.query.filter_by(name=username, provider=provider).first()
            if u is None:
                u = User(name=username, provider=provider)
                db.session.add(u)
                db.session.commit()
            return u
    return None


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        user = get_user(request.form['username'], "Local", request.form['password']) or get_user(request.form['username'], "PAM", request.form['password'])
        if user is not None:
            login_user(user)
            flash("Logged in successfully.", "success")
            return redirect(url_for("index"))
        else:
            flash("Wrong username of password.", "danger")
    return render_template("login.html")


# """Velruse login page"""
# @app.route('/logged_in', methods=['POST'])
# def login_callback():
#     token = request.form['token']
#     payload = {'format': 'json', 'token': token}
#     response = requests.get(request.host_url + 'velruse/auth_info', params=payload)
#     #TODO parse response here
#     return redirect(url_for("index"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
