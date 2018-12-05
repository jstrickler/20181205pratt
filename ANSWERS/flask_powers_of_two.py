#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    page = '<h1>Powers of two </h1>\n'
    for i in range(32):
        page += f'<b>2^{i} = {2**i}</b><br/>\n'
    return page

if __name__ == '__main__':
    app.run(debug=True)
z`
