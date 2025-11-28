import sqlite3
from config import DB_PATH


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Users DB
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Stats Table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS stats (
            id INTEGER PRIMARY KEY,
            bg INTEGER DEFAULT 0,
            enhance INTEGER DEFAULT 0,
            dp INTEGER DEFAULT 0,
            face INTEGER DEFAULT 0,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def add_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()


def get_all_users():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM users")
    users = [u[0] for u in cur.fetchall()]
    conn.close()
    return users


# ---- STATS FUNCTIONS ---- #

def increment_stat(column: str):
    """column must be: bg / enhance / dp / face"""
    conn = sqli
