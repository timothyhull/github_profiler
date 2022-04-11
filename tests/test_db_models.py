#!/usr/bin/env pytest
""" Tests for db/db_models.py. """

# Imports - Python Standard Library

# Imports - Third-Party

# Imports - Local
from db.db_models import Repos

# Constants
REPO_NAME = 'test_repo'
REPO_OWNER = 'timothyhull'
REPO_URL = f'https://github.com/{REPO_OWNER}/{REPO_NAME}'
REPOS_REPR_STRING = (
    f'<Repo(name={REPO_NAME}, owner={REPO_OWNER}, url={REPO_URL})>'
)


# Test functions
def test_repos() -> None:
    """ Test the Repos class.

        Determine if the Repos.__repr__ method returns the expected
        string value.

        Args:
            None.

        Returns:
            None.
    """

    # Create an instance of the Repos class and set attributes
    repo = Repos()
    repo.name = REPO_NAME
    repo.owner = REPO_OWNER
    repo.url = REPO_URL

    assert str(repo) == REPOS_REPR_STRING
