import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import serial


def response():
 email_user = ''
 email_password = ''
 email_send = ''
 port = '/dev/ttyACM0'
 ser = serial.Serial(port,9600)

 var= ser.readline()

 l=0
 while l!=1 :
  if (var== '1\r\n'):    
   subject = "ALERT!!! ATM SKIMMING!!!"
   break;
  if (var== '2\r\n'):    
   subject = "ALERT!!! DESTRUCTION OF CAMERA!!!"
   break;
  if (var== '3\r\n'):    
   subject = "ALERT!!! DESTRUCTION OF ATM!!!"
   break;
  if (var== '4\r\n'):    
   subject = "ALERT!!! CAMERA FEED DISRUPTED!!!"
   break;
  if (var== '5\r\n'):    
   subject = "TRANSACTION TAKING TOO LONG"
   break;


 msg = MIMEMultipart()
 msg['From'] = email_user
 msg['To'] = email_send
 msg['Subject'] = subject

 body = ''
 msg.attach(MIMEText(body,'plain'))

 text = msg.as_string()
 server = smtplib.SMTP('smtp.gmail.com',587)
 server.starttls()
 server.login(email_user,email_password)


 server.sendmail(email_user,email_send,text)
 server.quit()
