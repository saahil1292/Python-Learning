#!/usr/bin/python2.7

import smtplib

sender = 'saahil1292@gmail.com'
receiver = 'saahil12.coolguy@gmail.com'
pwd = 'hunk6999'

message = '''
From: %s
To: %s
Subject: test mail

Hi,

This is a test mail... DO NOT PAY ATTENTION !!''' % (sender, receiver)

try:
    server = smtplib.SMTP('smtp.gmail.com','587')
    server.ehlo()
    server.starttls()
    server.login(sender,pwd)
    server.sendmail(sender, receiver, message)
    print "Mail Sent Successfully"
    server.quit()
except:
    print "Failed to deliver the Message"

