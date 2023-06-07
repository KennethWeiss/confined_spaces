from flask_app import app
from flask import render_template, redirect, request, url_for, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import space

@app.route("/userspaces")
def display_user_spaces():
    spaces = space.Space.get_users_spaces()
    return render_template("wall.html", spaces=spaces)

@app.route("/addspace", methods=["POST"])
def add_space():
    return render_template("create_space.html")