from flask_app import app
from flask import render_template, redirect, request, url_for, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import space, user

@app.route("/displayspaces")
def display_spaces():
    spaces = space.Space.get_spaces()
    return render_template("display_spaces.html", spaces=spaces)

@app.route("/userspaces")
def display_user_spaces():
    print(session)
    print("new session")
    data = {"email":session['email']}
    print(session)
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
    return redirect("/displayspaces")

@app.route("/editspace/<id>")
def display_edit_space(id):
    print("displaying edit space")
    current_space = ""
    current_space = (space.Space.get_space(id))
    return render_template("edit_space.html", current_space = current_space)

@app.route("/editspace/editspace/<id>", methods=["POST"])
def edit_space(id):
    print("Editing Space")
    name = request.form['name']
    data = {
            "id":id,
            "name":name
            }
    space.Space.edit_space(data)
    return redirect("/displayspaces")

@app.route("/deletespace/<id>")
def delete_space(id):
    data = {"id":id}
    space.Space.delete_space(data)
    return redirect("/displayspaces")