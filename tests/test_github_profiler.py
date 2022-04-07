#!/usr/bin/env pytest
""" Tests for app/github_profiler.py. """

# Imports - Python Standard Library
from unittest.mock import MagicMock, patch

# Imports - Third-Party
from pytest import raises
from pytest import mark
from github.GithubException import BadCredentialsException
from requests import get
from requests.exceptions import ConnectionError
import github

# Imports - Local
from app.github_profiler import github_auth

# Constants
GITHUB_API_URL = 'https://api.github.com'
MOCK_GITHUB_KEY = '0123456789'
MOCK_GITHUB_RATE_LIMITS = (4999, 5000)
MOCK_GITHUB_USER = 'timothyhull'
MOCK_GITHUB_URL = 'https://github.com/timothyhull'

# Test for GitHub API online connectivity
try:
    # Send a GET request to the GitHub API
    get(
        url=GITHUB_API_URL
    )

    # Set the github_api_online variable to True for successful connections
    github_api_online = True

except ConnectionError:
    # Set the github_api_online variable to False for unsuccessful connections
    github_api_online = False


# Mock classes
class Github_Mock:
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
                None.
        """

        # Set rate limiting attribute tuple
        self.rate_limiting = MOCK_GITHUB_RATE_LIMITS

        return None


class Github_Auth_Mock:
    """ Mock of the PyGithub AuthenticatedUser class.

        The full mock object path is:
        github.AuthenticatedUser.AuthenticatedUser.
    """

    def __init__(self) -> None:
        """ Class initializer.

            Args:
                None.

            Returns:
                None.
        """

        self.name = MOCK_GITHUB_USER
        self.url = MOCK_GITHUB_URL

        return None


# Test functions
@patch.object(
    target=github,
    attribute='Github'
)
def test_github_auth(
    github_mock_obj: MagicMock
) -> None:
    """ Test the github_auth function.

        Mock the github.Github object with the test class Github_Mock.

        Args:
            github_mock_obj (unittest.mock.MagicMock):
                Mock of the github.Github object.

        Returns:
            None.
    """

    # Set the unitest.mock.patch.object return value to a Github_Mock instance
    github_mock_obj.return_value = Github_Mock(
        login_or_token=MOCK_GITHUB_KEY
    )

    # Create a mock authenticated Github object
    gh = github_auth(
        github_token=MOCK_GITHUB_KEY
    )

    # Assert the value of the mock Github_Mock.rate_limiting attribute
    assert gh.rate_limiting == MOCK_GITHUB_RATE_LIMITS


@mark.skipif(
    condition='github_api_online == False'
)
def test_github_auth_login_exception() -> None:
    """ Test authentication exceptions in the github_auth function.

        This test requires online connectivity to the GitHub API. Use
        pytest.mark.skipif to skip the test when GitHub API
        connectivity is not available.

        Args:
            None.

        Returns:
            None.
    """

    # Send a GitHub authentication request with an invalid token
    with raises(BadCredentialsException):
        github_auth(
            github_token=MOCK_GITHUB_KEY
        )


@patch.object(
    target=github,
    attribute='AuthenticatedUser'
)
def test_github_get_user(
    github_mock_auth_obj: MagicMock
) -> None:
    """ Test the github_get_user function.

        Mock the github.Github.get_user method with the test class
        Github_Mock.

        Args:
            github_mock_auth_obj (unittest.mock.MagicMock):
                Mock of the github.AuthenticatedUser object.

        Returns:
            None.
    """

    # Set the unitest.mock.patch.object return value to a Github_Mock instance
    github_mock_auth_obj.return_value = Github_Auth_Mock()

    gam = Github_Auth_Mock()

    assert gam.name == MOCK_GITHUB_USER
