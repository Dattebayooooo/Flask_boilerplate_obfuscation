# -*- coding: utf-8 -*-

from app import app
from flask import render_template

__version__ = '1.0.0'


@app.route('/')
@app.route('/home')
def home():
    return render_template('html/multiplan.html', data="Welcome to page")
