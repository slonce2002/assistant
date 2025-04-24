# skills/emailer.py

import smtplib
from email.mime.text import MIMEText
from config import EMAIL_ADDRESS, EMAIL_PASSWORD

def handle(text: str) -> str:
    """
    Sends an email via SMTP. Prompts entirely via text input.
    """
    try:
        # 1) Recipient
        to_addr = input("Recipient email address: ").strip()
        if not to_addr:
            return "Canceled: no recipient provided."

        # 2) Subject
        subj = input("Email subject: ").strip()
        if not subj:
            return "Canceled: no subject provided."

        # 3) Body (multi-line)
        print("Enter your message. End with an empty line:")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        body = "\n".join(lines)
        if not body:
            return "Canceled: no message body provided."

        # 4) Build and send
        msg = MIMEText(body)
        msg["Subject"] = subj
        msg["From"]    = EMAIL_ADDRESS
        msg["To"]      = to_addr

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        return f"✔️ Email successfully sent to {to_addr}."
    except Exception as e:
        return f"❌ Failed to send email: {e}"

