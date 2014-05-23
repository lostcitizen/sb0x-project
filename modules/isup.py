"""
isupe.py - Check if host if Up

Author: Levi Nachamni (levi0x0)
Date: 13-04-2014
Version: 0.1
License: GPL 3

Description:
	Check if Host Is up

"""

MODULE_NAME = "IsUp?"
MODULE_AUTHOR = "Levi Nachamni (levi0x0)"
MODULE_LICENSE = "GPL 3"
MODULE_VERSION = "0.1"
MODULE_DESC = "Check if Host Is up/or Down"
from socket import *
import sys
from api.std import *

class isUp(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def test_host(self):
        try:
            self.s = socket(AF_INET, SOCK_STREAM) #open tcp/IPv4 socket
            self.s.connect((self.host, self.port))
        except error:
             print("Host: %s:%d is Down." %(self.host, self.port))
        else:
            print("Host %s:%d is Up." %(self.host, self.port))


def main():
    host = raw_input("Host IP:")
    port = int(raw_input("Port: (80):")) or 80
    start = isUp(host, port)
    start.test_host()
