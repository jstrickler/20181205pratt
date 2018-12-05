#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)  # <1>


@app.route('/')  # <2>  DECORATOR
def index():  # <3> # view function
    return '<h1>Hello, Pratt & Whitney Flask world!</h1>' # <4>

@app.route('/koala/nesting/pictures/hires')
@app.route('/wombat')  # <2>  DECORATOR
def wombats():  # view function
    name = 'Bob'
    return f'I like wombats<br/> and koalas! My name is {name}' # <4>

# index = app.route('/')(index)

if __name__ == '__main__':
    app.run(debug=True, port=5001) # <5>
