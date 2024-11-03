# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
RUN pip install --no-cache-dir fastapi uvicorn jinja2 plotly pandas

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable for Uvicorn host
ENV HOST=0.0.0.0

# Run FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]