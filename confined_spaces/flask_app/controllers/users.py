from flask_app import app
from flask import render_template, redirect, request, url_for, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import user

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not user.User.is_valid(request.form):
        return redirect(url_for("index"))
    else:
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password": bcrypt.generate_password_hash(request.form["password"])
        }
        user.User.create(data)
    return render_template("user_spaces.html")

@app.route("/login", methods=["POST"])
def login():
    data = {
        "email": request.form["email"]
    }
    user_from_db = user.User.get_by_email(data)
    session["first_name"] = user_from_db.first_name
    session["last_name"] = user_from_db.last_name
    session["name"] = f"{user_from_db.first_name} {user_from_db.last_name}"
    session["email"] = user_from_db.email
    session["logged_in"] = True

    if not user_from_db:
        flash("Invalid Login", 'login')
        return redirect(url_for("index"))
    if not bcrypt.check_password_hash(user_from_db.password, request.form["password"]):
        flash("Invalid login", 'login')
        return redirect(url_for("index"))
    session['email']=request.form['email']
    session['logged_in'] = True
    return redirect("/userspaces")
    
@app.route("/success")
def success_display():
    if session.get('logged_in') == True:
        return render_template("user_spaces.html")
    return "You are not logged in"

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))