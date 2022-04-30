#!/usr/bin/env python3
""" GitHub profiler web application for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library

# Imports - Third-Party
from flask import Flask, url_for

# Imports - Local

# Flask web application object
app = Flask(
    import_name=(__name__)
)


# Default route
@app.route(
    rule='/'
)
def index() -> str:
    """ Display all repositories.

        Args:
            None.

        Returns:
            TODO
    """
    return 'index'


# Testing the url_for method, which will automatically escape special chars
# https://flask.palletsprojects.com/en/2.1.x/quickstart/#url-building
with app.test_request_context():
    print(url_for('index'))
