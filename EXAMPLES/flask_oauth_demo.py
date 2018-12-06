#!/usr/bin/env python
import os
import requests

from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, session
from flask_oauth_github import CLIENT_ID, CLIENT_SECRET

SECRET_KEY = os.urandom(24)

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template(
        'oauth_demo_main.html', client_id=CLIENT_ID
    )


@app.route('/callback')
def callback():
    session_code = request.args.get('code')

    # ask for an access_token
    response = requests.post(
        'https://github.com/login/oauth/access_token',
        data={
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'code': session_code,
        },
        headers={
            'accept': 'application/json',
        }
    )

    if response.status_code == requests.codes.OK:
        session['access_token'] = response.json()['access_token']
    else:
        session['access_token'] = 'FOOOOOOOFEEEEEEE'

    return render_template(
        'oauth_demo_callback.html',
        access_token=session['access_token'],
    )


@app.route('/listfiles')
def list_files():
    file_list = get_file_list()

    return render_template(
        'oauth_demo_list.html',
        file_list=file_list,
    )


def get_api(url):
    return requests.get(
        url,
        params={
            'access_token': session['access_token'],
        },
    ).json()


def get_file_list():
    # fetch the reference object
    ref_json = get_api('https://api.github.com/repos/jstrickler/funnytexts/git/refs/heads/master')
    commit_url = ref_json['object']['url']

    # fetch the commit object
    commit_json = get_api(commit_url)
    tree_url = commit_json['tree']['url']

    # fetch the tree object
    tree_json = get_api(tree_url)

    # get the file names from the the tree object
    file_list = []
    for file_data in tree_json['tree']:
        file_list.append(file_data['path'])

    return file_list


if __name__ == '__main__':
    app.secret_key = SECRET_KEY
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
