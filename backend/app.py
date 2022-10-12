#!/bin/python

from flask import Flask
from flask_cors import CORS
import os
import config

from exts import db

from views import routes

# Application initialization
# The two arguments after the __name__ are responsible for Flask correct handling of React static files
app = Flask(__name__, static_url_path='', static_folder=config.static_folder_path)

app.register_blueprint(routes)

basedir = os.path.abspath(os.path.dirname(__file__))

# Production DB URI (comment while on devloppement)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database/db.sqlite'

# Developpement DB URI (comment while on production)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#Comment this on deployment
CORS(app) 
 
# Run server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)