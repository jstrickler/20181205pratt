#!/usr/bin/env python
# (c) 2016 John Strickler
#
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('grade')
parser.add_argument('name')

STUDENTS = {}   # faux database

def get_new_student_id():
    if STUDENTS:
        old_max = max(STUDENTS.keys())
        new_id = old_max + 1
    else:
        new_id = 1
    return new_id

def error_on_missing_id(id):
    if id not in STUDENTS:
        abort(404, message="Student {} doesn't exist".format(id))

class StudentList(Resource):
    """
    Resource for lists of students
    """

    def get(self):
        """
        Get list of all students

        :return: List of students
        """
        return STUDENTS

    def post(self):
        """
        Add one student to database

        :return: None
        """
        args = parser.parse_args()
        id = get_new_student_id()
        name = args['name']
        grade = args['grade']
        # update record in DB
        STUDENTS[id] = { 'name': name, 'grade': grade }
        return STUDENTS[id], 201

class Student(Resource):
    """
    Resource for individual student
    """

    def get(self, id):
        """
        Return details for one student

        :param id: The student ID
        :return: Student details as JSON
        """
        error_on_missing_id(id)
        return STUDENTS.get(id), 201

    def put(self, id):
        """
        Update one student record.

        :param id: The student ID
        :return: Confirmation
        """
        error_on_missing_id(id)
        args = parser.parse_args()
        name = args['name']
        grade = args['grade']
        STUDENTS[id] = { 'name': name, 'grade': grade }
        return STUDENTS[id], 200  # send 201 if new record

    def delete(self, id):
        """
        Delete a student from the database

        :param id: The student ID
        :return: None (Status 204)
        """
        error_on_missing_id(id)
        del STUDENTS[id]
        return '', 204

api.add_resource(StudentList, '/api/1/students')
api.add_resource(Student, '/api/1/student/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
