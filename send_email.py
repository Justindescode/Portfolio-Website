import smtplib, ssl
from decouple import config


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = config('username', default='')
    password = config('password', default='')
    receiver = "justinsmall1171@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


