from db import db

def get_all_reviews(restaurant_id):
    sql = "SELECT u.username, u.id as user_id, r.stars, r.comment, r.id as review_id FROM users as u, reviews as r WHERE u.id = r.user_id AND r.restaurant_id=:restaurant_id ORDER BY r.id DESC"
    result = db.session.execute(sql, {"restaurant_id":restaurant_id})
    return result.fetchall()

def new_review(user_id, restaurant_id, stars, comment):
    try:
        sql = "INSERT INTO reviews (user_id, restaurant_id, stars, comment) VALUES (:user_id, :restaurant_id, :stars, :comment)"
        db.session.execute(sql, {"user_id":user_id, "restaurant_id":restaurant_id, "stars":stars, "comment":comment})
        db.session.commit()
    except:
        return False

def delete_review(review_id):
    sql = "DELETE from reviews WHERE id=:review_id"
    db.session.execute(sql, {"review_id":review_id})
    db.session.commit()
