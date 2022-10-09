from db import db

def get_all_restaurants():
    sql = "SELECT id, name FROM restaurants ORDER BY name"
    return db.session.execute(sql).fetchall()

def get_restaurant_info(id):
    sql = "SELECT name FROM restaurants WHERE id<=:id"
    return db.session.execute(sql, {"id":id}).fetchone()

def check(name):
    # True jos name-niminen ravintola on jo olemassa
    sql = "SELECT name FROM restaurants WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    rest = result.fetchone()
    if not rest:
        return False

def add_restaurant(owner_id, name, cuisine):
    try:
        sql = "INSERT INTO restaurants (owner_id, name, cuisine) VALUES (:owner_id, :name, :cuisine)"
        db.session.execute(sql, {"owner_id":owner_id, "name":name, "cuisine":cuisine})
        db.session.commit()
    except:
        return False
