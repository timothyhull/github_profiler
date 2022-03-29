#!/usr/bin/env python3
""" GitHub profiler web application for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library
from os import getenv

# Imports - Third-Party
from dotenv import load_dotenv
from flask import Flask

# Imports - Local

# Load environment variables
load_dotenv()

# Constants
FLASK_DEBUG = getenv('FLASK_DEBUG') or False
FLASK_DEV_ENV = bool(getenv('FLASK_DEV_ENV')) or False
FLASK_HOST = getenv('FLASK_HOST') or 'localhost'
FLASK_PORT = getenv('FLASK_PORT') or 5000

# Flask web application object
app = Flask(__name__)


# Default route
@app.route('/')
def home() -> str:
    """ Default route testing.

        Args:
            None.

        Returns:
            output (str):
                String of text to output in a browser
    """

    output = 'This is a test.'

    return output


# Run the Flask application for development environments only
if FLASK_DEV_ENV is True:
    Flask.run(
        app,
        host=FLASK_HOST,
        port=FLASK_PORT,
        debug=FLASK_DEBUG
    )
