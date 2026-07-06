from gmail_service import authenticate, send_test_email
from config import SENDER_EMAIL

service = authenticate()

send_test_email(
    service,
    SENDER_EMAIL,
    SENDER_EMAIL
)

print("Test email sent successfully!")