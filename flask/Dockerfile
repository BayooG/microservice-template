# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

# Copy requirements file to /app 
ADD requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /app 
ADD . /app

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
