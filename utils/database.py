import sqlite3

# Create or connect database
con = sqlite3.connect("bot.db", check_same_thread=False)
cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    processed INTEGER DEFAULT 0
)
""")
con.commit()


# Add user to database
def add_user(uid: int):
    cur.execute("INSERT OR IGNORE INTO users(user_id) VALUES(?)", (uid,))
    con.commit()


# Increment image processing count
def increment(uid: int):
    cur.execute("UPDATE users SET processed = processed + 1 WHERE user_id=?", (uid,))
    con.commit()


# Total users
def total_users():
    row = cur.execute("SELECT COUNT(*) FROM users").fetchone()
    return row[0]


# Total processed images
def total_processed():
    row = cur.execute("SELECT SUM(processed) FROM users").fetchone()
    return row[0] if row[0] else 0


# Fetch all user IDs (for broadcast)
def all_users():
    return cur.execute("SELECT user_id FROM users").fetchall()
