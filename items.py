import db

def add_item(title, book_name, stars, review, user_id):
    sql = """INSERT INTO items (title, book_name, stars, review, user_id) VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, book_name, stars, review, user_id])

def get_items():
    sql = """SELECT id, title, book_name FROM items ORDER BY id DESC"""
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.title, items.book_name, items.stars, items.review, users.username
            FROM items, users
            WHERE items.user_id = users.id AND
                items.id = ?"""
    return db.query(sql, [item_id])[0]