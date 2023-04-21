# London Temp Guess App


🚀<b>Usage</b>:

<i>This is a simple web app game where users need to guess the temperature at a certain date and time from the past in London.

This was created built with Python, SQL, MySQL, HTML, CSS , JavaScript, Flask Framework and a CSV file for the temperature data.</i>

<img width="956" alt="picpic" src="https://user-images.githubusercontent.com/79287671/216978137-52fb7585-ad1c-4aab-a333-46650c941e56.png">

<img width="940" alt="picpic1" src="https://user-images.githubusercontent.com/79287671/216978177-b29cf5b2-9171-434f-aa35-6fc1294f2a31.png">

<img width="944" alt="pic2" src="https://user-images.githubusercontent.com/79287671/216766039-4548db10-927c-447d-91c8-c6e3fd67316f.png">

<img width="373" alt="pic3" src="https://user-images.githubusercontent.com/79287671/216766062-92ecc54c-67e0-4d39-8803-5236816f6fa7.png">
                           

✨<b>How to Run:</b>

* Install the dependencies by running `pip install -r requirements.txt` in the terminal or command prompt on your system.

* Run the 'models.py' file to create your database and it's tables.


* set up your environmental variables in a '.env' file in the root. With variables for :
  * USER = "[your MYSQL user]"
  * DATABASEPASSWORD = "[your MYSQL password]"  
  * HOST = "[your MYSQL host]" 
  * SECRET_KEY = "[your secret key]"

* Run `python app.py` in the terminal of the root directory of the project or run the 'run.py' file directly and then click the link: http://127.0.0.1:5000.


✨<b>How to Test:</b>

* Run `python test.py` in the terminal of the root directory of the project or run the 'test.py' file directly.



* Code Structure reference: https://youtu.be/44PvX0Yv368


❔ <b>Follow-Up Questions</b>: ❓

● Framework/libraries did you use for the front-end and back-end: 

 ● Flask - I used the Flask framework to create the app since it's a small web application which would allow me to render html templates and use flashes to notify users of their attempts number + if their guess was correct or incorrect , also use of sessions to store data.
 
 ● Bootstrap - I used Bootstrap for the flash message colours for error , success and info flash messages. 

 ● csv - to open the csv file.
 ● random - to get random rows from the csv file.
 ● datetime - to format the datetime to make it more readable on the frontend.
 ● flask_sqlalchemy - to communicate with the database with SQLAlchemy instead of using raw sql to prevent sql injection.
 ● flask_wtf/FlaskForm - to create submission form with csrf token and validators.


● If you had more time, what further improvements or new features would you add?
> New feature: Add a streaks feature if user got a few correct in a row & feature for users to choose their answer out of three temperatures to make it easier.
> I would also save the csv into a variable to make it less expensive so that it doesn't have to access the csv file each time a new date and time is selected.

● What steps did you take to future proof the application for possible expansions?
> Using a base html so that I can easily make it a multi-page web app if I wanted to expand it without repeating code
> Using Unit Testing to make sure the code functionality is working as expected.
> I've used SQL Indexes in my Database to speed up database queries and make data retrieval more efficient.



● Which part of the challenge are you most proud of and why?
> I'm most proud of the efficient and scalable backend system developed for the web app and the seamless integration of the backend with the frontend, which provides a smooth and responsive user experience & the unit testing and mocking.

● Which parts did you spend the most time with? What did you find most difficult?
> The functionality to ensure that the csv was validating the correct temperature against the users temperature guess whilst also refreshing the page without calling the same function twice on the GET and POST request. Also I came across a session cache issues with certain browsers which I later developed a solution to solve this problem .
