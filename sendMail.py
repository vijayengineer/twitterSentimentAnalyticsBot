import smtplib


class SendMail():
    def __init__(self, email, password, to_email):
        self.my_email = email
        self.password = password
        self.to_email = to_email

    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr=self.my_email,
                                to_addrs=self.to_email, msg=f"Subject: Bitcoin statistics!\n\n{message}")
