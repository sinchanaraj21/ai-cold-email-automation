import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(BASE_DIR, "campaign.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_database():
    conn = get_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS campaign_logs (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        recipient_email TEXT UNIQUE,

        full_name TEXT,

        company TEXT,

        status TEXT,

        message_id TEXT,

        sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        error_message TEXT

    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database created successfully.")