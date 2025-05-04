import db

def get_all_classes():
    sql = "SELECT category, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for category, value in result:
        classes[category] = []
    for category, value in result:
        classes[category].append(value)

    return classes

def add_item(title, book_name, stars, review, user_id, classes):
    sql = """INSERT INTO items (title, book_name, stars, review, user_id) VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, book_name, stars, review, user_id])

    item_id = db.last_insert_id()

    sql = "INSERT INTO item_classes (item_id, category, value) VALUES (?, ?, ?)"
    for category, value in classes:
        db.execute(sql, [item_id, category, value])

def add_comment(item_id, user_id, comment):
    sql = """INSERT INTO comments (item_id, user_id, comment) VALUES (?, ?, ?)"""
    db.execute(sql, [item_id, user_id, comment])

def remove_comment(item_id, comment_id):
    sql = "DELETE FROM comments WHERE id = ? AND item_id = ?"
    db.execute(sql, [comment_id, item_id])

def get_comments(item_id):
    sql = """SELECT comments.id, comments.comment, users.id user_id, users.username
            FROM comments, users
            WHERE comments.item_id = ? AND comments.user_id = users.id
            ORDER BY comments.id DESC"""
    return db.query(sql, [item_id])

def get_class(item_id):
    sql = "SELECT category, value FROM item_classes WHERE item_id = ?"
    return db.query(sql, [item_id])

def get_items():
    sql = """SELECT items.id, items.title, items.book_name, items.stars, users.id user_id, users.username,
                COUNT(comments.id) comment_count
            FROM items JOIN users ON items.user_id = users.id
                        LEFT JOIN comments ON items.id = comments.item_id
            GROUP BY items.id
            ORDER BY items.id DESC"""
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

def update_item(item_id, title, book_name, stars, review, classes):
    sql = """UPDATE items SET title = ?,book_name = ?, stars = ?, review = ?
                WHERE id = ?"""
    db.execute(sql, [title, book_name, stars, review, item_id])

    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])

    sql = "INSERT INTO item_classes (item_id, category, value) VALUES (?, ?, ?)"
    for category, value in classes:
        db.execute(sql, [item_id, category, value])

def remove_item(item_id):
    sql = "DELETE FROM comments WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])

def find_items(query):
    sql = """SELECT id, title, book_name, stars
                FROM items
                WHERE review LIKE ? OR book_name LIKE ?
                ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])