#!/usr/bin/env python
from flask import Flask
from flask_sample_blueprint import sample

app = Flask(__name__)
app.register_blueprint(sample)


if __name__ == '__main__':
    app.run(debug=True)
