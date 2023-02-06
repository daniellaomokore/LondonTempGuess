import sqlalchemy
if __name__ == '__main__':
    from config import DATABASEPASSWORD, DATABASENAME, HOST, USER
else:
    from londonweatherguess.config import DATABASEPASSWORD, DATABASENAME, USER,HOST
from sqlalchemy import create_engine, Column, Integer, DateTime, orm

Base = sqlalchemy.orm.declarative_base()

class the_user(Base):
    __tablename__ = 'the_user'
    UserAttempt = Column(Integer, autoincrement=True, primary_key=True)
    UserGuess = Column(Integer)
    ActualTemp = Column(Integer)
    DateTime = Column(DateTime)

engine = create_engine("mysql+mysqlconnector://{user}:{password}@{host}/{DatabaseName}".format(
    user=USER,
    password=DATABASEPASSWORD,
    host=HOST,
    DatabaseName=DATABASENAME
))


Base.metadata.create_all(engine)





