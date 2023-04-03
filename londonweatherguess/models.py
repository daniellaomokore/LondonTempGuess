import sqlalchemy
import mysql.connector
if __name__ == '__main__':
    from config import DATABASEPASSWORD, DATABASENAME, HOST, USER
else:
    from londonweatherguess.config import DATABASEPASSWORD, DATABASENAME, USER,HOST
from sqlalchemy import create_engine, Column, Integer, DateTime, orm

# TO CREATE THE DATABASE
# Note: I put this in a function to prevent cnx from running when i run the app even when I haven't ran the models file.
def create_database():
    # Establish a connection to the MySQL server
    cnx = mysql.connector.connect(user=USER, password=DATABASEPASSWORD, host=HOST)

    # Create a cursor object to execute SQL commands
    cursor = cnx.cursor()

    # Execute the SQL command to create the new database
    cursor.execute("CREATE DATABASE {}".format(DATABASENAME))

    # Commit the transaction to make the database creation permanent
    cnx.commit()

    # Close the cursor and the connection
    cursor.close()
    cnx.close()



# DATABASE TABLE SCHEMA

Base = sqlalchemy.orm.declarative_base()

class TheUser(Base):
    __tablename__ = 'the_user'
    UserAttempt = Column(Integer, autoincrement=True, primary_key=True, index=True) #The 'index=True' argument tells SQLAlchemy to create an index on the corresponding column
    UserGuess = Column(Integer)
    ActualTemp = Column(Integer)
    DateTime = Column(DateTime)



engine = create_engine("mysql+mysqlconnector://{user}:{password}@{host}/{DatabaseName}".format(
    user=USER,
    password=DATABASEPASSWORD,
    host=HOST,
    DatabaseName=DATABASENAME
))

def create_database_table():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_database()
    create_database_table()
