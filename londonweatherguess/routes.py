from flask import request, flash, session, render_template, redirect
from londonweatherguess.forms import temperatureGuess
from londonweatherguess import app
from londonweatherguess.weatherAppFunctions import saveResultToDatabase, check_if_temps_match, getUserAttemptNumber, \
    get_random_row


@app.route("/", methods=["GET", "POST"])
def gamepage():
    form = temperatureGuess()

    if request.method == "POST":
        if form.validate_on_submit():
            users_guess = form.users_guess.data
            saveResultToDatabase(UserGuess=users_guess, ActualTemp=session["roundTemp"], DateTime=session["dt"])
            result = check_if_temps_match(users_guess, session["roundTemp"])
            flash("Correct Answer! Well done", "success") if result else flash(
                "Incorrect this time! It was {}°C".format(session["roundTemp"]), "error")
            flash("Attempt Number: {}".format(getUserAttemptNumber()), "info")
            return redirect("/")

    if request.method == "GET":
        dt, formatted_date, roundTemp = get_random_row()
        session["dt"]=dt
        session["formatted_date"]=formatted_date
        session["roundTemp"] = roundTemp

    return render_template("gamepage.html", form=form, formatted_date=session["formatted_date"])