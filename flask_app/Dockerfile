# Use Python 3.8 on a slim Buster image as the base
FROM python:3.8-slim-buster

# Set the working directory inside the container to /python-docker
WORKDIR /python-docker

# Copy the requirements.txt file to the container and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy all files from the current directory to the container
COPY . .

# Set the FLASK_APP environment variable
ENV FLASK_APP=app.py

# Command to run the Flask application
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
