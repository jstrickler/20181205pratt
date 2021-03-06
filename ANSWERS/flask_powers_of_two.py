#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = 'marmalade'

DebugToolbarExtension(app)

@app.route('/')
def index():
    page = '<body><h1>Powers of two </h1>\n'
    for i in range(32):
        page += f'<b>2^{i} = {2**i}</b><br/></body></html>\n'
    page += "</body>"
    return page

if __name__ == '__main__':
    app.run(debug=True)

