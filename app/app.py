#!/usr/bin/env python3
""" GitHub profiler web application for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library

# Imports - Third-Party
from flask import Flask

# Imports - Local

# Flask web application object
app = Flask(__name__)


# Default route
@app.route('/')
def default_route() -> str:
    """ Default route testing.

        Args:
            None.

        Returns:
            output (str):
                String of text to output in a browser
    """

    output = 'This is a test.'

    return output
