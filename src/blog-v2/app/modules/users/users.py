from flask import request
from flask import redirect
from flask import session
from flask import Blueprint
from flask import render_template
from flask import url_for
from flask import flash
from functools import wraps
from flask import g

from flask import current_app


mod = Blueprint('users', __name__)


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
def user_list():
    users = g.userdb.getUsers()
    return render_template('users/user.html', users=users)


@mod.route('/<username>')
def user_profile(username):
    user = g.userdb.getUserByUsername(username)
    return render_template('users/profile.html', user=user)


@mod.route('/', methods=['POST'])
def create_user():
    username = request.form["username"]
    name = request.form["name"]
    password = request.form["password"]

    results = g.userdb.createUser(
        username=username,
        name=name,
        password=password)

    if results is True:
        flash('User creation successful', 'create_user_success')
        return redirect(url_for('.user_list'))
    else:
        session["message_create_user"] = "User creation failed!"
        return redirect(url_for('.user_list'))
