import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'gfhrjrynsrxc'

db = SQL("sqlite:///users.db")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure email was submitted
        if not email:
            return render_template("failure.html", message="Email is required!")
        
        # Ensure password was submitted
        if not password:
            return render_template("failure.html", message="Password is required!")

        # Ensure confirmation was submitted
        if not confirmation:
            return render_template("failure.html", message="Password confirmation is required!")

        # Ensure password matches confirmation
        if password != confirmation:
            return render_template("failure.html", message="Password does not match!")

        # Ensure length of password(7 characters min)
        if len(password) < 7:
            return render_template("failure.html", message="7 characters minimum!")

        #hash password
        hash = generate_password_hash(password)

        # Ensure email is unique or taken???????
        emails = db.execute("SELECT email FROM users")
        if email in emails:
            return render_template("failure.html", message="Email already exists!")

    
        # Add email to database
        db.execute("INSERT INTO users (email, hash) VALUES(?, ?)", email, hash)

        # Redirect user to home page
        return redirect("/")
        
    else:
        return render_template("signup.html")


# @app.route("/signin", methods=["GET", "POST"])
# def signin():
#     if request.method == "POST":

#     else:
#         return render_template("signin.html")


# @app.route("/shop", methods=["GET", "POST"])
# def shop():
#     user_id = 


if __name__ == "__main__":
  app.run()
