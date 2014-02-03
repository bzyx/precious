# -*- coding: utf-8 -*-

from flask import flash, render_template
from precious import *
from precious.models import *

@app.route('/')
def index():
    return render_template('base.html', projects=["precious", "sok9001", "wtf2014"])
