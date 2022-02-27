import re
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jsonVal import *


def start():
    email_address = input("enter email address:")
    check_val(email_address)


def check_val(email_address):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email_address)):
        send_email(email_address)
    else:
        print("The email address isn't valid")
        start()


def get_sub():
    subject = input("enter email subject")
    if (subject == ""):
        print("subject is empty")
        get_sub()
    else:
        return subject


def send_email(email_address):
    sender_email = 'devgcx@gmail.com'
    receiver_email = email_address
    password = 'HelloWorld8@.!a[]hd'

    message = MIMEMultipart("alternative")

    subject = get_sub()
    content = input("enter email content")

    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    text = MIMEText(content, "plain")
    message.attach(text)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
        print("an email was successfully sent to "+receiver_email+", with subject "+subject+" and body "+content)
    except smtplib.SMTPException:
        print ("Error: unable to send email")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()

