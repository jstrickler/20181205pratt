#!/usr/bin/env python
from flask import Blueprint, render_template

sample = Blueprint('sample', __name__)


@sample.route('/', defaults={'page': 'index'})
@sample.route('/<page>')
def display_page(page):
    return '<h1>Displaying the "{}" page</h1>'.format(page)
