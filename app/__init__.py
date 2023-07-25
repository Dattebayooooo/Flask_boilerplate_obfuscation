# -*- coding: utf-8 -*-

import os
from os.path import dirname as up
from flask import Flask, send_from_directory
from app import models, routes


__version__ = '1.0.0'
application_dir = up(up(__file__))


app = Flask(__name__, 
            template_folder=os.path.join( application_dir, 'frontend', 'templates')
            )

app.config['CUSTOM_STATIC_PATH'] = app.static_folder + '/../../frontend/static'
@app.route('/cdn/<path:filename>')
def custom_static(filename):
    "Helps to import the static folder outside of app"
    return send_from_directory(app.config['CUSTOM_STATIC_PATH'], filename)


