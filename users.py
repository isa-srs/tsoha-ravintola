import os
from db import db
from flask import session, abort, request
from werkzeug.security import generate_password_hash, check_password_hash

def login(username, password):
    sql = "SELECT id, username, password, role FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    print(user)
    if not user:
        return False
    if not check_password_hash(user[2], password):
        return False
    session["user_id"] = user.id
    session["username"] = user.username
    session["userrole"] = user.role
    session["csrf_token"] = os.urandom(16).hex()
    return True

def logout():
    del session["user_id"]
    del session["username"]
    del session["userrole"]
    del session["csrf_token"]

def register(username, password, role):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password, role) VALUES (:username, :password, :role)"
        db.session.execute(sql, {"username":username, "password":hash_value, "role":role})
        db.session.commit()
    except:
        return False
    return login(username, password)

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
