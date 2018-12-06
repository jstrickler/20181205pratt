#!/usr/bin/env python
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud_user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'email')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('email')

class UsersResource(Resource):

    def post(self):
        args = parser.parse_args()

        # username = request.get_json('username')
        # email = request.get_json('email')
        username = args['username']
        email = args['email']
        new_user = User(username, email)

        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user)

    def get(self):
        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return jsonify(result.data)


class UserResource(Resource):

    def get(self, id):
        user = User.query.get(id)
        return user_schema.jsonify(user)

    def put(self, id):
        user = User.query.get(id)
        username = request.args['username']
        email = request.json['email']

        user.email = email
        user.username = username

        db.session.commit()
        return user_schema.jsonify(user)

    def delete(self, id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()

        return user_schema.jsonify(user)

api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/user/<int:id>')



if __name__ == '__main__':
    app.run(debug=True)
