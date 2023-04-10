import unittest
from unittest.mock import patch, mock_open, Mock
from londonweatherguess.weatherAppFunctions import saveResultToDatabase, check_if_temps_match, getUserAttemptNumber, \
    get_random_row
from sqlalchemy.exc import IntegrityError,OperationalError



# The '@patch' decorator is used in this test case to replace the actual 'database','the_users' and 'datetime' module,
# in the main module with a mock object, created by the 'mock_database','mock_TheUser' and 'mock_datetime'  fixture.
class TestSaveResultToDatabase(unittest.TestCase):
    @patch('londonweatherguess.weatherAppFunctions.database')
    def test_save_result_to_database_success(self, mock_database):

        # Call the function under test
        result = saveResultToDatabase(UserGuess='5', ActualTemp='12', DateTime="1979-01-01 06:00:00 +0000 UTC")

        # Make assertions about the result
        self.assertEqual(result, 'Result Saved')

    @patch('londonweatherguess.database.session.add')
    @patch('londonweatherguess.database.session.commit')
    def test_save_result_to_database_IntegrityError(self, mock_commit, mock_add):
        # Mocking the database.session.add method to raise an IntegrityError

        mock_add.side_effect = IntegrityError(None, None, None)
        mock_commit.side_effect = IntegrityError(None, None, None)

        result = saveResultToDatabase(UserGuess='5', ActualTemp='12', DateTime="1979-01-01 06:00:00 +0000 UTC")

        self.assertEqual(result, 'Data already exists in database')

    @patch('londonweatherguess.database.session.add')
    @patch('londonweatherguess.database.session.commit')
    def test_save_result_to_database_IntegrityError(self, mock_commit, mock_add):
        # Mocking the database.session.add method to raise an IntegrityError

        mock_add.side_effect = OperationalError(None, None, None)
        mock_commit.side_effect = OperationalError(None, None, None)

        result = saveResultToDatabase(UserGuess='5', ActualTemp='12', DateTime="1979-01-01 06:00:00 +0000 UTC")

        self.assertEqual(result, "Unable to connect to database")

class TestCheckIfTempsMatch(unittest.TestCase):

    def test_temps_match(self):
        actual_temp = 20
        user_guess = 20
        result = check_if_temps_match(actual_temp, user_guess)
        self.assertTrue(result)

    def test_temps_do_not_match(self):
        actual_temp = 20
        user_guess = 21
        result = check_if_temps_match(actual_temp, user_guess)
        self.assertFalse(result)



# The '@patch' decorator is used in this test case to replace the actual 'database.session.query',
# in the main module with a mock object, created by the 'mock_query' fixture.
class TestGetUserAttemptNumber(unittest.TestCase):
    """
     Testing the 'getUserAttemptNumber()' function with mocking.
    """

    @patch('londonweatherguess.database.session.query')
    def test_get_user_attempt_number(self, mock_query):

        # Set up the mock to return the expected value
        mock_query.return_value.scalar.return_value = 5

        self.assertEqual(getUserAttemptNumber(), 5)



if __name__ == '__main__':
    unittest.main()
