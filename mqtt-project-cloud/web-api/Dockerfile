# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 5000 for the Flask API
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=run.py

# Run flask command to start the Flask API
CMD ["flask", "run", "--host=0.0.0.0"]
