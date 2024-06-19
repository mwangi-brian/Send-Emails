#!/usr/bin/python3

import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

SMTP_SERVER = os.environ['SMTP_SERVER']
SMTP_PORT = os.environ['SMTP_PORT']
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
RECIPIENT_EMAIL = os.environ['RECIPIENT_EMAIL']

SUBJECT = 'Email Subject'
BODY = '#rejectFinanceBill!!'

COUNT_FILE = 'email_count.txt'

def send_emails():
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_HOST, EMAIL_PASSWORD)
        message = f"Subject: {SUBJECT}\n\n{BODY}"
        server.sendmail(EMAIL_HOST, RECIPIENT_EMAIL, message)

def email_count():
    if not os.path.exists(COUNT_FILE):
        with open(COUNT_FILE, 'w') as file:
            file.write('0')
    with open(COUNT_FILE, 'r') as file:
        count = int(file.read().strip())
    return count

def increment_count(count):
    with open(COUNT_FILE, 'w') as file:
        file.write(str(count))

def main():
    count = email_count()
    if count < 1000000:
        send_emails()
        increment_count(count + 1)

if __name__ == '__main__':
    main()