#!/usr/bin/env python
# (c) 2016 John Strickler
#
import requests

API_URL = "http://localhost:5000/api/1.0/Cheese"

response = requests.get(API_URL)

if response.status_code == requests.codes.OK:
    print("RAW RESPONSE:", response.content.decode())
    print()
    data = response.json()
    print(data)  # convert json string to Python data structure

# print(data.items())
