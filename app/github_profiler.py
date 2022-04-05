#!/usr/bin/env python3
""" GitHub profiler application for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library
from os import getenv

# Imports - Third-Party
from dotenv import load_dotenv
from github.GithubException import BadCredentialsException
import github

# Imports - Local

# Load environment variables
load_dotenv()

# Constants
GITHUB_TOKEN = getenv('GITHUB_TOKEN')


# Functions
def github_auth(
    github_token: str = None
) -> github.Github:
    """ Create a Github object with public or login/token auth.

        Args:
            github_token (str, optional):
                Github user token for user authentication.  Default
                value is None, which provides public authentication,
                with 60 API requests per hour.  Token-authenticated
                Github objects have 5,000 API requests per hour.

        Returns:
            github_object (github.Github):
                Instance of the github.Github class.
    """

    # Create a Github object
    github_object = github.Github(
        login_or_token=github_token
    )

    # Attempt to determine authentication status
    try:
        github_object.rate_limiting

    # Handle a BadCredentialsException and re-raise the exception
    except BadCredentialsException as e:
        print(f'Error: {e.status} {e.data}\n')
        raise

    return github_object
