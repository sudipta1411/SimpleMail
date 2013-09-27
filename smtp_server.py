#!/usr/bin/env python

class Server:
    smtp_server = None

    @classmethod
    def set(cls,server):
        cls.smtp_server = server

    @classmethod
    def get(cls):
        return cls.smtp_server