import json
from datetime import datetime
from flask import request
from flask import redirect
from flask import session
from flask import Blueprint
from flask import render_template
from functools import wraps
from flask import g

from flask import current_app


mod = Blueprint('default', __name__)


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'username' in session:
            return test(*args, **kwargs)
        else:
            current_app.logger.info("Unauthorized access attempted!")
            return redirect('login')
    return wrap


@mod.route('/')
@login_required
def index():

    logged_user = session['username']
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('default/index.html', server_time=current_time, logged_user=logged_user)


@mod.route('/login', methods=['GET'])
def login_page():
    return render_template('default/login.html')


@mod.route('/login', methods=['POST'])
def login_submit():

    username = request.form["username"]
    password = request.form["password"]

    user = g.userdb.getUserByUsername(username=username)

    current_app.logger.info("Someone tried to login! %s", username)
    current_app.logger.info("User: %s", json.dumps(user, indent=4))

    if password != user.get("password"):
        return "Failed!"
    else:
        print username
        session['username'] = user.get("username")
        session['name'] = user.get("name")
        return redirect('/')


@mod.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('login')
