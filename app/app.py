#!/usr/bin/env python3
""" GitHub profiler web application for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library

# Imports - Third-Party
from flask import Flask
from markupsafe import escape

# Imports - Local

# Flask web application object
app = Flask(__name__)


# Default route
@app.route(rule='/')
def home() -> str:
    """ Default route.

        Args:
            None.

        Returns:
            output (str):
                String of text to output in a browser
    """

    output = 'This is a test.'

    return output


# The trailing / in the rule argument auto-redirects requests with no /
@app.route(rule='/<name>/')
def hello(
    name: str
) -> str:
    """ Hello, "Name" route.

        Args:
            None.

        Returns:
            output (str):
                String of text to output in a browser
    """

    # markupsafe.escape causes any 'name' variable input to render as text
    # This prevents injection attacks
    # https://flask.palletsprojects.com/en/2.1.x/quickstart/#html-escaping
    output = f'Hello, {escape(name)}.'

    return output
