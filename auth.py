#! /usr/bin/env python
import smtplib
import imaplib
import pygtk
pygtk.require('2.0')
import gtk

import smtp_server
import imap_server

smtp_server_name = 'smtp.gmail.com'
smtp_port='587'

imap_server_name = 'imap.gmail.com'
imap_port = '993'

class LoginError(Exception):
    pass

def auth(username,password) :
    try:
        server = smtplib.SMTP(smtp_server_name + ':' + smtp_port)
        smtp_server.Server.set(server)
        server.starttls()
        if username != '' and password != '':
            server.login(username,password)
            #print "Logged in"
            #print smtp_server
        else:
            raise LoginError,'User Name or Password is blank'
    except smtplib.SMTPAuthenticationError:
        print 'Can not authenticate user %s' %username
        #smtp_server = None
        message = gtk.MessageDialog(type=gtk.MESSAGE_ERROR, buttons=gtk.BUTTONS_OK)
        message.set_markup('Can not authenticate user %s' %username)
        message.run()