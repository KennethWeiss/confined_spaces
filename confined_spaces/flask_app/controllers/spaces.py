from flask_app import app
from flask import render_template, redirect, request, url_for, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import space

@app.route("/displayspaces")
def display_spaces():
    print("Got here")
    spaces = space.Space.get_spaces()
    return render_template("display_spaces.html", spaces=spaces)

@app.route("/userspaces")
def display_user_spaces():
    spaces = space.Space.get_users_spaces()
    return render_template("user_spaces.html", spaces=spaces)

@app.route("/addspace", methods=["GET"])
def display_space():
    return render_template("create_space.html")

@app.route("/create_space", methods=["POST"])
def add_space():
    data = {
        "name" : request.form["name"]
    }
    space.Space.create_space(data)
    print("after sql")
    return render_template("create_space.html")

@app.route("/editspace")
def display_edit_space():
    return render_template("edit_space.html")

@app.route("/editspace", methods=["POST"])
def edit_space():
    return redirect("/userspaces")