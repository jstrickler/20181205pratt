#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)  # <1>


@app.route('/')  # <2>
def index():  # <3>
    return '<h1>Hello, Flask world!</h1>' # <4>


if __name__ == '__main__':
    app.run(debug=True) # <5>
