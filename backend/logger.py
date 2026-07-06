from database import get_connection


def log_success(email, full_name, company, message_id):

    conn = get_connection()

    conn.execute("""
        INSERT INTO campaign_logs
        (recipient_email, full_name, company, status, message_id)

        VALUES (?, ?, ?, ?, ?)
    """, (
        email,
        full_name,
        company,
        "SENT",
        message_id
    ))

    conn.commit()
    conn.close()


def already_sent(email):

    conn = get_connection()

    cursor = conn.execute(
        "SELECT 1 FROM campaign_logs WHERE recipient_email=?",
        (email,)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None