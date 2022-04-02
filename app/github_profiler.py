#!/usr/bin/env python3
""" GitHub profiler application for #100DaysofCode Days 59+60. """

# Imports - Python Standard Library
from os import getenv

# Imports - Third-Party
from dotenv import load_dotenv
from github import Github

# Imports - Local

# Load environment variables
load_dotenv()

# Constants
GITHUB_TOKEN = getenv('GITHUB_TOKEN')

# Test Github object
gh = Github(
    login_or_token=GITHUB_TOKEN
)

# Display GitHub rate limits
print(gh.rate_limiting)
