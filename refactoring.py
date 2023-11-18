import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:
    def __init__(self, smpt, imap):
        self.msg = MIMEMultipart()
        self.mail = imaplib.IMAP4_SSL(imap)
        self.ms = smtplib.SMTP(smpt, 587)  # identify ourselves to smtp gmail client

    def send_msg(self, login, password, receivers: list, subject, message):
        self.msg["From"] = login
        self.msg["To"] = ", ".join(receivers)
        self.msg["Subject"] = subject
        self.msg.attach(MIMEText(message))

        self.ms.ehlo()      # secure our email with tls encryption
        self.ms.starttls()  # re-identify ourselves as an encrypted connection
        self.ms.ehlo()

        self.ms.login(login, password)
        self.ms.sendmail(login, receivers, self.msg.as_string())

        self.ms.quit()

    def get_mail(self, login, password, header):
        self.mail.login(login, password)
        self.mail.list()
        self.mail.select("inbox")

        res, data = self.mail.uid("search", None, "(HEADER Subject '%s')" % header if header else "ALL")
        assert data[0], "There are no letters with current header"

        res, data = self.mail.uid("fetch", data[0].split()[-1], "(RFC822)")
        email_message = email.message_from_string(data[0][1])

        self.mail.logout()
        return email_message


if __name__ == "__main__":
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    log = "login@gmail.com"
    passw = "qwerty"
    subj = "Subject"
    recipients = ["vasya@email.com", "petya@email.com"]
    msg = "Message"
    head = None

    email = Mail(GMAIL_SMTP, GMAIL_IMAP)

    email.send_msg(log, passw, recipients, subj, msg)
    email.get_mail(log, passw, head)
