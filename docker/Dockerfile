# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose Flask's default port
EXPOSE 5000

# Start the Flask application
CMD ["python3", "app.py"]