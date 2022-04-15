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

Shop page which where user can see all the products that available on the website. There are six different categories with six different pages for each.
Dresses, Tops, Shoes, Jeans, Skirts and Sweaters! Each page represented by separate HTML file. for example, top.html, jeans.html and so on.. 

<img width="694" alt="Screen Shot 2022-04-15 at 7 07 45 PM" src="https://user-images.githubusercontent.com/95029840/163599895-3f37126c-f3b8-4d57-b474-4a02d7942329.png">




In each page, user can see variety of elegant products, such as item name, price and image that shows the details of items. 


<img width="693" alt="Screen Shot 2022-04-15 at 7 05 42 PM" src="https://user-images.githubusercontent.com/95029840/163599723-b7df6d67-40e0-4fd0-9cfa-354949824b86.png">

A user has the ability to add any of the items into his shopping cart simply by clicking on "Add to Cart" button. After that, user will be redirected to shopping cart page which is bag.html, and can see what items he add to cart, the quantity and the total price. 

The about page, contains information about this e-commerce website.

## Usage:

1. Requirements:

- Python 3
- Pip (Python package manager)


2. To run the application:

 set FLASK_APP=application.py
 flask run
