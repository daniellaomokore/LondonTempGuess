


# Start with a base image that includes Python 3.10 and some basic dependencies
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the SQL script into the container
COPY createDatabase.sql .

# Install mysql-client for executing the SQL script
RUN apt-get update && apt-get install -y default-mysql-client

# Copy the rest of the application code into the container
COPY . .

# Set the environment variable for Flask
#Note:This app doesnt have any


# Expose the port that the app will run on
EXPOSE 5000

# Run the SQL script before starting the Flask app
RUN mysql -h mydatabasehost -u myuser -p mypassword mydatabase < myscript.sql

# Start the Flask app
CMD ["flask", "app:run", "--host=0.0.0.0"]