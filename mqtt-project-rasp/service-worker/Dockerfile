# Base image for Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the service worker code (config.py)
COPY config.py /app/config.py

# Copy the tasks directory, ensuring it is available for Celery to discover
COPY tasks /app/tasks

# Run Celery worker with task auto-discovery
CMD ["celery", "-A", "config", "worker", "--loglevel=info"]
