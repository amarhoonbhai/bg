import sqlite3
from config import DB_PATH


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Stats table
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


# -------- Stats System -------- #

def increment_stat(column: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(f"INSERT INTO stats ({column}) VALUES (1)")
    conn.commit()
    conn.close()


def get_total_stats():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT SUM(bg), SUM(enhance), SUM(dp), SUM(face) FROM stats")
    row = cur.fetchone()
    conn.close()

    return {
        "bg": row[0] or 0,
        "enhance": row[1] or 0,
        "dp": row[2] or 0,
        "face": row[3] or 0
    }


def get_last_24h_stats():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        SELECT SUM(bg), SUM(enhance), SUM(dp), SUM(face)
        FROM stats
        WHERE timestamp >= datetime('now', '-1 day')
    """)

    row = cur.fetchone()
    conn.close()

    return {
        "bg": row[0] or 0,
        "enhance": row[1] or 0,
        "dp": row[2] or 0,
        "face": row[3] or 0
    }
