from flask import Flask, url_for
from flask_debugtoolbar import DebugToolbarExtension
from knight import Knight

app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = 'marmalade'

DebugToolbarExtension(app)


@app.route('/')
def index():
    page = '<body><h1>'
    knight_list = Knight.get_knight_names()
    for knight_name in knight_list:
        link = url_for('knight_detail', name=knight_name)
        snippet = f'<a href="{link}">{knight_name}</a><br/>'
        page += snippet
    page += "</h1></body>"
    return page

@app.route('/knight/<name>')
def knight_detail(name):
    knight = Knight(name)
    page = '<body>'
    page += f"<h1>{knight.name}</h1>"
    page += f"<h2>{knight.title}</h1>"
    page += f"<h2>{knight.quest}</h1>"
    page += f"<h2>{knight.color}</h1>"
    page += f"<h2>{knight.comment}</h1>"
    home_link = url_for('index')
    page += f"<a href={home_link}>Return to main page</a>"
    page += "</body>"
    return page


if __name__ == '__main__':
    app.run(debug=True)

