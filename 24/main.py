# Day 24/69 sending automatic email using python (smtplib)

import smtplib
from dotenv import load_dotenv #get environment variables from .env file
import os
from email.message import EmailMessage

load_dotenv() # load env data

# email details

sender_email = os.getenv("sender_email")
sender_password = os.getenv("sender_password") # use app password if 2 factor authentication is enabled

recevier_email = "keyurbhatia30@gmail.com"


# create email  msg

msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = recevier_email

msg["Subject"] = "hey there this is a test email for day24/69 python"

msg.set_content("""
    Hi there,
                
    this email is sent automatically using python smtplib module.
    
    no clicking.
    no typing.
                just pure automation.
                Regards,
                Everyday Python
                
                """)# three double use for multi line string

# connect to Gmail smtp

try:
    print("connecting... to gmail smtp server...")

    server = smtplib.SMTP("smtp.gmail.com",587) # smtp server and port number
    server.starttls() # start tls for security

    server.login(sender_email,sender_password)
    print("Login sucsess...!")

    # send email

    server.send_message(msg)
    print("Email sent sucess...!")
    server.quit()

except Exception as e:
    print("something went wrong...!",)
    print(e)

print("End day 24/69 python")