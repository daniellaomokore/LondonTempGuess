import os
from dotenv import load_dotenv


"""
    The code below sets up the necessary environmental variables for connecting to a MySQL database and sets a secret key.
"""

# load environmental variables
load_dotenv()

# Mysqlworkbench
# environmental variables stored

"""DATABASENAME = "tempGuess_user"
"""
"""
USER = os.environ.get('USER')
DATABASEPASSWORD = os.environ.get('DATABASEPASSWORD')  # THIS IS YOUR MYSQLWORKBENCH PASSWORD
HOST = os.environ.get('HOST')

# secret key
SECRET_KEY = os.environ.get('SECRET_KEY')"""


DATABASENAME = "heroku_b30aff198b29397"
USER = "b03ee4d90b32be"
DATABASEPASSWORD = "70cbe40f"  # THIS IS YOUR MYSQLWORKBENCH PASSWORD
HOST = "us-cdbr-east-06.cleardb.net"

# secret key
SECRET_KEY = "secretkey"

