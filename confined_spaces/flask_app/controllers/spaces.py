from flask_app import app
from flask import render_template, redirect, request, url_for, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import space, user

@app.route("/displayspaces")
def display_spaces():
    if session.get('logged_in') == True:
        spaces = space.Space.get_spaces()
        return render_template("display_spaces.html", spaces=spaces)
    else:
        return redirect("/")


@app.route("/userspaces")
def display_user_spaces():
    if session.get('logged_in') == None:
        return redirect("/")
    print(session)
    print("new session")
    data = {"email":session['email'], "id":session['id']}
    print(session)
    spaces = space.Space.get_users_spaces(data)
    return render_template("user_spaces.html", spaces=spaces)

@app.route("/addspace", methods=["GET"])
def display_space():
    if session.get('logged_in') == None:
        return redirect("/")
    return render_template("create_space.html")

@app.route("/create_space", methods=["POST"])
def add_space():
    if session.get('logged_in') == None:
        return redirect("/")
    data = {
        "name" : request.form["name"]
    }
    space.Space.create_space(data)
    print("after sql")
    return redirect("/displayspaces")

@app.route("/editspace/<id>")
def display_edit_space(id):
    if session.get('logged_in') == None:
        return redirect("/")
    print("displaying edit space")
    current_space = ""
    current_space = (space.Space.get_space(id))
    return render_template("edit_space.html", current_space = current_space)

@app.route("/editspace/editspace/<id>", methods=["POST"])
def edit_space(id):
    if session.get('logged_in') == None:
        return redirect("/")
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
    if session.get('logged_in') == None:
        return redirect("/")
    data = {"id":id}
    space.Space.delete_space(data)
    return redirect("/displayspaces")

@app.route("/deletespacefromuser/<id>")
def delete_space_from_user(id):
    if session.get('logged_in') == None:
        return redirect("/")
    data = {
            "id":session['id'],
            "space_id":id
            }
    space.Space.delete_space_from_user(data)
    return redirect("/userspaces")

@app.route("/addspacetouser/<space_id>")
def add_space_to_user(space_id):
    if session.get('logged_in') == None:
        return redirect("/")
    print(session)
    data = {
            'space_id':space_id,
            'user_id':session['id']
            }
    space.Space.add_space_to_user(data)
    print(session)
    return redirect("/userspaces")