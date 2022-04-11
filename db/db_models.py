#!/usr/bin/env python3
""" SQLAlchemy Models for database interactions. """

# Imports - Python Standard Library

# Imports - Third-Party
from sqlalchemy import (
    Column, DateTime, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base

# Imports - Local

# Constants
BASE = declarative_base()


# Classes
class Repos(BASE):
    """ Create a table for repos.

        Args:
            BASE (sqlalchemy.ext.declarative.declarative_base).

        Returns:
            repr_string (str):
                Informational database table string.
    """

    # Assign DB table name
    __tablename__ = 'repos'

    # Assign table columns
    id = Column(
        type=Integer,
        primary_key=True
    )
    description = Column(
        type=String(100)
    )
    name = Column(
        type=String(50)
    )
    owner = Column(
        String(40)
    )
    url = Column(
        type=String(length=50)
    )
    last_updated = Column(
        type=DateTime
    )

    # Define repr function
    def __repr__(self):
        """ Function that returns the repo name and owner.
            Args:
                None.
            Returns:
                repr_string (str):
                    Returns a string with the hashtag and hashtag
                    count.
        """

        # Create a repr string
        repr_string = (
            f'<Repo(name={self.name}, owner={self.owner}, url={self.url})>'
        )

        return repr_string
