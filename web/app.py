#!/usr/bin/env python3
""" GitHub profiler web application for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library

# Imports - Third-Party
from flask import Flask, render_template, url_for

# Imports - Local
from db import db_helper

# Flask web application object
app = Flask(
    import_name=(__name__)
)


# Default route
@app.route(
    rule='/'
)
@app.route(
    rule='/<repo>'
)
def index(
    repo: str = None
) -> str:
    """ Display all repositories.

        Args:
            repo (str):
                Name of a repo to filter by.

        Returns:
            repos (str):
                List of all repositories.
    """

    # Request all repos from the database
    repos_list = db_helper.get_repos(
        repo_name=repo
    )

    # Build repos string
    repos = ''
    repos += f'Total repos: {len(repos_list)}\n'

    for index, repo in enumerate(repos_list):
        repos += (
            f'{index + 1}. Repo name: {repo.name}\n'
        )

    return render_template(
        template_name_or_list='index.html',
        repo=repo
    )


# Testing the url_for method, which will automatically escape special chars
# https://flask.palletsprojects.com/en/2.1.x/quickstart/#url-building
with app.test_request_context():
    print(url_for('index'))
