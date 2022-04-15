import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

app.config['SECRET_KEY'] = 'gfhrjrynsrxc'

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

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
                flash("Email is already exist!", "warning")
                return redirect("/signup")

    
        # Add email to database
        db.execute("INSERT INTO users (email, hash) VALUES(?, ?)", email, hash)

         # Redirect user to home page
        return redirect("/")
        
    else:
        return render_template("signup.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        input_email = request.form.get("email")
        password = request.form.get("password")

        #make sure user typed email and password
        if not input_email:
            flash("Must provide email!", "warning")
            return redirect("/signin")
        if not password:
            flash("Must provide password!", "warning")
            return redirect("/signin")
        
        #make sure email and pw matches the database
        emails = db.execute("SELECT email FROM users")

        for email in emails:
            if email["email"] == input_email:
                hash = db.execute(f"SELECT hash FROM users where email = '{input_email}'")[0]["hash"]
                correct_password = check_password_hash(hash,password)
                #if email exists and password matches hash
                if(correct_password):
                    flash("Successfully logged in!")
                    return redirect("/")
                else:
                    flash("Looks like you have entered wrong email or password!", "warning")
                    return redirect("/signin")
                

        #if user logged in, store his email and password in the session to remember him
        session["email"] = email
        session["password"] = password
        
        


    else:
        return render_template("signin.html")
    



@app.route("/shop", methods=["GET", "POST"])
def shop():
    return render_template("shop.html")


  
@app.route("/bag", methods=["GET", "POST"])
def bag():

    # # Ensure cart exists
    # if "bag" not in session:
    #     session["bag"] = []

    print(session)
    # POST
    if request.method == "POST":
        id = request.form.get("id")
        if id:
            session["bag"].append(id)
        return redirect("/bag")
    
    print(session)

    # GET
    items = db.execute("SELECT * FROM items")
    return render_template("bag.html", items=items)


     



if __name__ == "__main__":
  app.run()