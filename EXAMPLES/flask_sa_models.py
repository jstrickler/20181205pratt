#!/usr/bin/env python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../DATA/presidents.db'
db = SQLAlchemy(app)


class President(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    birthstate = db.Column(db.String(2))

    def __init__(self, firstname, lastname, state):
        self.firstname = firstname
        self.lastname = lastname
        self.birthstate = state

    def __repr__(self):
        return '<President {} {}>'.format(self.firstname, self.lastname)


def create_db():
    '''Warning! Only run this once for production!!!!'''
    db.create_all()


if __name__ == '__main__':
    create_db()
