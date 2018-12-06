#!/usr/bin/env python
# (c) 2016 John Strickler
#
import random
from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)
api = Api(app)

USERS = {
    'mary': '$3cr3t',
    'bob': 'l0lz',
}

CHEESES = {
    "Bel Gioioso Cheese": "Aged Provolone",
    "Bleu Mont Dairy": "Bandaged Cheddar",
    "Capri Cheesery ": "St. Pauline",
    "Carr Valley": "Cocoa Cardona",
    "Cesar's Cheese": "Queso Oaxaca",
    "Cedar Grove": "Butterkase",
    "Chalet Cheese Cooperative": "Baby Swiss",
    "Crave Brothers Farmstead Cheese": "Petit Frere",
    "Edelweiss Creamery": "Grass Based Emmentaler",
    "Emmi Roth USA": "Grand Cru Gruyere Surchoix",
    "Fantome Farm": "Fleuri Noir",
    "Hennings Cheese": "Peppercorn Cheddar",
    "Hidden Springs Creamery": "Driftless",
    "Hollands Family Cheese": "Foenegreek Gouda",
    "Hook's Cheese": "10-Year Cheddar",
    "Klondike Cheese": "Feta",
    "LaClare Farm": "Evalon",
    "Maple Leaf Cheese Cooperative": "English Hollow",
    "Meister Cheese ": "Eagle Cave Reserve ",
    "Nordic Creamery": "Capriko",
    "Roelli Cheese": "Dunbarton  Blue",
    "Sartori": "SarVecchio",
    "Saxon Homestead Creamery": "Big Ed's",
    "Seymour Dairy": "Ader Kase Reserve",
    "Uplands Cheese": "Pleasant Ridge Reserve",
    "Widmer's Cheese Cellars": "Brick",
}
cheese_makers = list(CHEESES.keys())

@auth.verify_password
def verify_password(user, password):
    if USERS.get(user) == password:
        return True
    else:
        return False

class Cheese(Resource):
    decorators = [auth.login_required]

    def get(self):
        cheese_maker = random.choice(cheese_makers)
        cheese = CHEESES.get(cheese_maker)
        return {cheese_maker: cheese}

api.add_resource(Cheese, '/api/1.0/Cheese')

if __name__ == '__main__':
    app.run(debug=True)
