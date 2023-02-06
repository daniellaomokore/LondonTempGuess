import csv
import random
from datetime import datetime
from sqlalchemy import func
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
    result = database.session.query(func.max(TheUser.UserAttempt)).scalar()
    return result


def get_random_row():
    """
    This function gets a random row from the csv file, formats some data to be more readable and saves the values from the row into the session
    """
    # Select rows of temperature data from csv file at random
    with open('londonweatherguess/Static/resource/london_temp.csv') as london_temps:
        data = csv.reader(london_temps)
        chosen_row = random.choice(list(data))

        # grab data in a more readable format
        dt = chosen_row[1]
        date_object = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S %z %Z")
        formatted_date = date_object.strftime("%d/%m/%Y %I:%M %p")

        temp = chosen_row[2]
        roundTemp = round(float(temp))

        return dt, formatted_date, roundTemp


def saveResultToDatabase(UserGuess, ActualTemp, DateTime):
    """
    This function saves the user guess, the date-time and the actual temperature of London on the current datatime into the database.
    """
    DateTime = datetime.strptime(DateTime[:-4],
                                 '%Y-%m-%d %H:%M:%S %z')  # formats date using strptime and slicing to get rid of 'UTC'

    data = TheUser(UserGuess=UserGuess, ActualTemp=ActualTemp, DateTime=DateTime)
    database.session.add(data)
    database.session.commit()

    return "Result Saved"
