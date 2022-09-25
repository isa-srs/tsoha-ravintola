from flask import Flask
from flask import redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # session["username"] = username
    return redirect("/logintest")

@app.route("/login", methods=["GET"])
def login2():
    return render_template("login.html")

@app.route("/logintest", methods=["POST"])
def user():
    return render_template("logintest.html", name=request.form["username"])