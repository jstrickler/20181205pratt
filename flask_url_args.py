from flask import Flask, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = 'marmalade'

DebugToolbarExtension(app)


@app.route('/')
def index():
    page = '<body><h1>Query strings demo</h1>'
    for query_name, query_value in request.args.items():
        page += f"{query_name}: {query_value}<br/>"
    page += "<hr/>"
    for thing in dir(request):
        page += f"{thing}<br/>"
    page += "</body>"
    return page



if __name__ == '__main__':
    app.run(debug=True)

