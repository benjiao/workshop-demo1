from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello workshop!"


@app.route('/user')
def user_list():
    return "<h1>This is the user page</h1>"


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
