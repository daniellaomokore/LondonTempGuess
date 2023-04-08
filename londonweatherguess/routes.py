from flask import request, flash, session, render_template, redirect
from londonweatherguess.forms import temperatureGuess
from londonweatherguess import app
from londonweatherguess.weatherAppFunctions import saveResultToDatabase, check_if_temps_match, getUserAttemptNumber, \
    get_random_row


@app.route("/", methods=["GET", "POST"])
def gamepage():
    """
    This function displays the webpage for the game and handles GET and POST requests to the root URL ("/").
    """
    form = temperatureGuess()   # create a form object of the form class

    if request.method == "POST": # if a post method request is made
        if form.validate_on_submit():  # if the users guess submission is valid
            users_guess = form.users_guess.data   # get the users guess from their form submission
            saveResultToDatabase(UserGuess=users_guess, ActualTemp=session["roundTemp"], DateTime=session["dt"])
            result = check_if_temps_match(users_guess, session["roundTemp"])
            flash("Correct Answer! Well done", "success") if result else flash(
                "Incorrect this time! It was {}°C".format(session["roundTemp"]), "error")
            flash("Attempt Number: {}".format(getUserAttemptNumber()), "info")
            return redirect("/")

    if request.method == "GET":   # if a get method request is made/when the page loads
        dt, formatted_date, roundTemp = get_random_row()  # call the get_random_row() function and put the data returned into variables

        # save the data into sessions
        session["dt"] = dt
        session["formatted_date"]=formatted_date
        session["roundTemp"] = roundTemp

    return render_template("gamepage.html", form=form, formatted_date=session["formatted_date"])