# cs50-2022-final-project

A simple e-commerce website using Flask framework, Jinja2, SQLite, HTML, CSS, Jinja2, Bootstrap and Python.

## Video Demo: 

 https://youtu.be/qMttOYvET98

## Project Description:

The application contains different pages. A user opens the first page of a website. A session-id is created for him and sent back to his browser.

Signup page which where user can create an account using email, password and password confirmation.After user submit the form,his information (email and password) will be stored in a SQLite3 database.
Shopping page, loads a gallery of clothing items that includes item's name, picture adn price. The clothing information is stored in a SQLite database.
If user already has an account he can switch easily into the signin page where he can type his email and password. At that time,login request has arrived on the server, email and password are checked against one another

Also, both signin and signup pages make sure that user submitted all fields and if not warning message will appear so he can't skip any. 

Shop page which where user can see all the products that avalable on the website. There are six different categories with six different pages for each.
Dresses, Tops, Shoes, Jeans, Skirts and Sweaters! 





![sc](https://user-images.githubusercontent.com/95029840/163598814-c2bc45f0-76ce-4722-8ced-dc00c6daa4b0.jpeg)







## Usage:

1. Requirements:

- Python 3
- Pip (Python package manager)


2. To run the application:

 set FLASK_APP=application.py
 flask run
