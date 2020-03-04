import smtplib
from email.mime.text import MIMEText

sender = 'SendersEmail@email.com'

def sendEmail(text, subject, recipientList):
    msg = MIMEText(text)

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ",".join(recipientList)
    
    smtpServer = 'smtp.server' # smtp server info here
    s = smtplib.SMTP(smtpServer)
    s.sendmail(sender, recipientList, msg.as_string())
    s.quit()

if __name__ == "__main__":
    sendEmail('This is the email body!', 'This is the email subject.', 'ReceiversEmail@email.com')