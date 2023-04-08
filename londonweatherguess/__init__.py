from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from londonweatherguess.config import DATABASEPASSWORD, DATABASENAME, SECRET_KEY

"""
Code Structure reference: 
https://youtu.be/44PvX0Yv368
"""

"""
This code block sets up a Flask web application with a secret key for encryption and a MySQL database for storage. It also initializes a database connection using the SQLAlchemy library, and imports the URL routes and view functions defined in the routes module.
"""



# Initialise the flask app
app = Flask(__name__)

# Set the apps configs
app.config['SECRET_KEY'] = f"{SECRET_KEY}"  # secret key for the WTForm forms you create
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{PASSWORD}@localhost/{DatabaseName}'.format(
    PASSWORD=DATABASEPASSWORD, DatabaseName=DATABASENAME)

# Initialise the database connection
database = SQLAlchemy(app)

from londonweatherguess import routes
