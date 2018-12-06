#!/usr/bin/env python
# (c) 2016 John Strickler
#
import requests

STUDENTS = [
    ('Bill Gates', 95),
    ('Linus Torvalds', 99),
    ('Guido van Rossum', 100),
    ('Larry Wall', 92),
    ('Larry Ellison', 88),
]

# collection URL
BASE_URL = "http://localhost:5000/api/1/"
STUDENTS_URL = BASE_URL + "students"
# item URL
STUDENT_URL = BASE_URL + "student"

def main():
    add_records()
    fetch_record(1)
    fetch_record(4)
    update_grade(1, 98)
    delete_record(5)
    fetch_all_records()

def add_records():
    print("ADDING:")
    for student, grade in STUDENTS:
        payload = { 'name': student, 'grade': grade }
        response = requests.post(STUDENTS_URL, data=payload)
        if response.status_code == requests.codes.CREATED:
            print(response.json())
    print()

def update_grade(id, grade):
    print("UPDATING:")
    url = '{}/{}'.format(STUDENT_URL, id)
    old_record = requests.get(url).json()
    payload = { 'name': old_record['name'], 'grade': grade }
    response = requests.put(url, data=payload)
    if response.status_code in (200, 201, 204):
        print(response.json())
    print()

def delete_record(id):
    print("DELETING:")
    url = '{}/{}'.format(STUDENT_URL, id)
    response = requests.delete(url)
    if response.status_code in (200, 201, 204):
        print("deleted\n")


def fetch_all_records():
    print("FETCHING ALL:")
    response = requests.get(STUDENTS_URL)
    if response.status_code == 200:
        records = response.json().items()
        for id, student_data in sorted(records, key=lambda e: int(e[0])):
            print('ID {0}: {1[name]} {1[grade]}'.format(id, student_data))
    print()

def fetch_record(id):
    print("FETCHING RECORD {}:".format(id))
    response = requests.get("{}/{}".format(STUDENT_URL, id))
    if response.status_code == 200:
        data = response.json()
        print('{0[name]} {0[grade]}'.format(data))
    print()

if __name__ == '__main__':
    main()
