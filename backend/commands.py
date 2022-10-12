#!/bin/python

from exts import db
from app import app

def create_all ():
    with app.app_context():
        db.create_all()

create_all()