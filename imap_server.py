#! /usr/bin/env python

class Server:
    imap_server = None
    @classmethod
    def set(cls,server):
        cls.imap_server = server

    @classmethod
    def get(cls):
        return cls.imap_server
