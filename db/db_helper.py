#!/usr/bin/env python3
""" GitHub profiler database for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library
from os import getenv
from os.path import abspath, dirname, join
from pathlib import Path
from sqlite3 import connect
from sys import argv

# Imports - Third-Party
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session as SessionObject
from sqlalchemy.orm import sessionmaker

# Imports - Local
from db.db_models import BASE

# Load environment variables
load_dotenv()

# Constants
CURRENT_DIR = Path(dirname(__file__))
CURRENT_DIR_ABSPATH = abspath(CURRENT_DIR)
DB_AUTOFLUSH = True
DB_LOGGING = True
DB_FUTURE_COMPATIBLE = True
DB_NAME = getenv(key='DB_NAME', default=None)
DB_TEST_NAME = getenv(key='TEST_DB_NAME', default=None)
DB_TEST_URL = getenv(key='DB_TEST_URL', default=None)
DB_URL = getenv(key='DB_URL', default=None)

# Create a sqllite3 database connection, and database if none exists
connect(
    database=join(CURRENT_DIR_ABSPATH, DB_NAME)
)


# Classes
Session = sessionmaker(
    autoflush=DB_AUTOFLUSH
)


# Functions
def _create_session() -> SessionObject:
    """ Create and Bind an Engine object to a Session object.
        Add an sqlalchemy.engine.Engine binding to the custom
        Session class.

        Args:
            None.

        Returns:
            session (sqlalchemy.orm.Session as SessionObject):
                Instance of the Session class with an engine binding.
    """

    # Set the context appropriate DB URL
    if 'pytest' in argv[0]:
        db_url = DB_TEST_URL
    else:
        db_url = DB_URL

    # Verify db_url is not None
    if db_url is None:
        raise EnvironmentError(
            '\nSet the "DB_URL" and/or "DB_TEST_URL" environment variables\n'
        )

    # Create an sqlalchemy.engine.Engine object
    engine = create_engine(
        url=db_url,
        echo=DB_LOGGING,
        future=DB_FUTURE_COMPATIBLE
    )

    # Create database tables, if they don't already exist
    BASE.metadata.create_all(
        bind=engine
    )

    # Bind the engine object to a Session object
    Session.configure(
        bind=engine
    )

    # Create a session class instance
    session = Session()

    return session
