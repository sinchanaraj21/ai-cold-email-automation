from config import SENDER_EMAIL
from excel_reader import load_hr_data
from email_generator import generate_email
from gmail_service import authenticate
from sender import send_email
from logger import log_success, already_sent

# Authenticate
service = authenticate()

# Load HR data
df = load_hr_data()

# First HR
hr = df.iloc[0]

# IMPORTANT: For testing, still send to yourself
recipient = SENDER_EMAIL

# Check duplicate
if already_sent(recipient):
    print("⚠️ This email has already been logged.")
    exit()

# Generate email
html = generate_email(hr)

# Send
message_id = send_email(
    service=service,
    sender=SENDER_EMAIL,
    recipient=recipient,
    subject="ColdMail Automation Test",
    html_body=html
)

# Log
log_success(
    email=recipient,
    full_name=hr["Full Name"],
    company=hr["Company Name"],
    message_id=message_id
)

print("=" * 60)
print("✅ Email sent and logged successfully!")
print("Message ID:", message_id)
print("=" * 60)