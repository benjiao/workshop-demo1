"""
Example 1. This demonstrates a barebones Flask application
"""

import logging
from app import app

app.secret_key = "This is a secret"
app.config.from_object('config.Config')


# Setup Logging
formatter = logging.Formatter(app.config.get('LOG_FORMAT'))
fh = logging.FileHandler(filename=app.config.get('LOG_FILE'))
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
app.logger.addHandler(fh)


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
