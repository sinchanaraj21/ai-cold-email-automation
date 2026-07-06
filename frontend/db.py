import sqlite3
import pandas as pd

DB_PATH = "../campaign.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def get_total_emails():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM campaign_logs
        WHERE status='SENT'
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total

def get_total_companies():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(DISTINCT company)
        FROM campaign_logs
        WHERE status='SENT'
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total
def get_total_recruiters():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(DISTINCT recipient_email)
        FROM campaign_logs
        WHERE status='SENT'
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_success_rate():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM campaign_logs")
    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM campaign_logs
        WHERE status='SENT'
    """)
    sent = cursor.fetchone()[0]

    conn.close()

    if total == 0:
        return 0

    return round((sent / total) * 100, 1)

def get_campaign_history():
    conn = get_connection()

    query = """
    SELECT
        full_name AS Recruiter,
        company AS Company,
        status AS Status,
        sent_at AS "Sent At"
    FROM campaign_logs
    ORDER BY sent_at DESC
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    return df