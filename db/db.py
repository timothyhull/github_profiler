#!/usr/bin/env python3
""" GitHub profiler database for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library
from os import getenv
from os.path import abspath, dirname, join
from pathlib import Path
from sqlite3 import connect

# Imports - Third-Party
from dotenv import load_dotenv

# Imports - Local

# Load environment variables
load_dotenv()

# Constants
CURRENT_DIR = Path(dirname(__file__))
CURRENT_DIR_ABSPATH = abspath(CURRENT_DIR)
DB_URL = getenv(key='DB_URL', default=None)
DB_NAME = getenv(key='DB_NAME', default=None)
DB_TEST_NAME = getenv(key='TEST_DB_NAME', default=None)

# Create a sqllite3 database connection, and database if none exists
conn = connect(
    database=join(CURRENT_DIR_ABSPATH, DB_NAME)
)

# Functions
