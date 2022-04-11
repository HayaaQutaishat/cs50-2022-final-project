import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'gfhrjrynsrxc'

db = SQL("sqlite:///project.db")

@app.route("/home")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/dress")
def dress():
    return render_template("dress.html")


@app.route("/skirt")
def skirt():
    return render_template("skirt.html")

@app.route("/jeans")
def jeans():
    return render_template("jeans.html")

@app.route("/sweater")
def sweater():
    return render_template("sweater.html")


@app.route("/shoes")
def shoes():
    return render_template("shoes.html")


@app.route("/top")
def top():
    return render_template("top.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        #hash password
        hash = generate_password_hash(password)

        # Ensure email is unique or taken
        emails = db.execute("SELECT email FROM users")
        for dict_email in emails:
            if email == dict_email["email"]:
                return render_template("failure.html", message="Email already exists!")
    
        # Add email to database
        db.execute("INSERT INTO users (email, hash) VALUES(?, ?)", email, hash)

         # Redirect user to home page
        return redirect("/")
        
    else:
        return render_template("signup.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    return render_template("signin.html")

    #return render_template("signin.html")
    #if request.method == "POST":

        #session.clear()
        #email = request.form.get("email")
        #password = request.form.get("password")
        

    #check if email and pw matches the db, id yess send user to home page, if not send them to failure 
       # if not email:
          #  flash("Must provide email!", "warning") 
            #return redirect(url_for('signin'))
        #if not password:
            #flash("Must provide password!", "warning") 

        #rows = db.execute("SELECT * FROM users WHERE id = ?", id)



    #else:
       # return render_template("signin.html")


@app.route("/shop", methods=["GET", "POST"])
def shop():
    return render_template("shop.html")


  
@app.route("/bag")
def bag():

    def usd(value):
        return f"${value:,.2f}"

    #go to session, and check the value of the key"user_id"
    #user_id = session["user_id"]
    #rows = db.execute("SELECT item,amount,price FROM cart WHERE user_id = ?", user_id)

    return render_template("bag.html")  



if __name__ == "__main__":
  app.run()