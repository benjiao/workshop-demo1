"""
Example 1. This demonstrates a barebones Flask application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Welcome to Flask!</h1>"


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
