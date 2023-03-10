import unittest
from unittest.mock import patch

from londonweatherguess.weatherAppFunctions import saveResultToDatabase, check_if_temps_match, getUserAttemptNumber



# The @patch decorator is used in this test case to replace the actual 'database','the_users' and 'datetime' module,
# in the main module with a mock object, created by the mock_database fixture
class TestSaveResultToDatabase(unittest.TestCase):
    @patch('londonweatherguess.weatherAppFunctions.datetime')
    @patch('londonweatherguess.weatherAppFunctions.TheUser')
    @patch('londonweatherguess.weatherAppFunctions.database')
    def test_save_result_to_database(self, mock_database, mock_TheUser, mock_datetime):
        result = saveResultToDatabase(UserGuess='5', ActualTemp='12', DateTime="1979-01-01 06:00:00 +0000 UTC")

        self.assertEqual(result, 'Result Saved')


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


# Testing the getUserAttemptNumber() Function with mocking
class TestGetUserAttemptNumber(unittest.TestCase):

    @patch('londonweatherguess.database.session.query')
    def test_get_user_attempt_number(self, mock_query):
        mock_query.return_value.scalar.return_value = 42
        result = getUserAttemptNumber()
        self.assertEqual(result, 42)


if __name__ == '__main__':
    unittest.main()
