import csv
import random
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError,OperationalError
from londonweatherguess import database
from londonweatherguess.models import TheUser


def check_if_temps_match(users_guess, actualTemp):
    """
        This function returns true/false depending on if the user has guessed correctly or not
    """

    if int(actualTemp) == int(users_guess):
        return True
    else:
        return False


def getUserAttemptNumber():
    """
    This function returns the number of guessing attempts the user has had
    """

    # note: Since we've created an index named 'idx_user_attempt' for the 'UserAttempt' column,
    # MySQL will automatically use the index to optimize the query. We don't need to specify the index
    # in the query since SQLAlchemy will handle it for us.
    # Using the index will speed up the search
    result = database.session.query(func.max(TheUser.UserAttempt)).scalar()
    return result


def get_random_row():
    """
    This function gets a random row from the csv file, formats some data to be more readable and returns the data
    """
    try:
        # Select rows of temperature data from csv file at random
        with open('londonweatherguess/Static/resource/london_temp.csv') as london_temps:
            data = csv.reader(london_temps)
            randomly_chosen_row = random.choice(list(data))

            # GETTING + FORMATTING THE DATETIME
            dt = randomly_chosen_row[1] # select the second column of the 'randomly_chosen_row' to get 'dt_iso' column (date time in ISO format) and set to it to 'dt' variable.
            # format the date time to be more readable for later use.
            date_object = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S %z %Z")
            formatted_date = date_object.strftime("%d/%m/%Y %I:%M %p")

            # GETTING + ROUNDING UP THE TEMPERATURE
            temp = randomly_chosen_row[2]
            roundTemp = round(float(temp))

    # Log the exception and return an error message
    except FileNotFoundError as e:
        print("Error: could not find the temperature data file.")
        return "Error: could not find the temperature data file."

    else:
        return dt, formatted_date, roundTemp #unformatted date time, formatted date time, rounded temperature


def saveResultToDatabase(UserGuess, ActualTemp, DateTime):
    """
    This function saves the user guess, the date-time and the actual temperature of London on the current datatime into the database.
    """
    try:
        DateTime = datetime.strptime(DateTime[:-4], '%Y-%m-%d %H:%M:%S %z')
        data = TheUser(UserGuess=UserGuess, ActualTemp=ActualTemp, DateTime=DateTime)
        database.session.add(data)
        database.session.commit()
    except IntegrityError:
        # If the data is already in the database and raise an error
        return "Data already exists in database"
    except OperationalError:
        # If there's a database connection error and raise an error
        return "Unable to connect to database"
    else:
        # If the transaction is successful, return a success message
        return "Result Saved"
