# Use the official Python base image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

ENV DB_HOST = db
ENV DB_PORT = 3306
ENV DB_USER = root
ENV DB_PASSWORD = pass
ENV DB_DATABASE = planner

# Expose the port the application runs on
EXPOSE 8080

# Define the command to run the application
# Replace 'app.py' and 'main_function' with your actual application entry point
CMD ["python", "apis.py"]
