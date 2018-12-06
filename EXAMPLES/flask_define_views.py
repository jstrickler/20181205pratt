#!/usr/bin/env python
# (c)2015 John Strickler

from flask import Flask

from president import President

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    """Default page for this site"""
    return '''<h1>Hello, Flask world!</h1>
    <h2>try .../president/#</h1>
    '''


@app.route('/president/<int:termnum>/', methods=['GET','POST'])
def president_by_term(termnum):
    """Retrieve president information for a specified term number"""
    if 0 < termnum < 46:
        return format_html_for_president(termnum)
    else:
        html_content = '<h2>Sorry,  {} is not a valid term number</h2>'.format(termnum)
    return html_content

@app.route('/president/<last_name>/', methods=['GET','POST'])
def president_by_last_name(last_name):
    """Retrieve president information for a specified last name;
        May return info for more than one president
    """
    html_content = ''
    for i in range(1, 45):
        p = President(i)
        if p.last_name.lower() == last_name.lower():
            html_content += format_html_for_president(i)

    if html_content:
        return html_content
    else:
        return '<body><h2>Sorry,  {} not found</h2></body>'.format(last_name)

def format_html_for_president(term_num):
    """Return HTML for one president"""
    p = President(term_num)
    return  '''<body>
    <h1>{}: {} {}</h1>
    <h2>Born in: {}</h2>
    <h2>Lived: {} to {}</h2>
    <h2>Party: {}</h2>
    </body>'''.format(
        term_num, p.first_name, p.last_name, p.birth_state, p.birth_date,
        p.death_date, p.party
    )


if __name__ == '__main__':
    app.run(debug=True)
