#!/usr/bin/env pytest
""" Tests for app/app.py. """

# Imports - Python Standard Library

# Imports - Third-Party

# Imports - Local
from app.app import home, hello

# Constants
HOME_OUTPUT = 'This is a test.'
HELLO_NAME = 'Tim'
HELLO_OUTPUT = 'Hello, Tim.'


# Test functions
def test_home() -> None:
    """ Test the home function.

        Args:
            None.

        Returns:
            None.
    """

    assert home() == HOME_OUTPUT


def test_hello() -> None:
    """ Test the hello function.

        Args:
            None.

        Returns:
            None.
    """

    assert hello(name=HELLO_NAME) == HELLO_OUTPUT
