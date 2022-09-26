import os
from db import db
from flask import session
from werkzeug.security import generate_password_hash

def register(username, password, role):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password, role) VALUES (:name, :password, :role)"
        db.session.execute(sql, {"name":username, "password":hash_value, "role":role})
        db.session.commit()
    except:
        return False
    return True
