#!/usr/bin/env python
# (c) 2016 John Strickler
#
import requests

API_URL = "http://localhost:5000/api/1.0/Cheese"

response = requests.get(API_URL, auth=('bob', 'l0lz'))
print("Status code:", response.status_code)
if response.status_code == requests.codes.OK:
    print(response.json())
