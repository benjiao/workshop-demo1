from flask import Flask
from flask import render_template
from datetime import datetime


from flask import session
from flask import request
from functools import wraps
from flask import redirect

app = Flask(__name__)


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'username' in session:
            return test(*args, **kwargs)
        else:
            app.logger.info("Unauthorized access attempted!")
            return redirect('login')
    return wrap


@app.route('/')
@login_required
def index():
    logged_user = session['username']
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', server_time=current_time, logged_user=logged_user)


@app.route('/user')
@login_required
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
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_submit():
    username = request.form["username"]
    password = request.form["password"]

    app.logger.info("Someone tried to login! %s", username)

    if password != "password":
        return "Failed!"
    else:
        print username
        session['username'] = "benjie"
        return "Success! Logged in as %s" % username


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('login')
