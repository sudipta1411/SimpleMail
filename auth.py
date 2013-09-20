#! /usr/bin/env python
import smtplib
import pygtk
pygtk.require('2.0')
import gtk

server_name = 'smtp.gmail.com'
port='587'

class LoginError(Exception):
    pass
def auth(username,password) :
    try:
        server = smtplib.SMTP(server_name + ':' + port)
        server.starttls()
        if username != '' and password != '':
            server.login(username,password)
        else:
            raise LoginError,'User Name or Password is blank'
    except smtplib.SMTPAuthenticationError:
        print 'Can not authenticate user %s' %username
        message = gtk.MessageDialog(type=gtk.MESSAGE_ERROR, buttons=gtk.BUTTONS_OK)
        message.set_markup('Can not authenticate user %s' %username)
        message.run()
