#!/usr/bin/env python3
""" GitHub profiler database for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library
from os import getenv
from os.path import abspath, dirname, join
from pathlib import Path
from sqlite3 import connect
from sys import argv
from typing import List

# Imports - Third-Party
from sqlalchemy import create_engine
from sqlalchemy.orm import Session as SessionObject
from sqlalchemy.orm import sessionmaker

# Imports - Local
from _github_profiler.github_helper import load_env_vars
from db.db_models import BASE, Repos

# Load environment variables
load_env_vars()

# Constants
CURRENT_DIR = Path(dirname(__file__))
CURRENT_DIR_ABSPATH = abspath(CURRENT_DIR)
DB_AUTOFLUSH = True
DB_LOGGING = True
DB_FUTURE_COMPATIBLE = True
DB_NAME = getenv(key='DB_NAME', default=None)
DB_PATH = join(CURRENT_DIR_ABSPATH, DB_NAME)
DB_TEST_NAME = getenv(key='TEST_DB_NAME', default=None)
DB_TEST_URL_ROOT = 'sqlite+pysqlite:///:memory:'
DB_TEST_URL = f'{DB_TEST_URL_ROOT}'
DB_URL_ROOT = 'sqlite+pysqlite:///'
DB_URL = f'{DB_URL_ROOT}{DB_PATH}'

# Create a sqllite3 database connection, and database if none exists
connect(
    database=DB_PATH
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
            '\nSet either the "DB_NAME" or "DB_TEST_URL" '
            'environment variables.\n'
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


# Create a session object using _create_session
session = _create_session()


def commit_session(
    session: SessionObject = session
) -> bool:
    """ Commit the SQLAlchemy session to the database.

        Args:
            session (sqlalchemy.orm.Session (SessionObject), optional):
                By default, uses the session object created by the
                _create_session function.  Allows the ability to pass a
                mock Session object for pytest testing.

        Returns:
            session_in_transaction (bool):
                False if the transaction is complete, True if the
                transaction is neither committed nor rolled back.
    """

    # Commit the changes to the database
    session.commit()

    # Collect the session transaction status
    session_in_transaction = session.in_transaction()

    return session_in_transaction


def truncate_tables(
    session: SessionObject = session
) -> bool:
    """ Remove all rows from the database tables.

        Args:
            session (sqlalchemy.orm.Session (SessionObject), optional):
                By default, uses the session object created by the
                _create_session function.  Allows the ability to pass a
                mock Session object for pytest testing.

        Returns:
            session_active (bool):
                False if the transaction is complete, True if the
                transaction is neither committed nor rolled back.
    """

    # Delete data returned by a query of the Repos table
    session.query(Repos).delete()

    # Commit the changes to the database
    session_active = commit_session(
        session=session
    )

    return session_active


def get_repos(
    session: SessionObject = session
) -> List:
    """ Get all repos from the database.

        Args:
            session (sqlalchemy.orm.Session (SessionObject), optional):
                By default, uses the session object created by the
                _create_session function.  Allows the ability to pass a
                mock Session object for pytest testing.

        Returns:
            repos (List):
                All entries in the repos table, sorted alphabetically,
                by name.
    """

    # Retreive and sort all entries from the hashtags table
    repos = session.query(Repos).order_by(Repos.name).all()

    return repos


def add_repos(
    repos: List,
    session: SessionObject = session
) -> bool:
    """ Add repos to the database.

        Args:
            repos (List):
                List object with new hashtags.

            session (sqlalchemy.orm.Session (SessionObject), optional):
                By default, uses the session object created by the
                _create_session function.  Allows the ability to pass a
                mock Session object for pytest testing.

        Returns:
           session_active (bool):
                False if the transaction is complete, True if the
                transaction is neither committed nor rolled back.
    """

    # Add new repos to the session object
    for repo in repos:
        session.add(
            instance=Repos(
                name=repo.name,
                description=repo.description,
                private=repo.private,
                owner=repo.owner,
                url=repo.url,
                updated_at=repo.updated_at
            )
        )

    # Commit the changes to the database
    session_active = commit_session(
        session=session
    )

    return session_active
