import smtplib
import os
from email.mime.text import MIMEText

mail_from = os.getenv('EMAIL_FROM')
mail_to = os.getenv('EMAIL_TO')
mail_to2 = os.getenv('EMAIL_TO2')
mail_pw = os.getenv('EMAIL_PW')


# Sending an e-mail to myself (and some friends) whenever a tweet that meets the criteria is detected
def send_mail(text):
    msg = MIMEText(text)
    mailing_list = [mail_to, mail_to2]
    msg['From'] = mail_from
    msg['To'] = ', '.join(mailing_list)
    msg['Subject'] = 'New stonks tweet alert!'

    smtp_server_name = 'smtp.gmail.com'

    server = smtplib.SMTP('{}:{}'.format(smtp_server_name, 587))
    server.starttls()

    server.login(mail_from, mail_pw)
    server.send_message(msg)
    server.close()
