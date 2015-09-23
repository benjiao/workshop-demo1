from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', server_time=current_time)


@app.route('/user')
def user_list():

    users = [
        {'id': 1, 'username': 'benjie', 'name': 'Benjie Jiao', 'is_active': True},
        {'id': 2, 'username': 'luke', 'name': 'Luke Skywalker', 'is_active': True},
        {'id': 3, 'username': 'han', 'name': 'Han Solo', 'is_active': False}
    ]

    return render_template('user.html', users=users)


@app.route('/user/<username>')
def user_profile(username):
    return "<h1>This is the profile page of %s" % username


@app.route('/post/<int:post_id>')
def post_page(user_id):
    return "<h1>This is the profile ID page of %s" % user_id


@app.route('/login', methods=['GET'])
def login_page():
    return "LOGIN!"


@app.route('/login', methods=['POST'])
def login_submit():
    return "LOGIN!"
