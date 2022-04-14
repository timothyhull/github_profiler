#!/usr/bin/env python3
""" GitHub profiler application for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library
from collections import namedtuple
from os import getenv

# Imports - Third-Party
from dotenv import load_dotenv
from github.AuthenticatedUser import AuthenticatedUser
from github.GithubException import BadCredentialsException
from github.GithubObject import NotSet, _NotSetType
from typing import List, Union
import github

# Imports - Local

# Load environment variables
load_dotenv()

# Constants
GITHUB_AFFILIATION = 'owner'
GITHUB_TOKEN = getenv('GITHUB_TOKEN')

# namedtuple objects
GitHubRepo = namedtuple(
    # Object to attributes for individual GitHub repos
    typename='GitHubRepo',
    field_names=[
        'name',
        'description',
        'owner',
        'url',
        'last_modified'
    ]
)


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


def get_github_user(
    github_object: github.Github,
    github_user_id: Union[str, _NotSetType] = NotSet
) -> github.AuthenticatedUser.AuthenticatedUser:
    """ Create a GitHub authenticated user object.

        Calls the github.Github.get_user method on the github_object.

        Args:
            github_object (github.Github):
                github.Github user object of class type
                github.AuthenticatedUser.AuthenticatedUser.

            github_user_id (
                str | github.GithubObject._NotSetType, optional
            ):
                User ID (str) of GitHub user to retreive data for.
                Default is github.GithubObject._NotSetType, which
                retrieves data for the user associated with the
                github.Github authentication token.

        Returns:
            github_user (github.AuthenticatedUser.AuthenticatedUser):
                GitHub authenticated user object.
    """

    # Create the GitHub authenticated user object
    github_user = github_object.get_user(
        login=github_user_id
    )

    return github_user


def get_github_repos(
    github_user_object: AuthenticatedUser
) -> List:
    """ Get a user's GitHub repos.

        Calls the get_repos method on the
        github.AuthenticatedUser.AuthenticatedUser github_user.

        Args:
            github_user (github.AuthenticatedUser.AuthenticatedUser):
                github.AuthenticatedUser.AuthenticatedUser object for
                a GitHub user.

        Returns:
            repo_list (List):
                List of GitHubRepo namedtuple objects for each GitHub
                repos.
    """

    # Get a list of repos for a GitHub user
    repos = github_user_object.get_repos(
        affiliation=GITHUB_AFFILIATION
    )

    # Create a list to hold each repo as a list item
    repo_list = []

    # Loop over the repos PaginatedList object
    for repo in repos:

        # Create a GitHubRepo namedtuple object for the current repo iteration
        repo_object = GitHubRepo(
            name=repo.name,
            description=repo.description,
            owner=repo.owner,
            url=repo.url,
            last_modified=repo.last_modified
        )

        # Append the repo_object to repo_list
        repo_list.append(repo_object)

    # Sort the repo list by repo name
    repo_list.sort(
        key=lambda repo: repo.name,
        reverse=True
    )

    return repo_list
