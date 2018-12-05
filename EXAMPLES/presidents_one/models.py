#!/usr/bin/env python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

print(db.Model.metadata.tables.items())

class President(db.Model):
    __table__ = db.Model.metadata.tables['president']

    def __repr__(self):
        return '<President {} {}>'.format(self.firstname, self.lastname)


# class President(db.Model):
# #    id = db.Column(db.Integer, primary_key=True)
#     termnum = db.Column(db.Integer, primary_key=True)
#     fname = db.Column(db.String(80))
#     lname = db.Column(db.String(80))
#     dbirth = db.Column(db.Date())
#     ddeath = db.Column(db.Date())
#     birthplace = db.Column(db.String(80))
#     birthstate = db.Column(db.String(80))
#     dstart = db.Column(db.Date())
#     dend = db.Column(db.Date())
#     party = db.Column(db.String(32))
#
#     def __repr__(self):
#         return '<President {} {}>'.format(self.fname, self.lastname)
