#!/bin/python

#This file is required for the wsgi server setup

from server import app

if __name__ == "__main__":
    app.run()