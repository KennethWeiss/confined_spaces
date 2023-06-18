from flask_app import app
from flask import render_template, redirect, request, url_for, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import space, user, hazard

@app.route("/displayhazards")
def display_hazards():
    if session.get('logged_in') == None:
        return redirect("/")
    hazards = hazard.Hazard.get_hazards()
    print(hazards)
    return render_template("display_hazards.html", hazards=hazards)

@app.route("/createhazard")
def display_create_hazard():
    if session.get('logged_in') == None:
        return redirect("/")
    return render_template("create_hazard.html")

@app.route("/createhazard", methods=["POST"])
def create_hazard():
    if session.get('logged_in') == None:
        return redirect("/")
    data = {
        "name" : request.form['name'],
        "description" : request.form['description']
    }
    hazard.Hazard.create_hazard(data)
    return redirect("/displayhazards")

@app.route("/addhazardtospace", methods=["POST"])
def add_hazard_to_route():
    data = {
            "hazard_id": request.form['hazard_id'],
            "confined_space_id": request.form['space_id']
            }
    hazard.Hazard.add_hazard_to_space(data)
    return redirect("/displayspaces")

@app.route("/deletehazard/<id>")
def delete_hazard(id):
    if session.get('logged_in') == None:
        return redirect("/")
    data = {
            "id" : id
    }
    hazard.Hazard.delete_hazard(data)
    return redirect("/displayhazards")
