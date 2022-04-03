#!/usr/bin/env pytest
""" Tests for app/github_profiler.py. """

# Imports - Python Standard Library
from unittest.mock import MagicMock, patch

# Imports - Third-Party
from github import Github

# Imports - Local
from app.github_profiler import github_auth

# Constants
MOCK_GITHUB_TOKEN = '0123456789'
MOCK_GITHUB_RATE_LIMITS = (4950, 5000)


# Mock classes
class Github_Mock():
    """ Mock of the PyGithub github.Github class. """

    def __init__(
        self,
        login_or_token: str = None
    ) -> None:
        """ Class initializer.

            Args:
                login_or_token (str, optional):
                    Placeholder argument for a mock GitHub token.

            Returns:
                None
        """

        # Set rate limiting attribute tuple
        self.rate_limiting = MOCK_GITHUB_RATE_LIMITS

        return None


# Test functions
@patch.object(
    target=Github,
    attribute='rate_limiting',
    return_value=MOCK_GITHUB_RATE_LIMITS
)
def test_github_auth(
    github_obj: MagicMock
) -> None:
    """ Test the github_auth function.

        Args:
            github_obj (unittest.mock.MagicMock):
                unittest MagicMock object for the github.Github object.

        Returns:
            None.
    """

    # Create a mock authenticated Github object
    github_object = github_auth(
        github_token=MOCK_GITHUB_TOKEN
    )

    assert github_object == MOCK_GITHUB_RATE_LIMITS
