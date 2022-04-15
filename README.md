# cs50-2022-final-project

A simple e-commerce website using Flask, Jinja2, SQLite, HTML, CSS, Jinja2, Bootstrap and Python.

-Video Demo: https://youtu.be/qMttOYvET98

-Project Description:

The application contains different pages. A user opens the first page of a website. A session-id is created for him and sent back to his browser.

The Signup page which where user can create an account using email, password and password confirmation.After user submit the form,his information (email and password) will be stored in a SQLite3 database.
Shopping page, loads a gallery of clothing items that includes item's name, picture adn price. The clothing information is stored in a SQLite database.
If user already has an account he can switch easily into the signin page where he can type his email and password. At that time,login request has arrived on the server, email and password are checked against one another


Also, both signin and signup pages make sure that user submitted all fields and if not warning message will appear.














To run the application:

set FLASK_APP=application.py
flask run
