from flask_app import app
from flask import render_template, redirect, request, url_for, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import space, user, hazard

@app.route("/displayhazards")
def display_hazards():
    hazards = hazard.Hazard.get_hazards()
    print(hazards)
    return render_template("display_hazards.html", hazards=hazards)