#!/usr/bin/env python3
""" SQLAlchemy Models for database interactions. """

# Imports - Python Standard Library

# Imports - Third-Party
from sqlalchemy import (
    Boolean, Column, DateTime, Integer, String
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

        Attributes:
            name (str):
                Repository name.

            description (str),
                Repository description.

            private (bool):
                Private repository status.

            owner (str):
                Repository owner.

            url (str):
                Repository URL

            updated_at (datetime.datetime.utcnow):
                Timestamp for the last repository update.

        Returns:
            repr_string (str):
                Informational database table string.
    """

    # Assign DB table name
    __tablename__ = 'repos'

    # Assign table columns
    id = Column(
        Integer,
        primary_key=True
    )
    name = Column(String(50))
    description = Column(String(100))
    owner = Column(String(40))
    private = Column(Boolean)
    url = Column(String(50))
    updated_at = Column(DateTime)

    # Define repr function
    def __repr__(self):
        """ Function that returns the repo name and owner.

            Args:
                None.

            Returns:
                repr_string (str):
                    Returns a string with the repo name,
                    owner, private status, and URL.
        """

        # Create a repr string
        repr_string = (
            f'<Repo(name={self.name}, owner={self.owner}, '
            f'private={self.private}, url={self.url})>'
        )

        return repr_string
