#! /usr/bin/env python3

# Send a test email to myself.
#
# References:
#   - Gmail app password https://myaccount.google.com/security
#   - Tutorial https://realpython.com/python-send-email/

import smtplib
import os
import ssl

# SMTP Server info
port = 465  # For non SSL use 587
smtp_server = 'smtp.gmail.com'

# Sender info
sender_email = os.environ['EMAIL_ADDRESS']
password = os.environ['EMAIL_PASSWORD']
receiver_email = sender_email

# Message
message = """\
Subject: Testing Python email

Dear Greg,

I can't believe this works!

Sincerely,

Myself
"""

# Send the message
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)