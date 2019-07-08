

import datetime
import email
import imaplib
import mailbox
import serial
p=5
def actions() :
 while p!=0:
  serialport="/dev/ttyUSB0"
  serialport="/dev/ttyACM0"

  mail = imaplib.IMAP4_SSL('imap.gmail.com')
  (retcode, capabilities) = mail.login('email ID','password')
  mail.list()
  mail.select('inbox')

  n=0
  (retcode, messages) = mail.search(None, '(UNSEEN)')
  if retcode == 'OK':

   for num in messages[0].split() :
      print ('Processing')
      n=n+1
      typ, data = mail.fetch(num,'(RFC822)')
      for response_part in data:
         if isinstance(response_part, tuple):
             original = email.message_from_string(response_part[1])
             print (original['From'])
             if (original['From'] == "Email ID which is sending the commands"): 
                 
                if (original['Subject'] =="ENGAGE SMOKE"):
                    ser1 = serial.Serial(serialport,9600)
                    ser1.write(b'3') 
                    break;
                if (original['Subject'] =="UNLOCK"):
                    ser1 = serial.Serial(serialport,9600)
                    ser = serial.Serial(serialport,9600)
                    ser1.write(b'4') 
                    ser.write(b'6')
                    break;          
                if (original['Subject'] =="LOCK"):
                    ser1 = serial.Serial(serialport,9600)
                    ser1.write(b'5')
                    break;

                
                if (original['Subject'] =="OFF SMOKE"):
                    ser1 = serial.Serial(serialport,9600)
                    ser1.write(b'0')
                    
              
          
             typ, data = mail.store(num,'+FLAGS','\\Seen')

  print (n)
