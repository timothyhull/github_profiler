# GitHub Profiler Repository

[![BCH compliance](https://bettercodehub.com/edge/badge/timothyhull/github_profiler?branch=main)](https://bettercodehub.com/results/timothyhull/github_profiler)

![[Linting and Static Code Analysis](https://github.com/timothyhull/github_profiler/actions/workflows/lint-files.yml)](https://img.shields.io/github/workflow/status/timothyhull/github_profiler/Linting%20and%20Static%20Code%20Analysis?label=Linting%20and%20Static%20Code%20Analysis)

![[GitHub Workflow Status](https://github.com/timothyhull/github_profiler/actions/workflows/pytest.yml)](https://img.shields.io/github/workflow/status/timothyhull/github_profiler/pytest%20Testing?label=pytest)

## Setup Procedures

1. Create a `.env` file at the root of your working directory that also
   hosts the `Dockerfile`.

2. Populate the `.env` file as follows:

    ```text
    FLASK_APP=web.app.py
    FLASK_DEBUG=True
    FLASK_HOST=127.0.0.1:8080
    FLASK_RUN_PORT=8080
    GITHUB_TOKEN=<your_github_personal_access_token>
    DB_NAME=github_profiler.db
    TEST_DB_NAME=test_github_profiler.db
    ```

3. Build the Docker image with the following command:

    ```bash
    docker build -t github-profiler .
    ```

4. Create and run the Docker container with the following command:

    ```bash
    docker run -dp --rm --env-file ./.env github-profiler
    ```
