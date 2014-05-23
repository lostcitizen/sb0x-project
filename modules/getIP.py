"""
getIP.py - get ip module

Author: Levi Nachamni (levi0x0)
Date: 20/05/2014
Version: 0.1
License: GPL 3

Description:
	print out your Local ip and remote ip 

"""
from os import system
from socket import *
import urllib
import re
from api.std import *

MODULE_NAME = "getIP"
MODULE_AUTOHR = "Levi Nachamni (levi0x0)"
MODULE_LICENSE = "GPL 3"
MODULE_VERSION = "0.1"
MODULE_DESC = "print out Your local IP and your Remote IP"

class get_ip(object):
	def get_local_ip(self):
		s = socket(AF_INET, SOCK_STREAM)
		s.connect(("google.com", 80))
		lip = s.getsockname()[0]
		return lip


	def get_remote_ip(self):
		f = urllib.urlopen("http://www.canyouseeme.org/") #grab the ip address form this site
		html_doc = f.read()
		f.close()
		m = re.search('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',html_doc)
		ip =  m.group(0)
		return ip

def main():
	try:
		ip = get_ip()
		lip = ip.get_local_ip()
		notify("[+] Local IP: %s" % (lip))
		rip  = ip.get_remote_ip()
		notify("[+] Remote IP: %s" % (rip))
	except:
		error("[-] Socket, Failed..")
