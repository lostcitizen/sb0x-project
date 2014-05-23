"""
WebScanner.py - A simple Web scanner

Author: Levi Nachamni (levi0x0)
Date: 20/05/2014
Version: 0.1
License: GPL 3

Description:
	A Simple Webscanner with TCP/Connect Port scanner, Server banner graber

"""

MODULE_NAME = "Web Scanner"
MODULE_AUTHOR = "Levi Nachmani (levi0x0)"
MODULE_LICENSE = "GPL 3"
MODULE_VERSION = "0.1"
MODULE_DESC = "A Simple Web scanner with TCP/Connect Port scanner, Server banner graber"

import urllib2
import sys
from socket import *
from api.std import *

class sb0xg(object):
	def __init__(self, target, tcpRange):
		self.target = target
		self.tcprange = tcpRange

	def get_info(self):
		self.re = urllib2.urlopen(self.target).info()
		self.ServInf = self.re.get('Server')
		notify("[*]Server: %s" % (self.ServInf))
		self.TimeInf = self.re.get('Date')
		notify("[*]Server Time: %s" % (self.TimeInf))
		self.ask = raw_input("Scan Open Ports (Y/n)")
		if self.ask == "no" or self.ask == "n":
			notify("[*]DONE!")
		elif self.ask == "yes" or self.ask == "y":
			self.t = self.target.replace("http://", "")
			self.t = self.t.replace("https://", "")
			notify("[*]TCP Connect Scanner..")
			notify("[*]Defualt Range 1024")
			for ports in range(1,self.tcprange):
				s = socket(AF_INET, SOCK_STREAM)
				opens = s.connect_ex((self.t, ports))
				if opens == 0:
					warning("OPEN:%d" % (ports))
					s.close()
				else:	
					pass
					s.close()
		else:
			error("[-] Yes or NO!")


def main():
	try:
		target = raw_input("Target:")
		if not "://" in target:
			error("[-] http:// requierd..")
		else:
			notify("[*]Scan target: %s:80......" % (target))
		tcpRange = 1024 #Default 1024
	
		start = sb0xg(target, tcpRange)
		start.get_info()

	except KeyboardInterrupt as e:
		print e.message
	except (urllib2.URLError, gaierror):
		error("[-]Connection Failed!")
	except Exception as e:
		print e.message
