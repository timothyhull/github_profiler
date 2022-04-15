#!/usr/bin/env python3
""" GitHub profiler database for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library
from os import getenv

# Imports - Third-Party
# from dotenv import load_dotenv
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# Imports - Local
import sqlite3

# Load environment variables
# from db_models import BASE, Repos

# Constants
AUTO_FLUSH = True
DB_LOGGING = True
DB_URL = getenv(key='DB_URL', default=None)

# SQLite3 Database
sqlite_db = sqlite3.connect(
    database='github_profiler.db'
)

# Functions
