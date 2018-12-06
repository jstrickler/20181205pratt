#!/usr/bin/env python

from flask import Flask, make_response
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.debug = False

app.config['SECRET_KEY'] = 'marmalade'

DebugToolbarExtension(app)

@app.route('/')
def index():
    return '''
        <body><h1>HTTP Responses</h1>
        <h2>Try:</h2>
        <h2>/str/</h2>
        <h2>/obj/</h2>
        <h2>/tuple/</h2></body>
    '''


@app.route('/str/')
def return_str():
    return "<body><h1>String</h1></body>"


@app.route('/obj/')
def return_obj():
    response = make_response(
        ('<body><h1>Response object</h1></body>', 200, {'Content-type': 'text/html'})
    )
    return response


@app.route('/tuple/')
def return_tuple():
    return "", 403, {'Content-type': 'text/html'}


if __name__ == '__main__':
    app.run(debug=True)
