import os
import smtplib

sender_email = os.environ["SENDER"]
password = os.environ["PASSWORD"]
rec_email = os.environ["RECEIVER"]


# this function sends mail to the specified person
def send_otp(code: str):
    body = "Your code is: " + code

    headers = ["From: " + sender_email,
               "Subject: " + "Your OTP code",
               "To: " + rec_email,
               "MIME-Version: 1.0",
               "Content-Type: text/plain"]
    headers = "\r\n".join(headers)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email, password)
    print("login successful")
    server.sendmail(sender_email, rec_email, headers + "\r\n\r\n" + body)
    print("Email has been sent to", rec_email)
    server.quit()
    return
