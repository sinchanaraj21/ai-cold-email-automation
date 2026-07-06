import base64
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RESUME_PATH = os.path.join(
    BASE_DIR,
    "uploads",
    "Resume.pdf"
)


def send_email(service, sender, recipient, subject, html_body):

    message = MIMEMultipart()

    message["To"] = recipient
    message["From"] = sender
    message["Subject"] = subject

    # HTML body
    message.attach(MIMEText(html_body, "html"))

    # Resume attachment
    with open(RESUME_PATH, "rb") as f:
        attachment = MIMEApplication(f.read(), _subtype="pdf")

    attachment.add_header(
        "Content-Disposition",
        "attachment",
        filename="Sinchana_Raj_Resume.pdf"
    )

    message.attach(attachment)

    raw = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    sent = (
        service.users()
        .messages()
        .send(
            userId="me",
            body={"raw": raw}
        )
        .execute()
    )

    return sent["id"]