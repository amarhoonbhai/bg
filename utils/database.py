import sqlite3

con = sqlite3.connect("bot.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    processed INTEGER DEFAULT 0
)
""")
con.commit()

def add_user(user_id: int):
    cur.execute("INSERT OR IGNORE INTO users(user_id) VALUES(?)", (user_id,))
    con.commit()

def increment(user_id: int):
    cur.execute("UPDATE users SET processed = processed + 1 WHERE user_id=?", (user_id,))
    con.commit()

def total_users():
    return cur.execute("SELECT COUNT(*) FROM users").fetchone()[0]

def total_processed():
    return cur.execute("SELECT SUM(processed) FROM users").fetchone()[0] or 0

def all_users():
    return cur.execute("SELECT user_id FROM users").fetchall()
