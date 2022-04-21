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
from typing import Any
import github

# Imports - Local
from app.github_profiler import (
    GitHubRepo, github_auth, get_github_user, get_github_repos
)

# Constants
GITHUB_API_URL = 'https://api.github.com'
MOCK_GITHUB_KEY = '0123456789'
MOCK_GITHUB_RATE_LIMITS = (4999, 5000)
MOCK_GITHUB_USER = 'timothyhull'
MOCK_GITHUB_URL = 'https://github.com/timothyhull'
MOCK_GITHUB_PRIVATE = True
MOCK_GITHUB_REPO_NAME = 'my_repo'
MOCK_GITHUB_REPO_LIST = [
    GitHubRepo(
        name=MOCK_GITHUB_REPO_NAME,
        description='This is my repo',
        owner=MOCK_GITHUB_USER,
        private=MOCK_GITHUB_PRIVATE,
        url=MOCK_GITHUB_URL,
        updated_at=None
    )
]

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
class Github_Auth_Mock:
    """ Mock of the PyGithub AuthenticatedUser class.

        The full path to the mocked object is:
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

    def get_repos(
        self,
        *args: Any,
        **kwargs: Any
    ):
        """ Mock of the AuthenticatedUser.get_repos method.

            The full path to the mocked object is:
            github.AuthenticatedUser.AuthenticatedUser.get_repos.

            Args:
                *args (Any):
                    Positional arguments with no specified paramater.

                **kwargs (Any):
                    Keyword arguments with no specified paramater.

            Returns:
                github_repos (GitHub_PaginatedList_Mock):
                    Instance of the GitHub_PaginatedList_Mock class.
        """

        # Create a mock github.PaginatedList.PaginatedList object
        github_repos_mock = MOCK_GITHUB_REPO_LIST

        return github_repos_mock


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

    def get_user(
        self,
        login: str = None
    ) -> Github_Auth_Mock:
        """ Mock of the github.Github.get_user method.

            Args:
                login (str, optional):
                    GitHub user ID to retreive data for.  Default is
                    None, which retrieves data for the user associated
                    with the github.Github token authentication.

            Returns:
                github_mock_user (Github_Auth_Mock):
                    Instance of the Github_Auth_Mock class.
        """

        # Create a mock github.AuthenticatedUser.AuthenticatedUser object
        github_mock_user = Github_Auth_Mock()

        return github_mock_user


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


@patch(
    target='github.Github.get_user'
)
def test_get_github_user(
    github_mock_auth_obj: MagicMock
) -> None:
    """ Test the get_github_user function.

        Mock the github.Github.get_user method with the test class
        Github_Mock.

        Args:
            github_mock_auth_obj (unittest.mock.MagicMock):
                Mock of the github.AuthenticatedUser object.

        Returns:
            None.
    """

    # Call the get_github_user function with a mock github.Github object
    gh_user = get_github_user(
        github_object=Github_Mock()
    )

    assert gh_user.name == MOCK_GITHUB_USER


@patch(
    target='github.AuthenticatedUser.AuthenticatedUser.get_repos'
)
def test_get_github_repos(
    github_mock_repos_obj: MagicMock
) -> None:
    """ Test the get_github_repos function.

        Mock the github.PaginatedList.PaginatedList object returned by
        the github.AuthenticatedUser.AuthenticatedUser.get_repos
        method.

        Args:
            github_mock_auth_obj (unittest.mock.MagicMock):
                Mock of the github.AuthenticatedUser object.

        Returns:
            None.
    """

    # Call the get_github_repos function with a mock AuthenticatedUser object
    gh_repos = get_github_repos(
        github_user_object=Github_Auth_Mock()
    )

    assert gh_repos[0].name == MOCK_GITHUB_REPO_NAME
