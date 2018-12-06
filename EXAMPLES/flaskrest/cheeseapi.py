#!/usr/bin/env python
# (c) 2016 John Strickler
#
import random
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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

class Cheese(Resource):
    """
    The Cheese resource
    """
    def get(self):
        """
        Retrieve a random cheesery and cheese.

        :return: Tuple of cheesery and cheese as JSON
        """
        cheese_maker = random.choice(cheese_makers)
        cheese = CHEESES.get(cheese_maker)
        return {cheese_maker: cheese}

api.add_resource(Cheese, '/api/1.0/Cheese')

if __name__ == '__main__':
    app.run(debug=True)
