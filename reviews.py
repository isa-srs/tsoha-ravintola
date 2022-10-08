from db import db

def get_all_reviews():
    sql = "SELECT username, title, stars, comment FROM reviews ORDER BY id DESC"
    return db.session.execute(sql).fetchall()

def new_review(username, title, stars, comment):
    try:
        sql = "INSERT INTO reviews (username, title, stars, comment) VALUES (:username, :title, :stars, :comment)"
        db.session.execute(sql, {"username":username, "title":title, "stars":stars, "comment":comment})
        db.session.commit()
    except:
        return False
