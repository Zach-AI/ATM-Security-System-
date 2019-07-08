import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def sendmail1():
 email_user = ''
 email_password = ''
 email_send = ''

 subject = 'ALERT!!!DANGEROUS TOOL DETECTED!!!'

 msg = MIMEMultipart()
 msg['From'] = email_user
 msg['To'] = email_send
 msg['Subject'] = subject

 body = 'Alert!Dangerous Tool detected inside the ATM.Security measures have been taken.'
 msg.attach(MIMEText(body,'plain'))

 filename='path of the folder you saved the photo'
 attachment  =open(filename,'rb')
 part = MIMEBase('application','octet-stream')
 part.set_payload((attachment).read())
 encoders.encode_base64(part)
 part.add_header('Content-Disposition',"attachment; filename= "+filename)
 msg.attach(part)

 text = msg.as_string()
 server = smtplib.SMTP('smtp.gmail.com',587)
 server.starttls()
 server.login(email_user,email_password)

 server.sendmail(email_user,email_send,text)
 server.quit()
