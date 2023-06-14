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

@app.route("/createhazard")
def display_create_hazard():
    return render_template("create_hazard.html")

@app.route("/createhazard", methods=["POST"])
def create_hazard():
    data = {
        "name" : request.form['name'],
        "description" : request.form['description']
    }
    hazard.Hazard.create_hazard(data)
    return redirect("/displayhazards")

@app.route("/deletehazard/<id>")
def delete_hazard(id):
    data = {
            "id" : id
    }
    hazard.Hazard.delete_hazard(data)
    return redirect("/displayhazards")
