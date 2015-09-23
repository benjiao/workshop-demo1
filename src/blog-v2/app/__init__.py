from flask import Flask
from flask import g

import MySQLdb
import MySQLdb.cursors

from modules import default
from modules import users

app = Flask(__name__)


def connect_db():
    conn = MySQLdb.connect(
        host=app.config.get('MYSQL_HOST'),
        user=app.config.get('MYSQL_USER'),
        passwd=app.config.get('MYSQL_PASSWD'),
        db=app.config.get('MYSQL_DB'),
        cursorclass=MySQLdb.cursors.DictCursor,
        use_unicode=True,
        charset='UTF8'
    )
    return conn


@app.before_request
def before_request():
    """
    Before Request contains scripts to run before executing a request.
    Here, a database connection for the request is created.

    Note: g.db can be used within the route function called
    """
    g.conn = connect_db()
    g.userdb = users.UserDB(conn=g.conn)


@app.teardown_request
def teardown_request(exception):
    """
    Cleanup scripts for every requests.
    Includes closing of database connections.
    """

    conn = getattr(g, 'conn', None)
    userdb = getattr(g, 'userdb', None)

    if userdb is not None:
        userdb = None

    if conn is not None:
        conn.close()

app.register_blueprint(default.mod)
app.register_blueprint(users.mod, url_prefix="/user")
