#!/usr/bin/env pytest
""" Tests for app/github_profiler.py. """

# Imports - Python Standard Library
from unittest.mock import MagicMock, patch

# Imports - Third-Party
import github

# Imports - Local
from app.github_profiler import github_auth

# Constants
MOCK_GITHUB_TOKEN = '0123456789'
MOCK_GITHUB_RATE_LIMITS = (4999, 5000)


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
    target=github,
    attribute='Github'
)
def test_github_auth(
    github_obj: MagicMock
) -> None:
    """ Test the github_auth function.

        Mock the github.Github object with the test class Github_Mock.

        Args:
            github_obj (unittest.mock.MagicMock):
                Mock of the github.Github object.

        Returns:
            None.
    """

    # Set the unitest.mock.patch.object return value to a Github_Mock instance
    github_obj.return_value = Github_Mock(
        login_or_token=MOCK_GITHUB_TOKEN
    )

    # Create a mock authenticated Github object
    gh = github_auth(
        github_token=MOCK_GITHUB_TOKEN
    )

    # Assert the value of the mock Github_Mock.rate_limiting attribute
    assert gh.rate_limiting == MOCK_GITHUB_RATE_LIMITS
