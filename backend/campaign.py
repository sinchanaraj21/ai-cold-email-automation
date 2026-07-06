import random
import time

from config import SENDER_EMAIL
from excel_reader import load_hr_data
from email_generator import generate_email
from gmail_service import authenticate
from sender import send_email
from logger import log_success, already_sent
from subject_generator import generate_subject

# -----------------------------
# Configuration
# -----------------------------
DRY_RUN = False          # True = Preview only, False = Send emails
DAILY_LIMIT = 50         # Keep low while testing

# -----------------------------
# Initialize
# -----------------------------
service = authenticate()
df = load_hr_data()

sent_today = 0

# -----------------------------
# Campaign Loop
# -----------------------------
for _, hr in df.iterrows():

    if sent_today >= DAILY_LIMIT:
        print("\n✅ Daily limit reached.")
        break

    recipient = hr["Email"]

    if already_sent(recipient):
        print(f"⏭️ Skipping (already sent): {recipient}")
        continue

    html = generate_email(hr)
    subject = generate_subject(hr["Company Name"])

    print("\n" + "=" * 60)
    print(f"Recipient : {recipient}")
    print(f"Name      : {hr['Full Name']}")
    print(f"Company   : {hr['Company Name']}")
    print(f"Title     : {hr['Title']}")
    print(f"Subject   : {subject}")
    print("=" * 60)

    # Preview only
    if DRY_RUN:
        print("🟡 DRY RUN - Email NOT sent.")
        sent_today += 1
        continue

    # Auto send

    try:
        message_id = send_email(
            service=service,
            sender=SENDER_EMAIL,
            recipient=recipient,
            subject=subject,
            html_body=html
        )

        log_success(
            email=recipient,
            full_name=hr["Full Name"],
            company=hr["Company Name"],
            message_id=message_id
        )

        sent_today += 1

        print(f"[{sent_today}/{DAILY_LIMIT}] ✅ {recipient}")

        delay = random.randint(50, 80)
        print(f"⏳ Waiting {delay} seconds...\n")
        time.sleep(delay)

    except Exception as e:
        print(f"❌ Error sending to {recipient}")
        print(e)

print("\nCampaign Finished.")