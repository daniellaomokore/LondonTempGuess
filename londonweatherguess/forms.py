from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired


class temperatureGuess(FlaskForm):
    """
        This class creates a submission form for users temperature guesses
    """
    users_guess = IntegerField("users_temp_guess:", validators=[DataRequired()])
    submit = SubmitField("Submit Answer")
