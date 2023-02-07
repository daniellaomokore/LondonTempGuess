from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from londonweatherguess.config import DATABASEPASSWORD, DATABASENAME, SECRET_KEY


# Initialise the flask app
app = Flask(__name__)

# Set the apps configs
app.config['SECRET_KEY'] = f"{SECRET_KEY}"  # secret key for the WTForm forms you create
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{PASSWORD}@localhost/{DatabaseName}'.format(
    PASSWORD=DATABASEPASSWORD, DatabaseName=DATABASENAME)

# Initialise the database connection
database = SQLAlchemy(app)

from londonweatherguess import routes
