# GitHub Profiler Container
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /app

# Update OS package list and install git
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

# Copy the Python pip requirements file
COPY requirements/requirements.txt requirements/requirements.txt

# Upgrade pip and install requirements from the requirements file
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements/requirements.txt && \
    rm -rf requirements

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Copy the application files to the container image
COPY /app /app

# Expose required ports
EXPOSE 8080/tcp

# Start the application
CMD ["flask, run"]
