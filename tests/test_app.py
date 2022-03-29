#!/usr/bin/env pytest
""" Tests for app/app.py. """

# Imports - Python Standard Library

# Imports - Third-Party

# Imports - Local
from app.app import home

# Constants
HOME_OUTPUT = 'This is a test.'


# Test functions
def test_home() -> None:
    """ Test the home function.

        Args:
            None.

        Returns:
            None.
    """

    assert home() == HOME_OUTPUT
