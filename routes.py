from webbrowser import get
from app import app
from flask import render_template, request, redirect, session
import users
import restaurants
import reviews

@app.route("/")
def index():
    return render_template("index.html", restaurants=restaurants.get_all_restaurants())

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

@app.route("/add_restaurant", methods=["get", "post"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    
    if request.method == "POST":
        name = request.form["name"]
        if restaurants.check(name):
            return render_template("error.html", message=f"{name} on jo olemassa.")
        
        descr = request.form["descr"]
        if not restaurants.add(name, descr):
            return render_template("error.html", message="Ravintolan lisääminen epäonnistui.")
        return redirect("/")

@app.route("/restaurant/<int:id>", methods=["get", "post"])
def get_restaurant_page(id):
    if request.method == "GET":
        info = restaurants.get_restaurant_info(id)
        return render_template("restaurant.html", res_id=id, res_name=info[0], desc=info[1], reviews=reviews.get_all_reviews())

    if request.method == "POST":
        user_id = session["user_id"]
        stars = int(request.form["stars"])
        comment = request.form["comment"]
        print(user_id)
        print(stars)
        print(comment)
        if not reviews.new_review(user_id, stars, comment):
            print("new review virhe")
        
        info = restaurants.get_restaurant_info(id)
        return render_template("restaurant.html", res_id=id, res_name=info[0], desc=info[1], reviews=reviews.get_all_reviews())
