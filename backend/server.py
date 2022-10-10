#!/bin/python

from flask import Flask, send_from_directory, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os
import json

from marshmallow import Schema, fields

# Application initialization
# The two arguments after the __name__ are responsible for Flask correct handling of React static files

app = Flask(__name__, static_url_path='', static_folder='./../frontend/build')

CORS(app) #Comment this on deployment

basedir = os.path.abspath(os.path.dirname(__file__))

# Database

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

# Message class/model

class Message(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255), unique=False)

    def __init__(self, message):
        self.message = message

# Message Schema

class MessageSchema(ma.Schema):
    class Meta:
        fields= ('_id', 'message')

class MessageSchema2(Schema):
    _id = fields.Int()
    message = fields.Str()

# Init schema

message_schema = MessageSchema2()
messages_schema = MessageSchema2(many = True) 

# Route setup

@app.route("/")
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Create a message

@app.route("/api/test", methods=['POST'])
def add_message():

    message = request.json['message']

    new_message = Message(message)

    db.session.add(new_message)
    db.session.commit()

    messages = Message.query.all()

    return messages_schema.dump(messages)

#Get all messages

@app.route("/api/test", methods=['GET'])
def get_messages():

    messages = Message.query.all()

    return messages_schema.dump(messages)

# Create a message

@app.route("/api/test", methods=['PUT'])
def update_message():

    newMessage = request.json['message']
    id = request.json['id']

    message = Message.query.get(id)

    message.message = newMessage

    db.session.commit()

    messages = Message.query.all()

    return messages_schema.dump(messages)

# Delete a message

@app.route("/api/test", methods=['DELETE'])
def delete_message():

    id = request.json['id']

    message = Message.query.get(id)

    db.session.delete(message)
    db.session.commit()

    messages = Message.query.all()

    return messages_schema.dump(messages)


# Run server

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)


