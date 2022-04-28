#!/usr/bin/env python3
""" GitHub profiler helper functions application. """

# Imports - Python Standard Library
from os import getcwd
from os.path import join

# Imports - Third-Party
from dotenv import load_dotenv


def load_env_vars(
    env_path: str | None = None
) -> bool:
    """ Load environment variables from multiple paths.

        Args:
            path (str, optional):
                Custom path to an environment variable file

        Returns:
            result (bool):
                Combined result of all load_dotenv calls

    """

    # Load environment variables from the directory of this script
    script_path = load_dotenv(
        dotenv_path='./.env'
    )

    # Load environment variables from the script user's working directory
    workdir_path = load_dotenv(
        dotenv_path=join(
            getcwd(), '.env'
        )
    )

    # Load environment variables from a custom path
    if env_path is not None:
        custom_path = load_dotenv(
            dotenv_path=env_path
        )
    else:
        custom_path = True

    # Calculate a boolean result
    result = script_path and workdir_path and custom_path

    return result
