import db

def add_item(title, book_name, stars, review, user_id):
    sql = """INSERT INTO items (title, book_name, stars, review, user_id) VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, book_name, stars, review, user_id])

def get_items():
    sql = """SELECT id, title, book_name FROM items ORDER BY id DESC"""
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.id,
                    items.title,
                    items.book_name,
                    items.stars,
                    items.review,
                    users.id user_id,
                    users.username
            FROM items, users
            WHERE items.user_id = users.id AND
                items.id = ?"""
    result = db.query(sql, [item_id])
    return result[0] if result else None

def update_item(item_id, title, book_name, stars, review):
    sql = """UPDATE items SET title = ?,book_name = ?, stars = ?, review = ?
                WHERE id = ?"""
    db.execute(sql, [title, book_name, stars, review, item_id])

def remove_item(item_id):
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])

def find_items(query):
    sql = """SELECT id, title, book_name
                FROM items
                WHERE review LIKE ? OR book_name LIKE ?
                ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])