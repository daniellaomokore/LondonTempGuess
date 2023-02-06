from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from londonweatherguess.config import DATABASEPASSWORD, DATABASENAME, SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = f"{SECRET_KEY}"  # secret key for the WTForm forms you create
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{PASSWORD}@localhost/{DatabaseName}'.format(
    PASSWORD=DATABASEPASSWORD, DatabaseName=DATABASENAME)
database = SQLAlchemy(app)

from londonweatherguess import routes
