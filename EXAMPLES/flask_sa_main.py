#!/usr/bin/env python
from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sa_models import db, President

app = Flask(__name__)

@app.route('/president/<int:term>')
def add_pres(term):
    # get user input here from form or API or wherever....
    president = President('Abraham', 'Lincoln', 'IL')
    db.session.add(president)
    db.session.commit()

    return '''<h1>Added.</h1''', 201


if __name__ == '__main__':
    app.run(debug=True)
