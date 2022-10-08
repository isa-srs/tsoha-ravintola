from db import db

def get_all_restaurants():
    sql = "SELECT id, name, descr FROM restaurants ORDER BY name"
    return db.session.execute(sql).fetchall()

def check(name):
    # True jos name-niminen ravintola on jo olemassa
    sql = "SELECT name FROM restaurants WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    rest = result.fetchone()
    if not rest:
        return False
    return True

def add(name, descr):
    try:
        sql = "INSERT INTO restaurants (name, descr) VALUES (:name, :descr)"
        db.session.execute(sql, {"name":name, "descr":descr})
        db.session.commit()
    except:
        return False
    return True

def get_restaurant_info(id):
    sql = "SELECT name, descr FROM restaurants WHERE id=:id"
    return db.session.execute(sql, {"id":id}).fetchone()
