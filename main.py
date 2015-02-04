#!/usr/bin/python
import os, time , smtplib

def sendemail(message):
           #   smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % 'sender_email@email.com'
    header += 'To: %s\n' % 'reciever_email@email.com'
    #header += 'Cc: %s\n' % '[recievers,email,list]'
    header += 'Subject: %s\n\n' % 'Subject , can be replaced by a varialble '
    message = header + message
 
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('username','pwd')
    problems = server.sendmail('sender_mail@gmail.com',['list','of','actual','recipents'], message)
    server.quit()

path_to_watch = "."
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (10)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  if added: 
    print "Added: ", ", ".join (added)
    temp=str(added)
    sendemail(temp)

  
  
  if removed: print "Removed: ", ", ".join (removed)
  before = after
