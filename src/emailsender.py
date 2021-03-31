import smtplib
import os
from email.message import EmailMessage

mail_from = os.getenv("EMAIL_FROM")
mail_to = os.getenv("EMAIL_TO")
mail_pw = os.getenv("EMAIL_PW")


# Sending an e-mail to myself (and some friends) whenever a tweet that meets the criteria is detected
def send_mail(text: str, contains_img: bool):
    msg = EmailMessage()
    msg["From"] = mail_from
    msg["To"] = mail_to
    msg["Subject"] = "New stonks tweet alert!"

    msg.set_content(text)

    if contains_img is True:
        with open(os.path.join(os.getcwd(), "image-tested.jpg"), 'rb') as content_file:
            content = content_file.read()
            msg.add_attachment(content, maintype="application", subtype="jpg", filename="image-tested.jpg")

    smtp_server_name = "smtp.gmail.com"

    server = smtplib.SMTP(smtp_server_name, 587)
    server.starttls()

    server.login(mail_from, mail_pw)
    server.send_message(msg)
    server.close()
