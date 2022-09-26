from app import app
from flask import render_template, request, redirect

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    else:
        username = request.form["username"]
        password = request.form["password"]
        return redirect("/logintest")

@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    else:
        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]
        return redirect("/logintest")

@app.route("/logintest", methods=["post"])
def user():
    return render_template("logintest.html", name=request.form["username"])
