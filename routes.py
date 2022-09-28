from app import app
from flask import render_template, request, redirect, session
import users

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not users.login(username, password):
            return render_template("error.html", message="Väärä käyttäjänimi tai salasana")
        session["username"] = username
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 4 or len(username) > 15:
            return render_template("error.html", message="Käyttäjänimen tulee olla 4-15 merkkiä pitkä.")
        
        password = request.form["password"]
        if len(password) < 6:
            return render_template("error.html", message="Salasana liian lyhyt. Salasanassa tulee olla vähintään 6 merkkiä.")
        
        role = request.form["role"]
        if not users.register(username, password, role):
            return render_template("error.html", message="Rekisteröinti epäonnistui.")
        return redirect("/")
