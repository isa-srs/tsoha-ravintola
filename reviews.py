from db import db

def get_all_reviews():
    sql = "SELECT u.username, r.stars, r.comment FROM users as u, reviews as r WHERE u.id = r.user_id ORDER BY r.id DESC"
    return db.session.execute(sql).fetchall()

def new_review(user_id, stars, comment):
    try:
        sql = "INSERT INTO reviews (user_id, stars, comment) VALUES (:user_id, :stars, :comment)"
        db.session.execute(sql, {"user_id":user_id, "stars":stars, "comment":comment})
        db.session.commit()
    except:
        return False
