#! /usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

import auth

class PopUp:
    def delete_event(self, widget, event, data=None):
        #gtk.main_quit()
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        """
         A simple pop-up dialog box to prompt user to input
        name and password
        """
        #self.smtp_server = smtp_server
        #self.smtp_server = self.smtp_server_list[0]
        self.popUpWindow = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.popUpWindow.set_border_width(40)
        self.popUpWindow.set_resizable(False)
        self.popUpWindow.set_title('Simple Mail')
        self.popUpWindow.set_icon(gtk.gdk.pixbuf_new_from_file('mail.jpg'))
        color = gtk.gdk.color_parse('#C0C0C0')
        self.popUpWindow.modify_bg(gtk.STATE_NORMAL, color)

        self.popUpWindow.connect("delete_event", self.delete_event)
        self.popUpWindow.connect("destroy", self.destroy)

        self.username_label = gtk.Label('User Name:  ')
        self.username_label.set_alignment(0,0)
        self.username_entry = gtk.Entry()
        #self.username_entry.set_alignment(0.5)
        self.username = None

        self.password_label = gtk.Label('Password:    ')
        self.password_label.set_alignment(0,0)
        self.password_entry = gtk.Entry()
        #self.password_entry.set_alignment(0.5)
        self.password_entry.set_visibility(False) # for password
        self.password = None

        self.password_remember = gtk.CheckButton('Remember Password')
        self.password_remember_bool = False
        self.password_remember.connect('toggled',self.remember_button_toggled,None)

        self.continue_button = gtk.Button('Continue')
        self.continue_button.connect('clicked',self.continue_button_clicked,None)
        self.continue_button.connect_object('clicked',gtk.Widget.destroy,self.popUpWindow)
        #self.continue_button.connect('clicked',gtk.main_quit,None)

        self.vbox_pack = gtk.VBox()
        self.popUpWindow.add(self.vbox_pack)

        #packing username
        self.hbox_pack_username = gtk.HBox()
        self.hbox_pack_username.pack_start(self.username_label)
        self.hbox_pack_username.pack_start(self.username_entry)
        self.username_label.show()
        self.username_entry.show()

        self.vbox_pack.pack_start(self.hbox_pack_username)
        self.hbox_pack_username.show()

        #packing password
        self.hbox_pack_password = gtk.HBox()
        self.hbox_pack_password.pack_start(self.password_label)
        self.hbox_pack_password.pack_start(self.password_entry)
        self.password_label.show()
        self.password_entry.show()

        self.vbox_pack.pack_start(self.hbox_pack_password)
        self.hbox_pack_password.show()

        self.vbox_pack.pack_start(self.password_remember)
        self.password_remember.show()
        self.vbox_pack.pack_start(self.continue_button)
        self.continue_button.show()
        self.vbox_pack.show()

        self.popUpWindow.show()

    def remember_button_toggled(self,widget,Data=None):
        state = widget.get_active()
        if state == 1:
            self.password_remember_bool = True
        else:
            self.password_remember_bool = False
        #print self.password_remember_bool

    def continue_button_clicked(self,widget,data=None):
        self.username = self.username_entry.get_text()
        #print 'User Name : %s' %self.username
        self.password = self.password_entry.get_text()
        #print 'Password : %s' %self.password
        auth.auth(self.username,self.password)
        #if self.smtp_server is not None:
        #    print 'Successfully logged in'
        #else:
        #    print 'unsuccessful attempt'

    def main(self):
        gtk.main()

if __name__ == '__main__':
    #smtp_server = None
    pop = PopUp()
    #print smtp_server
    pop.main()
